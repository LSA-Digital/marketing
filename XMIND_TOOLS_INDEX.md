# XMIND Tools & Documentation Index

## Overview

Complete toolkit for analyzing and managing post-id assignments in the LSARS mindmap (`docs/mindmaps/LSARS_posts_v2.xmind`).

## Quick Stats

- **Total Nodes**: 180
- **With Post-ID**: 34 (18.9%)
- **Without Post-ID**: 146 (81.1%)
- **Main Topics (Depth 2)**: 42 (25 assigned, 17 pending)

## Tools

### 1. Analysis Script
**File**: `scripts/analyze_xmind_coverage.py`

Analyzes the XMIND file and generates reports on post-id coverage.

**Usage**:
```bash
# Human-readable report
python3 scripts/analyze_xmind_coverage.py

# JSON export (for scripts/automation)
python3 scripts/analyze_xmind_coverage.py --json > coverage.json

# CSV export (for spreadsheets)
python3 scripts/analyze_xmind_coverage.py --csv > coverage.csv
```

**Output**: Summary statistics, list of pending nodes, list of assigned nodes

---

### 2. Update Script
**File**: `scripts/update_xmind_labels.py`

Adds post-id labels to specific nodes in the XMIND file.

**Usage**:
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

---

### 3. Dump Script
**File**: `scripts/dump_xmind_tree.py`

Displays the full tree structure of the XMIND file with all node details.

**Usage**:
```bash
python3 scripts/dump_xmind_tree.py docs/mindmaps/LSARS_posts_v2.xmind
```

---

## Documentation

### Quick Reference
**File**: `XMIND_QUICK_REFERENCE.txt`

One-page cheat sheet with:
- Current status
- Common commands
- Post-ID naming convention
- Quick workflow steps

**Best for**: Quick lookups while working

---

### Full Analysis Guide
**File**: `docs/XMIND_ANALYSIS_GUIDE.md`

Comprehensive guide covering:
- How to use each script
- Understanding the output
- Assigning post-IDs
- Naming conventions
- Workflow integration
- Troubleshooting

**Best for**: Learning the system, detailed reference

---

### Coverage Summary
**File**: `docs/XMIND_COVERAGE_SUMMARY.md`

Executive summary with:
- Key metrics and statistics
- List of all 17 pending main topics (with node IDs)
- List of all 25 assigned main topics
- Next steps and related files

**Best for**: Planning which topics to create next, tracking progress

---

### Update Instructions
**File**: `.claude/commands/update-mindmap-node.md`

Detailed instructions for updating mindmap nodes, including:
- How the XMind file format works
- Finding node IDs
- Applying labels
- Verification steps
- Integration with `/new-post` command

**Best for**: Understanding the technical details

---

## Workflow: Create a New Post

1. **Analyze coverage** to find pending topics:
   ```bash
   python3 scripts/analyze_xmind_coverage.py
   ```

2. **Choose a topic** from the pending list and note its Node ID

3. **Assign a post-id** to the node:
   ```bash
   python3 scripts/update_xmind_labels.py \
     docs/mindmaps/LSARS_posts_v2.xmind \
     <NODE_ID> \
     <POST_ID>
   ```

4. **Create the post** using the `/new-post` command

5. **Verify** the assignment:
   ```bash
   python3 scripts/analyze_xmind_coverage.py | grep "<POST_ID>"
   ```

6. **Commit** your changes

---

## File Locations

| File | Purpose |
|------|---------|
| `scripts/analyze_xmind_coverage.py` | Analysis tool (main) |
| `scripts/update_xmind_labels.py` | Update tool |
| `scripts/dump_xmind_tree.py` | Tree viewer |
| `docs/mindmaps/LSARS_posts_v2.xmind` | The mindmap file |
| `docs/XMIND_ANALYSIS_GUIDE.md` | Full guide |
| `docs/XMIND_COVERAGE_SUMMARY.md` | Coverage summary |
| `XMIND_QUICK_REFERENCE.txt` | Quick reference |
| `XMIND_TOOLS_INDEX.md` | This file |
| `.claude/commands/update-mindmap-node.md` | Update instructions |

---

## Post-ID Naming Convention

Format: `YYYY-X-NNN`

- **YYYY**: Year (e.g., 2026)
- **X**: Category
  - **B** = Business
  - **T** = Technology
  - **SM** = Smart Mobility (optional)
- **NNN**: Sequential number (001-999)

**Examples**:
- `2026-B-001` = Business post #1
- `2026-T-010` = Technology post #10
- `2026-B-020` = Business post #20

---

## Key Insights

### Main Topics Status
- **42 main topics** (depth 2) in the mindmap
- **25 already assigned** (59.5%) - ready for content creation
- **17 pending** (40.5%) - need post-id assignment

### Pending Main Topics by Category
- **Business**: 5 topics
- **Technology**: 2 topics
- **Smart Mobility**: 7 topics
- **Metadata/Structural**: 3 topics (may not need post-ids)

### Coverage Opportunity
- 146 nodes without post-ids represent detailed subtopics
- Main topics (depth 2) are the priority for post creation
- Subtopics (depth 3+) can be addressed after main topics

---

## Troubleshooting

### "Node not found" Error
- Verify Node ID is correct (copy from analysis output)
- Check node exists in current version of file

### Post-ID Not Appearing
- Re-run analysis script (reads fresh from file)
- Verify label was added to correct node

### Need to Find a Specific Node?
```bash
python3 scripts/analyze_xmind_coverage.py --csv | grep "search term"
```

---

## Integration Points

### With `/new-post` Command
The post creation workflow should:
1. Create post folder and content
2. Update `post-index.md`
3. **Assign post-id to mindmap node** (immediately)
4. Verify with analysis script
5. Commit changes

### With Git Workflow
- Commit the updated XMIND file after assigning post-ids
- Include post-id assignment in the same commit as post creation
- Use meaningful commit messages referencing the post-id

---

## Questions?

Refer to:
1. **Quick lookup**: `XMIND_QUICK_REFERENCE.txt`
2. **How-to guide**: `docs/XMIND_ANALYSIS_GUIDE.md`
3. **Current status**: `docs/XMIND_COVERAGE_SUMMARY.md`
4. **Technical details**: `.claude/commands/update-mindmap-node.md`
5. **Script source**: `scripts/analyze_xmind_coverage.py`

---

**Created**: 2026-02-10  
**Last Updated**: 2026-02-10  
**Maintainer**: Marketing Team
