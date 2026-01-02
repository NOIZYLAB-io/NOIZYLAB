import os
import shutil
from pathlib import Path

# Source and destination
SRC = Path("/Volumes/4TB Blue Fish/Native Instruments")
DEST = Path("/Volumes/6TB/NI_2026")

# All relevant NI extensions
NI_EXTS = [
    ".nki", ".nkm", ".nkc", ".nkr", ".nkx", ".ncw", ".nks", ".nka", ".nkb", ".nkt", ".nksf", ".nksr",
    ".wav", ".aiff", ".flac", ".mp3", ".ogg", ".rex", ".rx2", ".sf2", ".sfz",
    ".ens", ".ism", ".kit"
]

def is_library_integrity_good(lib_path):
    # Check for at least one of each critical NI file type
    found = {ext: False for ext in [".nki", ".nkm", ".ncw"]}
    for dirpath, _, filenames in os.walk(lib_path):
        for fname in filenames:
            ext = Path(fname).suffix.lower()
            if ext in found:
                found[ext] = True
        if all(found.values()):
            return True
    return False

def check_and_move_libraries(src, dest):
    moved = 0
    for item in src.iterdir():
        if item.is_dir():
            print(f"Checking: {item.name}")
            if is_library_integrity_good(item):
                dest_folder = dest / item.name
                if dest_folder.exists():
                    print(f"❗ Destination already exists: {dest_folder}, skipping.")
                    continue
                print(f"✅ Integrity good, moving: {item.name}")
                shutil.move(str(item), str(dest_folder))
                moved += 1
            else:
                print(f"❌ Integrity check failed: {item.name}")
    print(f"\n🏁 Done! {moved} libraries moved to {dest}")

if __name__ == "__main__":
    DEST.mkdir(parents=True, exist_ok=True)
    check_and_move_libraries(SRC, DEST)