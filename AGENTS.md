# MARKETING PROJECT KNOWLEDGE BASE

**Last Updated:** 2026-02-10 | **Branch:** main

Marketing content and campaign management for LSA Digital products.

---

## STRUCTURE

```
.
├── posts/                   # Marketing blog posts
├── docs/                    # Marketing documentation
├── marketingCampaignFeb2026.md  # Current campaign
├── post-index.md            # Post index/catalog
└── lsaProductExpertAlignment.md # Product alignment doc
```

---

## RULES

| Rule                       | Description                                                              |
| -------------------------- | ------------------------------------------------------------------------ |
| **CONTEXT7 FIRST**   | Tech research starts with Context7 (via lazy-mcp proxy), not web search. |
| **CONSISTENT VOICE** | Maintain LSA Digital brand voice across all content.                     |

---

## POST METADATA GUIDELINES

Individual post files should contain MINIMAL metadata. All authoritative metadata lives in `squawk-index.md`.

### Post File Structure:

```markdown
# Post Title

## Metadata
- **Post ID**: 2026-B-001
- **CTA**: book a working session at [lsars.com](https://lsars.com)

## Post
...content...

## Artifacts
- Remote:
  - https://lsars.com

## Post asset ideas
- [ ] Screenshot: example

## Citations / Sources
- https://example.com/source (when citing specific data, reports, or public records)
```

### Citations / Sources Section

When a post cites specific external data, public records, reports, or regulatory filings, include a **"Citations / Sources"** section at the end of the post file. This provides transparency and allows readers to verify claims.

**When to include:**

- Citing specific public dockets, permits, or regulatory filings
- Referencing government reports or environmental impact statements
- Using data from official utility or agency websites
- Any claim that could benefit from a verifiable source

**Format:**

```markdown
## Citations / Sources
- https://www.mass.gov/info-details/hmlp-reliability-project
- https://heirp.com/wp-content/uploads/2024/11/HMLP_ZE_Petition_FINAL.pdf (Project components; see pp. 2 and 5)
- https://heirp.com/wp-content/uploads/2024/11/HMLP_EFSB_Petition_20241111-1.pdf (Broad Street Route and Lake Street Route; see pp. 17-18 and 107-111; MassDOT Work Zone Safety reference; see p. 148; Orders of Conditions; see pp. 149-150; MBTA railroad operations constraints; see pp. 52 and 85)
```

Include brief context in parentheses for PDFs or complex documents (page numbers, specific sections).

**Example post with citations:** `posts/2026/02/2026-02-10_2026-B-021_accelerate-utility-permitting/post-accelerate-utility-permitting-2026-B-021.md`

### Authoritative Source:

**post-index.md** is the single source of truth for:

- Status tracking
- Dependencies (Depends On column)
- Theme tags
- Product assignments
- Expert assignments
- Audience targeting
- Publication platforms

---

## MCP TOOLS (via lazy-mcp proxy)

Tools are lazy-loaded through the `lazy-mcp` proxy. Only 2 meta-tools load at startup:

- `get_tools_in_category(path)` — Discover tools in a category
- `execute_tool(tool_path, arguments)` — Execute a discovered tool

### Architecture: Global Shared Config

```
~/dev/common/lazy-mcp/           # Shared across all projects
├── config.json                  # 5 servers: atlassian, context7, chrome-devtools, google-workspace, epms
└── hierarchy/                   # Generated tool discovery files

~/dev/marketing/.mcp.json        # Points to shared config (no graph-code - not a code project)
```

### Tool Categories (5 shared servers)

| Category             | Tools | Use For                              | When                     |
| -------------------- | ----- | ------------------------------------ | ------------------------ |
| `atlassian`        | 43    | Jira tickets, Confluence pages       | Content planning, docs   |
| `chrome-devtools`  | 26    | Browser automation, screenshots      | Visual content capture   |
| `context7`         | 2     | Library documentation lookup         | Tech research            |
| `epms`             | 23    | Product management data              | Product info for content |
| `google-workspace` | 32    | Gmail, Calendar, Drive, Docs, Sheets | Content collaboration    |

### Technology Questions

```
1. execute_tool("context7.resolve-library-id", {"libraryName": "<tech>", "query": "<question>"})
2. execute_tool("context7.query-docs", {"libraryId": "<id>", "query": "<specific question>"})
3. ONLY IF fails: Delegate to librarian agent
```

### Rollback

If proxy fails: delete `.mcp.json` and restart OpenCode.

---

## AGENTS

| Agent                     | Model                | Use For                   |
| ------------------------- | -------------------- | ------------------------- |
| **Sisyphus**        | claude-opus-4-5      | Primary orchestrator      |
| **librarian**       | gemini-2.5-flash     | Web search, external docs |
| **document-writer** | gemini-3-pro-preview | Content creation          |

**Config:** `.opencode/oh-my-opencode.json`

---

## Changelog

| Date       | Author   | Change                                                                                                                   |
| ---------- | -------- | ------------------------------------------------------------------------------------------------------------------------ |
| 2026-02-10 | Sisyphus | Created AGENTS.md with lazy-mcp proxy setup. Uses global config at ~/dev/common/lazy-mcp/.                               |
| 2026-02-13 | Sisyphus | Standardized post metadata: only Post ID and CTA allowed in individual posts. All other metadata lives in post-index.md. |
| 2026-02-14 | Sisyphus | Added Citations / Sources section guidelines to document when and how to include source references in post files.        |
