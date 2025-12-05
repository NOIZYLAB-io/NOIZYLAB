#!/usr/bin/env python3
import os
import sys
import json
import csv
import shutil
from pathlib import Path
from datetime import datetime
import hashlib

HOME = Path.home()
KONTAKT_LAB = HOME / "Desktop" / "KONTAKT_LAB"
REPORTS = KONTAKT_LAB / "REPORTS"
REPORTS.mkdir(parents=True, exist_ok=True)
TS = datetime.now().strftime('%Y%m%d_%H%M%S')
RUN_DIR = REPORTS / f"REHOMING_{TS}"
RUN_DIR.mkdir(parents=True, exist_ok=True)
SAFETY_DIR = RUN_DIR / "SAFETY"
SAFETY_DUPES = SAFETY_DIR / "DUPLICATES"
SAFETY_CONFLICTS = SAFETY_DIR / "CONFLICTS"
for d in (SAFETY_DIR, SAFETY_DUPES, SAFETY_CONFLICTS):
    d.mkdir(parents=True, exist_ok=True)

HASH_LIMIT = 200 * 1024 * 1024  # 200MB
TRUSTED_METHODS = {"size+hash", "size+mtime"}


def sha1(path: Path, chunk_size: int = 2**20) -> str:
    h = hashlib.sha1()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(chunk_size), b''):
            h.update(chunk)
    return h.hexdigest()


def latest_mapping_json() -> Path:
    cands = sorted([p for p in REPORTS.glob('ORIGINAL_HOMES_MAP_*.json')], key=lambda p: p.stat().st_mtime)
    if not cands:
        print("[ERROR] No mapping JSON found in REPORTS.")
        sys.exit(1)
    return cands[-1]


def rel_under_kontakt(p: Path) -> Path:
    try:
        return p.relative_to(KONTAKT_LAB)
    except Exception:
        return Path(p.name)


def safe_move(src: Path, dst: Path) -> str:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if not dst.exists():
        shutil.move(str(src), str(dst))
        return "moved"
    # destination exists; decide if duplicate or conflict
    try:
        same = False
        if src.stat().st_size == dst.stat().st_size:
            if src.stat().st_size <= HASH_LIMIT:
                same = (sha1(src) == sha1(dst))
            else:
                # Large file: approximate by size+mtime tolerance
                same = abs(int(src.stat().st_mtime) - int(dst.stat().st_mtime)) < 3
        if same:
            # keep destination as truth; move src copy to SAFETY_DUPES
            rel = rel_under_kontakt(src)
            safe_target = SAFETY_DUPES / rel
            safe_target.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(safe_target))
            return "duplicate_preserved"
    except Exception:
        pass
    # conflict — don't overwrite; move src to SAFETY_CONFLICTS with path structure
    rel = rel_under_kontakt(src)
    conflict_target = SAFETY_CONFLICTS / rel
    conflict_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(conflict_target))
    return "conflict_parked"


def main():
    mapping_path = latest_mapping_json()
    print(f"[INFO] Using mapping: {mapping_path}")
    with open(mapping_path) as f:
        data = json.load(f)
    results = data.get('results', [])

    # Prepare logs
    actions_csv = RUN_DIR / "rehoming_actions.csv"
    summary_txt = RUN_DIR / "summary.txt"

    counts = {"eligible": 0, "moved": 0, "duplicate_preserved": 0, "conflict_parked": 0, "skipped": 0, "missing_src": 0}

    with open(actions_csv, 'w', newline='') as fa:
        w = csv.writer(fa)
        w.writerow(["current_path","best_original","method","action","note"])
        for r in results:
            method = r.get('match_method','')
            if method not in TRUSTED_METHODS:
                counts["skipped"] += 1
                continue
            src = Path(r['current_path'])
            dst = Path(r.get('best_original') or '')
            if not dst:
                counts["skipped"] += 1
                continue
            if not src.exists():
                counts["missing_src"] += 1
                w.writerow([str(src), str(dst), method, "missing_src", ""])
                continue
            # If src already at destination, skip
            if src.resolve() == dst.resolve() if dst.exists() else False:
                counts["skipped"] += 1
                w.writerow([str(src), str(dst), method, "already_at_destination", ""])
                continue
            counts["eligible"] += 1
            try:
                action = safe_move(src, dst)
                counts[action] += 1
                w.writerow([str(src), str(dst), method, action, ""])
            except Exception as e:
                counts["skipped"] += 1
                w.writerow([str(src), str(dst), method, "error", str(e)])

    with open(summary_txt, 'w') as fs:
        fs.write(f"Rehoming run: {TS}\n")
        fs.write(f"Mapping: {mapping_path}\n")
        for k,v in counts.items():
            fs.write(f"{k}: {v}\n")
        fs.write(f"Actions CSV: {actions_csv}\n")
        fs.write(f"Safety dir: {SAFETY_DIR}\n")

    print("[DONE] Rehoming complete.")
    for k,v in counts.items():
        print(f"  {k}: {v}")
    print(f"[ACTIONS] {actions_csv}")
    print(f"[SAFETY] {SAFETY_DIR}")

if __name__ == '__main__':
    main()
