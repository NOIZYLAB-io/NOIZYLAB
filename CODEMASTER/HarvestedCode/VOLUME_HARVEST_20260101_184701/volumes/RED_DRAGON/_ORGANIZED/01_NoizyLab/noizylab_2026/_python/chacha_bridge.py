#!/usr/bin/env python3
"""
chacha_bridge.py
Lets Cha-Cha (voice) talk with VS Buddy (scripts).
Wraps Buddy commands and reads results aloud.
"""

import subprocess
import os

VOICE = "Siri Voice 3"  # elegant British female Siri premium voice

def speak(text: str):
    subprocess.run(["say", "-v", VOICE, text])

def run_vsbuddy(command: str):
    """
    Runs VS Buddy with a command string, speaks summary.
    """
    workspace = os.path.expanduser("~/Documents/Noizyfish_Aquarium/Noizy_Workspace")
    buddy = os.path.join(workspace, "check_vsbuddy.py")

    if not os.path.exists(buddy):
        speak("VS Buddy script not found, my dear.")
        return

    try:
        result = subprocess.check_output(["python3", buddy, command], text=True)
        print("Buddy said:\n", result)
        # Speak a shortened summary
        summary = result.splitlines()[0] if result else "No output."
        speak(f"Buddy reports: {summary}")
    except subprocess.CalledProcessError as e:
        speak("Buddy encountered an error, my dear.")
        print("Buddy error:", e.output)

if __name__ == "__main__":
    # Example: Cha-Cha asks Buddy to audit
    run_vsbuddy("audit")
