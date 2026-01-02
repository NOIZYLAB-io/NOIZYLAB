from pathlib import Path
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed

AGENTS_TOTAL = 96
SOURCE = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Mission_Control"
DEST = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace" / "Audio_Project"
AUDIO_EXTS = {".wav", ".aiff", ".mp3", ".flac"}

def copy_audio(file):
    dest_file = DEST / file.name
    shutil.copy2(file, dest_file)
    print(f"Copied: {file} → {dest_file}")

def main():
    DEST.mkdir(parents=True, exist_ok=True)
    files = [f for f in SOURCE.rglob("*") if f.is_file() and f.suffix.lower() in AUDIO_EXTS]
    print(f"Found {len(files)} audio files in Mission_Control.")
    with ThreadPoolExecutor(max_workers=AGENTS_TOTAL) as pool:
        futures = [pool.submit(copy_audio, f) for f in files]
        for f in as_completed(futures):
            f.result()
    print("✅ All audio files copied to Audio_Project.")

if __name__ == "__main__":
    main()