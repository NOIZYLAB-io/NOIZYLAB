#!/usr/bin/env python3
"""
Import a single URL into an Aquarium archive with dedupe and index update.
- Detects target archive by extension (svg -> Artwork_Archive)
- Downloads to a temp file, hashes, dedupes against manifest, writes final file
- Updates manifest and index
- Prints JSON summary
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen, Request

HOME = Path.home()
AQUARIUM = HOME / 'NoizyFish_Aquarium'
ARTWORK = AQUARIUM / '🎨 Artwork_Archive'
ARTWORK_INDEX = ARTWORK / 'ARTWORK_INDEX.md'
ARTWORK_MANIFEST = ARTWORK / 'artwork_manifest.json'

IMAGE_EXTS = {
    '.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg', '.avif', '.heic', '.bmp', '.tif', '.tiff',
    '.psd', '.ai', '.eps', '.pdf'
}


def file_sha1(p: Path, buf: int = 1024 * 1024) -> str:
    h = hashlib.sha1()
    with p.open('rb') as f:
        while True:
            b = f.read(buf)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def ensure_dirs():
    ARTWORK.mkdir(parents=True, exist_ok=True)


def load_manifest(path: Path) -> dict:
    if path.exists():
        try:
            return json.loads(path.read_text())
        except Exception:
            return {}
    return {}


def save_manifest(path: Path, data: dict):
    path.write_text(json.dumps(data, indent=2))


def write_artwork_index(manifest: dict):
    lines = []
    lines.append('# 🎨 Artwork Archive Index')
    lines.append('')
    lines.append(f'Archive: {ARTWORK}')
    lines.append(f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    lines.append('')
    lines.append(f"- Total items archived: {len(manifest)}")
    lines.append('')
    items = list(manifest.items())[-20:]
    if items:
        lines.append('## Recent items')
        for sha, meta in reversed(items):
            lines.append(f"- {Path(meta['archive_path']).name} ← {meta['original_path']}")
        lines.append('')
    ARTWORK_INDEX.write_text('\n'.join(lines))


def detect_archive(url: str) -> str:
    ext = Path(url.split('?')[0]).suffix.lower()
    if ext in IMAGE_EXTS:
        return 'artwork'
    return 'artwork'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--url', required=True)
    args = ap.parse_args()
    url = args.url

    target_archive = detect_archive(url)
    ensure_dirs()

    # Download
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(req) as resp:
        data = resp.read()

    # Temp file to hash
    with tempfile.NamedTemporaryFile(delete=False) as tf:
        tf.write(data)
        tmp_path = Path(tf.name)

    sha = file_sha1(tmp_path)
    if target_archive == 'artwork':
        manifest = load_manifest(ARTWORK_MANIFEST)
        if sha in manifest:
            # Already present
            tmp_path.unlink(missing_ok=True)
            print(json.dumps({'status': 'duplicate', 'sha1': sha, 'archive': str(ARTWORK)}))
            return
        # Name
        suggested = Path(url.split('/')[-1].split('?')[0])
        name = suggested.name if suggested.name else f'asset-{sha[:8]}.bin'
        dest = ARTWORK / name
        if dest.exists():
            stem, ext = dest.stem, dest.suffix
            dest = ARTWORK / f"{stem}-{sha[:8]}{ext}"
        shutil.move(str(tmp_path), str(dest))
        manifest[sha] = {
            'archive_path': str(dest),
            'original_path': url,
            'filename': dest.name,
            'size': dest.stat().st_size,
            'created_at': datetime.now().isoformat(timespec='seconds')
        }
        save_manifest(ARTWORK_MANIFEST, manifest)
        write_artwork_index(manifest)
        print(json.dumps({'status': 'imported', 'sha1': sha, 'path': str(dest), 'archive': str(ARTWORK)}))
        return


if __name__ == '__main__':
    main()
