import os
import shutil

# Base directory
BASE_DIR = '/Volumes/4TBSG/2025_NOIZYFISH'
PY_DIR = os.path.join(BASE_DIR, 'py')
SH_DIR = os.path.join(BASE_DIR, 'sh')

# Create central folders if they don't exist
os.makedirs(PY_DIR, exist_ok=True)
os.makedirs(SH_DIR, exist_ok=True)

# Helper to move files
def move_file(src, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)
    dest = os.path.join(dest_dir, os.path.basename(src))
    if os.path.abspath(src) != os.path.abspath(dest):
        shutil.move(src, dest)
        print(f"Moved {src} -> {dest}")

# Walk through all files in BASE_DIR
for root, dirs, files in os.walk(BASE_DIR):
    # Skip central folders to avoid moving already organized files
    if root.startswith(PY_DIR) or root.startswith(SH_DIR):
        continue
    for file in files:
        src_path = os.path.join(root, file)
        # Organize Python scripts
        if file.endswith('.py'):
            move_file(src_path, PY_DIR)
        # Organize shell scripts
        elif file.endswith('.sh'):
            move_file(src_path, SH_DIR)
        # Organize other files into project folders
        else:
            # Try to infer project folder from root
            rel_root = os.path.relpath(root, BASE_DIR)
            if rel_root == '.' or rel_root.startswith('_') or rel_root.startswith('audioenv') or rel_root.startswith('music_ai_env') or rel_root.startswith('pyenv'):
                # Skip root and environment folders
                continue
            project_folder = os.path.join(BASE_DIR, rel_root)
            move_file(src_path, project_folder)

print("Organization complete.")
