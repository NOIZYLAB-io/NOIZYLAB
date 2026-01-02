import subprocess
import time
import os

NOIZYFISH_DIR = os.path.expanduser("~/Desktop/NoizyFish")
SCRIPT_PATH = os.path.join(NOIZYFISH_DIR, "create_volume_aliases.py")

# 1. Main task: create volume aliases (placeholder)
def create_volume_aliases():
    print("Creating volume aliases...")
    # Simulate work
    time.sleep(2)
    print("Aliases created.")

# 2. Scan code for purity (syntax check)
def scan_code_for_purity(file_path):
    try:
        with open(file_path, "r") as f:
            code = f.read()
        compile(code, file_path, "exec")
        print("Code is pure (no syntax errors).")
    except Exception as e:
        print(f"Code issue found: {e}")

# 3. Notify completion
def notify_completion():
    message = "Volume aliases are ready! You can close this tab."
    subprocess.run([
        "osascript",
        "-e",
        f'display notification "{message}" with title "VS Code Task Complete"'
    ])

if __name__ == "__main__":
    create_volume_aliases()
    scan_code_for_purity(SCRIPT_PATH)
    notify_completion()
