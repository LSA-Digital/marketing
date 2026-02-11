#!/usr/bin/env python3
"""
XMind Post-ID Coverage Analyzer

Analyzes LSARS_posts_v2.xmind to identify:
1. Total nodes in the mindmap
2. Nodes with post-id labels (already assigned)
3. Nodes without post-id labels (need assignment)

Usage:
    python3 scripts/analyze_xmind_coverage.py [--json] [--csv]

Output formats:
    --json: Machine-readable JSON output
    --csv:  CSV format for spreadsheet import
    (default: Human-readable text)
"""

import json
import zipfile
import sys
import os
import argparse
from typing import List, Dict, Any

XMIND_PATH = "docs/mindmaps/LSARS_posts_v2.xmind"

def read_xmind_content(xmind_path: str) -> List[Dict]:
    """Extract and parse content.json from XMind file."""
    with zipfile.ZipFile(xmind_path, "r") as zf:
        content = zf.read("content.json")
        return json.loads(content)

def collect_nodes(node: Dict, nodes_list: List[Dict], depth: int = 0) -> None:
    """Recursively collect all nodes with their metadata."""
    title = node.get("title", "Unknown")
    node_id = node.get("id", "No ID")
    labels = node.get("labels", [])
    
    # Detect post-id labels (pattern: YYYY-X-NNN or similar)
    post_id_labels = [l for l in labels if '-' in l and len(l.split('-')) >= 2]
    has_post_id = len(post_id_labels) > 0
    
    nodes_list.append({
        'id': node_id,
        'title': title,
        'labels': labels,
        'post_id': post_id_labels[0] if post_id_labels else None,
        'has_post_id': has_post_id,
        'depth': depth
    })
    
    children = node.get("children", {})
    if isinstance(children, dict) and "attached" in children:
        for child in children["attached"]:
            collect_nodes(child, nodes_list, depth + 1)
    elif isinstance(children, list):
        for child in children:
            collect_nodes(child, nodes_list, depth + 1)

def format_text_output(nodes: List[Dict]) -> str:
    """Format output as human-readable text."""
    # Filter out root node (depth 0)
    nodes = [n for n in nodes if n['depth'] > 0]
    
    total_nodes = len(nodes)
    with_post_id = sum(1 for n in nodes if n['has_post_id'])
    without_post_id = total_nodes - with_post_id
    
    output = []
    output.append("=" * 80)
    output.append("XMIND NODE ANALYSIS: LSARS_posts_v2.xmind")
    output.append("=" * 80)
    output.append(f"\nTOTAL NODES: {total_nodes}")
    output.append(f"  ✓ With post-id labels: {with_post_id}")
    output.append(f"  ✗ Without post-id labels: {without_post_id}")
    output.append(f"  Coverage: {(with_post_id/total_nodes*100):.1f}%")
    
    output.append("\n" + "=" * 80)
    output.append("NODES WITHOUT POST-ID LABELS (Need Assignment)")
    output.append("=" * 80)
    
    remaining = [n for n in nodes if not n['has_post_id']]
    for i, node in enumerate(remaining, 1):
        indent = "  " * (node['depth'] - 1)
        output.append(f"\n{i}. {indent}{node['title']}")
        output.append(f"   ID: {node['id']}")
        if node['labels']:
            output.append(f"   Current labels: {', '.join(node['labels'])}")
    
    output.append("\n" + "=" * 80)
    output.append("NODES WITH POST-ID LABELS (Already Assigned)")
    output.append("=" * 80)
    
    assigned = [n for n in nodes if n['has_post_id']]
    for i, node in enumerate(assigned, 1):
        indent = "  " * (node['depth'] - 1)
        output.append(f"\n{i}. {indent}{node['title']}")
        output.append(f"   Post-ID: {node['post_id']}")
        output.append(f"   ID: {node['id']}")
    
    return "\n".join(output)

def format_json_output(nodes: List[Dict]) -> str:
    """Format output as JSON."""
    nodes = [n for n in nodes if n['depth'] > 0]
    
    total_nodes = len(nodes)
    with_post_id = sum(1 for n in nodes if n['has_post_id'])
    without_post_id = total_nodes - with_post_id
    
    output = {
        "summary": {
            "total_nodes": total_nodes,
            "with_post_id": with_post_id,
            "without_post_id": without_post_id,
            "coverage_percent": round((with_post_id/total_nodes*100), 1)
        },
        "nodes_without_post_id": [n for n in nodes if not n['has_post_id']],
        "nodes_with_post_id": [n for n in nodes if n['has_post_id']]
    }
    
    return json.dumps(output, indent=2)

def format_csv_output(nodes: List[Dict]) -> str:
    """Format output as CSV."""
    nodes = [n for n in nodes if n['depth'] > 0]
    
    output = []
    output.append("Title,Node ID,Post ID,Status,Labels,Depth")
    
    for node in nodes:
        status = "ASSIGNED" if node['has_post_id'] else "PENDING"
        labels = "|".join(node['labels']) if node['labels'] else ""
        post_id = node['post_id'] if node['post_id'] else ""
        
        # Escape quotes in title
        title = f'"{node["title"].replace(chr(34), chr(34)+chr(34))}"'
        
        output.append(f"{title},{node['id']},{post_id},{status},{labels},{node['depth']}")
    
    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--csv', action='store_true', help='Output as CSV')
    args = parser.parse_args()
    
    if not os.path.exists(XMIND_PATH):
        print(f"Error: File not found: {XMIND_PATH}")
        sys.exit(1)
    
    content = read_xmind_content(XMIND_PATH)
    all_nodes = []
    
    for sheet in content:
        if "rootTopic" in sheet:
            collect_nodes(sheet["rootTopic"], all_nodes)
    
    if args.json:
        print(format_json_output(all_nodes))
    elif args.csv:
        print(format_csv_output(all_nodes))
    else:
        print(format_text_output(all_nodes))

if __name__ == "__main__":
    main()
