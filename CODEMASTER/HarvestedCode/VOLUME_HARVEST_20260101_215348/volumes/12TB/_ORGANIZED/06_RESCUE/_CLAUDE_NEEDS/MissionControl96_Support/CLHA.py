#!/usr/bin/env python3
"""
Superclean: Keep everything super clean
- Removes junk files (.DS_Store, '._*', Thumbs.db, desktop.ini, Icon\r)
- Prunes empty directories under selected roots (safely, with protections)
- Skips system/noisy dirs and protects Aquarium top-level categories
- Appends a concise summary to MASTER_DIRECTORY_SCAN.md
"""
from __future__ import annotations
import os
from pathlib import Path
from datetime import datetime
import fnmatch

HOME = Path.home()
SCRIPTS = HOME / 'RSP' / 'Scripts'
REPORT_MD = SCRIPTS / 'MASTER_DIRECTORY_SCAN.md'
AQUARIUM = HOME / 'NoizyFish_Aquarium'

ROOTS = [
    HOME / 'Desktop', HOME / 'Documents', HOME / 'Downloads', HOME / 'Developer',
    HOME / 'Projects', HOME / 'Code', HOME / 'Workspace', HOME / 'RSP', AQUARIUM
]

EXCLUDE_DIR_NAMES = {
    '.git', '.hg', '.svn', 'node_modules', '.next', '.nuxt', '.cache', '.gradle', '.m2',
    '.venv', 'venv', 'env', '__pycache__', 'Library', 'Applications', 'System', 'Volumes',
    'tmp', 'private', 'cores', '.Trash'
}

JUNK_PATTERNS = [
    '.DS_Store', 'Thumbs.db', 'desktop.ini', 'Icon\r',
]
# AppleDouble resource forks (._filename) pattern handled via glob

# Category protection under Aquarium
PROTECT_AQUARIUM_LEVELS = {
    '🐍 Python_Projects', '🌟 JavaScript_Projects', '🦀 Rust_Projects', '☕ Java_Projects',
    '💎 Ruby_Projects', '🐹 Go_Projects', '🌐 Web_Projects', '🤖 AI_ML_Projects',
    '🎮 Game_Projects', '📱 Mobile_Projects', '🐳 DevOps_Projects', '📊 Data_Projects',
    '🧞‍♂️ NoizyGenie_Creations', '🔧 Tools_And_Utilities', '🧪 Experimental', '📚 Learning_Projects'
}


def is_excluded_dir(name: str) -> bool:
    lname = name.lower()
    return name in EXCLUDE_DIR_NAMES or lname in EXCLUDE_DIR_NAMES


def remove_junk(root: Path) -> int:
    removed = 0
    for dirpath, dirnames, filenames in os.walk(root):
        # prune noisy dirs
        dirnames[:] = [d for d in dirnames if not d.startswith('.') and not is_excluded_dir(d)]
        p = Path(dirpath)
        # files matching patterns
        for fname in list(filenames):
            # explicit junk names
            if fname in JUNK_PATTERNS:
                fp = p / fname
                try:
                    fp.unlink()
                    removed += 1
                except Exception:
                    pass
            # AppleDouble pattern
            if fname.startswith('._'):
                fp = p / fname
                try:
                    fp.unlink()
                    removed += 1
                except Exception:
                    pass
    return removed


def prune_empty(root: Path) -> int:
    removed = 0
    # Build protection set
    protect: set[Path] = {root}
    if root == AQUARIUM:
        protect.add(AQUARIUM)
        for name in PROTECT_AQUARIUM_LEVELS:
            protect.add(AQUARIUM / name)
    for dirpath, dirnames, filenames in os.walk(root, topdown=False):
        p = Path(dirpath)
        if p in protect:
            continue
        if is_excluded_dir(p.name) or p.name.startswith('.'):
            continue
        # never remove within protected paths
        if any(str(p).startswith(str(pp)) for pp in protect):
            # allow pruning deeper under protected as long as not the protected node itself
            pass
        try:
            if not any(p.iterdir()):
                p.rmdir()
                removed += 1
        except Exception:
            continue
    return removed


def append_report(junk_removed: int, empties_removed: int):
    try:
        lines = [
            '',
            '### ✨ Superclean Summary',
            f'- Junk files removed: {junk_removed}',
            f'- Empty folders removed: {empties_removed}',
            f'- Run at: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
        ]
        with REPORT_MD.open('a') as f:
            f.write('\n'.join(lines) + '\n')
    except Exception:
        pass


def main():
    total_junk = 0
    total_empty = 0
    for root in ROOTS:
        if not root.exists():
            continue
        total_junk += remove_junk(root)
        total_empty += prune_empty(root)
    append_report(total_junk, total_empty)
    print({
        'junk_removed': total_junk,
        'empties_removed': total_empty
    })

if __name__ == '__main__':
    main()
