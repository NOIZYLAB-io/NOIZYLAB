#!/usr/bin/env python3
"""
Scan Duplicates (report-only): Walk a root (default: /Volumes/12TB) and identify duplicate files by SHA-1.
- Skips system/noisy dirs
- Supports size pre-filtering to avoid hashing small uniques
- Prints a JSON report with top duplicate groups and a CSV path for full list
"""
from __future__ import annotations
import os
import sys
import csv
import json
import hashlib
from pathlib import Path
from collections import defaultdict
from datetime import datetime

DEFAULT_ROOT = Path('/Volumes/12TB')
EXCLUDE_DIRS = {'.git', 'node_modules', '.cache', '__pycache__', '.Spotlight-V100', '.fseventsd', '.Trashes'}
REPORT_DIR = Path.home() / 'RSP' / 'Scripts'
CSV_OUT = REPORT_DIR / 'duplicate_files_12TB.csv'


def file_sha1(p: Path, buf: int = 1024 * 1024) -> str:
    h = hashlib.sha1()
    with p.open('rb') as f:
        while True:
            b = f.read(buf)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def scan(root: Path) -> dict:
    size_map = defaultdict(list)
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith('.') and d not in EXCLUDE_DIRS]
        p = Path(dirpath)
        for fname in filenames:
            fp = p / fname
            try:
                s = fp.stat().st_size
            except Exception:
                continue
            if s == 0:
                continue
            size_map[s].append(fp)

    dup_groups = []
    with CSV_OUT.open('w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['sha1', 'size', 'path'])
        for size, paths in size_map.items():
            if len(paths) < 2:
                continue
            hash_map = defaultdict(list)
            for pth in paths:
                try:
                    sha = file_sha1(pth)
                except Exception:
                    continue
                hash_map[sha].append(pth)
            for sha, files in hash_map.items():
                if len(files) > 1:
                    dup_groups.append({'sha1': sha, 'size': size, 'count': len(files), 'sample': [str(x) for x in files[:5]]})
                    for x in files:
                        w.writerow([sha, size, str(x)])

    dup_groups.sort(key=lambda d: (-d['size'] * d['count'], -d['count']))
    total_dupe_files = sum(d['count'] - 1 for d in dup_groups)
    total_dupe_bytes = sum(d['size'] * (d['count'] - 1) for d in dup_groups)
    return {
        'root': str(root),
        'groups': dup_groups[:50],
        'csv': str(CSV_OUT),
        'total_dupe_files': total_dupe_files,
        'total_dupe_bytes': total_dupe_bytes,
        'generated': datetime.now().isoformat(timespec='seconds')
    }


def main():
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_ROOT
    if not root.exists():
        print(json.dumps({'error': f'root does not exist: {root}'}))
        return
    report = scan(root)
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
