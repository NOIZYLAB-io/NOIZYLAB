#!/usr/bin/env python3
"""
Super Brain - Parallels Desktop Setup Orchestrator
Drives Bubba to configure Parallels Desktop + Tools for Noizyfish projects.
"""

import subprocess
from pathlib import Path

PARALLELS_APP = Path("/Applications/Parallels Desktop.app")

def check_parallels():
    if not PARALLELS_APP.exists():
        return "❌ Parallels Desktop not installed. Please download the .dmg."
    return "✅ Parallels Desktop found."

def create_vm(name="Win11_Noizy", cpu=4, ram=8192, disk=100000):
    try:
        result = subprocess.check_output([
            "prlctl", "create", name, "--distribution", "win-11"
        ], text=True)
        return f"VM created: {result}"
    except subprocess.CalledProcessError as e:
        return f"Error creating VM: {e.output.strip()}"
    except FileNotFoundError:
        return "Error: prlctl command not found. Ensure Parallels Desktop is installed."

def install_tools(name="Win11_Noizy"):
    try:
        result = subprocess.check_output(["prlctl", "installtools", name], text=True)
        return f"Parallels Tools installation triggered: {result}"
    except subprocess.CalledProcessError as e:
        return f"Error installing tools: {e.output.strip()}"
    except FileNotFoundError:
        return "Error: prlctl command not found. Ensure Parallels Desktop is installed."

def mount_workspace(name="Win11_Noizy"):
    workspace = str(Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace")
    return f"Mounting {workspace} into {name} shared folders (manual confirm in Parallels prefs)."

if __name__ == "__main__":
    print(check_parallels())
    print(create_vm())
    print(install_tools())
    print(mount_workspace())