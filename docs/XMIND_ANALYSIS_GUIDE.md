# XMIND Post-ID Coverage Analysis Guide

## Quick Summary

**File**: `docs/mindmaps/LSARS_posts_v2.xmind`

### Current Status
- **Total Nodes**: 180
- **With Post-ID Labels**: 34 (18.9%)
- **Without Post-ID Labels**: 146 (81.1%)

## How to Use the Analysis Script

### 1. View Human-Readable Report
```bash
python3 scripts/analyze_xmind_coverage.py
```
Shows formatted text output with:
- Summary statistics
- List of all nodes needing post-id assignment
- List of all nodes already assigned

### 2. Export as JSON (for programmatic use)
```bash
python3 scripts/analyze_xmind_coverage.py --json > coverage.json
```
Useful for:
- Integrating with other tools
- Parsing in scripts
- Automated workflows

### 3. Export as CSV (for spreadsheet)
```bash
python3 scripts/analyze_xmind_coverage.py --csv > coverage.csv
```
Then open in Excel/Sheets to:
- Sort by depth or status
- Filter by assignment status
- Bulk edit node information

## Understanding the Output

### Node Structure
Each node has:
- **Title**: The node's text content
- **Node ID**: Unique identifier (used for updates)
- **Post ID**: Label assigned (format: YYYY-X-NNN, e.g., 2026-B-005)
- **Status**: PENDING (needs post-id) or ASSIGNED (has post-id)
- **Depth**: Hierarchy level (1=top-level, 2=main topics, 3+=subtopics)

### Example Node (Pending)
```
Title: How does LSARS help accelerate Data Center permitting?
Node ID: 9801d04d690b4df392dd467d72
Status: PENDING
Depth: 2
```

### Example Node (Assigned)
```
Title: How does LSARS test permit scenarios faster and cheaper?
Node ID: 1d67c542d31d4b42a3349c66de
Post ID: 2026-B-005
Status: ASSIGNED
Depth: 2
```

## Assigning Post-IDs

### Step 1: Identify Node to Assign
From the analysis output, find a node with status PENDING and note its Node ID.

### Step 2: Assign Post-ID Label
```bash
python3 scripts/update_xmind_labels.py \
  docs/mindmaps/LSARS_posts_v2.xmind \
  <NODE_ID> \
  <POST_ID>
```

**Example**:
```bash
python3 scripts/update_xmind_labels.py \
  docs/mindmaps/LSARS_posts_v2.xmind \
  9801d04d690b4df392dd467d72 \
  2026-B-020
```

### Step 3: Verify Assignment
Re-run the analysis to confirm:
```bash
python3 scripts/analyze_xmind_coverage.py | grep "2026-B-020"
```

## Post-ID Naming Convention

Post-IDs follow the pattern: `YYYY-X-NNN`

- **YYYY**: Year (e.g., 2026)
- **X**: Category (B=Business, T=Technology)
- **NNN**: Sequential number (001-999)

### Examples
- `2026-B-001` - Business post #1
- `2026-T-010` - Technology post #10
- `2026-B-020` - Business post #20

## Workflow Integration

### When Creating a New Post
1. Create post folder and content
2. Update `post-index.md`
3. **Immediately assign post-id to mindmap node**:
   ```bash
   python3 scripts/update_xmind_labels.py \
     docs/mindmaps/LSARS_posts_v2.xmind \
     <NODE_ID> \
     <POST_ID>
   ```
4. Verify with analysis script
5. Commit changes

### Why This Matters
The XMind file is the **source of truth** for which topics have been used. Assigning labels immediately prevents:
- Duplicate post creation
- Lost topic assignments
- Confusion about coverage

## Troubleshooting

### "Node not found" Error
- Verify the Node ID is correct (copy from analysis output)
- Check the node exists in the current version of the file

### Post-ID Not Appearing in Analysis
- Re-run the analysis script (it reads fresh from the file)
- Verify the label was added (check XMind file directly)

### Need to Find a Specific Node?
Use the CSV export and search in your spreadsheet application:
```bash
python3 scripts/analyze_xmind_coverage.py --csv > coverage.csv
# Then search for keywords in the Title column
```

## Related Files

- **Analysis Script**: `scripts/analyze_xmind_coverage.py`
- **Update Script**: `scripts/update_xmind_labels.py`
- **Dump Script**: `scripts/dump_xmind_tree.py` (detailed tree view)
- **Post Index**: `post-index.md` (list of created posts)
- **Mindmap File**: `docs/mindmaps/LSARS_posts_v2.xmind`

## Technical Details

### XMind File Format
XMind files are ZIP archives containing:
- `content.json` - Main mindmap content (nodes, labels, structure)
- `metadata.json` - File metadata
- `manifest.json` - File manifest
- `resources/` - Embedded images/attachments

The analysis script:
1. Extracts `content.json` from the ZIP
2. Recursively traverses the node tree
3. Identifies post-id labels (pattern: contains `-` with 2+ parts)
4. Generates statistics and reports

### Label Detection
A label is considered a "post-id" if it:
- Contains at least one hyphen (`-`)
- Has at least 2 parts when split by hyphen
- Examples: `2026-B-005`, `2026-T-010`, `backlog`

## Questions?

Refer to:
- `.claude/commands/update-mindmap-node.md` - Detailed update instructions
- `scripts/update_xmind_labels.py` - Source code with inline documentation
- `scripts/analyze_xmind_coverage.py` - Analysis script source
