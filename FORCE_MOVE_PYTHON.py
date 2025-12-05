#!/usr/bin/env python3
# FORCE_MOVE_PYTHON.py
# Force copy all code files then delete from system drive

import os
import shutil
import sys

HOME_DIR = "/Users/rsp_ms"
BACKUP_DIR = "/Volumes/4TB_02/CODE_MASTER/System_Backup"

print("🚨 FORCE COPY AND DELETE - Moving all code files")
print("")

# Create backup directories
os.makedirs(f"{BACKUP_DIR}/.config", exist_ok=True)
os.makedirs(f"{BACKUP_DIR}/.windsurf", exist_ok=True)
os.makedirs(f"{BACKUP_DIR}/.codegpt", exist_ok=True)
os.makedirs(f"{BACKUP_DIR}/.gemini", exist_ok=True)
os.makedirs(f"{BACKUP_DIR}/.rest-client", exist_ok=True)

def copy_and_delete(src, dest, name):
    if not os.path.exists(src):
        print(f"⏭️  {name}: Not found")
        return False
    
    print(f"📦 {name}...")
    
    try:
        if os.path.isdir(src):
            shutil.copytree(src, dest, dirs_exist_ok=True)
            shutil.rmtree(src)
        else:
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            shutil.copy2(src, dest)
            os.remove(src)
        print(f"   ✅ Copied and deleted")
        return True
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

# Move directories
copy_and_delete(f"{HOME_DIR}/.config/gcloud", f"{BACKUP_DIR}/.config/gcloud", ".config/gcloud")
copy_and_delete(f"{HOME_DIR}/.config/configstore", f"{BACKUP_DIR}/.config/configstore", ".config/configstore")
copy_and_delete(f"{HOME_DIR}/.config/Dadroit", f"{BACKUP_DIR}/.config/Dadroit", ".config/Dadroit")
copy_and_delete(f"{HOME_DIR}/.rest-client", f"{BACKUP_DIR}/.rest-client", ".rest-client")
copy_and_delete(f"{HOME_DIR}/.codegpt", f"{BACKUP_DIR}/.codegpt", ".codegpt")
copy_and_delete(f"{HOME_DIR}/.gemini", f"{BACKUP_DIR}/.gemini", ".gemini")

# Move .windsurf Python files
print("📁 .windsurf Python files...")
windsurf_ext = f"{HOME_DIR}/.windsurf/extensions"
if os.path.exists(windsurf_ext):
    for root, dirs, files in os.walk(windsurf_ext):
        if 'node_modules' in root:
            continue
        for file in files:
            if file.endswith(('.py', '.js', '.json')):
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, f"{HOME_DIR}/.windsurf")
                dest_path = os.path.join(BACKUP_DIR, ".windsurf", rel_path)
                try:
                    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                    shutil.copy2(src_path, dest_path)
                    os.remove(src_path)
                    print(f"   ✅ {file}")
                except Exception as e:
                    print(f"   ⚠️  {file}: {e}")

print("")
print("📊 Summary:")
try:
    total_size = sum(
        os.path.getsize(os.path.join(dirpath, filename))
        for dirpath, dirnames, filenames in os.walk(BACKUP_DIR)
        for filename in filenames
    )
    size_mb = total_size / (1024 * 1024)
    print(f"   Total: {size_mb:.2f} MB")
except:
    print("   Calculating...")

print("")
print("✅ Force copy and delete complete!")

