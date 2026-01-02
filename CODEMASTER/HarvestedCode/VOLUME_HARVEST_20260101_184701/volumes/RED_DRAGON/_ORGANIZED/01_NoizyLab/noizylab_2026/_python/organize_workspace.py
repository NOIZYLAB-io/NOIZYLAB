import os
import shutil
from datetime import datetime, timedelta

# Set base paths
BASE = '/Users/rsp_ms/Documents/Noizyfish_Aquarium/Noizy_Workspace'
PROJECTS = os.path.join(BASE, 'Projects')
MUSICAPP_AUDIO = os.path.join(PROJECTS, 'MusicApp', 'src', 'audio')
BACKUP = os.path.join(BASE, 'Archive_Backups')

# Ensure backup folder exists
os.makedirs(BACKUP, exist_ok=True)
os.makedirs(MUSICAPP_AUDIO, exist_ok=True)

# Helper: Move latest file, archive older versions

def organize_python_files():
    # Map: filename (without date/version) -> list of files
    file_map = {}
    for root, dirs, files in os.walk(BASE):
        for f in files:
            if f.endswith('.py'):
                full_path = os.path.join(root, f)
                # Ignore backup/history folders
                if '.history' in full_path or 'Archive_Backups' in full_path:
                    continue
                # Use base name for grouping
                base_name = f.split('_')[0] if '_' in f else f.replace('.py', '')
                file_map.setdefault(base_name, []).append(full_path)

    for base, paths in file_map.items():
        # Sort by modified time, newest first
        paths.sort(key=lambda p: os.path.getmtime(p), reverse=True)
        latest = paths[0]
        # Move latest to MusicApp audio folder (customize as needed)
        dest = os.path.join(MUSICAPP_AUDIO, os.path.basename(latest))
        if not os.path.exists(dest):
            shutil.move(latest, dest)
        # Archive older versions
        for old in paths[1:]:
            backup_dest = os.path.join(BACKUP, os.path.basename(old))
            if not os.path.exists(backup_dest):
                shutil.move(old, backup_dest)

if __name__ == '__main__':
    organize_python_files()
    print('Python files organized. Latest versions moved to MusicApp/audio, older versions archived.')
