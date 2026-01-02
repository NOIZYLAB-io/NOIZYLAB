import os
from pathlib import Path
import shutil

KTK_REBUILDS = Path.home() / "Desktop" / "KTK_Rebuilds"

def move_duplicates_force(root):
    moved = 0
    for dirpath, dirnames, filenames in os.walk(root):
        for fname in filenames:
            if "copy" in fname.lower():
                src = Path(dirpath) / fname
                duplicates_folder = Path(dirpath) / "Duplicates"
                duplicates_folder.mkdir(exist_ok=True)
                dest = duplicates_folder / fname
                # If destination exists, forcibly overwrite
                try:
                    if dest.exists():
                        dest.unlink()  # Remove existing file
                    shutil.move(str(src), str(dest))
                    print(f"Moved: {src} -> {dest}")
                    moved += 1
                except Exception as e:
                    print(f"Failed to move {src}: {e}")
    print(f"\n✅ Done! {moved} duplicate files force-moved into 'Duplicates' folders.")

if __name__ == "__main__":
    move_duplicates_force(KTK_REBUILDS)