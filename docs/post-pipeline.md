# Post Pipeline

**Purpose:** Authoritative end-to-end process for the LSA Digital marketing content lifecycle, from exploration through approval and index sync.

**Last Verified:** 2026-02-21

---

## Pipeline Overview

The marketing content pipeline consists of seven distinct stages. Each stage must be completed before moving to the next.

| Stage | Activity | Primary Tools |
|-------|----------|---------------|
| 1. Exploration | Topic identification and SME alignment | XMind, Campaign Doc |
| 2. Post Creation | Drafting content and initial ingestion | /new-post, Squawk MCP |
| 3. Asset Creation | Capturing screenshots and diagrams | Playwright, assetpipe/ |
| 4. Post Updates | Refining metadata and dependencies | /update-post, Squawk MCP |
| 5. Review & Readiness | AI assessment and editorial review | Squawk MCP |
| 6. Approval | Final sign-off for publication | Squawk MCP |
| 7. Index Sync | Rebuilding the post catalog | build-squawk-index.js |

---

## Stage 1: Exploration

Identify the core message and target audience before drafting.

1. **Campaign Context:** Consult `marketingCampaignFeb2026.md` for current themes and audience priorities (business vs. technical).
2. **SME Alignment:** Use `lsaProductExpertAlignment.md` to select the appropriate expert and product for the post.
3. **Mind Map Discovery:** Browse `docs/mindmaps/` to find specific nodes that anchor the post in the existing content strategy.

---

## Stage 2: Post Creation

Use the `/new-post` command to initialize the post folder and file.

1. **Command Execution:** Run `/new-post [slug]`.
2. **Folder Structure:** The command creates `posts/YYYY/MM/YYYY-MM-DD_[postid]_slug/`.
3. **Minimal File:** The post markdown file contains only the **Post ID** and **CTA**.
4. **Squawk Ingestion:** Metadata is sent to Squawk via `upsert_document_draft` and `update_post_draft`.

---

## Stage 3: Asset Creation

Create visual evidence to support the post claims. Refer to `docs/asset-creation-pipeline.md` for the full procedure.

1. **Directory Setup:** Create the assets folder: `mkdir -p posts/.../assets`.
2. **Capture Types:**
    - **UI Screenshots:** Use Playwright MCP and scripts in `assetpipe/` to capture product UIs.
    - **Code Snippets:** Read source code from product repos and format as fenced blocks.
    - **Diagrams:** Write Mermaid syntax directly in the post markdown.
    - **Tables:** Use standard markdown tables for feature matrices or checklists.
3. **Reusable Scripts:** Reference `assetpipe/` for existing capture logic (e.g., `lsars-captures.js`, `epms-captures.js`).
4. **Storage:** Assets are filesystem-only. They are not stored in Squawk.

---

## Stage 4: Post Updates

Refine the post metadata as the content evolves.

1. **Command Execution:** Use `/update-post` to modify fields like expert, product, or dependencies.
2. **Dependency Management:** Link posts using the `dependsOnPostId` field in Squawk.
3. **Theme Assignment:** Update themes via `referenceContext.themes` in the Squawk MCP tools.

---

## Stage 5: Review & Readiness

Squawk performs an automated AI assessment of every ingested document.

1. **Readiness Score:** Check the `readinessScore` via `list_review_queue`.
2. **Readiness Summary:** Review the `readinessSummary` for suggested improvements.
3. **Readiness Gate:** A document must have a `readinessScore` of `ready` before it can be approved. Items marked `needs_work` or with empty scores must remain in `PENDING_REVIEW`.

---

## Stage 6: Approval

Finalize the document for the publication queue.

1. **Verification:** Ensure all assets are present and the text aligns with the LSA Digital voice.
2. **Tool Call:** Execute `approve_content_item` with the document CUID.
3. **Status Change:** The document status moves from `PENDING_REVIEW` to `APPROVED`.

---

## Stage 7: Index Sync

Rebuild the derived `squawk-index.md` to reflect the current state of the pipeline.

1. **Execution:** Run the sync script: `node scripts/build-squawk-index.js`.
2. **Data Sources:** The script reads the cached Squawk MCP JSON and scans local `assets/` directories.
3. **Output:** The script writes `squawk-index.md`.

---

## Squawk MCP Quick Reference

### Tool Table

| Tool | Purpose |
|------|---------|
| `upsert_document_draft` | Create or update a document from markdown |
| `update_post_draft` | Set post-level fields (expert, product, dependency) |
| `link_theme_source` | Link document to messaging theme (not used in regular workflow) |
| `approve_content_item` | Approve document for publish |
| `get_content_item` | Read back a document or post by CUID |
| `list_review_queue` | List all documents with review metadata |
| `list_experts` | Get expert CUIDs |
| `list_products` | Get product CUIDs |
| `list_messaging_themes` | Get theme CUIDs |
| `get_sync_status` | Check repo sync state |
| `push_content_item` | Push approved doc assets to GitHub |
| `approve_and_push_one` | Approve and push in one call |

### Expert CUIDs

| Expert | CUID |
|--------|------|
| Keith Mangold | `cml8m3t3e00020ys4ml0dfbl8` |
| Mike Idengren | `cmksysncp000c67s4v38u04d0` |
| Nelson Smith | `cmksysdl4000a67s4m1u7625r` |
| Thad Perry | `cmksysl3d000b67s4rd4kuhbq` |

### Product CUIDs

| Product | CUID |
|---------|------|
| LSARS Permit Intelligence | `cmksy89a7000367s4e634xb3k` |
| Health Risk Assessment (HSRA) | `cml77dhiy000g623jup13ylgk` |
| EPMS | `cmlqx3cm3000hh8s4ujarwpcx` |
| ReimagineIt | `cmksy7vqw000267s45kk14jq3` |
| MEDICODAX | `cmlqx2xq1000gh8s4vkijzvid` |
| Human-AI Concept Lab | `cmlqx3u2q000ih8s4xcorgqim` |

### Invocation Pattern

Use the `execute_tool` function via the lazy-mcp proxy:

```javascript
execute_tool("squawk.<tool_name>", {
  "param1": "value1",
  "param2": "value2"
})
```

**Pacing Note:** Limit calls to 1 or 2 at a time to avoid proxy timeouts.

---

## Commands Reference

| Command | Description |
|---------|-------------|
| `/new-post` | Initializes a new post folder, file, and Squawk draft. |
| `/update-post` | Updates metadata for an existing post in Squawk. |
| `/list-posts` | Displays a filtered list of posts from the index. |

---

## post-index.md Deprecation Notice

The file `post-index.md` is fully deprecated and archived. It was previously used as the manual source of truth for post metadata. 

**Replacement:**
- **Source of Truth:** All metadata now lives in the Squawk MCP database.
- **Derived View:** The `squawk-index.md` file provides a read-only view of the Squawk data, reconstructed from scratch during each sync.

Do not edit `post-index.md`. It is read by `scripts/build-squawk-index.js` as a transitional data source for historical columns (audience, product, themes, expert) that are not yet returned by the Squawk MCP `list_review_queue` response. As Squawk becomes the complete SoT for all columns, this dependency will be removed.
