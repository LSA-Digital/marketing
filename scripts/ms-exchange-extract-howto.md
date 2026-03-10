# Extracting Emails from O365 Shared Mailboxes via Microsoft Graph API

A step-by-step guide for bulk-downloading emails from shared Exchange Online mailboxes
to local `.eml` files on macOS, using Python and the Microsoft Graph API.

---

## Overview

**Goal:** Extract all emails from one or more O365 shared mailboxes (e.g.,
`employeearchive@lsadigital.com`, `admin@lsadigital.com`, etc.) and save them as
individual `.eml` files on your Mac for offline processing.

**Approach:** Register an Azure AD (Entra ID) app with application-level mail
permissions, then run a Python script that authenticates via client credentials,
iterates through every message in each shared mailbox using the Graph API, and
downloads the raw MIME content as `.eml` files.

**Why this approach:** Outlook for Mac does not support exporting shared mailboxes
to PST or OLM. The Graph API is the only reliable method for programmatic bulk
extraction from Exchange Online shared mailboxes.

---

## Prerequisites

- macOS with Python 3.9+ installed (check with `python3 --version`)
- Admin access to your Microsoft 365 tenant (Azure portal / Entra ID)
- Exchange Online admin access (for optional access policy scoping)
- The email addresses of every shared mailbox you want to extract

---

## Part 1: Azure AD App Registration

### Step 1: Create the App Registration

1. Go to https://entra.microsoft.com (or https://portal.azure.com > Microsoft Entra ID)
2. Navigate to **App registrations** > **New registration**
3. Fill in:
   - **Name:** `Mailbox Export Tool` (or any descriptive name)
   - **Supported account types:** "Accounts in this organizational directory only" (Single tenant)
   - **Redirect URI:** Leave blank (not needed for client credentials)
4. Click **Register**
5. On the app's overview page, copy and save:
   - **Application (client) ID** — you'll need this
   - **Directory (tenant) ID** — you'll need this

### Step 2: Create a Client Secret

1. In your app registration, go to **Certificates & secrets**
2. Click **New client secret**
3. Set a description (e.g., "mailbox-export") and an expiry (e.g., 6 months)
4. Click **Add**
5. **Immediately copy the secret Value** — it will not be shown again

### Step 3: Grant API Permissions

1. Go to **API permissions** > **Add a permission**
2. Select **Microsoft Graph** > **Application permissions**
3. Search for and add: **`Mail.Read`**
   (This grants read access to mail in all mailboxes. For shared mailboxes via
   application permissions, `Mail.Read` is sufficient — you do NOT need
   `Mail.Read.Shared`, which is a delegated permission.)
4. Click **Grant admin consent for [your org]** (requires Global Admin or
   Privileged Role Admin)
5. Verify the status column shows a green checkmark for the permission

### Step 4 (Recommended): Restrict Access to Specific Mailboxes

By default, `Mail.Read` application permission grants access to ALL mailboxes in
your tenant. To restrict this to only your shared mailboxes:

1. Create a **mail-enabled security group** in Exchange Online containing only the
   shared mailboxes you want to export
2. Open **Exchange Online PowerShell** (or use the Exchange admin center):

```powershell
# Connect to Exchange Online
Connect-ExchangeOnline

# Create the access policy to restrict the app to only the security group
New-ApplicationAccessPolicy `
  -AppId "<your-app-client-id>" `
  -PolicyScopeGroupId "<security-group-email>" `
  -AccessRight RestrictAccess `
  -Description "Restrict mailbox export tool to shared mailboxes only"

# Test that it works
Test-ApplicationAccessPolicy `
  -Identity "employeearchive@lsadigital.com" `
  -AppId "<your-app-client-id>"
# Should return: Granted

Test-ApplicationAccessPolicy `
  -Identity "someother-user@lsadigital.com" `
  -AppId "<your-app-client-id>"
# Should return: Denied
```

---

## Part 2: Local Environment Setup (macOS)

### Step 1: Create a Project Directory

```bash
mkdir ~/mailbox-export
cd ~/mailbox-export
```

### Step 2: Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install msal requests
```

Only two packages are needed:

| Package    | Purpose                                              |
|------------|------------------------------------------------------|
| `msal`     | Microsoft Authentication Library — handles OAuth token acquisition |
| `requests` | HTTP client — makes the Graph API calls              |

### Step 4: Create a Configuration File

Create `config.py`:

```python
TENANT_ID = "your-tenant-id-here"
CLIENT_ID = "your-app-client-id-here"
CLIENT_SECRET = "your-client-secret-here"

# Add all shared mailboxes you want to export
SHARED_MAILBOXES = [
    "employeearchive@lsadigital.com",
    "admin@lsadigital.com",
    "hello@lsadigital.com",
    "info@lsadigital.com",
    "itadmin@lsadigital.com",
    "sales@lsadigital.com",
]

# Where to save the .eml files
OUTPUT_DIR = "./exported_emails"

# Graph API page size (max 1000, default 10)
PAGE_SIZE = 100
```

> **Security note:** Do not commit `config.py` to version control. Add it to
> `.gitignore` if using git. Consider using environment variables or a `.env`
> file for production use.

---

## Part 3: The Export Script

Create `export_mailbox.py`:

```python
#!/usr/bin/env python3
"""
Bulk export emails from O365 shared mailboxes via Microsoft Graph API.
Saves each email as an individual .eml file.
"""

import os
import sys
import time
import re
import msal
import requests
from datetime import datetime

from config import (
    TENANT_ID, CLIENT_ID, CLIENT_SECRET,
    SHARED_MAILBOXES, OUTPUT_DIR, PAGE_SIZE,
)

GRAPH_BASE = "https://graph.microsoft.com/v1.0"
SCOPES = ["https://graph.microsoft.com/.default"]


def get_access_token():
    """Authenticate using client credentials and return an access token."""
    app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=f"https://login.microsoftonline.com/{TENANT_ID}",
        client_credential=CLIENT_SECRET,
    )

    # Try to get a cached token first
    result = app.acquire_token_silent(SCOPES, account=None)
    if not result:
        result = app.acquire_token_for_client(scopes=SCOPES)

    if "access_token" in result:
        return result["access_token"]
    else:
        print(f"Authentication failed: {result.get('error_description', 'Unknown error')}")
        sys.exit(1)


def sanitize_filename(name, max_length=100):
    """Remove or replace characters that are invalid in filenames."""
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', '_', name)
    name = name.strip('. ')
    return name[:max_length] if name else "no_subject"


def list_all_messages(token, mailbox):
    """
    Retrieve metadata for ALL messages in a mailbox using pagination.
    Returns a list of message dicts with id, subject, receivedDateTime.
    """
    headers = {"Authorization": f"Bearer {token}"}
    url = (
        f"{GRAPH_BASE}/users/{mailbox}/messages"
        f"?$select=id,subject,receivedDateTime"
        f"&$orderby=receivedDateTime desc"
        f"&$top={PAGE_SIZE}"
    )

    all_messages = []
    page = 1

    while url:
        response = requests.get(url, headers=headers)

        if response.status_code == 429:
            # Throttled — respect Retry-After header
            retry_after = int(response.headers.get("Retry-After", 30))
            print(f"    Throttled. Waiting {retry_after}s...")
            time.sleep(retry_after)
            continue

        if response.status_code != 200:
            print(f"    Error listing messages (HTTP {response.status_code}): {response.text}")
            break

        data = response.json()
        messages = data.get("value", [])
        all_messages.extend(messages)

        print(f"    Page {page}: fetched {len(messages)} messages ({len(all_messages)} total)")

        # Follow pagination link if present
        url = data.get("@odata.nextLink")
        page += 1

    return all_messages


def download_eml(token, mailbox, message_id):
    """
    Download the raw MIME content (.eml) of a single message.
    Uses the /$value endpoint which returns the RFC 2822 MIME stream.
    """
    headers = {"Authorization": f"Bearer {token}"}
    url = f"{GRAPH_BASE}/users/{mailbox}/messages/{message_id}/$value"

    response = requests.get(url, headers=headers)

    if response.status_code == 429:
        retry_after = int(response.headers.get("Retry-After", 30))
        time.sleep(retry_after)
        response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.content
    else:
        print(f"    Failed to download message {message_id}: HTTP {response.status_code}")
        return None


def export_mailbox(token, mailbox):
    """Export all emails from a single shared mailbox."""
    mailbox_name = mailbox.split("@")[0]
    mailbox_dir = os.path.join(OUTPUT_DIR, mailbox_name)
    os.makedirs(mailbox_dir, exist_ok=True)

    print(f"\n{'='*60}")
    print(f"Exporting: {mailbox}")
    print(f"Output:    {mailbox_dir}")
    print(f"{'='*60}")

    # Step 1: List all messages
    print(f"  Listing all messages...")
    messages = list_all_messages(token, mailbox)
    print(f"  Found {len(messages)} messages total")

    if not messages:
        print("  No messages to export.")
        return 0

    # Step 2: Download each message as .eml
    exported = 0
    skipped = 0
    failed = 0

    for i, msg in enumerate(messages, 1):
        msg_id = msg["id"]
        subject = msg.get("subject", "no_subject") or "no_subject"
        received = msg.get("receivedDateTime", "unknown")

        # Build filename: YYYY-MM-DD_subject_[id-prefix].eml
        date_prefix = received[:10] if received != "unknown" else "unknown"
        safe_subject = sanitize_filename(subject, max_length=80)
        id_suffix = msg_id[:8]
        filename = f"{date_prefix}_{safe_subject}_{id_suffix}.eml"
        filepath = os.path.join(mailbox_dir, filename)

        # Skip if already downloaded (for resumability)
        if os.path.exists(filepath):
            skipped += 1
            continue

        # Download
        eml_content = download_eml(token, mailbox, msg_id)
        if eml_content:
            with open(filepath, "wb") as f:
                f.write(eml_content)
            exported += 1
        else:
            failed += 1

        # Progress indicator
        if i % 50 == 0 or i == len(messages):
            print(f"    Progress: {i}/{len(messages)} "
                  f"(exported: {exported}, skipped: {skipped}, failed: {failed})")

        # Small delay to avoid throttling
        time.sleep(0.1)

    print(f"\n  Done: {exported} exported, {skipped} skipped, {failed} failed")
    return exported


def main():
    print("Microsoft 365 Shared Mailbox Exporter")
    print(f"Started: {datetime.now().isoformat()}")
    print(f"Mailboxes to export: {len(SHARED_MAILBOXES)}")

    # Authenticate
    print("\nAuthenticating...")
    token = get_access_token()
    print("Authentication successful.")

    # Create output directory
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Export each mailbox
    total_exported = 0
    for mailbox in SHARED_MAILBOXES:
        count = export_mailbox(token, mailbox)
        total_exported += count

    print(f"\n{'='*60}")
    print(f"COMPLETE: Exported {total_exported} emails total")
    print(f"Output directory: {os.path.abspath(OUTPUT_DIR)}")
    print(f"Finished: {datetime.now().isoformat()}")


if __name__ == "__main__":
    main()
```

---

## Part 4: Running the Export

### Step 1: Activate Environment and Run

```bash
cd ~/mailbox-export
source venv/bin/activate
python export_mailbox.py
```

### Step 2: Expected Output

```
Microsoft 365 Shared Mailbox Exporter
Started: 2026-03-08T15:30:00
Mailboxes to export: 6

Authenticating...
Authentication successful.

============================================================
Exporting: employeearchive@lsadigital.com
Output:    ./exported_emails/employeearchive
============================================================
  Listing all messages...
    Page 1: fetched 100 messages (100 total)
    Page 2: fetched 100 messages (200 total)
    Page 3: fetched 47 messages (247 total)
  Found 247 messages total
    Progress: 50/247 (exported: 50, skipped: 0, failed: 0)
    ...
```

### Step 3: Output Structure

```
exported_emails/
  employeearchive/
    2026-03-01_Welcome_to_the_team_AAMkADZj.eml
    2026-02-28_Invoice_12345_AANkBBCc.eml
    ...
  admin/
    ...
  hello/
    ...
  info/
    ...
  itadmin/
    ...
  sales/
    ...
```

### Step 4: Resumability

The script skips files that already exist on disk. If the script is interrupted
(network issue, throttling, etc.), just run it again and it will pick up where it
left off.

---

## Part 5: Working with the Exported .eml Files

### Opening .eml Files on macOS

- **Apple Mail:** Double-click any `.eml` file to open it in Mail.app
- **Outlook for Mac:** Drag and drop `.eml` files into an Outlook folder
- **Programmatic parsing:** Use Python's built-in `email` library:

```python
import email
from email import policy

with open("example.eml", "rb") as f:
    msg = email.message_from_binary_file(f, policy=policy.default)

print(f"From:    {msg['from']}")
print(f"To:      {msg['to']}")
print(f"Subject: {msg['subject']}")
print(f"Date:    {msg['date']}")

# Get plain text body
body = msg.get_body(preferencelist=("plain",))
if body:
    print(f"Body:    {body.get_content()}")

# List attachments
for attachment in msg.iter_attachments():
    print(f"Attachment: {attachment.get_filename()} ({attachment.get_content_type()})")
```

### Converting .eml to Other Formats

- **To PDF:** Use `wkhtmltopdf` or a Python library like `weasyprint`
- **To CSV/spreadsheet:** Parse with the `email` library and write to CSV
- **To PST:** Use `readpst` (part of `libpst`, installable via Homebrew:
  `brew install libpst`) — though going .eml to PST is unusual
- **To mbox:** Concatenate .eml files into a single mbox file:

```bash
# Simple concatenation into mbox format
for f in exported_emails/employeearchive/*.eml; do
    echo "From - $(date)"
    cat "$f"
    echo ""
done > employeearchive.mbox
```

---

## Troubleshooting

### Authentication Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `AADSTS7000215` | Invalid client secret | Regenerate the secret in Azure portal |
| `AADSTS700016` | App not found in tenant | Check TENANT_ID and CLIENT_ID in config |
| `AADSTS65001` | No admin consent | Grant admin consent in API permissions |

### API Errors

| HTTP Code | Meaning | Fix |
|-----------|---------|-----|
| 401 | Token expired or invalid | Script auto-handles; if persistent, re-check permissions |
| 403 | Insufficient permissions | Ensure Mail.Read is granted + admin consented. Check application access policy. |
| 404 | Mailbox not found | Verify the shared mailbox email address is correct |
| 429 | Throttled | Script auto-handles with Retry-After. Reduce PAGE_SIZE if frequent. |

### Performance Notes

- Graph API throttling limit: ~10,000 requests per 10 minutes per app
- With the 0.1s delay and 100-message pages, expect ~500 emails/minute
- For a mailbox with 5,000 emails, expect ~10 minutes
- The script is safe to run multiple times (skips existing files)

---

## Security Cleanup

After you're done exporting:

1. **Delete the client secret** in Azure portal (Certificates & secrets > delete)
2. **Delete the app registration** if no longer needed
3. **Remove the application access policy** in Exchange Online:
   ```powershell
   Get-ApplicationAccessPolicy | Where-Object {$_.AppId -eq "<your-app-id>"} | Remove-ApplicationAccessPolicy
   ```
4. **Secure the exported files** — they contain actual email content

---

## Quick Reference: Key URLs

| Resource | URL |
|----------|-----|
| Azure / Entra ID portal | https://entra.microsoft.com |
| App registrations | https://entra.microsoft.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade |
| Exchange admin center | https://admin.exchange.microsoft.com |
| Graph API Explorer (for testing) | https://developer.microsoft.com/en-us/graph/graph-explorer |
| MSAL Python docs | https://learn.microsoft.com/en-us/entra/msal/python/ |
| Graph API mail reference | https://learn.microsoft.com/en-us/graph/api/resources/mail-api-overview |

---

## References

- [Microsoft Graph: Get message MIME content](https://learn.microsoft.com/en-us/graph/api/message-get)
- [Microsoft Graph: Access shared mailbox messages](https://learn.microsoft.com/en-us/graph/outlook-share-messages-folders)
- [MSAL Python on PyPI](https://pypi.org/project/msal/)
- [Downloading .eml from Graph API (Jed Laundry)](https://www.jlaundry.nz/2019/downloading-eml-message-content-from-the-microsoft-graph-api/)
- [Restrict app to specific mailboxes](https://www.2azure.nl/2022/10/02/restrict-azure-app-permissions-to-specific-mailboxes-only/)
- [Graph API pagination](https://learn.microsoft.com/en-us/graph/paging)
