import os, shutil, datetime

desktop = os.path.expanduser("~/Desktop")
aquarium = os.path.expanduser("~/Documents/_The_Aquarium")
folders_dest = os.path.join(aquarium, "_folders")
unassigned = os.path.join(aquarium, "_unassigned")
log_dir = os.path.join(aquarium, "_documents")
os.makedirs(folders_dest, exist_ok=True)
os.makedirs(unassigned, exist_ok=True)
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, "desktop_cleanup_log.txt")

def log(msg):
    with open(log_file, "a") as logf:
        logf.write(f"[{datetime.datetime.now()}] {msg}\n")

# Delete empty folders, move non-empty ones
for item in os.listdir(desktop):
    path = os.path.join(desktop, item)
    if os.path.isdir(path):
        if not os.listdir(path):  # empty
            os.rmdir(path)
            log(f"Deleted empty folder: {item}")
        else:  # move to _folders
            dest = os.path.join(folders_dest, item)
            if os.path.exists(dest):
                dest = os.path.join(folders_dest, f"{item}_{int(datetime.datetime.now().timestamp())}")
            shutil.move(path, dest)
            log(f"Moved folder {item} -> {dest}")
    elif os.path.isfile(path):
        dest = os.path.join(unassigned, item)
        if os.path.exists(dest):
            base, ext = os.path.splitext(item)
            dest = os.path.join(unassigned, f"{base}_{int(datetime.datetime.now().timestamp())}{ext}")
        shutil.move(path, dest)
        log(f"Moved file {item} -> {dest}")

print("✅ Desktop cleaned. Check _The_Aquarium/_folders and _The_Aquarium/_unassigned.") Asshole