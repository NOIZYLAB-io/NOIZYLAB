import os
import subprocess
import time

# CONFIGURATION
FILE_PATH = "/Users/rsp_ms/Documents/rituals/my_script.py"  # Update this path
RUNTIME = "python3"  # Or "node", "bash", etc.
GIT_ENABLED = True
GIT_COMMIT_MSG = "🔁 Ritual Executed: Capsule Clean — Soul Synced to Legacy Grid"

def is_valid_python(file_path):
    try:
        subprocess.check_output([RUNTIME, "-m", "py_compile", file_path])
        return True
    except subprocess.CalledProcessError:
        return False

def auto_save_and_run():
    print("🔮 NoizyGenieMode: Validating...")
    if is_valid_python(FILE_PATH):
        print("✅ Code is clean. Running ritual...")
        subprocess.run([RUNTIME, FILE_PATH])
        if GIT_ENABLED:
            git_sync()
    else:
        print("❌ Syntax error detected. Launching fallback overlay...")
        launch_debugger()

def git_sync():
    print("🌐 Syncing soul to GitHub...")
    subprocess.run(["git", "add", FILE_PATH])
    subprocess.run(["git", "commit", "-m", GIT_COMMIT_MSG])
    subprocess.run(["git", "push"])

def launch_debugger():
    print("🧠 Fallback triggered. Opening debugger overlay...")
    subprocess.run(["code", FILE_PATH])  # Opens file in VS Code

if __name__ == "__main__":
    auto_save_and_run()
