#!/usr/bin/env python3
import os
import shutil

SOURCE_DIR = "/Volumes/4TBSG/_SHITE_TO_SORT/_COPIES TO SORT"
LOG_FILE = os.path.join(SOURCE_DIR, "organize_log.txt")

EXT_GROUPS = {
    ".nki": "NKI",
    ".wav": "WAV",
    ".aif": "AIF",
    ".aiff": "AIF"
}

def organize_by_extension(source_dir=SOURCE_DIR, log_file=LOG_FILE):
    moved = []
    for fname in os.listdir(source_dir):
        fpath = os.path.join(source_dir, fname)
        if not os.path.isfile(fpath):
            continue
        ext = os.path.splitext(fname)[1].lower()
        group = EXT_GROUPS.get(ext)
        if group:
            dest_dir = os.path.join(source_dir, group)
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            dest_path = os.path.join(dest_dir, fname)
            try:
                shutil.move(fpath, dest_path)
                moved.append(f"Moved: {fpath} -> {dest_path}")
                print(f"Moved: {fpath} -> {dest_path}")
            except Exception as e:
                print(f"Failed to move {fpath}: {e}")
    if moved:
        with open(log_file, "w") as log:
            log.write("\n".join(moved))
        print(f"\nMove log saved to {log_file}")
    else:
        print("\nNo files moved.")

if __name__ == "__main__":
    organize_by_extension()
