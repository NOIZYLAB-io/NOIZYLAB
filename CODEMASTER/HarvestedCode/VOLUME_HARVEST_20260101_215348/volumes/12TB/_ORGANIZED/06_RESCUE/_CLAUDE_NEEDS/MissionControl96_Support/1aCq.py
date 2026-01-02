#!/usr/bin/env python3
"""
NoizyAuto Assistant v1.0 — Unified Ritual Script
- Detects Bluetooth connection to Honda CR-V
- Activates hotspot (symbolic trigger)
- Launches cockpit apps (symbolic)
- Syncs archive to OneDrive
- Logs ritual
- Runs graphics diagnostics
"""

import os, subprocess, time, sys
from pathlib import Path

# === Ritual Anchors ===
ROOT = Path(os.environ.get("MYTHIC_STACK_ROOT", Path.home() / "MythicStack")).resolve()
LOGS = ROOT / "Logs"
ARCHIVE = ROOT / "Archive"
DRIVELOGS = ARCHIVE / "Projects" / "LifeSaviour_Pod" / "DriveLogs"
LOGS.mkdir(parents=True, exist_ok=True)
DRIVELOGS.mkdir(parents=True, exist_ok=True)
TIMESTAMP = time.strftime("%Y%m%d_%H%M%S")
LOGFILE = LOGS / f"noizyauto_log_{TIMESTAMP}.log"

def log(msg):
    with open(LOGFILE, "a") as f:
        f.write(msg + "\n")
    print(msg)

# === 1. Detect Bluetooth Connection ===
def detect_honda_bt():
    try:
        output = subprocess.check_output(["system_profiler", "SPBluetoothDataType"]).decode()
        if "Honda CR-V" in output:
            log("✔ Honda CR-V Bluetooth detected.")
            return True
        else:
            log("⚠ Honda CR-V not connected.")
            return False
    except Exception as e:
        log(f"⚠ Bluetooth check failed: {e}")
        return False

# === 2. Symbolic Hotspot Activation ===
def activate_hotspot():
    log("🔮 Symbolic Hotspot Activation: Please confirm manually on iPhone.")

# === 3. Launch Ritual Apps ===
def launch_apps():
    log("🚀 Launching cockpit apps...")
    subprocess.run(["open", "-a", "Maps"])
    subprocess.run(["open", "-a", "Music"])

# === 4. Cloud Sync Ritual ===
def cloud_sync():
    log("☁️ Syncing Archive to OneDrive...")
    try:
        SYNC_SRC = ARCHIVE
        SYNC_DST = Path.home() / "OneDrive" / "MythicStack_Archive"
        subprocess.run(["rsync", "-av", "--exclude", "*.tmp", str(SYNC_SRC), str(SYNC_DST)])
        log("✔ Cloud sync complete.")
    except Exception as e:
        log(f"⚠ Cloud sync failed: {e}")

# === 5. Graphics Diagnostics ===
def graphics_diagnostics():
    log("🧪 Running graphics diagnostics...")
    try:
        import matplotlib.pyplot as plt
        import numpy as np
        from PIL import Image, ImageDraw

        # Plot
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        plt.plot(x, y)
        plt.title("NoizyAuto Sin Wave")
        plt.savefig(LOGS / "sin_wave_plot.png")
        plt.close()
        log("✔ Plot saved.")

        # Image
        img = Image.new("RGB", (400, 200), color="black")
        draw = ImageDraw.Draw(img)
        draw.text((50, 80), "NoizyAuto Assistant", fill="white")
        img.save(LOGS / "noizyauto_image.png")
        log("✔ Image capsule saved.")
    except Exception as e:
        log(f"⚠ Graphics diagnostics failed: {e}")

# === 6. Log Ritual Capsule ===
def log_capsule():
    capsule = DRIVELOGS / f"INFO_{TIMESTAMP}.txt"
    with open(capsule, "w") as f:
        f.write(f"NoizyAuto Ritual\nTimestamp: {TIMESTAMP}\nVehicle: Honda CR-V\nHotspot: Activated\nApps: Maps, Music\nSync: OneDrive\n")
    log(f"📄 Capsule saved: {capsule.name}")

# === Main Ritual ===
def main():
    log("=== NoizyAuto Assistant Ritual Start ===")
    if detect_honda_bt():
        activate_hotspot()
        launch_apps()
        cloud_sync()
        graphics_diagnostics()
        log_capsule()
    else:
        log("❌ Ritual aborted: Honda CR-V not detected.")
    log("=== Ritual Complete ===")

if __name__ == "__main__":
    main()