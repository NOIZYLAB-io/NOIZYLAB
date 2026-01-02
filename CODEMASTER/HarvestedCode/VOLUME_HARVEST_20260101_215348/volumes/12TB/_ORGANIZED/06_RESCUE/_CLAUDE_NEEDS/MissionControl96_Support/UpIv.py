import os
import time

WATCH_FILE = "/Users/rsp_ms/Documents/rituals/NoizyAutoRun.py"
GIT_COMMIT_MSG = "🔁 CODE IS GOOD, RSP IS GREAT!!! — Capsule Eternalized"

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
