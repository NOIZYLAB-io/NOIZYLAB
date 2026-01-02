#!/usr/bin/env python3
import os
import shutil
import json
from pathlib import Path
from datetime import datetime

HOME = Path.home()
DESKTOP = HOME / 'Desktop'
AQUARIUM = HOME / 'NoizyFish_Aquarium'
CATEGORY = '📚 Learning_Projects'
TARGET_DIR = AQUARIUM / CATEGORY

CANDIDATES = [
    'RSP_Selects',
    'WORK OF TODAY',
    'Hand of God',
]


def unique_target(path: Path) -> Path:
    if not path.exists():
        return path
    base = path.name
    parent = path.parent
    if path.is_file() and '.' in base:
        stem, ext = base.rsplit('.', 1)
        ext = '.' + ext
    else:
        stem, ext = base, ''
    i = 2
    while True:
        candidate = parent / f"{stem}-{i}{ext}"
        if not candidate.exists():
            return candidate
        i += 1


def move_folder(src: Path, dst_parent: Path):
    dst_parent.mkdir(parents=True, exist_ok=True)
    target = unique_target(dst_parent / src.name)
    shutil.move(str(src), str(target))
    return target


def main():
    moved = []
    skipped = []
    errors = []

    for name in CANDIDATES:
        src = DESKTOP / name
        try:
            if src.exists() and src.is_dir():
                target = move_folder(src, TARGET_DIR)
                moved.append({'name': name, 'from': str(src), 'to': str(target)})
            else:
                skipped.append({'name': name, 'reason': 'not found or not a directory'})
        except Exception as e:
            errors.append({'name': name, 'error': str(e)})

    print(json.dumps({
        'category': CATEGORY,
        'target_dir': str(TARGET_DIR),
        'moved_count': len(moved),
        'moved': moved,
        'skipped': skipped,
        'errors': errors
    }, indent=2))

if __name__ == '__main__':
    main()
