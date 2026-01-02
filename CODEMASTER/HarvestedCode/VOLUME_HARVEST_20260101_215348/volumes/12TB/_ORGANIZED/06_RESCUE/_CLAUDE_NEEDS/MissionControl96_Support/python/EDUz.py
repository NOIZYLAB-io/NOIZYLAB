#!/usr/bin/env python3
"""
parallels_setup.py
Cha-Cha + Bubba helper to manage Parallels + Windows 11 VM
"""

import subprocess
import shutil

VM_NAME = "Windows 11"
ISO_PATH = "/Users/rsp_ms/Downloads/Win11_Installer.iso"  # update this if needed

def run(cmd):
    try:
        return subprocess.check_output(cmd, text=True).strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"

def ensure_vm():
    # Create VM if missing
    vms = run(["prlctl", "list", "-a"])
    if VM_NAME not in vms:
        print(f"❌ {VM_NAME} not found. Creating...")
        run(["prlctl", "create", VM_NAME, "--ostype", "win-11"])
        run(["prlctl", "set", VM_NAME, "--device-set", "cdrom0", "--connect", "--image", ISO_PATH])
        print(f"✅ VM {VM_NAME} created and ISO attached.")
    else:
        print(f"✅ {VM_NAME} already exists.")

def start_vm():
    print(f"▶️ Starting {VM_NAME}...")
    run(["prlctl", "start", VM_NAME])

def status_vm():
    status = run(["prlctl", "list", "-a"])
    print(f"📋 VM Status:\n{status}")

def main():
    if not shutil.which("prlctl"):
        print("❌ Parallels CLI (prlctl) not found. Install Parallels Desktop first.")
        return
    ensure_vm()
    start_vm()
    status_vm()
    print("👉 Once Windows boots, go to macOS menu: Actions → Install Parallels Tools")

if __name__ == "__main__":
    main()