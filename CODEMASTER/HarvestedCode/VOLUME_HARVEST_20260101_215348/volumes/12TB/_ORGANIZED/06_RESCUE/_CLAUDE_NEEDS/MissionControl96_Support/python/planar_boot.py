import os
import subprocess
import time

# === CONFIG ===
RITUAL_FOLDERS = {
    "Design": os.path.expanduser("~/Noizy/Rituals/Design"),
    "Sound": os.path.expanduser("~/Noizy/Rituals/Sound"),
    "Code": os.path.expanduser("~/Noizy/Rituals/Code"),
    "Share": os.path.expanduser("~/Noizy/Rituals/Share"),
    "LifeSaviour": os.path.expanduser("~/Noizy/Rituals/LifeSaviour")
}
RITUAL_APPS = {
    "Design": "/Applications/Figma.app",
    "Sound": "/Applications/Logic Pro X.app",
    "Code": "/Applications/Visual Studio Code.app",
    "Share": "/Applications/OBS.app",
    "LifeSaviour": os.path.expanduser("~/Noizy/LifeSaverTablet/run_cockpit.sh")
}

# === UTILITIES ===
def play_chime():
    subprocess.run(["afplay", "/System/Library/Sounds/Glass.aiff"])

def launch_app(path):
    if os.path.exists(path):
        subprocess.Popen(["open", path])
    else:
        print(f"App not found: {path}")

def open_folder(path):
    if os.path.exists(path):
        subprocess.Popen(["open", path])
    else:
        print(f"Folder not found: {path}")

# === RITUALS ===
def activate_ritual(name):
    print(f"Activating {name} Ritual...")
    play_chime()
    open_folder(RITUAL_FOLDERS[name])
    launch_app(RITUAL_APPS[name])

# === MAIN BOOT SEQUENCE ===
def planar_boot_sequence():
    print("🧭 Planar Slab Awakening...")
    play_chime()
    time.sleep(1)
    activate_ritual("Code")  # Default boot ritual

if __name__ == "__main__":
    planar_boot_sequence()
