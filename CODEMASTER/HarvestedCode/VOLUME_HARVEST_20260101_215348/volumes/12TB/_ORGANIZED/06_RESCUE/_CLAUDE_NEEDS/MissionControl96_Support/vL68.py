#!/usr/bin/env python3
"""
Builds a complete Repair USB for DELL Inspiron 17 7779 2-in-1.
Copies Windows ISO, Dell drivers, firmware, updates, and fleet tools to the USB.
Run on Windows, Mac, or Linux. Specify USB mount point and resource folders.
"""
import shutil, os, sys
from pathlib import Path

# CONFIGURE THESE PATHS
USB_MOUNT = Path(input("Enter USB mount path (e.g., E:/ or /Volumes/CORSAIR): ").strip())
WIN_ISO = Path(input("Path to Windows ISO: ").strip())
DELL_DRIVERS = Path(input("Path to DELL drivers folder: ").strip())
DELL_FIRMWARE = Path(input("Path to DELL firmware folder: ").strip())
WIN_UPDATES = Path(input("Path to Windows updates folder: ").strip())
FLEET_TOOLS = Path(input("Path to fleet tools folder: ").strip())

folders = [
    (WIN_ISO, USB_MOUNT / "Windows_ISO"),
    (DELL_DRIVERS, USB_MOUNT / "DELL_DRIVERS"),
    (DELL_FIRMWARE, USB_MOUNT / "DELL_FIRMWARE"),
    (WIN_UPDATES, USB_MOUNT / "WIN_UPDATES"),
    (FLEET_TOOLS, USB_MOUNT / "FLEET_TOOLS"),
]

def copytree(src, dst):
    if src.is_file():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    else:
        shutil.copytree(src, dst, dirs_exist_ok=True)

print(f"Building Repair USB at {USB_MOUNT}…")
for src, dst in folders:
    if src.exists():
        print(f"Copying {src} → {dst}")
        copytree(src, dst)
    else:
        print(f"⚠️ Source not found: {src}")
print("✅ Repair USB build complete.")
