import os
from pathlib import Path
import shutil
import subprocess
import sys

NCW_FOLDER = Path.home() / "Desktop" / "KTK_Rebuilds" / "DEEP_ORGANIZED" / "NCW"

def move_to_trash(file_path):
    try:
        # Use macOS 'osascript' to move to Trash
        subprocess.run([
            "osascript", "-e",
            f'tell app "Finder" to move POSIX file "{file_path}" to trash'
        ], check=True)
        print(f"Trashed: {file_path}")
        return True
    except Exception as e:
        print(f"Failed to trash {file_path}: {e}")
        return False

def trash_duplicates_ncw(folder):
    trashed = 0
    for fname in os.listdir(folder):
        if "copy" in fname.lower():
            src = folder / fname
            if move_to_trash(str(src)):
                trashed += 1
    print(f"\n✅ Done! {trashed} duplicate files moved to Trash from NCW.")

if __name__ == "__main__":
    trash_duplicates_ncw(NCW_FOLDER)