#!/usr/bin/env python3
import os
from pathlib import Path

ROOT = Path.home() / "Desktop" / "NoizyFish"

broken_files = []
for dirpath, dirnames, filenames in os.walk(ROOT):
    for fname in filenames:
        fpath = Path(dirpath) / fname
        try:
            # Try to open as text to check for code file integrity
            if fpath.suffix in {'.py', '.js', '.ts', '.sh', '.json', '.yaml', '.yml'}:
                with fpath.open("r", encoding="utf-8") as f:
                    f.read()
            else:
                with fpath.open("rb") as f:
                    f.read(1024)  # Just check file is readable
        except Exception as e:
            broken_files.append((str(fpath), str(e)))

if broken_files:
    print("Broken or unreadable files detected:")
    for path, err in broken_files:
        print(f"{path}: {err}")
else:
    print("All files in NoizyFish are readable and appear OK.")

python3 ~/Desktop/NoizyFish/quick_safety_scan.py
