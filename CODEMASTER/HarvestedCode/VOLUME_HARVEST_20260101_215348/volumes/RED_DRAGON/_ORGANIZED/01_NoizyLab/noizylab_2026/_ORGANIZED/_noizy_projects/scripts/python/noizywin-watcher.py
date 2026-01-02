import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

ISO_PATH = os.path.expanduser("~/Downloads/Win11_25H2_ARM64.iso")
ASSET_DIR = os.path.expanduser("~/NOIZYWIN_ASSETS")
BUILDER_SCRIPT = os.path.expanduser("~/Desktop/MissionControl96/noizywin-iso-builder.py")
LOG_FILE = os.path.expanduser("~/Desktop/MissionControl96/logs/watcher.log")

class ChangeHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path == ISO_PATH or event.src_path.startswith(ASSET_DIR):
            log(f"Detected new file: {event.src_path}. Triggering build.")
            run_builder()
    def on_modified(self, event):
        if event.src_path == ISO_PATH or event.src_path.startswith(ASSET_DIR):
            log(f"Detected modified file: {event.src_path}. Triggering build.")
            run_builder()

def log(msg):
    with open(LOG_FILE, "a") as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {msg}\n")
    print(msg)

def run_builder():
    try:
        subprocess.run(["python3", BUILDER_SCRIPT], check=True)
        log("ISO build completed.")
    except Exception as e:
        log(f"ISO build failed: {e}")

def main():
    log("Starting NOIZYWIN watcher...")
    event_handler = ChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=ASSET_DIR, recursive=True)
    observer.schedule(event_handler, path=os.path.dirname(ISO_PATH), recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
