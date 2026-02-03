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
   - `slug` is optional. If missing, generate one from the user’s working title/idea (kebab-case).
   - `date` is optional. If missing, default to today in `YYYY-MM-DD`.

2. Run a short guided intake (ask in a single message, then proceed). Minimum required inputs:
   - **Working title or idea** (1–2 sentences)
   - **Audience**: business | technical | mixed
   - **Theme**: Experts+AI | AI technology | Compliance+scale
   - **Product(s)** (if applicable): LSARS | HRA | MEDICODA | EPMS | ReimagineIt | Human‑AI Concept Lab | other
   - **One concrete “what we did” artifact** to anchor the post (screenshot, demo clip, architecture diagram, test/validation evidence, workflow step)
   - **Stage / claim boundaries**: prototype | in progress | public beta | deployed
   - **Channel**: LinkedIn post | demo clip script | longer artifact
   - **CTA**: book a working session | request a demo | see artifacts
   - **Publish target** (date/time) and **Poster** (company page | founder | SME)

3. Supporting material collection (optional but strongly encouraged):
   - **Remote links** (product pages, partner sites, prior posts, specs)
   - **Local assets** (images/video/diagrams/PDF):
     - If the user can attach files in the chat, ask them to attach them now.
     - If the user has files on disk, ask for file paths; copy them into `assets/` using the same (or cleaner) filenames.
     - If the user can’t provide files yet, create an `assets/README.md` with a checklist of missing assets to add later.

4. SME alignment (keep claims accurate):
   - Read `lsaProductExpertAlignment.md` and pick the **default reviewer(s)** based on the chosen product(s).
   - If the post is LSARS/HRA-heavy, suggest whether it’s appropriate to tag LSARS principals **only after pre-coordination**.

5. Create the post folder:
   - Directory structure: `posts/YYYY/MM/YYYY-MM-DD_slug/`
   - Create `assets/` subdirectory
   - Create `post.md` by using `posts/_template/post.md` as the base, but **fill it in**:
     - Title
     - Metadata fields (Channel, Theme, Status=draft, Publish target, Poster, SME reviewer, CTA)
     - A complete first draft of the post text (artifact-first; “what we did” before advice)
     - Artifacts list (local paths + remote links)
     - Claim boundaries (what we can say safely vs should NOT claim)
     - Notes section including:
       - 3 repost-kit caption variants (business / technical / partner voice)
       - A question prompt for comments
       - UTM block (use `utm_campaign=feb_2026_human_ai` and `utm_content=<slug>`)

6. Create companion files as needed:
   - `links.md` (if any remote links exist): include canonical URLs + optional UTM variants
   - `notes.md` (if approvals/research are relevant): include SME review notes, open questions, and “needs evidence” items

7. Confirm results:
   - Output the created folder path and the primary file to edit (`post.md`).
   - Summarize what still needs to be provided (missing assets, SME review, final CTA link, etc.).

Follow the structure defined in `posts/README.md`:
- Use date format: `YYYY-MM-DD_slug`
- Create `post.md` from template and **fill it with a complete draft**
- Create `assets/` directory for local files
