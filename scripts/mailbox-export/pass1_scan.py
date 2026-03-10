#!/usr/bin/env python3
"""
PASS 1: Scan all shared mailboxes via Graph API.
Downloads lightweight metadata (sender, subject, date, headers) for every message.
Stores everything in SQLite. No email bodies are downloaded — this is fast.
"""

import sys
import time
import msal
import requests
from datetime import datetime
from tqdm import tqdm

from config import (
    TENANT_ID, CLIENT_ID, CLIENT_SECRET,
    SHARED_MAILBOXES, PAGE_SIZE, TEST_MODE,
)
from db import get_db, init_db, get_or_create_mailbox, upsert_message, get_stats

GRAPH_BASE = "https://graph.microsoft.com/v1.0"
SCOPES = ["https://graph.microsoft.com/.default"]

SELECT_FIELDS = ",".join([
    "id", "subject", "receivedDateTime", "from", "sender",
    "toRecipients", "internetMessageHeaders",
    "importance", "isRead", "hasAttachments",
])

MAILING_LIST_HEADERS = {
    "List-Unsubscribe", "List-Id", "List-Post", "List-Archive",
    "X-Mailer", "X-Campaign", "X-Mailchimp-Id", "X-MC-User",
    "X-SG-ID", "X-SFMC-Stack", "X-Mandrill-User", "X-PM-Message-Id",
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


def fetch_all_messages(token, mailbox_email):
    """Fetch metadata for all messages via pagination.
    Respects TEST_MODE — stops after TEST_MODE messages if set."""
    headers = {"Authorization": f"Bearer {token}"}
    fetch_size = min(PAGE_SIZE, TEST_MODE) if TEST_MODE else PAGE_SIZE

    url = (
        f"{GRAPH_BASE}/users/{mailbox_email}/messages"
        f"?$select={SELECT_FIELDS}"
        f"&$orderby=receivedDateTime desc"
        f"&$top={fetch_size}"
    )
    all_messages = []
    page = 1

    while url:
        resp = requests.get(url, headers=headers)
        if resp.status_code == 429:
            wait = int(resp.headers.get("Retry-After", 30))
            print(f"    Throttled. Waiting {wait}s...")
            time.sleep(wait)
            continue
        if resp.status_code != 200:
            print(f"    Error (HTTP {resp.status_code}): {resp.text[:200]}")
            break

        data = resp.json()
        msgs = data.get("value", [])
        all_messages.extend(msgs)
        print(f"    Page {page}: {len(msgs)} messages ({len(all_messages)} total)")

        if TEST_MODE and len(all_messages) >= TEST_MODE:
            all_messages = all_messages[:TEST_MODE]
            print(f"    TEST_MODE: capped at {TEST_MODE} messages")
            break

        url = data.get("@odata.nextLink")
        page += 1

    return all_messages


def extract_metadata(raw):
    """Flatten a Graph API message dict for storage."""
    sender_address = ""
    sender_name = ""
    from_field = raw.get("from") or {}
    if from_field.get("emailAddress"):
        sender_address = from_field["emailAddress"].get("address", "")
        sender_name = from_field["emailAddress"].get("name", "")

    to_list = []
    for r in raw.get("toRecipients") or []:
        if r.get("emailAddress"):
            to_list.append(r["emailAddress"].get("address", ""))

    headers = raw.get("internetMessageHeaders") or []
    found = [h["name"] for h in headers if h.get("name") in MAILING_LIST_HEADERS]

    return {
        "subject": raw.get("subject", ""),
        "sender_address": sender_address,
        "sender_name": sender_name,
        "to_recipients": "; ".join(to_list),
        "received_at": raw.get("receivedDateTime", ""),
        "importance": raw.get("importance", ""),
        "is_read": raw.get("isRead", False),
        "has_attachments": raw.get("hasAttachments", False),
        "has_list_headers": len(found) > 0,
        "list_header_names": found,
        "internet_headers": headers,
    }


def scan_mailbox(db, token, mailbox_cfg):
    email = mailbox_cfg["email"]
    name = mailbox_cfg["name"]
    mailbox_id = get_or_create_mailbox(db, email, name)

    print(f"\n{'='*60}")
    print(f"Scanning: {name} ({email})")
    print(f"{'='*60}")

    raw_messages = fetch_all_messages(token, email)
    print(f"  Total messages: {len(raw_messages)}")

    for raw in tqdm(raw_messages, desc="  Storing"):
        meta = extract_metadata(raw)
        upsert_message(db, mailbox_id, raw["id"], meta)

    db.execute(
        "UPDATE mailboxes SET scanned_at = ?, total_messages = ? WHERE id = ?",
        (datetime.utcnow().isoformat(), len(raw_messages), mailbox_id)
    )
    db.commit()
    return len(raw_messages)


def main():
    print("=" * 60)
    print("PASS 1: Metadata Scan → SQLite")
    if TEST_MODE:
        print(f"*** TEST MODE: {TEST_MODE} emails per mailbox ***")
    print(f"Started: {datetime.now().isoformat()}")
    print("=" * 60)

    init_db()
    token = get_access_token()
    print("Authenticated.\n")

    db = get_db()
    total = 0
    for mb in SHARED_MAILBOXES:
        total += scan_mailbox(db, token, mb)

    print(f"\n{'='*60}")
    print(f"SCAN COMPLETE: {total} messages indexed")
    print(f"\nPer-mailbox breakdown:")
    get_stats(db)
    print(f"\nNext: python pass2_classify.py")
    print(f"{'='*60}")
    db.close()


if __name__ == "__main__":
    main()
