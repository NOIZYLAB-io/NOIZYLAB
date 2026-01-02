#!/usr/bin/env python3
"""
NoizyAuto Assistant v1.0 — TEST VERSION
- Bypasses Bluetooth check for demonstration
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
LOGFILE = LOGS / f"noizyauto_test_log_{TIMESTAMP}.log"

def log(msg):
    with open(LOGFILE, "a") as f:
        f.write(msg + "\n")
    print(msg)

# === 1. Detect Bluetooth Connection (TEST VERSION) ===
def detect_honda_bt():
    log("🧪 TEST MODE: Simulating Honda CR-V Bluetooth connection")
    return True

# === 2. Symbolic Hotspot Activation ===
def activate_hotspot():
    log("🔮 Symbolic Hotspot Activation: Please confirm manually on iPhone.")

# === 3. Launch Ritual Apps ===
def launch_apps():
    log("🚀 Launching cockpit apps...")
    try:
        subprocess.run(["open", "-a", "Maps"], check=False)
        subprocess.run(["open", "-a", "Music"], check=False)
        log("✔ Apps launched successfully")
    except Exception as e:
        log(f"⚠ App launch failed: {e}")

# === 4. Cloud Sync Ritual ===
def cloud_sync():
    log("☁️ Syncing Archive to OneDrive...")
    try:
        SYNC_SRC = ARCHIVE
        SYNC_DST = Path.home() / "OneDrive" / "MythicStack_Archive"
        SYNC_DST.mkdir(parents=True, exist_ok=True)
        
        # Create test file if archive is empty
        if not any(SYNC_SRC.iterdir()):
            test_file = SYNC_SRC / "test_sync.txt"
            test_file.write_text("Test sync file created by NoizyAuto")
        
        result = subprocess.run(["rsync", "-av", "--exclude", "*.tmp", str(SYNC_SRC) + "/", str(SYNC_DST)], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            log("✔ Cloud sync complete.")
        else:
            log(f"⚠ Cloud sync had issues: {result.stderr}")
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
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, 'b-', linewidth=2)
        plt.title("NoizyAuto Sin Wave Diagnostic")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plot_path = LOGS / "sin_wave_plot.png"
        plt.savefig(plot_path, dpi=150, bbox_inches='tight')
        plt.close()
        log(f"✔ Plot saved: {plot_path}")

        # Image
        img = Image.new("RGB", (400, 200), color=(25, 25, 112))  # Dark blue
        draw = ImageDraw.Draw(img)
        draw.text((50, 80), "NoizyAuto Assistant", fill=(255, 255, 255))
        draw.text((50, 110), f"Test Run: {TIMESTAMP}", fill=(200, 200, 200))
        img_path = LOGS / "noizyauto_image.png"
        img.save(img_path)
        log(f"✔ Image capsule saved: {img_path}")
    except Exception as e:
        log(f"⚠ Graphics diagnostics failed: {e}")

# === 6. Log Ritual Capsule ===
def log_capsule():
    capsule = DRIVELOGS / f"INFO_{TIMESTAMP}.txt"
    with open(capsule, "w") as f:
        f.write(f"""NoizyAuto Ritual Test Run
Timestamp: {TIMESTAMP}
Vehicle: Honda CR-V (Simulated)
Hotspot: Activated
Apps: Maps, Music
Sync: OneDrive
Graphics: Generated
Status: Complete
""")
    log(f"📄 Capsule saved: {capsule}")

# === Main Ritual ===
def main():
    log("=== NoizyAuto Assistant TEST Ritual Start ===")
    if detect_honda_bt():
        activate_hotspot()
        launch_apps()
        cloud_sync()
        graphics_diagnostics()
        log_capsule()
        log(f"📁 Check logs at: {LOGS}")
        log(f"📁 Check capsules at: {DRIVELOGS}")
    else:
        log("❌ Ritual aborted: Honda CR-V not detected.")
    log("=== TEST Ritual Complete ===")

if __name__ == "__main__":
    main()