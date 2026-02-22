# Post Pipeline: Process Doc + Command Implementation

## TL;DR

> **Quick Summary**: Create `docs/post-pipeline.md` as the authoritative end-to-end process for creating and updating marketing posts (exploration → approval), then update all commands, scripts, and AGENTS.md to route through Squawk MCP as the sole source of truth, fully deprecating post-index.md.
> 
> **Deliverables**:
> - `docs/post-pipeline.md` — End-to-end process document (exploration → approval → index sync)
> - `docs/asset-creation-pipeline.md` — Updated with lifecycle context + Squawk cross-references
> - `.claude/commands/new-post.md` — Rewritten for Squawk-first ingestion, post-index.md removed
> - `.claude/commands/update-post.md` — New command replacing update-status.md, routes through Squawk MCP
> - `.claude/commands/list-posts.md` — Dual mode: squawk-index.md default + `--live` Squawk MCP flag
> - `.claude/commands/README.md` — Updated command listing
> - `AGENTS.md` — Comprehensive update: Squawk as SoT, file tree, MCP tools, metadata guidelines
> - `scripts/build-squawk-index.js` — Updated to handle new posts without post-index.md dependency
> - `post-index.md` — Deprecation banner added (file kept as read-only archive)
> 
> **Estimated Effort**: Medium
> **Parallel Execution**: YES — 3 waves
> **Critical Path**: Task 1 (process doc) → Task 3 (new-post) → Task 8 (AGENTS.md)

---

## Context

### Original Request
Create a plan in `docs/post-pipeline.md` describing the end-to-end process for creating and updating posts, from exploration to approval, including assets. Reference `docs/asset-creation-pipeline.md`. Separately, create an implementation plan so that post-pipeline can be executed with the commands, which may also include deterministic scripts. Update commands and AGENTS.md for the regular content workflow (not migration).

### Interview Summary
**Key Decisions**:
- **post-index.md**: Fully deprecated — stop writing, Squawk is sole SoT, add deprecation banner
- **Pipeline scope**: Exploration → Creation → Assets → Updates → Review → Approval → Index Sync (no publication/push stage)
- **list-posts data source**: Dual mode — squawk-index.md default, `--live` flag queries Squawk MCP directly
- **Post metadata in files**: Keep minimal (Post ID + CTA only) — full data goes via `referenceContext` params in commands
- **Theme handling**: `referenceContext.themes` text labels only — no `link_theme_source` CUID-based linking
- **Post ID generation**: Scan directory names for highest existing B/T number, increment

### Research Findings
- **Current state**: 82 posts in Squawk with full metadata. `squawk-index.md` has 82 rows, 15 columns. Build script at `scripts/build-squawk-index.js` (184 lines) reads cached MCP JSON + post-index.md for supplementary data.
- **AGENTS.md contradiction**: Line 33 says "metadata lives in squawk-index.md" but line 84 says "post-index.md is the single source of truth" — already inconsistent and confusing agents.
- **Build script CUID mapping**: Hardcoded table (lines 16-36) with 82 entries. No growth mechanism for new posts.
- **list_review_queue limit**: Maximum 100 items per call. With 82 posts, close to ceiling.
- **Squawk MCP tools**: 12 tools — 5 write, 4 read, 2 publish, 1 info. Key workflow tools: `upsert_document_draft`, `update_post_draft`, `approve_content_item`, `list_review_queue`, `get_content_item`.
- **Asset creation pipeline**: 379 lines, comprehensive Playwright/Docker/auth coverage, but no lifecycle context or Squawk cross-reference.
- **Migration doc post-migration section**: Lines 584-619 already outline this work — commands, AGENTS.md, list-posts.

### Metis Review
**Identified Gaps** (addressed in plan):
- CUID mapping growth mechanism needed for new posts → Task 7 (build script update)
- Post ID generation after post-index.md removal → Task 3 (new-post) includes directory scanning
- 100-item limit on list_review_queue → Task 5 (list-posts) handles pagination for --live mode
- Squawk MCP unavailability during /new-post → Task 3 includes graceful fallback
- All references to post-index.md across codebase must be found and updated → Task 9 (deprecation) includes codebase-wide search
- Theme handling clarified: referenceContext.themes only, no link_theme_source

---

## Work Objectives

### Core Objective
Establish the regular content workflow by creating a process document and updating all tooling to route through Squawk MCP as the sole source of truth, eliminating the dual-write to post-index.md.

### Concrete Deliverables
- `docs/post-pipeline.md` — 7-stage pipeline process document
- `docs/asset-creation-pipeline.md` — Updated with lifecycle stage cross-references
- `.claude/commands/new-post.md` — Squawk-first, no post-index.md writes
- `.claude/commands/update-post.md` — New, replaces update-status.md
- `.claude/commands/list-posts.md` — Dual-mode with squawk-index.md + `--live`
- `.claude/commands/README.md` — Updated
- `AGENTS.md` — Squawk as SoT, updated file tree and rules
- `scripts/build-squawk-index.js` — Handles new posts, phased post-index.md removal
- `post-index.md` — Deprecation banner

### Definition of Done
- [ ] `docs/post-pipeline.md` exists and covers all 7 stages
- [ ] `/new-post` command includes Squawk ingestion steps (upsert + update_post_draft)
- [ ] `/new-post` command does NOT reference post-index.md
- [ ] `/update-post` command exists with status/metadata update flows through Squawk
- [ ] `/list-posts` command supports both default and `--live` modes
- [ ] `AGENTS.md` references Squawk as SoT, not post-index.md
- [ ] `post-index.md` has a deprecation banner at the top
- [ ] `scripts/build-squawk-index.js` can handle posts not in the hardcoded mapping
- [ ] All files that referenced post-index.md as SoT have been updated or deprecated

### Must Have
- Process doc covers: Exploration, Creation, Assets, Updates, Review, Approval, Index Sync
- Process doc references `docs/asset-creation-pipeline.md` for the asset stage
- `/new-post` creates post folder + ingests into Squawk in one flow
- `/update-post` supports: status change, expert/product update, dependency update, theme update
- `/update-post` enforces readiness gate (Rule 7) for approvals
- `/list-posts` default mode parses squawk-index.md for output
- `AGENTS.md` has correct file tree including squawk-index.md, scripts/, assetpipe/, docs/post-pipeline.md
- `AGENTS.md` MCP tools table includes Squawk (12 tools)
- Build script handles growth (new posts beyond hardcoded 82)

### Must NOT Have (Guardrails)
- **DO NOT** modify Squawk MCP tools/backend — this is consumer-side work only
- **DO NOT** implement publication/push stage — pipeline stops at approval
- **DO NOT** use `link_theme_source` — themes go via `referenceContext.themes` only
- **DO NOT** delete post-index.md — add deprecation banner, keep as read-only archive
- **DO NOT** change post file content structure — files stay minimal (Post ID + CTA)
- **DO NOT** modify `docs/squawk-migration-process.md` — that's a completed project record
- **DO NOT** modify XMind integration (`scripts/update_xmind_labels.py`) — stays as-is
- **DO NOT** add commands beyond the 3 specified (new-post, update-post, list-posts)
- **DO NOT** over-engineer the build script — update data sources, not rendering logic
- **DO NOT** modify any existing post files in `posts/` — only command/doc/script files

---

## Verification Strategy

> **ZERO HUMAN INTERVENTION** — ALL verification is agent-executed. No exceptions.

### Test Decision
- **Infrastructure exists**: NO (marketing content repo, not a code project)
- **Automated tests**: None — these are markdown command files and process docs
- **Framework**: N/A

### QA Policy
Every task MUST include agent-executed QA scenarios.
Evidence saved to `.sisyphus/evidence/task-{N}-{scenario-slug}.{ext}`.

- **Command files**: Read the file, verify required sections exist, verify no references to deprecated sources
- **Process docs**: Read the file, verify all stages documented, verify cross-references resolve
- **Scripts**: Run the script, verify output, diff against baseline
- **AGENTS.md**: Read the file, verify no contradictions, verify file tree accuracy

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1 (Start Immediately — process doc + independent updates):
├── Task 1: Create docs/post-pipeline.md (process document) [writing]
├── Task 2: Update docs/asset-creation-pipeline.md (lifecycle refs) [quick]
├── Task 9: Deprecate post-index.md (add banner + find all refs) [quick]
└── Task 6: Update .claude/commands/README.md [quick]

Wave 2 (After Wave 1 — commands that reference the process doc):
├── Task 3: Rewrite .claude/commands/new-post.md [unspecified-high]
├── Task 4: Create .claude/commands/update-post.md [unspecified-high]
├── Task 5: Rewrite .claude/commands/list-posts.md [quick]
└── Task 7: Update scripts/build-squawk-index.js [unspecified-high]

Wave 3 (After Wave 2 — AGENTS.md depends on final command names + script state):
└── Task 8: Update AGENTS.md [unspecified-high]

Wave FINAL (After ALL tasks — independent review, 4 parallel):
├── Task F1: Plan compliance audit (oracle)
├── Task F2: Content quality review (unspecified-high)
├── Task F3: Cross-reference integrity check (unspecified-high)
└── Task F4: Scope fidelity check (deep)

Critical Path: Task 1 → Task 3 → Task 8 → F1-F4
Parallel Speedup: ~50% faster than sequential
Max Concurrent: 4 (Wave 1)
```

### Dependency Matrix

| Task | Depends On | Blocks | Wave |
|------|-----------|--------|------|
| 1 | — | 3, 4, 5, 8 | 1 |
| 2 | — | 8 | 1 |
| 6 | — | 8 | 1 |
| 9 | — | 3, 4, 7, 8 | 1 |
| 3 | 1, 9 | 8 | 2 |
| 4 | 1, 9 | 8 | 2 |
| 5 | 1 | 8 | 2 |
| 7 | 9 | 8 | 2 |
| 8 | 1, 2, 3, 4, 5, 6, 7, 9 | F1-F4 | 3 |
| F1-F4 | 8 | — | FINAL |

### Agent Dispatch Summary

- **Wave 1**: **4** — T1 → `writing`, T2 → `quick`, T6 → `quick`, T9 → `quick`
- **Wave 2**: **4** — T3 → `unspecified-high`, T4 → `unspecified-high`, T5 → `quick`, T7 → `unspecified-high`
- **Wave 3**: **1** — T8 → `unspecified-high`
- **FINAL**: **4** — F1 → `oracle`, F2 → `unspecified-high`, F3 → `unspecified-high`, F4 → `deep`

---

## TODOs

- [ ] 1. Create `docs/post-pipeline.md` — End-to-End Process Document

  **What to do**:
  - Create `docs/post-pipeline.md` covering the 7-stage content lifecycle:
    1. **Exploration** — XMind mindmap browsing (`docs/mindmaps/LSARS_posts_v2.xmind`), campaign doc review (`marketingCampaignFeb2026.md`), topic ideation. Reference `scripts/analyze_xmind_coverage.py` for coverage analysis. Reference `docs/XMIND_ANALYSIS_GUIDE.md` and `docs/XMIND_COVERAGE_SUMMARY.md`.
    2. **Post Creation** — `/new-post` command flow: folder creation, draft writing, XMind label (if from mindmap), Squawk ingestion (`upsert_document_draft` + `update_post_draft`). Include post ID generation (scan directories), post type detection (B/T from mindmap location), metadata via `referenceContext`.
    3. **Asset Creation** — Reference `docs/asset-creation-pipeline.md` for the full procedure. Summarize asset types: Playwright screenshots, code snippets, Mermaid diagrams, markdown tables. Reference `assetpipe/` for reusable capture scripts. Note that assets are filesystem-only (not in Squawk).
    4. **Post Updates** — `/update-post` command flow: metadata changes (status, expert, product, themes, dependencies) via Squawk MCP. Status transitions and readiness gate enforcement.
    5. **Review & Readiness** — `list_review_queue` for queue inspection, readiness assessment by Squawk AI, `needs_work` vs `ready` states, how to address readiness issues.
    6. **Approval** — Readiness gate (Rule 7): only approve when `readinessScore = ready`. `approve_content_item` call. Grandfathered items note.
    7. **Index Sync** — `scripts/build-squawk-index.js` rebuilds `squawk-index.md` from scratch. Run after any Squawk data change. Cache the MCP response, run the script, verify output.
  - Include a **Squawk MCP Quick Reference** section: tool names, invocation patterns (`execute_tool("squawk.<tool>", {...})`), lookup tables (Expert CUIDs, Product CUIDs), pacing notes (1-2 calls at a time)
  - Include a **Commands Reference** section summarizing `/new-post`, `/update-post`, `/list-posts`
  - Include a **post-index.md Deprecation Notice** section: what it was, why it's archived, what replaces it
  - Write in the style of existing docs (e.g., `docs/asset-creation-pipeline.md` — procedural, tables, code blocks, no fluff)

  **Must NOT do**:
  - DO NOT include a publication/push stage
  - DO NOT reference post-index.md as a source of truth (except in the deprecation section)
  - DO NOT duplicate the full content of asset-creation-pipeline.md — reference it
  - DO NOT include Squawk MCP tool schemas — just names and brief descriptions

  **Recommended Agent Profile**:
  - **Category**: `writing`
    - Reason: This is a process documentation task — structured technical writing with cross-references
  - **Skills**: []
    - No special skills needed — the content comes from existing files
  - **Skills Evaluated but Omitted**:
    - `frontend-ui-ux`: Not a UI task
    - `playwright`: Not a browser task

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 2, 6, 9)
  - **Blocks**: Tasks 3, 4, 5, 8
  - **Blocked By**: None (can start immediately)

  **References** (CRITICAL):

  **Pattern References** (existing docs to follow):
  - `docs/asset-creation-pipeline.md` — Writing style, structure, section format. This is the gold standard for process docs in this repo.
  - `docs/squawk-migration-process.md:73-230` — Merge rules and Squawk data model. NOT to be modified, but the rendering rules (Rules 1-8) define how Squawk data maps to squawk-index.md and are relevant context for the Index Sync stage.
  - `docs/squawk-migration-process.md:584-619` — Post-migration work section that outlines what this plan implements.

  **API/Type References**:
  - `docs/squawk-migration-process.md:19-58` — Squawk MCP tool table, Expert CUIDs, Product CUIDs. Copy into the Quick Reference section.
  - `docs/squawk-migration-process.md:62-69` — Document vs Post data model explanation.

  **Content References** (what each stage should cover):
  - `docs/mindmaps/` — XMind files for exploration stage
  - `docs/XMIND_ANALYSIS_GUIDE.md` — XMind analysis methodology
  - `scripts/analyze_xmind_coverage.py` — Coverage analysis tool
  - `marketingCampaignFeb2026.md:1-50` — Campaign overview for exploration context
  - `lsaProductExpertAlignment.md:1-25` — Expert/Product alignment table
  - `.claude/commands/new-post.md` — Current creation flow (to be summarized, not copied)
  - `assetpipe/README.md` — Asset capture script index
  - `scripts/build-squawk-index.js` — Build script for index sync stage

  **WHY Each Reference Matters**:
  - asset-creation-pipeline.md: Sets the writing style — procedural, tables, code blocks, no fluff. The process doc should read like a companion to this.
  - squawk-migration-process.md: Contains the Squawk data model, merge rules, and tool reference that the process doc should summarize (not repeat verbatim).
  - The command files: The process doc describes WHAT happens at each stage; the commands define HOW. The doc should reference commands by name without duplicating their instructions.

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: Process doc covers all 7 stages
    Tool: Bash (grep)
    Preconditions: docs/post-pipeline.md exists
    Steps:
      1. grep -c "Exploration" docs/post-pipeline.md → ≥ 1
      2. grep -c "Post Creation" docs/post-pipeline.md → ≥ 1
      3. grep -c "Asset Creation" docs/post-pipeline.md → ≥ 1
      4. grep -c "Post Updates" docs/post-pipeline.md → ≥ 1
      5. grep -c "Review" docs/post-pipeline.md → ≥ 1
      6. grep -c "Approval" docs/post-pipeline.md → ≥ 1
      7. grep -c "Index Sync" docs/post-pipeline.md → ≥ 1
    Expected Result: All 7 stage headings present
    Evidence: .sisyphus/evidence/task-1-stages-present.txt

  Scenario: Cross-references to asset-creation-pipeline.md resolve
    Tool: Bash (grep + test)
    Preconditions: Both files exist
    Steps:
      1. grep "asset-creation-pipeline" docs/post-pipeline.md → shows reference
      2. test -f docs/asset-creation-pipeline.md → exists
    Expected Result: Reference exists and target file exists
    Evidence: .sisyphus/evidence/task-1-crossref-assets.txt

  Scenario: No reference to post-index.md as source of truth
    Tool: Bash (grep)
    Steps:
      1. grep -i "source of truth" docs/post-pipeline.md | grep -i "post-index" → empty
    Expected Result: No lines match
    Evidence: .sisyphus/evidence/task-1-no-postindex-sot.txt

  Scenario: Squawk MCP Quick Reference section exists
    Tool: Bash (grep)
    Steps:
      1. grep -c "upsert_document_draft" docs/post-pipeline.md → ≥ 1
      2. grep -c "update_post_draft" docs/post-pipeline.md → ≥ 1
      3. grep -c "approve_content_item" docs/post-pipeline.md → ≥ 1
    Expected Result: Key Squawk tools referenced
    Evidence: .sisyphus/evidence/task-1-squawk-tools.txt
  ```

  **Commit**: YES (groups with Wave 1: Tasks 2, 6, 9)
  - Message: `docs: create post-pipeline process doc and deprecate post-index.md`
  - Files: `docs/post-pipeline.md`

- [ ] 2. Update `docs/asset-creation-pipeline.md` — Lifecycle Context

  **What to do**:
  - Add a **Pipeline Context** section near the top (after the "Purpose" paragraph, before "Reusable Scripts") explaining where asset creation fits in the post lifecycle:
    - Assets are created AFTER the post draft exists and BEFORE review/approval
    - Reference `docs/post-pipeline.md` for the full lifecycle
    - Note: assets are filesystem-only — they are NOT stored in Squawk MCP
    - The `Assets Preview` column in squawk-index.md is generated by the build script scanning local `./assets/` directories
  - Add a **Squawk Index Integration** subsection explaining:
    - How assets appear in squawk-index.md (thumbnails, PDF links, video tags)
    - The build script (`scripts/build-squawk-index.js`) scans asset directories automatically
    - No manual registration needed — just put files in the `assets/` directory
  - Update the "Delegation Pattern" section (lines 302-321) to add Squawk context:
    - After asset creation, the post should be re-ingested into Squawk if content changed (`upsert_document_draft` with updated body including image references)
    - Run `scripts/build-squawk-index.js` after adding assets to see them in the index

  **Must NOT do**:
  - DO NOT restructure the existing doc — it's 379 lines and well-organized
  - DO NOT add Squawk asset tracking features (Squawk doesn't store assets)
  - DO NOT change the screenshot capture procedure sections
  - DO NOT remove any existing content

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Small, scoped additions to an existing doc — ~20-30 lines of new content
  - **Skills**: []
  - **Skills Evaluated but Omitted**:
    - `playwright`: Not performing browser tasks, just editing docs about Playwright

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 6, 9)
  - **Blocks**: Task 8
  - **Blocked By**: None

  **References**:

  **Pattern References**:
  - `docs/asset-creation-pipeline.md:1-8` — Existing header/purpose section. Insert new section after this.
  - `docs/asset-creation-pipeline.md:302-321` — Delegation Pattern section to update.

  **Content References**:
  - `docs/squawk-migration-process.md:206-229` — Rule 8: Asset Preview Column. This defines exactly how assets render in squawk-index.md.
  - `scripts/build-squawk-index.js:87-144` — `getAssetsPreview()` function. Shows exactly how assets are scanned and rendered.

  **WHY Each Reference Matters**:
  - Rule 8 defines the rendering contract — the asset pipeline doc should explain this so that post creators know what their assets will look like in the index.
  - The build script function shows the scanning logic — useful for the "no manual registration" explanation.

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: Pipeline Context section added
    Tool: Bash (grep)
    Steps:
      1. grep -c "Pipeline Context\|Lifecycle\|Post Pipeline" docs/asset-creation-pipeline.md → ≥ 1
      2. grep "post-pipeline.md" docs/asset-creation-pipeline.md → shows cross-reference
    Expected Result: New section exists with cross-reference
    Evidence: .sisyphus/evidence/task-2-pipeline-context.txt

  Scenario: Squawk Index Integration subsection added
    Tool: Bash (grep)
    Steps:
      1. grep -c "squawk-index\|Squawk Index\|build-squawk-index" docs/asset-creation-pipeline.md → ≥ 1
    Expected Result: Squawk index reference present
    Evidence: .sisyphus/evidence/task-2-squawk-integration.txt

  Scenario: Existing content preserved
    Tool: Bash (wc)
    Steps:
      1. wc -l docs/asset-creation-pipeline.md → ≥ 379 (original line count)
    Expected Result: File has grown, not shrunk
    Evidence: .sisyphus/evidence/task-2-content-preserved.txt
  ```

  **Commit**: YES (groups with Wave 1)
  - Message: `docs: create post-pipeline process doc and deprecate post-index.md`
  - Files: `docs/asset-creation-pipeline.md`

- [ ] 3. Rewrite `.claude/commands/new-post.md` — Squawk-First Post Creation

  **What to do**:
  - Rewrite the existing 256-line command to route through Squawk MCP instead of post-index.md. The overall structure (usage, examples, intake, tone guidance, file structure reference) stays the same. Key changes:

  **Post ID Generation (replaces Step 6)**:
  - Remove "Read post-index.md to find the next available ID"
  - Replace with: Scan `posts/2026/02/` directory names for highest existing B-### and T-### numbers, increment by 1
  - Pattern: `ls posts/2026/02/ | grep -oP '2026-[BT]-\d+' | sort | tail -1`
  - Fallback: If directory scan fails, query Squawk `list_review_queue` and parse `title` or item metadata for highest ID

  **Post Creation Checklist (replaces Step 9 and adds new steps)**:
  - Remove: "post-index.md updated with new row" and "post-index.md Next IDs incremented"
  - Add: Squawk ingestion steps (insert between file creation and XMind label):
    - **Step 9a**: Ingest into Squawk via `upsert_document_draft`:
      ```
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
      ```
    - **Step 9b**: Set expert and product on the post via `update_post_draft`:
      ```
      execute_tool("squawk.update_post_draft", {
        "postId": "<returned-post-cuid>",
        "expertId": "<expert-cuid>",
        "productId": "<product-cuid>"
      })
      ```
    - **Step 9c**: If post has dependencies, set dependency:
      ```
      execute_tool("squawk.update_post_draft", {
        "postId": "<returned-post-cuid>",
        "dependsOnPostId": "<dependency-post-cuid>"
      })
      ```
    - **Step 9d**: Verify ingestion: `execute_tool("squawk.get_content_item", {"id": "<document-cuid>", "itemType": "document"})`
    - **Step 9e**: Append CUID to build script mapping (or a separate `cuid-mapping.json`)

  **Metadata standard (update Step 7 / line 100-104)**:
  - Keep minimal metadata in post files: Post ID + CTA only
  - But the COMMAND passes full metadata via `referenceContext` params — audience, product, themes, expert come from the intake answers in Step 3
  - Update the metadata reference to point to `docs/post-pipeline.md` instead of AGENTS.md

  **Expert/Product CUID lookup**:
  - Add a lookup table section with Expert CUIDs and Product CUIDs (from `docs/squawk-migration-process.md:38-57`)
  - The command uses these CUIDs when calling `update_post_draft`

  **Squawk unavailability fallback**:
  - If Squawk MCP calls fail (timeout, connection error), the command should:
    1. Complete the post creation locally (folder, file, assets dir, XMind label)
    2. Log a warning: "⚠ Squawk ingestion failed. Run /update-post <post-id> to ingest later."
    3. Do NOT block the commit/push

  **Remove all post-index.md references**:
  - Remove Step 9 (update post-index.md), Step "Next IDs incremented"
  - Remove from the checklist: "post-index.md updated with new row"
  - Update the verification step to check Squawk instead of post-index.md

  **Must NOT do**:
  - DO NOT change the tone guidance section (lines 170-245) — it's excellent
  - DO NOT change the file structure reference (lines 247-256)
  - DO NOT change the XMind integration steps (Step 10) — they work correctly
  - DO NOT change the guided vs mindmap mode intake logic
  - DO NOT add post-index.md writes as a "backup"

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
    - Reason: Complex rewrite of a 256-line command with Squawk MCP integration, multiple steps, error handling
  - **Skills**: []
  - **Skills Evaluated but Omitted**:
    - `playwright`: Not a browser task
    - `git-master`: Not a git operation

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 4, 5, 7)
  - **Blocks**: Task 8
  - **Blocked By**: Tasks 1, 9

  **References**:

  **Pattern References**:
  - `.claude/commands/new-post.md` — THE file being rewritten. Read it entirely. Preserve lines 170-256 (tone guidance, file structure) verbatim. Modify lines 1-168 (checklist, instructions, steps).
  - `docs/squawk-migration-process.md:315-395` — Squawk MCP call patterns used during migration. Follow the same `execute_tool("squawk.<tool>", {...})` format.
  - `docs/squawk-migration-process.md:38-57` — Expert CUID and Product CUID lookup tables. Copy into the command.

  **API/Type References**:
  - `docs/squawk-migration-process.md:62-69` — Document vs Post data model. The command creates a Document (via upsert), which auto-creates a Post. Then update_post_draft sets metadata on the Post.

  **Content References**:
  - `docs/post-pipeline.md` (Task 1 output) — The process doc this command implements. Reference it for "see docs/post-pipeline.md for the full lifecycle."
  - `lsaProductExpertAlignment.md:16-24` — Master table for expert/product assignment.

  **WHY Each Reference Matters**:
  - The existing new-post.md is the base — preserve its structure, tone, and style while swapping the data backend.
  - Migration process patterns are battle-tested — the same MCP call format was used for 82 posts successfully.
  - Expert/Product CUIDs must be correct — these are live Squawk IDs that the command will use.

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: No post-index.md references remain
    Tool: Bash (grep)
    Steps:
      1. grep -c "post-index" .claude/commands/new-post.md → 0
    Expected Result: Zero references to post-index.md
    Failure Indicators: Any line containing "post-index"
    Evidence: .sisyphus/evidence/task-3-no-postindex.txt

  Scenario: Squawk ingestion steps present
    Tool: Bash (grep)
    Steps:
      1. grep -c "upsert_document_draft" .claude/commands/new-post.md → ≥ 1
      2. grep -c "update_post_draft" .claude/commands/new-post.md → ≥ 1
      3. grep -c "referenceContext" .claude/commands/new-post.md → ≥ 1
    Expected Result: All 3 Squawk tool references present
    Evidence: .sisyphus/evidence/task-3-squawk-ingestion.txt

  Scenario: Post ID generation uses directory scan
    Tool: Bash (grep)
    Steps:
      1. grep -c "posts/2026\|directory\|scan\|highest" .claude/commands/new-post.md → ≥ 1
      2. grep -v "post-index" .claude/commands/new-post.md | grep -c "Next ID\|next available" → shows directory-based approach
    Expected Result: Post ID generation references directory scanning, not post-index.md
    Evidence: .sisyphus/evidence/task-3-postid-gen.txt

  Scenario: Expert/Product CUID tables present
    Tool: Bash (grep)
    Steps:
      1. grep -c "cml8m3t3e00020ys4ml0dfbl8" .claude/commands/new-post.md → ≥ 1 (Keith's CUID)
      2. grep -c "cmksy89a7000367s4e634xb3k" .claude/commands/new-post.md → ≥ 1 (LSARS Product CUID)
    Expected Result: CUIDs embedded in the command
    Evidence: .sisyphus/evidence/task-3-cuid-tables.txt

  Scenario: Tone guidance preserved verbatim
    Tool: Bash (grep)
    Steps:
      1. grep -c "House voice" .claude/commands/new-post.md → 1
      2. grep -c "Artifact-first" .claude/commands/new-post.md → 1
      3. grep -c "Short, punchy paragraphs" .claude/commands/new-post.md → 1
    Expected Result: All tone guidance markers present
    Evidence: .sisyphus/evidence/task-3-tone-preserved.txt

  Scenario: Fallback for Squawk unavailability documented
    Tool: Bash (grep)
    Steps:
      1. grep -ci "fail\|fallback\|unavailable\|timeout" .claude/commands/new-post.md → ≥ 1
    Expected Result: Error handling guidance present
    Evidence: .sisyphus/evidence/task-3-fallback.txt
  ```

  **Commit**: YES (groups with Wave 2: Tasks 4, 5, 7)
  - Message: `commands: rewrite new-post, create update-post, update list-posts for Squawk pipeline`
  - Files: `.claude/commands/new-post.md`

- [ ] 4. Create `.claude/commands/update-post.md` — Replaces update-status.md

  **What to do**:
  - Create a new command file at `.claude/commands/update-post.md` that replaces the 22-line `update-status.md`
  - Delete `.claude/commands/update-status.md` after creating the replacement
  - The new command supports updating ANY post-level field through Squawk MCP, not just status

  **Command structure**:
  ```
  # Update Post
  
  Update any post-level field through Squawk MCP.
  
  ## Usage
  /update-post <post-id> <field> <value>
  
  ## Examples
  - /update-post 2026-B-001 status approved
  - /update-post 2026-T-013 expert "Mike, Keith"
  - /update-post 2026-B-006 product "LSARS, HSRA"
  - /update-post 2026-B-014 themes "DASHBOARD_ACCOUNTABILITY, COMMUNITY_TRANSPARENCY"
  - /update-post 2026-T-001 depends-on 2026-B-001
  ```

  **Supported fields and their Squawk MCP routing**:

  | Field | Squawk Tool | Parameter | Notes |
  |-------|------------|-----------|-------|
  | `status` | Conditional | See below | Maps status values to Squawk actions |
  | `expert` | `update_post_draft` | `expertId` | Resolve name → CUID from lookup table |
  | `product` | `update_post_draft` | `productId` | Resolve name → CUID from lookup table |
  | `themes` | `upsert_document_draft` | `referenceContext.themes` | Re-ingest with updated themes |
  | `depends-on` | `update_post_draft` | `dependsOnPostId` | Resolve target post ID → CUID |
  | `content` | `upsert_document_draft` | (re-ingest) | Re-ingest the post file to update extracted text |

  **Status transitions (with readiness gate — Rule 7)**:

  | Status Value | Squawk Action | Precondition |
  |-------------|--------------|--------------|
  | `draft` | No Squawk action (local only) | — |
  | `in_review` | No Squawk action | — |
  | `approved` | `approve_content_item` | `readinessScore` MUST be `ready`. If not ready, REJECT with message. |
  | `published` | No Squawk action | Must already be `APPROVED` |

  **Readiness gate enforcement**:
  ```
  Before calling approve_content_item:
  1. Call get_content_item for the document
  2. Check readinessScore
  3. If readinessScore ≠ "ready" → REFUSE with: "Cannot approve: readiness is '{score}'. Address readiness issues first."
  4. If readinessScore = "ready" → proceed with approve_content_item
  ```

  **CUID resolution**:
  - The command needs to resolve human-readable post ID (e.g., `2026-B-001`) to Squawk document CUID
  - Use the CUID mapping from `scripts/build-squawk-index.js:15-37` (hardcoded table)
  - Or query `list_review_queue` and search by title match
  - Include Expert CUID and Product CUID lookup tables (same as in new-post.md)

  **Post-update actions**:
  - After any update, suggest running `scripts/build-squawk-index.js` to refresh the index
  - After status change, verify with `get_content_item`

  **Must NOT do**:
  - DO NOT write to post-index.md
  - DO NOT write to the post markdown file (except for `content` updates that re-read the file)
  - DO NOT approve items with readinessScore ≠ `ready` (readiness gate)
  - DO NOT implement publication/push actions
  - DO NOT support batch updates (one post at a time)

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
    - Reason: New command creation with Squawk MCP routing, readiness gate logic, CUID resolution
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 3, 5, 7)
  - **Blocks**: Task 8
  - **Blocked By**: Tasks 1, 9

  **References**:

  **Pattern References**:
  - `.claude/commands/update-status.md` — The file being replaced. Understand what it does, then create the broader replacement.
  - `.claude/commands/new-post.md` (Task 3 output) — Follow the same Squawk MCP invocation patterns.
  - `docs/squawk-migration-process.md:165-177` — Readiness gate rule (Rule 7). This is the authoritative reference for approval preconditions.

  **API/Type References**:
  - `docs/squawk-migration-process.md:38-57` — Expert and Product CUID lookup tables.
  - `docs/squawk-migration-process.md:96-108` — Status mapping table (post-index status → Squawk review status).
  - `scripts/build-squawk-index.js:15-37` — Hardcoded CUID mapping for post ID → document CUID resolution.

  **WHY Each Reference Matters**:
  - update-status.md shows what the OLD command did — the new one is a superset.
  - Readiness gate is the most critical logic — approval without checking readiness would violate Rule 7.
  - CUID mapping is essential — without it, the command can't resolve human-readable IDs to Squawk IDs.

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: update-post.md exists and update-status.md is deleted
    Tool: Bash (test)
    Steps:
      1. test -f .claude/commands/update-post.md → exists
      2. test ! -f .claude/commands/update-status.md → does not exist
    Expected Result: New file exists, old file deleted
    Evidence: .sisyphus/evidence/task-4-file-swap.txt

  Scenario: All supported fields documented
    Tool: Bash (grep)
    Steps:
      1. grep -c "status\|expert\|product\|themes\|depends-on\|content" .claude/commands/update-post.md → ≥ 6
    Expected Result: All 6 field types referenced
    Evidence: .sisyphus/evidence/task-4-fields.txt

  Scenario: Readiness gate enforcement documented
    Tool: Bash (grep)
    Steps:
      1. grep -c "readiness\|readinessScore\|ready" .claude/commands/update-post.md → ≥ 2
      2. grep -c "REFUSE\|Cannot approve\|reject" .claude/commands/update-post.md → ≥ 1
    Expected Result: Readiness gate logic present with rejection message
    Evidence: .sisyphus/evidence/task-4-readiness-gate.txt

  Scenario: No post-index.md references
    Tool: Bash (grep)
    Steps:
      1. grep -c "post-index" .claude/commands/update-post.md → 0
    Expected Result: Zero references
    Evidence: .sisyphus/evidence/task-4-no-postindex.txt

  Scenario: Squawk MCP tools referenced correctly
    Tool: Bash (grep)
    Steps:
      1. grep -c "update_post_draft" .claude/commands/update-post.md → ≥ 1
      2. grep -c "approve_content_item" .claude/commands/update-post.md → ≥ 1
      3. grep -c "get_content_item" .claude/commands/update-post.md → ≥ 1
    Expected Result: All 3 key tools referenced
    Evidence: .sisyphus/evidence/task-4-squawk-tools.txt
  ```

  **Commit**: YES (groups with Wave 2)
  - Message: `commands: rewrite new-post, create update-post, update list-posts for Squawk pipeline`
  - Files: `.claude/commands/update-post.md`, `.claude/commands/update-status.md` (delete)

- [ ] 5. Rewrite `.claude/commands/list-posts.md` — Dual Mode

  **What to do**:
  - Rewrite the 27-line command to support two modes:
    1. **Default mode**: Parse `squawk-index.md` to list posts with their metadata
    2. **Live mode** (`--live` flag): Query Squawk MCP `list_review_queue` directly

  **Default mode (squawk-index.md)**:
  ```
  /list-posts [status] [--live]
  ```
  - Parse the squawk-index.md markdown table
  - Extract columns: Post ID, Title, Review Status, Readiness, Audience, Product, Expert
  - If status filter provided, filter by Review Status column
  - Display in readable format with alignment

  **Live mode (--live flag)**:
  ```
  /list-posts --live [status]
  ```
  - Call `execute_tool("squawk.list_review_queue", {"includeApproved": true, "limit": 100})`
  - Parse response items for: title, reviewStatus, readinessScore
  - If status filter provided, filter by reviewStatus
  - Display in readable format
  - Note: 100-item limit — if response has exactly 100 items, warn that results may be truncated

  **Valid status filters**:
  - Default mode: `PENDING_REVIEW`, `APPROVED`, `PUBLISHED` (matches squawk-index.md values)
  - Live mode: Same values (from Squawk API)
  - Also accept lowercase variants: `pending`, `approved`, `published`

  **Output format**:
  ```
  Posts (82 total, showing: all)
  
  | Post ID    | Title                              | Status         | Readiness  | Product |
  |------------|-------------------------------------|----------------|------------|---------|
  | 2026-B-001 | Trust Through Auditable AI          | APPROVED       | ready      | LSARS   |
  | ...        | ...                                 | ...            | ...        | ...     |
  ```

  **Must NOT do**:
  - DO NOT read from post-index.md
  - DO NOT read from individual post files (the old approach)
  - DO NOT modify squawk-index.md
  - DO NOT implement pagination for --live mode beyond the 100-item limit warning

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Small, well-scoped rewrite of a 27-line file with clear requirements
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 3, 4, 7)
  - **Blocks**: Task 8
  - **Blocked By**: Task 1

  **References**:

  **Pattern References**:
  - `.claude/commands/list-posts.md` — The file being rewritten. Current structure to follow.
  - `squawk-index.md:1-10` — The table format that default mode will parse (15-column header).

  **API/Type References**:
  - `docs/squawk-migration-process.md:28` — `list_review_queue` tool reference.

  **WHY Each Reference Matters**:
  - The existing command sets the expected UX (usage, examples, output format).
  - squawk-index.md defines the parsing target for default mode.

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: Command supports both modes
    Tool: Bash (grep)
    Steps:
      1. grep -c "\-\-live" .claude/commands/list-posts.md → ≥ 2
      2. grep -c "squawk-index" .claude/commands/list-posts.md → ≥ 1
      3. grep -c "list_review_queue" .claude/commands/list-posts.md → ≥ 1
    Expected Result: Both modes documented
    Evidence: .sisyphus/evidence/task-5-dual-mode.txt

  Scenario: No post-index.md or filesystem scanning references
    Tool: Bash (grep)
    Steps:
      1. grep -c "post-index\|post.md\|posts/ directory" .claude/commands/list-posts.md → 0
    Expected Result: No references to old data sources
    Evidence: .sisyphus/evidence/task-5-no-old-sources.txt
  ```

  **Commit**: YES (groups with Wave 2)
  - Message: `commands: rewrite new-post, create update-post, update list-posts for Squawk pipeline`
  - Files: `.claude/commands/list-posts.md`

- [ ] 6. Update `.claude/commands/README.md` — Command Listing

  **What to do**:
  - Update the README to reflect the renamed/new commands:
    - `/new-post` — Create a new marketing post (unchanged name)
    - `/update-post` — Update post metadata and status via Squawk (NEW — replaces `/update-status`)
    - `/list-posts` — List all posts from squawk-index or Squawk MCP (updated description)
    - `/update-mindmap-node` — Update XMind mind map nodes (unchanged)
  - Remove reference to `/update-status`
  - Add brief note: "All post commands route through Squawk MCP. See `docs/post-pipeline.md` for the full content lifecycle."

  **Must NOT do**:
  - DO NOT change the "Adding New Commands" section structure
  - DO NOT add commands that don't exist

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Trivial 5-line edit to an existing README
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 9)
  - **Blocks**: Task 8
  - **Blocked By**: None

  **References**:

  **Pattern References**:
  - `.claude/commands/README.md` — The file being edited. 27 lines.

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: README lists correct commands
    Tool: Bash (grep)
    Steps:
      1. grep -c "update-post" .claude/commands/README.md → ≥ 1
      2. grep -c "update-status" .claude/commands/README.md → 0
      3. grep -c "new-post" .claude/commands/README.md → ≥ 1
      4. grep -c "list-posts" .claude/commands/README.md → ≥ 1
    Expected Result: New command listed, old command removed
    Evidence: .sisyphus/evidence/task-6-readme.txt
  ```

  **Commit**: YES (groups with Wave 1)
  - Message: `docs: create post-pipeline process doc and deprecate post-index.md`
  - Files: `.claude/commands/README.md`

- [ ] 7. Update `scripts/build-squawk-index.js` — Handle New Posts

  **What to do**:
  - The build script currently reads post-index.md (lines 39-60) for audience, product, expert, dependencies, and relationship data. With post-index.md deprecated, new posts created after this change won't be in post-index.md.
  - **Phase 1 (this task)**: Make the script robust to missing post-index entries. For posts NOT in post-index.md, read the supplementary data from the MCP cache JSON instead (where available in the Squawk response fields).
  - **Phase 2 (future, not this task)**: Fully remove post-index.md dependency.

  **Specific changes**:

  1. **CUID mapping growth**: The hardcoded mapping table (lines 16-36) only has 82 entries. For new posts:
     - Add logic to dynamically discover post IDs from the MCP cache items that aren't in the hardcoded mapping
     - Each MCP item has metadata that may contain the human-readable post ID (check `referenceContext.postId` or `title` for the post ID pattern `2026-[BT]-\d+`)
     - Fallback: If a new post can't be mapped, log a warning and skip it

  2. **Squawk data fallback for missing post-index entries**:
     - Currently: `const pi = postIndex[pid] || {};` — if post isn't in post-index, all fields are empty
     - Change to: If `pi` is empty/missing AND the MCP item has the field, use the MCP value
     - Fields to extract from MCP items (check what `list_review_queue` returns):
       - `audience` → from extraction or item metadata
       - `product` → from extraction or item metadata
       - `expert` → from item metadata
       - `dependsOn` → resolve from `dependsOnPostId` if present
       - `relationship` → from referenceContext or item metadata
     - If neither post-index nor MCP has the field → show `—`

  3. **Dynamic date in header**: Change the hardcoded "Last rebuilt: 2026-02-21" to `new Date().toISOString().slice(0, 10)`

  4. **Keep backward compatibility**: The script should still work with the existing post-index.md present. It just won't fail if post-index.md entries are missing for new posts.

  **Must NOT do**:
  - DO NOT rewrite the entire script — only modify data source fallback logic
  - DO NOT change the asset preview logic (`getAssetsPreview`)
  - DO NOT change the markdown rendering format (columns, header, escaping)
  - DO NOT remove the post-index.md parsing — just make it optional/fallback
  - DO NOT add live Squawk MCP calls — keep using the cached JSON approach

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
    - Reason: Script modification requiring understanding of Squawk API response format and data resolution logic
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 2 (with Tasks 3, 4, 5)
  - **Blocks**: Task 8
  - **Blocked By**: Task 9

  **References**:

  **Pattern References**:
  - `scripts/build-squawk-index.js` — THE file being modified. Read entirely. Focus on lines 39-60 (post-index parsing), lines 146-169 (row building).
  - `scripts/build-squawk-index.js:87-144` — Asset preview logic. DO NOT MODIFY.
  - `scripts/build-squawk-index.js:15-37` — Hardcoded CUID mapping. Supplement, don't replace.

  **API/Type References**:
  - The cached MCP JSON at the path in `process.argv[2]` — Examine its structure to understand what fields are available per item.

  **WHY Each Reference Matters**:
  - The build script IS the deliverable — understanding every line is essential for a safe modification.
  - The MCP cache structure determines what fallback fields are available.

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: Script runs successfully with current data
    Tool: Bash
    Preconditions: Current cached MCP JSON and post-index.md exist
    Steps:
      1. PATH="/Users/idengrenme/.local/share/fnm/node-versions/v20.19.5/installation/bin:$PATH" node scripts/build-squawk-index.js
      2. Check output: "Wrote 82 rows to squawk-index.md"
    Expected Result: 82 rows generated without errors
    Evidence: .sisyphus/evidence/task-7-build-success.txt

  Scenario: Dynamic date in header
    Tool: Bash (grep)
    Steps:
      1. Run the script
      2. head -5 squawk-index.md | grep "Last rebuilt"
    Expected Result: Date matches today's date, not hardcoded "2026-02-21"
    Evidence: .sisyphus/evidence/task-7-dynamic-date.txt

  Scenario: Script handles missing post-index entry gracefully
    Tool: Bash
    Steps:
      1. Temporarily add a fake entry to the CUID mapping with a CUID that exists in the MCP cache
      2. Run the script
      3. Verify the row is generated (even without a post-index entry)
    Expected Result: Row generated with available data, "—" for missing fields
    Evidence: .sisyphus/evidence/task-7-missing-entry.txt
  ```

  **Commit**: YES (groups with Wave 2)
  - Message: `commands: rewrite new-post, create update-post, update list-posts for Squawk pipeline`
  - Files: `scripts/build-squawk-index.js`

- [ ] 8. Update `AGENTS.md` — Squawk as Source of Truth

  **What to do**:
  - Comprehensive update to AGENTS.md (currently 155 lines). This is the LAST implementation task because it references all other deliverables.

  **Section-by-section changes**:

  1. **Header**: Update "Last Updated" date to today.

  2. **STRUCTURE section** (lines 10-18): Replace file tree with:
     ```
     .
     ├── posts/                          # Marketing blog posts (82 posts)
     ├── docs/
     │   ├── post-pipeline.md            # End-to-end content lifecycle process
     │   ├── asset-creation-pipeline.md  # Playwright screenshot & asset procedures
     │   ├── squawk-migration-process.md # Migration reference (completed)
     │   └── mindmaps/                   # XMind source material
     ├── scripts/
     │   ├── build-squawk-index.js       # Rebuild squawk-index.md from Squawk MCP
     │   └── update_xmind_labels.py      # Apply post ID labels to XMind nodes
     ├── assetpipe/                      # Reusable Playwright capture scripts
     ├── squawk-index.md                 # Auto-generated index (DO NOT EDIT)
     ├── post-index.md                   # DEPRECATED — archived, read-only
     ├── marketingCampaignFeb2026.md     # Current campaign organizing doc
     └── lsaProductExpertAlignment.md    # Expert/product alignment reference
     ```

  3. **RULES section** (lines 22-28): Add Squawk-first rule:
     | Rule | Description |
     |------|-------------|
     | **SQUAWK FIRST** | All post metadata reads/writes go through Squawk MCP. `squawk-index.md` is a derived artifact, never edited manually. |
     | **CONTEXT7 FIRST** | Tech research starts with Context7 (via lazy-mcp proxy), not web search. |
     | **CONSISTENT VOICE** | Maintain LSA Digital brand voice across all content. |

  4. **POST METADATA GUIDELINES section** (lines 31-93): Major rewrite.
     - Change "All authoritative metadata lives in `squawk-index.md`" → "All authoritative metadata lives in **Squawk MCP**. `squawk-index.md` is a derived view rebuilt from Squawk on each sync."
     - Keep the post file structure example (Post ID + CTA) — this is CORRECT for minimal metadata
     - Change the "Authoritative Source" subsection:
       - Remove "**post-index.md** is the single source of truth for..."
       - Replace with: "**Squawk MCP** is the single source of truth for: Status tracking (reviewStatus), Dependencies (dependsOnPostId), Theme tags (declaredThemes), Product assignments (productId), Expert assignments (expertId), Audience targeting (extraction.audience), Readiness assessment (readinessScore, readinessSummary)"
       - Add: "`squawk-index.md` is a read-only derived view rebuilt by `scripts/build-squawk-index.js`"
       - Add: "`post-index.md` is **DEPRECATED** — kept as a read-only archive only"

  5. **MCP TOOLS section** (lines 96-133): Add Squawk to the tool categories table:
     | Category | Tools | Use For | When |
     |----------|-------|---------|------|
     | `squawk` | 12 | Post ingestion, metadata, review, approval | Content pipeline |
     - Add a Squawk subsection with key tools: upsert_document_draft, update_post_draft, approve_content_item, list_review_queue, get_content_item
     - Update the config reference: "6 servers" instead of "5 servers"

  6. **AGENTS section** (lines 137-145): No change needed.

  7. **Changelog** (lines 149-155): Add new entry:
     | Date | Author | Change |
     |------|--------|--------|
     | 2026-02-20 | Sisyphus | Post-pipeline implementation: Squawk is sole SoT, post-index.md deprecated, commands updated, docs/post-pipeline.md created. |

  8. **NEW SECTION: Content Pipeline Quick Reference** (add before Changelog):
     - Brief summary: "For the full content lifecycle, see `docs/post-pipeline.md`"
     - Commands: `/new-post`, `/update-post`, `/list-posts`
     - Index rebuild: `node scripts/build-squawk-index.js [mcp-cache-path]`

  **Must NOT do**:
  - DO NOT remove the Citations / Sources section — it's still valid
  - DO NOT change the Technology Questions pattern (Context7 first)
  - DO NOT change the AGENTS table (models/agents are correct)
  - DO NOT reference post-index.md as a source of truth anywhere

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
    - Reason: Comprehensive multi-section update requiring understanding of all other deliverables
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Wave 3 (sequential — depends on all Wave 1+2 tasks)
  - **Blocks**: F1-F4
  - **Blocked By**: Tasks 1, 2, 3, 4, 5, 6, 7, 9

  **References**:

  **Pattern References**:
  - `AGENTS.md` — THE file being modified. Read entirely. Preserve structure and style.

  **Content References**:
  - `docs/post-pipeline.md` (Task 1 output) — Referenced in the new Quick Reference section.
  - `.claude/commands/new-post.md` (Task 3 output) — Command name for reference section.
  - `.claude/commands/update-post.md` (Task 4 output) — Command name for reference section.
  - `.claude/commands/list-posts.md` (Task 5 output) — Command name for reference section.
  - `docs/squawk-migration-process.md:19-34` — Squawk MCP tool table to reference.

  **WHY Each Reference Matters**:
  - AGENTS.md is THE knowledge base for all agents working in this repo. Inaccurate information here cascades to every future task.
  - The deliverables from other tasks define what AGENTS.md should reference.

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: No contradictions about source of truth
    Tool: Bash (grep)
    Steps:
      1. grep -i "source of truth" AGENTS.md → should only mention Squawk MCP
      2. grep -i "source of truth" AGENTS.md | grep -i "post-index" → empty
    Expected Result: Squawk is the only SoT mentioned
    Evidence: .sisyphus/evidence/task-8-sot-consistency.txt

  Scenario: File tree includes all new files
    Tool: Bash (grep)
    Steps:
      1. grep -c "post-pipeline.md" AGENTS.md → ≥ 1
      2. grep -c "squawk-index.md" AGENTS.md → ≥ 1
      3. grep -c "build-squawk-index" AGENTS.md → ≥ 1
      4. grep -c "assetpipe" AGENTS.md → ≥ 1
      5. grep -c "DEPRECATED" AGENTS.md → ≥ 1 (post-index.md entry)
    Expected Result: All 5 file references present
    Evidence: .sisyphus/evidence/task-8-file-tree.txt

  Scenario: Squawk in MCP tools table
    Tool: Bash (grep)
    Steps:
      1. grep -c "squawk" AGENTS.md → ≥ 3 (table row + mentions)
      2. grep "squawk.*12\|12.*squawk" AGENTS.md → ≥ 1 (12 tools)
    Expected Result: Squawk listed with 12 tools
    Evidence: .sisyphus/evidence/task-8-squawk-tools.txt

  Scenario: SQUAWK FIRST rule present
    Tool: Bash (grep)
    Steps:
      1. grep -c "SQUAWK FIRST" AGENTS.md → ≥ 1
    Expected Result: Rule exists
    Evidence: .sisyphus/evidence/task-8-squawk-rule.txt

  Scenario: Changelog updated
    Tool: Bash (grep)
    Steps:
      1. grep "2026-02" AGENTS.md | grep -c "post-pipeline\|deprecated\|Squawk" → ≥ 1
    Expected Result: New changelog entry present
    Evidence: .sisyphus/evidence/task-8-changelog.txt
  ```

  **Commit**: YES (Wave 3 — separate commit)
  - Message: `agents: update AGENTS.md for Squawk-first content workflow`
  - Files: `AGENTS.md`

- [ ] 9. Deprecate `post-index.md` — Add Banner + Find All References

  **What to do**:
  - **Step 1**: Add a deprecation banner at the top of `post-index.md`:
    ```markdown
    > **⚠ DEPRECATED** — This file is no longer maintained. All post metadata now lives in **Squawk MCP**.
    > 
    > - To view posts: `squawk-index.md` (auto-generated) or `/list-posts`
    > - To update posts: `/update-post <post-id> <field> <value>`
    > - For the full content lifecycle: `docs/post-pipeline.md`
    > 
    > This file is kept as a read-only archive for historical reference.
    ```
    Insert this BEFORE the `# Post Index` heading.

  - **Step 2**: Search the ENTIRE codebase for all references to `post-index.md` and classify each:

    | Reference Location | Action |
    |-------------------|--------|
    | `.claude/commands/new-post.md` | Updated in Task 3 (removes post-index writes) |
    | `.claude/commands/update-status.md` | Deleted in Task 4 (replaced by update-post.md) |
    | `.claude/commands/list-posts.md` | Updated in Task 5 (reads squawk-index.md instead) |
    | `AGENTS.md` | Updated in Task 8 (marks deprecated) |
    | `scripts/build-squawk-index.js` | Updated in Task 7 (optional fallback) |
    | `docs/squawk-migration-process.md` | NO CHANGE — historical reference, kept as-is |
    | `docs/post-pipeline.md` (Task 1) | Will reference deprecation in its deprecation section |

  - **Step 3**: Use `grep -r "post-index" --include="*.md" --include="*.js" --include="*.py"` to find any references NOT listed above. For each:
    - If it's in a file being modified by another task → note it's covered
    - If it's in an unplanned file → add a note about what to do

  **Must NOT do**:
  - DO NOT delete post-index.md
  - DO NOT modify the table content (keep all 82 rows intact)
  - DO NOT modify any other files — just post-index.md itself + the reference audit

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Simple banner insertion + grep audit
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Tasks 1, 2, 6)
  - **Blocks**: Tasks 3, 4, 7, 8
  - **Blocked By**: None

  **References**:

  **Pattern References**:
  - `post-index.md:1-5` — Where to insert the deprecation banner (before the heading).

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: Deprecation banner present
    Tool: Bash (grep)
    Steps:
      1. head -10 post-index.md | grep -c "DEPRECATED" → ≥ 1
      2. head -10 post-index.md | grep -c "Squawk MCP" → ≥ 1
    Expected Result: Banner visible at top of file
    Evidence: .sisyphus/evidence/task-9-banner.txt

  Scenario: All post-index.md references catalogued
    Tool: Bash (grep)
    Steps:
      1. grep -r "post-index" --include="*.md" --include="*.js" --include="*.py" -l | sort
      2. Compare output against the planned reference table
    Expected Result: All references accounted for (either updated by other tasks or noted as historical)
    Evidence: .sisyphus/evidence/task-9-references.txt

  Scenario: Table content preserved
    Tool: Bash (wc + grep)
    Steps:
      1. wc -l post-index.md → ≥ 140 (original had 140 lines)
      2. grep -c "2026-B-001" post-index.md → 1 (first row still exists)
      3. grep -c "2026-T-045" post-index.md → 1 (last row still exists)
    Expected Result: All original content intact
    Evidence: .sisyphus/evidence/task-9-content-preserved.txt
  ```

  **Commit**: YES (groups with Wave 1)
  - Message: `docs: create post-pipeline process doc and deprecate post-index.md`
  - Files: `post-index.md`

---

## Final Verification Wave (MANDATORY — after ALL implementation tasks)

> 4 review agents run in PARALLEL. ALL must APPROVE. Rejection → fix → re-run.

- [ ] F1. **Plan Compliance Audit** — `oracle`
  Read the plan end-to-end. For each "Must Have": verify implementation exists (read file, check content). For each "Must NOT Have": search codebase for forbidden patterns — reject with file:line if found. Check evidence files exist in .sisyphus/evidence/. Compare deliverables against plan.
  Output: `Must Have [N/N] | Must NOT Have [N/N] | Tasks [N/N] | VERDICT: APPROVE/REJECT`

- [ ] F2. **Content Quality Review** — `unspecified-high`
  Read ALL modified/created files. Check for: dead references to post-index.md as SoT, inconsistent Squawk tool names, wrong file paths, contradictory instructions between commands. Verify all Squawk MCP tool invocation patterns match the format from `docs/squawk-migration-process.md:315-395`. Check for AI slop: vague instructions, missing concrete examples, hand-wavy steps.
  Output: `Files [N clean/N issues] | Dead Refs [N found] | Consistency [PASS/FAIL] | VERDICT`

- [ ] F3. **Cross-Reference Integrity Check** — `unspecified-high`
  Verify every cross-reference between files resolves: post-pipeline.md → asset-creation-pipeline.md, new-post.md → post-pipeline.md, AGENTS.md → all referenced files in file tree, README.md → all command files. Search for ALL remaining references to "post-index.md" across the codebase — any reference calling it "source of truth" or "master" is a REJECT.
  Output: `Cross-refs [N/N valid] | Dead post-index refs [N found] | VERDICT`

- [ ] F4. **Scope Fidelity Check** — `deep`
  For each task: read "What to do", read actual file changes. Verify 1:1 — everything in spec was built (no missing), nothing beyond spec was built (no creep). Check "Must NOT do" compliance. Verify no post files in `posts/` were modified. Verify no new commands beyond the 3 specified. Verify squawk-migration-process.md was NOT modified.
  Output: `Tasks [N/N compliant] | Creep [CLEAN/N issues] | Forbidden [CLEAN/N violations] | VERDICT`

---

## Commit Strategy

- **Wave 1**: `docs: create post-pipeline process doc and deprecate post-index.md` — docs/post-pipeline.md, docs/asset-creation-pipeline.md, post-index.md, .claude/commands/README.md
- **Wave 2**: `commands: rewrite new-post, create update-post, update list-posts for Squawk pipeline` — .claude/commands/new-post.md, .claude/commands/update-post.md, .claude/commands/update-status.md (delete), .claude/commands/list-posts.md, scripts/build-squawk-index.js
- **Wave 3**: `agents: update AGENTS.md for Squawk-first content workflow` — AGENTS.md

---

## Success Criteria

### Verification Commands
```bash
# Verify all deliverables exist
ls -la docs/post-pipeline.md docs/asset-creation-pipeline.md .claude/commands/new-post.md .claude/commands/update-post.md .claude/commands/list-posts.md .claude/commands/README.md AGENTS.md scripts/build-squawk-index.js

# Verify update-status.md is deleted
test ! -f .claude/commands/update-status.md && echo "DELETED" || echo "STILL EXISTS"

# Verify post-index.md has deprecation banner
head -5 post-index.md  # Should show deprecation notice

# Verify no file references post-index.md as "source of truth"
grep -r "source of truth" --include="*.md" -l | xargs grep -l "post-index"  # Should be empty or only post-index.md itself

# Verify AGENTS.md references Squawk
grep -c "Squawk" AGENTS.md  # Should be > 0
grep -c "squawk-index.md" AGENTS.md  # Should be > 0
```

### Final Checklist
- [ ] All "Must Have" present
- [ ] All "Must NOT Have" absent
- [ ] All 9 files modified/created as specified
- [ ] No post files in posts/ modified
- [ ] No references to post-index.md as SoT remain (except in squawk-migration-process.md which is historical)
