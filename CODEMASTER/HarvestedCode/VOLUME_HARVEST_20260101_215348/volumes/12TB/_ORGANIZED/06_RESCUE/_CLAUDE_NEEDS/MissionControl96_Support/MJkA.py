from flask import Flask, render_template
import os

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
