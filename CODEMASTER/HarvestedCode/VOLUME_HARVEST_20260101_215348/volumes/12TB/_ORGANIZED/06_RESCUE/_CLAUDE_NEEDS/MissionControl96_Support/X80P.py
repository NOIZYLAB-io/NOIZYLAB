import os
import time

AUTO_APPROVE = True
WATCH_FILE = "/Users/rsp_ms/Documents/rituals/NoizyAutoRun.py"

def run_capsule():
    print("Capsule executed!")
    # Add your capsule logic here

def watch_file():
    last_modified = os.path.getmtime(WATCH_FILE)
    print("Watching for changes...")
    while True:
        time.sleep(2)
        current_modified = os.path.getmtime(WATCH_FILE)
        if current_modified != last_modified:
            last_modified = current_modified
            run_capsule()

if __name__ == "__main__":
    watch_file()
