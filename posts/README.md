# Posts folder standard

Everything that ships as content lives under `posts/`.

## Core rules
- **Each post gets its own sub-folder** under `posts/`.
- A “post” is defined by **one Markdown file** (canonical post text) + optional supporting assets (images/video/diagrams/PDF exports).
- **Local assets** must live **with** the Markdown file (same post folder, usually in `assets/`).
- **Remote links** are allowed (product pages, partner sites, YouTube, etc.).

## Recommended structure (date + slug)

`posts/YYYY/MM/YYYY-MM-DD_slug/`
- `post.md` — canonical post text + metadata + publication notes
- `assets/` — optional local assets
- `links.md` — optional: citations, UTMs, canonical URLs
- `notes.md` — optional: research, SME feedback, approvals

Example:

`posts/2026/02/2026-02-03_lsars-expert-verification/`
- `post.md`
- `assets/lsars_workflow_before_after.png`
- `links.md`

## Template
Copy `posts/_template/` to start a new post.

