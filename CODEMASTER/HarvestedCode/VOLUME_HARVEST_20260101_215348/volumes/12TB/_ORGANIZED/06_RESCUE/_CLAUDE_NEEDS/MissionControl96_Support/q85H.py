import os
from pathlib import Path
import shutil

KTK_REBUILDS = Path.home() / "Desktop" / "KTK_Rebuilds"

def move_duplicates(root):
    moved = 0
    for dirpath, dirnames, filenames in os.walk(root):
        for fname in filenames:
            if "copy" in fname.lower():
                src = Path(dirpath) / fname
                # Create "Duplicates" folder in the same parent directory
                duplicates_folder = Path(dirpath) / "Duplicates"
                duplicates_folder.mkdir(exist_ok=True)
                dest = duplicates_folder / fname
                # Avoid overwrite
                if dest.exists():
                    base, ext = os.path.splitext(fname)
                    dest = duplicates_folder / f"{base}_dupe{ext}"
                shutil.move(str(src), str(dest))
                print(f"Moved: {src} -> {dest}")
                moved += 1
    print(f"\n✅ Done! {moved} duplicate files moved into 'Duplicates' folders.")

if __name__ == "__main__":
    move_duplicates(KTK_REBUILDS)