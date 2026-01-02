#!/usr/bin/env python3
"""
cha_cha_to_bubba.py
Bridge between Cha-Cha (listener/voice) and Bubba (VS Buddy core).
"""

import subprocess
import sys
from pathlib import Path

WORKSPACE = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace"
VOICE = "Siri Voice 3"  # Confirm with `say -v "?"`

def speak(msg):
    subprocess.run(["say", "-v", VOICE, msg], check=False)

def run_bubba(command: str):
    """
    Bubba = formerly VS Buddy. Expects a Python script like bubba_core.py
    in the same workspace that can accept a string command and print results.
    """
    bubba = WORKSPACE / "bubba_core.py"
    if not bubba.exists():
        return f"Bubba core not found at {bubba}"

    try:
        result = subprocess.check_output(
            ["python3", str(bubba), command],
            text=True
        )
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"Bubba error: {e.output}"

def main():
    if len(sys.argv) < 2:
        speak("What shall I tell Bubba, my dear?")
        return
    cmd = " ".join(sys.argv[1:])
    speak(f"Passing to Bubba: {cmd}")
    result = run_bubba(cmd)
    print("Bubba says:", result)
    speak(f"Bubba says: {result}")

if __name__ == "__main__":
    main()
