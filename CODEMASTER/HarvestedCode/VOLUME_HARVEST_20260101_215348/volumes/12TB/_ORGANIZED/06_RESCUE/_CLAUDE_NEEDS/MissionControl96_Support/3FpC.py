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

def extract_info(filename):
    """
    Example extraction: Try to get Manufacturer and Library from filename.
    Adjust the regex or logic as needed for your file naming conventions.
    """
    # Example: "Spitfire_Albion_One_Percussion_001.nki" → Manufacturer: Spitfire, Library: Albion_One
    match = re.match(r"([A-Za-z0-9]+)_([A-Za-z0-9_]+)", filename)
    if match:
        manufacturer = match.group(1)
        library = match.group(2)
        return manufacturer, library
    else:
        return "Unknown", "Unknown"

def organize_files(folder):
    for file in folder.iterdir():
        if file.is_file():
            manufacturer, library = extract_info(file.stem)
            dest_folder = folder / manufacturer / library
            dest_folder.mkdir(parents=True, exist_ok=True)
            dest_path = dest_folder / file.name
            print(f"Moving {file.name} → {dest_folder}/")
            shutil.move(str(file), str(dest_path))

if __name__ == "__main__":
    organize_files(KTK_TO_ORGANIZE)
    subprocess.Popen(["python3", str(Path.home() / "Desktop" / "KONTAKT_LAB" / "PROJECT_ORGANIZER" / "organize_ktk_to_organize.py")])