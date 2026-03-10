#!/usr/bin/env python3
"""
PASS 3: Sync classification results to Outlook as categories.
  - KEEP messages: apply their LLM tags (GOV, RISK, LEAD, etc.)
  - SPAM/NEWSLETTER messages: apply a "DELETE" category

This pass is NON-DESTRUCTIVE. No emails are deleted.
After running, open Outlook and review the DELETE-tagged emails.
When satisfied, run pass4_delete.py to actually remove them.
"""

import sys
import time
import json
import msal
import requests
from datetime import datetime
from tqdm import tqdm

from config import TENANT_ID, CLIENT_ID, CLIENT_SECRET, SHARED_MAILBOXES
from db import get_db, get_stats

GRAPH_BASE = "https://graph.microsoft.com/v1.0"
SCOPES = ["https://graph.microsoft.com/.default"]

OUTLOOK_CATEGORY_MAP = {
    "GOV":       "GOV",
    "RISK":      "RISK",
    "LEAD":      "LEAD",
    "CLIENT":    "CLIENT",
    "FINANCIAL": "FINANCIAL",
    "INTERNAL":  "INTERNAL",
    "HR":        "HR",
    "LEGAL":     "LEGAL",
}


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


def apply_categories(token, mailbox_email, graph_id, categories):
    """Apply Outlook categories to a message via PATCH."""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    url = f"{GRAPH_BASE}/users/{mailbox_email}/messages/{graph_id}"
    body = {"categories": categories}

    resp = requests.patch(url, headers=headers, json=body)
    if resp.status_code == 429:
        time.sleep(int(resp.headers.get("Retry-After", 30)))
        resp = requests.patch(url, headers=headers, json=body)
    return resp.status_code == 200


def main():
    print("=" * 60)
    print("PASS 3: Outlook Tag Sync (non-destructive)")
    print(f"Started: {datetime.now().isoformat()}")
    print("=" * 60)

    token = get_access_token()
    print("Authenticated.\n")

    db = get_db()

    # ── Step 1: Apply LLM tags to KEEP messages ──
    print("Step 1: Tagging KEEP messages with LLM categories...")

    keep_msgs = db.execute("""
        SELECT m.id, m.graph_id, m.subject, mb.email as mailbox_email
        FROM messages m
        JOIN mailboxes mb ON mb.id = m.mailbox_id
        WHERE m.action = 'KEEP'
          AND m.outlook_synced_at IS NULL
    """).fetchall()

    keep_tagged = 0
    for msg in tqdm(keep_msgs, desc="  Tagging KEEP"):
        tag_rows = db.execute(
            "SELECT tag FROM tags WHERE message_id = ?", (msg["id"],)
        ).fetchall()

        categories = [
            OUTLOOK_CATEGORY_MAP[r["tag"]]
            for r in tag_rows
            if r["tag"] in OUTLOOK_CATEGORY_MAP
        ]

        if categories:
            success = apply_categories(
                token, msg["mailbox_email"], msg["graph_id"], categories
            )
            if success:
                db.execute("""
                    UPDATE messages SET
                        outlook_categories = ?,
                        outlook_synced_at = ?
                    WHERE id = ?
                """, (
                    json.dumps(categories),
                    datetime.utcnow().isoformat(),
                    msg["id"]
                ))
                keep_tagged += 1
        else:
            db.execute("""
                UPDATE messages SET outlook_synced_at = ? WHERE id = ?
            """, (datetime.utcnow().isoformat(), msg["id"]))

        db.commit()
        time.sleep(0.1)

    print(f"  KEEP messages tagged: {keep_tagged}")

    # ── Step 2: Apply "DELETE" category to SPAM/NEWSLETTER ──
    print("\nStep 2: Tagging SPAM/NEWSLETTER with DELETE category...")

    delete_msgs = db.execute("""
        SELECT m.id, m.graph_id, m.subject, m.action,
               mb.email as mailbox_email
        FROM messages m
        JOIN mailboxes mb ON mb.id = m.mailbox_id
        WHERE m.action IN ('SPAM', 'NEWSLETTER')
          AND m.outlook_synced_at IS NULL
    """).fetchall()

    delete_tagged = 0
    for msg in tqdm(delete_msgs, desc="  Tagging DELETE"):
        categories = ["DELETE", msg["action"]]

        success = apply_categories(
            token, msg["mailbox_email"], msg["graph_id"], categories
        )
        if success:
            db.execute("""
                UPDATE messages SET
                    outlook_categories = ?,
                    outlook_synced_at = ?
                WHERE id = ?
            """, (
                json.dumps(categories),
                datetime.utcnow().isoformat(),
                msg["id"]
            ))
            delete_tagged += 1

        db.commit()
        time.sleep(0.1)

    print(f"  Spam/newsletter tagged DELETE: {delete_tagged}")

    print(f"\n{'='*60}")
    print(f"TAG SYNC COMPLETE (no emails were deleted)")
    print(f"  KEEP messages tagged:         {keep_tagged}")
    print(f"  SPAM/NEWSLETTER tagged DELETE: {delete_tagged}")
    print(f"")
    print(f"  NEXT: Open Outlook and review DELETE-tagged emails.")
    print(f"  Filter by category 'DELETE' in each shared mailbox.")
    print(f"")
    print(f"  If any DELETE email should be KEPT instead:")
    print(f"    sqlite3 mailbox_export.db")
    print(f"    UPDATE messages SET action='KEEP' WHERE id=<id>;")
    print(f"    Then re-run: python pass3_outlook_sync.py")
    print(f"")
    print(f"  When satisfied: python pass4_delete.py")
    print(f"{'='*60}")
    db.close()


if __name__ == "__main__":
    main()
