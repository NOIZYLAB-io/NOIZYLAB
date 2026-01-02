import os
import shutil
from pathlib import Path

SOURCE = os.path.expanduser("~/Library/Application Support")
DEST = "/Volumes/4TB_UTILITY/Audio_Migrated"
AUDIO_EXTS = {".wav", ".mp3", ".aiff", ".flac", ".ogg", ".m4a", ".aac"}
DRY_RUN = True  # Set to False to actually move files

audio_files = []
for root, _, files in os.walk(SOURCE):
    for file in files:
        if Path(file).suffix.lower() in AUDIO_EXTS:
            full_path = os.path.join(root, file)
            try:
                size = os.path.getsize(full_path)
                audio_files.append((size, full_path))
            except Exception as e:
                print(f"Could not access {full_path}: {e}")

audio_files.sort(reverse=True)

print(f"\nFound {len(audio_files)} audio files.")
print("Top 20 largest audio files:")
for size, path in audio_files[:20]:
    print(f"{size/1024/1024:.2f} MB\t{path}")

moved = 0
for size, path in audio_files:
    rel_path = os.path.relpath(path, SOURCE)
    dest_path = os.path.join(DEST, rel_path)
    if DRY_RUN:
        print(f"[DRY RUN] Would move {path} -> {dest_path}")
    else:
        try:
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)
            shutil.move(path, dest_path)
            print(f"Moved {path} -> {dest_path}")
            moved += 1
        except Exception as e:
            print(f"Failed to move {path}: {e}")

if DRY_RUN:
    print(f"\n[DRY RUN] No files moved. {len(audio_files)} files would be moved.")
else:
    print(f"\nDone! {moved} files moved to {DEST}")