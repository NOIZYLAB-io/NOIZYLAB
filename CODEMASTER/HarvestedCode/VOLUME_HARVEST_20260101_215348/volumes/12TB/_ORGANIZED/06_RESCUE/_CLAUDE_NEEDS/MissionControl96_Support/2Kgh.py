#!/usr/bin/env python3
"""
Setup Fishnet: Use an external volume as the main storage for Aquarium archives.

Actions:
- Ensure fishnet root exists (default: /Volumes/12TB/NoizyFish_Fishnet)
- For each archive (Artwork, Conversations, Music):
  - Move existing local archive dir there (merge if needed)
  - Create a symlink at the original Aquarium path pointing to the fishnet target

Safe and idempotent: Can be re-run; will detect existing symlinks/targets.
"""
from __future__ import annotations
import json
import os
import shutil
from pathlib import Path
from datetime import datetime

HOME = Path.home()
SCRIPTS = HOME / 'RSP' / 'Scripts'
CONFIG = SCRIPTS / 'noizygenie_config.json'
AQUARIUM = HOME / 'NoizyFish_Aquarium'

ARCHIVES = [
    '🎨 Artwork_Archive',
    '🗣️ Conversations_Archive',
    '🎵 Original_Music_Archive',
]


def load_config():
    cfg = {}
    if CONFIG.exists():
        try:
            cfg = json.loads(CONFIG.read_text())
        except Exception:
            cfg = {}
    return cfg


def ensure_symlink(local_dir: Path, fishnet_dir: Path, summary: dict):
    fishnet_dir.mkdir(parents=True, exist_ok=True)
    # If local is already a symlink to fishnet, done
    if local_dir.is_symlink():
        try:
            if local_dir.resolve() == fishnet_dir.resolve():
                summary['symlinks_ok'].append(str(local_dir))
                return
        except Exception:
            pass
        # Wrong symlink -> replace
        try:
            local_dir.unlink()
        except Exception:
            pass

    # If local exists as a real directory, merge contents into fishnet, then replace with symlink
    if local_dir.exists() and local_dir.is_dir():
        for item in local_dir.iterdir():
            target = fishnet_dir / item.name
            if not target.exists():
                try:
                    shutil.move(str(item), str(target))
                except Exception:
                    summary['errors'].append(f"move:{item}")
            else:
                # if both exist, skip; user can resolve manually later
                summary['skipped_existing'].append(str(target))
        # remove now-empty local dir
        try:
            local_dir.rmdir()
        except Exception:
            pass

    # Create symlink back to fishnet
    try:
        local_dir.parent.mkdir(parents=True, exist_ok=True)
        if not local_dir.exists():
            local_dir.symlink_to(fishnet_dir)
            summary['symlinks_created'].append(str(local_dir))
    except Exception:
        summary['errors'].append(f"symlink:{local_dir} -> {fishnet_dir}")


def main():
    cfg = load_config()
    fishnet_root = Path(os.path.expanduser(cfg.get('fishnet_root', '/Volumes/12TB/NoizyFish_Fishnet')))
    fishnet_root.mkdir(parents=True, exist_ok=True)

    summary = {
        'fishnet_root': str(fishnet_root),
        'archives': [],
        'symlinks_created': [],
        'symlinks_ok': [],
        'skipped_existing': [],
        'errors': [],
        'completed_at': datetime.now().isoformat(timespec='seconds')
    }

    for name in ARCHIVES:
        local_dir = AQUARIUM / name
        fishnet_dir = fishnet_root / name
        ensure_symlink(local_dir, fishnet_dir, summary)
        summary['archives'].append({'local': str(local_dir), 'fishnet': str(fishnet_dir)})

    print(json.dumps(summary, indent=2))


if __name__ == '__main__':
    main()
