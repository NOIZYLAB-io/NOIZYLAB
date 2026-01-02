import os
import shutil
from pathlib import Path

# Output folder
OUTPUT_DIR = Path.home() / "Desktop" / "AudioContents"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Locations to scan: root mounts and Desktop itself
SEARCH_PATHS = [
    Path("/Volumes"),         # macOS external drives
    Path("/mnt"),             # Linux-style mounts
    Path.home() / "Desktop",  # Desktop itself
]

def collect_txt_files():
    txt_files = []

    for base in SEARCH_PATHS:
        if not base.exists():
            continue
        for root, _, files in os.walk(base):
            for file in files:
                if file.lower().endswith(".txt"):
                    filepath = Path(root) / file
                    txt_files.append(filepath)
    return txt_files

def copy_txt_files(txt_files):
    for file in txt_files:
        target = OUTPUT_DIR / file.name
        # Avoid overwriting — add suffix if needed
        counter = 1
        while target.exists():
            target = OUTPUT_DIR / f"{file.stem}_{counter}{file.suffix}"
            counter += 1

        print(f"Copying {file} → {target}")
        shutil.copy2(file, target)

if __name__ == "__main__":
    txts = collect_txt_files()
    print(f"Found {len(txts)} .txt files")
    copy_txt_files(txts)
    print("✅ All text files copied to ~/Desktop/AudioContents")
