#!/usr/bin/env python3
"""
bubba_desktop_sweep.py

Bubba scans the Desktop, sorts files into Noizy_Workspace project folders
based on extension. If the folder doesn’t exist yet, Bubba creates it.
Logs results for review.
"""

import shutil
from pathlib import Path

# --- Config ---
WORKSPACE = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace"
DESKTOP = Path.home() / "Desktop"
LOGS = WORKSPACE / "Saved_Notes"
LOGS.mkdir(parents=True, exist_ok=True)

CATEGORIES = {
    "Audio_Project": [".wav", ".aiff", ".aif", ".mp3", ".flac", ".ogg", ".m4a"],
    "Code_Project":  [".py", ".sh", ".js", ".ts", ".cpp", ".c", ".h", ".rb", ".php", ".java"],
    "Docs_Project":  [".txt", ".md", ".rtf", ".doc", ".docx", ".pdf", ".xlsx", ".csv", ".pptx"],
    "Images_Project":[ ".png", ".jpg", ".jpeg", ".gif", ".svg", ".bmp", ".tiff", ".tif", ".webp"]
}

def unique_dest(dest: Path) -> Path:
    """Never overwrite: append (1), (2)..."""
    if not dest.exists():
        return dest
    stem, suf = dest.stem, dest.suffix
    parent = dest.parent
    i = 1
    while True:
        alt = parent / f"{stem} ({i}){suf}"
        if not alt.exists():
            return alt
        i += 1

def sort_file(file: Path) -> str:
    ext = file.suffix.lower()
    for proj, exts in CATEGORIES.items():
        if ext in exts:
            dest_dir = WORKSPACE / proj
            dest_dir.mkdir(parents=True, exist_ok=True)  # auto-create if missing
            dest = unique_dest(dest_dir / file.name)
            try:
                shutil.move(str(file), str(dest))
                return f"Moved: {file.name} -> {dest_dir.name}"
            except (shutil.Error, OSError) as err:
                return f"Error moving {file.name}: {err}"
    return f"Skipped: {file.name} (no matching category)"

def main():
    if not DESKTOP.exists():
        print("❌ No Desktop folder found.")
        return

    log_lines = []
    moved, skipped = 0, 0

    for item in DESKTOP.iterdir():
        if item.is_file():
            result = sort_file(item)
            log_lines.append(result)
            if result.startswith("Moved"):
                moved += 1
            elif result.startswith("Error"):
                skipped += 1
            else:
                skipped += 1

    summary = (
        f"Desktop Sweep complete.\n"
        f"Files moved: {moved}\n"
        f"Files skipped: {skipped}\n"
        f"Workspace: {WORKSPACE}\n"
    )
    print(summary)
    (LOGS / f"desktop_sweep_{Path.home().name}.txt").write_text("\n".join(log_lines) + "\n\n" + summary)

    print("✅ Bubba is ready for a restart. Reboot when you’re set.")

if __name__ == "__main__":
    main()