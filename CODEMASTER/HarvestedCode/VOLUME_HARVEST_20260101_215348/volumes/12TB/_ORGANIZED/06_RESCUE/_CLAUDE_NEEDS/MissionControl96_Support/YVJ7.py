import os
import shutil
from pathlib import Path
# from collections import defaultdict

ROOT = Path.home() / "Desktop" / "KONTAKT_LAB"
DEST = Path.home() / "Desktop" / "KTK_Rebuilds"
EXTENSIONS = [".ncw", ".nki", ".nkm", ".nkc", ".wav", ".aiff", ".sf2", ".sfz", ".rex", ".rx2", ".mp3", ".flac"]

def move_and_group_files(root, dest, extensions):
    moved = 0
    for dirpath, _, filenames in os.walk(root):
        rel_dir = os.path.relpath(dirpath, root)
        if rel_dir == "." or rel_dir.startswith("PROJECT_ORGANIZER"):
            continue  # Skip root and organizer folder
        for fname in filenames:
            ext = Path(fname).suffix.lower()
            if ext in extensions:
                # Group by immediate folder (library) and extension
                parts = Path(rel_dir).parts
                if parts:
                    lib_folder = parts[0]
                else:
                    lib_folder = "ROOT"
                ext_folder = ext.lstrip(".").upper()
                src_path = Path(dirpath) / fname
                dest_folder = dest / lib_folder / ext_folder
                dest_folder.mkdir(parents=True, exist_ok=True)
                dest_path = dest_folder / fname
                # Avoid overwrite
                if dest_path.exists():
                    base, extn = os.path.splitext(fname)
                    dest_path = dest_folder / f"{base}_copy{extn}"
                shutil.copy2(src_path, dest_path)
                print(f"Moved: {src_path} -> {dest_path}")
                moved += 1
    print(f"\n✅ Done! {moved} files copied to {dest}")

if __name__ == "__main__":
    DEST.mkdir(exist_ok=True)
    move_and_group_files(ROOT, DEST, EXTENSIONS)
