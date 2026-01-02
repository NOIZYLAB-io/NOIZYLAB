
import os
import shutil
from pathlib import Path
from multiprocessing import Pool, cpu_count

# Set destination folder
DEST_FOLDER = '/Users/rsp_ms/Documents/_2026_WDC/Noizyfish_Aquarium'
# Set volume root (macOS typical mount point)
VOLUMES_ROOT = '/Volumes'
# Volume to exclude
EXCLUDE_VOLUME = 'mission control'

# Code file extensions and their target subfolders
EXTENSION_MAP = {
    '.py': 'python',
    '.sh': 'shell',
    '.js': 'javascript',
    '.java': 'java',
    '.c': 'c',
    '.cpp': 'cpp',
    '.rb': 'ruby',
    '.go': 'go',
    '.ts': 'typescript',
    '.php': 'php',
    '.pl': 'perl',
    '.swift': 'swift',
    '.cs': 'csharp',
    '.html': 'html',
    '.css': 'css',
    '.json': 'json',
    '.xml': 'xml',
    '.md': 'markdown',
    '.bat': 'batch',
    '.ps1': 'powershell',
    '.r': 'r',
    '.jl': 'julia',
    '.ipynb': 'notebooks',
}

def is_code_file(filename):
    return any(filename.lower().endswith(ext) for ext in EXTENSION_MAP)

def move_code_file(args):
    src_file, ext = args
    subfolder = EXTENSION_MAP.get(ext, ext[1:] if ext else 'other')
    dest_dir = os.path.join(DEST_FOLDER, subfolder)
    os.makedirs(dest_dir, exist_ok=True)
    dest_file = os.path.join(dest_dir, os.path.basename(src_file))
    try:
        shutil.move(src_file, dest_file)
        print(f"Moved: {src_file} -> {dest_file}")
    except Exception as e:
        print(f"Error moving {src_file}: {e}")

def organize_code_files_parallel():
    tasks = []
    for volume in os.listdir(VOLUMES_ROOT):
        if volume.lower() == EXCLUDE_VOLUME.lower():
            continue
        vol_path = os.path.join(VOLUMES_ROOT, volume)
        for root, dirs, files in os.walk(vol_path):
            for file in files:
                if is_code_file(file):
                    ext = Path(file).suffix.lower()
                    src_file = os.path.join(root, file)
                    tasks.append((src_file, ext))
    # Use up to 96 minions (processes)
    minions = min(96, cpu_count())
    with Pool(processes=minions) as pool:
        pool.map(move_code_file, tasks)
    print("Code file organization complete (parallel mode).")

def delete_empty_dirs():
    for volume in os.listdir(VOLUMES_ROOT):
        if volume.lower() == EXCLUDE_VOLUME.lower():
            continue
        vol_path = os.path.join(VOLUMES_ROOT, volume)
        for root, dirs, files in os.walk(vol_path, topdown=False):
            if not os.listdir(root):
                try:
                    os.rmdir(root)
                    print(f"Deleted empty folder: {root}")
                except Exception as e:
                    print(f"Error deleting {root}: {e}")
    print("Empty folder cleanup complete.")

if __name__ == "__main__":
    organize_code_files_parallel()
    delete_empty_dirs()
