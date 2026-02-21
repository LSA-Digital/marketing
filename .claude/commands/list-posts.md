# List Posts

List all marketing posts, optionally filtered by status.

## Usage
/list-posts [status] [--live]

## Examples
- /list-posts — List all posts from squawk-index.md
- /list-posts approved — List only approved posts
- /list-posts --live — List all posts live from Squawk MCP
- /list-posts --live pending — List pending posts live from Squawk MCP

## Modes

### Default Mode (squawk-index.md)
Reads the local `squawk-index.md` file. Fast, always available.
Use this for day-to-day browsing. Rebuild the index first if you need fresh data:
```bash
PATH="/Users/idengrenme/.local/share/fnm/node-versions/v20.19.5/installation/bin:$PATH" node scripts/build-squawk-index.js
```

### Live Mode (--live flag)
Queries Squawk MCP directly for real-time data.
```
execute_tool("squawk.list_review_queue", {"includeApproved": true, "limit": 100})
```
**Note:** Maximum 100 items per call. If exactly 100 items are returned, results may be truncated.

## Instructions

When the user invokes this command:

### 1. Parse args
- If `--live` flag present: use Live Mode
- Otherwise: use Default Mode
- If status filter provided: filter results by that status

### 2. Default Mode: Parse squawk-index.md
1. Read `squawk-index.md`
2. Parse the markdown table rows (lines starting with `| 2026-`)
3. Extract columns: Post ID (col 1), Title (col 2), Review Status (col 4), Readiness (col 5), Audience (col 8), Product (col 9), Expert (col 10)
4. If status filter provided, filter rows where Review Status matches (case-insensitive)
5. Display in readable format

### 3. Live Mode: Query Squawk MCP
1. Call: execute_tool("squawk.list_review_queue", {"includeApproved": true, "limit": 100})
2. Parse response items for: title, reviewStatus, readinessScore, updatedAt
3. If status filter provided, filter by reviewStatus
4. Display in readable format
5. If response has exactly 100 items, warn: "Results may be truncated (100-item limit). Use squawk-index.md for complete listing."

### 4. Output format
Display results as a table:
```
Posts (N total, showing: [filter or "all"])

| Post ID    | Title                              | Status         | Readiness  |
|------------|-------------------------------------|----------------|------------|
| 2026-B-001 | Trust Through Auditable AI          | APPROVED       | ready      |
| ...        | ...                                 | ...            | ...        |
```

## Valid Status Filters
- PENDING_REVIEW (or: pending)
- APPROVED (or: approved)
- PUBLISHED (or: published)
