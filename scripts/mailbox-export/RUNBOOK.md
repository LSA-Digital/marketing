# Mailbox Export Runbook

Step-by-step phased execution guide. Complete each phase fully before
moving to the next.

---

## Phase 1: Setup (one-time, ~20 minutes)

You need two things: an Azure app registration and a Gemini API key.

### 1A. Register the Azure app

1. Go to https://entra.microsoft.com > App registrations > New registration
2. Name: `Mailbox Export Tool`, Single tenant, no redirect URI
3. Copy the **Application (client) ID** and **Directory (tenant) ID**
4. Go to Certificates & secrets > New client secret > copy the **Value**
5. Go to API permissions > Add permission > Microsoft Graph > Application permissions
6. Add **Mail.Read** and **Mail.ReadWrite**
7. Click **Grant admin consent**

### 1B. Get a Gemini API key

1. Go to https://aistudio.google.com/apikey
2. Create a key > copy it

### 1C. Configure and install

```bash
# Copy the mailbox-export folder to your Mac
cd ~/mailbox-export

# Edit config.py — fill in these 4 values:
#   TENANT_ID, CLIENT_ID, CLIENT_SECRET, GEMINI_API_KEY

# Run setup
chmod +x setup.sh
./setup.sh
source venv/bin/activate
python db.py
```

**Phase 1 is done when:** `setup.sh` completes without errors and
`mailbox_export.db` exists.

---

## Phase 2: Test Run (100 emails per mailbox, ~10 minutes)

This validates the entire pipeline with a small subset before
touching all your email. `TEST_MODE = 100` is already set in config.py.

### 2A. Scan metadata

```bash
python pass1_scan.py
```

**Verify:** You should see ~100 messages per mailbox in the output.

```bash
sqlite3 mailbox_export.db "SELECT mb.display_name, COUNT(*) FROM messages m JOIN mailboxes mb ON mb.id = m.mailbox_id GROUP BY mb.id;"
```

### 2B. Classify with Gemini

Classification uses the **Gemini Batch API** — emails are submitted as a
single batch job to Google, which processes them asynchronously (up to 24h SLA,
often faster). This is 50% cheaper than real-time and avoids rate limits.

```bash
python pass2_classify.py
```

The script will:
1. Chunk unclassified messages into batches of up to 10,000
2. Submit each batch to Google's Batch API
3. Poll for completion (prints status every 30s)
4. Extract results and update the database

**Resume support:** If you Ctrl+C or the script crashes, just re-run it.
Active batch jobs are tracked in `.batch_state.json` and will be resumed.

**Check batch status independently:**
```bash
python batch_status.py
```

**Verify:** Every message has a classification.

```bash
# Should return 0
sqlite3 mailbox_export.db "SELECT COUNT(*) FROM messages WHERE action IS NULL;"

# See the breakdown
sqlite3 mailbox_export.db "SELECT action, COUNT(*) FROM messages GROUP BY action;"

# See tags
sqlite3 mailbox_export.db "SELECT tag, COUNT(*) FROM tags GROUP BY tag ORDER BY COUNT(*) DESC;"

# Spot-check some classifications
sqlite3 mailbox_export.db "SELECT action, sender_address, subject FROM messages ORDER BY RANDOM() LIMIT 20;"
```

### 2C. Apply tags to Outlook (non-destructive)

```bash
python pass3_outlook_sync.py
```

**Verify in Outlook:**
- Open each shared mailbox
- Look for category tags on emails (GOV, RISK, LEAD, etc.)
- Filter by "DELETE" category — these are the spam/newsletters
- Check that DELETE-tagged emails actually are spam

**If any DELETE email should be kept:**

```bash
# Find its ID
sqlite3 mailbox_export.db "SELECT id, sender_address, subject FROM messages WHERE action IN ('SPAM','NEWSLETTER') ORDER BY received_at DESC;"

# Override it
sqlite3 mailbox_export.db "UPDATE messages SET action='KEEP', outlook_synced_at=NULL WHERE id=<THE_ID>;"

# Re-sync
python pass3_outlook_sync.py
```

### 2D. Confirm and delete spam

```bash
python pass4_delete.py
```

It will show you exactly what will be deleted and ask you to type `DELETE`.

**Verify in Outlook:** The DELETE-tagged emails should now be in
Deleted Items. They are recoverable from there.

### 2E. Download KEEP emails only

```bash
python pass5_export.py
```

**Verify:**

```bash
# Count downloaded files
find exported_emails -name "*.eml" | wc -l

# Count KEEP messages in DB (should match)
sqlite3 mailbox_export.db "SELECT COUNT(*) FROM messages WHERE action='KEEP';"

# Confirm no spam was downloaded
sqlite3 mailbox_export.db "SELECT COUNT(*) FROM messages WHERE action IN ('SPAM','NEWSLETTER') AND eml_path IS NOT NULL;"
# ↑ Should return 0

# Test full-text search
sqlite3 mailbox_export.db "SELECT m.subject FROM messages m JOIN messages_fts ON messages_fts.rowid = m.id WHERE messages_fts MATCH 'test' LIMIT 5;"
```

**Phase 2 is done when:** All 5 checks pass:
- Tags visible in Outlook on KEEP emails
- DELETE category visible on spam in Outlook
- Spam moved to Deleted Items after pass4
- .eml files exist only for KEEP messages
- Full-text search works

---

## Phase 3: Production Run (all emails)

### 3A. Reset the database

```bash
rm mailbox_export.db
rm -rf exported_emails
```

### 3B. Switch off test mode

Edit `config.py`:
```python
TEST_MODE = None   # <-- Full production run
```

### 3C. Run the full pipeline

```bash
python db.py
python pass1_scan.py
```

Wait for scan to complete. Check the count:
```bash
sqlite3 mailbox_export.db "SELECT mb.display_name, COUNT(*) FROM messages m JOIN mailboxes mb ON mb.id = m.mailbox_id GROUP BY mb.id;"
```

```bash
python pass2_classify.py
```

This is the longest step. For 20K emails expect 1–24 hours (Google Batch API
SLA). The script submits all emails as batch jobs and polls for completion.

Check progress independently with:
```bash
python batch_status.py
```

Or check the database:
```bash
sqlite3 mailbox_export.db "SELECT action, COUNT(*) FROM messages GROUP BY action;"
```

### 3D. Review and sync

```bash
python pass3_outlook_sync.py
```

Open Outlook and review DELETE-tagged emails across all shared mailboxes.
Take your time here — this is the last chance before deletion.

### 3E. Delete confirmed spam

```bash
python pass4_delete.py
# Type DELETE when ready
```

### 3F. Download all KEEP emails

```bash
python pass5_export.py
```

**Phase 3 is done when:** All KEEP emails are downloaded as .eml files
and indexed in SQLite.

---

## Phase 4: Cleanup

1. Delete the client secret in Azure portal
2. Delete the app registration if no longer needed
3. Secure `mailbox_export.db` and `exported_emails/` — they contain real email
4. Revoke your Gemini API key if no longer needed

---

## Quick Reference

| What | Command |
|------|---------|
| Activate env | `source venv/bin/activate` |
| Stats overview | `sqlite3 mailbox_export.db "SELECT action, COUNT(*) FROM messages GROUP BY action;"` |
| Tag breakdown | `sqlite3 mailbox_export.db "SELECT tag, COUNT(*) FROM tags GROUP BY tag ORDER BY COUNT(*) DESC;"` |
| All RISK emails | `sqlite3 mailbox_export.db "SELECT sender_address, subject FROM messages m JOIN tags t ON t.message_id=m.id WHERE t.tag='RISK';"` |
| Full-text search | `sqlite3 mailbox_export.db "SELECT m.subject FROM messages m JOIN messages_fts ON messages_fts.rowid=m.id WHERE messages_fts MATCH 'keyword';"` |
| Override a classification | `sqlite3 mailbox_export.db "UPDATE messages SET action='KEEP' WHERE id=123;"` |
| Re-classify unknowns | `sqlite3 mailbox_export.db "UPDATE messages SET action=NULL WHERE sender_address LIKE '%@domain.com';"` then `python pass2_classify.py` |
| Check batch job status | `source venv/bin/activate && python batch_status.py` |
| Open DB visually | Download DB Browser for SQLite from https://sqlitebrowser.org |
