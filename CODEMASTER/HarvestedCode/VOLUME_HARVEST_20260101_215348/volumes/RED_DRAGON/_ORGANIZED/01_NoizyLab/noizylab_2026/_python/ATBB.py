#!/usr/bin/env python3
"""
cha_cha_hotrod.py
Cha-Cha’s safe performance tune-up for macOS.
"""

import subprocess
from pathlib import Path
from datetime import datetime

WORKSPACE = Path.home() / "Documents" / "Noizyfish_Aquarium/Noizy_Workspace"
SAVED = WORKSPACE / "Saved_Notes"
SAVED.mkdir(parents=True, exist_ok=True)
VOICE = "Siri Voice 3"

def speak(msg):
    subprocess.run(["say", "-v", VOICE, msg])

def log(note):
    f = SAVED / f"hotrod_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    f.write_text(note)

def tune_dock():
    subprocess.run(["defaults", "write", "com.apple.dock", "expose-animation-duration", "-float", "0.1"])
    subprocess.run(["killall", "Dock"])
    return "Dock & Mission Control animations sped up."

def reset_coreaudio():
    subprocess.run(["sudo", "pkill", "-9", "coreaudiod"])
    return "CoreAudio restarted."

def flush_caches():
    subprocess.run(["sudo", "purge"])
    return "Memory caches flushed."

def run_all():
    notes = []
    notes.append(tune_dock())
    notes.append(reset_coreaudio())
    notes.append(flush_caches())
    note = "\n".join(notes)
    log(note)
    speak("Your Mac is hot-rodded, my dear. Everything is snappier now.")
    return note

if __name__ == "__main__":
    print(run_all())
