#!/usr/bin/env python3
"""
Collect Conversations: Gather chat/transcript style files into
~/NoizyFish_Aquarium/🗣️ Conversations_Archive with dedupe and indexing.

What it does
- Scans common roots (Desktop, Documents, Downloads, RSP, Projects, Code, Workspace,
  NoizyGenie_Master_Workspace, NoizyFish_Aquarium)
- Targets likely conversation files by extension and name patterns
- Deduplicates by SHA-1; keeps one canonical copy
- Name collision with different content appends -<short-hash>
- Creates CONVERSATIONS_INDEX.md and conversations_manifest.json
- Skips system/noisy directories
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

HOME = Path.home()
SCRIPTS = HOME / 'RSP' / 'Scripts'
AQUARIUM = HOME / 'NoizyFish_Aquarium'
ARCHIVE = AQUARIUM / '🗣️ Conversations_Archive'
INDEX_MD = ARCHIVE / 'CONVERSATIONS_INDEX.md'
MANIFEST_JSON = ARCHIVE / 'conversations_manifest.json'
CONFIG_JSON = SCRIPTS / 'noizygenie_config.json'

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

# Likely conversation file extensions
CONVO_EXTS = {'.md', '.mdx', '.txt', '.json', '.log', '.html'}

# Heuristic name patterns (case-insensitive)
NAME_PATTERNS = [
    'chat', 'conversation', 'convo', 'transcript', 'dialog', 'dialogue', 'log',
    'noizygenie', 'hand of god', 'omnipotent', 'trillion', 'ideas', 'work of today'
]

MAX_FILE_SIZE_MB = 25  # safety cap per file


def load_config_overrides():
    global ROOTS, EXCLUDE_DIR_NAMES, CONVO_EXTS, NAME_PATTERNS, MAX_FILE_SIZE_MB
    if not CONFIG_JSON.exists():
        return
    try:
        cfg = json.loads(CONFIG_JSON.read_text())
    except Exception:
        return
    roots = cfg.get('conversation_roots')
    if isinstance(roots, list):
        ROOTS = [Path(os.path.expanduser(r)) for r in roots]
    excludes = cfg.get('exclude_dir_names')
    if isinstance(excludes, list):
        EXCLUDE_DIR_NAMES = set(excludes)
    exts = cfg.get('conversation_exts')
    if isinstance(exts, list):
        CONVO_EXTS = set(e if e.startswith('.') else f'.{e}' for e in exts)
    pats = cfg.get('conversation_name_patterns')
    if isinstance(pats, list):
        NAME_PATTERNS = [str(p).lower() for p in pats]
    max_mb = cfg.get('conversation_max_file_mb')
    if isinstance(max_mb, (int, float)):
        MAX_FILE_SIZE_MB = int(max_mb)


def is_excluded_dir(name: str) -> bool:
    lname = name.lower()
    return name in EXCLUDE_DIR_NAMES or lname in EXCLUDE_DIR_NAMES


def file_sha1(p: Path, buf: int = 1024 * 1024) -> str:
    h = hashlib.sha1()
    with p.open('rb') as f:
        while True:
            b = f.read(buf)
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


def maybe_conversation_file(path: Path) -> bool:
    # Extension check
    if path.suffix.lower() not in CONVO_EXTS:
        return False
    # Name heuristic
    name_lower = path.name.lower()
    if any(k in name_lower for k in NAME_PATTERNS):
        return True
    # Lightweight content heuristic: check first 4KB for conversation-like markers
    try:
        if path.suffix.lower() in {'.md', '.mdx', '.txt'}:
            with path.open('r', errors='ignore') as f:
                sample = f.read(4096).lower()
            if any(s in sample for s in ['user:', 'assistant:', 'system:', '###', '```']):
                return True
        elif path.suffix.lower() in {'.json'}:
            # Look for a structure with messages or similar
            with path.open('r', errors='ignore') as f:
                sample = f.read(4096)
            if any(k in sample for k in ['"messages"', '"role"', '"content"']):
                return True
        elif path.suffix.lower() in {'.html', '.log'}:
            with path.open('r', errors='ignore') as f:
                sample = f.read(4096).lower()
            if any(s in sample for s in ['chat', 'conversation', 'transcript', 'assistant']):
                return True
    except Exception:
        return False
    return False


def safe_copy(src: Path, manifest: Dict[str, Dict]) -> Tuple[bool, Path, str]:
    try:
        # size cap
        if src.stat().st_size > MAX_FILE_SIZE_MB * 1024 * 1024:
            return False, src, 'too_large'
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


def scan_and_collect() -> Dict:
    found = 0
    copied = 0
    skipped_dupe = 0
    skipped_large = 0
    manifest = load_manifest()

    for root in ROOTS:
        if not root.exists():
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if not d.startswith('.') and not is_excluded_dir(d)]
            p = Path(dirpath)
            for fname in filenames:
                src = p / fname
                if str(src).startswith(str(ARCHIVE)):
                    continue
                if not maybe_conversation_file(src):
                    continue
                found += 1
                ok, target, info = safe_copy(src, manifest)
                if ok:
                    copied += 1
                else:
                    if info == 'duplicate':
                        skipped_dupe += 1
                    elif info == 'too_large':
                        skipped_large += 1
    save_manifest(manifest)
    write_index(manifest)
    return {
        'found': found,
        'copied': copied,
        'skipped_dupe': skipped_dupe,
        'skipped_large': skipped_large,
        'archive': str(ARCHIVE)
    }


def write_index(manifest: Dict[str, Dict]):
    lines = []
    lines.append('# 🗣️ Conversations Archive Index')
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


def main():
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    load_config_overrides()
    summary = scan_and_collect()
    print(json.dumps(summary, indent=2))

if __name__ == '__main__':
    main()
