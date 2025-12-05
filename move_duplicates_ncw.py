import os
from pathlib import Path
import shutil

NCW_FOLDER = Path.home() / "Desktop" / "KTK_Rebuilds" / "DEEP_ORGANIZED" / "NCW"

def move_duplicates_ncw(folder):
    moved = 0
    for fname in os.listdir(folder):
        if "copy" in fname.lower():
            src = folder / fname
            duplicates_folder = folder / "Duplicates"
            duplicates_folder.mkdir(exist_ok=True)
            dest = duplicates_folder / fname
            try:
                if dest.exists():
                    dest.unlink()  # Remove existing file
                shutil.move(str(src), str(dest))
                print(f"Moved: {src} -> {dest}")
                moved += 1
            except Exception as e:
                print(f"Failed to move {src}: {e}")
    print(f"\n✅ Done! {moved} duplicate files force-moved into 'Duplicates' in NCW.")

if __name__ == "__main__":
    move_duplicates_ncw(NCW_FOLDER)
python3 /Users/rsp_ms/Desktop/KONTAKT_LAB/PROJECT_ORGANIZER/move_duplicates_ncw.py