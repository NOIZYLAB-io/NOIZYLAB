#!/usr/bin/env python3
import os
import shutil

# List of root directories to search
SEARCH_ROOTS = ["/Volumes", "/Users"]
# Name pattern to search for
PATTERN = "Bombay"
# Destination folder for found files
DEST_FOLDER = "/Volumes/4TB BLK/_The Clean-Up/worldbeat bombay"
# File extensions to consider (add more if needed)
FILE_EXTENSIONS = [".nki", ".wav", ".aif", ".aiff"]

def find_and_move_files(search_roots, pattern, dest_folder, extensions):
    for root in search_roots:
        for dirpath, dirnames, filenames in os.walk(root):
            for fname in filenames:
                if pattern.lower() in fname.lower() and any(fname.lower().endswith(ext) for ext in extensions):
                    src_path = os.path.join(dirpath, fname)
                    dest_path = os.path.join(dest_folder, fname)
                    try:
                        shutil.copy2(src_path, dest_path)
                        print(f"Copied: {src_path} -> {dest_path}")
                    except Exception as e:
                        print(f"Error copying {src_path}: {e}")

if __name__ == "__main__":
    os.makedirs(DEST_FOLDER, exist_ok=True)
    find_and_move_files(SEARCH_ROOTS, PATTERN, DEST_FOLDER, FILE_EXTENSIONS)
