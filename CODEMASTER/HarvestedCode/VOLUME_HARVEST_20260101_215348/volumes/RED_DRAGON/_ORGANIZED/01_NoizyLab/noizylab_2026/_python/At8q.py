#!/usr/bin/env python3
"""
bootstrap_voice.py
One-stop launcher for voice_to_osc.py:
 - Ensures a virtual environment exists in ~/noizyvenv
 - Installs required packages if missing
 - Runs voice_to_osc.py with forwarded args
"""

import os
import sys
import subprocess
import venv
from pathlib import Path

VENV_PATH = Path.home() / "noizyvenv"
REQUIREMENTS = ["speechrecognition", "sounddevice", "numpy"]


def ensure_venv():
    if not VENV_PATH.exists():
        print(f"[NOIZY] Creating virtual environment at {VENV_PATH}")
        venv.create(VENV_PATH, with_pip=True)
    else:
        print(f"[NOIZY] Using existing virtual environment at {VENV_PATH}")


def run_pip_install():
    pip_path = VENV_PATH / "bin" / "pip"
    for pkg in REQUIREMENTS:
        print(f"[NOIZY] Installing {pkg} …")
        subprocess.check_call([str(pip_path), "install", "--upgrade", pkg])


def run_script(args):
    python_path = VENV_PATH / "bin" / "python"
    script_path = Path(__file__).parent / "voice_to_osc.py"

    if not script_path.exists():
        sys.exit(f"[ERROR] Could not find {script_path}. Place voice_to_osc.py next to bootstrap_voice.py")

    cmd = [str(python_path), str(script_path)] + args
    print(f"[NOIZY] Running: {' '.join(cmd)}")
    os.execv(str(python_path), cmd)


def main():
    ensure_venv()
    run_pip_install()
    run_script(sys.argv[1:])


if __name__ == "__main__":
    main()
