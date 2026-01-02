#!/usr/bin/env python3
"""
NoizyGenie Graphics Diagnostic Ritual
- Checks macOS display info
- Verifies Python rendering stack (matplotlib, PIL)
- Tests image and plot generation
- Logs results to Mythic Stack
"""

import os, sys, subprocess, time
from pathlib import Path

ROOT = Path(os.environ.get("MYTHIC_STACK_ROOT", Path.home() / "MythicStack")).resolve()
LOGS = ROOT / "Logs"
LOGS.mkdir(parents=True, exist_ok=True)
LOGFILE = LOGS / f"graphics_diagnostic_{int(time.time())}.log"

def log(msg):
    with open(LOGFILE, "a") as f:
        f.write(msg + "\n")
    print(msg)

def check_display_info():
    log("=== Display Info ===")
    if sys.platform == "darwin":
        try:
            output = subprocess.check_output(["system_profiler", "SPDisplaysDataType"]).decode()
            log(output)
        except Exception as e:
            log(f"⚠ Could not fetch display info: {e}")
    else:
        log("⚠ Display info check is macOS-specific.")

def test_matplotlib():
    log("\n=== Matplotlib Plot Test ===")
    try:
        import matplotlib.pyplot as plt
        import numpy as np

        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        plt.plot(x, y)
        plt.title("Graphics Diagnostic: Sin Wave")
        plt.xlabel("Time")
        plt.ylabel("Amplitude")
        plt.grid(True)
        plt.savefig(LOGS / "sin_wave_plot.png")
        plt.close()
        log("✔ Matplotlib plot saved: sin_wave_plot.png")
    except Exception as e:
        log(f"⚠ Matplotlib test failed: {e}")

def test_pillow():
    log("\n=== PIL Image Test ===")
    try:
        from PIL import Image, ImageDraw

        img = Image.new("RGB", (400, 200), color="black")
        draw = ImageDraw.Draw(img)
        draw.text((50, 80), "NoizyGenie Mode", fill="white")
        img.save(LOGS / "noizygenie_image.png")
        log("✔ PIL image saved: noizygenie_image.png")
    except Exception as e:
        log(f"⚠ PIL image test failed: {e}")

def check_packages():
    log("\n=== Python Package Check ===")
    packages = ["matplotlib", "numpy", "Pillow", "opencv-python"]
    for pkg in packages:
        try:
            __import__(pkg.replace("-", "_"))
            log(f"✔ {pkg} installed")
        except ImportError:
            log(f"⚠ {pkg} missing")

def main():
    log("=== NoizyGenie Graphics Diagnostic Start ===")
    check_display_info()
    check_packages()
    test_matplotlib()
    test_pillow()
    log("=== Complete ===")
    log(f"Log written to {LOGFILE}")

if __name__ == "__main__":
    main()
