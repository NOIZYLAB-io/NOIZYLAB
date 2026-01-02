"""
find_wav_files.py
-----------------
Recursively searches for all .wav files in a specified directory.

Usage:
    python find_wav_files.py /path/to/search

Outputs a list of .wav files found.
"""

import os
import sys


def find_wav_files(search_path):
    wav_files = []
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if file.lower().endswith('.wav'):
                full_path = os.path.join(root, file)
                wav_files.append(full_path)
    return wav_files


def main():
    if len(sys.argv) < 2:
        print("Usage: python find_wav_files.py /path/to/search")
        sys.exit(1)
    search_path = sys.argv[1]
    if not os.path.exists(search_path):
        print(f"Error: Path '{search_path}' does not exist.")
        sys.exit(1)
    wav_files = find_wav_files(search_path)
    print(f"Found {len(wav_files)} .wav files:")
    for f in wav_files:
        print(f)


if __name__ == "__main__":
    main()
