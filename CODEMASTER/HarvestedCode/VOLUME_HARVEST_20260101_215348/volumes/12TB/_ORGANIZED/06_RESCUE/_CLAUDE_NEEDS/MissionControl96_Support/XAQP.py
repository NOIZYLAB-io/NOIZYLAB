#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Noizy Fish UltraScan — 96-agent parallel scanner
Fastest possible pipeline: scans all mounted volumes + common roots,
indexes audio + instrument extensions, dedupes by checksum, exports master catalog.
"""

import os, sys, csv, json, hashlib, yaml
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

# --- Config ---
MAX_WORKERS = 96
COMMON_ROOTS = [
    "/Users/Shared/Native Instruments",
    "/Library/Application Support/Native Instruments",
    "/Library/Application Support/iZotope",
    "~/Documents/Native Instruments",
    "~/Documents/iZotope",
    "/Library/Audio/Plug-Ins/Components",
    "/Library/Audio/Plug-Ins/VST",
    "/Library/Audio/Plug-Ins/VST3",
    "/Library/Application Support/Avid/Audio/Plug-Ins",
    "/Libraries",
    "~/Music",
]
EXTS = {
    "audio_lossless": {".wav",".aiff",".aif",".flac"},
    "audio_lossy": {".mp3",".m4a",".aac",".ogg"},
    "instruments": {".nki",".nkm",".nkc",".nkr",".nkx",".ncw",".nicnt"},
    "presets": {".preset",".bank",".bundle",".nks",".nis"},
    "plugins": {".component",".vst",".vst3",".aaxplugin"},
    "docs": {".pdf"},
}
ALL_EXTS = set().union(*EXTS.values())
OUT_CSV = "noizyfish_ultrascan.csv"
OUT_YAML = "noizyfish_ultrascan.yaml"

# --- Helpers ---
def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    try:
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
    return {
        "category": categorize(ext),
        "path": str(p),
        "name": p.name,
        "ext": ext,
        "size_bytes": size,
        "checksum": sha256_file(p),
        "volume": p.anchor or p.parts[0],
    }

def list_roots(extra):
    roots = []
    for r in COMMON_ROOTS:
        rp = Path(r).expanduser().resolve()
        if rp.exists(): roots.append(rp)
    vols = Path("/Volumes")
    if vols.exists():
        roots += [v for v in vols.iterdir() if v.is_dir()]
    for r in extra:
        rp = Path(r).expanduser().resolve()
        if rp.exists(): roots.append(rp)
    return list({str(p):p for p in roots}.values())

# --- Main ---
def main():
    extra = sys.argv[1:]
    roots = list_roots(extra)
    print(f"Scanning {len(roots)} roots with {MAX_WORKERS} agents…")

    files = []
    for root in roots:
        try:
            for p in root.rglob("*"):
                if p.is_file() and p.suffix.lower() in ALL_EXTS:
                    files.append(p)
        except Exception: continue
    print(f"Candidate files: {len(files)}")

    results = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futs = [ex.submit(scan_file, p) for p in files]
        for f in as_completed(futs):
            rec = f.result()
            if rec: results.append(rec)

    uniq = {}
    for r in results:
        key = r["checksum"] or f"path:{r['path']}"
        prev = uniq.get(key)
        if not prev or (r["category"]=="instruments" and prev["category"]!="instruments"):
            uniq[key] = r
    rows = list(uniq.values())
    print(f"Unique items: {len(rows)}")

    headers = ["category","path","name","ext","size_bytes","checksum","volume"]
    with open(OUT_CSV,"w",newline="") as f:
        w=csv.DictWriter(f,fieldnames=headers); w.writeheader(); w.writerows(rows)
    Path(OUT_YAML).write_text(yaml.safe_dump(
        {"generated": datetime.utcnow().isoformat(),"items":rows}, sort_keys=False
    ))

    # Summary
    cats = {}
    for r in rows: cats[r["category"]] = cats.get(r["category"],0)+1
    print("Summary:")
    for c,n in cats.items(): print(f"  {c}: {n}")
    print(f"Exported {OUT_CSV}, {OUT_YAML}")

if __name__=="__main__":
    main()

python utilities/noizyfish_omnifinder.py scan --pdf-keywords RBC "Invoice"
python utilities/noizyfish_omnifinder.py plan --base /Libraries
python utilities/noizyfish_omnifinder.py ignite --base /Libraries

