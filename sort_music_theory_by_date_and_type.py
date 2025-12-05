#!/usr/bin/env python3
import os
import shutil
import time
from datetime import datetime

ROOT_DIR = "/Volumes/4TBSG/_SHITE_TO_SORT/ 2025 MUSIC THEORY"
SORTED_DIR = os.path.join(ROOT_DIR, "SORTED_BY_DATE")
LOG_FILE = os.path.join(ROOT_DIR, "sort_log.txt")

# Supported file types for grouping
VIDEO_EXTS = {".mp4", ".mov", ".avi", ".mkv"}
BOOK_EXTS = {".pdf", ".epub", ".mobi", ".djvu"}
AUDIO_EXTS = {".mp3", ".wav", ".flac", ".aac"}
SHEET_EXTS = {".xml", ".mid", ".midi"}


def get_group(ext):
    ext = ext.lower()
    if ext in VIDEO_EXTS:
        return "Videos"
    elif ext in BOOK_EXTS:
        return "Books"
    elif ext in AUDIO_EXTS:
        return "Audio"
    elif ext in SHEET_EXTS:
        return "SheetMusic"
    else:
        return "Other"


def sort_by_date_and_type(root_dir=ROOT_DIR, sorted_dir=SORTED_DIR, log_file=LOG_FILE):
    moved = []
    if not os.path.exists(sorted_dir):
        os.makedirs(sorted_dir)
    for folder, dirs, files in os.walk(root_dir):
        # Skip the sorted output folder itself
        if sorted_dir in folder:
            continue
        for fname in files:
            fpath = os.path.join(folder, fname)
            ext = os.path.splitext(fname)[1]
            group = get_group(ext)
            try:
                # Get creation time (fallback to modification time)
                try:
                    ctime = os.path.getctime(fpath)
                except Exception:
                    ctime = os.path.getmtime(fpath)
                date_str = datetime.fromtimestamp(ctime).strftime("%Y-%m-%d")
                # Build destination folder
                dest_folder = os.path.join(sorted_dir, group, date_str)
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                dest_path = os.path.join(dest_folder, fname)
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
    sort_by_date_and_type()
