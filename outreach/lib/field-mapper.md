# Field Mapper — Agent Instructions

**Purpose:** Semantically map dynamic JSON input fields to discovered form element UIDs using AI reasoning. This is the core intelligence of the outreach system — it handles the fact that every contact form labels its fields differently.

---

## Inputs

1. **Contact data** — a single JSON object (excluding `_meta`) with arbitrary keys and string values
2. **Form field inventory** — the structured output from form-discovery (UIDs, names, types, placeholders)

## Outputs

A **mapping** — an array of `{ uid, value }` pairs ready for `fill_form`, plus any unmapped fields.

---

## Mapping Strategy

### Rule 1: Semantic matching, not exact matching

The JSON keys will NOT match form labels exactly. Use semantic understanding:

| JSON Key | Should Match Form Labels Like |
|----------|-------------------------------|
| `name`, `fullName`, `full_name` | "Name", "Full Name", "Your Name" |
| `firstName`, `first_name`, `first` | "First Name", "First" |
| `lastName`, `last_name`, `last` | "Last Name", "Last", "Surname" |
| `email`, `emailAddress`, `workEmail`, `work_email` | "Email", "Email Address", "Work Email", "Your Email" |
| `phone`, `phoneNumber`, `tel` | "Phone", "Phone Number", "Telephone" |
| `company`, `organization`, `org` | "Company", "Company Name", "Organization" |
| `jobTitle`, `title`, `role` | "Job Title", "Title", "Your Role" |
| `message`, `body`, `yourMessage`, `comments`, `msg` | "Message", "Your Message", "Comments", "How can we help?" |
| `subject`, `topic` | "Subject", "Topic", "Regarding" |
| `interest`, `reason`, `inquiry_type` | "I'm interested in", "Reason for contact", "Interest" |

### Rule 2: Type-aware matching

Match field types for disambiguation:
- If JSON value looks like an email → prefer `type: "email"` fields
- If JSON value is multi-sentence → prefer `textarea` fields
- If JSON key matches a select option value → map to that select's UID with the option value
- If JSON value matches a select option exactly → use it directly

### Rule 3: Handle select/dropdown mapping

For `combobox`/`select` fields:
1. Check if the JSON value matches an option value exactly (e.g., `"partnership"` matches option `"partnership"`)
2. If not exact, check if it matches semantically (e.g., `"demo"` → `"product-demo"`)
3. If no match, skip the field and log a warning

### Rule 4: Handle combined name fields

If the form has a single "Name" field but JSON has `firstName` + `lastName`:
- Concatenate: `"${firstName} ${lastName}"`

If the form has separate First/Last fields but JSON has a single `name`:
- Split on first space: `name.split(" ")` → first = [0], last = [1..]

---

## Procedure

### Step 1: List all JSON data fields

Extract all keys from the contact object, excluding `_meta`:

```
Input: { "_meta": {...}, "firstName": "Sarah", "lastName": "Chen", "workEmail": "sarah@co.com", "message": "Hello" }
Data fields: { "firstName": "Sarah", "lastName": "Chen", "workEmail": "sarah@co.com", "message": "Hello" }
```

### Step 2: Score each JSON field against each form field

For each `(jsonKey, formField)` pair, compute a confidence score based on:
- **Label similarity** (highest weight): Does the JSON key semantically match the form field's `name`?
- **Type compatibility**: Does the value type match the field type?
- **Placeholder hint**: Does the form field's placeholder suggest the same kind of data?

### Step 3: Assign mappings (greedy best-match)

1. Sort all pairs by confidence score (descending)
2. For each pair, if neither the JSON key nor the form UID is already assigned, create the mapping
3. This ensures 1:1 mapping — no field gets filled twice

### Step 4: Build fill_form payload

```json
{
  "mapped": [
    { "uid": "a1b2", "value": "Sarah" },
    { "uid": "c3d4", "value": "Chen" },
    { "uid": "e5f6", "value": "sarah@co.com" },
    { "uid": "g7h8", "value": "Hello" }
  ],
  "unmapped_json_keys": [],
  "unmapped_form_fields": ["phone", "jobTitle"]
}
```

### Step 5: Execute fill

```
execute_tool("chrome-devtools.fill_form.fill_form", {
  "elements": [
    { "uid": "a1b2", "value": "Sarah" },
    { "uid": "c3d4", "value": "Chen" },
    { "uid": "e5f6", "value": "sarah@co.com" },
    { "uid": "g7h8", "value": "Hello" }
  ]
})
```

---

## Edge Cases

| Scenario | Handling |
|----------|----------|
| More JSON fields than form fields | Fill what maps; log unmapped JSON keys |
| More form fields than JSON fields | Fill what maps; leave unmapped form fields empty (unless required) |
| Required form field with no JSON match | Log warning: `"required_field_unmapped"` |
| JSON value too long for input (maxlength) | Truncate to maxlength if detectable |
| Boolean JSON value for checkbox | Check the checkbox if true, leave unchecked if false |
| Numeric JSON value | Convert to string for text input |

---

## Validation

After `fill_form` completes, take a fresh snapshot to verify:
1. All mapped fields contain the expected values
2. No form validation errors are displayed
3. The submit button is in an interactable state (unless CAPTCHA blocks it)
