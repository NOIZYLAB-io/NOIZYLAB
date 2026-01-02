# BOOM Organizer Script (Python version, saved as .txt for reference)
# This script renames project folders to _lowercase, builds hierarchy, and sorts files.

import os, shutil, datetime

root = os.path.expanduser("~/Documents/_The_Aquarium")

subdirs = ["_documents", "audio", "images", "video", "scripts", "archives", "misc"]
file_map = {
    "_documents": [".pdf", ".docx", ".txt", ".md", ".rtf"],
    "audio": [".wav", ".aiff", ".mp3", ".flac"],
    "images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "video": [".mp4", ".mov", ".avi", ".mkv"],
    "scripts": [".sh", ".zsh", ".py", ".js"],
    "archives": [".zip", ".tar.gz", ".rar"]
}

def ensure_structure(project_path):
    for s in subdirs:
        os.makedirs(os.path.join(project_path, s), exist_ok=True)

def log_action(project_path, msg):
    log_file = os.path.join(project_path, "_documents", "super_brain_log.txt")
    with open(log_file, "a") as log:
        log.write(f"[{datetime.datetime.now()}] {msg}\n")

# Pass 1: reorganize folders
for item in os.listdir(root):
    item_path = os.path.join(root, item)
    if os.path.isdir(item_path):
        project_name = "_" + item.lower().lstrip("_")
        project_path = os.path.join(root, project_name)
        if item_path != project_path:
            os.rename(item_path, project_path)
            item_path = project_path
        ensure_structure(project_path)
        for f in os.listdir(project_path):
            f_path = os.path.join(project_path, f)
            if os.path.isfile(f_path):
                ext = os.path.splitext(f)[1].lower()
                placed = False
                for folder, exts in file_map.items():
                    if ext in exts:
                        shutil.move(f_path, os.path.join(project_path, folder, f))
                        log_action(project_path, f"Moved {f} -> {folder}")
                        placed = True
                        break
                if not placed:
                    shutil.move(f_path, os.path.join(project_path, "misc", f))
                    log_action(project_path, f"Moved {f} -> misc")

# Pass 2: handle loose files
for item in os.listdir(root):
    item_path = os.path.join(root, item)
    if os.path.isfile(item_path):
        unassigned = os.path.join(root, "_unassigned")
        ensure_structure(unassigned)
        ext = os.path.splitext(item)[1].lower()
        placed = False
        for folder, exts in file_map.items():
            if ext in exts:
                shutil.move(item_path, os.path.join(unassigned, folder, item))
                log_action(unassigned, f"Moved {item} -> {folder}")
                placed = True
                break
        if not placed:
            shutil.move(item_path, os.path.join(unassigned, "misc", item))
            log_action(unassigned, f"Moved {item} -> misc")

# Pass 3: delete empties
for item in os.listdir(root):
    item_path = os.path.join(root, item)
    if os.path.isdir(item_path) and not os.listdir(item_path):
        os.rmdir(item_path)
