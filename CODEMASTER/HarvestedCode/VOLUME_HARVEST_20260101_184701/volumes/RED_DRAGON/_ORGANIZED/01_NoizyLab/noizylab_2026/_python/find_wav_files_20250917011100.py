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

try:
    from mutagen.wave import WAVE
except ImportError:
    WAVE = None
    print("Warning: mutagen not installed. Metadata editing will be skipped.")


def find_wav_files(search_path):
    wav_files = []
    keywords = ["original", "music", "track", "Noizyfish"]  # Add your artist name or more keywords here
    for root, dirs, files in os.walk(search_path):
        for file in files:
            if file.lower().endswith('.wav'):
                full_path = os.path.join(root, file)
                # Filter for original music tracks by filename or folder name
                name = file.lower() + root.lower()
                if any(kw in name for kw in keywords):
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
    print(f"Found {len(wav_files)} original music .wav files:")
    for f in wav_files:
        print(f)
        # Correct metadata for mislabeled sound effects libraries
        if WAVE:
            try:
                audio = WAVE(f)
                tags = audio.tags or {}
                # Example: If genre is 'Sound Effects', but filename/keywords indicate music, update genre
                if tags.get('genre', '').lower() == 'sound effects':
                    tags['genre'] = 'Music'
                    tags['artist'] = 'Noizyfish'  # Update with your artist name
                    tags['title'] = os.path.splitext(os.path.basename(f))[0]
                    audio.save()
                    print(f"  Updated metadata: genre -> Music, artist -> Noizyfish")
            except Exception as e:
                print(f"  Metadata update failed: {e}")
        else:
            print("  Skipping metadata correction (mutagen not installed)")


if __name__ == "__main__":
    main()

# To install the required mutagen package, run:
pip install mutagen
