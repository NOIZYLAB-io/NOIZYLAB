#!/usr/bin/env python3
import os
import shutil

# Define folder paths
main_drive_folder = "/Users/rsp_ms/Documents/_2026_WDC/Noizyfish_Aquarium"
vm_drive_folder = "/Volumes/NoizyWind/Noizyfish_Aquarium"
desktop_noizy_temp = os.path.expanduser("~/Desktop/Noizy_Temp")
old_noizybitz_folder = os.path.expanduser("~/Documents/_NOIZYBITZ")

# Code file extensions and subfolders
code_exts = {".txt": "TXT", ".py": "PY", ".sh": "SH", ".md": "MD"}

def check_and_create(folder_path):
    if os.path.exists(folder_path):
        print(f"✅ Folder exists: {folder_path}")
    else:
        os.makedirs(folder_path, exist_ok=True)
        print(f"📁 Folder created: {folder_path}")

def move_code_files(src_folder, dst_folder):
    if os.path.exists(src_folder):
        for filename in os.listdir(src_folder):
            ext = os.path.splitext(filename)[1].lower()
            src = os.path.join(src_folder, filename)
            dst_subfolder = os.path.join(dst_folder, code_exts.get(ext, "OTHER"))
            os.makedirs(dst_subfolder, exist_ok=True)
            dst = os.path.join(dst_subfolder, filename)
            if os.path.isfile(src) and ext in code_exts:
                shutil.move(src, dst)
                print(f"📦 Moved {filename} to {dst_subfolder}")
    else:
        print(f"❌ Source folder not found: {src_folder}")

def delete_empty_folder(folder_path):
    if os.path.exists(folder_path):
        if not os.listdir(folder_path):
            shutil.rmtree(folder_path)
            print(f"✅ Deleted empty folder: {folder_path}")
        else:
            print(f"⚠️ Folder {folder_path} is not empty. No action taken.")
    else:
        print(f"ℹ️ Folder {folder_path} does not exist. No action needed.")

# Step 1: Check and create Noizyfish_Aquarium on both drives
print("Checking Noizyfish_Aquarium on main drive...")
check_and_create(main_drive_folder)
print("Checking Noizyfish_Aquarium on VM/external drive...")
check_and_create(vm_drive_folder)

# Step 2: Move code files from Desktop Noizy_Temp and old _NOIZYBITZ to Noizyfish_Aquarium
move_code_files(desktop_noizy_temp, main_drive_folder)
move_code_files(old_noizybitz_folder, main_drive_folder)

# Step 3: Delete _NOIZYBITZ folder if it exists and is empty
delete_empty_folder(old_noizybitz_folder)

print("🎉 All code files are now organized in Noizyfish_Aquarium. Automation complete.")