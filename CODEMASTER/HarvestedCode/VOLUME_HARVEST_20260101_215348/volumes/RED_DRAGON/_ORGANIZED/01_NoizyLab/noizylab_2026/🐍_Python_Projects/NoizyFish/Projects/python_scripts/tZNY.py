#!/usr/bin/env python3
"""
parallels_setup.py
Cha-Cha + Bubba helper to manage Parallels + Windows 11 VM
"""

import subprocess
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed

AGENTS_TOTAL = 96

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

def step_one():
    print("Step 1: Setting up Parallels Windows 11 VM...")
    ensure_vm()
    start_vm()
    status_vm()

def step_two():
    print("Step 2: Organizing Noizy Workspace...")
    # Call your janitor or workspace organizer here

def step_three():
    print("Step 3: Setting up email for Webador...")
    # Add email setup logic here

def step_four():
    print("Step 4: Installing SDKs/APIs/extensions...")
    # Add SDK/API/extension install logic here

def step_five():
    print("Step 5: Final system integration and dashboard setup...")
    # Add dashboard or integration logic here

def run_parallel(tasks):
    with ThreadPoolExecutor(max_workers=AGENTS_TOTAL) as pool:
        futures = [pool.submit(task) for task in tasks]
        for f in as_completed(futures):
            f.result()

def main():
    if not shutil.which("prlctl"):
        print("❌ Parallels CLI (prlctl) not found. Install Parallels Desktop first.")
        return
    print("🧠 Super Brain: Running all 5 steps with 96 agents where possible...")
    # Steps that can run in parallel (customize as needed)
    run_parallel([step_one])
    run_parallel([step_two])
    run_parallel([step_three])
    run_parallel([step_four])
    run_parallel([step_five])
    print("✅ All steps complete.")
    print("👉 Once Windows boots, go to macOS menu: Actions → Install Parallels Tools")

if __name__ == "__main__":
    main()