#!/usr/bin/env python3
"""
NoizyFish Aquarium Organizer
- Creates ~/NoizyFish_Aquarium with project-first categories
- Detects projects by common indicators and moves whole project folders
- Falls back to extension-based bucketing for loose files (non-project items)
- Skips system/noisy dirs and the script's own working folder
- Idempotent-ish: avoids overwriting; adds numeric suffix on conflicts
- Writes AQUIARIUM_INDEX.md summary under the aquarium root
"""
from __future__ import annotations
import os
import shutil
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

HOME = Path.home()
AQUARIUM = HOME / 'NoizyFish_Aquarium'
AQUARIUM_INDEX = AQUARIUM / 'AQUARIUM_INDEX.md'

# Scan roots
ROOTS = [
    HOME / 'Desktop', HOME / 'Documents', HOME / 'Downloads', HOME / 'Developer',
    HOME / 'Projects', HOME / 'Code', HOME / 'Workspace', HOME / 'RSP'
]

# Exclusions
EXCLUDE_DIR_NAMES = {
    '.git', '.hg', '.svn', 'node_modules', '.next', '.nuxt', '.cache', '.gradle', '.m2',
    '.venv', 'venv', 'env', '__pycache__', 'Library', 'Applications', 'System', 'Volumes',
    'tmp', 'private', 'cores', '.Trash'
}

# Project indicators
INDICATORS = [
    '.git', '.vscode', 'package.json', 'requirements.txt', 'Cargo.toml', 'pom.xml',
    'composer.json', 'Gemfile', 'go.mod', 'Makefile', 'README.md'
]

CATEGORY_MAP = {
    'js': '🌟 JavaScript_Projects',
    'ts': '🌟 JavaScript_Projects',
    'json': '🌟 JavaScript_Projects',
    'py': '🐍 Python_Projects',
    'rs': '🦀 Rust_Projects',
    'java': '☕ Java_Projects',
    'kt': '☕ Java_Projects',
    'rb': '💎 Ruby_Projects',
    'go': '🐹 Go_Projects',
    'html': '🌐 Web_Projects',
    'css': '🌐 Web_Projects',
    'md': '🔧 Tools_And_Utilities',
    'sh': '🔧 Tools_And_Utilities',
}

CATEGORIES = [
    '🐍 Python_Projects', '🌟 JavaScript_Projects', '🦀 Rust_Projects', '☕ Java_Projects',
    '💎 Ruby_Projects', '🐹 Go_Projects', '🌐 Web_Projects', '🤖 AI_ML_Projects',
    '🎮 Game_Projects', '📱 Mobile_Projects', '🐳 DevOps_Projects', '📊 Data_Projects',
    '🧞‍♂️ NoizyGenie_Creations', '🔧 Tools_And_Utilities', '🧪 Experimental', '📚 Learning_Projects'
]

MAX_DEPTH_DIR_FIND = 3  # how deep to look for indicators

# Will be set at runtime to avoid moving our working folder
RUNTIME_EXCLUDES: List[Path] = []


def is_excluded_dir(name: str) -> bool:
    lname = name.lower()
    return name in EXCLUDE_DIR_NAMES or lname in EXCLUDE_DIR_NAMES


def detect_project_category(path: Path) -> str | None:
    # Fast checks for indicators up to MAX_DEPTH_DIR_FIND
    for depth in range(MAX_DEPTH_DIR_FIND + 1):
        try:
            for root, dirs, files in os.walk(path):
                # limit depth relative to base path
                rel = Path(root).relative_to(path)
                if len(rel.parts) > MAX_DEPTH_DIR_FIND:
                    # prune deeper
                    dirs[:] = []
                    continue
                # skip noisy dirs
                dirs[:] = [d for d in dirs if not d.startswith('.') and not is_excluded_dir(d)]
                names = set(files) | set(dirs)
                # indicators
                if any(ind in names for ind in INDICATORS):
                    # decide category
                    if 'package.json' in names or any(f.endswith(('.js', '.ts')) for f in files):
                        return '🌟 JavaScript_Projects'
                    if 'requirements.txt' in names or any(f.endswith('.py') for f in files):
                        return '🐍 Python_Projects'
                    if 'Cargo.toml' in names:
                        return '🦀 Rust_Projects'
                    if 'pom.xml' in names or any(f.endswith(('.java', '.kt')) for f in files):
                        return '☕ Java_Projects'
                    if 'Gemfile' in names or any(f.endswith('.rb') for f in files):
                        return '💎 Ruby_Projects'
                    if 'go.mod' in names or any(f.endswith('.go') for f in files):
                        return '🐹 Go_Projects'
                    if any(f.endswith(('.html', '.css')) for f in files):
                        return '🌐 Web_Projects'
                    # name heuristics
                    name = path.name.lower()
                    if any(k in name for k in ['ai', 'ml', 'neural']):
                        return '🤖 AI_ML_Projects'
                    if any(k in name for k in ['docker', 'k8s', 'kubernetes', 'devops', 'ci', 'cd']):
                        return '🐳 DevOps_Projects'
                    if any(k in name for k in ['data', 'analysis', 'analytics']):
                        return '📊 Data_Projects'
                    if any(k in name for k in ['game', 'unity', 'unreal']):
                        return '🎮 Game_Projects'
                    if any(k in name for k in ['mobile', 'android', 'ios', 'flutter', 'react-native']):
                        return '📱 Mobile_Projects'
                    if any(k in name for k in ['noizygenie', 'noizy', 'genie', 'bionic', 'omnipotent']):
                        return '🧞‍♂️ NoizyGenie_Creations'
                    return '🔧 Tools_And_Utilities'
        except Exception:
            break
    return None


def ensure_categories():
    AQUARIUM.mkdir(exist_ok=True)
    for cat in CATEGORIES:
        (AQUARIUM / cat).mkdir(exist_ok=True)


def unique_target(path: Path) -> Path:
    if not path.exists():
        return path
    base = path.name
    parent = path.parent
    stem = base
    suffix = ''
    if '.' in base and path.is_file():
        stem, suffix = base.rsplit('.', 1)
        suffix = '.' + suffix
    i = 2
    while True:
        candidate = parent / f"{stem}-{i}{suffix}"
        if not candidate.exists():
            return candidate
        i += 1


def move_project_folder(src: Path, category: str) -> Tuple[bool, Path | None, str | None]:
    target = unique_target(AQUARIUM / category / src.name)
    try:
        shutil.move(str(src), str(target))
        return True, target, None
    except Exception as e:
        return False, None, str(e)


def bucket_loose_file(file_path: Path):
    # Determine category by extension; default Tools
    ext = file_path.suffix.lower().lstrip('.')
    category = CATEGORY_MAP.get(ext, '🔧 Tools_And_Utilities')
    # Create extension subfolder
    ext_folder = AQUARIUM / category / f"by_extension/{ext or 'noext'}"
    ext_folder.mkdir(parents=True, exist_ok=True)
    target = unique_target(ext_folder / file_path.name)
    try:
        shutil.move(str(file_path), str(target))
        return True, target, None
    except Exception as e:
        return False, None, str(e)


def is_within_excluded(p: Path) -> bool:
    for ex in RUNTIME_EXCLUDES:
        try:
            p.relative_to(ex)
            return True
        except Exception:
            continue
    return False


def organize():
    ensure_categories()

    summary = {
        'moved_projects': 0,
        'moved_files': 0,
        'errors': 0,
        'by_category': {},
        'by_extension': {},
        'skipped': 0,
        'empties_removed': 0,
        'details': []
    }

    # Discover top-level directories and files in roots
    for root in ROOTS:
        if not root.exists():
            continue
        try:
            for entry in os.scandir(root):
                p = Path(entry.path)
                name = p.name
                if name.startswith('.') or is_excluded_dir(name):
                    continue
                if is_within_excluded(p) or str(p).startswith(str(AQUARIUM)):
                    continue
                if entry.is_dir(follow_symlinks=False):
                    cat = detect_project_category(p)
                    if cat:
                        ok, target, err = move_project_folder(p, cat)
                        if ok:
                            summary['moved_projects'] += 1
                            summary['by_category'][cat] = summary['by_category'].get(cat, 0) + 1
                            summary['details'].append({'type': 'project', 'src': str(p), 'dst': str(target), 'category': cat})
                        else:
                            summary['errors'] += 1
                            summary['details'].append({'type': 'project', 'src': str(p), 'error': err})
                    else:
                        # Not project-like: descend one level to bucket loose files without tearing structure too deeply
                        try:
                            for sub in os.scandir(p):
                                sp = Path(sub.path)
                                if sub.is_file(follow_symlinks=False):
                                    ok, target, err = bucket_loose_file(sp)
                                    if ok:
                                        summary['moved_files'] += 1
                                        ext = sp.suffix.lower().lstrip('.') or 'noext'
                                        summary['by_extension'][ext] = summary['by_extension'].get(ext, 0) + 1
                                        summary['details'].append({'type': 'file', 'src': str(sp), 'dst': str(target), 'ext': ext})
                                    else:
                                        summary['errors'] += 1
                                        summary['details'].append({'type': 'file', 'src': str(sp), 'error': err})
                        except Exception:
                            summary['skipped'] += 1
                            continue
                elif entry.is_file(follow_symlinks=False):
                    ok, target, err = bucket_loose_file(p)
                    if ok:
                        summary['moved_files'] += 1
                        ext = p.suffix.lower().lstrip('.') or 'noext'
                        summary['by_extension'][ext] = summary['by_extension'].get(ext, 0) + 1
                        summary['details'].append({'type': 'file', 'src': str(p), 'dst': str(target), 'ext': ext})
                    else:
                        summary['errors'] += 1
                        summary['details'].append({'type': 'file', 'src': str(p), 'error': err})
        except PermissionError:
            continue

    # Write index
    write_index(summary)
    return summary


def write_index(summary: Dict):
    lines = []
    lines.append(f"# 🐠 NoizyFish Aquarium Index")
    lines.append("")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"Aquarium: {AQUARIUM}")
    lines.append("")
    lines.append(f"- Moved projects: {summary['moved_projects']}")
    lines.append(f"- Moved loose files: {summary['moved_files']}")
    lines.append(f"- Errors: {summary['errors']}")
    lines.append(f"- Skipped: {summary['skipped']}")
    lines.append(f"- Empty folders removed: {summary.get('empties_removed', 0)}")
    lines.append("")
    lines.append("## By Category")
    if summary['by_category']:
        for cat, n in sorted(summary['by_category'].items(), key=lambda x: (-x[1], x[0])):
            lines.append(f"- {cat}: {n}")
    else:
        lines.append("- None")
    lines.append("")
    lines.append("## Aquarium Structure (top level)")
    for cat in CATEGORIES:
        cat_path = AQUARIUM / cat
        try:
            items = [d for d in os.listdir(cat_path) if not d.startswith('.')]
        except Exception:
            items = []
        lines.append(f"- {cat} ({len(items)} items)")
    lines.append("")
    AQUARIUM_INDEX.write_text('\n'.join(lines))


def main():
    # Exclude current working scripts dir to avoid moving while running
    try:
        RUNTIME_EXCLUDES.append(Path(__file__).resolve().parent)
    except Exception:
        pass
    AQUARIUM.mkdir(exist_ok=True)
    summary = organize()

    # After moving, prune empty directories in roots (excluding roots themselves, Aquarium, and excluded dirs)
    def prune_empty_under(root: Path) -> int:
        removed = 0
        if not root.exists():
            return 0
        for dirpath, dirnames, filenames in os.walk(root, topdown=False):
            p = Path(dirpath)
            if p == root:
                continue
            if is_within_excluded(p):
                continue
            if str(p).startswith(str(AQUARIUM)):
                continue
            if is_excluded_dir(p.name) or p.name.startswith('.'):
                continue
            try:
                if not any(p.iterdir()):
                    p.rmdir()
                    removed += 1
            except Exception:
                continue
        return removed

    empties_total = 0
    for rt in ROOTS:
        empties_total += prune_empty_under(rt)
    summary['empties_removed'] = empties_total
    try:
        write_index(summary)
    except Exception:
        pass

    print(json.dumps({
        'aquarium': str(AQUARIUM),
        'moved_projects': summary['moved_projects'],
        'moved_files': summary['moved_files'],
        'errors': summary['errors'],
        'empties_removed': summary.get('empties_removed', 0)
    }, indent=2))

if __name__ == '__main__':
    main()
