#!/usr/bin/env python3
"""Auto-run the ultimate organizer"""
import subprocess
import sys
import os
from pathlib import Path

os.chdir(Path(__file__).parent)

print("🎵 AUTO-LAUNCHING ULTIMATE ORGANIZER...")
print("="*80 + "\n")

try:
    result = subprocess.run(
        [sys.executable, "ULTIMATE_ORGANIZER.py"],
        capture_output=False,
        text=True
    )
    sys.exit(result.returncode)
except Exception as e:
    print(f"❌ Subprocess failed: {e}")
    print("\nTrying direct execution...\n")
    try:
        with open("ULTIMATE_ORGANIZER.py") as f:
            code = f.read()
        exec(code)
    except Exception as e2:
        print(f"❌ Direct execution failed: {e2}")
        import traceback
        traceback.print_exc()

