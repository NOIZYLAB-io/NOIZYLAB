from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import time, subprocess, sys, os

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

import subprocess
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
subprocess.Popen([sys.executable, str(ROOT_DIR / "core" / "watcher.py")])