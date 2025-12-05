#!/usr/bin/env python3
import os
import shutil

# Path to the file listing missing files (one per line)
MISSING_FILES_LIST = "missing_files.txt"
# Root folder where the reconstructed hierarchy will be created
RECONNECT_ROOT = "Reconnected_Libraries"

def get_original_path(line):
    # Extract original path from the line (customize if needed)
    # Example: '/Volumes/DriveA/Libraries/Omnisphere/Presets/patch.nki'
    return line.strip()

def reconnect_libraries(missing_files_list, reconnect_root):
    if not os.path.exists(missing_files_list):
        print(f"Missing files list not found: {missing_files_list}")
        return
    with open(missing_files_list, "r") as f:
        missing_files = [line.strip() for line in f if line.strip()]
    for orig_path in missing_files:
        if not os.path.exists(orig_path):
            print(f"Original file not found: {orig_path}")
            continue
        # Recreate hierarchy under reconnect_root
        rel_path = os.path.relpath(orig_path, start=os.path.commonpath([orig_path]))
        target_path = os.path.join(reconnect_root, rel_path)
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        try:
            shutil.copy2(orig_path, target_path)
            print(f"Copied: {orig_path} -> {target_path}")
        except Exception as e:
            print(f"Error copying {orig_path}: {e}")

if __name__ == "__main__":
    reconnect_libraries(MISSING_FILES_LIST, RECONNECT_ROOT)
