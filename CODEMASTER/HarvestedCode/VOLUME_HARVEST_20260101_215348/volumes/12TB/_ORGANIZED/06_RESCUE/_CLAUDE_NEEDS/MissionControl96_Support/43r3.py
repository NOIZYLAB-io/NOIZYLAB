import os
import subprocess
import time

# CONFIGURATION
WATCH_FILE = "/Users/rsp_ms/Documents/rituals/NoizyAutoRun.py"
RUNTIME = "python3"
GIT_ENABLED = True
AUTO_APPROVE = True
AUTO_KEEP = True
GIT_COMMIT_MSG = "🔁 CODE IS GOOD, RSP IS GREAT!!! — Capsule Eternalized"

def speak(message):
    os.system(f'say "{message}"')

def is_valid_python(file_path):
    try:
        subprocess.check_output([RUNTIME, "-m", "py_compile", file_path])
        return True
    except subprocess.CalledProcessError:
        return False

def run_capsule():
    speak("Validating capsule...")
    if is_valid_python(WATCH_FILE):
        speak("CODE IS GOOD, RSP IS GREAT!!!")
        subprocess.run([RUNTIME, WATCH_FILE])
        if GIT_ENABLED and AUTO_KEEP:
            git_sync()
    else:
        speak("Syntax error detected. Launching fallback overlay.")
        subprocess.run(["code", WATCH_FILE])  # Opens in VS Code

def git_sync():
    speak("AutoKeep activated. Syncing soul to GitHub...")
    subprocess.run(["git", "-C", os.path.dirname(WATCH_FILE), "add", "."])
    subprocess.run(["git", "-C", os.path.dirname(WATCH_FILE), "commit", "-m", GIT_COMMIT_MSG])
    subprocess.run(["git", "-C", os.path.dirname(WATCH_FILE), "push"])

def watch_file():
    last_modified = os.path.getmtime(WATCH_FILE)
    speak("NOIZYLAB AutoKeep Daemon is watching...")
    while True:
        time.sleep(2)
        current_modified = os.path.getmtime(WATCH_FILE)
        if current_modified != last_modified:
            last_modified = current_modified
            speak("Change detected. Validating and eternalizing capsule.")
            run_capsule()

if __name__ == "__main__":
    watch_file()
