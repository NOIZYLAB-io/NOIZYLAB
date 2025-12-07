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


HOME = Path.home()
REPORTS = HOME / "Desktop" / "KONTAKT_LAB" / "REPORTS"
REPORTS.mkdir(parents=True, exist_ok=True)
TS = datetime.now().strftime('%Y%m%d_%H%M%S')
LOG = REPORTS / f"HOG_TARGETED_{TS}.log"
DEST_VENDOR_ROOT = Path("/Volumes/6TB/_NI_2026/LIBRARIES")

# Hand of God script path
HOG_PATH = Path("/Users/rsp_ms/NoizyFish_Aquarium/🐍 Python_Projects/file_management/hand_of_god_search_fixed.py")
if not HOG_PATH.exists():
    print(f"[ERROR] Cannot find original script at {HOG_PATH}")
    sys.exit(1)

# Import the original script as a module
spec = importlib.util.spec_from_file_location("hand_of_god_search_fixed", str(HOG_PATH))
hog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hog)  # type: ignore

# Reuse/override search roots from the original script with filtering
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

NOISY_PATHS = [
    str(HOME / "Desktop" / "KONTAKT_LAB" / "REPORTS"),
    str(HOME / "NoizyFish_VAULT"),
    str(Path("/Volumes/6TB/_NI_2026/SAFETY")),
]

def _is_noisy(p: str) -> bool:
    try:
        p = str(p)
        return any(p.startswith(ex) for ex in NOISY_PATHS)
    except Exception:
        return False

# Patch the module's search roots
_orig_search_vols = getattr(hog, 'SEARCH_VOLUMES', [])
_orig_divine_paths = getattr(hog, 'DIVINE_SEARCH_PATHS', [])
_filtered_search_vols = []
for v in _orig_search_vols:
    try:
        vp = Path(v)
        if vp.exists() and not _is_noisy(str(vp)):
            _filtered_search_vols.append(vp)
    except Exception:
        continue
hog.SEARCH_VOLUMES = _filtered_search_vols or SEARCH_VOLUMES

_filtered_divine_paths = []
for v in _orig_divine_paths:
    try:
        vp = Path(v)
        if vp.exists() and not _is_noisy(str(vp)):
            _filtered_divine_paths.append(str(vp))
    except Exception:
        continue
hog.DIVINE_SEARCH_PATHS = _filtered_divine_paths or [str(p) for p in DIVINE_SEARCH_PATHS]

# Silence backup search spam and filter results
_orig_backup = hog.HandOfGodSearcher.search_library_backups
def _quiet_backup(self, lib_name):
    orig_log = getattr(self, 'divine_log', None)
    try:
        if orig_log:
            self.divine_log = lambda *a, **k: None
        res = _orig_backup(self, lib_name)
    finally:
        if orig_log:
            self.divine_log = orig_log
    return [b for b in res if not _is_noisy(str(b))]
hog.HandOfGodSearcher.search_library_backups = _quiet_backup


def analyze_library(lib_name: str, lib_root: Path) -> tuple[str, dict]:
    s = hog.HandOfGodSearcher()
    analysis = s.analyze_broken_library(lib_root)
    backups = s.search_library_backups(lib_name)
    analysis["backup_locations"] = [b for b in backups if not _is_noisy(str(b))]
    return lib_name, analysis


def search_one_volume(volume: str | Path, targets: list[str]) -> dict:
    s = hog.HandOfGodSearcher()
    return s.divine_search_volume(Path(volume), targets)


def load_partial_targets(deep_reports_dir: Path | None) -> dict[str, Path]:
    # Locate latest deep scan if not provided
    base = deep_reports_dir or (REPORTS / "DEEP")
    candidates = sorted(base.glob("NI_DEEP_*"))
    if not candidates:
        raise RuntimeError(f"No deep-scan reports found under {base}")
    latest = candidates[-1]
    with open(latest / "summary.json", 'r') as f:
        d = json.load(f)
    targets: dict[str, Path] = {}
    for item in d.get("items", []):
        if item.get("complete"):
            continue
        name = item.get("name") or Path(item.get("path", "")).name
        # Try original path
        p = Path(item.get("path", ""))
        if p.exists():
            targets[name] = p
            continue
        # Try report 'dest'
        dest = item.get("dest") or ""
        if dest:
            dp = Path(dest)
            if dp.exists():
                targets[name] = dp
                continue
        # Reconstruct from vendor/status/name under _NI_2026
        vendor = (item.get("vendor") or "Native Instruments").strip() or "Native Instruments"
        status = item.get("status") or ("PARTIAL" if not item.get("complete") else "COMPLETE")
        lib_name = name
        guess = DEST_VENDOR_ROOT / vendor / status / lib_name
        if guess.exists():
            targets[name] = guess
    return targets


def main():
    ap = argparse.ArgumentParser(description="Hand of God Targeted Repair for PARTIAL libraries")
    ap.add_argument("--workers", type=int, default=32)
    ap.add_argument("--limit-volumes", type=int, default=0)
    ap.add_argument("--deep-reports", type=str, default="")
    args = ap.parse_args()

    deep_dir = Path(args.deep_reports) if args.deep_reports else None
    targets = load_partial_targets(deep_dir)
    print(f"[INFO] PARTIAL libraries targeted: {len(targets)}")
    if not targets:
        print("[DONE] No partial libraries to repair.")
        return

    start = time.time()
    with open(LOG, 'w') as lf:
        lf.write(f"HOG Targeted run at {TS} with {args.workers} workers\n")

    # Analyze in parallel
    search_results: dict[str, dict] = {}
    all_missing: list[str] = []
    with ThreadPoolExecutor(max_workers=args.workers) as tpe:
        futs = [tpe.submit(analyze_library, name, root) for name, root in targets.items()]
        for fut in as_completed(futs):
            name, analysis = fut.result()
            search_results[name] = analysis
            all_missing.extend(analysis.get("missing_samples", []))

    unique_missing = sorted(set(all_missing))
    print(f"[INFO] Unique missing samples: {len(unique_missing)}")
    if not unique_missing:
        print("[DONE] Nothing missing; exiting.")
        return

    # Build volumes to scan
    volumes: list[Path] = []
    for v in hog.SEARCH_VOLUMES + [Path(p) for p in hog.DIVINE_SEARCH_PATHS]:
        pv = Path(v)
        if pv.exists():
            pv_str = str(pv)
            if any(pv_str.startswith(ex) for ex in NOISY_PATHS):
                continue
            volumes.append(pv)
    if args.limit_volumes:
        volumes = volumes[: args.limit_volumes]
    print(f"[INFO] Volumes to scan: {len(volumes)}")

    # Volume search in processes
    found: dict[str, list[str]] = {}
    with ProcessPoolExecutor(max_workers=args.workers) as ppe:
        futs = {ppe.submit(search_one_volume, v, unique_missing): v for v in volumes}
        for fut in as_completed(futs):
            vol = futs[fut]
            try:
                res = fut.result()
                for sample, locs in res.items():
                    found.setdefault(sample, []).extend(locs)
            except Exception as e:
                print(f"[WARN] Volume {vol} failed: {e}")

    # Process found samples serially
    processor = hog.HandOfGodSearcher()
    recovery_count = 0
    for sample, locs in found.items():
        # Map back to library
        for lib_name, analysis in search_results.items():
            if sample in analysis.get("missing_samples", []):
                for loc in locs:
                    try:
                        if processor.process_found_sample(sample, loc, lib_name):
                            recovery_count += 1
                    except Exception:
                        pass
                break

    processor.generate_divine_report(search_results, found, recovery_count)
    dur = time.time() - start
    print(f"[DONE] Targeted repair complete in {dur/60:.1f} min. Recovered: {recovery_count}")


if __name__ == "__main__":
    main()
