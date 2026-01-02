import os
import shutil
from pathlib import Path

# Set source to the Application Support folder inside bobby-mission-control
SOURCE = os.path.expanduser("~/bobby-mission-control/Application Support")
DEST = "/Volumes/4TB_UTILITY/Audio_Migrated"
AUDIO_EXTS = {".wav", ".mp3", ".aiff", ".flac", ".ogg", ".m4a", ".aac"}
DRY_RUN = True      # Set to False to actually move files
MIN_MB = 10         # Only move files >= this size (MB)
TOP_N = None        # Set to an int to move only the N largest files, or None for all

def scan_audio_files():
    files = []
    for root, _, fs in os.walk(SOURCE):
        for f in fs:
            if Path(f).suffix.lower() in AUDIO_EXTS:
                p = os.path.join(root, f)
                try:
                    sz = os.path.getsize(p)
                    if sz >= MIN_MB * 1024 * 1024:
                        files.append((sz, p))
                except Exception as e:
                    print(f"Could not access {p}: {e}")
    return files

def main():
    audio_files = scan_audio_files()
    audio_files.sort(reverse=True)
    if TOP_N:
        audio_files = audio_files[:TOP_N]

    print(f"\nFound {len(audio_files)} audio files >= {MIN_MB} MB.")
    print("Top 20 largest audio files:")
    for sz, p in audio_files[:20]:
        print(f"{sz/1024/1024:.2f} MB\t{p}")

    moved = 0
    for sz, src in audio_files:
        rel = os.path.relpath(src, SOURCE)
        dst = os.path.join(DEST, rel)
        if DRY_RUN:
            print(f"[DRY RUN] Would move {src} -> {dst}")
        else:
            try:
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.move(src, dst)
                print(f"Moved {src} -> {dst}")
                moved += 1
            except Exception as e:
                print(f"Failed to move {src}: {e}")

    print(f"\n{'[DRY RUN] ' if DRY_RUN else ''}Done! {moved if not DRY_RUN else len(audio_files)} files {'would be' if DRY_RUN else 'were'} moved to {DEST}")

if __name__ == "__main__":
    main()