# Contact Form Submit

Batch-submit contact forms using Chrome DevTools MCP browser automation.

## Usage
`/contact-form-submit [prod | test] [auto | human]`

## Arguments

| Arg | Values | Default | Description |
|-----|--------|---------|-------------|
| **environment** | `prod`, `test` | `test` | Which contact dataset to use |
| **mode** | `auto`, `human` | `auto` | Whether agent submits or human reviews first |

## Examples
- `/contact-form-submit test auto` — Run test contacts against localhost fixtures, auto-submit
- `/contact-form-submit test human` — Run test contacts, pause before each submit for human review
- `/contact-form-submit prod auto` — Run production contacts against real external URLs, auto-submit
- `/contact-form-submit prod human` — Run production contacts, pause before each submit for human review
- `/contact-form-submit` — Defaults to `test auto`

---

## Instructions

### 1. Parse args

Parse `$ARGUMENTS` for two positional parameters:

- **First arg** (`prod` | `test`): environment selector
  - `prod` → dataset: `outreach/examples/medicodax-all-contacts.json`
  - `test` → dataset: `outreach/examples/medicodax-test-contacts.json`
  - If missing → default to `test`
- **Second arg** (`auto` | `human`): submission mode
  - `auto` → agent fills and submits forms automatically
  - `human` → agent fills form, takes pre-submit screenshot, then **pauses** for human to review/edit and press submit
  - If missing → default to `auto`

Announce the parsed configuration:
```
Environment: [test | prod]
Dataset: [file path]
Mode: [auto | human]
Contacts: [N entries]
```

### 2. Prerequisites check

#### 2a. Chrome must be running with remote debugging
Verify Chrome is reachable. If not, instruct the operator:
```
Chrome must be running with remote debugging enabled:

"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --remote-debugging-port=9222 \
  --user-data-dir="/tmp/chrome-outreach-test" \
  --no-first-run \
  --no-default-browser-check \
  --window-size=1280,900 &
```

#### 2b. Test environment only: fixture servers must be running
If environment is `test`, verify localhost:8090 is reachable. If not:
```
Test fixture servers must be running:

cd outreach/test-fixtures && ./serve.sh
# HTTP server on :8090, mail backend on :8091
```

#### 2c. SMTP configuration
Verify project root `.env` has SMTP keys: `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASSWORD`, `SMTP_FROM`, `SMTP_USE_TLS`, `SMTP_TO`.

### 3. Load and validate dataset

Read the JSON file selected in step 1. Validate:
- File exists and parses as JSON
- Is a non-empty array
- Each entry has `_meta.contactFormURL`

Report: "Loaded N contacts from [file]"

### 4. Process each contact

Follow the agent instruction docs in `outreach/lib/` for the full workflow. For each contact entry (index `i`, starting at 1):

#### 4a. Navigate and discover form
Follow `outreach/lib/form-discovery.md`:
- `navigate_page` to `_meta.contactFormURL`
- `take_snapshot` to get a11y tree
- Extract form field inventory (UIDs, labels, types)

If navigation fails → log error, continue to next contact.

#### 4b. Map and fill fields
Follow `outreach/lib/field-mapper.md`:
- Extract payload from `contact_form.payload` (production schema) or top-level fields (simple schema)
- Semantically map JSON keys to form element UIDs
- Execute `fill_form` or individual `fill` calls
- For select dropdowns: use display text (e.g., "Partnership"), not option value

Log any unmapped fields.

#### 4c. Handle CAPTCHA (if detected)
Follow `outreach/lib/captcha-handler.md`:
- Detect CAPTCHA from snapshot
- Attempt checkbox click or other solving strategies
- **If unsolvable and mode = `auto`**: skip this contact, log as skipped, continue to next
- **If unsolvable and mode = `human`**: pause and prompt operator to solve it manually ("done" / "skip")

#### 4d. Pre-submit screenshot
```
execute_tool("chrome-devtools.take_screenshot.take_screenshot", {
  "filePath": "outreach/logs/screenshots/YYYYMMDD-NNN-pre-submit.png"
})
```
**Note:** The parameter is `filePath` (NOT `savePath`).

#### 4e. Submit — MODE-DEPENDENT

**If mode = `auto`:**
- Click the submit button UID
- Wait for confirmation
- Take post-submit screenshot

**If mode = `human`:**
- Do NOT click submit
- Take pre-submit screenshot (already done in 4d)
- Display to the operator:
  ```
  ═══════════════════════════════════════════
    HUMAN REVIEW — Entry N of M
  ═══════════════════════════════════════════
    URL: [contactFormURL]
    Organization: [_meta.organization or "N/A"]
    Contact: [contact_person.name or "N/A"]
  ───────────────────────────────────────────
    Form is filled. Screenshot saved.

    → Review the form in the browser
    → Edit any fields if needed
    → Press the Submit button in the browser
    → Then type "done" to continue

    Or type "skip" to skip this contact.
  ═══════════════════════════════════════════
  ```
- Wait for operator response:
  - `done` → take post-submit screenshot, verify confirmation, log as success
  - `skip` → log as skipped, continue to next contact

#### 4f. Post-submit screenshot (auto mode, or after human confirms)
```
execute_tool("chrome-devtools.take_screenshot.take_screenshot", {
  "filePath": "outreach/logs/screenshots/YYYYMMDD-NNN-post-submit.png"
})
```

#### 4g. Verify submission
Take snapshot and check for confirmation text ("thank you", "received", "sent successfully", "we'll be in touch").

#### 4h. Log entry
Append to `outreach/logs/contactForm-submissions-YYYYMMDD.md` following the format in `outreach/lib/batch-runner.md`. Screenshots must be rendered inline:
```markdown
![Pre-submit](screenshots/YYYYMMDD-NNN-pre-submit.png)
![Post-submit](screenshots/YYYYMMDD-NNN-post-submit.png)
```
**No lazy `filename.png` references** — always use `![alt](path)` syntax.

### 5. Batch summary

After all contacts are processed, output:
```
═══════════════════════════════════════════
  OUTREACH BATCH COMPLETE
═══════════════════════════════════════════
  Environment:  [test | prod]
  Mode:         [auto | human]
  Total:        N
  Success:      N
  Failed:       N
  Skipped:      N
  Uncertain:    N
───────────────────────────────────────────
  Log: outreach/logs/contactForm-submissions-YYYYMMDD.md
  Screenshots: outreach/logs/screenshots/
═══════════════════════════════════════════
```

---

## Important Notes

- **`filePath` not `savePath`**: The `take_screenshot` tool's file-save parameter is `filePath`. `savePath` is silently ignored.
- **`fill` for dropdowns**: Use option display text ("Partnership"), not option value ("partnership").
- **`wait_for` text param**: Takes an array: `{"text": ["Thank you"], "timeout": 10000}`
- **Error isolation**: One contact's failure must NOT stop the batch. Wrap each in try/catch logic.
- **Rate limiting**: Wait 3–5 seconds between contacts on the same domain, 1–2 seconds between different domains.
- **Production data**: `medicodax-all-contacts.json` contains real external URLs and real names. Use with care. Never use for automated testing.
- **SMTP**: Forms POST to a mail backend that reads SMTP config from the project root `.env`. Emails are sent to `SMTP_TO` (currently `mike@lsa.dev`).
