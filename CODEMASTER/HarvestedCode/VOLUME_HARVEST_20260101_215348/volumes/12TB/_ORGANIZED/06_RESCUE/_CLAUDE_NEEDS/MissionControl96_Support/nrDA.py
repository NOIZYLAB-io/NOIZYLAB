#!/usr/bin/env python3
import csv
import json
import os
import shutil
import sys
import time
from pathlib import Path
from typing import Dict, List, Tuple


SOURCE = Path("/Volumes/6TB/Native Instruments")
DEST_ROOT = Path("/Volumes/6TB/Native_Instruments_2026/03_CORE_INSTRUMENTS/Native Instruments")
SAFETY_ROOT = Path("/Volumes/6TB/_NI_2026/SAFETY")
REPORTS_BASE = Path("/Users/rsp_ms/Desktop/KONTAKT_LAB/REPORTS/MIGRATIONS")


ALLOWED_AUDIO_EXT = {".wav", ".aif", ".aiff", ".ncw"}
INSTRUMENT_EXT = {".nki", ".nkm"}
IGNORED_FILE_PREFIXES = {"._"}
IGNORED_FILENAMES = {".DS_Store", "Thumbs.db"}


def human_bytes(n: int) -> str:
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if n < 1024.0:
            return f"{n:3.1f} {unit}"
        n /= 1024.0
    return f"{n:.1f} PB"


def purity_check(lib_path: Path) -> Tuple[bool, Dict[str, int], List[str]]:
    """Strict but fast purity test:
    - No zero-byte files (excluding ignored filenames)
    - No broken symlinks
    - At least one instrument file (.nki/.nkm)
    - At least 10 audio samples (.wav/.aif/.aiff/.ncw)
    - All files readable for basic metadata (stat ok)
    """
    stats = {
        "files": 0,
        "dirs": 0,
        "bytes": 0,
        "zero_bytes": 0,
        "broken_symlinks": 0,
        "nki": 0,
        "audio": 0,
        "ignored": 0,
        "errors": 0,
    }
    reasons: List[str] = []

    for root, dirs, files in os.walk(lib_path):
        stats["dirs"] += len(dirs)
        for name in files:
            # ignore trivial files
            if name in IGNORED_FILENAMES or any(name.startswith(p) for p in IGNORED_FILE_PREFIXES):
                stats["ignored"] += 1
                continue
            p = Path(root) / name
            try:
                stats["files"] += 1
                if p.is_symlink():
                    # broken symlink?
                    try:
                        target_exists = p.exists()
                    except Exception:
                        target_exists = False
                    if not target_exists:
                        stats["broken_symlinks"] += 1
                try:
                    sz = p.stat().st_size
                except Exception:
                    stats["errors"] += 1
                    reasons.append(f"stat_error:{p}")
                    continue
                stats["bytes"] += sz
                if sz == 0:
                    stats["zero_bytes"] += 1
                ext = p.suffix.lower()
                if ext in INSTRUMENT_EXT:
                    stats["nki"] += 1
                elif ext in ALLOWED_AUDIO_EXT:
                    stats["audio"] += 1
            except Exception as e:
                stats["errors"] += 1
                reasons.append(f"walk_error:{p}:{e}")

    # Decisions
    if stats["zero_bytes"] > 0:
        reasons.append("has_zero_byte_files")
    if stats["broken_symlinks"] > 0:
        reasons.append("has_broken_symlinks")
    if stats["nki"] < 1:
        reasons.append("no_instruments")
    if stats["audio"] < 10:
        reasons.append("insufficient_audio")
    if stats["errors"] > 0:
        reasons.append("io_errors")

    passed = len(reasons) == 0
    return passed, stats, reasons


def safe_move(src: Path, dest_dir: Path) -> Tuple[str, Path]:
    """Move src directory into dest_dir/src.name.
    If a folder already exists, move to SAFETY with a timestamped suffix.
    Returns (action, final_path)
    """
    dest_dir.mkdir(parents=True, exist_ok=True)
    SAFETY_ROOT.mkdir(parents=True, exist_ok=True)
    target = dest_dir / src.name
    if not target.exists():
        shutil.move(str(src), str(target))
        return ("moved", target)
    # Collision: park in safety
    ts = time.strftime("%Y%m%d_%H%M%S")
    parked = SAFETY_ROOT / f"{src.name}__COLLISION__{ts}"
    shutil.move(str(src), str(parked))
    return ("collision_parked", parked)


def run(execute: bool = True) -> None:
    ts = time.strftime("%Y%m%d_%H%M%S")
    report_dir = REPORTS_BASE / f"NI_PURITY_{ts}"
    report_dir.mkdir(parents=True, exist_ok=True)
    csv_path = report_dir / "summary.csv"
    json_path = report_dir / "summary.json"

    if not SOURCE.exists():
        print(f"[ERROR] Source not found: {SOURCE}")
        sys.exit(1)

    rows: List[Dict[str, object]] = []
    totals = {"examined": 0, "passed": 0, "failed": 0, "moved": 0, "collision_parked": 0, "bytes": 0}

    print(f"[INFO] Scanning libraries in: {SOURCE}")
    for entry in sorted(SOURCE.iterdir(), key=lambda p: p.name.lower()):
        if entry.name.startswith('.'):
            continue
        if not entry.is_dir():
            continue
        totals["examined"] += 1
        print(f"[CHECK] {entry.name}")
        started = time.time()
        passed, stats, reasons = purity_check(entry)
        action = "noop"
        final_path = ""
        if passed:
            totals["passed"] += 1
            totals["bytes"] += stats["bytes"]
            if execute:
                action, moved_path = safe_move(entry, DEST_ROOT)
                final_path = str(moved_path)
                if action == "moved":
                    totals["moved"] += 1
                elif action == "collision_parked":
                    totals["collision_parked"] += 1
        else:
            totals["failed"] += 1
        dur = time.time() - started
        rows.append({
            "name": entry.name,
            "source": str(entry),
            "passed": passed,
            "reasons": ";".join(reasons),
            "files": stats["files"],
            "dirs": stats["dirs"],
            "bytes": stats["bytes"],
            "human_bytes": human_bytes(stats["bytes"]),
            "zero_bytes": stats["zero_bytes"],
            "broken_symlinks": stats["broken_symlinks"],
            "nki": stats["nki"],
            "audio": stats["audio"],
            "ignored": stats["ignored"],
            "errors": stats["errors"],
            "action": action,
            "dest": final_path,
            "duration_sec": round(dur, 2),
        })

    # Write reports
    with csv_path.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else [])
        if rows:
            writer.writeheader()
            writer.writerows(rows)
    with json_path.open('w') as f:
        json.dump({"totals": totals, "items": rows}, f, indent=2)

    print("\n[SUMMARY]")
    print(json.dumps(totals, indent=2))
    print(f"CSV: {csv_path}")
    print(f"JSON: {json_path}")


if __name__ == "__main__":
    # --dry-run to only scan and not move
    execute = True
    if len(sys.argv) > 1 and sys.argv[1] == "--dry-run":
        execute = False
    # Ensure dest roots exist
    DEST_ROOT.mkdir(parents=True, exist_ok=True)
    SAFETY_ROOT.mkdir(parents=True, exist_ok=True)
    run(execute=execute)
