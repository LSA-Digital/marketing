# Squawk-Index Updates: Readiness Gate, Column Pruning, Assets Preview

## TL;DR

> **Quick Summary**: Three updates to the squawk-index system — add a readiness gate rule to the process doc, remove 5 low-value columns, and add an Assets Preview column with inline thumbnails/links. Also move the build script from /tmp into the repo.
> 
> **Deliverables**:
> - Updated `docs/squawk-migration-process.md` with readiness gate rule, column exclusion spec, and asset preview rendering rules
> - Regenerated `squawk-index.md` with 15 columns (was 19: removed 5, added 1)
> - Build script moved to `scripts/build-squawk-index.js` in the repo
> 
> **Estimated Effort**: Short
> **Parallel Execution**: YES - 2 waves
> **Critical Path**: Task 1 (process doc) → Task 2 (build script + regenerate)

---

## Context

### Original Request
Three changes to the squawk-index system:
1. Add readiness gate rule: Review Status should not be APPROVED until readiness = "ready" (process doc only, no Squawk MCP changes)
2. Remove 5 columns from squawk-index.md: Squawk CUID, Doc Status, Critical, Posts, Published
3. Add an "Assets Preview" column with inline thumbnails for images, links for PDFs, `<video>` tags for videos

### Interview Summary
**Key Discussions**:
- User decided NOT to un-approve the 20 currently APPROVED-but-not-ready items in Squawk — rule is for future enforcement only
- User views markdown in Markdown Preview Enhanced (VS Code webview) which supports HTML `<img>`, `<video>`, and `<iframe>` tags
- squawk-index.md is auto-generated from scratch each sync — never hand-edited

**Research Findings**:
- 12 Squawk MCP tools — no "unapprove" or "set_review_status" tool exists
- 51 asset files across 26 posts: 47 PNG, 4 PDF, 0 video
- 22 posts have assets dirs with ONLY README.md (not real assets) — must be excluded
- 34 posts have no assets dir at all
- Build script at `/tmp/build-squawk-index.js` reads cached MCP JSON + post-index.md — volatile location, hardcoded paths

### Metis Review
**Identified Gaps** (addressed):
- Build script is in `/tmp` (volatile) with hardcoded MCP cache path — moved to repo as part of this plan
- Process doc Rule 4 lists removed columns as "Do Not Touch" — will be reconciled
- Summary Table (line 167) references removed columns — will be updated
- README.md files in asset dirs must be excluded from scanning
- Multi-asset posts (up to 4 PNGs) need size constraints to prevent table blowout

---

## Work Objectives

### Core Objective
Update the squawk-index rendering pipeline: add a readiness gate rule, slim down the table, and add visual asset previews.

### Concrete Deliverables
- `docs/squawk-migration-process.md` — updated with 3 new/amended rules
- `squawk-index.md` — regenerated with 15 columns (removed 5, added 1 Assets Preview)
- `scripts/build-squawk-index.js` — build script moved from /tmp into repo, updated with column changes + asset scanning

### Definition of Done
- [ ] `squawk-index.md` has exactly 15 columns (verify: count `|` in header)
- [ ] Columns Squawk CUID, Doc Status, Critical, Posts, Published are absent
- [ ] Assets Preview column present with `<img>` tags for PNGs, links for PDFs
- [ ] Process doc contains readiness gate rule
- [ ] Process doc column references are consistent (no mentions of removed columns as rendered)
- [ ] Build script is at `scripts/build-squawk-index.js` and runs successfully

### Must Have
- Readiness gate rule in process doc (future enforcement)
- 5 columns removed from squawk-index.md rendering
- Assets Preview column with inline thumbnails
- Build script in repo (not /tmp)

### Must NOT Have (Guardrails)
- NO MCP calls to change review status (user explicitly deferred)
- NO hand-editing squawk-index.md directly — all changes via build script
- NO Title linkification (Rule 6) — out of scope
- NO build script modernization beyond the 3 stated changes (no CLI args, no error handling improvements)
- NO asset metadata enrichment (file sizes, dimensions, alt text)
- DO NOT include README.md files from assets dirs in the preview column
- DO NOT expand beyond the 3 stated changes

---

## Verification Strategy

> **ZERO HUMAN INTERVENTION** — ALL verification is agent-executed. No exceptions.

### Test Decision
- **Infrastructure exists**: NO (not a code project)
- **Automated tests**: None
- **Framework**: N/A

### QA Policy
Every task MUST include agent-executed QA scenarios.
Evidence saved to `.sisyphus/evidence/task-{N}-{scenario-slug}.{ext}`.

- **Markdown validation**: Bash — count columns, grep for removed/added content
- **Build script**: Bash — run script, verify output
- **Process doc**: Bash — grep for rule text, verify consistency

---

## Execution Strategy

### Parallel Execution Waves

```
Wave 1 (Start Immediately — process doc + build script):
├── Task 1: Update process doc (readiness gate + column exclusion + asset preview rules) [quick]
├── Task 2: Move build script to repo + update for column/asset changes [unspecified-high]

Wave 2 (After Wave 1 — regenerate):
├── Task 3: Regenerate squawk-index.md from updated build script [quick]

Wave FINAL (After ALL tasks):
├── Task F1: Verify squawk-index.md columns and content [quick]
```

### Dependency Matrix

| Task | Depends On | Blocks |
|------|-----------|--------|
| 1 | — | F1 |
| 2 | — | 3 |
| 3 | 2 | F1 |
| F1 | 1, 3 | — |

### Agent Dispatch Summary

- **Wave 1**: 2 tasks — T1 → `quick`, T2 → `unspecified-high`
- **Wave 2**: 1 task — T3 → `quick`
- **FINAL**: 1 task — F1 → `quick`

---

## TODOs

- [ ] 1. Update Migration Process Doc

  **What to do**:
  - Add **Rule 7: Readiness Gate** (or amend Rule 2 status mapping table): "Do NOT call `approve_content_item` for any document where `readinessScore` ≠ `ready`. Items with `needs_work` or empty readiness MUST remain `PENDING_REVIEW` regardless of post-index status. This is a pre-approval check, not a post-hoc correction."
  - Update **Rule 4** ("Do Not Touch" fields): Remove Doc Status, Critical, Posts, Published from the rendered-columns context. These fields still exist in Squawk and are still maintained by Squawk, but they are **excluded from squawk-index.md rendering**. Keep Repost By, Updated, Readiness Score, Readiness Notes as rendered columns.
  - Update **Summary Table** (around line 160): Adjust entries 6 (Do not touch) and add entry for column exclusion.
  - Add **new section or rule**: "Excluded Columns" — Squawk CUID, Doc Status, Critical, Posts count, Published count are available in Squawk but excluded from squawk-index.md for readability. They can be queried via `get_content_item` or `list_review_queue` when needed.
  - Add **Asset Preview rendering spec**: Document how the Assets Preview column is generated:
    - Scan `posts/2026/02/*_{postId}_*/assets/` for files
    - Exclude README.md and .DS_Store
    - PNG/JPG/GIF/SVG → `<img src="{relative_path}" width="60">`
    - PDF → `[📄 {filename}]({relative_path})`  (truncate filename to 25 chars if longer)
    - MP4/WEBM → `<video width="120" controls><source src="{relative_path}" type="video/{ext}"></video>`
    - YouTube/Vimeo URLs (from post metadata Assets field) → `<iframe width="160" height="90" src="{url}" frameborder="0"></iframe>`
    - Google Drive links → `[🔗 Drive]({url})`
    - Multiple assets in one cell: space-separated, max 3 inline thumbnails. If >3 images, show first 3 + `+{N}` text.
    - No assets → `—`

  **Must NOT do**:
  - Do NOT implement Title linkification (Rule 6)
  - Do NOT rewrite the entire process doc — surgical edits only
  - Do NOT change any migration step descriptions (Steps 0-5)

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Surgical doc edits to an existing 571-line file
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Task 2)
  - **Blocks**: F1
  - **Blocked By**: None

  **References**:

  **Pattern References**:
  - `docs/squawk-migration-process.md:82-169` — Current merge rules section (Rules 1-6 + Summary Table) — this is where new rules and amendments go
  - `docs/squawk-migration-process.md:129-143` — Rule 4 "Do Not Touch" fields — must be updated to note columns excluded from rendering
  - `docs/squawk-migration-process.md:160-169` — Summary Table — must be updated with new rule numbers and column exclusion entry

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: Readiness gate rule exists in process doc
    Tool: Bash (grep)
    Preconditions: docs/squawk-migration-process.md exists
    Steps:
      1. grep -c "readiness.*ready\|Readiness Gate" docs/squawk-migration-process.md
      2. Assert count ≥ 2 (rule heading + rule text)
    Expected Result: Readiness gate rule is documented
    Evidence: .sisyphus/evidence/task-1-readiness-gate-rule.txt

  Scenario: Removed columns documented as excluded
    Tool: Bash (grep)
    Preconditions: docs/squawk-migration-process.md exists
    Steps:
      1. grep -i "excluded.*column\|column.*excluded\|excluded from.*rendering" docs/squawk-migration-process.md
      2. Assert at least 1 match
    Expected Result: Column exclusion is documented
    Evidence: .sisyphus/evidence/task-1-column-exclusion-doc.txt

  Scenario: Rule 4 no longer implies removed columns appear in squawk-index.md
    Tool: Bash (grep)
    Preconditions: docs/squawk-migration-process.md updated
    Steps:
      1. Read Rule 4 section
      2. Verify it clarifies that Doc Status, Critical, Posts, Published are excluded from squawk-index.md rendering but still maintained by Squawk
    Expected Result: No contradiction between Rule 4 and actual rendered columns
    Evidence: .sisyphus/evidence/task-1-rule4-consistency.txt
  ```

  **Commit**: YES (group with Task 2, 3)
  - Message: `docs: add readiness gate rule, column exclusion, and asset preview spec to migration process`
  - Files: `docs/squawk-migration-process.md`

---

- [ ] 2. Move Build Script to Repo + Update for Column/Asset Changes

  **What to do**:
  - **Move** `/tmp/build-squawk-index.js` → `scripts/build-squawk-index.js`
  - **Update header template** (currently line ~117-118): Remove columns Squawk CUID, Doc Status, Critical, Posts, Published from the header row and separator row
  - **Update row construction** (currently line ~108): Remove the corresponding data fields from each row template: `docId`, `docStatus`, `critical`, `posts`, `published`
  - **Add Assets Preview column**: After Title column in header. In row construction, add logic to:
    1. Derive the post's directory path from the Post ID using the consistent naming pattern: `posts/2026/02/*_${postId}_*/assets/`
    2. Use `fs.readdirSync` (with try/catch for missing dirs) to list files in the assets dir
    3. Exclude README.md, .DS_Store
    4. For each file, classify by extension:
       - `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg` → `<img src="${relativePath}" width="60">`
       - `.pdf` → `[📄 ${truncate(filename, 25)}](${relativePath})`
       - `.mp4`, `.webm` → `<video width="120" controls><source src="${relativePath}" type="video/${ext}"></video>`
    5. If >3 image thumbnails, show first 3 + ` +${remaining}` text
    6. If 0 real assets → `—`
  - **Update MCP cache path**: Change the hardcoded path on line 4 to accept a CLI argument or environment variable, with the current path as default: `const mcpPath = process.argv[2] || "/Users/idengrenme/.local/share/opencode/tool-output/tool_c7d8cfc360012e4yQZHnqX1bKL";`
  - **Add post directory glob**: The script needs `const { globSync } = require('fs');` or manual directory scanning to find asset dirs by Post ID pattern

  **Must NOT do**:
  - Do NOT add Title linkification
  - Do NOT refactor the overall script architecture
  - Do NOT add test framework or linting
  - Do NOT change the MCP data parsing logic (it works)
  - Do NOT add README.md files from assets dirs

  **Recommended Agent Profile**:
  - **Category**: `unspecified-high`
    - Reason: Script modification with filesystem scanning logic, needs careful path handling
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: YES
  - **Parallel Group**: Wave 1 (with Task 1)
  - **Blocks**: Task 3
  - **Blocked By**: None

  **References**:

  **Pattern References**:
  - `/tmp/build-squawk-index.js:1-123` — Current build script (full file). Key areas: line 4 (MCP path), lines 82-108 (row construction), lines 111-119 (header template)
  - Asset directory naming convention: `posts/2026/02/2026-02-DD_2026-{B|T}-NNN_{slug}/assets/` — Post ID always appears in dir name after the date

  **Data References**:
  - 26 posts with real assets (47 PNG, 4 PDF): `B-002, B-004, B-010, B-020, B-021, B-034, T-001, T-004, T-005, T-008, T-011, T-014, T-017, T-018, T-019, T-020, T-021, T-022, T-024, T-027, T-029, T-032, T-033, T-035, T-038, T-039`
  - Multi-asset posts: T-017 (4 PNGs), T-019 (3 PNGs), T-024 (3 PNGs), T-027 (3 PNGs), T-029 (3 PNGs), T-035 (3 PNGs)
  - PDF-only posts: B-021 (2 PDFs), B-034 (2 PDFs)

  **External References**:
  - Node.js `fs.readdirSync` — standard library, no external deps needed
  - Node.js `path.extname` — for file extension classification

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: Build script exists in repo
    Tool: Bash
    Preconditions: None
    Steps:
      1. ls -la scripts/build-squawk-index.js
      2. Assert file exists and is non-empty
    Expected Result: File exists at scripts/build-squawk-index.js
    Evidence: .sisyphus/evidence/task-2-script-exists.txt

  Scenario: Build script runs without errors
    Tool: Bash
    Preconditions: scripts/build-squawk-index.js exists, MCP cache file exists
    Steps:
      1. PATH="/Users/idengrenme/.local/share/fnm/node-versions/v20.19.5/installation/bin:$PATH" node scripts/build-squawk-index.js
      2. Assert exit code 0
      3. Assert output contains "Wrote 82 rows"
    Expected Result: Script completes successfully, writes 82 rows
    Evidence: .sisyphus/evidence/task-2-script-runs.txt

  Scenario: Generated squawk-index.md has correct column count
    Tool: Bash
    Preconditions: Script has been run
    Steps:
      1. head -8 squawk-index.md | grep "^| Post ID" | tr -cd '|' | wc -c
      2. Assert count = 16 (15 columns + trailing pipe)
    Expected Result: Header has exactly 15 columns
    Evidence: .sisyphus/evidence/task-2-column-count.txt

  Scenario: Removed columns are absent
    Tool: Bash (grep)
    Preconditions: squawk-index.md regenerated
    Steps:
      1. grep -c "Doc Status\|Squawk CUID\| Critical \| Posts \| Published " squawk-index.md
      2. Assert count = 0
    Expected Result: None of the 5 removed columns appear
    Evidence: .sisyphus/evidence/task-2-columns-removed.txt

  Scenario: Assets Preview column present with thumbnails
    Tool: Bash (grep)
    Preconditions: squawk-index.md regenerated
    Steps:
      1. grep -c "Assets Preview" squawk-index.md — assert ≥ 1
      2. grep -c '<img src=' squawk-index.md — assert ≥ 20 (26 posts have PNGs, some with multiple)
      3. grep -c '📄' squawk-index.md — assert ≥ 2 (B-021 and B-034 have PDFs)
    Expected Result: Assets Preview column present, thumbnails and PDF links rendered
    Evidence: .sisyphus/evidence/task-2-assets-preview.txt

  Scenario: Posts without assets show dash
    Tool: Bash
    Preconditions: squawk-index.md regenerated
    Steps:
      1. Count rows where Assets Preview column = "—"
      2. Assert count ≥ 50 (56 posts have no real assets)
    Expected Result: Posts without assets show "—" not empty cells
    Evidence: .sisyphus/evidence/task-2-no-assets-dash.txt
  ```

  **Commit**: YES (group with Task 1, 3)
  - Message: `scripts: add build-squawk-index.js with column pruning and asset preview`
  - Files: `scripts/build-squawk-index.js`

---

- [ ] 3. Regenerate squawk-index.md

  **What to do**:
  - Run the updated build script: `PATH="/Users/idengrenme/.local/share/fnm/node-versions/v20.19.5/installation/bin:$PATH" node scripts/build-squawk-index.js`
  - Verify output: 82 rows, 15 columns, asset thumbnails present for 26 posts
  - Spot-check 3-4 rows manually: one with multiple assets (T-017), one with PDFs (B-021), one without assets (B-006)

  **Must NOT do**:
  - Do NOT hand-edit the generated file
  - Do NOT add/remove rows manually

  **Recommended Agent Profile**:
  - **Category**: `quick`
    - Reason: Single command execution + verification
  - **Skills**: []

  **Parallelization**:
  - **Can Run In Parallel**: NO
  - **Parallel Group**: Wave 2 (sequential after Wave 1)
  - **Blocks**: F1
  - **Blocked By**: Task 2

  **References**:

  **Pattern References**:
  - `scripts/build-squawk-index.js` — the updated build script from Task 2

  **Acceptance Criteria**:

  **QA Scenarios (MANDATORY):**

  ```
  Scenario: squawk-index.md has 82 data rows
    Tool: Bash
    Preconditions: Build script has been run
    Steps:
      1. grep -c "^| 2026-" squawk-index.md
      2. Assert count = 82
    Expected Result: 82 post rows
    Evidence: .sisyphus/evidence/task-3-row-count.txt

  Scenario: Multi-asset post renders correctly (T-017 — 4 PNGs)
    Tool: Bash (grep)
    Preconditions: squawk-index.md regenerated
    Steps:
      1. grep "2026-T-017" squawk-index.md
      2. Assert row contains at least 3 '<img src=' occurrences and '+1' text (since >3 assets)
    Expected Result: T-017 shows 3 thumbnails + "+1" overflow indicator
    Evidence: .sisyphus/evidence/task-3-multi-asset.txt

  Scenario: PDF-only post renders correctly (B-021)
    Tool: Bash (grep)
    Preconditions: squawk-index.md regenerated
    Steps:
      1. grep "2026-B-021" squawk-index.md
      2. Assert row contains '📄' and '.pdf' but no '<img'
    Expected Result: B-021 shows PDF links, no image thumbnails
    Evidence: .sisyphus/evidence/task-3-pdf-only.txt

  Scenario: No-asset post shows dash (B-006)
    Tool: Bash (grep)
    Preconditions: squawk-index.md regenerated
    Steps:
      1. Extract B-006 row and check Assets Preview column value
      2. Assert value is "—"
    Expected Result: B-006 shows "—" in Assets Preview
    Evidence: .sisyphus/evidence/task-3-no-assets.txt
  ```

  **Commit**: YES (group with Task 1, 2)
  - Message: `squawk-index: regenerate with 15 columns, add asset previews`
  - Files: `squawk-index.md`

---

## Final Verification Wave

- [ ] F1. **Column and Content Audit** — `quick`
  Count columns in header (expect 15). Grep for all 5 removed column names (expect 0 matches in header). Count `<img src=` tags (expect ≥ 20). Count `📄` PDF links (expect ≥ 4). Count `—` in Assets Preview column (expect ≥ 50). Verify process doc contains readiness gate rule, column exclusion section, and asset preview spec. Verify no contradictions in Rule 4 / Summary Table.
  Output: `Columns [15/15] | Removed [0 matches] | Assets [N img + N pdf + N dash] | Process Doc [rules present] | VERDICT`

---

## Commit Strategy

Single commit after all 3 tasks complete:
- `squawk: readiness gate rule + column pruning + asset preview column`
- Files: `docs/squawk-migration-process.md`, `scripts/build-squawk-index.js`, `squawk-index.md`

---

## Success Criteria

### Verification Commands
```bash
# Column count (expect 16 pipes = 15 columns)
head -8 squawk-index.md | grep "^| Post ID" | tr -cd '|' | wc -c

# Row count (expect 82)
grep -c "^| 2026-" squawk-index.md

# Removed columns absent (expect 0)
grep -c "Squawk CUID\|Doc Status\| Critical \| Posts \| Published " squawk-index.md

# Asset thumbnails present (expect ≥20)
grep -c '<img src=' squawk-index.md

# PDF links present (expect ≥4)
grep -c '📄' squawk-index.md

# Readiness gate rule in process doc (expect ≥1)
grep -c "Readiness Gate\|readiness.*ready.*APPROVED" docs/squawk-migration-process.md

# Build script in repo (expect 1)
ls scripts/build-squawk-index.js | wc -l
```

### Final Checklist
- [ ] All "Must Have" present
- [ ] All "Must NOT Have" absent
- [ ] squawk-index.md renders correctly in Markdown Preview Enhanced
- [ ] Process doc is internally consistent
