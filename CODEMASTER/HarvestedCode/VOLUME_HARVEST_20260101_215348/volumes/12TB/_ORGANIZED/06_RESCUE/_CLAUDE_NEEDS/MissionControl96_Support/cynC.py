import sys
import os
import csv
import json
import time
import shutil
import logging
from pathlib import Path
from datetime import datetime

try:
    from mutagen import File as MutagenFile
except ImportError:
    print("Please install mutagen: pip install mutagen")
    sys.exit(1)

# --- CONFIGURATION ---
AUDIO_EXTS = [".wav", ".mp3", ".aiff", ".flac", ".ogg", ".m4a", ".aac", ".wma", ".alac"]
EXPORT_BASE = Path.home() / "Desktop" / "FishNetScans"
SCAN_INTERVAL = 600  # seconds between scans (10 minutes)
AUTO_MOVE = False   # Set True to auto-organize files by extension
LOG_PATH = EXPORT_BASE / "fishnet_scan.log"

# --- LOGGING SETUP ---
EXPORT_BASE.mkdir(parents=True, exist_ok=True)
logging.basicConfig(filename=LOG_PATH, level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s')

def get_scan_paths():
    # Always include ~/Desktop/instruments
    paths = [str(Path.home() / "Desktop" / "instruments")]
    # Add all mounted volumes except system disk
    volumes_dir = Path("/Volumes")
    if volumes_dir.exists():
        for vol in volumes_dir.iterdir():
            if vol.is_dir() and not str(vol).startswith("/Volumes/Macintosh"):
                paths.append(str(vol))
    return paths

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

def extract_audio_metadata(file_path):
    meta = {"file_path": file_path}
    try:
        audio = MutagenFile(file_path)
        if audio is not None:
            meta.update({
                "duration": getattr(audio.info, "length", None),
                "bitrate": getattr(audio.info, "bitrate", None),
                "sample_rate": getattr(audio.info, "sample_rate", None),
                "channels": getattr(audio.info, "channels", None),
                "format": type(audio).__name__
            })
    except Exception as e:
        meta["error"] = str(e)
        logging.warning(f"Metadata extraction failed for {file_path}: {e}")
    return meta

def scan_all(paths):
    sound_files = []
    extensions = set()
    docs = []
    seen_hashes = set()
    metadata = []
    stats = {"total_size": 0, "by_ext": {}, "duplicates": 0}
    for root_dir in paths:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            for file in filenames:
                ext = os.path.splitext(file)[1].lower()
                extensions.add(ext)
                full_path = os.path.join(dirpath, file)
                if ext in AUDIO_EXTS:
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
                        meta = extract_audio_metadata(full_path)
                        metadata.append(meta)
                    except Exception as e:
                        logging.warning(f"Error reading {full_path}: {e}")
                        continue
                    sound_files.append(full_path)
                if file.lower().startswith(('readme', 'license', 'manual', 'doc')):
                    docs.append(full_path)
    return sound_files, extensions, docs, stats, metadata

def export_results(sound_files, extensions, docs, stats, metadata, export_dir):
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
            "stats": stats,
            "metadata": metadata
        }, jsonfile, indent=2)
    # Export metadata CSV
    meta_csv_path = export_dir / "audio_metadata.csv"
    if metadata:
        with open(meta_csv_path, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=list(metadata[0].keys()))
            writer.writeheader()
            for meta in metadata:
                writer.writerow(meta)
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
    if metadata:
        shutil.copy(meta_csv_path, backup_dir / f"audio_metadata_{export_dir.name}.csv")
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
    print("Hello, NoizyFish!")
    while True:
        try:
            print(f"\nStarting scan at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            export_dir = EXPORT_BASE / f"Scan_{timestamp}"
            scan_paths = get_scan_paths()
            sound_files, extensions, docs, stats, metadata = scan_all(scan_paths)
            export_results(sound_files, extensions, docs, stats, metadata, export_dir)
            if AUTO_MOVE:
                auto_move_files(sound_files, export_dir)
                print(f"Files auto-organized by extension in {export_dir/'organized'}")
            print(f"Waiting {SCAN_INTERVAL} seconds for next scan...\n")
            time.sleep(SCAN_INTERVAL)
        except Exception as e:
            logging.error(f"Error in main loop: {e}")
            print(f"Error occurred: {e}. Continuing...")
            time.sleep(SCAN_INTERVAL)
        os.system('prlctl list --all')
