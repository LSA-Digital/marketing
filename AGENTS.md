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

| Rule | Description |
|------|-------------|
| **CONTEXT7 FIRST** | Tech research starts with Context7 (via lazy-mcp proxy), not web search. |
| **CONSISTENT VOICE** | Maintain LSA Digital brand voice across all content. |

---

## POST METADATA GUIDELINES

Individual post files should contain MINIMAL metadata. All authoritative metadata lives in `post-index.md`.

### Allowed in Individual Post Files (2 fields only):

| Field | Purpose | Example |
|-------|---------|---------|
| **Post ID** | Reference identifier for the post | `- **Post ID**: 2026-B-001` |
| **CTA** | Call-to-action specific to this post | `- **CTA**: book a working session at [lsars.com](https://lsars.com)` |

### NOT Allowed in Individual Post Files:

The following fields are tracked in `post-index.md` only and should NEVER appear in individual post files:

- Status (draft, approved, published, etc.)
- Depends on (dependencies are tracked in post-index.md "Depends On" column)
- Product (LSARS, HSRA)
- Themes (tags like AGENT_GUARDRAILS, COMMUNITY_TRANSPARENCY)
- Expert (assigned experts)
- Audience (business/tech)
- Target Platforms (LSARS, LSA Digital)
- Publish dates
- Channel, Theme, Poster, etc.

### Post File Structure:

```markdown
# Post Title

## Metadata
- **Post ID**: 2026-B-001
- **CTA**: book a working session at [lsars.com](https://lsars.com)

## Post
...content...
```

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

| Category | Tools | Use For | When |
|----------|-------|---------|------|
| `atlassian` | 43 | Jira tickets, Confluence pages | Content planning, docs |
| `chrome-devtools` | 26 | Browser automation, screenshots | Visual content capture |
| `context7` | 2 | Library documentation lookup | Tech research |
| `epms` | 23 | Product management data | Product info for content |
| `google-workspace` | 32 | Gmail, Calendar, Drive, Docs, Sheets | Content collaboration |

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

| Agent | Model | Use For |
|-------|-------|---------|
| **Sisyphus** | claude-opus-4-5 | Primary orchestrator |
| **librarian** | gemini-2.5-flash | Web search, external docs |
| **document-writer** | gemini-3-pro-preview | Content creation |

**Config:** `.opencode/oh-my-opencode.json`

---

## Changelog

| Date | Author | Change |
|------|--------|--------|
| 2026-02-10 | Sisyphus | Created AGENTS.md with lazy-mcp proxy setup. Uses global config at ~/dev/common/lazy-mcp/. |
| 2026-02-13 | Sisyphus | Standardized post metadata: only Post ID and CTA allowed in individual posts. All other metadata lives in post-index.md. |
