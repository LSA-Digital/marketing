# Outreach — AI-Powered Contact Form Automation

**Jira:** [MKT-2](https://lsadigital.atlassian.net/browse/MKT-2)

AI agent workflow that fills and submits contact forms using dynamic JSON input and Chrome DevTools MCP browser automation.

---

## Quick Start

### 1. Start the test fixture server

```bash
./test-fixtures/serve.sh
# Forms available at http://localhost:8090/
```

### 2. Prepare your contact JSON

Create a JSON file following the schema. Each entry has a `_meta` object (workflow control) and dynamic fields (form data):

```json
[
  {
    "_meta": {
      "contactFormURL": "http://localhost:8090/simple-form.html"
    },
    "name": "Alex Rivera",
    "email": "alex@example.com",
    "message": "I'd like to discuss a collaboration."
  }
]
```

See `examples/` for more samples.

### 3. Run the agent workflow

The agent follows the instruction docs in `lib/` using Chrome DevTools MCP tools:

1. **form-discovery.md** — Navigate to URL, snapshot the page, extract form fields
2. **field-mapper.md** — Semantically map JSON keys to form element UIDs
3. **captcha-handler.md** — Detect and attempt CAPTCHA solving
4. **batch-runner.md** — Orchestrate the full batch with logging and screenshots

---

## Directory Structure

```
outreach/
├── README.md                        ← You are here
├── schema/
│   └── contact-input.schema.json    # JSON Schema for input validation
├── examples/
│   ├── simple-contact.json          # Basic: name, email, message
│   ├── multi-field-contact.json     # Complex: 8 fields + select dropdown
│   └── batch-contacts.json          # Mixed-schema batch (all 3 form types)
├── test-fixtures/
│   ├── simple-form.html             # Minimal "Get in Touch" form
│   ├── multi-field-form.html        # Enterprise "Request a Demo" form
│   ├── captcha-form.html            # Form with simulated reCAPTCHA checkbox
│   └── serve.sh                     # Local HTTP server (python3)
├── lib/
│   ├── form-discovery.md            # Agent: navigate + extract form fields
│   ├── field-mapper.md              # Agent: semantic JSON → form mapping
│   ├── captcha-handler.md           # Agent: CAPTCHA detection + solving
│   └── batch-runner.md              # Agent: batch processing + logging
└── logs/                            # Execution logs (gitignored)
    └── .gitkeep
```

## JSON Input Format

The `_meta` object controls workflow behavior. All other fields are dynamic and get semantically mapped to form elements — the JSON keys do NOT need to match form labels exactly.

| `_meta` Field | Required | Description |
|---------------|----------|-------------|
| `contactFormURL` | Yes | URL of the contact form |
| `notes` | No | Operator notes (not submitted) |
| `skipCaptcha` | No | If `true`, skip this entry when CAPTCHA is detected |

Dynamic fields can use any key names. The AI agent maps them semantically:
- `name`, `fullName`, `full_name` → form fields labeled "Name", "Full Name", etc.
- `email`, `workEmail`, `emailAddress` → "Email", "Work Email", "Email Address"
- `message`, `body`, `comments`, `yourMessage` → "Message", "Comments", "Your Message"

## Test Fixtures

Three HTML contact forms simulating real-world variation:

| Fixture | Fields | CAPTCHA | Simulates |
|---------|--------|---------|-----------|
| `simple-form.html` | Name, Email, Message | No | Small-business "Get in Touch" |
| `multi-field-form.html` | 8 fields + dropdown | No | Enterprise "Request a Demo" |
| `captcha-form.html` | 4 fields + reCAPTCHA | Yes (checkbox) | Gated contact form |

## Logs

Execution logs are written to `outreach/logs/`:
- `contactForm-submissions-YYYYMMDD.md` — daily markdown log with per-contact details
- `screenshots/YYYYMMDD-NNN-pre-submit.png` — filled form before submission
- `screenshots/YYYYMMDD-NNN-post-submit.png` — confirmation after submission

## Chrome DevTools MCP Tools Used

| Tool | Purpose |
|------|---------|
| `navigate_page` | Open contact form URL |
| `wait_for` | Wait for page/form to load |
| `take_snapshot` | Get a11y tree with form field UIDs |
| `fill_form` | Fill multiple form elements at once |
| `fill` | Fill a single form element |
| `click` | Click CAPTCHA checkbox or submit button |
| `take_screenshot` | Capture pre/post submission state |
