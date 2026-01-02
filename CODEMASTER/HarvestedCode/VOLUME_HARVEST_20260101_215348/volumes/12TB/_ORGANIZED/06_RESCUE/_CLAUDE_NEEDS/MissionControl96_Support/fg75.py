#!/usr/bin/env python3
import os
import sys
import csv
import json
import hashlib
import time
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

# Configuration
HOME = Path.home()
KONTAKT_LAB = HOME / "Desktop" / "KONTAKT_LAB"
REPORTS = KONTAKT_LAB / "REPORTS"
REPORTS.mkdir(parents=True, exist_ok=True)
TS = datetime.now().strftime("%Y%m%d_%H%M%S")
CSV_PATH = REPORTS / f"ORIGINAL_HOMES_MAP_{TS}.csv"
JSON_PATH = REPORTS / f"ORIGINAL_HOMES_MAP_{TS}.json"
LOG_PATH = REPORTS / f"ORIGINAL_HOMES_MAP_{TS}.log"

# Likely source roots to search (exclude KONTAKT_LAB itself)
SEARCH_ROOTS = [
    HOME / "Desktop",
    HOME / "Documents",
    HOME / "Downloads",
    HOME / "Music",
    HOME / "Library" / "Audio",
    Path("/Library/Audio"),
    Path("/Users/Shared"),
    Path("/Applications/Native Instruments"),
    Path("/Library/Application Support"),
    Path("/Volumes"),  # external drives
]

# Optional: ignore very large files for hashing beyond this (bytes). Hash on demand only.
HASH_LIMIT = 200 * 1024 * 1024  # 200 MB


def sha1(path: Path, chunk_size: int = 2**20) -> str:
    h = hashlib.sha1()
    with open(path, 'rb') as f:
        while True:
            b = f.read(chunk_size)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def safe_stat(p: Path):
    try:
        st = p.stat()
        return st.st_size, int(st.st_mtime)
    except Exception:
        return None


def walk_filtered(root: Path, allowed_names: set):
    # Walk root, but only yield files whose basename is in allowed_names
    # Skip KONTAKT_LAB subtree
    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        try:
            # Prune KONTAKT_LAB if encountered
            if str(KONTAKT_LAB) == dirpath or dirpath.startswith(str(KONTAKT_LAB) + os.sep):
                dirnames[:] = []
                continue
        except Exception:
            pass
        for fn in filenames:
            if fn in allowed_names:
                yield Path(dirpath) / fn


def build_kontakt_file_list(base: Path) -> List[Path]:
    files = []
    for dirpath, dirnames, filenames in os.walk(base, followlinks=False):
        for fn in filenames:
            p = Path(dirpath) / fn
            files.append(p)
    return files


def main():
    if not KONTAKT_LAB.exists():
        print(f"[ERROR] KONTAKT_LAB not found at {KONTAKT_LAB}")
        sys.exit(1)

    print(f"[INFO] Building file list from {KONTAKT_LAB} ...")
    files = build_kontakt_file_list(KONTAKT_LAB)
    names_set = {p.name for p in files}
    print(f"[INFO] Files to map: {len(files)} unique names: {len(names_set)}")

    # Build index: basename -> list of candidates ({path,size,mtime})
    index: Dict[str, List[Dict]] = {}

    def add_candidate(p: Path):
        st = safe_stat(p)
        if not st:
            return
        size, mtime = st
        entry = {"path": str(p), "size": size, "mtime": mtime}
        index.setdefault(p.name, []).append(entry)

    # Scan search roots
    start = time.time()
    scanned_dirs = 0
    print("[INFO] Scanning likely source roots for candidates ...")
    for root in SEARCH_ROOTS:
        if not root.exists():
            continue
        try:
            for p in walk_filtered(root, names_set):
                add_candidate(p)
            scanned_dirs += 1
            if scanned_dirs % 2 == 0:
                print(f"[PROGRESS] Scanned {scanned_dirs} roots so far ...")
        except PermissionError:
            continue
        except Exception as e:
            print(f"[WARN] Error scanning {root}: {e}")

    print(f"[INFO] Index built in {time.time()-start:.1f}s. Names indexed: {len(index)}")

    results = []
    unresolved = 0

    # Prepare CSV
    with open(CSV_PATH, 'w', newline='') as fcsv, open(LOG_PATH, 'w') as flog:
        writer = csv.writer(fcsv)
        writer.writerow([
            'current_path','filename','size','mtime','candidates','best_original','match_method','notes'
        ])

        for i, cur in enumerate(files, 1):
            st = safe_stat(cur)
            if not st:
                writer.writerow([str(cur), cur.name, '', '', 0, '', 'stat_error', ''])
                continue
            csize, cmtime = st
            cands = index.get(cur.name, [])
            best_path = ''
            method = 'none'
            notes = ''

            # Filter by exact size first
            same_size = [c for c in cands if c['size'] == csize]

            if not cands:
                unresolved += 1
                notes = 'no_name_match'
            elif same_size:
                # Try mtime proximity
                same_size_sorted = sorted(same_size, key=lambda c: abs(c['mtime'] - cmtime))
                best = same_size_sorted[0]
                best_path = best['path']
                method = 'size+mtime'

                # If multiple with identical size and close mtime, confirm by hash (only if file <= HASH_LIMIT)
                if len(same_size_sorted) > 1 and csize <= HASH_LIMIT:
                    try:
                        cur_hash = sha1(cur)
                        for cand in same_size_sorted[:5]:
                            cp = Path(cand['path'])
                            try:
                                if sha1(cp) == cur_hash:
                                    best_path = str(cp)
                                    method = 'size+hash'
                                    break
                            except Exception:
                                continue
                    except Exception:
                        pass
            else:
                # No exact size match; fallback heuristic: substring path hints (Native Instruments, Kontakt, etc.)
                hints = ['native instruments','kontakt','library','samples','eastwest','spitfire','komplete','masch']
                scored = []
                for c in cands:
                    score = 0
                    pl = c['path'].lower()
                    for h in hints:
                        if h in pl:
                            score += 1
                    # prefer paths outside KONTAKT_LAB and under typical shared locations
                    if '/users/shared' in pl or '/library/audio' in pl:
                        score += 1
                    # prefer similar directory name to current parent
                    try:
                        parent_name = cur.parent.name.lower()
                        if parent_name and parent_name in pl:
                            score += 1
                    except Exception:
                        pass
                    scored.append((score, c))
                if scored:
                    scored.sort(key=lambda x: (-x[0], abs(x[1]['mtime'] - cmtime)))
                    best = scored[0][1]
                    best_path = best['path']
                    method = 'name+heuristic'
                else:
                    unresolved += 1
                    notes = 'no_size_match'

            writer.writerow([
                str(cur), cur.name, csize, cmtime, len(cands), best_path, method, notes
            ])
            results.append({
                'current_path': str(cur),
                'filename': cur.name,
                'size': csize,
                'mtime': cmtime,
                'candidates': len(cands),
                'best_original': best_path,
                'match_method': method,
                'notes': notes
            })

            if i % 500 == 0:
                print(f"[PROGRESS] Processed {i} files ...")

    with open(JSON_PATH, 'w') as fj:
        json.dump({'generated_at': TS, 'kontakt_lab': str(KONTAKT_LAB), 'results': results}, fj, indent=2)

    resolved = len(results) - unresolved
    print(f"[DONE] Original homes mapping complete. Total: {len(results)}, Resolved: {resolved}, Unresolved: {unresolved}")
    print(f"[REPORT] CSV: {CSV_PATH}")
    print(f"[REPORT] JSON: {JSON_PATH}")
    print(f"[LOG] {LOG_PATH}")


if __name__ == '__main__':
    main()
