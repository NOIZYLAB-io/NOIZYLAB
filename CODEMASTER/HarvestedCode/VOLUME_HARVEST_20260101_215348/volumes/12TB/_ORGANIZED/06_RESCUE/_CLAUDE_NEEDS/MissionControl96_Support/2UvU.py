import os
import subprocess
import time

# CONFIGURATION
WATCH_FILE = "/Users/rsp_ms/Documents/rituals/NoizyAutoRun.py"
RUNTIME = "python3"
GIT_ENABLED = True
GIT_COMMIT_MSG = "🔁 AutoRun Capsule Executed — Code Saved & Soul Synced"

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
        speak("Code is clean. Executing capsule.")
        subprocess.run([RUNTIME, WATCH_FILE])
        if GIT_ENABLED:
            git_sync()
    else:
        speak("Syntax error detected. Launching fallback overlay.")
        subprocess.run(["code", WATCH_FILE])  # Opens in VS Code

def git_sync():
    speak("Syncing soul to GitHub...")
    subprocess.run(["git", "-C", os.path.dirname(WATCH_FILE), "add", "."])
    subprocess.run(["git", "-C", os.path.dirname(WATCH_FILE), "commit", "-m", GIT_COMMIT_MSG])
    subprocess.run(["git", "-C", os.path.dirname(WATCH_FILE), "push"])

def watch_file():
    last_modified = os.path.getmtime(WATCH_FILE)
    speak("NOIZYLAB AutoRun Daemon is watching...")
    while True:
        time.sleep(2)
        current_modified = os.path.getmtime(WATCH_FILE)
        if current_modified != last_modified:
            last_modified = current_modified
            speak("Change detected. Saving and running capsule.")
            run_capsule()

if __name__ == "__main__":
    watch_file()
