#!/usr/bin/env python3
"""
RSP Lift-Off Focus Launcher — Parallels, Windows 10, Planar
Author: RSP
Purpose: Automate launch of Parallels VM (Windows 10) and Planar Template workspace.
"""

import os, subprocess, datetime, json
from pathlib import Path

PARALLELS_APP = "/Applications/Parallels Desktop.app"
VM_NAME = "NoizyWin10"
PLANAR_TEMPLATE = str(Path.home() / "RSP_Planar_Template")
LOG_PATH = str(Path.home() / "RSP/LiftOffLogs/focus_sessions.jsonl")

# Log session start
session = {
    "timestamp": datetime.datetime.now().isoformat(),
    "project": "Parallels + Windows 10 + Planar",
    "action": "start"
}
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
with open(LOG_PATH, "a") as f:
    f.write(json.dumps(session) + "\n")

print("Launching Parallels Desktop…")
subprocess.Popen(["open", PARALLELS_APP])

print("Starting Windows 10 VM…")
subprocess.run(["prlctl", "start", VM_NAME])

print("Opening Planar Template workspace…")
subprocess.Popen(["open", PLANAR_TEMPLATE])

print("Focus session started: Parallels, Windows 10, and Planar Template ready!")
