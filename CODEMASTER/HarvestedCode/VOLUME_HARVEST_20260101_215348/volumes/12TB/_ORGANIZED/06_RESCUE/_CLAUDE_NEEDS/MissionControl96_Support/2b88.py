#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

ROOT = Path.home() / "Desktop" / "NoizyFish"
PYTHON_SCRIPTS_DIR = ROOT / "Projects" / "python_scripts"
UTILITIES_DIR = PYTHON_SCRIPTS_DIR / "utilities"
UTILITIES_DIR.mkdir(parents=True, exist_ok=True)

UTILITY_EXTS = {'.py', '.sh', '.bat', '.pl', '.rb', '.js', '.ts', '.yaml', '.yml', '.json'}
UTILITY_KEYWORDS = {'util', 'utility', 'setup', 'organize', 'scan', 'sort', 'manage', 'tool', 'script'}
WORKFLOW_KEYWORDS = {'workflow', 'process', 'pipeline', 'batch', 'auto', 'audit', 'clean', 'move', 'group', 'catalog', 'report', 'structure'}

def is_utility(file_path):
    ext = file_path.suffix.lower()
    name = file_path.stem.lower()
    if ext in UTILITY_EXTS:
        return True
    for kw in UTILITY_KEYWORDS | WORKFLOW_KEYWORDS:
        if kw in name:
            return True
    return False

def get_unique_target(target):
    base = target.stem
    ext = target.suffix
    i = 1
    new_target = target
    while new_target.exists():
        new_target = target.parent / f"{base}_copy{i}{ext}"
        i += 1
    return new_target

def organize_files():
    for dirpath, _, filenames in os.walk(ROOT):
        for fname in filenames:
            fpath = Path(dirpath) / fname
            # Skip if already in utilities or not a file
            if UTILITIES_DIR in fpath.parents or not fpath.is_file() or fpath.is_symlink():
                continue
            if is_utility(fpath):
                target = UTILITIES_DIR / fpath.name
                if fpath != target:
                    target = get_unique_target(target)
                    shutil.move(str(fpath), str(target))
                    print(f"Moved {fpath} -> {target}")
            else:
                # If not utility, organize by project
                project_name = fpath.stem.split('_')[0].capitalize()
                project_dir = PYTHON_SCRIPTS_DIR / project_name
                project_dir.mkdir(parents=True, exist_ok=True)
                target = project_dir / fpath.name
                if fpath != target:
                    if target.exists():
                        target = project_dir / f"{fpath.stem}_copy{fpath.suffix}"
                    shutil.move(str(fpath), str(target))
                    print(f"Moved {fpath} -> {target}")
    print("Organization complete: utilities and projects in python_scripts.")

if __name__ == "__main__":
    organize_files()
