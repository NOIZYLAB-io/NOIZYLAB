#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Systemwide Snapshot — Noizy Fish
Non-destructive, timestamped snapshot of catalogs, configs, and volume topology.
"""

import os, sys, shutil, json, csv, hashlib, subprocess
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parent
OUT_ROOT = ROOT / "snapshots"
TS = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
SNAP_DIR = OUT_ROOT / f"snapshot_{TS}"
ARCHIVE = OUT_ROOT / f"snapshot_{TS}.zip"

# Known outputs to collect if present
OMNI_DIR = ROOT / "omnifinder_out"
CANDIDATES = [
    "omnifinder_out/master_catalog.yaml",
    "omnifinder_out/music_catalog.yaml",
    "omnifinder_out/instruments_catalog.yaml",
    "omnifinder_out/sfx_catalog.yaml",
    "omnifinder_out/docs_catalog.yaml",
    "omnifinder_out/volume_map.yaml",
    "omnifinder_out/expected_missing.yaml",
    "omnifinder_out/relocation_plan.yaml",
    "noizyfish_ultrascan.yaml",
    "noizyfish_ultrascan.csv",
    "digital_landscape.yaml",
    "fishnet_vendors.yaml",
    ".vscode/tasks.json",
    ".vscode/keybindings.json",
]

def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def write_text(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)

def capture_volumes():
    vols = []
    vroot = Path("/Volumes")
    if vroot.exists():
        for v in vroot.iterdir():
            if v.is_dir():
                try:
                    total = None
                    vols.append({"volume": v.name, "path": str(v), "exists": True})
                except Exception:
                    vols.append({"volume": v.name, "path": str(v), "exists": True})
    write_text(SNAP_DIR / "volumes.json", json.dumps({"generated": TS, "volumes": vols}, indent=2))

def capture_diskutil():
    try:
        # macOS only — safe read of disk layout
        r = subprocess.run(["diskutil", "list"], capture_output=True, text=True, check=False)
        write_text(SNAP_DIR / "diskutil_list.txt", r.stdout or "")
    except Exception:
        write_text(SNAP_DIR / "diskutil_list.txt", "diskutil not available")

def copy_candidates():
    copied = []
    for rel in CANDIDATES:
        src = ROOT / rel
        if src.exists():
            dest = SNAP_DIR / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dest)
            copied.append(str(dest))
    write_text(SNAP_DIR / "copied_files.json", json.dumps({"copied": copied}, indent=2))

def hash_snapshot_files():
    manifest = []
    for p in SNAP_DIR.rglob("*"):
        if p.is_file():
            try:
                manifest.append({"path": str(p.relative_to(SNAP_DIR)), "sha256": sha256_file(p), "size": p.stat().st_size})
            except Exception:
                manifest.append({"path": str(p.relative_to(SNAP_DIR)), "sha256": None, "size": None})
    write_text(SNAP_DIR / "integrity_manifest.json", json.dumps({"generated": TS, "files": manifest}, indent=2))

def archive_snapshot():
    # Zip the entire snapshot directory
    shutil.make_archive(str(ARCHIVE).replace(".zip",""), "zip", str(SNAP_DIR))

def main():
    ensure_dir(OUT_ROOT)
    ensure_dir(SNAP_DIR)
    # Volume state
    capture_volumes()
    capture_diskutil()
    # Collect known outputs and configs
    copy_candidates()
    # Integrity manifest
    hash_snapshot_files()
    # Archive
    archive_snapshot()
    print(f"Snapshot saved: {SNAP_DIR}")
    print(f"Archive: {ARCHIVE}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "ignite":
        base_path = Path(sys.argv[3]) if len(sys.argv) > 3 else ROOT
        ROOT = base_path
        OUT_ROOT = ROOT / "snapshots"
        SNAP_DIR = OUT_ROOT / f"snapshot_{TS}"
        ARCHIVE = OUT_ROOT / f"snapshot_{TS}.zip"
    main()

# Install required packages
subprocess.check_call([sys.executable, "-m", "pip", "install", "PyYAML", "rich", "PyPDF2", "click"])