# Squawk MCP Migration Process

**Created:** 2026-02-20 | **Status:** Test phase complete (4/82 posts migrated)

This document captures the full, proven process for migrating post metadata from `post-index.md` into Squawk via MCP tool calls, and verifying the data round-trips correctly.

---

## Goal

Migrate all post-index.md metadata INTO Squawk as the single source of truth, then rebuild squawk-index.md entirely from Squawk MCP reads.

**`squawk-index.md` is a derived artifact, not a source of truth.** It is reconstructed FROM SCRATCH every time data is pulled from Squawk MCP. It is never edited by hand, never diffed incrementally, and never used as input to any write operation. If Squawk data changes, `squawk-index.md` is deleted and regenerated. The merge rules in this document define how Squawk's raw API responses are transformed into the table format — they are rendering rules, not migration rules that run once.

---

## Prerequisites

### MCP Tools (12 total, via lazy-mcp proxy)

| Tool | Purpose | Used In Migration |
|------|---------|-------------------|
| `upsert_document_draft` | Ingest/update a document from raw markdown | **Write** |
| `update_post_draft` | Set post-level fields (expert, product, dependency) | **Write** |
| `link_theme_source` | Link a document to a messaging theme | **Write** |
| `approve_content_item` | Approve a document for publish | **Write** |
| `get_content_item` | Read back a document or post by CUID | **Verify** |
| `list_review_queue` | List all documents with review metadata | **Verify** |
| `list_experts` | Get expert CUIDs for assignment | **Lookup** |
| `list_products` | Get product CUIDs for assignment | **Lookup** |
| `list_messaging_themes` | Get theme CUIDs for linking | **Lookup** |
| `get_sync_status` | Check repo sync state for a document | Info |
| `push_content_item` | Push approved doc assets to GitHub | Post-migration |
| `approve_and_push_one` | Approve + push in one call | Post-migration |

### Lookup Tables (retrieved via `list_experts`, `list_products`, `list_messaging_themes`)

**Experts:**

| Name | CUID |
|------|------|
| Keith Mangold | `cml8m3t3e00020ys4ml0dfbl8` |
| Mike Idengren | `cmksysncp000c67s4v38u04d0` |
| Nelson Smith | `cmksysdl4000a67s4m1u7625r` |
| Thad Perry | `cmksysl3d000b67s4rd4kuhbq` |

**Products:**

| Name | CUID |
|------|------|
| LSARS Permit Intelligence | `cmksy89a7000367s4e634xb3k` |
| Health Risk Assessment (HSRA) | `cml77dhiy000g623jup13ylgk` |
| EPMS | `cmlqx3cm3000hh8s4ujarwpcx` |
| ReimagineIt | `cmksy7vqw000267s45kk14jq3` |
| MEDICODAX | `cmlqx2xq1000gh8s4vkijzvid` |
| Human-AI Concept Lab | `cmlqx3u2q000ih8s4xcorgqim` |

**Themes:** 22 themes available — see `list_messaging_themes` output. Theme labels (e.g., `AGENT_GUARDRAILS`) map to CUIDs used for `link_theme_source`.

---

## Data Model: Document vs Post

Squawk has two entity types relevant to migration:

- **Document** (`IngestedDocument`): The source markdown artifact. Holds extracted text, themes, audience, product text, readiness score. One document can spawn multiple posts.
- **Post**: A publishable unit linked to one document. Holds `expertId`, `productId`, `dependsOnPostId`, `scheduledFor`, `repostKit`, and publishing profile info.

**Key distinction:** `expertId`, `productId`, and `dependsOnPostId` live on the **Post**, not the Document. The Document holds text-level extraction (audience, product name as text, themes). Both must be populated for a complete migration.

---

## Merge Rules (User-Defined)

These rules serve two purposes:

1. **Migration (one-time):** How data from `post-index.md` is written into Squawk via MCP.
2. **Rendering (every time):** How `squawk-index.md` is reconstructed from scratch from Squawk MCP reads.

`squawk-index.md` is never incrementally updated. Every sync deletes it and rebuilds from Squawk API responses using these rules. The rules are permanent — they define the rendering contract between Squawk data and the markdown table.

### Rule 1: Post-Index Wins for Shared Fields

Post-index overwrites Squawk for ALL of the following:

| Field | Source | Notes |
|-------|--------|-------|
| Audience | post-index `Audience` column | "business" or "tech" |
| Product | post-index `Product` column | First-listed becomes `productId`; full list in `referenceContext.products` |
| Expert | post-index `Expert` column | Simplified per post-index. First-listed becomes `expertId`; full list in `referenceContext.experts` |
| Depends On | post-index `Depends On` column | Resolved to Squawk post CUID via `update_post_draft.dependsOnPostId` |
| Dep. Name | post-index `Dependency Name` column | Passed via `referenceContext.dependencyName` |
| Themes | post-index `Themes` column | **Post-index is master. Overwrite in all cases.** (See Rule 3) |

### Rule 2: Status Mapping + Relationship/Comments Routing

**Status → Review Status mapping:**

| post-index Status | Squawk Review Status | Readiness | Additional Action |
|-------------------|---------------------|-----------|-------------------|
| `draft` | `PENDING_REVIEW` | (from Squawk) | — |
| `draft/delayed` | `PENDING_REVIEW` | `needs_work` | Route comments per content-based logic below |
| `draft/updated` | `PENDING_REVIEW` | `needs_work` | Route comments per content-based logic below |
| `in_review` | `PENDING_REVIEW` | (from Squawk) | Not currently used in post-index |
| `approved` | `APPROVED` | (from Squawk) | Call `approve_content_item` |
| `published` | `PUBLISHED` | (from Squawk) | — |

**Note:** Always use only Squawk-supported schema options. All draft-family statuses (`draft`, `draft/delayed`, `draft/updated`, `in_review`) map to `PENDING_REVIEW`.

**Relationship/Comments routing logic (content-based):**

Routing is determined by whether the post has a dependency, not by status:

| Condition | Comment Destination | Format |
|-----------|-------------------|--------|
| Post HAS `Depends On` value + has comment | **Relationship** column | Verbatim comment text |
| Post has NO `Depends On` + status is `draft/delayed` or `draft/updated` | **Readiness Notes** | `DELAYED: {comment text}` |
| Post has NO `Depends On` + any other status | **Readiness Notes** | Verbatim comment text (no prefix) |
| Empty or `—` comment | Nothing to route | — |

**Rationale:** The Relationship column is reserved exclusively for explaining inter-post dependencies. All other comments (delay reasons, editorial notes, article summaries) go to Readiness Notes.

**Edge case — delayed post WITH dependency:** Comment routes to Relationship (dependency explanation). Readiness = `needs_work` (from status). Readiness Notes falls back to Squawk AI summary (no `DELAYED:` override since the comment went to Relationship).

### Rule 3: Themes — Post-Index is Master

Post-index themes **overwrite** Squawk themes in all cases. Passed via `referenceContext.themes` during ingestion.

### Rule 4: Do Not Touch (Squawk-Maintained Fields)

These fields are read-only from Squawk. Never overwrite during migration:

| Field | Maintained By |
|-------|--------------|
| Repost By | Squawk (derived from publishing profiles + AI suggestions) |
| Doc Status | Squawk (INGESTED, etc.) |
| Critical (concern count) | Squawk (AI readiness assessment) |
| Posts (count) | Squawk (auto-counted) |
| Published (count) | Squawk (auto-counted) |
| Updated | Squawk (auto-timestamped) |
| Readiness Score | Squawk (AI assessment, except `needs_work` override for delayed posts) |
| Readiness Notes | Squawk (AI summary), BUT overwritten with `DELAYED:` prefix when post-index status is `draft/delayed` or `draft/updated` |

**Rendering exclusions:** The following fields are maintained by Squawk but **excluded from squawk-index.md** for readability. They remain queryable via `get_content_item` or `list_review_queue`:
- Doc Status (always `INGESTED` after migration)
- Critical concern count
- Posts count
- Published posts count
- Squawk CUID (document ID — available in the CUID mapping table in this doc)

### Rule 5: Drop Target Platforms

Target Platforms column is **no longer tracked**. Squawk handles distribution as part of its core publishing responsibilities. This column does not appear in squawk-index.md.

### Rule 6: Title Linkification

Use the document's `sourcePath` from Squawk to construct a local markdown link. The Title field in squawk-index.md should be a clickable link to the post's markdown file:

```
[Title Text](posts/2026/02/.../post-...-2026-B-001.md)
```

For posts not in Squawk, use the post-index `Link` column value instead.

### Rule 7: Readiness Gate

**Do NOT call `approve_content_item` for any document where `readinessScore` ≠ `ready`.**

Items with `needs_work` or empty readiness MUST remain `PENDING_REVIEW` regardless of post-index status. This is a pre-approval check enforced at migration time and on every future sync.

| Readiness Score | Action |
|----------------|--------|
| `ready` | Proceed to `approve_content_item` if post-index status = `approved` |
| `needs_work` | Leave as `PENDING_REVIEW` — do NOT approve |
| `—` (empty) | Leave as `PENDING_REVIEW` — do NOT approve |

**Note:** 20 posts were approved in Squawk before this rule was established and currently have `APPROVED` status with `needs_work` readiness. These are grandfathered — no retroactive un-approval. This rule applies to all future migration cycles.

### Summary Table

| # | Rule | Detail |
|---|------|--------|
| 1 | Shared fields | post-index wins: Audience, Product, Expert, Depends On, Dep. Name, Themes — overwrite all |
| 2 | Status mapping | All draft-family statuses → PENDING_REVIEW. approved → APPROVED. published → PUBLISHED |
| 3 | Relationship routing | Has Depends On → comment to Relationship. No Depends On + delayed → `DELAYED:` in Readiness Notes. No Depends On + not delayed → comment to Readiness Notes (no prefix) |
| 4 | Readiness for delayed | Readiness = `needs_work` when post-index status is draft/delayed or draft/updated |
| 5 | Themes | Post-index is master — overwrite in all cases |
| 6 | Do not touch | Repost By, Doc Status, Critical, Posts, Published count, Updated — excluded from squawk-index.md rendering |
| 7 | Readiness Gate | Do NOT approve if readinessScore ≠ ready. Leave as PENDING_REVIEW. |
| 8 | Title linkification | Use Source Paths to make Title a clickable link to the post markdown file |
| 9 | Excluded columns | Squawk CUID, Doc Status, Critical, Posts, Published — in Squawk but not rendered in squawk-index.md |
| 10 | Drop | Target Platforms — no longer tracked |

### Excluded Columns

The following Squawk fields are available via MCP but excluded from `squawk-index.md` for readability:

| Column | Squawk Field | How to Query |
|--------|-------------|-------------|
| Squawk CUID | `id` (document) | See CUID mapping table in this doc |
| Doc Status | `documentStatus` | `get_content_item` with `itemType: "document"` |
| Critical | `criticalConcernCount` | `list_review_queue` response |
| Posts | `postsCount` | `list_review_queue` response |
| Published | `publishedPostsCount` | `list_review_queue` response |

### Rule 8: Asset Preview Column

The `Assets Preview` column in squawk-index.md is generated by scanning each post's `./assets/` directory relative to the post markdown file.

**Scanning rules:**
- Directory pattern: `posts/2026/02/*_{postId}_*/assets/`
- Exclude: `README.md`, `.DS_Store`, any hidden files
- If directory does not exist or contains no qualifying files → render `—`

**Rendering by file type:**

| Extension | Render |
|-----------|--------|
| `.png`, `.jpg`, `.jpeg`, `.gif`, `.svg` | `<a href="{relative_path}"><img src="{relative_path_from_repo_root}" width="180"></a>` (hyperlinked, opens full-size on click) |
| `.pdf` | `[📄 {filename_truncated_25_chars}]({relative_path})` |
| `.mp4`, `.webm` | `<video width="120" controls><source src="{relative_path}" type="video/{ext}"></video>` |
| YouTube/Vimeo URL | `<iframe width="160" height="90" src="{url}" frameborder="0"></iframe>` |
| Google Drive URL | `[🔗 Drive]({url})` |

**Multi-asset cap:** If a post has more than 3 image thumbnails, show the first 3 followed by ` +{N}` (e.g., `+1`). PDF links and video tags are always shown in full (no cap).

**Paths:** All `src` and `href` values use paths relative to the repo root (where squawk-index.md lives), e.g., `posts/2026/02/2026-02-04_2026-T-017_.../assets/epms-kanban-hux.png`.

**Viewer:** squawk-index.md is viewed in Markdown Preview Enhanced (VS Code webview), which renders HTML `<img>`, `<video>`, and `<iframe>` tags natively.

---

## Migration Approach (Test → Confirm → Full)

The migration follows a phased approach to minimize risk:

1. **Test batch (4+4 posts):** Migrate representative samples covering different statuses, products, expert configurations, and dependency relationships. Batch 1 (B-001, T-013, B-016, T-018) covered no-dependency cases. Batch 2 adds posts with dependencies to verify Relationship/Depends On/Dep. Name fields.
2. **Sample table reconstruction:** After each test batch, read all test posts back from Squawk via MCP and reconstruct a sample squawk-index.md table. Present to user for confirmation that data round-tripped correctly and merge rules render as expected.
3. **Full migration (remaining posts):** After user confirms sample, migrate all remaining posts using the same per-post sequence (Step 0 → Step 1 → Step 2 → Step 3 → Step 4 → Verify).
4. **Full squawk-index.md rebuild:** Pull ALL data from Squawk MCP and reconstruct the complete squawk-index.md. This is the final deliverable confirming Squawk is the single source of truth.

**Per-post sequence summary:** Step 0 (update post file metadata) → Step 1 (upsert document draft) → Step 2 (update post draft) → Step 3 (link themes if needed) → Step 4 (approve if applicable) → Verify.

---

## Per-Post Migration Sequence

### Step 0: Update Post File Metadata

**Tool:** File edit (no MCP call)

**Purpose:** Ensure the post markdown file contains the full metadata section that Squawk's LLM extraction will parse. Without this, the LLM extraction produces nulls for audience, product, themes, etc., and the `referenceContext` alone may not fully compensate.

**Source of truth:** `post-index.md` — all metadata values come from the post-index row for this post.

**Required metadata section in post file:**

```markdown
## Metadata
- **Post ID**: 2026-T-001
- **Audience**: tech
- **Product**: LSARS, HSRA
- **Themes**: AGENT_GUARDRAILS, COMMUNITY_TRANSPARENCY
- **Expert**: Mike, Keith
- **Depends On**: 2026-B-001
- **Dependency Name**: Trust Through Auditable AI
- **Relationship**: Advisor/research-agent split makes the audit trail inspectable
- **Assets**: zero-trust-boundary-diagram.png, architecture-diagram.png
- **CTA**: see artifacts at [lsadigital.com](https://lsadigital.com)
```

**Field mapping from post-index.md:**

| Post file field | post-index column | Notes |
|----------------|-------------------|-------|
| Post ID | Post ID | Already present in most files |
| Audience | Audience | "business" or "tech" |
| Product | Product | Comma-separated list |
| Themes | Themes | Comma-separated theme labels |
| Expert | Expert | Comma-separated short names |
| Depends On | Depends On | External post ID (e.g., "2026-B-001") or "—" |
| Dependency Name | Dependency Name | Title of the dependency target, or "—" |
| Relationship | Relationship / Comments | Verbatim comment text, or omit if empty |
| Assets | Post `assets/` folder + external links | See Asset References below |
| CTA | — | Keep existing CTA (not from post-index) |

**Asset References:**

The `Assets` field lists files and links that accompany the post. Values can be:

- **Local filenames** — files in the post's `./assets/` folder (e.g., `diagram.png`, `hero.png`). Squawk derives the assets directory from `sourcePath` automatically (`{post-dir}/assets/`).
- **Google Drive links** — for assets too large for GitHub (e.g., video files, high-res renders). Use the full sharing URL.
- **Mix of both** — comma-separated list combining local filenames and external URLs.

Examples:
```markdown
- **Assets**: hero.png, architecture-diagram.svg
- **Assets**: hero.png, https://drive.google.com/file/d/1abc.../view
- **Assets**: https://drive.google.com/file/d/1abc.../view
- **Assets**: —
```

Squawk's AI analysis parses this field to identify available assets and flag missing ones. Local files are downloaded from GitHub via Squawk's asset sync pipeline (not during MCP ingestion — handled separately by Squawk after documents are ingested). Google Drive links are stored as references in the extraction metadata.

**Verification before proceeding to Step 1:** Open the post file and confirm all metadata fields are present and match post-index.md. If any field is missing or shows only Post ID + CTA, the file must be updated before ingestion.

**Why both metadata AND referenceContext are needed:**
- Post file metadata → parsed by Squawk's LLM during ingestion (primary extraction path)
- `referenceContext` in Step 1 → structured override/supplement that ensures accuracy even if the LLM misparses

Both channels must be populated from the same post-index.md data. If the post file metadata is missing, the LLM extraction returns nulls, and `referenceContext` alone may not fill all fields (e.g., `audience` and `product` as text are extracted from markdown, not from referenceContext).

---

### Step 1: Upsert Document Draft

**Tool:** `upsert_document_draft`

**Purpose:** Creates or updates the document in Squawk. Passes the raw markdown (with full metadata from Step 0) for LLM extraction, plus a `referenceContext` object for structured metadata that the LLM might miss.

**Required arguments:**

```json
{
  "rawMarkdown": "<full markdown content of the post file>",
  "sourcePath": "posts/2026/02/2026-02-04_2026-B-001_.../post-...-2026-B-001.md",
  "sourceRepoUrl": "https://github.com/LSA-Digital/marketing.git",
  "referenceContext": {
    "postId": "2026-B-001",
    "name": "Trust Through Auditable AI",
    "audience": "business",
    "products": ["LSARS", "HSRA"],
    "themes": ["AGENT_GUARDRAILS", "COMMUNITY_TRANSPARENCY"],
    "experts": ["Nelson", "Thad", "Mike"],
    "relationshipComments": "optional - delay reason or relationship note",
    "dependsOnPostId": "optional - external post ID like 2026-B-001"
  }
}
```

**Critical: Omit `sourceCommitSha`.**

The ingestion pipeline (ingest-document-core.ts lines 163-181) checks `sourceCommitSha` for idempotency. If the SHA matches an existing document, the pipeline returns early with `alreadyExists: true` **without processing `referenceContext`**. By omitting `sourceCommitSha`, the pipeline always re-processes.

**Response contains:**

```json
{
  "documentId": "cmla2aisk002kqk3jypq1n0wl",
  "alreadyExists": true,
  "existingPostId": "cmlmipucl001g6gs4tjxficpb",
  "extraction": { ... },
  "plan": { ... }
}
```

The `existingPostId` is the post CUID needed for Step 2. If the document is new, the response includes a `postId` field instead.

**What `referenceContext` does:**
- `experts` array → maps to `repostByNames` (document-level repost targets, NOT the post-level `expertId`)
- `themes` array → declared themes on the document
- `products` array → text-level product references
- `audience` → stored in extraction
- `relationshipComments` → stored in `aiExtraction` JSON, read back via `get_content_item`
- `dependsOnPostId` → stored in `aiExtraction` JSON

### Step 2: Update Post Draft

**Tool:** `update_post_draft`

**Purpose:** Sets the post-level structured metadata fields that require CUIDs.

**Required arguments:**

```json
{
  "postId": "cmlmipucl001g6gs4tjxficpb",
  "expertId": "cmksysdl4000a67s4m1u7625r",
  "productId": "cmksy89a7000367s4e634xb3k",
  "dependsOnPostId": "cmlmipucl001g6gs4tjxficpb"
}
```

**Field mapping rules:**
- `expertId`: Singular. Use the **first-listed** expert from post-index as the primary. Remaining experts are captured via `referenceContext.experts` → `repostByNames` on the document.
- `productId`: Singular. Use the **first-listed** product. Multi-product posts (e.g., "LSARS, HSRA") pick the primary.
- `dependsOnPostId`: Must be a **Squawk post CUID**, not an external post ID. Resolve "2026-B-001" → actual CUID by looking up posts already migrated. Posts without dependencies pass `null`.

**Response confirms:**

```json
{
  "id": "cmlmipucl001g6gs4tjxficpb",
  "title": "Trust Through Auditable AI...",
  "status": "DRAFT",
  "expertId": "cmksysdl4000a67s4m1u7625r",
  "productId": "cmksy89a7000367s4e634xb3k",
  "dependsOnPostId": null,
  "scheduledFor": null,
  "updatedAt": "2026-02-20T20:39:33.576Z"
}
```

### Step 3: Link Themes (if needed)

**Tool:** `link_theme_source`

**Purpose:** Explicitly links a document to a messaging theme by CUID.

```json
{
  "themeId": "cmlqwntdz0000ozs45deti004",
  "sourceType": "DOCUMENT",
  "sourceId": "cmla2aisk002kqk3jypq1n0wl"
}
```

**When needed:** If the document's `declaredThemes` array is empty or incorrect after upsert. In practice, themes declared in the markdown metadata section are auto-extracted by the LLM during ingestion, so this step is a fallback.

### Step 4: Approve (for approved posts)

**Tool:** `approve_content_item`

**Purpose:** Moves the document review status from `PENDING_REVIEW` to `APPROVED`.

Only call for posts with `status: approved` or `status: published` in post-index.md. Posts with `draft`, `draft/delayed`, or `draft/updated` stay as `PENDING_REVIEW`.

---

## Verification

### Per-Post Verification

**Tool:** `get_content_item` with `itemType: "post"` and the post CUID.

**Verify these fields are populated:**

| Field | Expected |
|-------|----------|
| `expertId` | Non-null CUID |
| `expertName` | Resolved name (e.g., "Nelson Smith") |
| `productId` | Non-null CUID |
| `productName` | Resolved name (e.g., "LSARS Permit Intelligence") |
| `externalPostId` | Matches post-index Post ID (e.g., "2026-B-001") |
| `dependsOnPostId` | CUID of dependency target, or null |
| `dependsOnExternalPostId` | External ID of dependency, or null |
| `tags` | Array of theme labels |
| `content` | Post body text |

**Also verify document level** with `itemType: "document"`:

| Field | Expected |
|-------|----------|
| `extraction.audience` | "business" or "tech" |
| `extraction.product` | Product name(s) as text |
| `declaredThemes` | Array of theme labels |
| `extraction.repostByNames` | Array of expert short names |
| `extraction.relationshipComments` | Relationship text from post-index |

### Bulk Verification

**Tool:** `list_review_queue` returns all documents with summary metadata. Use to verify:
- Total count matches expectations
- `postsCount` ≥ 1 for all migrated documents
- `declaredThemes` populated
- `readinessScore` present

---

## Test Results (4 Posts)

| Post ID | Expert | Product | Themes | Deps | Status |
|---------|--------|---------|--------|------|--------|
| B-001 | Nelson Smith ✅ | LSARS Permit Intelligence ✅ | AGENT_GUARDRAILS, COMMUNITY_TRANSPARENCY ✅ | none ✅ | DRAFT ✅ |
| T-013 | Mike Idengren ✅ | LSARS Permit Intelligence ✅ | LOCATION_INTELLIGENCE, RISK_INVESTMENTS, SMART_MOBILITY ✅ | none ✅ | INCOMPLETE ✅ |
| B-016 | Nelson Smith ✅ | LSARS Permit Intelligence ✅ | COMMUNITY_TRANSPARENCY, DASHBOARD_ACCOUNTABILITY, DATA_CENTER ✅ | none ✅ | DRAFT ✅ |
| T-018 | Mike Idengren ✅ | EPMS ✅ | TECH_UX, AGENTICAI_DEVOPS, FUTUREAI_PRODDEV ✅ | none ✅ | INCOMPLETE ✅ |

---

## Post Metadata Requirements

Individual post markdown files include metadata that Squawk extracts. The metadata section format:

```markdown
## Metadata
- **Post ID**: 2026-B-001
- **Audience**: business
- **Product**: LSARS, HSRA
- **Themes**: AGENT_GUARDRAILS, COMMUNITY_TRANSPARENCY
- **Expert**: Nelson, Thad, Mike
- **Depends On**: —
- **Relationship**: <optional relationship note or delay reason>
- **CTA**: book a working session at [lsars.com](https://lsars.com)
```

The LLM extraction parses these fields from the markdown. The `referenceContext` object in `upsert_document_draft` serves as a structured override/supplement to ensure accuracy.

**Note on post-index.md metadata standard:** Per AGENTS.md, individual post files should contain minimal metadata (Post ID + CTA only). The extended metadata above was added as part of this migration to feed Squawk's extraction. After migration, `post-index.md` remains the authoritative source for metadata, and `squawk-index.md` will be rebuilt purely from Squawk reads.

---

## Known Issues & Workarounds

### 1. `sourceCommitSha` Idempotency Bypass

**Problem:** If `sourceCommitSha` matches the existing document's SHA, the pipeline skips re-processing entirely — `referenceContext` is never applied.

**Workaround:** Omit `sourceCommitSha` from the `upsert_document_draft` call. This forces re-processing every time.

**Source:** `packages/api/modules/documents/lib/ingest-document-core.ts` lines 163-181.

### 2. Singular Expert/Product Fields

**Problem:** Post-index lists multiple experts and products per post (e.g., "Nelson, Julian, Mike" and "LSARS, HSRA"), but `expertId` and `productId` on the Post entity are singular.

**Workaround:** Use the first-listed as the primary post-level assignment. Additional experts are captured via `referenceContext.experts` → `repostByNames` on the document, which drives repost targeting.

### 3. "Julian" Has No Publishing Profile

**Problem:** Squawk warns `Could not find profile for repost name: "Julian"` — Julian is referenced in post-index expert assignments but has no corresponding Squawk publishing profile.

**Impact:** Julian won't appear in repost targets. Not blocking for migration.

### 4. `dependsOnPostId` Requires CUID Resolution

**Problem:** Post-index stores dependencies as external IDs (e.g., "2026-B-001"), but `update_post_draft.dependsOnPostId` requires a Squawk post CUID.

**Workaround:** During migration, maintain a lookup table of `externalPostId → postCUID` built from `upsert_document_draft` responses. Process dependency-free posts first, then posts with dependencies once their targets have CUIDs.

### 5. Stale lazy-mcp Hierarchy

**Problem:** The lazy-mcp proxy caches tool schemas in static JSON files under `~/dev/common/lazy-mcp/hierarchy/squawk/`. When Squawk adds new tools or fields, the proxy silently strips unrecognized fields — calls "succeed" but data doesn't persist.

**How it was caught:** `update_post_draft` accepted `expertId`/`productId` without error but the fields weren't stored. Reading the Squawk repo source revealed the actual schema had these fields, but the proxy's cached schema didn't.

**Fix:** Regenerate hierarchy from the live MCP server:
1. Fetch live tools: `curl` to Squawk's MCP endpoint with `tools/list` JSON-RPC
2. Save as `{serverName: "squawk", tools: [...]}`
3. Run `structure_generator -input <file> -output <hierarchy_dir>`

**Postmortem:** `~/dev/common/lazy-mcp-stale-hierarchy-postmortem.md`

---

## Migration Order Strategy

### Phase 0: Test Batch (COMPLETE)

4 representative posts migrated and verified: B-001, T-013, B-016, T-018.

### Phase 1: Sample Table Reconstruction (NEXT)

Read all 4 test posts from Squawk. Apply merge rules (Section: Merge Rules) to reconstruct a sample squawk-index.md table. Present to user for confirmation before proceeding.

### Phase 2: Migrate All Remaining Posts (78 documents)

Every post in post-index.md must conform to metadata requirements and be ingested into Squawk. Posts with existing Squawk CUIDs will be re-ingested (upsert). Posts without CUIDs will be created fresh. The sequence is identical for both:

1. `upsert_document_draft` with `referenceContext` (omit SHA) → get post CUID
2. `update_post_draft` with expertId/productId
3. Record `externalPostId → postCUID` mapping
4. Apply merge rules for status → review status, relationship routing, readiness

### Phase 3: Dependency Resolution

After all posts have CUIDs, iterate over posts with `Depends On` values:
1. Look up target external ID in the mapping table
2. Call `update_post_draft` with `dependsOnPostId` = target's post CUID

### Phase 4: Approvals

For posts with `status: approved` or `status: published` in post-index:
1. Call `approve_content_item` with the document CUID

### Phase 5: Full squawk-index.md Rebuild

**Delete `squawk-index.md` and regenerate from scratch.** Pull ALL data from Squawk MCP using `list_review_queue` + `get_content_item` for each document/post. Apply the merge rules (status mapping, content-based relationship routing, title linkification, readiness overrides) to render the complete table. This is not a diff or incremental update — it is a full reconstruction every time.

This same from-scratch process applies to every future Squawk sync. `squawk-index.md` is disposable; Squawk is the source of truth. After full migration, every post in post-index.md will have a corresponding Squawk document.

---

## Post-Migration Work

After full migration is complete and squawk-index.md is rebuilt with all rows, the following updates are needed to align the day-to-day content workflow with Squawk as the source of truth.

### 1. Update `.claude/commands/new-post.md`

The current command creates posts with minimal metadata (Post ID + CTA) and updates `post-index.md` only. Post-migration, new posts must:
- Include full metadata section (Audience, Product, Themes, Expert, Depends On, Dependency Name, Relationship, Assets, CTA) per Step 0 requirements
- Ingest into Squawk via `upsert_document_draft` + `update_post_draft` as part of post creation
- Trigger squawk-index.md reconstruction (or note it as a separate sync step)

### 2. Convert `.claude/commands/update-status.md` → `update-post.md`

The current `update-status` command only changes a status field. Post-migration, updates go through Squawk:
- Rename to `update-post.md` to reflect broader scope
- Support updating any post-level field (status, expert, product, themes, dependencies, assets)
- Route updates through Squawk MCP tools (`update_post_draft`, `approve_content_item`, etc.)
- Rebuild squawk-index.md after changes (or batch rebuilds)

### 3. Update `AGENTS.md`

The current AGENTS.md has outdated guidance that conflicts with the post-migration workflow:
- **Post Metadata Guidelines**: Still says "MINIMAL metadata" and "Post ID + CTA only". Must be updated to reflect the full metadata section required for Squawk ingestion (per Step 0)
- **Authoritative Source**: Still says "post-index.md is the single source of truth". Must be updated to reflect that Squawk is the source of truth and squawk-index.md is a derived artifact
- **Structure section**: Add `squawk-index.md` and `docs/squawk-migration-process.md` to the file tree
- **MCP Tools section**: Add Squawk to the tool categories table (12 tools)
- **Changelog**: Record the migration completion

### 4. Review other commands

| Command | Current State | Post-Migration Action |
|---------|--------------|----------------------|
| `list-posts.md` | Lists from post-index.md | Consider listing from squawk-index.md or Squawk MCP directly |
| `update-mindmap-node.md` | XMind label updates | No change needed — independent of Squawk |
| `README.md` | Command directory readme | Update if command names change |

---

## File References

| File | Purpose |
|------|---------|
| `post-index.md` | Source of truth for merge data (82 posts, 13 columns) |
| `squawk-index.md` | Target — will be rebuilt from Squawk reads after migration |
| `posts/2026/02/*/post-*.md` | Individual post markdown files with metadata sections |
| `~/dev/common/lazy-mcp/hierarchy/squawk/` | MCP tool schema cache (12 tools) |
| `~/dev/common/lazy-mcp/config.json` | Proxy config with Squawk server URL |
| `~/dev/common/lazy-mcp-stale-hierarchy-postmortem.md` | Proxy caching incident writeup |
