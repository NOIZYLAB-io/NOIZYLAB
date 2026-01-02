#!/usr/bin/env python3
"""
bubba_desktop_sorter.py
Moves files from Desktop into matching project folders inside Noizy_Workspace,
based on extension. If no folder exists, file is left in place.
"""

import os
import shutil
from pathlib import Path

# --- Config ---
WORKSPACE = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace"
DESKTOP = Path.home() / "Desktop"

CATEGORIES = {
    "Audio_Project": [".wav", ".aiff", ".aif", ".mp3", ".flac", ".ogg", ".m4a"],
    "Code_Project":  [".py", ".sh", ".js", ".ts", ".cpp", ".c", ".h", ".rb", ".php", ".java"],
    "Docs_Project":  [".txt", ".md", ".rtf", ".doc", ".docx", ".pdf", ".xlsx", ".csv", ".pptx"],
    "Images_Project":[ ".png", ".jpg", ".jpeg", ".gif", ".svg", ".bmp", ".tiff", ".tif", ".webp"]
}

def sort_file(file: Path):
    ext = file.suffix.lower()
    for proj, exts in CATEGORIES.items():
        if ext in exts:
            dest_dir = WORKSPACE / proj
            if dest_dir.exists():  # Only move if project folder is already there
                dest = dest_dir / file.name
                if dest.exists():
                    base, suf = dest.stem, dest.suffix
                    i = 1
                    while True:
                        alt = dest_dir / f"{base} ({i}){suf}"
                        if not alt.exists():
                            dest = alt
                            break
                        i += 1
                shutil.move(str(file), str(dest))
                print(f"Moved: {file.name} -> {dest_dir.name}")
                return True
    return False  # No match / no folder

def main():
    if not DESKTOP.exists():
        print("No Desktop folder found.")
        return

    moved, skipped = 0, 0
    for item in DESKTOP.iterdir():
        if item.is_file():
            try:
                if sort_file(item):
                    moved += 1
                else:
                    skipped += 1
            except (shutil.Error, OSError) as err:
                print(f"Error moving {item.name}: {err}")
                skipped += 1

    print(f"\n✅ Bubba Desktop Sorter complete. {moved} moved, {skipped} left in place.")

if __name__ == "__main__":
    main()