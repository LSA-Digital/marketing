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
- [ ] `post-index.md` updated with new row
- [ ] `post-index.md` "Next IDs" incremented
- [ ] Git commit created with post + index + mindmap updates
- [ ] Changes pushed to remote (`origin`)

### Required for Mind Map mode
- [ ] XMind label applied directly using: `python3 scripts/update_xmind_labels.py <xmind-file> <node-id> <post-id>`
- [ ] Label verified using XMind MCP `search_nodes` with `searchIn: ["labels"]`
- [ ] If node has relationships to other topic areas, identify and create linked post pairs

### Verification
- [ ] Verify post-index.md row matches post file metadata

---

## Instructions

### 1. Parse args
- `slug` is optional. If missing, generate one from the user's working title/idea (kebab-case).
- `date` is optional. If missing, default to today in `YYYY-MM-DD`.

### 2. Choose creation mode (ask in a single message, then proceed)
- **Guided**: user answers prompts; agent drafts from scratch
- **Mind map**: agent pulls from an XMind node (recommended when the topic already exists in `docs/mindmaps/`)

### 3. Run intake

**If Guided mode**, minimum required inputs:
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

**If Mind map mode**, minimum required inputs:
- **XMind file path** (default: `docs/mindmaps/LSARS_posts_v2.xmind`)
- **Which node to pull from**: node title/path (preferred) or node ID
- Then use the XMind MCP tools to extract the node subtree and draft the post.

**Automatic post type detection from mind map location**:
The mind map structure determines the post type automatically—do NOT ask the user:
- **Tech post (T-type)**: Nodes under `LSARS > Technology` (includes AI / Best Practices and all other Technology sub-nodes)
- **Business post (B-type)**: All other top-level topic areas (Permit Requestor, Regulatory Alignment, Communities, Data Centers, Smart Mobility, "How does LSARS help Governments...", etc.)

**IMPORTANT**: Never pull a business post from any node under `LSARS > Technology`. All Technology nodes produce tech posts, regardless of their specific content.

Apply sensible defaults based on type:
- **Business posts**: Audience=business, Theme=Experts+AI or Compliance+scale, CTA=book a working session
- **Tech posts**: Audience=technical, Theme=AI technology, CTA=see artifacts or request a demo

**Check for linked post pairs**:
When creating from Mind map mode, check the XMind relationships for links between:
- AI/Best Practices nodes (tech posts) ↔ Business outcome nodes (business posts)
- If a relationship exists (e.g., "evidenced by", "enables", "builds", "supports"), create BOTH posts as a pair with the tech post depending on the business post.

### 4. Supporting material collection
- **Remote links** (product pages, partner sites, prior posts, specs)
- **Local assets**: If unavailable, create `assets/README.md` with a checklist of needed items

### 5. SME alignment
- Read `lsaProductExpertAlignment.md` and pick the **default reviewer(s)** based on the product(s).
- If LSARS/HRA-heavy, note that tagging principals requires pre-coordination.

### 6. Determine the Post ID
- Read `post-index.md` to find the next available ID.
- ID format: `YYYY-T-NNN` where `T` = `B` (business) or `T` (tech)

### 7. Create the post folder and file
- Directory: `posts/YYYY/MM/YYYY-MM-DD_[postid]_slug/`
- File: `post-[slug]-[postid].md`
- Include: Title, Metadata, Post text, Artifacts

**Metadata standards**: See `AGENTS.md` "POST METADATA GUIDELINES" section. Individual post files must ONLY contain:
- `Post ID`: The post identifier
- `CTA`: Call-to-action link

All other metadata (Status, Product, Themes, Expert, Audience, etc.) is tracked exclusively in `post-index.md`.

### 8. Create companion files as needed
- `links.md` for remote links with UTM variants
- `notes.md` for SME review notes and open questions

### 9. Update post-index.md
- Add new row with: Post ID, Name, Link, Status, Type, Product, Depends On, Dependency Name
- Increment "Next IDs" section

### 10. Update XMind with Post ID label (REQUIRED for Mind map mode)

**This is NOT optional. The agent MUST update the XMind file synchronously as part of post creation.**

**Step 10a: Apply the label**
```bash
python3 scripts/update_xmind_labels.py docs/mindmaps/LSARS_posts_v2.xmind <node-id> <post-id>
```

Example:
```bash
python3 scripts/update_xmind_labels.py docs/mindmaps/LSARS_posts_v2.xmind 85bee37e6bab4e0a8b5c7ad50b 2026-B-003
```

**Step 10b: Verify the label was applied**
Use the XMind MCP to confirm:
```
search_nodes(
  path: "docs/mindmaps/LSARS_posts_v2.xmind",
  query: "<post-id>",
  searchIn: ["labels"]
)
```

**If verification fails**, the post creation is incomplete. Debug and retry before proceeding.

### 11. Confirm results
Output a completion summary showing:
- Created folder path and primary file
- Post ID assigned
- XMind node labeled (confirmed by search)
- Any items still needed (assets, SME review, etc.)

### 12. Git commit + push (REQUIRED)

**Do not end the command until changes are committed and pushed.**

1. Verify what will be committed:
   - `git status`
   - `git diff`
2. Stage ALL outstanding changes:
   - `git add .`
   - This includes the new post folder(s), `post-index.md`, XMind files, and any other modified files in the repository
3. Create a commit with a clear message. Suggested format:
   - `posts: add <short-title> (<post-id>)`
   - If a linked tech/business pair was created, include both IDs in one commit message.
   - If other files beyond the post are included, mention them briefly if significant
4. Push to remote:
   - `git push`

Guardrails:
- Never commit secrets (e.g., `.env`, credentials, API keys).
- If `.env` or other sensitive files appear in `git status`, explicitly exclude them with `git reset HEAD <file>` before committing.

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
