#!/usr/bin/env python3
"""
NoizyFish Full Volume Contents Scanner
- Recursively scans all attached volumes and key workspace folders
- Indexes file/folder structure, size, and type
- Outputs a master inventory for use by the Big Organizer agent
"""

import os
from pathlib import Path
import json
import time

# Volumes and key roots to scan
VOLUMES = [
    Path("/Users/rsp_ms/NoizyFish_Aquarium"),
    Path("/Volumes/4TB Lacie"),
    Path("/Volumes/12TB"),
    Path("/Volumes/6TB"),
    Path("/Volumes/JOE"),
    Path("/Volumes/MAG 4TB"),
    Path("/Volumes/RED DRAGON"),
    Path("/Volumes/SIDNEY"),
]

SCAN_LIMIT = 1000000  # Max files to index (adjust as needed)

INDEX = []
COUNT = 0
START = time.time()

def scan_dir(root):
    global COUNT
    for dirpath, dirnames, filenames in os.walk(root):
        for name in dirnames:
            p = Path(dirpath) / name
            try:
                stat = p.stat()
                INDEX.append({
                    "type": "dir",
                    "path": str(p),
                    "size": stat.st_size,
                    "mtime": stat.st_mtime,
                })
                COUNT += 1
            except Exception:
                continue
            if COUNT >= SCAN_LIMIT:
                return
        for name in filenames:
            p = Path(dirpath) / name
            try:
                stat = p.stat()
                INDEX.append({
                    "type": "file",
                    "path": str(p),
                    "size": stat.st_size,
                    "mtime": stat.st_mtime,
                })
                COUNT += 1
            except Exception:
                continue
            if COUNT >= SCAN_LIMIT:
                return

def main():
    print("=== NoizyFish Full Volume Contents Scan ===")
    for vol in VOLUMES:
        if vol.exists():
            print(f"Scanning: {vol}")
            scan_dir(vol)
        else:
            print(f"(Skipping missing volume: {vol})")
        if COUNT >= SCAN_LIMIT:
            print(f"Reached scan limit of {SCAN_LIMIT} files.")
            break
    duration = time.time() - START
    print(f"Scan complete. {COUNT} items indexed in {duration:.1f} seconds.")
    out_file = Path.home() / f"NoizyFish_Volume_Index_{int(time.time())}.json"
    with open(out_file, "w") as f:
        json.dump(INDEX, f, indent=2)
    print(f"Index written to: {out_file}")

if __name__ == "__main__":
    main()
