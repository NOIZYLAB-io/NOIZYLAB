#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

ROOT = Path.home() / "Desktop" / "NoizyFish"
PROJECTS_DIR = ROOT / "Projects"

# Helper: Infer project name from filename or parent folder
def infer_project(file_path):
    # Use parent folder if inside Projects, else use stem
    rel = file_path.relative_to(ROOT)
    parts = rel.parts
    if len(parts) > 1 and parts[0] == "Projects":
        return parts[1]
    return file_path.stem.split('_')[0].capitalize()

# Move file to Projects/<Project>/<EXTENSION>_Master/
def move_file(file_path):
    project = infer_project(file_path)
    ext = file_path.suffix.lower()[1:] if file_path.suffix else "NOEXT"
    target_dir = PROJECTS_DIR / project / f"{ext.upper()}_Master"
    target_dir.mkdir(parents=True, exist_ok=True)
    target_path = target_dir / file_path.name
    if file_path != target_path:
        if target_path.exists():
            target_path = target_dir / f"{file_path.stem}_copy{file_path.suffix}"
        shutil.move(str(file_path), str(target_path))
        print(f"Moved {file_path} -> {target_path}")

# Scan all files in NoizyFish (recursively)
def organize_all():
    for dirpath, _, filenames in os.walk(ROOT):
        for fname in filenames:
            fpath = Path(dirpath) / fname
            # Skip files already in correct place
            if PROJECTS_DIR in fpath.parents:
                continue
            move_file(fpath)
    print("Automation complete. All files organized by project and extension.")

if __name__ == "__main__":
    organize_all()
