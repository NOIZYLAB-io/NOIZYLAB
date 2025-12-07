import os
import shutil
from collections import defaultdict

# Root directory to organize
ROOT = '/Volumes/4TBSG/2025_NOIZYFISH'

# List of top-level project folders to organize
PROJECTS = [
    'Projects', 'Projects-1', '_VSC_Codes_and_Docs', '__TO_ORGANIZE', '_THE_BEAST',
    'MusicMaster', 'NOIZY_PIX', 'NOIZY_SOUNDS', 'FabFilter', 'LANDR', 'LogicInstaller',
    'Magenta', 'music_ai_env', 'audioenv', 'noizy_env', 'pyenv', 'venvs', 'venv',
    'ChatGPT_Downloads', '_New 2025 SoundCloud Uploads', 'Ready_2_Go', 'Toolbox', 'MusicLand_Art'
]

# Extensions to ignore
IGNORE_EXTS = {'.DS_Store', ''}

# Log file for actions
LOG_FILE = os.path.join(ROOT, 'organize_log.txt')

def organize_by_extension(project_path):
    """Organize files in project_path into subfolders by extension."""
    ext_map = defaultdict(list)
    for root, dirs, files in os.walk(project_path):
        # Skip subfolders already named by extension
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in IGNORE_EXTS:
                continue
            ext_map[ext].append(os.path.join(root, file))
    # Move files into extension folders
    for ext, files in ext_map.items():
        ext_folder = os.path.join(project_path, ext[1:] if ext else 'no_extension')
        os.makedirs(ext_folder, exist_ok=True)
        for file_path in files:
            dest_path = os.path.join(ext_folder, os.path.basename(file_path))
            if os.path.abspath(file_path) == os.path.abspath(dest_path):
                continue  # Already in place
            try:
                shutil.move(file_path, dest_path)
                log_action(f"Moved: {file_path} -> {dest_path}")
            except Exception as e:
                log_action(f"ERROR moving {file_path}: {e}")

def log_action(msg):
    with open(LOG_FILE, 'a') as f:
        f.write(msg + '\n')

def main():
    # Clear previous log
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
    for project in PROJECTS:
        project_path = os.path.join(ROOT, project)
        if os.path.isdir(project_path):
            organize_by_extension(project_path)
            log_action(f"Organized project: {project_path}")
        else:
            log_action(f"Skipped (not a directory): {project_path}")
    print(f"Organization complete. See log: {LOG_FILE}")

if __name__ == '__main__':
    main()
