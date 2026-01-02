#!/usr/bin/env python3
"""
Nano File Creator with Bubba tracking.
Lets you pick a default folder, creates an empty file there,
opens Nano, and logs the path for Bubba to track.
"""

import subprocess, datetime
from pathlib import Path

WS   = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace"
DOCS = Path.home() / "Documents"
DESK = Path.home() / "Desktop"
LOGS = WS / "Saved_Notes"
LOGS.mkdir(parents=True, exist_ok=True)

def menu():
    print("\nWhere do you want to create this file?")
    print("1. Noizy Workspace")
    print("2. Documents")
    print("3. Desktop")
    print("4. Custom path")
    choice = input("Choose [1-4]: ").strip()
    return choice

def get_path(choice):
    if choice == "1":
        folder = WS
    elif choice == "2":
        folder = DOCS
    elif choice == "3":
        folder = DESK
    elif choice == "4":
        return Path(input("Enter full custom path: ").strip()).expanduser()
    else:
        print("Invalid choice, defaulting to Workspace.")
        folder = WS

    fname = input("Enter file name (example: bubba_test.py): ").strip()
    return folder / fname

def log_action(path):
    log_file = LOGS / "nano_file_log.txt"
    with open(log_file, "a") as f:
        f.write(f"[{datetime.datetime.now()}] Created {path}\n")

def main():
    choice = menu()
    path = get_path(choice)
    print(f"Opening Nano for: {path}")
    subprocess.run(["nano", str(path)])
    log_action(path)

if __name__ == "__main__":
    main()
