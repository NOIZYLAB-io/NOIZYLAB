#!/usr/bin/env python3
"""
Bubba Desktop Scanner
Scans your Desktop, sorts files by type, and moves them into the right
project folders in Noizy Workspace. Keeps logs so you always know what moved.
"""

import shutil
from pathlib import Path
from datetime import datetime

# Paths
HOME = Path.home()
DESKTOP = HOME / "Desktop"
WORKSPACE = HOME / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace"
BUBBA_BITZ = WORKSPACE / "Bubba's Bitz"
LOGS = BUBBA_BITZ / "Logs"

# Ensure dirs exist
for p in (WORKSPACE, BUBBA_BITZ, LOGS):
    p.mkdir(parents=True, exist_ok=True)

# Categories
CATEGORIES = {
    ".py": BUBBA_BITZ,
    ".txt": LOGS,
    ".md": LOGS,
    ".rtf": LOGS,
    ".wav": WORKSPACE / "Audio_Project",
    ".aiff": WORKSPACE / "Audio_Project",
    ".mp3": WORKSPACE / "Audio_Project",
    ".flac": WORKSPACE / "Audio_Project",
    ".png": WORKSPACE / "Images_Project",
    ".jpg": WORKSPACE / "Images_Project",
    ".jpeg": WORKSPACE / "Images_Project",
    ".svg": WORKSPACE / "Images_Project",
}

def safe_move(src: Path, dest_dir: Path):
    """Move file safely, avoid overwrites by renaming."""
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / src.name
    i = 1
    while dest.exists():
        dest = dest_dir / f"{src.stem} ({i}){src.suffix}"
        i += 1
    shutil.move(str(src), str(dest))
    return dest

def scan_and_sort():
    report = [f"=== Bubba Desktop Scan {datetime.now()} ==="]
    for item in DESKTOP.iterdir():
        if item.is_file():
            ext = item.suffix.lower()
            if ext in CATEGORIES:
                dest = safe_move(item, CATEGORIES[ext])
                report.append(f"MOVED {item.name} → {dest}")
            else:
                report.append(f"ORPHAN (left in place): {item.name}")
    return "\n".join(report)

if __name__ == "__main__":
    log_text = scan_and_sort()
    log_file = LOGS / f"desktop_scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    log_file.write_text(log_text, encoding="utf-8")
    print(f"✅ Desktop scan complete. Log saved to {log_file}")
