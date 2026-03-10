#!/usr/bin/env python3
"""
PASS 5: Download .eml files ONLY for KEEP messages and index them
in SQLite FTS5 for full-text search.

SPAM and NEWSLETTER are NEVER downloaded.
"""

import os
import sys
import re
import time
import email
from email import policy
import msal
import requests
from datetime import datetime
from tqdm import tqdm

from config import (
    TENANT_ID, CLIENT_ID, CLIENT_SECRET,
    SHARED_MAILBOXES, OUTPUT_DIR,
)
from db import get_db

GRAPH_BASE = "https://graph.microsoft.com/v1.0"
SCOPES = ["https://graph.microsoft.com/.default"]


def get_access_token():
    app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=f"https://login.microsoftonline.com/{TENANT_ID}",
        client_credential=CLIENT_SECRET,
    )
    result = app.acquire_token_silent(SCOPES, account=None)
    if not result:
        result = app.acquire_token_for_client(scopes=SCOPES)
    if "access_token" in result:
        return result["access_token"]
    print(f"Auth failed: {result.get('error_description', 'Unknown')}")
    sys.exit(1)


def sanitize_filename(name, max_length=100):
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '_', name)
    name = name.strip('. ')
    return name[:max_length] if name else "no_subject"


def download_eml(token, mailbox_email, graph_id):
    """Download raw MIME content via /$value endpoint."""
    headers = {"Authorization": f"Bearer {token}"}
    url = f"{GRAPH_BASE}/users/{mailbox_email}/messages/{graph_id}/$value"
    resp = requests.get(url, headers=headers)
    if resp.status_code == 429:
        time.sleep(int(resp.headers.get("Retry-After", 30)))
        resp = requests.get(url, headers=headers)
    return resp.content if resp.status_code == 200 else None


def extract_body_text(eml_bytes):
    """Parse .eml and extract plain text body for FTS indexing."""
    try:
        msg = email.message_from_bytes(eml_bytes, policy=policy.default)
        body = msg.get_body(preferencelist=("plain", "html"))
        if body:
            text = body.get_content()
            if "<html" in text.lower():
                text = re.sub(r'<[^>]+>', ' ', text)
                text = re.sub(r'\s+', ' ', text).strip()
            return text[:50000]
    except Exception:
        pass
    return ""


def main():
    print("=" * 60)
    print("PASS 5: Export .eml (KEEP only) + Full-Text Index")
    print(f"Started: {datetime.now().isoformat()}")
    print("=" * 60)

    token = get_access_token()
    print("Authenticated.\n")

    db = get_db()
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # ONLY get KEEP messages
    rows = db.execute("""
        SELECT m.id, m.graph_id, m.subject, m.sender_address,
               m.sender_name, m.received_at,
               mb.email as mailbox_email, mb.display_name as mailbox_name
        FROM messages m
        JOIN mailboxes mb ON mb.id = m.mailbox_id
        WHERE m.action = 'KEEP'
          AND m.exported_at IS NULL
        ORDER BY m.received_at DESC
    """).fetchall()

    print(f"  KEEP messages to export: {len(rows)}")

    # Verify: count non-KEEP to confirm they're excluded
    non_keep = db.execute(
        "SELECT COUNT(*) as c FROM messages WHERE action != 'KEEP' OR action IS NULL"
    ).fetchone()
    print(f"  SPAM/NEWSLETTER excluded: {non_keep['c']}")

    exported = 0
    skipped = 0
    failed = 0

    for row in tqdm(rows, desc="  Downloading"):
        mailbox_dir = os.path.join(
            OUTPUT_DIR, row["mailbox_email"].split("@")[0]
        )
        os.makedirs(mailbox_dir, exist_ok=True)

        date_prefix = (row["received_at"] or "unknown")[:10]
        safe_subject = sanitize_filename(row["subject"] or "no_subject", 80)
        filename = f"{date_prefix}_{safe_subject}_{row['graph_id'][:8]}.eml"
        filepath = os.path.join(mailbox_dir, filename)

        if os.path.exists(filepath):
            db.execute("""
                UPDATE messages SET eml_path = ?, exported_at = ? WHERE id = ?
            """, (filepath, datetime.utcnow().isoformat(), row["id"]))
            db.commit()
            skipped += 1
            continue

        eml_bytes = download_eml(token, row["mailbox_email"], row["graph_id"])
        if eml_bytes:
            with open(filepath, "wb") as f:
                f.write(eml_bytes)

            body_text = extract_body_text(eml_bytes)
            db.execute("""
                UPDATE messages SET eml_path = ?, exported_at = ? WHERE id = ?
            """, (filepath, datetime.utcnow().isoformat(), row["id"]))

            db.execute("""
                INSERT OR REPLACE INTO messages_fts(rowid, subject,
                    sender_address, sender_name, body_text)
                VALUES (?, ?, ?, ?, ?)
            """, (
                row["id"], row["subject"],
                row["sender_address"], row["sender_name"],
                body_text,
            ))

            db.commit()
            exported += 1
        else:
            failed += 1

        time.sleep(0.1)

    print(f"\n{'='*60}")
    print(f"EXPORT COMPLETE")
    print(f"  Exported:        {exported}")
    print(f"  Already existed: {skipped}")
    print(f"  Failed:          {failed}")
    print(f"  Output:          {os.path.abspath(OUTPUT_DIR)}")
    print(f"{'='*60}")
    db.close()


if __name__ == "__main__":
    main()
