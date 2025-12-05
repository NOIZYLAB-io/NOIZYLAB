#!/usr/bin/env python3
import os
import shutil

TARGET_FOLDER = "/Volumes/6TB/Native Instruments/8Dio Libraries/8Dio Hybrid Action Tools Equinox"
ROOT_SEARCH = "/Volumes/6TB/Native Instruments"  # Adjust as needed
LOG_FILE = "organize_equinox_log.txt"

def organize_equinox_files(target_folder=TARGET_FOLDER, root_search=ROOT_SEARCH, log_file=LOG_FILE):
    moved = []
    # Absolute path for target
    target_abs = os.path.join(root_search, target_folder)
    if not os.path.exists(target_abs):
        os.makedirs(target_abs)
    # Walk through all files and folders under root_search
    for root, dirs, files in os.walk(root_search):
        for fname in files:
            fpath = os.path.join(root, fname)
            # If file is loose and should be in target folder
            if target_folder in fpath and not fpath.startswith(target_abs):
                # Compute relative path after target_folder
                rel_path = fpath.split(target_folder, 1)[-1].lstrip(os.sep)
                dest_path = os.path.join(target_abs, rel_path)
                dest_dir = os.path.dirname(dest_path)
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
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
        print("\nNo loose files found to move.")

if __name__ == "__main__":
    organize_equinox_files()
