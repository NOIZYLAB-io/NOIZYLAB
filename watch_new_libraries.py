from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import time, subprocess, sys, os
import shutil
import re

WATCH_DIR = Path("/Volumes/4TB Blue Fish/Native Instruments")
SCRIPT = Path(__file__).parent / "cleaner.py"

class NewFolderHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            print(f"🐣 New folder detected: {event.src_path}")
            env = os.environ.copy()
            env["PERFECTIONIST_PATH"] = event.src_path
            try:
                subprocess.Popen([sys.executable, str(SCRIPT)], env=env)
            except Exception as e:
                print(f"Failed to launch cleaner: {e}")

if __name__ == "__main__":
    obs = Observer()
    handler = NewFolderHandler()
    obs.schedule(handler, str(WATCH_DIR), recursive=False)
    obs.start()
    print(f"👀 Watching {WATCH_DIR} for new libraries...")
    try:
        while True:
            time.sleep(2)
    except KeyboardInterrupt:
        obs.stop()
    obs.join()

    ROOT_DIR = Path(__file__).resolve().parents[1]
    subprocess.Popen([sys.executable, str(ROOT_DIR / "core" / "watcher.py")])

import os
import shutil
import re
from pathlib import Path

KTK_TO_ORGANIZE = Path.home() / "Desktop" / "KTK_TO_ORGANIZE"
BACKUP_DIR = Path.home() / "Desktop" / "KTK_TO_ORGANIZE_BACKUP"
ORGANIZED_DIR = Path.home() / "Desktop" / "KTK_ORGANIZED"

def backup_folder(src, dst):
    if not dst.exists():
        print(f"Backing up {src} to {dst} ...")
        shutil.copytree(src, dst)
    else:
        print(f"Backup already exists at {dst}")

def restore_factory_name(name):
    # Remove 'copy', 'duplicate', trailing numbers, underscores, etc.
    name = re.sub(r'(_copy\d*| copy|\sduplicate|\s\(\d+\))', '', name, flags=re.IGNORECASE)
    name = re.sub(r'_{2,}', '_', name)
    name = re.sub(r'\s+', '_', name)
    name = re.sub(r'(_|-)+$', '', name)  # Remove trailing underscores/hyphens
    name = name.strip('_- ')
    return name

def extract_info(filename):
    """
    Try to extract Manufacturer and Library from filename.
    Example: "Spitfire_Albion_One_Percussion_001.nki" → Manufacturer: Spitfire, Library: Albion_One
    Adjust this logic for your naming conventions.
    """
    parts = re.split(r'[_\-\s]', filename)
    if len(parts) >= 2:
        manufacturer = restore_factory_name(parts[0])
        library = restore_factory_name(parts[1])
        return manufacturer or "Unknown", library or "Unknown"
    else:
        return "Unknown", "Unknown"

def organize_and_restore(folder, dest):
    for root, dirs, files in os.walk(folder):
        for fname in files:
            fpath = Path(root) / fname
            # Restore name
            clean_name = restore_factory_name(fpath.stem) + fpath.suffix
            # Extract info for organizing
            manufacturer, library = extract_info(clean_name)
            dest_folder = dest / manufacturer / library
            dest_folder.mkdir(parents=True, exist_ok=True)
            dest_path = dest_folder / clean_name
            # Move and rename
            print(f"Moving {fpath} → {dest_path}")
            shutil.copy2(fpath, dest_path)
    print("✅ All files organized and names restored.")

if __name__ == "__main__":
    backup_folder(KTK_TO_ORGANIZE, BACKUP_DIR)
    ORGANIZED_DIR.mkdir(exist_ok=True)
    organize_and_restore(KTK_TO_ORGANIZE, ORGANIZED_DIR)
    print(f"\n🏁 Super Intelligent Organization Complete!\nCheck: {ORGANIZED_DIR}")