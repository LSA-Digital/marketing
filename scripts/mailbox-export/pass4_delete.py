#!/usr/bin/env python3
"""
PASS 4: Delete confirmed SPAM/NEWSLETTER emails from Outlook.

ONLY run this after:
  1. Running pass3_outlook_sync.py (which tagged them as DELETE)
  2. Reviewing DELETE-tagged emails in Outlook
  3. Overriding any false positives in SQLite

This is DESTRUCTIVE — deleted emails go to Deleted Items in Outlook.
"""

import sys
import time
import msal
import requests
from datetime import datetime
from tqdm import tqdm

from config import TENANT_ID, CLIENT_ID, CLIENT_SECRET
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


def delete_message(token, mailbox_email, graph_id):
    """Delete a message from Outlook (moves to Deleted Items)."""
    headers = {"Authorization": f"Bearer {token}"}
    url = f"{GRAPH_BASE}/users/{mailbox_email}/messages/{graph_id}"

    resp = requests.delete(url, headers=headers)
    if resp.status_code == 429:
        time.sleep(int(resp.headers.get("Retry-After", 30)))
        resp = requests.delete(url, headers=headers)
    return resp.status_code == 204


def main():
    print("=" * 60)
    print("PASS 4: Confirmed Deletion of SPAM/NEWSLETTER")
    print(f"Started: {datetime.now().isoformat()}")
    print("=" * 60)

    db = get_db()

    stats = db.execute("""
        SELECT m.action, mb.display_name, COUNT(*) as count
        FROM messages m
        JOIN mailboxes mb ON mb.id = m.mailbox_id
        WHERE m.action IN ('SPAM', 'NEWSLETTER')
          AND m.outlook_synced_at IS NOT NULL
          AND m.outlook_deleted_at IS NULL
        GROUP BY m.action, mb.display_name
    """).fetchall()

    total_to_delete = 0
    print("\nEmails to be DELETED from Outlook:")
    for row in stats:
        print(f"  {row['display_name']:20s}  {row['action']:12s}  {row['count']:5d}")
        total_to_delete += row["count"]

    if total_to_delete == 0:
        print("  Nothing to delete.")
        db.close()
        return

    print(f"\n  TOTAL: {total_to_delete} emails will be moved to Deleted Items")
    print(f"\n  Type 'DELETE' to confirm, anything else to abort: ", end="")
    confirmation = input().strip()

    if confirmation != "DELETE":
        print("  Aborted. No emails were deleted.")
        db.close()
        return

    token = get_access_token()
    print("Authenticated.\n")

    delete_msgs = db.execute("""
        SELECT m.id, m.graph_id, m.action, m.subject,
               mb.email as mailbox_email
        FROM messages m
        JOIN mailboxes mb ON mb.id = m.mailbox_id
        WHERE m.action IN ('SPAM', 'NEWSLETTER')
          AND m.outlook_synced_at IS NOT NULL
          AND m.outlook_deleted_at IS NULL
    """).fetchall()

    deleted = 0
    failed = 0
    for msg in tqdm(delete_msgs, desc="  Deleting"):
        success = delete_message(token, msg["mailbox_email"], msg["graph_id"])
        if success:
            db.execute("""
                UPDATE messages SET outlook_deleted_at = ? WHERE id = ?
            """, (datetime.utcnow().isoformat(), msg["id"]))
            deleted += 1
        else:
            failed += 1
        db.commit()
        time.sleep(0.1)

    print(f"\n{'='*60}")
    print(f"DELETION COMPLETE")
    print(f"  Deleted:  {deleted}")
    print(f"  Failed:   {failed}")
    print(f"\n  Deleted emails are in Outlook's 'Deleted Items' folder.")
    print(f"  They can be recovered from there if needed.")
    print(f"\nNext: python pass5_export.py")
    print(f"{'='*60}")
    db.close()


if __name__ == "__main__":
    main()
