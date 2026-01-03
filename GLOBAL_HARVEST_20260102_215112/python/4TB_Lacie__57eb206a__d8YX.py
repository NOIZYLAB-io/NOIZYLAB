#!/usr/bin/env python3
import os
import shutil

source_drive = "/Volumes/4TBSG"
aquarium_folder = "/Users/rsp_ms/Documents/Noizyfish_Aquarium"
folders = {
    ".py": "PY",
    ".sh": "SH",
    ".md": "MD",
    ".txt": "TXT"
}

# Ensure destination folders exist
for folder in folders.values():
    os.makedirs(os.path.join(aquarium_folder, folder), exist_ok=True)

def move_file(src, dst_folder):
    filename = os.path.basename(src)
    dst = os.path.join(dst_folder, filename)
    # Avoid overwriting files with the same name
    if os.path.exists(dst):
        base, ext = os.path.splitext(filename)
        i = 1
        while os.path.exists(os.path.join(dst_folder, f"{base}_{i}{ext}")):
            i += 1
        dst = os.path.join(dst_folder, f"{base}_{i}{ext}")
    shutil.move(src, dst)
    print(f"📦 Moved {filename} to {dst_folder}")

for dirpath, dirnames, filenames in os.walk(source_drive):
    for filename in filenames:
        ext = os.path.splitext(filename)[1].lower()
        if ext in folders:
            src = os.path.join(dirpath, filename)
            dst_folder = os.path.join(aquarium_folder, folders[ext])
            move_file(src, dst_folder)

print("🎉 All .py, .sh, .md, and .txt files from 4TBSG have been moved to Noizyfish_Aquarium.")
