# Batch Runner — Agent Instructions

**Purpose:** Process a JSON array of contacts sequentially, filling and submitting each contact form with full logging, screenshots, and error isolation.

---

## Inputs

- **JSON file path** — path to a file matching `contact-input.schema.json`
- **Log directory** — `outreach/logs/` (default)

## Outputs

1. **Per-contact screenshots** saved to `outreach/logs/screenshots/`
2. **Daily markdown submission log** at `outreach/logs/contactForm-submissions-YYYYMMDD.md`
3. **Console summary** at batch completion

---

## Procedure

### Step 1: Load and validate input

Read the JSON file. Verify it's a non-empty array where each entry has `_meta.contactFormURL`.

### Step 2: Initialize log file

Create or append to `outreach/logs/contactForm-submissions-YYYYMMDD.md` with today's date.

Create the screenshots directory:
```
mkdir -p outreach/logs/screenshots
```

**Log file header** (only if creating new file):
```markdown
# Contact Form Submissions — YYYY-MM-DD

| # | URL | Status | Time | Notes |
|---|-----|--------|------|-------|
```

### Step 3: Process each contact

For each entry in the array (index `i`, starting at 1):

#### 3a. Navigate and discover form
Follow `form-discovery.md`:
- Navigate to `_meta.contactFormURL`
- Take snapshot
- Extract form field inventory

If navigation fails → log error, continue to next contact.

#### 3b. Map and fill fields
Follow `field-mapper.md`:
- Map JSON fields to form UIDs
- Execute `fill_form`
- Log any unmapped fields

If fill fails → take debug screenshot, log error, continue to next contact.

#### 3c. Take pre-submission screenshot
After all fields are filled, before any CAPTCHA or submit interaction:

```
execute_tool("chrome-devtools.take_screenshot.take_screenshot", {
  "filePath": "outreach/logs/screenshots/YYYYMMDD-NNN-pre-submit.png"
})
```

Note: The parameter is `filePath` (not `savePath`). Uses absolute path or path relative to CWD.

#### 3d. Handle CAPTCHA (if detected)
Follow `captcha-handler.md`:
- Detect CAPTCHA from snapshot
- Attempt solving
- Fall back to human if needed
- If `_meta.skipCaptcha` is true and CAPTCHA detected → skip entry

#### 3e. Submit the form
Click the submit button identified during form discovery:

```
execute_tool("chrome-devtools.click.click", {
  "uid": "<submit-button-uid>"
})
```

Wait for response (confirmation message, page change, or error).

#### 3f. Take post-submission screenshot

```
execute_tool("chrome-devtools.take_screenshot.take_screenshot", {
  "filePath": "outreach/logs/screenshots/YYYYMMDD-NNN-post-submit.png"
})
```

#### 3g. Verify submission success
Take a snapshot and check for:
- Confirmation text: "thank you", "received", "sent successfully", "we'll be in touch"
- URL change (redirect to thank-you page)
- Form replaced by confirmation message

If none found → mark as `uncertain` (submitted but unverified).

#### 3h. Append to markdown log

Add a detailed entry to the daily log file:

```markdown
---

## Entry N — [Status]

- **URL:** https://example.com/contact
- **Time:** 2026-03-11 14:32:05 EST
- **Status:** success | failed | skipped | uncertain

### Fields Mapped
| JSON Key | Form Label | Value |
|----------|------------|-------|
| name | Name | Alex Rivera |
| email | Email | alex.rivera@lsadigital.com |
| message | Message | Hi, I came across... |

### Unmapped
- JSON keys not mapped: (none)
- Required form fields not filled: (none)

### CAPTCHA
- Detected: no
- Solved: n/a

### Screenshots
- Pre-submit: `screenshots/20260311-001-pre-submit.png`
- Post-submit: `screenshots/20260311-001-post-submit.png`

### Notes
(any errors, warnings, or operator notes)
```

### Step 4: Batch summary

After all contacts are processed, output a console summary:

```
═══════════════════════════════════════════
  OUTREACH BATCH COMPLETE
═══════════════════════════════════════════
  Total:      5
  Success:    3
  Failed:     1
  Skipped:    1
  Uncertain:  0
───────────────────────────────────────────
  Log: outreach/logs/contactForm-submissions-20260311.md
  Screenshots: outreach/logs/screenshots/
═══════════════════════════════════════════
```

Also update the summary table at the top of the markdown log file.

---

## Error Isolation

**Critical rule:** One contact's failure must NOT stop the batch.

- Wrap each contact's processing in try/catch logic
- On failure: log the error, take a debug screenshot, continue to next
- On CAPTCHA human fallback: pause only for that contact, then continue
- On navigation failure: skip the contact, log, continue

---

## Screenshot File Naming

```
YYYYMMDD-NNN-{stage}.png

YYYYMMDD  = date (e.g., 20260311)
NNN       = zero-padded entry number (e.g., 001, 002, 003)
stage     = pre-submit | post-submit | debug-error
```

Examples:
- `20260311-001-pre-submit.png`
- `20260311-001-post-submit.png`
- `20260311-002-debug-error.png`

---

## Rate Limiting

Between contacts (after one submission, before navigating to next):
- Wait 3–5 seconds between different URLs on the same domain
- Wait 1–2 seconds between different domains
- These delays reduce the chance of being flagged as automated traffic
