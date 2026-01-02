#!/usr/bin/env python3
import csv
import json
import os
import shutil
import sys
import time
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from typing import Dict, List, Optional, Tuple


SOURCE = Path("/Volumes/6TB/Native Instruments")
DEST_VENDOR_ROOT = Path("/Volumes/6TB/_NI_2026/LIBRARIES")
SAFETY_ROOT = Path("/Volumes/6TB/_NI_2026/SAFETY")
REPORTS_BASE = Path("/Users/rsp_ms/Desktop/KONTAKT_LAB/REPORTS/DEEP")


INSTRUMENT_EXT = {".nki", ".nkm"}
AUDIO_EXT = {".wav", ".aif", ".aiff", ".ncw"}
DOC_EXT = {".pdf", ".txt", ".rtf"}
IMG_EXT = {".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff"}
IGNORED_NAMES = {".DS_Store", "Thumbs.db"}


def human_bytes(n: int) -> str:
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if n < 1024.0:
            return f"{n:3.1f} {unit}"
        n /= 1024.0
    return f"{n:.1f} PB"


def parse_nicnt(lib: Path) -> Dict[str, str]:
    info: Dict[str, str] = {}
    try:
        nicnts = list(lib.rglob("*.nicnt"))
        if not nicnts:
            return info
        # Prefer the top-most nicnt
        nicnt = sorted(nicnts, key=lambda p: len(p.parts))[0]
        try:
            tree = ET.parse(nicnt)
            root = tree.getroot()
            # Try common tags
            for tag in ("SNPID", "Name", "name", "Company", "company", "RegKey", "regkey"):
                el = root.find(f".//{tag}")
                if el is not None and el.text:
                    info[tag.capitalize()] = el.text.strip()
            info["NicntPath"] = str(nicnt)
        except Exception:
            # not XML or unreadable
            info["NicntPath"] = str(nicnt)
    except Exception:
        pass
    return info


def read_wav_aiff_header(p: Path) -> Optional[Dict[str, int]]:
    try:
        with p.open('rb') as f:
            head = f.read(64)
        if head[:4] == b'RIFF' and head[8:12] == b'WAVE':
            # WAV fmt chunk position varies; do a simple scan
            i = 12
            while i + 8 <= len(head):
                ckid = head[i:i+4]
                cksz = int.from_bytes(head[i+4:i+8], 'little', signed=False)
                if ckid == b'fmt ':
                    fmt = head[i+8:i+8+cksz]
                    if len(fmt) >= 16:
                        ch = int.from_bytes(fmt[2:4], 'little')
                        sr = int.from_bytes(fmt[4:8], 'little')
                        bps = int.from_bytes(fmt[14:16], 'little')
                        return {"sr": sr, "ch": ch, "bps": bps}
                    break
                i += 8 + cksz + (cksz % 2)
        elif head[:4] == b'FORM' and head[8:12] in (b'AIFF', b'AIFC'):
            # Simplified COMM chunk parser
            i = 12
            while i + 8 <= len(head):
                ckid = head[i:i+4]
                cksz = int.from_bytes(head[i+4:i+8], 'big', signed=False)
                if ckid == b'COMM':
                    # COMM has channels (2), frames (4), bits (2), sample rate (10)
                    if i+8+cksz <= len(head) and cksz >= 18:
                        comm = head[i+8:i+8+cksz]
                        ch = int.from_bytes(comm[0:2], 'big')
                        bps = int.from_bytes(comm[6:8], 'big')
                        # Samplerate is 80-bit float; skip exact value, return None
                        return {"sr": 0, "ch": ch, "bps": bps}
                    break
                i += 8 + cksz + (cksz % 2)
        return None
    except Exception:
        return None


def scan_library(lib: Path) -> Tuple[bool, Dict[str, object]]:
    meta: Dict[str, object] = {
        "path": str(lib),
        "name": lib.name,
        "bytes": 0,
        "files": 0,
        "dirs": 0,
        "zero_bytes": 0,
        "broken_symlinks": 0,
        "nki": 0,
        "nkm": 0,
        "audio": 0,
        "audio_ext": Counter(),
        "docs": 0,
        "images": 0,
        "snapshots": 0,
        "vendor": "Native Instruments",
        "nicnt": {},
        "audio_sample_stats": Counter(),
    }

    nicnt_info = parse_nicnt(lib)
    if nicnt_info:
        meta["nicnt"] = nicnt_info
        vendor = nicnt_info.get("Company") or nicnt_info.get("Company".capitalize()) or nicnt_info.get("company")
        if vendor:
            meta["vendor"] = vendor

    for root, dirs, files in os.walk(lib):
        meta["dirs"] += len(dirs)
        root_p = Path(root)
        # Snapshots heuristic
        if root_p.name.lower() == "snapshots":
            # count files
            meta["snapshots"] += sum(1 for _ in files)
        for name in files:
            if name in IGNORED_NAMES or name.startswith("._"):
                continue
            p = root_p / name
            try:
                if p.is_symlink():
                    try:
                        if not p.exists():
                            meta["broken_symlinks"] += 1
                    except Exception:
                        meta["broken_symlinks"] += 1
                st = p.stat()
                meta["files"] += 1
                meta["bytes"] += st.st_size
                if st.st_size == 0:
                    meta["zero_bytes"] += 1
                ext = p.suffix.lower()
                if ext == ".nki":
                    meta["nki"] += 1
                elif ext == ".nkm":
                    meta["nkm"] += 1
                elif ext in AUDIO_EXT:
                    meta["audio"] += 1
                    meta["audio_ext"][ext] += 1
                    if ext in (".wav", ".aif", ".aiff") and meta["audio"] < 128:
                        h = read_wav_aiff_header(p)
                        if h:
                            key = f"sr{h.get('sr',0)}_ch{h.get('ch',0)}_b{h.get('bps',0)}"
                            meta["audio_sample_stats"][key] += 1
                elif ext in DOC_EXT:
                    meta["docs"] += 1
                elif ext in IMG_EXT:
                    meta["images"] += 1
            except Exception:
                # skip unreadable entries but record as zero_bytes? leave for now
                pass

    # completeness heuristic for 100%
    complete = (
        meta["zero_bytes"] == 0 and meta["broken_symlinks"] == 0 and
        (meta["nki"] + meta["nkm"]) >= 1 and meta["audio"] >= 10
    )
    return complete, meta


def safe_move(src: Path, dst: Path) -> Tuple[str, Path]:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if not dst.exists():
        shutil.move(str(src), str(dst))
        return ("moved", dst)
    ts = time.strftime("%Y%m%d_%H%M%S")
    parked = SAFETY_ROOT / f"{dst.name}__COLLISION__{ts}"
    parked.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(parked))
    return ("collision_parked", parked)


def run(execute: bool = False) -> None:
    ts = time.strftime("%Y%m%d_%H%M%S")
    report_dir = REPORTS_BASE / f"NI_DEEP_{ts}"
    report_dir.mkdir(parents=True, exist_ok=True)
    csv_path = report_dir / "summary.csv"
    json_path = report_dir / "summary.json"

    totals = {
        "examined": 0,
        "complete": 0,
        "moved": 0,
        "collision_parked": 0,
        "bytes": 0,
    }
    rows: List[Dict[str, object]] = []

    for entry in sorted(SOURCE.iterdir(), key=lambda p: p.name.lower()):
        if not entry.is_dir() or entry.name.startswith('.'):
            continue
        totals["examined"] += 1
        complete, meta = scan_library(entry)
        vendor = str(meta.get("vendor") or "Native Instruments").strip() or "Native Instruments"
        dest_dir = DEST_VENDOR_ROOT / vendor / meta["name"]
        action = "noop"
        final_path = ""
        if complete:
            totals["complete"] += 1
            totals["bytes"] += int(meta["bytes"]) if isinstance(meta["bytes"], int) else 0
            if execute:
                action, moved = safe_move(entry, dest_dir)
                final_path = str(moved)
                if action == "moved":
                    totals["moved"] += 1
                elif action == "collision_parked":
                    totals["collision_parked"] += 1

        # flatten counters for CSV/JSON
        audio_ext = dict(meta["audio_ext"]) if isinstance(meta.get("audio_ext"), Counter) else meta.get("audio_ext", {})
        sample_stats = dict(meta["audio_sample_stats"]) if isinstance(meta.get("audio_sample_stats"), Counter) else meta.get("audio_sample_stats", {})
        nicnt = meta.get("nicnt", {})

        rows.append({
            "name": meta["name"],
            "path": meta["path"],
            "vendor": vendor,
            "bytes": meta["bytes"],
            "human_bytes": human_bytes(int(meta["bytes"])) if isinstance(meta["bytes"], int) else "0 B",
            "files": meta["files"],
            "dirs": meta["dirs"],
            "nki": meta["nki"],
            "nkm": meta["nkm"],
            "audio": meta["audio"],
            "audio_ext": json.dumps(audio_ext),
            "docs": meta["docs"],
            "images": meta["images"],
            "snapshots": meta["snapshots"],
            "zero_bytes": meta["zero_bytes"],
            "broken_symlinks": meta["broken_symlinks"],
            "nicnt_name": nicnt.get("Name") or nicnt.get("name", ""),
            "nicnt_company": nicnt.get("Company") or nicnt.get("company", ""),
            "nicnt_snpid": nicnt.get("Snpid") or nicnt.get("SNPID", ""),
            "audio_sample_stats": json.dumps(sample_stats),
            "complete": complete,
            "action": action,
            "dest": final_path,
        })

    # write reports
    if rows:
        with csv_path.open('w', newline='') as f:
            cols = list(rows[0].keys())
            writer = csv.DictWriter(f, fieldnames=cols)
            writer.writeheader()
            writer.writerows(rows)
    with json_path.open('w') as f:
        json.dump({"totals": totals, "items": rows}, f, indent=2)

    print("[SUMMARY]")
    print(json.dumps(totals, indent=2))
    print(f"CSV: {csv_path}")
    print(f"JSON: {json_path}")


if __name__ == "__main__":
    execute = True
    if len(sys.argv) > 1 and sys.argv[1] == "--dry-run":
        execute = False
    DEST_VENDOR_ROOT.mkdir(parents=True, exist_ok=True)
    SAFETY_ROOT.mkdir(parents=True, exist_ok=True)
    run(execute=execute)
