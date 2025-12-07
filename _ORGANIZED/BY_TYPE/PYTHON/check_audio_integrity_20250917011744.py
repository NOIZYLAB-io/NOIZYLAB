#!/usr/bin/env python3
import soundfile as sf
import os

INPUT_FILE = "audio_files.txt"
OUTPUT_FILE = "corrupted_audio_files.txt"

def check_audio_integrity(input_file=INPUT_FILE, output_file=OUTPUT_FILE):
    corrupted = []
    checked = 0
    with open(input_file, "r") as f:
        for line in f:
            path = line.strip()
            if not path:
                continue
            checked += 1
            try:
                # Try to open and read a small chunk
                with sf.SoundFile(path) as snd:
                    snd.read(frames=1)
            except Exception as e:
                print(f"❌ Corrupted or unreadable: {path}\n   Reason: {e}")
                corrupted.append(path)
    if corrupted:
        with open(output_file, "w") as out:
            out.write("\n".join(corrupted))
        print(f"\nCorrupted files saved to {output_file}")
    else:
        print("\nNo corrupted files found!")
    print(f"Checked {checked} files.")

if __name__ == "__main__":
    check_audio_integrity()
