import sys
import os
import csv
import json
from pathlib import Path
from datetime import datetime

def select_volume(default=50):
    if len(sys.argv) > 1:
        try:
            vol = int(sys.argv[1])
            if 0 <= vol <= 100:
                print(f"Volume set to {vol}")
                return vol
            else:
                print("Please enter a number between 0 and 100.")
                return select_volume(default)
        except ValueError:
            print("Invalid input. Please enter a number.")
            return select_volume(default)
    while True:
        try:
            prompt = f"Enter volume (0-100){' [' + str(default) + ']' if default is not None else ''}: "
            inp = input(prompt)
            vol = int(inp) if inp else default
            if vol is not None and 0 <= vol <= 100:
                print(f"Volume set to {vol}")
                return vol
            else:
                print("Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def scan_directory(root_dir):
    sound_files = []
    extensions = set()
    docs = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            ext = os.path.splitext(file)[1].lower()
            extensions.add(ext)
            full_path = os.path.join(dirpath, file)
            sound_files.append(full_path)
            if file.lower().startswith(('readme', 'license', 'manual', 'doc')):
                docs.append(full_path)
    print(f"\nScanned: {root_dir}")
    print(f"Total files: {len(sound_files)}")
    print(f"Unique extensions: {sorted(list(extensions))}")
    print("Documentation files found:")
    for d in docs:
        print(f"  {d}")
    print("Sample sound files:")
    for f in sound_files[:10]:
        print(f"  {f}")
    return sound_files, extensions, docs

def export_results(sound_files, extensions, docs, export_dir):
    export_dir.mkdir(parents=True, exist_ok=True)
    # Export CSV
    csv_path = export_dir / "sound_inventory.csv"
    with open(csv_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["file_path", "extension", "is_doc"])
        for f in sound_files:
            ext = os.path.splitext(f)[1].lower()
            is_doc = any(f == doc for doc in docs)
            writer.writerow([f, ext, is_doc])
    # Export JSON
    json_path = export_dir / "sound_inventory.json"
    with open(json_path, "w") as jsonfile:
        json.dump({
            "files": sound_files,
            "extensions": sorted(list(extensions)),
            "docs": docs
        }, jsonfile, indent=2)
    print(f"\nExported results to:\n  {csv_path}\n  {json_path}")

if __name__ == "__main__":
    print("Welcome to the NoizyFish Big Giant Fish Net!")
    vol = select_volume(default=50)
    default_scan_path = str(Path.home() / "Desktop" / "instruments")
    root = input(f"\nEnter the root directory to scan [{default_scan_path}]: ") or default_scan_path
    sound_files, extensions, docs = scan_directory(root)
    # Export results to timestamped folder
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    export_dir = Path.home() / "Desktop" / f"FishNetScan_{timestamp}"
    export_results(sound_files, extensions, docs, export_dir)

python3 /Users/rsp_ms/Desktop/NoizyFish/scripts/fishnet_scanner.py