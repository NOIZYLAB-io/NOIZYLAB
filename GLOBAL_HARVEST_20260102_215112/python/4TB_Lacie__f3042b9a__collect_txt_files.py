#!/usr/bin/env python3
import os
import shutil
import hashlib
import csv
from pathlib import Path

OUTPUT_DIR = Path.home() / "Desktop" / "AudioContents"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

INDEX_FILE = OUTPUT_DIR / "file_index.csv"

SEARCH_PATHS = [
    Path("/Volumes"),         # macOS external drives
    Path("/mnt"),             # Linux mounts
    Path.home() / "Desktop",  # Desktop
]

TEXT_EXTENSIONS = [".txt", ".md", ".rtf", ".docx", ".pdf"]

def file_hash(path, algo="sha256", block_size=65536):
    """Generate hash for duplicate detection."""
    hasher = hashlib.new(algo)
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(block_size), b""):
            hasher.update(block)
    return hasher.hexdigest()

def collect_files():
    """Scan all drives for text-based files."""
    collected = []
    for base in SEARCH_PATHS:
        if not base.exists():
            continue
        for root, _, files in os.walk(base):
            for file in files:
                ext = Path(file).suffix.lower()
                if ext in TEXT_EXTENSIONS:
                    filepath = Path(root) / file
                    collected.append(filepath)
    return collected

def copy_and_index(files):
    """Copy files and build index."""
    with open(INDEX_FILE, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Original Path", "File Name", "Extension", "Size (bytes)", "Hash"])

        for file in files:
            try:
                size = file.stat().st_size
                ext = file.suffix.lower()
                h = file_hash(file)

                target = OUTPUT_DIR / file.name
                counter = 1
                while target.exists():
                    target = OUTPUT_DIR / f"{file.stem}_{counter}{file.suffix}"
                    counter += 1

                shutil.copy2(file, target)
                print(f"Copied {file} → {target}")

                writer.writerow([str(file), file.name, ext, size, h])
            except Exception as e:
                print(f"⚠️ Could not process {file}: {e}")


if __name__ == "__main__":
        print("🔍 Scanning for text-based files across all drives...")
        files = collect_files()
        print(f"Found {len(files)} candidate files")

        copy_and_index(files)
        print(f"✅ All files copied to {OUTPUT_DIR}")
        print(f"📑 Index saved at {INDEX_FILE}")
