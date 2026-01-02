import os
import time

WATCH_FILE = "/Users/rsp_ms/Documents/rituals/NoizyAutoRun.py"
GIT_COMMIT_MSG = "🔁 CODE IS GOOD, RSP IS GREAT!!! — Capsule Eternalized"

def speak(message):
    os.system(f'say "{message}"')

def run_capsule():
    speak("CODE IS GOOD, RSP IS GREAT!!!")
    print("Capsule executed!")
    # Add your capsule logic here

def watch_file():
    if not os.path.exists(WATCH_FILE):
        print(f"Error: {WATCH_FILE} does not exist.")
        return
    last_modified = os.path.getmtime(WATCH_FILE)
    print("Watching for changes...")
    while True:
        time.sleep(2)
        if not os.path.exists(WATCH_FILE):
            print(f"Error: {WATCH_FILE} was deleted.")
            break
        current_modified = os.path.getmtime(WATCH_FILE)
        if current_modified != last_modified:
            last_modified = current_modified
            run_capsule()

if __name__ == "__main__":
    watch_file()
