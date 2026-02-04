# New Post

Create a new marketing post folder **and draft the post content**, following the project standards in `posts/README.md`.

## Usage
`/new-post [slug] [date]`

## Examples
- `/new-post lsars-expert-verification`
- `/new-post epms-discovery 2026-02-15`
- `/new-post` (interactive; slug will be generated)

## Instructions
When the user invokes this command:
1. Parse args:
   - `slug` is optional. If missing, generate one from the user's working title/idea (kebab-case).
   - `date` is optional. If missing, default to today in `YYYY-MM-DD`.

2. Choose creation mode (ask in a single message, then proceed):
   - **Guided**: user answers prompts; agent drafts from scratch
   - **Mind map**: agent pulls from an XMind node (recommended when the topic already exists in `docs/mindmaps/`)

3. Run a short intake (ask in a single message, then proceed).

   **If Guided mode**, minimum required inputs:
   - **Working title or idea** (1–2 sentences)
   - **Audience**: business | technical | mixed
   - **Theme**: Experts+AI | AI technology | Compliance+scale
   - **Product(s)**: See `lsaProductExpertAlignment.md` for the canonical product list (LSARS | HRA | MEDICODA | EPMS | ReimagineIt | Human‑AI Concept Lab | CCN). If working from an XMind mindmap, extract product from the map structure. If working from post content alone, infer product from mentions and validate against the alignment doc.
   - **One concrete "what we did" artifact** to anchor the post (screenshot, demo clip, architecture diagram, test/validation evidence, workflow step)
   - **Stage / claim boundaries**: prototype | in progress | public beta | deployed
   - **Channel**: LinkedIn post | demo clip script | longer artifact
   - **CTA**: book a working session | request a demo | see artifacts
   - **Publish target** (date/time) and **Poster** (company page | founder | SME)

   **If Mind map mode**, minimum required inputs:
   - **XMind file path** (default: `docs/mindmaps/LSARS_posts_v2.xmind` unless the user specifies another)
   - **Which node to pull from**: node title/path (preferred) or node ID
   - **Audience / Channel / Theme / CTA** (same options as Guided mode)
   - Then use the XMind MCP tools to extract the node subtree (title, synopsis, notes, stakeholders, and technology best-practice children) and draft the post from that source.

4. Supporting material collection (optional but strongly encouraged):
   - **Remote links** (product pages, partner sites, prior posts, specs)
   - **Local assets** (images/video/diagrams/PDF):
     - If the user can attach files in the chat, ask them to attach them now.
     - If the user has files on disk, ask for file paths; copy them into `assets/` using the same (or cleaner) filenames.
     - If the user can't provide files yet, create an `assets/README.md` with a checklist of missing assets to add later.

5. SME alignment (keep claims accurate):
   - Read `lsaProductExpertAlignment.md` and pick the **default reviewer(s)** based on the chosen product(s).
   - If the post is LSARS/HRA-heavy, suggest whether it's appropriate to tag LSARS principals **only after pre-coordination**.

6. Determine the Post ID:
   - Read `post-index.md` (in project root) to find the next available ID.
   - ID format: `YYYY-T-NNN` where `T` = `B` (business/LSARS channel) or `T` (tech/LSA Digital channel), `NNN` = sequential number.
   - Check the "Next IDs" section at the bottom of `post-index.md` for the next available number.

7. Create the post folder:
   - Directory structure: `posts/YYYY/MM/YYYY-MM-DD_slug/`
   - Create `assets/` subdirectory
   - Create the post file using naming convention: `post-[slug]-[postid].md` (e.g., `post-auditable-ai-trust-2026-B-001.md`)
   - Use `posts/_template/post.md` as the base, but **fill it in**:
     - Title
     - Metadata fields (Post ID, Channel, Target page, Product, Theme, Audience, Status=draft, Publish target, Poster, SME reviewer, CTA, Depends on)
     - A complete first draft of the post text (artifact-first; "what we did" before advice)
     - Artifacts list (local paths + remote links)
     - Claim boundaries (what we can say safely vs should NOT claim)
     - Notes section including:
       - 3 repost-kit caption variants (business / technical / partner voice)
       - A question prompt for comments
       - UTM block (use `utm_campaign=feb_2026_human_ai` and `utm_content=<slug>`)

8. Create companion files as needed:
   - `links.md` (if any remote links exist): include canonical URLs + optional UTM variants
   - `notes.md` (if approvals/research are relevant): include SME review notes, open questions, and "needs evidence" items

9. Update `post-index.md` (in project root):
   - Add a new row to the Post Index table with: Post ID, Name, Link, Status, Type, Product, Publish Target, Depends On, Dependency Name.
   - Increment the "Next IDs" section at the bottom of the file.

10. XMind traceability (Mind map mode only):
   - After the post is created, mark the **source mind map node as used** by adding a label containing the Post ID (example label: `2026-B-003`).
   - Use the XMind MCP tools to locate the node (by path or node ID) and report its ID/path in the output so a human can quickly apply the label in XMind.
   - Note: the current XMind MCP tooling supports reading/extraction, but not reliably editing existing `.xmind` files in-place. Treat label application as a manual step in XMind unless tooling support is added.

11. Confirm results:
   - Output the created folder path and the primary file to edit.
   - Summarize what still needs to be provided (missing assets, SME review, final CTA link, etc.).

## Tone Guidance

### Business posts (B-type, LSARS channel)
- **Lead with the business problem**, not the technology. Open with the stakeholder pain point or industry challenge (e.g., "Data center permit fights are rarely about pollutants—they're about trust").
- Technology/AI comes second, as the "how we addressed it."

### Multi-stakeholder framing
- Write for **all stakeholders**. The most powerful framing is shared interest: "It's in everyone's interest to get permits approved faster."
- Start broad ("everyone benefits from..."), then discuss how specific stakeholders see it differently if relevant.
- **Avoid "Why it matters to you:" sections**—there are multiple stakeholders reading, so "you" is ambiguous. Instead, name the stakeholders explicitly when discussing their perspectives (e.g., "For permit requestors..." / "For community leadership...").

### Tech posts (T-type, LSA Digital channel)
- **Hook hard in the first 1–2 sentences.** Use a dramatic consequence (compliance failure, rework, hidden risk, security footguns) or a positive contrast (great UX in a domain where UX is typically poor). Then pivot to the best practice.
- **Do not reference the existence or timing of a dependent upstream post.** If the tech post is a repost/expansion, treat it as standalone—LinkedIn will already show context to anyone who wants it.
- **Keep it high-level.** Make the best-practice statement, then briefly explain how we implemented it—avoid low-level implementation specifics (e.g., specific databases, vendor tools, internal hostnames, exact services). Prefer phrasing like “pre-loaded into a database” or “behind a reverse proxy” instead of naming components.
- Still ground in the business outcome the tech enables.

### Post patterns (choose one; first two beats are always the same)

The first two beats should be consistent across posts:
- **Hook** (problem/bad pattern to avoid, or good practice that yields good results) — 1–2 sentences
- **What we did** — 1 sentence, concrete and artifact-first

After that, vary the structure for style diversity.

#### Pattern A (classic: proof → details → outcome)
- Hook
- What we did
- **Credibility**: A single human sentence that ties the practice to real LSARS work (no time-language, no internal IDs). Example: “We applied this in LSARS permitting workflows—where trust and auditability are the whole game.”
- **Key supporting details**: 3 bullets (high-level; no low-level stack specifics)
- **Result / outcome**: 1–2 sentences

#### Pattern B (outcome-forward: consequence → fix → proof)
- Hook
- What we did
- **Result / outcome**: 1–2 sentences (what improved / what got easier / what risk was reduced)
- **Key supporting details**: 3 bullets
- **Credibility**: “Proof point” line grounded in LSARS work (again, no “last week / yesterday”, and no internal IDs). If needed, link to a public page (e.g., LSARS website) rather than internal references.

#### Pattern C (best-practice manifesto: stance → guardrails → outcome)
- Hook
- What we did
- **Best-practice stance**: 1 sentence (“If AI influences X, then Y must be true…”)
- **Key supporting details**: 3 bullets (guardrails / controls / artifacts)
- **Credibility**: Mention the LSARS applied context in a human way (no timing assumptions, no internal IDs)
- Result / outcome

---

Follow the structure defined in `posts/README.md`:
- Use date format: `YYYY-MM-DD_slug` for the folder
- Create post file as `post-[slug]-[postid].md` (not just `post.md`)
- Fill with a complete draft from the template
- Create `assets/` directory for local files
