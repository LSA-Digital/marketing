#!/usr/bin/env python3
import json
import zipfile
import sys
import os


def read_xmind_content(xmind_path):
    with zipfile.ZipFile(xmind_path, "r") as zf:
        return json.loads(zf.read("content.json"))


def print_node(node, depth=0):
    title = node.get("title", "Unknown")
    node_id = node.get("id", "No ID")
    labels = node.get("labels", [])

    print(f"{'  ' * depth}- {title} (ID: {node_id}) Labels: {labels}")

    children = node.get("children", {})
    if isinstance(children, dict) and "attached" in children:
        for child in children["attached"]:
            print_node(child, depth + 1)
    elif isinstance(children, list):
        for child in children:
            print_node(child, depth + 1)


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 dump_xmind_tree.py <xmind_file>")
        sys.exit(1)

    xmind_path = sys.argv[1]
    content = read_xmind_content(xmind_path)

    for sheet in content:
        print(f"Sheet: {sheet.get('title', 'Untitled')}")
        if "rootTopic" in sheet:
            print_node(sheet["rootTopic"])


if __name__ == "__main__":
    main()
