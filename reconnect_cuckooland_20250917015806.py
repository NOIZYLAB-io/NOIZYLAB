#!/usr/bin/env python3
import os
import shutil

# Set your search root directories here
SEARCH_ROOTS = ["/Volumes", "/Users"]
# Set your target library name
TARGET_LIBRARY = "Cuckooland"
# Set your output directory for reconstructed hierarchy
OUTPUT_ROOT = "Reconnected_Cuckooland"
# File extensions to consider (add more as needed)
FILE_EXTENSIONS = [".nki", ".nkm", ".wav", ".aif", ".aiff", ".exs", ".sf2", ".pdf", ".txt"]

# Helper: Check if file or folder is part of the target library
def is_target_library(path):
    return TARGET_LIBRARY.lower() in path.lower()

# Main: Scan and reconstruct hierarchy

def scan_and_reconnect(search_roots, output_root):
    found_files = []
    for root in search_roots:
        for dirpath, dirnames, filenames in os.walk(root):
            if is_target_library(dirpath):
                for fname in filenames:
                    if any(fname.lower().endswith(ext) for ext in FILE_EXTENSIONS):
                        found_files.append(os.path.join(dirpath, fname))
            else:
                for fname in filenames:
                    fpath = os.path.join(dirpath, fname)
                    if is_target_library(fname) or any(fname.lower().endswith(ext) for ext in FILE_EXTENSIONS):
                        found_files.append(fpath)
    for orig_path in found_files:
        rel_path = os.path.relpath(orig_path, start=os.path.commonpath([orig_path]))
        target_path = os.path.join(output_root, rel_path)
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        try:
            shutil.copy2(orig_path, target_path)
            print(f"Copied: {orig_path} -> {target_path}")
        except Exception as e:
            print(f"Error copying {orig_path}: {e}")
    print(f"Total files reconnected: {len(found_files)}")

if __name__ == "__main__":
    scan_and_reconnect(SEARCH_ROOTS, OUTPUT_ROOT)
