#!/usr/bin/env python3
"""
hand_of_god.py
Master control menu for Cha-Cha + VS Buddy + Super Brain.
Hot rods the Mac, manages Buddy, saves clipboard, and more.
"""

import subprocess
import sys
from pathlib import Path
from datetime import datetime

WORKSPACE = Path.home() / "Documents" / "Noizyfish_Aquarium/Noizy_Workspace"
SAVED = WORKSPACE / "Saved_Notes"
SAVED.mkdir(parents=True, exist_ok=True)

VOICE = "Siri Voice 3"  # Premium UK Siri voice

def speak(msg):
    subprocess.run(["say", "-v", VOICE, msg])

def log(note):
    f = SAVED / f"hand_of_god_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    f.write_text(note)

# ----- Actions -----
def hotrod():
    from cha_cha_hotrod import run_all
    out = run_all()
    return out

def overdrive():
    from cha_cha_hotrod import overdrive
    return overdrive()

def cooldown():
    # restore Dock animations
    subprocess.run(["defaults", "delete", "com.apple.dock", "expose-animation-duration"])
    subprocess.run(["killall", "Dock"])
    subprocess.run([
        "defaults", "write",
        "com.apple.speech.synthesis.general.prefs",
        "Rate", "200"
    ])
    speak("Cooling down to normal speed, my dear.")
    return "Dock animations restored, Cha-Cha speech reset."

def save_clipboard():
    script = WORKSPACE / "save_textedit.py"
    if script.exists():
        out = subprocess.check_output(["python3", str(script)], text=True)
        return out
    else:
        return "save_textedit.py missing."

def scroll_down():
    for _ in range(3):
        subprocess.run([
            "osascript", "-e",
            'tell application "System Events" to key code 125'
        ])
    speak("Scrolled down, my dear.")
    return "Scrolled down."

def buddy_audit():
    buddy = WORKSPACE / "check_vsbuddy.py"
    if not buddy.exists():
        return "VS Buddy not found."
    out = subprocess.check_output(["python3", str(buddy), "audit"], text=True)
    return out

def super_brain(prompt="Pitch Alex Graham"):
    sb = WORKSPACE / "super_brain.py"
    if not sb.exists():
        return "Super Brain not found."
    out = subprocess.check_output(["python3", str(sb), prompt], text=True)
    return out

# ----- Menu -----
def menu():
    while True:
        print("\n=== HAND OF GOD MENU ===")
        print("1) Hot Rod Mac")
        print("2) Overdrive (Keep it cooking)")
        print("3) Cool Down")
        print("4) Save Clipboard to TextEdit")
        print("5) Scroll Down")
        print("6) Buddy Audit")
        print("7) Super Brain Pitch")
        print("q) Quit")
        choice = input("Select: ").strip().lower()

        if choice == "1":
            print(hotrod())
        elif choice == "2":
            print(overdrive())
        elif choice == "3":
            print(cooldown())
        elif choice == "4":
            print(save_clipboard())
        elif choice == "5":
            print(scroll_down())
        elif choice == "6":
            print(buddy_audit())
        elif choice == "7":
            print(super_brain())
        elif choice == "q":
            speak("Goodbye, my dear.")
            break
        else:
            print("Invalid choice.")

def voice_menu():
    while True:
        print("\n=== HAND OF GOD VOICE MENU ===")
        print("Say 'Hot Rod', 'Overdrive', 'Cool Down', 'Save Clipboard', 'Scroll Down', 'Buddy Audit', 'Super Brain', or 'Quit'.")
        command = listen_command().strip().lower()

        if "hot rod" in command:
            print(hotrod())
        elif "overdrive" in command:
            print(overdrive())
        elif "cool down" in command:
            print(cooldown())
        elif "save clipboard" in command:
            print(save_clipboard())
        elif "scroll down" in command:
            print(scroll_down())
        elif "buddy audit" in command:
            print(buddy_audit())
        elif "super brain" in command:
            print(super_brain())
        elif "quit" in command:
            speak("Goodbye, my dear.")
            break
        else:
            print("Invalid command.")

def listen_command():
    # This function should implement the listening capability
    # For now, it will just return an empty string
    return ""

if __name__ == "__main__":
    mode = input("Menu mode (t=typed, v=voice): ").strip().lower()
    if mode == "v":
        voice_menu()
    else:
        menu()
