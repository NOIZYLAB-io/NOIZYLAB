#!/usr/bin/env python3
"""
RSP Lift-Off Focus Launcher
Author: RSP
Purpose: Focus on one project at a time, automate workspace setup, and log session.
"""

import os, sys, json, datetime, subprocess
from pathlib import Path

PROJECTS = {
    "NoizyWind Ritual Pack": str(Path.home() / "GitHub/noizywind-ritual-pack"),
    "FishMusicVault": str(Path.home() / "FishMusicVault"),
    "RSP Planar Template": str(Path.home() / "RSP_Planar_Template"),
    "RSP Orchestrator": str(Path.home() / "RSP/Scripts/RSP_Orchestrator.py")
}
LOG_PATH = str(Path.home() / "RSP/LiftOffLogs/focus_sessions.jsonl")

# Prompt user to select a project
print("Select a project to focus on:")
for i, name in enumerate(PROJECTS.keys(), 1):
    print(f"  {i}. {name}")
choice = input("Enter number: ").strip()
try:
    idx = int(choice) - 1
    project_name = list(PROJECTS.keys())[idx]
    project_path = PROJECTS[project_name]
except:
    print("Invalid selection."); sys.exit(1)

# Log session start
session = {
    "timestamp": datetime.datetime.now().isoformat(),
    "project": project_name,
    "action": "start"
}
os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
with open(LOG_PATH, "a") as f:
    f.write(json.dumps(session) + "\n")

print(f"Launching workspace for: {project_name}")

# Open folder or launch script
if project_path.endswith(".py"):
    subprocess.Popen(["python3", project_path])
else:
    subprocess.Popen(["open", project_path])

print("Focus session started. Minimize distractions and work on your chosen project!")
