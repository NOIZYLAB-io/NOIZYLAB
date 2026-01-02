from flask import Flask, render_template
import os
import subprocess

app = Flask(__name__)

PLANAR_RESOLUTION = "1920x1080"

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

def activate_ritual(name):
    print(f"🔮 Activating {name} Ritual...")
    play_chime()
    open_folder(RITUAL_FOLDERS[name])
    launch_app(RITUAL_APPS[name])

def simulate_touch_gesture(gesture):
    gestures = {
        "3-finger-swipe-up": lambda: activate_ritual("Design"),
        "2-finger-tap": lambda: activate_ritual("Sound"),
        "5-finger-hold": lambda: activate_ritual("LifeSaviour")
    }
    if gesture in gestures:
        gestures[gesture]()
    else:
        print("Unknown gesture")

def voice_command(command):
    commands = {
        "activate design mode": lambda: activate_ritual("Design"),
        "begin share ritual": lambda: activate_ritual("Share"),
        "activate lifesaviour": lambda: activate_ritual("LifeSaviour")
    }
    cmd = command.lower()
    if cmd in commands:
        commands[cmd]()
    else:
        print("Unknown voice command")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/creative")
def creative():
    return "Creative Mode Ritual Triggered"

@app.route("/emotech")
def emotech():
    return "Emotional Tech Ritual Triggered"

@app.route("/emergency")
def emergency():
    return "Emergency Mode Ritual Triggered"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
