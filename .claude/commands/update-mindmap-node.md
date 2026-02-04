# Update Mind Map Node

Update nodes in XMind mind map files. Supports adding labels, modifying notes, and other node properties.

## Usage

```bash
# Add a label to a node
python3 scripts/update_xmind_labels.py <xmind-file> <node-id> <label>

# Example
python3 scripts/update_xmind_labels.py docs/mindmaps/LSARS_posts_v2.xmind 85bee37e6bab4e0a8b5c7ad50b 2026-B-003
```

## Verification

After applying a label, verify using the XMind MCP:

```
search_nodes(
  path: "docs/mindmaps/LSARS_posts_v2.xmind",
  query: "<post-id>",
  searchIn: ["labels"]
)
```

---

## Script Reference

**Location**: `scripts/update_xmind_labels.py`

**How it works**:
1. Extracts `content.json` from the `.xmind` ZIP archive
2. Finds the node by ID
3. Adds the label to the node's `labels` array
4. Repackages the `.xmind` file

**Usage**:
```bash
python3 scripts/update_xmind_labels.py <xmind_file> <node_id> <label>
```

---

## Technical Details

### XMind File Format

XMind files (`.xmind`) are ZIP archives containing:
- `content.json` — Main mind map content (nodes, relationships, labels)
- `metadata.json` — File metadata
- `manifest.json` — File manifest
- `resources/` — Embedded images/attachments

The Python script directly modifies `content.json` and repackages the ZIP, preserving all other files.

### Finding Node IDs

To find a node's ID, use the XMind MCP tools:

```
extract_node(
  path: "docs/mindmaps/LSARS_posts_v2.xmind",
  searchQuery: "partial node title"
)
```

Or search:
```
search_nodes(
  path: "docs/mindmaps/LSARS_posts_v2.xmind",
  query: "search term"
)
```

---

## Integration with /new-post

When creating posts from mind map nodes, the `/new-post` command **must** apply labels synchronously:

1. Create the post folder and content
2. Update `post-index.md`
3. **Apply the XMind label immediately**:
   ```bash
   python3 scripts/update_xmind_labels.py docs/mindmaps/LSARS_posts_v2.xmind <node-id> <post-id>
   ```
4. **Verify the label**:
   ```
   search_nodes(path, query="<post-id>", searchIn=["labels"])
   ```
5. Complete the post creation summary

**Labels must not be deferred.** The XMind file is the source of truth for which topics have been used.

---

## Error Handling

- **Node not found**: Double-check the node ID using `extract_node` or `search_nodes`
- **Write failure**: Original file remains intact; the script uses atomic write via temp file
- **Verification failure**: Re-run the script or check if the node ID is correct

---

## Quick Reference

```bash
# Add label
python3 scripts/update_xmind_labels.py docs/mindmaps/LSARS_posts_v2.xmind <node-id> <label>

# Verify (via MCP)
search_nodes(path="docs/mindmaps/LSARS_posts_v2.xmind", query="<label>", searchIn=["labels"])

# Find node ID
extract_node(path="docs/mindmaps/LSARS_posts_v2.xmind", searchQuery="node title")
```
