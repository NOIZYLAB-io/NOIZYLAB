#!/usr/bin/env python3
"""
scan_audio_files.py
Scans a given drive or folder for audio files and prints their paths.
Supported extensions: .wav, .mp3, .aiff, .flac, .m4a, .aac, .ogg, .wma, .mp4
"""
import os
from pathlib import Path

AUDIO_EXTS = {'.wav', '.mp3', '.aiff', '.flac', '.m4a', '.aac', '.ogg', '.wma', '.mp4'}

SCAN_ROOT = Path("/Volumes/JOE")

def scan_audio_files(root):
    for dirpath, dirnames, filenames in os.walk(root):
        for fname in filenames:
            ext = Path(fname).suffix.lower()
            if ext in AUDIO_EXTS:
                print(os.path.join(dirpath, fname))

if __name__ == "__main__":
    scan_audio_files(SCAN_ROOT)
