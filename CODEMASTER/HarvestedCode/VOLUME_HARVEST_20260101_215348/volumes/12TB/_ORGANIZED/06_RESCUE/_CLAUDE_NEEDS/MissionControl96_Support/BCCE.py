#!/usr/bin/env python3
"""
search_conversations: fast grep over Conversations_Archive with context.

Usage:
  python3 search_conversations.py --query "vector db" --context 2
"""
from __future__ import annotations
import argparse
import re
from pathlib import Path

HOME = Path.home()
ARCHIVE = HOME / 'NoizyFish_Aquarium' / '🗣️ Conversations_Archive'


def iter_files():
    if not ARCHIVE.exists():
        return
    for p in ARCHIVE.rglob('*'):
        if p.is_file() and p.suffix.lower() in {'.md', '.mdx', '.txt', '.json', '.log', '.html'}:
            yield p


def search(query: str, context: int):
    pattern = re.compile(query, re.IGNORECASE)
    for p in iter_files():
        try:
            lines = p.read_text(errors='ignore').splitlines()
        except Exception:
            continue
        matches = []
        for i, line in enumerate(lines):
            if pattern.search(line):
                start = max(0, i - context)
                end = min(len(lines), i + context + 1)
                snippet = '\n'.join(lines[start:end])
                matches.append((i + 1, snippet))
        if matches:
            print(f"\n=== {p} ===")
            for ln, snip in matches[:5]:
                print(f"[line {ln}]\n{snip}\n---")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--query', required=True, help='Regex or literal to search')
    ap.add_argument('--context', type=int, default=2, help='Context lines')
    args = ap.parse_args()
    search(args.query, args.context)

if __name__ == '__main__':
    main()
