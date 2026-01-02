#!/usr/bin/env python3
import csv
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Dict, List, Tuple


SOURCE_TOP = Path("/Volumes/6TB/Native Instruments")
DEST_TOP = Path("/Volumes/6TB/Native_Instruments_2026/03_CORE_INSTRUMENTS/Native Instruments")
SAFETY_ROOT = Path("/Volumes/6TB/_NI_2026/SAFETY")
REPORTS_BASE = Path("/Users/rsp_ms/Desktop/KONTAKT_LAB/REPORTS/RENAME")


INSTRUMENT_EXT = {".nki", ".nkm"}
ALLOWED_AUDIO_EXT = {".wav", ".aif", ".aiff", ".ncw"}
IGNORED_FILENAMES = {".DS_Store", "Thumbs.db"}


# Known name fixes for common NI products
KNOWN_FIXES = {
    # Apostrophes and brand punctuation
    "Alicias Keys": "Alicia's Keys",
    "Traktors 12": "Traktor's 12",
    # Spelling touch-ups (only when exact token matches)
}


def collapse_spaces(s: str) -> str:
    s = s.replace('\u00A0', ' ')  # non-breaking space
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def prettify_underscores(name: str) -> str:
    # Convert underscores to spaces when they look like word separators
    if re.search(r"[A-Za-z]_[A-Za-z]", name):
        name = name.replace("_", " ")
        name = collapse_spaces(name)
    return name


def apply_known_fixes(name: str) -> str:
    for k, v in KNOWN_FIXES.items():
        # whole-word replacement
        name = re.sub(rf"\b{re.escape(k)}\b", v, name)
    return name


def looks_like_library(path: Path) -> Tuple[int, int]:
    nki = 0
    audio = 0
    for root, _, files in os.walk(path):
        for f in files:
            if f in IGNORED_FILENAMES or f.startswith("._"):
                continue
            ext = Path(f).suffix.lower()
            if ext in INSTRUMENT_EXT:
                nki += 1
            elif ext in ALLOWED_AUDIO_EXT:
                audio += 1
            # quick exit for speed
            if nki >= 1 and audio >= 10:
                return nki, audio
    return nki, audio


def add_library_suffix_if_needed(name: str, path: Path) -> str:
    # Only add "Library" when it smells like a library and suffix isn't present
    lowered = name.lower()
    if lowered.endswith(" library") or lowered.endswith(" libraries"):
        return name
    nki, audio = looks_like_library(path)
    if nki >= 1 and audio >= 10:
        return name + " Library"
    return name


def sniff_missing_audio_ext(file_path: Path) -> str:
    # Returns suggested extension (including dot) or ""
    try:
        with file_path.open('rb') as f:
            head = f.read(12)
        if len(head) >= 12:
            if head[0:4] == b'RIFF' and head[8:12] == b'WAVE':
                return ".wav"
            if head[0:4] == b'FORM' and head[8:12] in (b'AIFF', b'AIFC'):
                return ".aif"
        # very conservative on NCW; skip unless extension already present
        return ""
    except Exception:
        return ""


def safe_rename(src: Path, dst: Path, execute: bool) -> Tuple[str, Path]:
    if src == dst:
        return ("noop", dst)
    dst.parent.mkdir(parents=True, exist_ok=True)
    if dst.exists():
        # Collision: park the src into safety with a timestamp
        SAFETY_ROOT.mkdir(parents=True, exist_ok=True)
        ts = time.strftime("%Y%m%d_%H%M%S")
        parked = SAFETY_ROOT / f"{dst.name}__RENAME_COLLISION__{ts}"
        if execute:
            os.rename(src, parked)
        return ("collision_parked", parked)
    else:
        if execute:
            os.rename(src, dst)
        return ("renamed", dst)


def normalize_top_level(top: Path, execute: bool, rows: List[Dict[str, object]]) -> None:
    for entry in sorted(top.iterdir(), key=lambda p: p.name.lower()):
        if not entry.is_dir() or entry.name.startswith('.'):
            continue
        original = entry.name
        name = collapse_spaces(original)
        name = prettify_underscores(name)
        name = apply_known_fixes(name)
        name = add_library_suffix_if_needed(name, entry)
        # final cleanup: collapse spaces again in case suffix added
        name = collapse_spaces(name)

        dst = entry.parent / name
        action, final_path = safe_rename(entry, dst, execute)
        rows.append({
            "scope": "dir",
            "top": str(top),
            "from": original,
            "to": name,
            "action": action,
            "final_path": str(final_path)
        })


def fix_missing_audio_extensions(root_dir: Path, execute: bool, rows: List[Dict[str, object]]) -> None:
    for root, _, files in os.walk(root_dir):
        root_p = Path(root)
        for name in files:
            if name in IGNORED_FILENAMES or name.startswith("._"):
                continue
            p = root_p / name
            if p.suffix == "":
                ext = sniff_missing_audio_ext(p)
                if ext:
                    dst = p.with_name(p.name + ext)
                    action, final_path = safe_rename(p, dst, execute)
                    rows.append({
                        "scope": "file",
                        "top": str(root_dir),
                        "from": str(p),
                        "to": str(dst),
                        "action": action,
                        "final_path": str(final_path)
                    })


def run(execute: bool = False) -> None:
    ts = time.strftime("%Y%m%d_%H%M%S")
    report_dir = REPORTS_BASE / f"NI_NAME_NORMALIZE_{ts}"
    report_dir.mkdir(parents=True, exist_ok=True)
    csv_path = report_dir / "renames.csv"
    json_path = report_dir / "renames.json"

    rows: List[Dict[str, object]] = []
    totals = {"dirs_processed": 0, "dir_renamed": 0, "file_ext_fixed": 0, "collision_parked": 0}

    # Normalize top-level names in both source and destination trees
    for top in (SOURCE_TOP, DEST_TOP):
        if not top.exists():
            continue
        before = len(rows)
        normalize_top_level(top, execute, rows)
        after = len(rows)
        totals["dirs_processed"] += max(0, after - before)
        # After directory renames, attempt missing audio extension fixes within each top
        fix_missing_audio_extensions(top, execute, rows)

    # Tally
    for r in rows:
        if r["action"] == "renamed":
            if r["scope"] == "dir":
                totals["dir_renamed"] += 1
            else:
                totals["file_ext_fixed"] += 1
        elif r["action"].startswith("collision_parked"):
            totals["collision_parked"] += 1

    # Write reports
    if rows:
        with csv_path.open('w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
    with json_path.open('w') as f:
        json.dump({"totals": totals, "items": rows}, f, indent=2)

    print(json.dumps({"totals": totals, "csv": str(csv_path), "json": str(json_path)}, indent=2))


if __name__ == "__main__":
    execute = True
    if len(sys.argv) > 1 and sys.argv[1] == "--dry-run":
        execute = False
    SAFETY_ROOT.mkdir(parents=True, exist_ok=True)
    run(execute=execute)
