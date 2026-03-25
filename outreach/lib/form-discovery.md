# Form Discovery — Agent Instructions

**Purpose:** Navigate to a contact form URL and extract a structured inventory of all fillable form fields using Chrome DevTools MCP.

---

## Inputs

- `contactFormURL` — the URL to navigate to (from `_meta.contactFormURL` in the JSON input)

## Outputs

A **form field inventory** — a list of objects, each containing:

| Property | Description |
|----------|-------------|
| `uid` | The element's unique ID from the a11y snapshot |
| `role` | The element's ARIA role (e.g., `textbox`, `combobox`, `checkbox`) |
| `name` | The accessible name (usually from the `<label>`) |
| `type` | HTML input type if available (e.g., `text`, `email`, `tel`) |
| `placeholder` | Placeholder text if present |
| `required` | Whether the field is required |
| `options` | For select/combobox: list of available option values |

---

## Procedure

### Step 1: Navigate to the form URL

```
execute_tool("chrome-devtools.navigate_page.navigate_page", {
  "url": "<contactFormURL>"
})
```

### Step 2: Wait for form to load

```
execute_tool("chrome-devtools.wait_for.wait_for", {
  "text": "submit",
  "timeout": 10000
})
```

If `wait_for` times out, fall back to a general wait:
```
execute_tool("chrome-devtools.wait_for.wait_for", {
  "text": "name",
  "timeout": 5000
})
```

### Step 3: Take a11y snapshot

```
execute_tool("chrome-devtools.take_snapshot.take_snapshot", {})
```

This returns the accessibility tree with UIDs for every interactive element.

### Step 4: Parse the snapshot for form fields

From the snapshot output, identify all elements that are fillable:

**Include these roles:**
- `textbox` — text inputs, email inputs, textareas
- `combobox` — select dropdowns
- `checkbox` — checkboxes (including CAPTCHA)
- `radio` — radio buttons
- `spinbutton` — number inputs

**Also identify:**
- The **submit button** — role `button` with text like "Submit", "Send", "Request", "Contact"
- Any **CAPTCHA widget** — look for:
  - Text containing "not a robot", "reCAPTCHA", "CAPTCHA", "verify"
  - Checkbox near CAPTCHA branding
  - iframes with `recaptcha` in the source

**Exclude:**
- Navigation links
- Header/footer elements
- Non-form buttons (e.g., nav toggles)

### Step 5: Return structured inventory

Return the inventory as a JSON array. Example:

```json
{
  "fields": [
    { "uid": "a1b2", "role": "textbox", "name": "Name", "type": "text", "placeholder": "Your full name", "required": true },
    { "uid": "c3d4", "role": "textbox", "name": "Email", "type": "email", "placeholder": "you@example.com", "required": true },
    { "uid": "e5f6", "role": "textbox", "name": "Message", "type": "textarea", "placeholder": "How can we help?", "required": true }
  ],
  "submitButton": { "uid": "g7h8", "text": "Send Message" },
  "captcha": null
}
```

If CAPTCHA is detected:
```json
{
  "captcha": {
    "type": "recaptcha-checkbox",
    "uid": "i9j0",
    "label": "I'm not a robot"
  }
}
```

---

## Error Handling

| Scenario | Action |
|----------|--------|
| Page fails to load (timeout/404) | Return error: `{ "error": "navigation_failed", "url": "..." }` |
| No form fields found in snapshot | Take a screenshot for debugging, return: `{ "error": "no_form_found" }` |
| Multiple forms on page | Use the first form that contains email-like fields |
| Form inside iframe | Note limitation — chrome-devtools snapshot may not penetrate iframes |
