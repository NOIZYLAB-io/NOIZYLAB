#!/usr/bin/env python3
# filepath: ultimate_ni_consolidation_and_cleanup.py
# NOIZYGENIE: Complete NI Consolidation + Empty Folder Cleanup + 96 Seals Protocol

import csv
import json
import os
import shutil
import time
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from typing import Dict, List, Tuple

print("🧙‍♂️ NOIZYGENIE: ULTIMATE CONSOLIDATION PROTOCOL")
print("⚡ NI Deep Scan + 96 Seals + Empty Folder Cleanup")
print("🔥" * 80)

# PATHS AND CONFIGURATION
SOURCE = Path("/Volumes/6TB/Native Instruments")
KONTAKT_LAB = Path("/Users/rsp_ms/Desktop/KONTAKT_LAB")
DEST_VENDOR_ROOT = Path("/Volumes/6TB/_NI_2026/LIBRARIES")
SAFETY_ROOT = Path("/Volumes/6TB/_NI_2026/SAFETY")
REPORTS_BASE = Path("/Users/rsp_ms/Desktop/KONTAKT_LAB/REPORTS/DEEP")

# Create all necessary directories
for path in [DEST_VENDOR_ROOT, SAFETY_ROOT, REPORTS_BASE]:
    path.mkdir(parents=True, exist_ok=True)

# EXTENSION DEFINITIONS
INSTRUMENT_EXT = {".nki", ".nkm"}
AUDIO_EXT = {".wav", ".aif", ".aiff", ".ncw"}
MONOLITH_EXT = {".nkx", ".nks", ".nkb", ".nksn", ".nkc", ".nkr"}
DOC_EXT = {".pdf", ".txt", ".rtf"}
IMG_EXT = {".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff"}
IGNORED_NAMES = {".DS_Store", "Thumbs.db"}

# VENDOR HINTS
VENDOR_HINTS = {
    "Cinesamples": "Cinesamples",
    "Audiobro": "Audiobro", 
    "8Dio": "8Dio",
    "8Dio Libraries": "8Dio",
    "Best Service": "Best Service",
    "Project Sam": "ProjectSAM",
    "Spitfire Audio": "Spitfire Audio",
    "Soundiron": "Soundiron",
    "Output": "Output",
    "Heavyocity": "Heavyocity",
    "EastWest": "EastWest",
    "BOOM Libraries Final 2025": "BOOM Library",
}

# THE 96 SEALS MATRIX
SEALS_MATRIX = {
    "01_ORCHESTRAL": ["02_ORCHESTRAL", "03_ACOUSTIC", "Celli", "Violin", "Viola", "STRINGS", "Aleatoric"],
    "02_ETHNIC_WORLD": ["06_WORLD_ETHNIC", "ERHU", "CHINA_SETS", "MID_EAST", "BANSURI", "DIGERIDOO", "CEYLON", "EGYPTIAN"],
    "03_WINDS": ["BAWU", "HOTCHIKU", "HULUSI", "KENA", "SHAKUHACHI", "SHAWN", "SHENAI", "SHENG", "WHISTLE", "CIARAMELLA", "DOUCAINE", "MANCOSEDDA"],
    "04_STRINGS": ["RENAISSANCE_LUTE", "CUMBUS", "TANBUR", "SAZ", "TIMPLE", "Lutes", "Reeds"],
    "05_ELECTRONIC": ["01_ELECTRONIC", "07_SYNTHESIZERS", "Industrial", "Evolve"],
    "06_DRUMS": ["08_DRUMS_PERCUSSION", "CLAPS", "BELLTREE", "CASTANETS", "CUICA", "TAMBORCITO", "GLASSES"],
    "07_KEYBOARDS": ["Scarbee", "HARMONIUM"],
    "08_VOCALS": ["11_VOCALS", "HUMAN_WHISTLING", "ALPINE_JODELING", "Spitfire"],
    "09_LOOPS": ["09_LOOPS_GROOVES", "12_CONSTRUCTION", "13_MULTIS", "Discolicks", "Runs_", "SawTooth", "Wavy", "Slow_"],
    "10_SOUNDSCAPES": ["10_SOUNDSCAPES_FX", "Quirky", "Cinescapes"],
    "11_FACTORY": ["Kontakt_Factory", "Native_Instruments_2026", "KONTAKT_LAB_2026", "NI2026"],
    "12_SYSTEM": ["_FIX", "_NKI", "_Staccato", "_TWEAKABLE", "BACKUP", "Data", "REPORTS", "PY_Scripts", "TEMP", "SAMPLE_ARCHIVES", "ORGANIZED", "Auxiliary", "Lite_Patches", "Excerpts"],
    "13_DOCS": [".txt", ".html", ".json", "LOG", "MASTER", "REPAIR", "MIGRATION"]
}

def collapse_spaces(s: str) -> str:
    return " ".join(str(s).replace("\u00A0", " ").split())

def add_library_suffix(name: str) -> str:
    nl = name.lower()
    return name if nl.endswith(" library") or nl.endswith(" libraries") else f"{name} Library"

def human_bytes(n: int) -> str:
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if n < 1024.0:
            return f"{n:3.1f} {unit}"
        n /= 1024.0
    return f"{n:.1f} PB"

def infer_vendor_from_path(p: Path, default: str) -> str:
    for part in p.parts[::-1]:
        if part in VENDOR_HINTS:
            return VENDOR_HINTS[part]
        if part.lower().endswith(" libraries"):
            return collapse_spaces(part[:-10])
    return default

def parse_nicnt(lib: Path) -> Dict[str, str]:
    info: Dict[str, str] = {}
    try:
        nicnts = list(lib.rglob("*.nicnt"))
        if not nicnts:
            return info
        nicnt = sorted(nicnts, key=lambda p: len(p.parts))[0]
        try:
            tree = ET.parse(nicnt)
            root = tree.getroot()
            for tag in ("SNPID", "Name", "name", "Company", "company", "RegKey", "regkey"):
                el = root.find(f".//{tag}")
                if el is not None and el.text:
                    info[tag.capitalize()] = el.text.strip()
            info["NicntPath"] = str(nicnt)
        except Exception:
            info["NicntPath"] = str(nicnt)
    except Exception:
        pass
    return info

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
        "monoliths": 0,
        "monolith_bytes": 0,
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
        if root_p.name.lower() == "snapshots":
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
                elif ext in MONOLITH_EXT:
                    meta["monoliths"] += 1
                    meta["monolith_bytes"] += st.st_size
                elif ext in DOC_EXT:
                    meta["docs"] += 1
                elif ext in IMG_EXT:
                    meta["images"] += 1
            except Exception:
                pass

    # Completeness check
    complete_reasons = []
    if meta["zero_bytes"] > 0:
        complete_reasons.append("zero_bytes")
    if meta["broken_symlinks"] > 0:
        complete_reasons.append("broken_symlinks")
    if (meta["nki"] + meta["nkm"]) < 1:
        complete_reasons.append("no_instruments")
    
    has_monoliths = meta.get("monoliths", 0) > 0
    has_nicnt = bool(meta.get("nicnt"))
    has_audio = meta.get("audio", 0) >= 1
    if not (has_audio or has_monoliths or has_nicnt):
        complete_reasons.append("no_samples_detected")
    
    complete = len(complete_reasons) == 0
    meta["incomplete_reasons"] = complete_reasons
    return complete, meta

def dir_has_instruments(p: Path) -> bool:
    for ext in INSTRUMENT_EXT:
        if any(p.rglob(f"*{ext}")):
            return True
    return False

def find_library_roots(base: Path, max_depth: int = 5) -> List[Path]:
    roots: List[Path] = []
    def depth(p: Path) -> int:
        try:
            return len(p.relative_to(base).parts)
        except Exception:
            return 0
    
    queue: List[Path] = [base]
    seen: set = set()
    
    while queue:
        curr = queue.pop(0)
        if curr in seen:
            continue
        seen.add(curr)
        if not curr.is_dir() or curr.name.startswith('.'):
            continue
        
        d = depth(curr)
        if d > 0:
            name = curr.name
            has_instr = dir_has_instruments(curr) or ((curr / "Instruments").exists() and dir_has_instruments(curr / "Instruments"))
            has_nicnt = any(curr.glob("*.nicnt"))
            has_monolith = any(curr.rglob("*" + ext) for ext in MONOLITH_EXT)
            
            if has_instr or has_nicnt or has_monolith or name.lower().endswith(" library"):
                roots.append(curr)
                continue
        
        if d < max_depth:
            try:
                for child in sorted(curr.iterdir(), key=lambda p: p.name.lower()):
                    if child.is_dir():
                        queue.append(child)
            except Exception:
                pass
    
    # Deduplicate
    roots = sorted(set(roots), key=lambda p: (len(p.parts), p.name.lower()))
    pruned: List[Path] = []
    for r in roots:
        if any(r != x and (str(r).startswith(str(x) + os.sep)) for x in pruned):
            continue
        pruned.append(r)
    return pruned

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

def apply_96_seals_to_kontakt_lab():
    """Apply the 96 Seals to KONTAKT_LAB contents"""
    print("\n🔥 APPLYING THE 96 SEALS TO KONTAKT_LAB...")
    print("─" * 80)
    
    destination = DEST_VENDOR_ROOT / "Native Instruments" / "COMPLETE"
    destination.mkdir(parents=True, exist_ok=True)
    
    # Create seal chambers
    for seal in SEALS_MATRIX:
        (destination / seal).mkdir(exist_ok=True)
    (destination / "99_MISC").mkdir(exist_ok=True)
    
    sealed_count = 0
    
    if not KONTAKT_LAB.exists():
        print("⚠️  KONTAKT_LAB not found, skipping 96 Seals...")
        return sealed_count
    
    for item in KONTAKT_LAB.iterdir():
        if not item.exists():
            continue
        
        sealed = False
        item_name = item.name
        
        # Apply seals
        for seal_name, patterns in SEALS_MATRIX.items():
            for pattern in patterns:
                if (pattern in item_name or 
                    item_name.startswith(pattern) or 
                    item_name.endswith(pattern) or
                    any(p in item_name for p in pattern.split("_"))):
                    
                    target = destination / seal_name / item_name
                    
                    # Handle conflicts
                    counter = 1
                    while target.exists():
                        stem = target.stem if target.suffix else target.name
                        suffix = target.suffix
                        target = target.parent / f"{stem}_COPY_{counter}{suffix}"
                        counter += 1
                    
                    try:
                        shutil.move(str(item), str(target))
                        sealed_count += 1
                        print(f"⚡ SEAL {sealed_count:03d}: {item_name} → {seal_name}")
                        sealed = True
                        break
                    except Exception as e:
                        print(f"❌ RESISTANCE: {item_name} - {e}")
            
            if sealed:
                break
        
        # Move unmatched to misc
        if not sealed and item.exists():
            target = destination / "99_MISC" / item_name
            counter = 1
            while target.exists():
                stem = target.stem if target.suffix else target.name
                suffix = target.suffix
                target = target.parent / f"{stem}_COPY_{counter}{suffix}"
                counter += 1
            
            try:
                shutil.move(str(item), str(target))
                sealed_count += 1
                print(f"📦 MISC {sealed_count:03d}: {item_name}")
            except Exception as e:
                print(f"❌ FINAL RESISTANCE: {item_name} - {e}")
    
    return sealed_count

def delete_empty_folders_all_volumes():
    """Delete empty folders across all volumes except protected directories"""
    print("\n🧹 CLEANING EMPTY FOLDERS ACROSS ALL VOLUMES...")
    print("─" * 80)
    
    # Protected directories
    protected_dirs = {
        "Mission Control", "System", "Library", "Applications", 
        "usr", "bin", "sbin", "etc", "var", "tmp", "dev", "proc",
        ".Spotlight-V100", ".fseventsd", ".TemporaryItems", ".Trashes", "lost+found"
    }
    
    volumes = []
    try:
        volumes_path = Path("/Volumes")
        if volumes_path.exists():
            volumes.extend([v for v in volumes_path.iterdir() if v.is_dir()])
        volumes.append(Path.home())
    except Exception as e:
        print(f"❌ Error detecting volumes: {e}")
    
    total_deleted = 0
    
    for volume in volumes:
        if not volume.exists() or not volume.is_dir():
            continue
        
        # Skip protected volumes
        if any(protected in str(volume) for protected in protected_dirs):
            continue
        
        volume_name = volume.name if volume.name else "Root"
        print(f"🔍 Scanning: {volume} ({volume_name})")
        
        deleted_count = 0
        try:
            for root, dirs, files in os.walk(volume, topdown=False):
                root_path = Path(root)
            for root, _, _ in os.walk(volume, topdown=False):
                root_path = Path(root)
                
                # Skip protected directories
                if any(protected in str(root_path) for protected in protected_dirs):
                    continue
                    if root_path.is_dir() and not any(root_path.iterdir()):
                        if (str(root_path) not in ["/", str(Path.home())] and 
                            not any(protected in str(root_path) for protected in protected_dirs)):
                            root_path.rmdir()
                            deleted_count += 1
                            total_deleted += 1
                except (PermissionError, OSError):
                    continue
        except (PermissionError, OSError):
            continue
        
        if deleted_count > 0:
            print(f"✅ {volume_name}: Deleted {deleted_count} empty folders")
    
    print(f"🎉 Empty folder cleanup complete! Deleted {total_deleted} folders")
    return total_deleted

def run_ni_deep_scan(execute: bool = True):
    """Run the NI Deep Scan and organization"""
    print("\n📊 RUNNING NI DEEP SCAN AND ORGANIZATION...")
    print("─" * 80)
    
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

    if not SOURCE.exists():
        print("⚠️  Source path not found, skipping NI Deep Scan...")
        return totals

    candidates = find_library_roots(SOURCE, max_depth=3)
    
    for entry in candidates:
        totals["examined"] += 1
        complete, meta = scan_library(entry)
        vendor = str(meta.get("vendor") or "Native Instruments").strip() or "Native Instruments"
        
        if vendor == "Native Instruments":
            vendor = infer_vendor_from_path(entry, vendor)
        
        lib_name = collapse_spaces(meta["name"])
        if lib_name.lower().endswith(" library") is False and (meta["nki"] + meta["nkm"]) >= 1:
            lib_name = add_library_suffix(lib_name)
        
        status = "COMPLETE" if complete else "PARTIAL"
        dest_dir = DEST_VENDOR_ROOT / vendor / status / lib_name
        
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
                if not complete:
                    totals["bytes"] += int(meta["bytes"]) if isinstance(meta["bytes"], int) else 0
            elif action == "collision_parked":
                totals["collision_parked"] += 1

        # Prepare row data
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
            "status": status,
            "incomplete_reasons": ";".join(meta.get("incomplete_reasons", [])),
            "action": action,
            "dest": final_path,
        })
        
        print(f"📦 {entry.name}: {status} - {action}")

    # Write reports
    if rows:
        with csv_path.open('w', newline='') as f:
            cols = list(rows[0].keys())
            writer = csv.DictWriter(f, fieldnames=cols)
            writer.writeheader()
            writer.writerows(rows)
    
    with json_path.open('w') as f:
        json.dump({"totals": totals, "items": rows}, f, indent=2)

    print(f"📄 Reports saved: {csv_path}, {json_path}")
    return totals

def main():
    """Execute all protocols"""
    start_time = time.time()
    
    print("🚀 STARTING ULTIMATE NOIZYGENIE PROTOCOL...")
    
    # 1. Run NI Deep Scan and Organization
    ni_totals = run_ni_deep_scan(execute=True)
    
    # 2. Apply 96 Seals to KONTAKT_LAB
    sealed_count = apply_96_seals_to_kontakt_lab()
    
    # 3. Delete empty folders
    deleted_folders = delete_empty_folders_all_volumes()
    
    # Final report
    elapsed = time.time() - start_time
    
    print("\n" + "🎉" * 80)
    print("🧙‍♂️ NOIZYGENIE ULTIMATE PROTOCOL COMPLETE!")
    print("🎉" * 80)
    print(f"⏱️  Total Time: {elapsed:.1f} seconds")
    print(f"📊 NI Libraries Processed: {ni_totals.get('examined', 0)}")
    print(f"✅ Complete Libraries: {ni_totals.get('complete', 0)}")
    print(f"📦 Libraries Moved: {ni_totals.get('moved', 0)}")
    print(f"⚡ 96 Seals Applied: {sealed_count}")
    print(f"🧹 Empty Folders Deleted: {deleted_folders}")
    print(f"💾 Total Data: {human_bytes(ni_totals.get('bytes', 0))}")
    print("\n🌟 ALL PROTOCOLS EXECUTED SUCCESSFULLY!")
    print("🏆 ULTIMATE CONSOLIDATION ACHIEVED!")

if __name__ == "__main__":
    main()
