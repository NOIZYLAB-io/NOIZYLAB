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

# Scan all files in Projects (recursively)
def move_utilities():
    for dirpath, _, filenames in os.walk(PROJECTS_DIR):
        for fname in filenames:
            fpath = Path(dirpath) / fname
            # Skip if already in utilities
            if UTILITIES_DIR in fpath.parents:
                continue
            if is_utility(fpath):
                target = UTILITIES_DIR / fpath.name
                if fpath != target:
                    if target.exists():
                        target = UTILITIES_DIR / f"{fpath.stem}_copy{fpath.suffix}"
                    shutil.move(str(fpath), str(target))
                    print(f"Moved {fpath} -> {target}")
    print("All utility files moved to utilities folder.")

if __name__ == "__main__":
    move_utilities()
