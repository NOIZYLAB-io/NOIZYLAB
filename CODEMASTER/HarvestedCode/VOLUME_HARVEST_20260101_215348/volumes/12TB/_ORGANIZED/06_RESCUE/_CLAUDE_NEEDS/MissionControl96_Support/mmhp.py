#!/usr/bin/env python3
import json
import os
import shutil
import subprocess
import datetime
from pathlib import Path

# VS Code workspace settings
VSCODE_SETTINGS = {
    "editor.fontFamily": "JetBrains Mono, Fira Mono, Menlo, Monaco, 'Courier New', monospace",
    "editor.fontSize": 14,
    "workbench.colorTheme": "Default Dark+"
}

# Tkinter GUI defaults
TKINTER_DEFAULTS = '''\
import tkinter as tk
root = tk.Tk()
root.option_add("*Font", "JetBrains Mono 14")
root.configure(bg="#222222")
# ...rest of your GUI code...
'''

NOIZYFISH_DIR = str(Path.home() / "Desktop" / "NoizyFish")
BACKUP_DIR = os.path.join(NOIZYFISH_DIR, "backups")
README_PATH = os.path.join(NOIZYFISH_DIR, "README.md")

# 1. Organize files and folders
def organize_workspace():
    folders = ["code", "docs", "media", "archive"]
    for folder in folders:
        path = os.path.join(NOIZYFISH_DIR, folder)
        os.makedirs(path, exist_ok=True)
    for item in os.listdir(NOIZYFISH_DIR):
        src = os.path.join(NOIZYFISH_DIR, item)
        if os.path.isfile(src):
            if item.endswith(".py"):
                shutil.move(src, os.path.join(NOIZYFISH_DIR, "code", item))
            elif item.endswith(".md"):
                shutil.move(src, os.path.join(NOIZYFISH_DIR, "docs", item))
            elif item.endswith(('.mp3', '.wav', '.png', '.jpg')):
                shutil.move(src, os.path.join(NOIZYFISH_DIR, "media", item))
            else:
                shutil.move(src, os.path.join(NOIZYFISH_DIR, "archive", item))

# 2. Universal look and feel (VS Code settings)
def apply_vscode_settings():
    settings_path = os.path.expanduser("~/Library/Application Support/Code/User/settings.json")
    settings = {
        "workbench.sideBar.location": "left",
        "files.autoSave": "afterDelay",
        "window.autoDetectColorScheme": True,
        "window.closeWhenEmpty": True,
        "editor.fontFamily": "Palatino",
        "editor.fontSize": 15,
        "workbench.colorTheme": "Default Dark+"
    }
    with open(settings_path, "w") as f:
        json.dump(settings, f, indent=4)

# 3. Custom startup message (sound)
def play_startup_sound():
    sound_path = os.path.join(NOIZYFISH_DIR, "media", "sarah_output.mp3")
    if os.path.exists(sound_path):
        subprocess.run(["afplay", sound_path])

# 4. Desktop notification
def send_notification(message):
    subprocess.run(["osascript", "-e", f'display notification "{message}" with title "NoizyFish"'])

# 5. Backup automation
def backup_workspace():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(BACKUP_DIR, f"backup_{timestamp}.zip")
    shutil.make_archive(backup_file.replace('.zip', ''), 'zip', NOIZYFISH_DIR)

# 6. Git setup
def setup_git():
    if not os.path.exists(os.path.join(NOIZYFISH_DIR, ".git")):
        subprocess.run(["git", "init", NOIZYFISH_DIR])
        subprocess.run(["git", "-C", NOIZYFISH_DIR, "add", "."])
        subprocess.run(["git", "-C", NOIZYFISH_DIR, "commit", "-m", "Initial commit"])

# 7. Create README/dashboard
def create_readme():
    with open(README_PATH, "w") as f:
        f.write("# NoizyFish Workspace\n\nWelcome to your organized, automated workspace!\n\n- Universal look and feel\n- Auto backups\n- Git version control\n- Custom startup sound\n- Desktop notifications\n")

# Write VS Code settings.json
vscode_dir = Path.home() / "Desktop" / "NoizyFish" / ".vscode"
vscode_dir.mkdir(parents=True, exist_ok=True)
settings_path = vscode_dir / "settings.json"
with open(settings_path, "w") as f:
    json.dump(VSCODE_SETTINGS, f, indent=2)
print(f"VS Code settings written to {settings_path}")

# Write Tkinter defaults example
example_path = Path.home() / "Desktop" / "NoizyFish" / "tkinter_defaults_example.py"
with open(example_path, "w") as f:
    f.write(TKINTER_DEFAULTS)
print(f"Tkinter GUI defaults example written to {example_path}")

if __name__ == "__main__":
    organize_workspace()
    apply_vscode_settings()
    play_startup_sound()
    send_notification("NoizyFish workspace is ready!")
    backup_workspace()
    setup_git()
    create_readme()
    print("NoizyFish workspace setup complete.")
