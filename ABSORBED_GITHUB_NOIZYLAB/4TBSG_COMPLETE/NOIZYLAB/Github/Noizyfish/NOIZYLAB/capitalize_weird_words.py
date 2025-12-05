#!/usr/bin/env python3
import os

# List of words to capitalize
WORDS_TO_CAPITALIZE = ["atmo", "but"]

# File containing paths to audio-related files
AUDIO_FILES_LIST = "track_filter_audio_files.txt"

def capitalize_words_in_files(file_list_path, words):
    if not os.path.exists(file_list_path):
        print(f"File not found: {file_list_path}")
        return
    with open(file_list_path, "r") as f:
        file_paths = [line.strip() for line in f if line.strip()]
    for fpath in file_paths:
        if not os.path.exists(fpath):
            print(f"File not found: {fpath}")
            continue
        try:
            with open(fpath, "r", encoding="utf-8") as fin:
                content = fin.read()
            for word in words:
                content = content.replace(word, word.upper())
            with open(fpath, "w", encoding="utf-8") as fout:
                fout.write(content)
            print(f"Updated: {fpath}")
        except Exception as e:
            print(f"Error processing {fpath}: {e}")

if __name__ == "__main__":
    capitalize_words_in_files(AUDIO_FILES_LIST, WORDS_TO_CAPITALIZE)
