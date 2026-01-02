#!/usr/bin/env python3
"""
Collect Artwork: Scan for image/design files, dedupe by content hash, and copy to
~/NoizyFish_Aquarium/🎨 Artwork_Archive with an index.

- Scans common roots (Desktop, Documents, Downloads, RSP, Projects, Code, Workspace,
  NoizyGenie_Master_Workspace, NoizyFish_Aquarium)
- Ignores system/noisy dirs (.git, node_modules, Library, etc.)
- Deduplicates by SHA1 to avoid copying the same content twice
- Preserves original filenames; on name collision with different content, adds -<short-hash>
- Generates ARTWORK_INDEX.md and artwork_manifest.json in the archive
- Prints a JSON summary {found, copied, skipped_dupe, archive}
"""
from __future__ import annotations
import os
import shutil
import hashlib
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

HOME = Path.home()
AQUARIUM = HOME / 'NoizyFish_Aquarium'
ARCHIVE = AQUARIUM / '🎨 Artwork_Archive'
INDEX_MD = ARCHIVE / 'ARTWORK_INDEX.md'
MANIFEST_JSON = ARCHIVE / 'artwork_manifest.json'

ROOTS = [
    HOME / 'Desktop', HOME / 'Documents', HOME / 'Downloads', HOME / 'RSP',
    HOME / 'Projects', HOME / 'Code', HOME / 'Workspace',
    HOME / 'NoizyGenie_Master_Workspace', HOME / 'NoizyFish_Aquarium'
]

EXCLUDE_DIR_NAMES = {
    '.git', '.hg', '.svn', 'node_modules', '.next', '.nuxt', '.cache', '.gradle', '.m2',
    '.venv', 'venv', 'env', '__pycache__', 'Library', 'Applications', 'System', 'Volumes',
    'tmp', 'private', 'cores', '.Trash'
}

IMAGE_EXTS = {
    '.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg', '.avif', '.heic', '.bmp', '.tif', '.tiff',
    '.psd', '.ai', '.eps', '.pdf'
}


def is_excluded_dir(name: str) -> bool:
    lname = name.lower()
    return name in EXCLUDE_DIR_NAMES or lname in EXCLUDE_DIR_NAMES


def file_sha1(path: Path, buf_size: int = 1024 * 1024) -> str:
    h = hashlib.sha1()
    with path.open('rb') as f:
        while True:
            b = f.read(buf_size)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def load_manifest() -> Dict[str, Dict]:
    if MANIFEST_JSON.exists():
        try:
            return json.loads(MANIFEST_JSON.read_text())
        except Exception:
            return {}
    return {}


def save_manifest(m: Dict[str, Dict]):
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    MANIFEST_JSON.write_text(json.dumps(m, indent=2))


def safe_copy(src: Path, manifest: Dict[str, Dict]) -> Tuple[bool, Path, str]:
    """Copy to ARCHIVE, dedupe by sha1. Returns (copied, target, reason|hash)."""
    try:
        sha = file_sha1(src)
    except Exception as e:
        return False, src, f"hash_error:{e}"

    if sha in manifest:
        # Already archived
        return False, Path(manifest[sha]['archive_path']), 'duplicate'

    # Base target path
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    base = ARCHIVE / src.name
    target = base

    # If a different file with same name exists, disambiguate by short hash
    if target.exists():
        short = sha[:8]
        stem = src.stem
        ext = src.suffix
        target = ARCHIVE / f"{stem}-{short}{ext}"

    # Perform copy
    try:
        shutil.copy2(str(src), str(target))
        manifest[sha] = {
            'archive_path': str(target),
            'original_path': str(src),
            'filename': src.name,
            'size': src.stat().st_size,
            'created_at': datetime.now().isoformat(timespec='seconds')
        }
        return True, target, sha
    except Exception as e:
        return False, src, f"copy_error:{e}"


def scan_and_collect() -> Dict:
    found = 0
    copied = 0
    skipped_dupe = 0
    ext_counts: Dict[str, int] = {}
    manifest = load_manifest()

    for root in ROOTS:
        if not root.exists():
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            # prune noisy dirs
            dirnames[:] = [d for d in dirnames if not d.startswith('.') and not is_excluded_dir(d)]
            p = Path(dirpath)
            for fname in filenames:
                ext = Path(fname).suffix.lower()
                if ext in IMAGE_EXTS:
                    src = p / fname
                    # skip files already in archive
                    if str(src).startswith(str(ARCHIVE)):
                        continue
                    found += 1
                    ok, target, info = safe_copy(src, manifest)
                    if ok:
                        copied += 1
                        ext_counts[ext] = ext_counts.get(ext, 0) + 1
                    else:
                        if info == 'duplicate':
                            skipped_dupe += 1
                        # else hash/copy error ignored but not counted as dup
    save_manifest(manifest)
    write_index(manifest, ext_counts)
    return {
        'found': found,
        'copied': copied,
        'skipped_dupe': skipped_dupe,
        'archive': str(ARCHIVE)
    }


def write_index(manifest: Dict[str, Dict], ext_counts: Dict[str, int]):
    lines = []
    lines.append('# 🎨 Artwork Archive Index')
    lines.append('')
    lines.append(f'Archive: {ARCHIVE}')
    lines.append(f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    lines.append('')
    lines.append(f'- Total items archived: {len(manifest)}')
    if ext_counts:
        lines.append('- By extension:')
        for ext, n in sorted(ext_counts.items(), key=lambda x: (-x[1], x[0])):
            lines.append(f'  - {ext}: {n}')
    lines.append('')
    # Show up to 20 recent items
    items = list(manifest.items())[-20:]
    if items:
        lines.append('## Recent items')
        for sha, meta in reversed(items):
            lines.append(f"- {Path(meta['archive_path']).name} ← {meta['original_path']}")
        lines.append('')
    INDEX_MD.write_text('\n'.join(lines))


def main():
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    summary = scan_and_collect()
    print(json.dumps(summary, indent=2))

if __name__ == '__main__':
    main()
