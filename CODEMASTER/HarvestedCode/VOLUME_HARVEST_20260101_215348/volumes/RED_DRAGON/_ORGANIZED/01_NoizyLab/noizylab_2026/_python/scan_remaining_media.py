#!/usr/bin/env python3
"""
scan_remaining_media.py
Scans /Volumes/JOE for remaining media files (audio, video, images) and prints their paths.
Supported extensions: .wav, .mp3, .aiff, .flac, .m4a, .aac, .ogg, .wma, .mp4, .mov, .avi, .mkv, .jpg, .jpeg, .png, .gif, .bmp, .tiff
"""
import os
from pathlib import Path

MEDIA_EXTS = {
    '.wav', '.mp3', '.aiff', '.flac', '.m4a', '.aac', '.ogg', '.wma',
    '.mp4', '.mov', '.avi', '.mkv',
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'
}

SCAN_ROOT = Path("/Volumes/JOE")

def scan_media_files(root):
    for dirpath, _, filenames in os.walk(root):
        for fname in filenames:
            ext = Path(fname).suffix.lower()
            if ext in MEDIA_EXTS:
                print(os.path.join(dirpath, fname))

if __name__ == "__main__":
    scan_media_files(SCAN_ROOT)
