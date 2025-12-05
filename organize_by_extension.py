import os
import shutil

# Set the target directory
TARGET_DIR = '/Users/rsp_ms'

# List all files in the target directory (ignore hidden files and folders)
for item in os.listdir(TARGET_DIR):
    item_path = os.path.join(TARGET_DIR, item)
    if os.path.isfile(item_path) and not item.startswith('.'):
        ext = os.path.splitext(item)[1].lower().lstrip('.')
        if ext:
            ext_dir = os.path.join(TARGET_DIR, ext + '_files')
            os.makedirs(ext_dir, exist_ok=True)
            shutil.move(item_path, os.path.join(ext_dir, item))

print('Files organized by extension.')
