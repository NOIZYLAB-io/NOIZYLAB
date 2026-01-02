#!/usr/bin/env python3
import os
import shutil
import re
from pathlib import Path
from datetime import datetime

ROOT = Path.home() / "Desktop" / "NoizyFish"
PROJECTS_DIR = ROOT / "Projects"
UTILITIES_DIR = PROJECTS_DIR / "utilities"
UTILITIES_DIR.mkdir(parents=True, exist_ok=True)

UTILITY_EXTS = {'.py', '.sh', '.bat', '.pl', '.rb', '.js', '.ts', '.yaml', '.yml', '.json'}
UTILITY_KEYWORDS = {'util', 'utility', 'setup', 'organize', 'scan', 'sort', 'manage', 'tool', 'script'}

# Auto-save the script source before running
SCRIPT_PATH = PROJECTS_DIR / 'utilities' / 'noizyfish_full_organizer.py'
def auto_save_self():
    import inspect, sys
    src = inspect.getsource(sys.modules[__name__])
    with open(SCRIPT_PATH, 'w', encoding='utf-8') as f:
        f.write(src)
    print(f"Script auto-saved to {SCRIPT_PATH}")

def infer_project(file_path):
    rel = file_path.relative_to(ROOT)
    parts = rel.parts
    if len(parts) > 1 and parts[0] == "Projects":
        return parts[1]
    return file_path.stem.split('_')[0].capitalize()

def get_unique_target(target):
    base = target.stem
    ext = target.suffix
    i = 1
    new_target = target
    while new_target.exists():
        new_target = target.parent / f"{base}_copy{i}{ext}"
        i += 1
    return new_target

def is_utility(file_path):
    ext = file_path.suffix.lower()
    name = file_path.stem.lower()
    if ext in UTILITY_EXTS:
        return True
    for kw in UTILITY_KEYWORDS:
        if kw in name:
            return True
    return False

def move_file(file_path):
    project = infer_project(file_path)
    ext = file_path.suffix.lower()[1:] if file_path.suffix else "NOEXT"
    target_dir = PROJECTS_DIR / project / f"{ext.upper()}_Master"
    target_dir.mkdir(parents=True, exist_ok=True)
    target_path = target_dir / file_path.name
    if file_path != target_path:
        if target_path.exists():
            target_path = get_unique_target(target_path)
        shutil.move(str(file_path), str(target_path))
        print(f"Moved {file_path} -> {target_path}")

def organize_all():
    for dirpath, _, filenames in os.walk(ROOT):
        for fname in filenames:
            fpath = Path(dirpath) / fname
            if PROJECTS_DIR in fpath.parents or UTILITIES_DIR in fpath.parents:
                continue
            move_file(fpath)
    print("Step 1: All files organized by project and extension.")

def move_utilities():
    moved_files = []
    for dirpath, _, filenames in os.walk(PROJECTS_DIR):
        for fname in filenames:
            fpath = Path(dirpath) / fname
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
    print(f"Step 2: Moved {len(moved_files)} utility files to utilities folder.")
    errors = []
    for _, target in moved_files:
        if not target.exists():
            errors.append(str(target))
    if errors:
        print("The following moved files could not be found:")
        for e in errors:
            print(f"  {e}")
    else:
        print("All moved utility file paths are accurate and exist.")

def audit_reconnection():
    print(f"\nStep 3: Auditing NoizyFish structure in: {PROJECTS_DIR}")
    for project in sorted(PROJECTS_DIR.iterdir()):
        if project.is_dir() and not project.name.startswith("_"):
            print(f"\n🗂️ Project: {project.name}")
            for ext_folder in sorted(project.iterdir()):
                if ext_folder.is_dir():
                    files = list(ext_folder.glob("*"))
                    print(f"  📁 {ext_folder.name} ({len(files)} files)")
                    for f in files:
                        print(f"    - {f.name}")

if __name__ == "__main__":
    auto_save_self()
    organize_all()
    move_utilities()
    audit_reconnection()
    print("\n✅ NoizyFish full organization and audit complete.")
