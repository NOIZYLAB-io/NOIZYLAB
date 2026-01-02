#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

PROJECTS_DIR = Path.home() / "Desktop" / "NoizyFish" / "Projects"
UTILITIES_DIR = PROJECTS_DIR / "utilities"
UTILITIES_DIR.mkdir(parents=True, exist_ok=True)

# List of utility file extensions and keywords
UTILITY_EXTS = {'.py', '.sh', '.bat', '.pl', '.rb', '.js', '.ts', '.yaml', '.yml', '.json'}
UTILITY_KEYWORDS = {'util', 'utility', 'setup', 'organize', 'scan', 'sort', 'manage', 'tool', 'script'}

def is_utility(file_path):
    ext = file_path.suffix.lower()
    name = file_path.stem.lower()
    if ext in UTILITY_EXTS:
        return True
    for kw in UTILITY_KEYWORDS:
        if kw in name:
            return True
    return False

def get_unique_target(target):
    """Return a unique target path if file exists."""
    base = target.stem
    ext = target.suffix
    i = 1
    new_target = target
    while new_target.exists():
        new_target = target.parent / f"{base}_copy{i}{ext}"
        i += 1
    return new_target

# Scan all files in Projects (recursively)
def move_utilities():
    moved_files = []
    for dirpath, _, filenames in os.walk(PROJECTS_DIR):
        for fname in filenames:
            fpath = Path(dirpath) / fname
            # Skip if already in utilities, is a symlink, or not a file
            if UTILITIES_DIR in fpath.parents or not fpath.is_file() or fpath.is_symlink():
                continue
            if is_utility(fpath):
                target = UTILITIES_DIR / fpath.name
                if fpath != target:
                    target = get_unique_target(target)
                    try:
                        shutil.move(str(fpath), str(target))
                        print(f"Moved {fpath} -> {target}")
                        moved_files.append((fpath, target))
                    except Exception as e:
                        print(f"Failed to move {fpath}: {e}")
    print(f"Moved {len(moved_files)} utility files to utilities folder.")

if __name__ == "__main__":
    move_utilities()
    os.system('python3 auto_move_utilities.py')
