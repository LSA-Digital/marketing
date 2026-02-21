# New Post

Create a new marketing post folder **and draft the post content**, following the project standards in `posts/README.md`.

## Usage
`/new-post [slug] [date]`

## Examples
- `/new-post lsars-expert-verification`
- `/new-post epms-discovery 2026-02-15`
- `/new-post` (interactive; slug will be generated)

---

## Post Creation Checklist

**Every post creation MUST complete ALL items below. Do not end the command until all are done.**

### Required for ALL posts
- [ ] Post folder created: `posts/YYYY/MM/YYYY-MM-DD_[postid]_slug/`
- [ ] Post file created: `post-[slug]-[postid].md` with complete draft
- [ ] `assets/` directory created (with README.md if assets are missing)
- [ ] Git commit created with post files
- [ ] Changes pushed to remote (`origin`) — required BEFORE Squawk ingestion (Squawk fetches assets from GitHub)
- [ ] Squawk ingestion complete (`upsert_document_draft` + `update_post_draft`)
- [ ] Squawk CUID recorded (document CUID and post CUID)

### Verification
- [ ] Squawk `get_content_item` confirms document and post exist with correct metadata

---

## Instructions

### 1. Parse args
- `slug` is optional. If missing, generate one from the user's working title/idea (kebab-case).
- `date` is optional. If missing, default to today in `YYYY-MM-DD`.

### 2. Run intake

Minimum required inputs:
- **Working title or idea** (1–2 sentences)
- **Audience**: business | technical | mixed
- **Theme**: Experts+AI | AI technology | Compliance+scale
- **Product(s)**: See `lsaProductExpertAlignment.md` for the canonical product list
- **One concrete "what we did" artifact** to anchor the post
- **Channel**: LinkedIn post | demo clip script | longer artifact
- **CTA**: book a working session | request a demo | see artifacts
  - Business posts (LSARS channel): use `https://lsars.com`
  - Tech posts (LSA Digital channel): use `https://lsadigital.com`
- **Poster** (company page | founder | SME)

Apply sensible defaults based on type:
- **Business posts**: Audience=business, Theme=Experts+AI or Compliance+scale, CTA=book a working session
- **Tech posts**: Audience=technical, Theme=AI technology, CTA=see artifacts or request a demo

### 3. Supporting material collection
- **Remote links** (product pages, partner sites, prior posts, specs)
- **Local assets**: If unavailable, create `assets/README.md` with a checklist of needed items

### 4. SME alignment
- Read `lsaProductExpertAlignment.md` and pick the **default reviewer(s)** based on the product(s).
- If LSARS/HRA-heavy, note that tagging principals requires pre-coordination.

### 5. Determine the Post ID
- Scan the `posts/2026/02/` directory for existing post IDs to find the next available number.
- ID format: `YYYY-T-NNN` where `T` = `B` (business) or `T` (tech)
- Pattern:
  ```bash
  ls posts/2026/02/ | grep -oP '2026-[BT]-\d+' | sort | tail -1
  ```
- Increment the highest existing number by 1. If no posts of that type exist yet, start at 001.

### 6. Create the post folder and file
- Directory: `posts/YYYY/MM/YYYY-MM-DD_[postid]_slug/`
- File: `post-[slug]-[postid].md`
- Include: Title, Metadata, Post text, Artifacts

**Metadata standards**: See `docs/post-pipeline.md` for the full lifecycle. Post files contain only Post ID + CTA. All other metadata (Status, Product, Themes, Expert, Audience, etc.) is sent to Squawk via ingestion.

### 7. Create companion files as needed
- `links.md` for remote links with UTM variants
- `notes.md` for SME review notes and open questions

### 8. Git commit + push (BEFORE Squawk ingestion)

**Squawk fetches assets from the remote GitHub repo, so changes must be pushed first.**

1. Stage the new post folder:
   - `git add posts/2026/02/<folder>/`
2. Commit:
   - `posts: add <short-title> (<post-id>)`
3. Push to remote:
   - `git push`

Guardrails:
- Never commit secrets (e.g., `.env`, credentials, API keys).
- If `.env` or other sensitive files appear in `git status`, explicitly exclude them with `git reset HEAD <file>` before committing.

### 9. Ingest into Squawk MCP

**Step 9a**: Ingest via `upsert_document_draft`:
```javascript
execute_tool("squawk.upsert_document_draft", {
  "filePath": "posts/2026/02/<folder>/post-<slug>-<postid>.md",
  "referenceContext": {
    "postId": "<post-id>",
    "audience": "<business|technical>",
    "products": "<product-name>",
    "experts": "<expert-names>",
    "themes": "<THEME_TAG_1, THEME_TAG_2>",
    "sourceRepoUrl": "https://github.com/lsadigital/marketing"
  }
})
```
Returns: `{ documentId, postId }` — save the documentId (document CUID) and postId (post CUID).

**Step 9b**: Set expert and product via `update_post_draft`:
```javascript
execute_tool("squawk.update_post_draft", {
  "postId": "<returned-post-cuid>",
  "expertId": "<expert-cuid-from-table-below>",
  "productId": "<product-cuid-from-table-below>"
})
```

**Step 9c**: If post has dependencies, set dependency:
```javascript
execute_tool("squawk.update_post_draft", {
  "postId": "<returned-post-cuid>",
  "dependsOnPostId": "<dependency-post-cuid>"
})
```
Note: dependency post CUID can be found by searching `squawk-index.md` for the dependency post ID.

**Step 9d**: Verify ingestion:
```javascript
execute_tool("squawk.get_content_item", {"id": "<document-cuid>", "itemType": "document"})
```

**Squawk unavailability fallback**: If Squawk MCP calls fail (timeout, connection error):
1. Complete post creation locally (folder, file, assets).
2. Log warning: "⚠ Squawk ingestion failed. Run `/update-post <post-id> content` to ingest later."
3. Do NOT block the commit/push.

### 10. Rebuild squawk-index.md
```bash
PATH="/Users/idengrenme/.local/share/fnm/node-versions/v20.19.5/installation/bin:$PATH" node scripts/build-squawk-index.js
```

### 11. Confirm results
Output a completion summary showing:
- Created folder path and primary file
- Post ID assigned
- Squawk document CUID and post CUID
- Any items still needed (assets, SME review, etc.)

---

## Expert CUIDs

| Expert | CUID |
|--------|------|
| Keith Mangold | cml8m3t3e00020ys4ml0dfbl8 |
| Mike Idengren | cmksysncp000c67s4v38u04d0 |
| Nelson Smith | cmksysdl4000a67s4m1u7625r |
| Thad Perry | cmksysl3d000b67s4rd4kuhbq |

## Product CUIDs

| Product | CUID |
|---------|------|
| LSARS Permit Intelligence | cmksy89a7000367s4e634xb3k |
| Health Risk Assessment (HSRA) | cml77dhiy000g623jup13ylgk |
| EPMS | cmlqx3cm3000hh8s4ujarwpcx |
| ReimagineIt | cmksy7vqw000267s45kk14jq3 |
| MEDICODAX | cmlqx2xq1000gh8s4vkijzvid |
| Human-AI Concept Lab | cmlqx3u2q000ih8s4xcorgqim |

---

## Tone Guidance

### House voice (applies to ALL posts)
- **Artifact-first**: anchor the post in one concrete thing we built or shipped (report, diagram, workflow, dataset, configuration spec). Mention it in the post text, and list it under **Artifacts**.
- **Short, punchy paragraphs**: 1–3 sentences per paragraph. Avoid walls of text.
- **Assertive, evidence-oriented claims**: prefer “show your work / evidence / audit trail / bounded” over hype.
- **Use bold for structure**: section headers like `**How it works:**`, `**Why this matters:**`, `**Result:**` and bold labels at the start of bullets.
- **No fluff**: avoid “leveraging”, “synergy”, “revolutionary”, “game-changing”, “disrupt”.
- **CTA lives at the end**: no horizontal rule (`---`) before the CTA; final sentence(s) should naturally include the link.

### Default post shape (works for both business + tech)
First two beats are always:
1. **Hook** (problem/bad pattern, or good practice) — 1–2 sentences
2. **What we did** — 1 sentence starting with “We built …” or “We built X to …”

Then pick one of these middle structures (keep it tight):
- **Pattern A (classic)**: Hook → What we did → `**How it works:**` (3 bullets) → `**Why this matters:**` → `**Result:**` → CTA
- **Pattern B (outcome-forward)**: Hook → What we did → `**Result:**` → `**How it works:**` (3 bullets) → CTA
- **Pattern C (best-practice manifesto)**: Hook → What we did → stance (“best practice is …”) → `**How it works:**` (3 guardrail bullets) → `**Result:**` → CTA

Bullet guidance:
- Use **3 bullets** by default (4 max).
- Start each bullet with a **bold label** and keep each bullet to 1–2 lines.

### Business posts (B-type, LSARS channel)
- **Lead with the stakeholder problem** (trust, timelines, defensibility, evidence). Tech/AI comes second as the “how”.
- **Multi-stakeholder framing**: explicitly name stakeholders (e.g., communities, permit applicants, regulators). Avoid “Why it matters to you:” phrasing.
- **Concrete outcome language**: “reduce back-and-forth”, “fewer surprises”, “defensible deltas vs baseline”, “commitments tracked against outcomes”.
- **CTA link**: `https://lsars.com`

Strong business hooks tend to look like:
- A reframing: “X isn’t about Y — it’s about Z.”
- A cost-of-failure line: “The bottleneck isn’t disagreement — it’s evidence.”
- A shared-interest line: “It’s in everyone’s interest to …”

### Tech posts (T-type, LSA Digital channel)
- **Hook hard in the first 1–2 sentences**: a sharp consequence, contrast, or contrarian best practice.
- **High-level engineering patterns** (not low-level implementation): architecture choices, permissions, routing, auditability, escalation.
- **Include at least one “critical design choice”** sentence (e.g., what capability was intentionally removed/gated).
- **Do not reference timing** of the dependent upstream post (no “in our last post…”, no “next week…”). You may cite the dependency in metadata only.
- **Do not use internal IDs in the post text** (e.g., `2026-B-010`). IDs belong in **Metadata** and `post-index.md`, not in content for normal readers.
- **CTA link**: `https://lsadigital.com`

Strong tech hooks tend to look like:
- “Most systems do X. That’s why they fail at Y.”
- “If you can’t explain ___, you can’t trust ___.”
- “You picked the model. That was the easy part.”

### Ready-to-fill mini-templates (copy/paste)

**Business (LSARS)**
- Hook (1–2 sentences)
- We built <artifact/system> to <outcome>.
- `**How it works:**`
  - **<Label>**: <1 line>
  - **<Label>**: <1 line>
  - **<Label>**: <1 line>
- `**Why this matters for stakeholders:**`
  - **<Stakeholder>** <benefit>
  - **<Stakeholder>** <benefit>
  - **<Stakeholder>** <benefit>
- `**Result:**` <1 sentence>
- CTA sentence + `https://lsars.com`

**Tech (LSA Digital)**
- Hook (1–2 sentences)
- We built <pattern/system> to <outcome>.
- `**How it works:**`
  - **P1 / <Layer>**: <1 line>
  - **P2 / <Layer>**: <1 line>
  - **P3 / <Layer>**: <1 line>
- The critical design choice: **<constraint/gating rule>**.
- `**Result:**` <latency/cost/auditability/safety outcome in 1 sentence>
- CTA sentence + `https://lsadigital.com`

---

## File Structure Reference

```
posts/YYYY/MM/YYYY-MM-DD_[postid]_slug/
├── post-[slug]-[postid].md    # Main post file
├── assets/                     # Local assets
│   └── README.md              # Asset checklist if items missing
├── links.md                   # Optional: remote links + UTMs
└── notes.md                   # Optional: SME notes, approvals
```
