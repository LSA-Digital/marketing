## [2026-02-21] Session: ses_38c6e6f52ffeyZyLYfrlUXoIrk

### Project Context
- 82 posts in Squawk MCP, all with full metadata
- squawk-index.md is auto-generated from Squawk MCP cache + local assets scan
- post-index.md is being FULLY DEPRECATED (all metadata goes to Squawk)
- Squawk MCP invoked via: execute_tool("squawk.<tool>", {...})

### Key Conventions
- Post files stay MINIMAL: Post ID + CTA only
- Full metadata goes via referenceContext params in commands
- Themes: referenceContext.themes text labels only (no link_theme_source)
- Post ID generation: scan posts/2026/02/ directory names for highest B/T number
- Node.js: MUST use fnm PATH: PATH="/Users/idengrenme/.local/share/fnm/node-versions/v20.19.5/installation/bin:$PATH"

### Squawk MCP Expert CUIDs
- Keith Mangold: cml8m3t3e00020ys4ml0dfbl8
- Mike Idengren: cmksysncp000c67s4v38u04d0
- Nelson Smith: cmksysdl4000a67s4m1u7625r
- Thad Perry: cmksysl3d000b67s4rd4kuhbq

### Squawk MCP Product CUIDs
- LSARS Permit Intelligence: cmksy89a7000367s4e634xb3k
- Health Risk Assessment (HSRA): cml77dhiy000g623jup13ylgk
- EPMS: cmlqx3cm3000hh8s4ujarwpcx
- ReimagineIt: cmksy7vqw000267s45kk14jq3
- MEDICODAX: cmlqx2xq1000gh8s4vkijzvid
- Human-AI Concept Lab: cmlqx3u2q000ih8s4xcorgqim

### Squawk MCP Invocation Pattern
execute_tool("squawk.upsert_document_draft", {
  "filePath": "posts/2026/02/<folder>/post-<slug>-<postid>.md",
  "referenceContext": {
    "postId": "<post-id>",
    "audience": "<business|technical>",
    "products": "<product-name>",
    "experts": "<expert-names>",
    "themes": "<THEME_TAG_1, THEME_TAG_2>",
    "sourceRepoUrl": "https://github.com/<org>/marketing"
  }
})

### Build Script
- Location: scripts/build-squawk-index.js
- Run: PATH="..." node scripts/build-squawk-index.js [mcp-cache-path]
- Reads: cached list_review_queue JSON + post-index.md (fallback)
- Writes: squawk-index.md (15 columns, 82 rows)
- CUID mapping: hardcoded in script lines 16-36

### Squawk-Index-Updates (COMPLETED)
- squawk-index-updates plan is DONE (commits 8816893, f889302)
- squawk-index.md: 15 columns, 82 rows, asset thumbnails 180px hyperlinked
- Process doc: Rules 1-8 + 10 summary entries

## Task 6: README.md Command Updates (2026-02-21)

**Completed**: Updated `.claude/commands/README.md` to reflect command changes:
- Replaced `/update-status` with `/update-post` (new command for metadata/status updates)
- Updated `/list-posts` description to mention squawk-index.md and --live mode
- Added note about Squawk MCP routing and post-pipeline.md reference

**Key Pattern**: Command documentation lives in `.claude/commands/README.md` and must be kept in sync with actual command files in `.claude/commands/` directory.

**Verification**: 
- `grep -c "update-post"` = 1 ✓
- `grep -c "update-status"` = 0 ✓

### Asset Creation Pipeline Documentation (Task 2 - 2026-02-21)

**Completed:** Updated `docs/asset-creation-pipeline.md` with lifecycle context

**Changes:**
1. Added "Pipeline Context" section (lines 9-27) after Purpose paragraph
   - Explains assets are Stage 3 of content lifecycle
   - References `docs/post-pipeline.md` for full pipeline
   - Clarifies assets are filesystem-only (NOT in Squawk MCP)
   - Documents how build script scans `./assets/` directories
   - Includes asset rendering table (PNG/JPG/GIF/SVG → hyperlinked thumbnails, PDF → links, MP4/WEBM → video tags)

2. Updated "Delegation Pattern" section (lines 337-356) with Squawk integration
   - Added Squawk re-ingest pattern using `execute_tool("squawk.upsert_document_draft", {...})`
   - Added build script invocation with fnm PATH prefix
   - Explains when to rebuild squawk-index.md (after adding assets that are referenced in post body)

**File Stats:**
- Original: 379 lines
- Updated: 421 lines (+42 lines)
- Content preserved: All existing sections intact, no restructuring

**Key Insight:**
Assets are scanned by `scripts/build-squawk-index.js` at build time. The script:
- Looks for `posts/2026/02/*_{postId}_*/assets/` directories
- Renders images as hyperlinked 180px thumbnails
- Renders PDFs as `[📄 filename](path)` links
- Renders videos as `<video>` tags
- Shows `—` if no assets found
- Caps image thumbnails at 3 + `+N` indicator if more exist

**Build Command Reference:**
```bash
PATH="/Users/idengrenme/.local/share/fnm/node-versions/v20.19.5/installation/bin:$PATH" node scripts/build-squawk-index.js
```


## Task 9: post-index.md Deprecation Banner (2026-02-21)

**Completed**: Added deprecation banner to `post-index.md` and audited all references.

**Changes:**
1. Inserted deprecation blockquote at top of post-index.md (before `# Post Index` heading)
   - Banner text: "⚠ DEPRECATED — This file is no longer maintained. All post metadata now lives in **Squawk MCP**."
   - Links to: squawk-index.md, /list-posts command, docs/post-pipeline.md
   - Clarifies file is kept as read-only archive for historical reference

2. Audited all references to post-index across codebase:
   - Found 17 files referencing post-index
   - Key files: new-post.md, update-status.md, list-posts.md, build-squawk-index.js, AGENTS.md
   - All will be updated in subsequent tasks (3, 4, 5, 7, 8)

**Content Preservation:**
- File line count: 148 lines (was 140, +8 for banner)
- 2026-B-001 marker: present ✓
- 2026-T-045 marker: present ✓
- All 82 post rows intact ✓

**Evidence Files Created:**
- `.sisyphus/evidence/task-9-banner.txt` → grep count = 1 ✓
- `.sisyphus/evidence/task-9-references.txt` → 17 files listed
- `.sisyphus/evidence/task-9-content-preserved.txt` → line count + marker verification

**Key Insight:**
post-index.md is now clearly marked as deprecated but preserved. The banner directs users to:
1. View posts via squawk-index.md or /list-posts
2. Update posts via /update-post command
3. Understand full lifecycle via docs/post-pipeline.md

This unblocks Tasks 3, 4, 5, 7, 8 which will update all references and remove post-index.md dependencies.

### Post Pipeline Documentation (Task 1 - 2026-02-21)

**Completed:** Created `docs/post-pipeline.md` as the authoritative process document.

**Key Features:**
- **7-Stage Lifecycle:** Exploration, Post Creation, Asset Creation, Post Updates, Review & Readiness, Approval, Index Sync.
- **Squawk Integration:** Defines Squawk as the single source of truth for metadata.
- **Readiness Gate:** Enforces Rule 7 (readinessScore must be `ready` for approval).
- **Tool Reference:** Includes a quick reference for 12 Squawk MCP tools, Expert CUIDs, and Product CUIDs.
- **Command Reference:** Documents `/new-post`, `/update-post`, and `/list-posts`.
- **Deprecation Notice:** Formally deprecates `post-index.md` in favor of Squawk and `squawk-index.md`.

**Key Insight:**
The pipeline stops at **Approval**. Publication and pushing to GitHub are handled by separate processes outside the scope of this document. The `squawk-index.md` file is a derived artifact that must be rebuilt using `scripts/build-squawk-index.js` to reflect changes in Squawk or the local filesystem.

## Task 5: list-posts.md Dual-Mode Rewrite (2026-02-21)

**Completed**: Rewrote `.claude/commands/list-posts.md` to support dual-mode operation.

**Changes:**
1. Removed old filesystem-based approach (searching posts/ directory for post.md files)
2. Implemented Default Mode: reads squawk-index.md locally
   - Parses markdown table rows (lines starting with `| 2026-`)
   - Extracts: Post ID, Title, Review Status, Readiness, Audience, Product, Expert
   - Supports status filtering (case-insensitive)
   - Includes rebuild command with fnm PATH prefix
3. Implemented Live Mode (--live flag): queries Squawk MCP directly
   - Uses: execute_tool("squawk.list_review_queue", {"includeApproved": true, "limit": 100})
   - Parses response for: title, reviewStatus, readinessScore, updatedAt
   - Supports status filtering
   - Warns if exactly 100 items returned (truncation possible)
4. Updated output format to table with Post ID, Title, Status, Readiness
5. Documented valid status filters: PENDING_REVIEW, APPROVED, PUBLISHED

**File Stats:**
- Original: 27 lines
- Updated: 67 lines (+40 lines)
- Removed: All post.md filesystem references
- Added: squawk-index.md parsing + Squawk MCP integration

**Verification:**
- grep -c "--live|squawk-index|list_review_queue" = 14 ✓ (exceeds minimum 3)
- grep -c "post-index|post.md|posts/ directory" = 0 ✓ (no old sources)
- Evidence files created: task-5-dual-mode.txt, task-5-no-old-sources.txt

**Key Pattern:**
Commands now support dual-mode operation:
1. Default mode uses local squawk-index.md (fast, always available)
2. Live mode queries Squawk MCP (real-time, 100-item limit)
3. Both modes support status filtering
4. Output format is consistent across modes

This pattern can be applied to other commands (e.g., /update-post could support --live mode for real-time Squawk updates).

## Task 7: Build Script Hardening (2026-02-21)

**Completed**: Updated `scripts/build-squawk-index.js` with 2 surgical changes (3rd was already handled).

**Changes:**
1. **Dynamic date in header**: Replaced hardcoded `Last rebuilt: 2026-02-21` with `${new Date().toISOString().slice(0, 10)}` — header now reflects actual build date.
2. **MCP cache discovery**: Added loop after hardcoded mapping to scan `mcp.items` titles for post IDs not in mapping. Logs warning and adds dynamically. Ensures new posts added to Squawk don't silently get dropped.
3. **Graceful fallback**: Already handled — `const pi = postIndex[pid] || {};` + `clean()` function converts missing/empty fields to "—". No change needed.

**Verification:**
- Script output: "Wrote 82 rows to squawk-index.md" ✓
- `grep -c "^| 2026-" squawk-index.md` = 82 ✓
- `head -5 squawk-index.md | grep "Last rebuilt"` = `> Last rebuilt: 2026-02-21` ✓

**Key Insight:**
The dynamic discovery loop uses title regex matching (`/2026-[BT]-\d+/`) which works because Squawk MCP stores the post ID in the document title. This is fragile — if title format changes, discovery will break. The hardcoded mapping remains the primary lookup; dynamic discovery is a safety net.

## Task 4: update-post.md Command File (2026-02-21)

**Completed**: Created `.claude/commands/update-post.md` replacing the 22-line `update-status.md`.

**Changes:**
1. Created update-post.md (160+ lines) supporting 6 fields: status, expert, product, themes, depends-on, content
2. Deleted update-status.md (22 lines, wrote to post-index.md and metadata bullet lines)
3. Readiness gate enforcement: approval REFUSED if readinessScore ≠ "ready" (Rule 7)
4. Full CUID mapping table (82 entries from build-squawk-index.js lines 16-36)
5. Expert CUIDs (4) and Product CUIDs (6) lookup tables
6. Status transitions: draft/in_review=no-op, approved=readiness-gated approve_content_item, published=must-be-approved

**Key Differences from old update-status.md:**
- Old: wrote to post file metadata bullets + post-index.md → New: routes through Squawk MCP
- Old: 2 actions (read file, update Status bullet) → New: 6 field types with distinct Squawk tools
- Old: no validation → New: readiness gate blocks premature approval
- Old: supported draft/delayed, rejected → New: only draft, in_review, approved, published

**Squawk Tool Routing:**
- update_post_draft: expert, product, depends-on
- approve_content_item: status=approved (with readiness gate)
- upsert_document_draft: themes, content (re-ingest)
- get_content_item: readiness check + verification

**Evidence:**
- task-4-file-swap.txt → PASS
- task-4-fields.txt → 29 field references
- task-4-readiness-gate.txt → 6 readiness references
- task-4-no-postindex.txt → 0 post-index references
- task-4-squawk-tools.txt → 10 Squawk tool references

## Task 3: new-post.md Squawk Routing Rewrite (2026-02-21)

**Completed**: Rewrote `.claude/commands/new-post.md` to route through Squawk MCP instead of post-index.md.

**Changes:**
1. **Checklist**: Removed "post-index.md updated" and "Next IDs incremented". Added "Squawk ingestion complete" and "Squawk CUID recorded". Updated verification to use `get_content_item`.
2. **Step 6 (Post ID)**: Replaced "Read post-index.md" with directory scanning: `ls posts/2026/02/ | grep -oP '2026-[BT]-\d+'`
3. **Step 7 (Metadata reference)**: Changed from AGENTS.md POST METADATA GUIDELINES to `docs/post-pipeline.md` reference.
4. **Step 9 (Squawk ingestion)**: Replaced "Update post-index.md" with full Squawk MCP integration (upsert_document_draft + update_post_draft + get_content_item verification). Includes fallback for Squawk unavailability.
5. **Step 11 (Confirm)**: Added "Squawk document CUID and post CUID" to completion summary.
6. **Step 12 (Git commit)**: Removed post-index.md from staged files description.
7. **CUID tables**: Embedded Expert (4) and Product (6) CUID lookup tables as reference sections.

**Conflict Note**: Line 276 (inside verbatim-preserved tone guidance) still references `post-index.md` in the phrasing "IDs belong in **Metadata** and `post-index.md`, not in content for normal readers." This is the ONLY remaining reference. It was preserved per the explicit MUST NOT DO rule: "Do NOT change the tone guidance section — preserve verbatim."

**Evidence:**
- task-3-no-postindex.txt → 1 (single reference in verbatim tone guidance)
- task-3-squawk-ingestion.txt → 7 (Squawk ingestion references)
- task-3-cuid-tables.txt → 2 (CUID table markers present)
- task-3-tone-preserved.txt → 3 (House voice, Artifact-first, Short punchy all present)
- task-3-fallback.txt → 6 (fallback/timeout/fail references)

**Key Pattern**: Squawk ingestion is 4 sub-steps: upsert_document_draft (creates doc+post) → update_post_draft (sets expert+product CUIDs) → optional update_post_draft (dependency) → get_content_item (verify). Fallback allows local-only completion if Squawk is unavailable.

## Task 8: AGENTS.md Squawk-First Update (2026-02-21)
Applied 9 changes: updated header date, expanded STRUCTURE tree (docs/, scripts/, assetpipe/, squawk-index.md, deprecated post-index.md), added SQUAWK FIRST rule, rewrote Authoritative Source for Squawk MCP, updated server count to 6 with squawk, added squawk to Tool Categories, added CONTENT PIPELINE section with commands and rebuild index, added changelog entry, fixed config path to .Claude/oh-my-Claude.json. Verification: squawk refs=14, SQUAWK FIRST=1, no live post-index.md references (5 deprecation/historical mentions only).
