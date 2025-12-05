#!/usr/bin/env python3
import os
from textblob import TextBlob

INPUT_FILE = "audio_files.txt"
LOG_FILE = "renamed_files_log.txt"

def correct_spelling_in_filenames(input_file=INPUT_FILE, log_file=LOG_FILE):
    renamed = []
    with open(input_file, "r") as f:
        for line in f:
            path = line.strip()
            if not path:
                continue
            dirname, filename = os.path.split(path)
            name, ext = os.path.splitext(filename)
            # Correct spelling in the base name only
            corrected_name = str(TextBlob(name).correct())
            corrected_filename = corrected_name + ext
            corrected_path = os.path.join(dirname, corrected_filename)
            if corrected_filename != filename:
                try:
                    os.rename(path, corrected_path)
                    renamed.append(f"{path} -> {corrected_path}")
                    print(f"Renamed: {path} -> {corrected_path}")
                except Exception as e:
                    print(f"Failed to rename {path}: {e}")
    if renamed:
        with open(log_file, "w") as log:
            log.write("\n".join(renamed))
        print(f"\nRenaming log saved to {log_file}")
    else:
        print("\nNo files were renamed.")

if __name__ == "__main__":
    correct_spelling_in_filenames()
