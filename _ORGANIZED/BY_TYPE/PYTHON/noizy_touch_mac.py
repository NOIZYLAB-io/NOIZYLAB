# NoizyTouch OS - Core Ritual Engine (macOS version)
# Author: Rob + Copilot
# Purpose: Transform Planar touchscreen into a branded ritual interface

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.core.window import Window
import os
import subprocess

# === CONFIG ===
Window.clearcolor = (0, 0, 0, 0)  # Transparent background
Window.fullscreen = 'auto'

RITUALS = {
    "Design": {
        "app": "/Applications/Figma.app",
        "folder": os.path.expanduser("~/Noizy/Rituals/Design"),
        "tone": "/System/Library/Sounds/Glass.aiff"
    },
    "Sound": {
        "app": "/Applications/Logic Pro X.app",
        "folder": os.path.expanduser("~/Noizy/Rituals/Sound"),
        "tone": "/System/Library/Sounds/Pop.aiff"
    },
    "Code": {
        "app": "/Applications/Visual Studio Code.app",
        "folder": os.path.expanduser("~/Noizy/Rituals/Code"),
        "tone": "/System/Library/Sounds/Hero.aiff"
    },
    "Share": {
        "app": "/Applications/OBS.app",
        "folder": os.path.expanduser("~/Noizy/Rituals/Share"),
        "tone": "/System/Library/Sounds/Submarine.aiff"
    },
    "LifeSaviour": {
        "app": os.path.expanduser("~/Noizy/LifeSaverTablet/run_cockpit.sh"),
        "folder": os.path.expanduser("~/Noizy/Rituals/LifeSaviour"),
        "tone": "/System/Library/Sounds/Funk.aiff"
    }
}

# === UTILITIES ===
def play_tone(tone_path):
    subprocess.run(["afplay", tone_path])

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
    ritual = RITUALS[name]
    play_tone(ritual["tone"])
    open_folder(ritual["folder"])
    launch_app(ritual["app"])

# === UI ===
class RitualButton(Button):
    def __init__(self, name, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.text = name
        self.font_size = 32
        self.background_color = (0.2, 0.2, 0.2, 0.8)
        self.color = (1, 1, 1, 1)
        self.size_hint = (0.3, 0.2)
        self.bind(on_press=self.invoke)

    def invoke(self, instance):
        activate_ritual(self.name)

class NoizyTouchApp(App):
    def build(self):
        layout = FloatLayout()
        positions = {
            "Design": (0.05, 0.7),
            "Sound": (0.35, 0.7),
            "Code": (0.65, 0.7),
            "Share": (0.2, 0.4),
            "LifeSaviour": (0.5, 0.4)
        }
        for name, pos in positions.items():
            btn = RitualButton(name, pos_hint={'x': pos[0], 'y': pos[1]})
            layout.add_widget(btn)
        return layout

if __name__ == "__main__":
    NoizyTouchApp().run()
