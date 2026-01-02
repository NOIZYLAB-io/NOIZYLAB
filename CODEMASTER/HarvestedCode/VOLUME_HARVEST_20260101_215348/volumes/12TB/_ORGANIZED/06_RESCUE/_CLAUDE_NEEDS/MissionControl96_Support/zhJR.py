import os
import shutil
from pathlib import Path

# Set your source and destination directories
SOURCE = os.path.expanduser("~/Library/Application Support")
DEST = "/Volumes/4TB_UTILITY/Audio_Migrated"

# Audio file extensions to look for
AUDIO_EXTS = {".wav", ".mp3", ".aiff", ".flac", ".ogg", ".m4a", ".aac"}

# Gather all audio files with their sizes
audio_files = []
for root, dirs, files in os.walk(SOURCE):
    for file in files:
        ext = Path(file).suffix.lower()
        if ext in AUDIO_EXTS:
            full_path = os.path.join(root, file)
            try:
                size = os.path.getsize(full_path)
                audio_files.append((size, full_path))
            except Exception:
                continue

# Sort by size, largest first
audio_files.sort(reverse=True)

# Print top 20 largest audio files
print("Top 20 largest audio files:")
for size, path in audio_files[:20]:
    print(f"{size/1024/1024:.2f} MB\t{path}")

# Move files (uncomment to enable moving)
os.makedirs(DEST, exist_ok=True)
for size, path in audio_files:
    rel_path = os.path.relpath(path, SOURCE)
    dest_path = os.path.join(DEST, rel_path)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    print(f"Moving {path} -> {dest_path}")
    shutil.move(path, dest_path)