import sys
import os
import csv
import json
import time
import shutil
import logging
from pathlib import Path
from datetime import datetime

# --- CONFIGURATION ---
SCAN_PATH = str(Path.home() / "Desktop" / "instruments")
EXPORT_BASE = Path.home() / "Desktop" / "FishNetScans"
SCAN_INTERVAL = 60  # seconds between scans
AUTO_MOVE = False   # Set True to auto-organize files by extension
LOG_PATH = EXPORT_BASE / "fishnet_scan.log"

# --- LOGGING SETUP ---
EXPORT_BASE.mkdir(parents=True, exist_ok=True)
logging.basicConfig(filename=LOG_PATH, level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

def select_volume(default=50):
    print(f"Volume set to {default}")
    return default

def scan_directory(root_dir):
    sound_files = []
    extensions = set()
    docs = []
    seen_hashes = set()
    stats = {"total_size": 0, "by_ext": {}, "duplicates": 0}
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            ext = os.path.splitext(file)[1].lower()
            extensions.add(ext)
            full_path = os.path.join(dirpath, file)
            try:
                size = os.path.getsize(full_path)
                stats["total_size"] += size
                stats["by_ext"].setdefault(ext, 0)
                stats["by_ext"][ext] += 1
                # Duplicate detection by file hash
                file_hash = hash_file(full_path)
                if file_hash in seen_hashes:
                    stats["duplicates"] += 1
                    continue
                seen_hashes.add(file_hash)
            except Exception as e:
                logging.warning(f"Error reading {full_path}: {e}")
                continue
            sound_files.append(full_path)
            if file.lower().startswith(('readme', 'license', 'manual', 'doc')):
                docs.append(full_path)
    return sound_files, extensions, docs, stats

def hash_file(path):
    import hashlib
    h = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            while True:
                chunk = f.read(8192)
                if not chunk:
                    break
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return None

def export_results(sound_files, extensions, docs, stats, export_dir):
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
            "docs": docs,
            "stats": stats
        }, jsonfile, indent=2)
    # Export stats
    stats_path = export_dir / "stats.txt"
    with open(stats_path, "w") as f:
        f.write(f"Total files: {len(sound_files)}\n")
        f.write(f"Total size: {stats['total_size']/1024/1024:.2f} MB\n")
        f.write(f"Unique extensions: {sorted(list(extensions))}\n")
        f.write(f"Duplicates skipped: {stats['duplicates']}\n")
        f.write("Files by extension:\n")
        for ext, count in stats["by_ext"].items():
            f.write(f"  {ext}: {count}\n")
    # Backup results
    backup_dir = EXPORT_BASE / "backups"
    backup_dir.mkdir(exist_ok=True)
    shutil.copy(csv_path, backup_dir / f"sound_inventory_{export_dir.name}.csv")
    shutil.copy(json_path, backup_dir / f"sound_inventory_{export_dir.name}.json")
    logging.info(f"Exported results to {export_dir}")

def auto_move_files(sound_files, export_dir):
    # Organize files by extension
    for f in sound_files:
        ext = os.path.splitext(f)[1].lower().replace(".", "")
        if not ext:
            ext = "unknown"
        target_dir = export_dir / "organized" / ext
        target_dir.mkdir(parents=True, exist_ok=True)
        try:
            shutil.copy2(f, target_dir)
        except Exception as e:
            logging.warning(f"Could not move {f} to {target_dir}: {e}")

if __name__ == "__main__":
    print("Welcome to the NoizyFish Big Giant Fish Net! (Phenomenal Mode)")
    vol = select_volume(default=50)
    while True:
        try:
            print(f"\nStarting scan at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            export_dir = EXPORT_BASE / f"Scan_{timestamp}"
            sound_files, extensions, docs, stats = scan_directory(SCAN_PATH)
            export_results(sound_files, extensions, docs, stats, export_dir)
            if AUTO_MOVE:
                auto_move_files(sound_files, export_dir)
                print(f"Files auto-organized by extension in {export_dir/'organized'}")
            print(f"Waiting {SCAN_INTERVAL} seconds for next scan...\n")
            time.sleep(SCAN_INTERVAL)
        except Exception as e:
            logging.error(f"Error in main loop: {e}")
            print(f"Error occurred: {e}. Continuing...")
            time.sleep(SCAN_INTERVAL)