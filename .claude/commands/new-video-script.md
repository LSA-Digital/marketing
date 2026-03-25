# New Video Script

Create a new outcome-driven video script package for a marketing, SME, or demo video. Use this command when the goal is to **develop a script from objectives and source material**, not to publish a post.

## Usage
`/new-video-script [slug] [date]`

## Examples
- `/new-video-script thad-rural-health-prioritization`
- `/new-video-script permit-trust-brief 2026-03-24`
- `/new-video-script` (interactive; slug will be generated)

---

## Video Script Creation Checklist

**Every script creation MUST complete ALL items below. Do not end the command until all are done.**

### Required for ALL scripts
- [ ] Script objective and intended outcome clearly defined
- [ ] Target audience and speaker identified
- [ ] Source material collected and reviewed
- [ ] Script folder or target asset location identified
- [ ] Script draft written in markdown
- [ ] Revision pass completed against the intended outcome
- [ ] Open questions, missing assets, and next production steps documented

---

## Instructions

### 1. Parse args
- `slug` is optional. If missing, generate one from the working title or idea in kebab-case.
- `date` is optional. If missing, default to today in `YYYY-MM-DD`.

### 2. Run intake

Minimum required inputs:
- **Working title or idea** (1-2 sentences)
- **Primary objective of the video**
  - educate
  - explain a capability
  - build trust
  - prepare for outreach
  - reinforce a campaign narrative
- **Desired outcome**
  - what should the viewer understand, believe, or do differently after watching?
- **Audience**
  - business | technical | mixed
  - plus the specific audience segment if known (for example: health departments, permit applicants, commerce teams, hospital leaders)
- **Speaker**
  - founder | SME | company page narrator | avatar
- **Format**
  - direct-to-camera
  - narrated demo
  - interview-style
  - voiceover
- **Target runtime**
  - default to `< 1 minute` unless the user specifies otherwise
- **Tone**
  - educational
  - informative
  - trust-building
  - technical
  - non-salesy
- **Artifact or source anchor**
  - one concrete thing the script is grounded in: report, product page, map, dataset, workflow, slide, prior post, transcript, or demo

Apply sensible defaults:
- If the speaker is an SME, default to **educational, informative, credibility-first** language
- If the user does not specify runtime, default to **45-60 seconds**
- If the video is early-funnel, default to **build trust / clarify the problem**, not hard CTA language

### 3. Clarify the outcome before drafting

Before writing the script, identify:
- the **main point** the viewer should remember
- the **misunderstanding or bad pattern** the video should correct
- the **one sentence summary** of what the script needs to accomplish

Examples:
- `Help state health leaders understand why tract-level prioritization is more defensible than county averages.`
- `Help permit requestors understand that community trust improves when benefits are tied to actual local conditions.`
- `Help commerce teams connect health conditions to economic resilience.`

### 4. Collect source material

Gather and review the material that should shape the script:
- existing post drafts
- strategic plan docs
- product pages
- previous scripts or transcripts
- partner or customer materials
- research notes
- screenshots, maps, or visual artifacts that the speaker may reference

For each script, document:
- **What sources were used**
- **Which source is the primary anchor**
- **What claims need to stay evidence-safe**

If source material is missing:
- create a `notes.md` or `README.md` checklist near the script target location
- list what still needs to be gathered before production

### 5. Determine the target file location

Use the most appropriate location based on the workflow:

- **If the script belongs to an existing post package**:
  - place it inside that post's `assets/` folder
  - recommended filename: `heygen-script-<slug>.md`

- **If the script is standalone**:
  - place it in a suitable project script location such as `videos/scripts/`
  - recommended filename: `<slug>.SCRIPT.md`

The command should prefer **co-locating scripts with the asset package they support**.

### 6. Draft the script

Write the script in markdown, optimized for the target format.

#### Default script structure
- **Title**
- **Production Notes**
  - speaker
  - format
  - target runtime
  - tone
  - audience
- **Script**
  - short spoken paragraphs only unless the user explicitly wants scenes
- **Optional On-Screen Text Cues**
  - only if helpful for HeyGen, captions, or editor handoff

#### Writing rules
- Keep paragraphs short enough to speak naturally
- Prefer spoken language over written-essay language
- Remove filler, hype, and jargon
- Avoid sounding salesy unless the user explicitly wants a conversion-oriented video
- Anchor the script in one concrete artifact, workflow, or observed problem
- If the speaker is an SME, lean into experience, pattern recognition, and practical judgment
- If the script cites data or a policy claim, keep wording precise and defensible

### 7. Revise against the intended outcome

After drafting, review the script against the original objective.

Mandatory revision checks:
- **Outcome check**: does the script actually move the viewer toward the stated outcome?
- **Speaker fit**: does it sound like the intended speaker, not generic brand copy?
- **Length check**: is it realistically speakable in the target runtime?
- **Clarity check**: is there one clear takeaway?
- **Tone check**: does it avoid accidental CTA or sales language if the brief is educational?
- **Evidence check**: are claims grounded in the collected source material?

If the script misses the intended outcome, revise it before ending the command.

### 8. Create companion notes when useful

When the workflow would benefit from it, create:
- `notes.md` for open questions, reviewer comments, alternate phrasings, or production flags
- `links.md` for source URLs, reference documents, and related assets

Useful things to capture:
- which lines may need SME review
- where the script may still sound too promotional or too generic
- visual references that should appear on screen
- terms or phrases the speaker would naturally use or avoid

### 9. Confirm results

Output a completion summary showing:
- script file path
- intended speaker
- target audience
- objective / desired outcome
- primary source material used
- any missing assets, open questions, or revision notes

---

## Tone Guidance

### House voice for informational videos
- **Outcome-first**: know what the viewer should leave with before writing the first line
- **Artifact-grounded**: tie the script to something concrete, not abstract claims
- **Short spoken paragraphs**: write for the ear, not for the page
- **Credibility over hype**: prefer experience, evidence, and plain language
- **One main takeaway**: the viewer should remember one thing clearly
- **No accidental pitch**: educational videos should not drift into CTA language unless the brief explicitly calls for it

### When the speaker is an SME
- let the script sound like a person who has seen the pattern many times
- favor lines like `In my experience...`, `What we see over and over is...`, or `The lesson is consistent...` when appropriate
- avoid brand-heavy intros unless the brief requires them

### Default mini-template

```markdown
# HeyGen Script: <title>

## Production Notes
- **Speaker:** <name>
- **Format:** <direct-to-camera | voiceover | narrated demo>
- **Target length:** <45-60 seconds>
- **Tone:** <educational / informative / technical / trust-building>
- **Goal:** <audience and intended outcome>

<Paragraph 1: hook or problem>

<Paragraph 2: what we built / what we observed>

<Paragraph 3: how it works or why it matters>

<Paragraph 4: outcome or lesson>

## On-Screen Text Cues
- <optional>
```

---

## File Location Guidance

```text
If tied to a post package:
posts/YYYY/MM/YYYY-MM-DD_[postid]_slug/
└── assets/
    └── heygen-script-<slug>.md

If standalone:
videos/scripts/
└── <slug>.SCRIPT.md
```
