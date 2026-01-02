#!/usr/bin/env python3
"""
move_mov_files.py
Moves all .mov files from /Volumes/JOE to /Volumes/4TB Utility/MOV.
"""
import os
import shutil
from pathlib import Path

SRC_ROOT = Path("/Volumes/JOE")
DEST_ROOT = Path("/Volumes/4TB Utility/MOV")

for dirpath, _, filenames in os.walk(SRC_ROOT):
    for fname in filenames:
        if fname.lower().endswith('.mov'):
            src_path = Path(dirpath) / fname
            dest_path = DEST_ROOT / fname
            try:
                shutil.move(str(src_path), str(dest_path))
                print(f"Moved: {src_path} -> {dest_path}")
            except Exception as e:
                print(f"Failed to move {src_path}: {e}")
