#!/usr/bin/env python3
import os
import shutil
from pathlib import Path
import hashlib

# Set target folder
GITHUB_PROJECTS = '/Users/rsp_ms/Documents/_2026_WDC/Noizyfish_Aquarium/GitHub/Projects'
ARCHIVE_FOLDER = os.path.join(GITHUB_PROJECTS, 'archive')

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

def file_hash(filepath):
    """Return SHA256 hash of file contents."""
    h = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b''):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return None

def organize_and_cleanup():
    seen_hashes = set()
    for root, dirs, files in os.walk(GITHUB_PROJECTS):
        for file in files:
            file_path = os.path.join(root, file)
            ext = Path(file).suffix.lower()
            if is_code_file(file):
                # Check for duplicates by hash
                f_hash = file_hash(file_path)
                if f_hash in seen_hashes:
                    try:
                        os.remove(file_path)
                        print(f"Deleted duplicate: {file_path}")
                    except Exception as e:
                        print(f"Error deleting duplicate {file_path}: {e}")
                    continue
                seen_hashes.add(f_hash)
                # Organize by extension
                subfolder = EXTENSION_MAP.get(ext, ext[1:] if ext else 'other')
                dest_dir = os.path.join(GITHUB_PROJECTS, subfolder)
                os.makedirs(dest_dir, exist_ok=True)
                dest_file = os.path.join(dest_dir, file)
                if file_path != dest_file:
                    try:
                        shutil.move(file_path, dest_file)
                        print(f"Moved: {file_path} -> {dest_file}")
                    except Exception as e:
                        print(f"Error moving {file_path}: {e}")
            else:
                # Move non-code files to archive
                os.makedirs(ARCHIVE_FOLDER, exist_ok=True)
                archive_file = os.path.join(ARCHIVE_FOLDER, file)
                if file_path != archive_file:
                    try:
                        shutil.move(file_path, archive_file)
                        print(f"Archived: {file_path} -> {archive_file}")
                    except Exception as e:
                        print(f"Error archiving {file_path}: {e}")
    print("Organization and cleanup complete.")

def delete_empty_dirs():
    for root, dirs, files in os.walk(GITHUB_PROJECTS, topdown=False):
        if not os.listdir(root):
            try:
                os.rmdir(root)
                print(f"Deleted empty folder: {root}")
            except Exception as e:
                print(f"Error deleting {root}: {e}")
    print("Empty folder cleanup complete.")

if __name__ == "__main__":
    organize_and_cleanup()
    delete_empty_dirs()
