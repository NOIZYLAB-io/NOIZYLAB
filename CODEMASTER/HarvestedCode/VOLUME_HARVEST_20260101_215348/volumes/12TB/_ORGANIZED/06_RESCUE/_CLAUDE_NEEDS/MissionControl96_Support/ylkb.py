#!/usr/bin/env python3
"""
NoizyGenie Orchestrator: one command to scan, organize, clean, and archive.

Runs available automation scripts in ~/RSP/Scripts:
- master_directory_scan.py
- move_working_sets.py
- organize_aquarium.py
- superclean.py
- collect_artwork.py
- collect_conversations.py

Usage:
  python3 noizygenie_orchestrator.py --all (default) or pick flags
"""
from __future__ import annotations
import argparse
import json
import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime

HOME = Path.home()
SCRIPTS = HOME / 'RSP' / 'Scripts'
REPORT = SCRIPTS / 'MASTER_DIRECTORY_SCAN.md'

SCRIPT_ORDER = [
    'master_directory_scan.py',
    'move_working_sets.py',
    'organize_aquarium.py',
    'superclean.py',
    'collect_artwork.py',
    'collect_conversations.py',
    'collect_original_music.py',
]

AVAILABLE = {s: (SCRIPTS / s) for s in SCRIPT_ORDER}


def run_script(path: Path) -> dict:
    if not path.exists():
        return {'status': 'missing', 'script': str(path.name)}
    try:
        proc = subprocess.run(
            [sys.executable or 'python3', str(path)],
            capture_output=True,
            text=True,
            cwd=str(SCRIPTS),
            timeout=60 * 20,
        )
        stdout = (proc.stdout or '').strip()
        stderr = (proc.stderr or '').strip()
        status = 'ok' if proc.returncode == 0 else 'error'
        parsed = None
        if stdout:
            try:
                parsed = json.loads(stdout)
            except Exception:
                parsed = None
        return {
            'status': status,
            'script': path.name,
            'returncode': proc.returncode,
            'stdout': stdout[-4000:],
            'stderr': stderr[-4000:],
            'parsed': parsed,
        }
    except subprocess.TimeoutExpired:
        return {'status': 'timeout', 'script': path.name}
    except Exception as e:
        return {'status': 'exception', 'script': path.name, 'error': str(e)}


def append_summary(summary: dict):
    lines = []
    lines.append('')
    lines.append('### 🚀 Orchestrator Summary')
    lines.append(f"- Run at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    for item in summary.get('steps', []):
        status = item.get('status')
        script = item.get('script')
        detail = ''
        parsed = item.get('parsed') or {}
        # include compact interesting metrics if available
        if isinstance(parsed, dict):
            interesting_keys = ['found', 'copied', 'skipped_dupe', 'skipped_large',
                                'junk_removed', 'empties_removed', 'moved_projects', 'moved_files']
            kv = {k: v for k, v in parsed.items() if k in interesting_keys}
            if kv:
                detail = ' ' + json.dumps(kv, ensure_ascii=False)
        lines.append(f"- {script}: {status}{detail}")
    lines.append('')
    try:
        with REPORT.open('a') as f:
            f.write('\n'.join(lines))
    except Exception:
        pass


def main():
    parser = argparse.ArgumentParser(description='NoizyGenie Orchestrator')
    parser.add_argument('--scan', action='store_true', help='Run master_directory_scan.py')
    parser.add_argument('--move-working-sets', action='store_true', help='Run move_working_sets.py')
    parser.add_argument('--organize', action='store_true', help='Run organize_aquarium.py')
    parser.add_argument('--superclean', action='store_true', help='Run superclean.py')
    parser.add_argument('--artwork', action='store_true', help='Run collect_artwork.py')
    parser.add_argument('--conversations', action='store_true', help='Run collect_conversations.py')
    parser.add_argument('--music', action='store_true', help='Run collect_original_music.py')
    parser.add_argument('--all', action='store_true', help='Run all tasks (default)')
    args = parser.parse_args()

    selected = []
    if any([args.scan, args.move_working_sets, args.organize, args.superclean, args.artwork, args.conversations, args.music]):
        if args.scan: selected.append('master_directory_scan.py')
        if args.move_working_sets: selected.append('move_working_sets.py')
        if args.organize: selected.append('organize_aquarium.py')
        if args.superclean: selected.append('superclean.py')
        if args.artwork: selected.append('collect_artwork.py')
        if args.conversations: selected.append('collect_conversations.py')
        if args.music: selected.append('collect_original_music.py')
    else:
        selected = SCRIPT_ORDER[:]

    steps = []
    for name in selected:
        res = run_script(AVAILABLE[name])
        steps.append(res)

    summary = {'steps': steps}
    append_summary(summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
