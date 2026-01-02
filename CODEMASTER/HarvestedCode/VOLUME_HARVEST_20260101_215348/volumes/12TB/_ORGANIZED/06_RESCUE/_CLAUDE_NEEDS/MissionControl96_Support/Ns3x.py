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
    pattern = re.compile(r"^(C\d+)\s*([A-Za-z0-9 ()\-]+)?(\.[a-z0-9]+)$", re.IGNORECASE)
    files_to_move = []

    # Collect all files recursively
    for root, dirs, files in os.walk(ROOT):
        for filename in files:
            abs_path = os.path.join(root, filename)
            rel_path = os.path.relpath(abs_path, ROOT)
            # Skip files already in grouped folders (by checking if rel_path has more than 1 sep)
            if rel_path.count(os.sep) > 0:
                continue
            files_to_move.append(filename)

    for filename in files_to_move:
        match = pattern.match(filename)
        if match:
            prefix = match.group(1)
            suffix = match.group(2).strip() if match.group(2) else "Other"
            suffix = normalize_suffix(suffix)
            target_dir = os.path.join(ROOT, prefix, suffix)
        else:
            target_dir = os.path.join(ROOT, MISC_FOLDER)

        os.makedirs(target_dir, exist_ok=True)
        src = os.path.join(ROOT, filename)
        dst = os.path.join(target_dir, filename)
        if os.path.abspath(src) != os.path.abspath(dst):
            shutil.move(src, dst)
            print(f"Moved: {filename} -> {target_dir}")

def delete_empty_folders(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for d in dirs:
            dir_path = os.path.join(root, d)
            if not os.listdir(dir_path):
                os.rmdir(dir_path)
                print(f"Deleted empty folder: {dir_path}")

if __name__ == "__main__":
    group_and_organize()
    delete_empty_folders(ROOT)