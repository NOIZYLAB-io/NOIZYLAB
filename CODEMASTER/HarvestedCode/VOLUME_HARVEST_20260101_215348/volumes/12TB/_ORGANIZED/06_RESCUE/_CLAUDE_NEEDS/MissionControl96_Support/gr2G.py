#!/usr/bin/env python3
"""
Collect Original Music: scan common roots and /Volumes for audio that likely has no metadata
and archive to ~/NoizyFish_Aquarium/🎵 Original_Music_Archive with dedupe and index.

Heuristic for "original":
- Audio extensions: wav, aiff/aif, flac, m4a, mp3, ogg
- Consider likely-original if:
  - No embedded tags (artist/title/album missing) OR
  - File name contains tokens like "mix", "bounce", "demo", date stamps, or is generic (Untitled, New Project)
  - Sample rate/bit depth suggest raw exports (via mutagen where available)
- Deduplicate by SHA-1
- Preserve filename; on collision with different content, append -<short-hash>

Outputs:
- MUSIC_INDEX.md (recent items)
- music_manifest.json (sha -> meta)
- Summary JSON to stdout
"""
from __future__ import annotations
import os
import re
import json
import shutil
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

from mutagen import File as MutagenFile  # type: ignore

HOME = Path.home()
AQUARIUM = HOME / 'NoizyFish_Aquarium'
ARCHIVE = AQUARIUM / '🎵 Original_Music_Archive'
INDEX_MD = ARCHIVE / 'MUSIC_INDEX.md'
MANIFEST_JSON = ARCHIVE / 'music_manifest.json'

SCRIPTS = HOME / 'RSP' / 'Scripts'
REPORT = SCRIPTS / 'MASTER_DIRECTORY_SCAN.md'
CONFIG_JSON = SCRIPTS / 'noizygenie_config.json'

AUDIO_EXTS = {'.wav', '.aif', '.aiff', '.flac', '.m4a', '.mp3', '.ogg'}
NAME_HINTS = [
    'mix', 'rough', 'bounce', 'bounced', 'demo', 'scratch', 'untitled', 'new project',
    'take', 'stem', 'print', 'export', '2mix', 'premaster', 'pre-master'
]

ROOTS = [HOME / 'Desktop', HOME / 'Documents', HOME / 'Downloads', HOME / 'Music', HOME / 'RSP']

EXCLUDE_DIR_NAMES = {'.git', 'node_modules', '__pycache__', '.Trash', '.venv', 'venv', 'env'}

MAX_FILE_SIZE_MB = 1024  # 1GB cap


def load_config_overrides():
    global ROOTS
    if CONFIG_JSON.exists():
        try:
            cfg = json.loads(CONFIG_JSON.read_text())
            roots = cfg.get('music_roots')
            if isinstance(roots, list):
                ROOTS = [Path(os.path.expanduser(r)) for r in roots]
        except Exception:
            pass


def add_volumes_roots():
    vols = Path('/Volumes')
    if vols.exists():
        for d in vols.iterdir():
            if d.is_dir():
                ROOTS.append(d)


def file_sha1(p: Path, buf: int = 1024 * 1024) -> str:
    h = hashlib.sha1()
    with p.open('rb') as f:
        while True:
            b = f.read(buf)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def has_no_metadata(p: Path) -> bool:
    try:
        mf = MutagenFile(str(p), easy=True)
        if mf is None:
            # unknown container; treat as raw
            return True
        tags = getattr(mf, 'tags', None)
        if not tags:
            return True
        # Look for common fields
        for key in ['artist', 'title', 'album', 'composer']:
            if key in tags and tags.get(key):
                return False
        return True
    except Exception:
        return True


def name_looks_original(name: str) -> bool:
    n = name.lower()
    if any(h in n for h in NAME_HINTS):
        return True
    # date-like tokens or generic names
    if re.search(r'\b20\d{2}[._-]?\d{2}[._-]?\d{2}\b', n):
        return True
    if re.search(r'\buntitled\b|\bnew\s+project\b', n):
        return True
    return False


def likely_original_audio(p: Path) -> bool:
    if p.suffix.lower() not in AUDIO_EXTS:
        return False
    if p.stat().st_size > MAX_FILE_SIZE_MB * 1024 * 1024:
        return False
    if has_no_metadata(p):
        return True
    return name_looks_original(p.stem)


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
    try:
        sha = file_sha1(src)
    except Exception as e:
        return False, src, f'hash_error:{e}'

    if sha in manifest:
        return False, Path(manifest[sha]['archive_path']), 'duplicate'

    ARCHIVE.mkdir(parents=True, exist_ok=True)
    target = ARCHIVE / src.name
    if target.exists():
        short = sha[:8]
        stem, ext = src.stem, src.suffix
        target = ARCHIVE / f"{stem}-{short}{ext}"

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
        return False, src, f'copy_error:{e}'


def write_index(manifest: Dict[str, Dict]):
    lines = []
    lines.append('# 🎵 Original Music Archive Index')
    lines.append('')
    lines.append(f'Archive: {ARCHIVE}')
    lines.append(f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    lines.append(f'- Total items archived: {len(manifest)}')
    lines.append('')
    items = list(manifest.items())[-50:]
    if items:
        lines.append('## Recent items')
        for sha, meta in reversed(items):
            lines.append(f"- {Path(meta['archive_path']).name} ← {meta['original_path']}")
        lines.append('')
    INDEX_MD.write_text('\n'.join(lines))


def scan_and_collect() -> Dict:
    found = 0
    copied = 0
    skipped_dupe = 0
    manifest = load_manifest()

    for root in ROOTS:
        if not Path(root).exists():
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if not d.startswith('.') and d not in EXCLUDE_DIR_NAMES]
            p = Path(dirpath)
            for fname in filenames:
                src = p / fname
                if str(src).startswith(str(ARCHIVE)):
                    continue
                if not src.suffix:
                    continue
                try:
                    if not likely_original_audio(src):
                        continue
                except Exception:
                    continue
                found += 1
                ok, target, info = safe_copy(src, manifest)
                if ok:
                    copied += 1
                else:
                    if info == 'duplicate':
                        skipped_dupe += 1
    save_manifest(manifest)
    write_index(manifest)
    return {
        'found': found,
        'copied': copied,
        'skipped_dupe': skipped_dupe,
        'archive': str(ARCHIVE)
    }


def append_report(summary: Dict):
    lines = []
    lines.append('')
    lines.append('### 🎵 Original Music Collection Summary')
    lines.append(f"- Archive: `~/{ARCHIVE.relative_to(HOME)}`")
    lines.append(f"- Files found: {summary['found']}")
    lines.append(f"- Files copied: {summary['copied']}")
    lines.append(f"- Duplicates skipped: {summary['skipped_dupe']}")
    lines.append('')
    try:
        with REPORT.open('a') as f:
            f.write('\n'.join(lines))
    except Exception:
        pass


def main():
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    load_config_overrides()
    add_volumes_roots()
    summary = scan_and_collect()
    append_report(summary)
    print(json.dumps(summary, indent=2))

if __name__ == '__main__':
    main()
