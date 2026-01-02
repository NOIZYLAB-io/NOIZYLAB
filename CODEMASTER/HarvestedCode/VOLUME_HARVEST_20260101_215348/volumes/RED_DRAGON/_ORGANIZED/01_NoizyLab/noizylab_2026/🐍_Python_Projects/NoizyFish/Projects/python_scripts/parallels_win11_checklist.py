#!/usr/bin/env python3
"""
Bubba's Windows 11 Installation Checklist
Guides the user through Parallels Desktop setup step-by-step.
"""

from pathlib import Path
from datetime import datetime

# Where Bubba will keep logs
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

def run_checklist():
    log_file = LOGS / f"win11_install_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    print("=== Bubba's Windows 11 Installation Checklist ===\n")

    for i, step in enumerate(steps, 1):
        input(f"[{i}/{len(steps)}] {step}\nPress Enter when done → ")
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"[{datetime.now().strftime('%H:%M:%S')}] Step {i}: {step} ✅\n")

    print("\n✅ All steps complete! Windows 11 and Parallels Tools should be ready.")
    print(f"📝 Log saved at: {log_file}")

if __name__ == "__main__":
    run_checklist()
