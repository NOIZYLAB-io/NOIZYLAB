import os
import re
import shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
MISC_FOLDER = "Misc"

def normalize_suffix(suffix):
    suffix = re.sub(r'\s*\d+\s*$', '', suffix)
    suffix = suffix.replace("140", "140Bpm")
    return suffix.strip() if suffix else "Other"

def group_and_organize():
    print(f"Scanning in: {ROOT}")
    c_pattern = re.compile(r"^(C\d+)\s*([A-Za-z0-9 ()\-]+)?(\.[a-z0-9]+)$", re.IGNORECASE)
    bod_lick_pattern = re.compile(r"^(Bod Lick)[\s\d\-]*.*(\.[a-z0-9]+)$", re.IGNORECASE)
    files_to_move = []

    for filename in os.listdir(ROOT):
        abs_path = os.path.join(ROOT, filename)
        if os.path.isfile(abs_path):
            files_to_move.append(filename)

    print(f"Found {len(files_to_move)} files to organize.")

    for filename in files_to_move:
        print(f"Processing: {filename}")
        match = c_pattern.match(filename)
        if match:
            prefix = match.group(1)
            suffix = match.group(2).strip() if match.group(2) else "Other"
            suffix = normalize_suffix(suffix)
            target_dir = os.path.join(ROOT, prefix, suffix)
        else:
            # Group all "Bod Lick..." files together
            bod_match = bod_lick_pattern.match(filename)
            if bod_match:
                target_dir = os.path.join(ROOT, "Bod Lick")
            else:
                target_dir = os.path.join(ROOT, MISC_FOLDER)

        os.makedirs(target_dir, exist_ok=True)
        src = os.path.join(ROOT, filename)
        dst = os.path.join(target_dir, filename)
        if os.path.abspath(src) != os.path.abspath(dst):
            try:
                shutil.move(src, dst)
                print(f"Moved: {src} -> {dst}")
            except Exception as e:
                print(f"Failed to move {src}: {e}")
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