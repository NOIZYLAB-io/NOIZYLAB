import os
import re
import shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
MISC_FOLDER = "Misc"

def normalize_suffix(suffix):
    # Remove trailing numbers and whitespace, e.g., "Bod Lick 01" -> "Bod Lick"
    suffix = re.sub(r'\s*\d+\s*$', '', suffix)
    # Replace '140' with '140Bpm'
    suffix = suffix.replace("140", "140Bpm")
    return suffix.strip() if suffix else "Other"

def group_and_organize():
    print(f"Scanning in: {ROOT}")
    pattern = re.compile(r"^(C\d+)\s*([A-Za-z0-9 ()\-]+)?(\.[a-z0-9]+)$", re.IGNORECASE)
    files_to_move = []

    # Collect all files recursively (including those in subfolders)
    for root, dirs, files in os.walk(ROOT):
        for filename in files:
            abs_path = os.path.join(root, filename)
            rel_path = os.path.relpath(abs_path, ROOT)
            # Always process, even if in subfolders
            files_to_move.append((abs_path, filename))

    print(f"Found {len(files_to_move)} files to organize.")

    for abs_path, filename in files_to_move:
        match = pattern.match(filename)
        if match:
            prefix = match.group(1)
            suffix = match.group(2).strip() if match.group(2) else "Other"
            suffix = normalize_suffix(suffix)
            target_dir = os.path.join(ROOT, prefix, suffix)
        else:
            target_dir = os.path.join(ROOT, MISC_FOLDER)

        os.makedirs(target_dir, exist_ok=True)
        dst = os.path.join(target_dir, filename)
        if os.path.abspath(abs_path) != os.path.abspath(dst):
            try:
                shutil.move(abs_path, dst)
                print(f"Moved: {abs_path} -> {dst}")
            except Exception as e:
                print(f"Failed to move {abs_path}: {e}")
        else:
            print(f"Skipped (already in place): {filename}")

def delete_empty_folders(path):
    print(f"Deleting empty folders in: {path}")
    for root, dirs, files in os.walk(path, topdown=False):
        for d in dirs:
            dir_path = os.path.join(root, d)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                print(f"Deleted empty folder: {dir_path}")

if __name__ == "__main__":
    print("Script started")
    group_and_organize()
    delete_empty_folders(ROOT)