#!/usr/bin/env python3
"""
parallels_setup.py
Helper script for automating Parallels Desktop + Tools setup checks.
"""

import subprocess
import shutil
from pathlib import Path

LOGS = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace" / "Bubbas_Bitz" / "Logs"
LOGS.mkdir(parents=True, exist_ok=True)

def log(msg: str):
    """Log to console and save to file."""
    print(msg)
    with open(LOGS / "parallels_setup.log", "a") as f:
        f.write(msg + "\n")

def check_parallels():
    """Check if Parallels Desktop is installed."""
    app_path = Path("/Applications/Parallels Desktop.app")
    if app_path.exists():
        log("✅ Parallels Desktop found.")
    else:
        log("❌ Parallels Desktop not found. Please install it from https://www.parallels.com/")

def launch_parallels():
    """Launch Parallels Desktop if available."""
    try:
        subprocess.run(["open", "-a", "Parallels Desktop"], check=True)
        log("🚀 Parallels Desktop launched.")
    except Exception as e:
        log(f"❌ Failed to launch Parallels: {e}")

def check_prlctl():
    """Check if Parallels CLI tools (prlctl) are available."""
    if shutil.which("prlctl"):
        result = subprocess.getoutput("prlctl list")
        log("✅ prlctl is installed. Current VMs:\n" + result)
    else:
        log("⚠️ prlctl not found. Install Parallels Command Line Tools from Parallels menu.")

def main():
    log("=== Parallels Setup Assistant ===")
    check_parallels()
    launch_parallels()
    check_prlctl()
    log("=== Setup Complete ===")

if __name__ == "__main__":
    main()
