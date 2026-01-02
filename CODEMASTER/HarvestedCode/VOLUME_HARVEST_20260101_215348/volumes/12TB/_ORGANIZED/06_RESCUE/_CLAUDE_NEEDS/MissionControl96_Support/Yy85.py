#!/usr/bin/env python3
"""
summarize_conversations: build a lightweight table of contents for recent conversations.
- Lists recent N files with first heading or first line
- Optional filter by regex
- Appends a short summary section to MASTER_DIRECTORY_SCAN.md
"""
from __future__ import annotations
import argparse
import re
from datetime import datetime
from pathlib import Path

HOME = Path.home()
ARCHIVE = HOME / 'NoizyFish_Aquarium' / '🗣️ Conversations_Archive'
REPORT = HOME / 'RSP' / 'Scripts' / 'MASTER_DIRECTORY_SCAN.md'


def first_heading_or_line(text: str) -> str:
    for line in text.splitlines():
        if not line.strip():
            continue
        if line.startswith('#'):
            return line.strip().lstrip('#').strip()
        return (line.strip()[:160] + ('…' if len(line.strip()) > 160 else ''))
    return ''


def list_recent(n: int, pattern: str | None):
    files = []
    for p in ARCHIVE.glob('*'):
        if p.is_file():
            files.append((p.stat().st_mtime, p))
    files.sort(reverse=True)
    out = []
    rx = re.compile(pattern, re.IGNORECASE) if pattern else None
    for _, p in files[: n * 3]:  # oversample then filter
        try:
            text = p.read_text(errors='ignore')
        except Exception:
            continue
        if rx and not rx.search(text):
            continue
        out.append((p, first_heading_or_line(text)))
        if len(out) >= n:
            break
    return out


def append_report(items):
    lines = []
    lines.append('')
    lines.append('### 🗣️ Recent Conversations Snapshot')
    lines.append(f'- Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    for p, title in items:
        rel = p.name
        nice = title or '(no title)'
        lines.append(f'- {rel} — {nice}')
    lines.append('')
    try:
        with REPORT.open('a') as f:
            f.write('\n'.join(lines))
    except Exception:
        pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=int, default=10)
    ap.add_argument('--filter', help='Regex to filter content', default=None)
    args = ap.parse_args()
    items = list_recent(args.limit, args.filter)
    append_report(items)

if __name__ == '__main__':
    main()
