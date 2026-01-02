import os
import sys
import csv
import json
import time
import shutil
import logging
from pathlib import Path
from datetime import datetime

# --- CONFIGURATION ---
# Scan all mounted volumes, including system and external drives
SCAN_ROOTS = [
    '/',  # System drive (Mission Control)
]
# Add all mounted volumes except system
for vol in os.listdir('/Volumes'):
    SCAN_ROOTS.append(os.path.join('/Volumes', vol))
# Optionally add NoizyFish project folder
SCAN_ROOTS.append(str(Path.home() / 'Desktop' / 'NoizyFish'))

EXCLUDE_PATHS = [
    '/System',
    '/private',
    '/Volumes/Noizy Wind 4/SomeFolderToSkip',  # Example exclusion
]
EXPORT_BASE = Path.home() / "Desktop" / "HandOfGodScans"
LOG_PATH = EXPORT_BASE / "hand_of_god_scan.log"

EXPORT_BASE.mkdir(parents=True, exist_ok=True)
logging.basicConfig(filename=LOG_PATH, level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

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

def scan_directory(root_dir):
    files = []
    extensions = set()
    docs = []
    seen_hashes = set()
    stats = {"total_size": 0, "by_ext": {}, "duplicates": 0}
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Exclude paths
        if any(os.path.abspath(dirpath).startswith(os.path.abspath(ex)) for ex in EXCLUDE_PATHS):
            continue
        for file in filenames:
            ext = os.path.splitext(file)[1].lower()
            extensions.add(ext)
            full_path = os.path.join(dirpath, file)
            try:
                size = os.path.getsize(full_path)
                stats["total_size"] += size
                stats["by_ext"].setdefault(ext, 0)
                stats["by_ext"][ext] += 1
                file_hash = hash_file(full_path)
                if file_hash in seen_hashes:
                    stats["duplicates"] += 1
                    continue
                seen_hashes.add(file_hash)
            except Exception as e:
                logging.warning(f"Error reading {full_path}: {e}")
                continue
            files.append(full_path)
            if file.lower().startswith(('readme', 'license', 'manual', 'doc')):
                docs.append(full_path)
    return files, extensions, docs, stats

def export_results(files, extensions, docs, stats, export_dir):
    export_dir.mkdir(parents=True, exist_ok=True)
    # Export CSV
    csv_path = export_dir / "inventory.csv"
    with open(csv_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["file_path", "extension", "is_doc"])
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            is_doc = any(f == doc for doc in docs)
            writer.writerow([f, ext, is_doc])
    # Export JSON
    json_path = export_dir / "inventory.json"
    with open(json_path, "w") as jsonfile:
        json.dump({
            "files": files,
            "extensions": sorted(list(extensions)),
            "docs": docs,
            "stats": stats
        }, jsonfile, indent=2)
    # Export stats
    stats_path = export_dir / "stats.txt"
    with open(stats_path, "w") as f:
        f.write(f"Total files: {len(files)}\n")
        f.write(f"Total size: {stats['total_size']/1024/1024:.2f} MB\n")
        f.write(f"Unique extensions: {sorted(list(extensions))}\n")
        f.write(f"Duplicates skipped: {stats['duplicates']}\n")
        f.write("Files by extension:\n")
        for ext, count in stats["by_ext"].items():
            f.write(f"  {ext}: {count}\n")
    logging.info(f"Exported results to {export_dir}")

if __name__ == "__main__":
    print("Welcome to the Hand of God Search!")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    export_dir = EXPORT_BASE / f"Scan_{timestamp}"
    all_files, all_extensions, all_docs, all_stats = [], set(), [], {"total_size": 0, "by_ext": {}, "duplicates": 0}
    for root in SCAN_ROOTS:
        print(f"Setting read permissions for: {root}")
        try:
            # Attempt to set read permissions recursively
            os.system(f"chmod -R +r '{root}'")
        except Exception as e:
            print(f"[WARNING] Could not set permissions for {root}: {e}")
        print(f"Scanning: {root}")
        files, extensions, docs, stats = scan_directory(root)
        all_files.extend(files)
        all_extensions.update(extensions)
        all_docs.extend(docs)
        all_stats["total_size"] += stats["total_size"]
        for ext, count in stats["by_ext"].items():
            all_stats["by_ext"].setdefault(ext, 0)
            all_stats["by_ext"][ext] += count
        all_stats["duplicates"] += stats["duplicates"]
    export_results(all_files, all_extensions, all_docs, all_stats, export_dir)
    print(f"Scan complete! Results exported to {export_dir}")
