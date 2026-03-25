# CAPTCHA Handler — Agent Instructions

**Purpose:** Detect, classify, and attempt to solve CAPTCHAs on contact forms. Behavior on unsolvable CAPTCHAs depends on submission mode (auto vs human).

---

## Inputs

- **Form field inventory** from form-discovery (specifically the `captcha` field)
- **Current page state** via snapshot and/or screenshot

## Outputs

- `{ "solved": true }` — CAPTCHA was solved, form is ready to submit
- `{ "solved": false, "reason": "human_required" }` — agent cannot solve, needs human
- `{ "solved": false, "reason": "no_captcha" }` — no CAPTCHA detected (proceed to submit)

---

## CAPTCHA Detection

### From a11y snapshot, look for:

1. **Checkbox with CAPTCHA-related label:**
   - Text: "I'm not a robot", "I am not a robot", "Verify you are human"
   - Role: `checkbox` near text containing "reCAPTCHA", "CAPTCHA", "robot"

2. **reCAPTCHA iframe:**
   - Element containing `recaptcha` in name or description
   - Nested frame with CAPTCHA content

3. **hCaptcha elements:**
   - Text: "hCaptcha", "Verify you are human"

4. **Custom CAPTCHA:**
   - Image with text like "Enter the characters"
   - Math problems: "What is 3 + 7?"
   - Question-based: "What color is the sky?"

### From screenshot (if snapshot is insufficient):

```
execute_tool("chrome-devtools.take_screenshot.take_screenshot", {})
```

Visually inspect for CAPTCHA widgets (reCAPTCHA badge, challenge images, verification boxes).

---

## Solving Strategies

### Strategy 1: Checkbox CAPTCHA (reCAPTCHA v2 checkbox)

This is the most common and most solvable type.

**Procedure:**
1. Identify the checkbox UID from the snapshot
2. Click it:
   ```
   execute_tool("chrome-devtools.click.click", {
     "uid": "<captcha-checkbox-uid>"
   })
   ```
3. Wait 2 seconds for response
4. Take a new snapshot to check result:
   - If `aria-checked="true"` → **Solved**
   - If image challenge appeared → proceed to Strategy 2
   - If submit button is now enabled → **Solved**

### Strategy 2: Image Challenge (reCAPTCHA v2 image grid)

**This is difficult for AI. Attempt once, then fall back to human.**

1. Take a screenshot of the challenge
2. Analyze the image:
   - Identify the instruction ("Select all images with traffic lights")
   - Identify the grid cells
3. If confident in the answer:
   - Click the matching grid cells by their UIDs
   - Click "Verify"
   - Check if solved
4. If not confident or verification fails → **Fall back to human**

### Strategy 3: Simple text/math CAPTCHA

1. Read the CAPTCHA question from the snapshot
2. Compute the answer (e.g., "What is 5 + 3?" → "8")
3. Fill the answer field:
   ```
   execute_tool("chrome-devtools.fill.fill", {
     "uid": "<captcha-answer-uid>",
     "value": "8"
   })
   ```

### Strategy 4: Invisible reCAPTCHA (v3)

reCAPTCHA v3 is score-based and has no visible widget. It typically:
- Runs automatically on page load
- Adds a hidden token to the form
- Scores the interaction (bot vs human)

**No direct solving is possible.** The best approach:
1. Interact with the page naturally (scroll, pause between fills)
2. Submit the form normally
3. If submission fails due to low score, log and skip

---

## Unsolvable CAPTCHA — Mode-Dependent Behavior

When the agent cannot solve the CAPTCHA after attempting all applicable strategies:

### Auto Mode (`auto`)

**Skip the entry and move on.** Do not block the batch.

1. Log the entry as skipped:
   ```
   { "status": "skipped", "reason": "captcha_unsolvable_auto_mode" }
   ```
2. Take a debug screenshot:
   ```
   execute_tool("chrome-devtools.take_screenshot.take_screenshot", {
     "filePath": "outreach/logs/screenshots/YYYYMMDD-NNN-debug-captcha.png"
   })
   ```
3. Continue to the next contact in the batch.

### Human Mode (`human`)

**Pause and wait for the human to solve it.**

#### Step 1: Announce the situation

Output to the operator:
```
⚠️  CAPTCHA DETECTED — Human assistance required

URL: https://example.com/contact
Type: reCAPTCHA image challenge
Status: All form fields have been filled. CAPTCHA remains unsolved.

ACTION NEEDED:
1. The form is open in the browser with all fields populated
2. Please solve the CAPTCHA manually in the browser window
3. After solving, type "done" to resume the workflow

Or type "skip" to skip this contact.
```

#### Step 2: Wait for human response

Pause the batch processing loop. Do NOT proceed to the next contact until the human responds.

- `done` → take snapshot to verify CAPTCHA is solved, then proceed to submit
- `skip` → log as skipped, continue to next contact

#### Step 3: Verify and continue

After human says "done":
1. Take a snapshot to verify CAPTCHA is solved
2. If solved → proceed to submit
3. If not solved → re-prompt the human

---

## skipCaptcha Flag

If `_meta.skipCaptcha` is `true` in the contact entry:
- Detect CAPTCHA normally
- If CAPTCHA is present → skip this entry entirely (regardless of mode)
- Log: `{ "status": "skipped", "reason": "captcha_detected_skip_flag" }`
- Continue to next contact in the batch

---

## Timing Considerations

- After clicking a CAPTCHA checkbox, wait at least 2 seconds before checking state
- Between form interactions, add small delays (500ms–1000ms) to appear more human-like
- Do NOT rush through — rapid interactions can trigger stricter CAPTCHA challenges
