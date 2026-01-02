#!/usr/bin/env python3
"""
Tab Guard — watches your VS Code workspace and automatically
saves & backs up all modified files every 60 seconds.
"""
import time, shutil
from pathlib import Path

WORKSPACE = Path("/Users/rsp_ms/NoizyFish_Aquarium/Desktop/KONTAKT_LAB/PROJECT_ORGANIZER")
BACKUP_DIR = WORKSPACE / "_backups"
BACKUP_DIR.mkdir(exist_ok=True)

def snapshot():
    for f in WORKSPACE.glob("**/*"):
        if f.suffix in {".py",".md",".txt",".json",".sh"} and f.is_file():
            dest = BACKUP_DIR / f"{f.stem}_{int(time.time())}{f.suffix}"
            try:
                shutil.copy2(f, dest)
            except Exception as e:
                print("skip", f, e)

if __name__ == "__main__":
    print("🛡 Tab Guard running — press Ctrl-C to stop")
    while True:
        snapshot()
        time.sleep(60)
