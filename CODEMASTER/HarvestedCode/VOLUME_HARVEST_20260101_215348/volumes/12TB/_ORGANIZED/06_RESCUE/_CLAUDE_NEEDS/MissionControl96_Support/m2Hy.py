import os
import shutil
from pathlib import Path

# Set source to the Application Support folder inside bobby-mission-control
SOURCE = os.path.expanduser("~/bobby-mission-control/Application Support")
DEST = "/Volumes/4TB_UTILITY/Audio_Migrated"
AUDIO_EXTS = {".wav"}
DRY_RUN = True      # Set to False to actually move files
MIN_MB = 0          # Move all .wav files regardless of size

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

def get_manufacturer(rel_path):
    # Manufacturer is the first folder in the relative path
    parts = rel_path.split(os.sep)
    return parts[0] if len(parts) > 1 else "Unknown"

def main():
    audio_files = scan_audio_files()
    audio_files.sort(reverse=True)

    print(f"\nFound {len(audio_files)} .wav files.")
    print("Top 20 largest .wav files:")
    for sz, p in audio_files[:20]:
        print(f"{sz/1024/1024:.2f} MB\t{p}")

    moved = 0
    for sz, src in audio_files:
        rel = os.path.relpath(src, SOURCE)
        manufacturer = get_manufacturer(rel)
        ext = Path(src).suffix.lower().lstrip(".")
        # New path: DEST/manufacturer/extension/original_file
        dst = os.path.join(DEST, manufacturer, ext, os.path.basename(src))
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