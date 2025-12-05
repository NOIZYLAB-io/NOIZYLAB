#!/usr/bin/env python3
import os
from mutagen import File

INPUT_FILE = "audio_files.txt"
OUTPUT_FILE = "files_with_no_metadata.txt"

def find_files_with_no_metadata(input_file=INPUT_FILE, output_file=OUTPUT_FILE):
    no_metadata = []
    checked = 0
    with open(input_file, "r") as f:
        for line in f:
            path = line.strip()
            if not path:
                continue
            checked += 1
            try:
                audio = File(path)
                if audio is None or not audio.tags:
                    no_metadata.append(path)
                    print(f"No metadata: {path}")
            except Exception as e:
                print(f"Error reading {path}: {e}")
    if no_metadata:
        with open(output_file, "w") as out:
            out.write("\n".join(no_metadata))
        print(f"\nFiles with no metadata saved to {output_file}")
    else:
        print("\nAll files have some metadata.")
    print(f"Checked {checked} files.")

if __name__ == "__main__":
    find_files_with_no_metadata()
