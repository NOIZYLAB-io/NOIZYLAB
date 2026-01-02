#!/usr/bin/env python3
"""
Master Directory Scanner (fast + safe)
- Scans common roots under the user home (incl. Desktop)
- Filters noisy dirs (node_modules, .git, caches, Library, etc.)
- Limits depth for speed (configurable)
- Produces:
  * MASTER_DIRECTORY_SCAN.md (summary report)
  * master_directory_index.json (detailed index)
  * master_directory_index.csv (tabular summary)
"""

from __future__ import annotations
import os
import sys
import json
import csv
import time
from pathlib import Path
from collections import Counter, defaultdict
from typing import Dict, List, Tuple

HOME = Path.home()
OUT_DIR = Path('/Users/rsp_ms/RSP/Scripts')
REPORT_MD = OUT_DIR / 'MASTER_DIRECTORY_SCAN.md'
REPORT_JSON = OUT_DIR / 'master_directory_index.json'
REPORT_CSV = OUT_DIR / 'master_directory_index.csv'

# Roots to scan (fast, targeted). Add more if needed.
ROOTS = [
    HOME / 'Desktop',
    HOME / 'Documents',
    HOME / 'Downloads',
    HOME / 'Developer',
    HOME / 'Projects',
    HOME / 'Code',
    HOME / 'Workspace',
    HOME / 'Scripts',
    HOME / 'RSP',
]

# Exclusion rules
EXCLUDE_DIR_NAMES = set([
    '.git', '.hg', '.svn',
    'node_modules', '.next', '.nuxt', '.cache', '.gradle', '.m2', '.venv', 'venv', 'env', '__pycache__',
    'Library', 'Applications', 'System', 'Volumes', 'tmp', 'private', 'cores',
])

# Ignore these file extensions for type stats (usually noise)
NOISY_EXTS = set(['.log', '.tmp', '.cache'])

MAX_DEPTH = 3  # depth relative to each root
SIZE_SAMPLE_LIMIT = 500000  # max files to stat in total for speed guard

PROJECT_INDICATORS = [
    '.git', '.vscode', 'package.json', 'requirements.txt', 'Cargo.toml', 'pom.xml',
    'composer.json', 'Gemfile', 'go.mod', 'Makefile', 'README.md'
]

start_time = time.time()
stat_count = 0


def depth_rel(path: Path, root: Path) -> int:
    try:
        return len(path.relative_to(root).parts)
    except Exception:
        return 0


def is_excluded_dir(name: str) -> bool:
    lname = name.lower()
    return name in EXCLUDE_DIR_NAMES or lname in EXCLUDE_DIR_NAMES


def safe_scandir(path: Path):
    try:
        return list(os.scandir(path))
    except Exception:
        return []


def scan_root(root: Path) -> Dict:
    global stat_count
    data = {
        'root': str(root),
        'dirs': [],  # list of dicts with summary per top-level under root
        'errors': []
    }
    if not root.exists():
        return data

    # Only scan immediate children as top-level buckets
    try:
        entries = safe_scandir(root)
        for entry in entries:
            if not entry.is_dir(follow_symlinks=False):
                continue
            name = entry.name
            if name.startswith('.'):
                continue
            if is_excluded_dir(name):
                continue
            subdir = Path(entry.path)
            summary = scan_dir_quick(subdir, max_depth=MAX_DEPTH)
            data['dirs'].append(summary)
    except Exception as e:
        data['errors'].append(f"{root}: {e}")

    return data


def scan_dir_quick(dir_path: Path, max_depth: int = 3) -> Dict:
    global stat_count
    total_size = 0
    file_count = 0
    dir_count = 0
    ext_counter: Counter[str] = Counter()
    project_like = False

    q = [dir_path]
    # BFS with depth check
    while q:
        current = q.pop(0)
        rel_depth = depth_rel(current, dir_path)
        if rel_depth > max_depth:
            continue
        try:
            with os.scandir(current) as it:
                for e in it:
                    name = e.name
                    if e.is_dir(follow_symlinks=False):
                        if name.startswith('.') or is_excluded_dir(name):
                            continue
                        dir_count += 1
                        # Project indicators check at shallow levels only to save time
                        if rel_depth <= 2 and any((current / ind).exists() for ind in PROJECT_INDICATORS):
                            project_like = True
                        # enqueue if depth allows
                        if rel_depth < max_depth:
                            q.append(Path(e.path))
                    elif e.is_file(follow_symlinks=False):
                        file_count += 1
                        if stat_count < SIZE_SAMPLE_LIMIT:
                            try:
                                total_size += e.stat().st_size
                                stat_count += 1
                            except Exception:
                                pass
                        # extension
                        _, ext = os.path.splitext(name)
                        if ext and ext.lower() not in NOISY_EXTS:
                            ext_counter[ext.lower()] += 1
        except Exception:
            # skip unreadable
            continue

    top_exts = ext_counter.most_common(5)

    return {
        'path': str(dir_path),
        'name': dir_path.name,
        'total_size_bytes': total_size,
        'file_count': file_count,
        'dir_count': dir_count,
        'top_extensions': top_exts,
        'project_like': project_like,
    }


def human_size(n: int) -> str:
    units = ['B', 'KB', 'MB', 'GB', 'TB']
    size = float(n)
    for u in units:
        if size < 1024:
            return f"{size:.1f} {u}"
        size /= 1024
    return f"{size:.1f} PB"


def write_reports(results: List[Dict]):
    # Flatten all dir summaries
    all_dirs: List[Dict] = []
    for r in results:
        all_dirs.extend(r.get('dirs', []))

    # Sort by size desc
    largest = sorted(all_dirs, key=lambda d: d['total_size_bytes'], reverse=True)

    # CSV
    with open(REPORT_CSV, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['name', 'path', 'size_bytes', 'size_human', 'files', 'dirs', 'project_like', 'top_extensions'])
        for d in largest:
            w.writerow([
                d['name'], d['path'], d['total_size_bytes'], human_size(d['total_size_bytes']),
                d['file_count'], d['dir_count'], d['project_like'], json.dumps(d['top_extensions'])
            ])

    # JSON
    with open(REPORT_JSON, 'w') as f:
        json.dump({'roots': [str(p) for p in ROOTS], 'max_depth': MAX_DEPTH, 'data': results}, f, indent=2)

    # Markdown summary
    elapsed = time.time() - start_time
    desktop_dirs = [d for d in results if d.get('root','').endswith('/Desktop')]
    desktop_items = desktop_dirs[0]['dirs'] if desktop_dirs else []

    project_like_count = sum(1 for d in all_dirs if d['project_like'])

    lines = []
    lines.append(f"# Master Directory Scan Report")
    lines.append("")
    lines.append(f"- Generated: {time.strftime('%Y-%m-%d %H:%M:%S')} ")
    lines.append(f"- Roots scanned (depth {MAX_DEPTH}):")
    for r in ROOTS:
        lines.append(f"  - {r}")
    lines.append(f"- Files stat'ed (sampled cap {SIZE_SAMPLE_LIMIT}): {stat_count}")
    lines.append(f"- Duration: {elapsed:.2f}s")
    lines.append("")

    # Desktop section
    lines.append("## Desktop Summary")
    if desktop_items:
        for d in sorted(desktop_items, key=lambda x: x['name'].lower()):
            lines.append(f"- {d['name']}: {human_size(d['total_size_bytes'])}, files={d['file_count']}, dirs={d['dir_count']}, project_like={d['project_like']}")
    else:
        lines.append("- No Desktop items scanned or Desktop not present.")
    lines.append("")

    # Largest dirs
    lines.append("## Top 20 Largest Directories (scanned scope)")
    for d in largest[:20]:
        exts = ', '.join([f"{e}:{c}" for e,c in d['top_extensions']]) if d['top_extensions'] else '—'
        lines.append(f"1. {d['name']} — {human_size(d['total_size_bytes'])} — files:{d['file_count']} dirs:{d['dir_count']} — {d['path']} — project_like:{d['project_like']} — top: {exts}")
    lines.append("")

    # Project-like but unmoved hint
    lines.append("## Project-like Folders Detected")
    for d in [x for x in all_dirs if x['project_like']]:
        lines.append(f"- {d['name']} — {d['path']}")
    if project_like_count == 0:
        lines.append("- None detected in scanned scope.")
    lines.append("")

    # Artifacts
    lines.append("## Artifacts")
    lines.append(f"- CSV: `{REPORT_CSV}`")
    lines.append(f"- JSON: `{REPORT_JSON}`")

    REPORT_MD.write_text('\n'.join(lines))


def main():
    results = []
    for root in ROOTS:
        results.append(scan_root(root))
    write_reports(results)
    print(f"✅ Scan complete. Report: {REPORT_MD}")
    print(f"   CSV: {REPORT_CSV}")
    print(f"   JSON: {REPORT_JSON}")

if __name__ == '__main__':
    main()
