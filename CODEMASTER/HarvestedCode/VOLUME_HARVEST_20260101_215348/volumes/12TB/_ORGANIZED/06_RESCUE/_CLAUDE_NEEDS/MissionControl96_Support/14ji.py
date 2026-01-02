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

KTK_TO_ORGANIZE = Path.home() / "Desktop" / "KTK_TO_ORGANIZE"
BACKUP_DIR = Path.home() / "Desktop" / "KTK_TO_ORGANIZE_BACKUP"
ORGANIZED_DIR = Path.home() / "Desktop" / "KTK_ORGANIZED"

# Optional: Provide a mapping of known libraries for perfect restoration
# Example: {"spitfire_albion_one": ("Spitfire Audio", "Albion One")}
KNOWN_LIBRARIES = {
    # "spitfire_albion_one": ("Spitfire Audio", "Albion One"),
    # Add more mappings as needed for 100% accuracy
}

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
    # Capitalize intuitively: "spitfire_albion_one" → "Spitfire_Albion_One"
    name = "_".join([w.capitalize() for w in name.split("_") if w])
    return name

def extract_info_from_folder(folder_name):
    key = folder_name.lower().replace(" ", "_").replace("-", "_")
    if key in KNOWN_LIBRARIES:
        return KNOWN_LIBRARIES[key]
    # Heuristic: split on underscores, dashes, or spaces
    parts = re.split(r'[_\-\s]', folder_name)
    if len(parts) >= 2:
        manufacturer = restore_factory_name(parts[0])
        library = restore_factory_name("_".join(parts[1:]))
        return manufacturer or "Unknown", library or "Unknown"
    else:
        return "Unknown", restore_factory_name(folder_name)

def restore_folder_and_files(src_folder, dest_root):
    for item in src_folder.iterdir():
        if item.is_dir():
            manufacturer, library = extract_info_from_folder(item.name)
            dest_folder = dest_root / manufacturer / library
            dest_folder.mkdir(parents=True, exist_ok=True)
            print(f"\n📦 Restoring Library: {item.name} → {dest_folder}")
            # Recursively restore all files and subfolders
            for root, dirs, files in os.walk(item):
                rel_root = Path(root).relative_to(item)
                for d in dirs:
                    d_clean = restore_factory_name(d)
                    (dest_folder / rel_root / d_clean).mkdir(parents=True, exist_ok=True)
                for f in files:
                    src_file = Path(root) / f
                    f_clean = restore_factory_name(Path(f).stem) + Path(f).suffix.lower()
                    dest_file = dest_folder / rel_root / f_clean
                    print(f"  Moving {src_file} → {dest_file}")
                    shutil.copy2(src_file, dest_file)
        elif item.is_file():
            # Handle loose files at the root
            f_clean = restore_factory_name(item.stem) + item.suffix.lower()
            dest_file = dest_root / "Unknown" / "Loose_Files" / f_clean
            dest_file.parent.mkdir(parents=True, exist_ok=True)
            print(f"  Moving {item} → {dest_file}")
            shutil.copy2(item, dest_file)

if __name__ == "__main__":
    backup_folder(KTK_TO_ORGANIZE, BACKUP_DIR)
    ORGANIZED_DIR.mkdir(exist_ok=True)
    restore_folder_and_files(KTK_TO_ORGANIZE, ORGANIZED_DIR)
    print(f"\n🏁 Factory Default Restoration Complete!\nCheck: {ORGANIZED_DIR}")

    print("\nTIP: For 100% accuracy, add your libraries to the KNOWN_LIBRARIES mapping at the top of this script.")
    subprocess.Popen(["python3", str(Path.home() / "Desktop" / "KONTAKT_LAB" / "PROJECT_ORGANIZER" / "super_intelligent_factory_restore.py")])