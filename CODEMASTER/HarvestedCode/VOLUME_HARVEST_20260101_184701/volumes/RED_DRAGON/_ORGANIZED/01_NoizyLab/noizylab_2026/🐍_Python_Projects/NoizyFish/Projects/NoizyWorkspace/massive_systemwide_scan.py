#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Massive Systemwide Scan — Instruments + Sounds
Scans all mounted volumes for instrument/sample/plugin extensions.
Deduplicates by checksum. Exports a master catalog (CSV + YAML).
Sorted by vendor/manufacturer, category, and file location.
"""

import os, csv, hashlib, yaml
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

# --- Config ---
MAX_WORKERS = 96
OUT_DIR = Path("./massive_scan_out")
OUT_DIR.mkdir(parents=True, exist_ok=True)
CSV_OUT = OUT_DIR / "massive_catalog.csv"
YAML_OUT = OUT_DIR / "massive_catalog.yaml"

# Extensions of interest
EXTS = {
    "instruments": {".nki",".nkm",".nkc",".nkr",".nkx",".ncw",".nicnt"},
    "audio_lossless": {".wav",".aiff",".aif",".flac"},
    "audio_lossy": {".mp3",".m4a",".aac",".ogg"},
    "presets": {".preset",".bank",".bundle",".nks",".nis"},
    "plugins": {".component",".vst",".vst3",".aaxplugin"},
}
ALL_EXTS = set().union(*EXTS.values())

def extract_vendor(p: Path):
    ignore = {"users", "shared", "documents", "music", "library", "application support", "volumes", "macintosh hd"}
    for part in reversed(p.parts[:-1]):
        if part.lower() not in ignore and len(part) > 2:
            return part
    return ""

def sha256_file(p: Path):
    try:
        h = hashlib.sha256()
        with p.open("rb") as f:
            for chunk in iter(lambda: f.read(1024*1024), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return None

def categorize(ext: str) -> str:
    for cat, exts in EXTS.items():
        if ext in exts: return cat
    return "other"

def scan_file(p: Path):
    if not p.is_file(): return None
    ext = p.suffix.lower()
    if ext not in ALL_EXTS: return None
    try: size = p.stat().st_size
    except Exception: size = None
    vendor = extract_vendor(p)
    return {
        "vendor": vendor,
        "category": categorize(ext),
        "path": str(p),
        "name": p.name,
        "ext": ext,
        "size_bytes": size,
        "checksum": sha256_file(p),
        "volume": p.anchor or p.parts[0],
    }

def list_roots():
    roots = []
    vols = Path("/Volumes")
    if vols.exists():
        roots += [v for v in vols.iterdir() if v.is_dir()]
    roots += [
        Path("~/Documents").expanduser(),
        Path("~/Music").expanduser(),
        Path("/Users/Shared").expanduser(),
        Path("/Library/Application Support").expanduser(),
    ]
    return list({str(p): p for p in roots}.values())

def main():
    print("Starting Massive Systemwide Scan — Instruments + Sounds")
    roots = list_roots()
    print(f"Scanning {len(roots)} roots with {MAX_WORKERS} agents…")

    candidates = []
    for root in roots:
        print(f"Scanning root: {root}")
        try:
            for p in root.rglob("*"):
                if p.is_file() and p.suffix.lower() in ALL_EXTS:
                    candidates.append(p)
        except Exception as e:
            print(f"Skipped {root}: {e}")
            continue
    print(f"Candidate files found: {len(candidates)}")

    results = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futs = [ex.submit(scan_file, p) for p in candidates]
        for f in as_completed(futs):
            rec = f.result()
            if rec: results.append(rec)

    # Deduplicate
    uniq = {}
    for r in results:
        key = r["checksum"] or f"path:{r['path']}"
        if key not in uniq: uniq[key] = r
    rows = list(uniq.values())
    print(f"Unique items after deduplication: {len(rows)}")

    # Sort by vendor, category, path
    rows.sort(key=lambda r: (r.get("vendor","").lower(), r.get("category",""), r.get("path","")))

    # Export CSV
    headers = ["vendor","category","path","name","ext","size_bytes","checksum","volume"]
    with CSV_OUT.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=headers)
        w.writeheader(); w.writerows(rows)
    print(f"CSV catalog exported to: {CSV_OUT.resolve()}")

    # Export YAML
    YAML_OUT.write_text(yaml.safe_dump(
        {"generated": datetime.utcnow().isoformat(), "items": rows}, sort_keys=False
    ))
    print(f"YAML catalog exported to: {YAML_OUT.resolve()}")

    # --- Auto-open CSV on Desktop at 1/3 screen size ---
    try:
        applescript = f'''
        tell application "Finder"
            open POSIX file "{CSV_OUT.resolve()}"
        end tell
        delay 1
        tell application "Numbers"
            activate
            set bounds of front window to {{100, 100, 1200, 900}}
        end tell
        '''
        os.system(f'osascript -e \'{applescript}\'')
        print("CSV auto-opened in Numbers at 1/3 screen size.")
    except Exception as e:
        print(f"Could not auto-open CSV: {e}")

    print("Scan complete.")

if __name__ == "__main__":
    main()

# To install required packages:
# pip install pillow icnsutil
