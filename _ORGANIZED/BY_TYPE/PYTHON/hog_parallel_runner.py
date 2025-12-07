#!/usr/bin/env python3
import os
import sys
import json
import time
import argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from datetime import datetime
import importlib.util

# Paths
HOME = Path.home()
KONTAKT_LAB = HOME / "Desktop" / "KONTAKT_LAB"
REPORTS = KONTAKT_LAB / "REPORTS"
REPORTS.mkdir(parents=True, exist_ok=True)
TS = datetime.now().strftime('%Y%m%d_%H%M%S')
LOG = REPORTS / f"HOG_PARALLEL_{TS}.log"

# External script path (original Hand of God)
HOG_PATH = Path("/Users/rsp_ms/NoizyFish_Aquarium/🐍 Python_Projects/file_management/hand_of_god_search_fixed.py")
if not HOG_PATH.exists():
    print(f"[ERROR] Cannot find original script at {HOG_PATH}")
    sys.exit(1)

# Dynamically import hand_of_god_search_fixed as module
spec = importlib.util.spec_from_file_location("hand_of_god_search_fixed", str(HOG_PATH))
hog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hog)  # type: ignore

# Mirror search paths defined in the original script
SEARCH_VOLUMES = [
    HOME / "Desktop",
    HOME / "Documents",
    HOME / "Downloads",
    HOME / "Music",
    Path("/Volumes"),
    Path("/Users/Shared"),
    HOME / "Library" / "Audio",
    HOME / "NoizyGenie_Master_Workspace",
]
DIVINE_SEARCH_PATHS = [
    "/Applications/Native Instruments",
    "/Library/Audio",
    "/System/Library/Audio",
    HOME / "Desktop" / "SAMPLE_ARCHIVES",
    HOME / "Desktop" / "BACKUP",
    HOME / "Desktop" / "ORGANIZED_LIBRARIES",
]

# Exclusions to avoid scanning our working/recovery areas
NOISY_PATHS = [
    str(KONTAKT_LAB / "REPORTS"),
    str(KONTAKT_LAB / "REPORTS" / "REHOMING_"),
    str(HOME / "NoizyFish_VAULT"),
]

# Monkey-patch original module to reduce noise and exclude paths in backup search
def _is_noisy(p: str) -> bool:
    try:
        p = str(p)
        return any(p.startswith(ex) for ex in NOISY_PATHS)
    except Exception:
        return False

# Override original module's search path lists to our filtered versions
_orig_search_vols = getattr(hog, 'SEARCH_VOLUMES', [])
_orig_divine_paths = getattr(hog, 'DIVINE_SEARCH_PATHS', [])
_filtered_search_vols = []
for v in _orig_search_vols:
    try:
        vp = Path(v)
        if vp.exists() and not _is_noisy(str(vp)) and vp.resolve() != KONTAKT_LAB.resolve():
            _filtered_search_vols.append(vp)
    except Exception:
        continue
hog.SEARCH_VOLUMES = _filtered_search_vols

_filtered_divine_paths = []
for v in _orig_divine_paths:
    try:
        vp = Path(v)
        # Strings like '/Library/Audio' will be Path constructed fine
        if vp.exists() and not _is_noisy(str(vp)):
            _filtered_divine_paths.append(str(vp))
    except Exception:
        continue
hog.DIVINE_SEARCH_PATHS = _filtered_divine_paths

# Wrap search_library_backups to suppress logs and filter out noisy matches
_orig_backup = hog.HandOfGodSearcher.search_library_backups
def _quiet_backup(self, lib_name):
    # Temporarily silence divine_log
    orig_log = getattr(self, 'divine_log', None)
    try:
        if orig_log:
            self.divine_log = lambda *a, **k: None  # no-op
        results = _orig_backup(self, lib_name)
    finally:
        if orig_log:
            self.divine_log = orig_log
    # Filter noisy results
    filtered = []
    for b in results:
        bl = str(b)
        if _is_noisy(bl):
            continue
        filtered.append(b)
    return filtered

hog.HandOfGodSearcher.search_library_backups = _quiet_backup


def analyze_library(lib_name: str, lib_data: dict) -> tuple[str, dict]:
    s = hog.HandOfGodSearcher()
    lib_path = Path(lib_data["path"]) if isinstance(lib_data.get("path"), str) else Path(lib_data.get("path", ""))
    analysis = s.analyze_broken_library(lib_path)
    backups = s.search_library_backups(lib_name)
    # Filter out noisy backup locations (our own safety/report folders)
    filtered = []
    for b in backups:
        bl = str(b)
        if any(bl.startswith(ex) for ex in NOISY_PATHS):
            continue
        filtered.append(b)
    analysis["backup_locations"] = filtered
    return lib_name, analysis


def search_one_volume(volume: str | Path, targets: list[str]) -> dict:
    s = hog.HandOfGodSearcher()
    return s.divine_search_volume(Path(volume), targets)


def main():
    ap = argparse.ArgumentParser(description="Hand of God Parallel Runner")
    ap.add_argument("--workers", type=int, default=8, help="Number of parallel workers")
    ap.add_argument("--limit-volumes", type=int, default=0, help="Limit number of volumes to scan (0 = all)")
    args = ap.parse_args()

    start = time.time()
    with open(LOG, 'w') as lf:
        lf.write(f"HOG Parallel run at {TS} with {args.workers} workers\n")

    verification_file = KONTAKT_LAB / "REBUILD_VERIFICATION_REPORT.json"
    if not verification_file.exists():
        print(f"[WARN] No verification report at {verification_file}, falling back to emergency scan via original script.")
        # Call the original script main (non-parallel) as a fallback
        hog.main()
        return

    with open(verification_file, 'r') as f:
        verification_data = json.load(f)

    problematic_libs = {
        name: data for name, data in verification_data.items()
        if data.get("rebuild_status") in [
            "BROKEN", "PARTIAL_SAMPLES_MISSING", "PARTIAL_INSTRUMENTS_MISSING"
        ]
    }
    print(f"[INFO] Libraries needing intervention: {len(problematic_libs)}")

    # Analyze libraries in parallel (threads are fine: heavy IO)
    search_results: dict[str, dict] = {}
    all_missing_samples: list[str] = []

    with ThreadPoolExecutor(max_workers=args.workers) as tpe:
        futs = [tpe.submit(analyze_library, ln, ld) for ln, ld in problematic_libs.items()]
        for fut in as_completed(futs):
            lib_name, analysis = fut.result()
            search_results[lib_name] = analysis
            all_missing_samples.extend(analysis.get("missing_samples", []))

    unique_missing = sorted(set(all_missing_samples))
    print(f"[INFO] Unique missing samples: {len(unique_missing)}")

    # Build volume list
    volumes: list[Path] = []
    for v in SEARCH_VOLUMES + [Path(p) for p in DIVINE_SEARCH_PATHS]:
        pv = Path(v)
        if pv.exists():
            # Skip noisy paths such as our reports/safety/recovery vault
            pv_str = str(pv)
            if any(pv_str.startswith(ex) for ex in NOISY_PATHS):
                continue
            # Avoid scanning KONTAKT_LAB itself as a volume
            try:
                if pv.resolve() == KONTAKT_LAB.resolve():
                    continue
            except Exception:
                pass
            volumes.append(pv)
    if args.limit_volumes > 0:
        volumes = volumes[: args.limit_volumes]
    print(f"[INFO] Volumes to scan: {len(volumes)}")

    # Search volumes in parallel processes (avoid GIL)
    found_samples: dict[str, list[str]] = {}
    with ProcessPoolExecutor(max_workers=args.workers) as ppe:
        futs = {ppe.submit(search_one_volume, v, unique_missing): v for v in volumes}
        for fut in as_completed(futs):
            vol = futs[fut]
            try:
                res = fut.result()
                for sample, locs in res.items():
                    found_samples.setdefault(sample, []).extend(locs)
            except Exception as e:
                print(f"[WARN] Volume {vol} failed: {e}")

    # Process found samples serially to avoid copy collisions
    recovery_count = 0
    processor = hog.HandOfGodSearcher()
    for sample, locations in found_samples.items():
        # Determine which library this sample belongs to
        for lib_name, analysis in search_results.items():
            if sample in analysis.get("missing_samples", []):
                for loc in locations:
                    try:
                        if processor.process_found_sample(sample, loc, lib_name):
                            recovery_count += 1
                    except Exception:
                        pass
                break

    # Generate divine report using original reporter
    processor.generate_divine_report(search_results, found_samples, recovery_count)

    dur = time.time() - start
    print(f"[DONE] Parallel Hand of God run completed in {dur/60:.1f} min. Recovery: {recovery_count}")


if __name__ == "__main__":
    main()
