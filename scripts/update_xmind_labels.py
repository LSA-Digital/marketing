#!/usr/bin/env python3
"""
XMind Label Updater

Updates labels on XMind nodes by:
1. Extracting the content.json from the .xmind ZIP archive
2. Adding labels to specified nodes
3. Repackaging the .xmind file

Usage:
    python3 update_xmind_labels.py <xmind_file> <node_id> <label>

Example:
    python3 update_xmind_labels.py docs/mindmaps/LSARS_posts_v2.xmind 85bee37e6bab4e0a8b5c7ad50b 2026-B-003
"""

import json
import zipfile
import shutil
import sys
import os


from typing import Optional


def read_xmind_content(xmind_path: str) -> dict:
    """Extract and parse content.json from XMind file."""
    with zipfile.ZipFile(xmind_path, "r") as zf:
        content = zf.read("content.json")
        return json.loads(content)


def write_xmind_content(xmind_path: str, content: dict):
    """Update content.json in XMind file while preserving other files."""
    temp_path = xmind_path + ".tmp"

    with zipfile.ZipFile(xmind_path, "r") as zf_in:
        with zipfile.ZipFile(temp_path, "w", zipfile.ZIP_DEFLATED) as zf_out:
            for item in zf_in.namelist():
                if item == "content.json":
                    zf_out.writestr(
                        item, json.dumps(content, ensure_ascii=False, indent=2)
                    )
                else:
                    zf_out.writestr(item, zf_in.read(item))

    shutil.move(temp_path, xmind_path)


def find_node_by_id(data: dict, node_id: str) -> Optional[dict]:
    """Recursively find a node by its ID."""
    if data.get("id") == node_id:
        return data

    if "rootTopic" in data:
        result = find_node_by_id(data["rootTopic"], node_id)
        if result:
            return result

    if "children" in data:
        children = data["children"]
        if isinstance(children, dict) and "attached" in children:
            children = children["attached"]
        if isinstance(children, list):
            for child in children:
                result = find_node_by_id(child, node_id)
                if result:
                    return result

    return None


def add_label_to_node(node: dict, label: str) -> bool:
    """Add a label to a node if not already present."""
    if "labels" not in node:
        node["labels"] = []

    if label not in node["labels"]:
        node["labels"].append(label)
        return True
    return False


def main():
    if len(sys.argv) != 4:
        print(__doc__)
        print("\nError: Expected 3 arguments: <xmind_file> <node_id> <label>")
        sys.exit(1)

    xmind_path = sys.argv[1]
    node_id = sys.argv[2]
    label = sys.argv[3]

    if not os.path.exists(xmind_path):
        print(f"Error: File not found: {xmind_path}")
        sys.exit(1)

    print(f"Adding label '{label}' to node {node_id}")

    # Load XMind content
    content = read_xmind_content(xmind_path)

    # Find and update node
    found = False
    for sheet in content:
        node = find_node_by_id(sheet, node_id)
        if node:
            if add_label_to_node(node, label):
                print(
                    f"✓ Added label '{label}' to: {node.get('title', 'Unknown')[:60]}"
                )
            else:
                print(f"- Label '{label}' already exists on node")
            found = True
            break

    if not found:
        print(f"✗ Node not found: {node_id}")
        sys.exit(1)

    # Write back
    write_xmind_content(xmind_path, content)
    print(f"✓ Updated {xmind_path}")


if __name__ == "__main__":
    main()
