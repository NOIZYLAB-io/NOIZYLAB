#!/usr/bin/env python3
"""
Bubba's Windows 11 Parallels Setup & Checklist
Automates Parallels VM creation and guides user through installation steps.
"""

import subprocess
from pathlib import Path
from datetime import datetime

# Config
VM_NAME = "Windows 11"
ISO_PATH = "/Users/rsp_ms/Downloads/Win11_Installer.iso"  # <-- Update this path!
LOGS = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace" / "Bubbas_Bitz" / "Logs"
LOGS.mkdir(parents=True, exist_ok=True)

steps = [
    "Boot VM → Windows logo should appear.",
    "Language, Time, Keyboard → Select and click Next → Install Now.",
    "Product Key → Enter or click 'I don’t have a product key'. Choose Windows 11 Pro.",
    "License Agreement → Accept and click Next.",
    "Installation Type → Choose Custom: Install Windows only (advanced).",
    "Drive Selection → Highlight virtual drive, click Next.",
    "Wait for installation (reboots may happen automatically).",
    "Region & Keyboard → Pick your region and layout.",
    "Device Name → Give your VM a name (e.g. Noizy-Win11).",
    "Account Setup → Sign in with Microsoft or choose Offline account.",
    "Privacy Settings → Adjust and continue.",
    "Windows 11 desktop loads 🎉.",
    "Parallels Tools → macOS menu bar: Actions → Install Parallels Tools.",
    "Run Parallels Tools installer inside Windows, reboot when finished."
]

def run(cmd):
    try:
        return subprocess.check_output(cmd, text=True, stderr=subprocess.STDOUT).strip()
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e.output}")
        return None

def ensure_vm():
    vms = run(["prlctl", "list", "-a"])
    if vms and VM_NAME not in vms:
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

def run_checklist():
    log_file = LOGS / f"win11_install_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    print("=== Bubba's Windows 11 Installation Checklist ===\n")

    for i, step in enumerate(steps, 1):
        input(f"[{i}/{len(steps)}] {step}\nPress Enter when done → ")
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().strftime('%H:%M:%S')}] Step {i}: {step} ✅\n")

    print("\n✅ All steps complete! Windows 11 and Parallels Tools should be ready.")
    print(f"📝 Log saved at: {log_file}")

def install_windows_software():
    print("💡 To automate Windows software installs, use Chocolatey:")
    print("Run this in Windows PowerShell:")
    print('Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString("https://community.chocolatey.org/install.ps1"))')
    print("Then install apps, e.g.: choco install vscode python git -y")

def install_parallels_tools():
    import subprocess
    subprocess.run([
        "osascript", "-e",
        'tell application "Parallels Desktop" to activate',
        "-e",
        'tell application "System Events" to keystroke "t" using {command down, shift down}'
    ])
    print("🔧 Parallels Tools installer triggered (check Windows VM).")

def workspace_health_check(workspace_path):
    from collections import defaultdict
    import hashlib
    workspace = Path(workspace_path)
    seen = defaultdict(list)
    for file in workspace.rglob("*"):
        if file.is_file():
            h = hashlib.sha256(file.read_bytes()).hexdigest()
            seen[h].append(file)
    for files in seen.values():
        if len(files) > 1:
            print(f"Duplicate files: {files}")

def setup_email_webador(email, password):
    print(f"Automating email setup for Webador: {email}")
    # You can use IMAP/SMTP libraries or Selenium for web automation
    # Example: Use smtplib for sending test email
    import smtplib
    server = smtplib.SMTP('smtp.webador.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, "Subject: Test\n\nHello from Bubba!")
    server.quit()
    print("✅ Test email sent.")

if __name__ == "__main__":
    print("🔄 Checking Parallels VM status...")
    ensure_vm()
    start_vm()
    status_vm()
    print("\n🚦 Proceed with Windows 11 installation in Parallels Desktop.")
    run_checklist()
    install_windows_software()
    install_parallels_tools()