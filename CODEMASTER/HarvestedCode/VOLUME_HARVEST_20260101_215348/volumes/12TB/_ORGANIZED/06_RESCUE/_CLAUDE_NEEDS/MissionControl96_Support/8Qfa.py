import os
from pathlib import Path
import subprocess

KTK_REBUILDS = Path.home() / "Desktop" / "KTK_Rebuilds"

def move_to_trash(path):
    try:
        subprocess.run([
            "osascript", "-e",
            f'tell app "Finder" to move POSIX file \"{path}\" to trash'
        ], check=True)
        print(f"Trashed: {path}")
        return True
    except Exception as e:
        print(f"Failed to trash {path}: {e}")
        return False

def trash_copy_files(root):
    trashed = 0
    for dirpath, dirnames, filenames in os.walk(root):
        for fname in filenames:
            if "copy" in fname.lower():
                file_path = Path(dirpath) / fname
                if move_to_trash(str(file_path)):
                    trashed += 1
    print(f"\n✅ Done! {trashed} files with 'copy' in the name moved to Trash.")

if __name__ == "__main__":
    trash_copy_files(KTK_REBUILDS)