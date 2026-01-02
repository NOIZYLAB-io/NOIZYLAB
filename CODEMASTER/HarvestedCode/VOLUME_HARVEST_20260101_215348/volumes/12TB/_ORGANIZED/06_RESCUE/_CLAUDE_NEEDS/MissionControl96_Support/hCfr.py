#!/usr/bin/env python3
import os, shutil

def organize_by_extension(target_dir):
    for root, _, files in os.walk(target_dir):
        for f in files:
            ext = os.path.splitext(f)[1].lower() or "_noext"
            dest = os.path.join(target_dir, ext.strip("."))
            os.makedirs(dest, exist_ok=True)
            src_file = os.path.join(root, f)
            try:
                shutil.move(src_file, os.path.join(dest, f))
            except Exception as e:
                print(f"Skipping {f}: {e}")

if __name__ == "__main__":
    folder = input("Enter folder to sort: ").strip()
    if os.path.exists(folder):
        organize_by_extension(folder)
        print("✅ Sorting complete!")
    else:
        print("❌ Folder not found.")
