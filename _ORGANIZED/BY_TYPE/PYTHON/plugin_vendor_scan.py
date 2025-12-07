#!/usr/bin/env python3
import os
import re
import csv
import sys
import json
import plistlib
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List

HOME = Path.home()
REPORTS_DIR = HOME / "Desktop" / "KONTAKT_LAB" / "REPORTS"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)
TS = datetime.now().strftime("%Y%m%d_%H%M%S")
MASTER_CSV = REPORTS_DIR / f"PLUGIN_INVENTORY_ENRICHED_{TS}.csv"
SUMMARY_JSON = REPORTS_DIR / f"PLUGIN_INVENTORY_ENRICHED_{TS}.json"

PLUGIN_DIRS = [
    ("AU", "/Library/Audio/Plug-Ins/Components", ".component"),
    ("AU", str(HOME / "Library/Audio/Plug-Ins/Components"), ".component"),
    ("VST3", "/Library/Audio/Plug-Ins/VST3", ".vst3"),
    ("VST3", str(HOME / "Library/Audio/Plug-Ins/VST3"), ".vst3"),
    ("VST", "/Library/Audio/Plug-Ins/VST", ".vst"),
    ("VST", str(HOME / "Library/Audio/Plug-Ins/VST"), ".vst"),
    ("CLAP", "/Library/Audio/Plug-Ins/CLAP", ".clap"),
    ("CLAP", str(HOME / "Library/Audio/Plug-Ins/CLAP"), ".clap"),
    ("MAS", "/Library/Audio/Plug-Ins/MAS", None),
    ("MAS", str(HOME / "Library/Audio/Plug-Ins/MAS"), None),
    ("HAL", "/Library/Audio/Plug-Ins/HAL", None),
    ("HAL", str(HOME / "Library/Audio/Plug-Ins/HAL"), None),
    ("WPAPI", "/Library/Audio/Plug-Ins/WPAPI", None),
    ("WPAPI", str(HOME / "Library/Audio/Plug-Ins/WPAPI"), None),
    ("AAX", "/Library/Application Support/Avid/Audio/Plug-Ins", ".aaxplugin"),
    ("AAX", str(HOME / "Library/Application Support/Avid/Audio/Plug-Ins"), ".aaxplugin"),
]

# Vendor dictionary (patterns -> canonical vendor)
VENDOR_MAP = [
    (r"native\s*instruments|kontakt|reaktor|massive|fm8|absynth|battery|maschine|guitar\s*rig|monark|form|rounds|skanner|polyplex|replika|raum|phasis|choral|flair|driver", "Native Instruments"),
    (r"east\s*west|opus|play", "EastWest"),
    (r"spitfire", "Spitfire Audio"),
    (r"project\s*sam|projectsam", "ProjectSAM"),
    (r"sonokinetic|sonkinetic", "Sonokinetic"),
    (r"impact\s*soundworks", "Impact Soundworks"),
    (r"8dio", "8Dio"),
    (r"bolder\s*sounds", "Bolder Sounds"),
    (r"boom(\s*library|\s*libraries)?|boom\s*audio", "BOOM Library"),
    (r"cine\s*samples|cinesamples", "Cinesamples"),
    (r"output", "Output"),
    (r"heavyocity", "Heavyocity"),
    (r"kirk\s*hunter", "Kirk Hunter Studios"),
    (r"scarbee", "Scarbee"),
    (r"teletone", "Teletone Audio"),
    (r"big\s*fish\s*audio|bfa", "Big Fish Audio"),
    (r"vienna|vsl|vienna\s*symphonic\s*library", "Vienna Symphonic Library"),
    (r"u-he|uhe", "u-he"),
    (r"izotope", "iZotope"),
    (r"waves", "Waves"),
    (r"arturia", "Arturia"),
    (r"softube", "Softube"),
]

VENDOR_CANONICALS = [v for _, v in VENDOR_MAP]
REQUESTED_VENDORS = [
    "ProjectSAM","Sonokinetic","Impact Soundworks","8Dio","Bolder Sounds","BOOM Library",
    "Cinesamples","Output","Heavyocity","Kirk Hunter Studios","Scarbee","Teletone Audio",
    "Big Fish Audio","Vienna Symphonic Library","Native Instruments","EastWest"
]


def read_plist_from_bundle(bundle: Path) -> Optional[Dict]:
    # Bundle Info.plist typically at Contents/Info.plist
    info = bundle / "Contents" / "Info.plist"
    if info.exists():
        try:
            with open(info, 'rb') as f:
                return plistlib.load(f)
        except Exception:
            return None
    return None


def detect_vendor(fields: Dict[str, str]) -> Optional[str]:
    hay = " ".join([str(fields.get(k, "")) for k in ["name","path","bundle_id","version","manufacturer","cf_bundle_name"]]).lower()
    for pattern, canon in VENDOR_MAP:
        if re.search(pattern, hay, re.IGNORECASE):
            return canon
    return None


def scan_plugins() -> List[Dict[str, str]]:
    rows: List[Dict[str, str]] = []
    for ptype, root, ext in PLUGIN_DIRS:
        root_path = Path(root)
        if not root_path.exists():
            continue
        try:
            if ext is None:
                # collect all items
                items = list(root_path.iterdir())
            else:
                items = list(root_path.glob(f"*{ext}"))
        except Exception:
            continue
        for item in items:
            try:
                bundle = Path(item)
                name = bundle.stem
                bundle_id = version = manufacturer = cf_bundle_name = ""
                plist = None
                # For bundles only (directories)
                if bundle.is_dir():
                    plist = read_plist_from_bundle(bundle)
                # AU/VST/VST3/AAX are usually bundles; CLAP may be file
                if plist:
                    bundle_id = str(plist.get("CFBundleIdentifier", ""))
                    version = str(plist.get("CFBundleShortVersionString", plist.get("CFBundleVersion", "")))
                    cf_bundle_name = str(plist.get("CFBundleName", ""))
                    # Manufacturer guesses from various keys
                    manufacturer = str(plist.get("Manufacturer", plist.get("CFBundleGetInfoString", "")))
                fields = {
                    "type": ptype,
                    "name": name,
                    "path": str(bundle),
                    "bundle_id": bundle_id,
                    "version": version,
                    "manufacturer": manufacturer,
                    "cf_bundle_name": cf_bundle_name,
                }
                vendor = detect_vendor(fields) or ""
                fields["vendor_detected"] = vendor
                rows.append(fields)
            except Exception:
                continue
    return rows


def write_reports(rows: List[Dict[str, str]]):
    # Write master CSV
    with open(MASTER_CSV, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=["type","name","path","bundle_id","version","manufacturer","cf_bundle_name","vendor_detected"])
        w.writeheader()
        for r in rows:
            w.writerow(r)
    # Summary JSON with counts
    summary = {
        "timestamp": TS,
        "master_csv": str(MASTER_CSV),
        "counts": {
            "total": len(rows),
        },
        "by_type": {},
        "by_vendor": {},
    }
    by_type: Dict[str,int] = {}
    by_vendor: Dict[str,int] = {}
    for r in rows:
        by_type[r["type"]] = by_type.get(r["type"], 0) + 1
        v = r.get("vendor_detected") or "(unknown)"
        by_vendor[v] = by_vendor.get(v, 0) + 1
    summary["by_type"] = by_type
    summary["by_vendor"] = dict(sorted(by_vendor.items(), key=lambda x: (-x[1], x[0])))
    with open(SUMMARY_JSON, 'w') as jf:
        json.dump(summary, jf, indent=2)

    # Per-requested-vendor CSVs
    for vendor in REQUESTED_VENDORS:
        out = REPORTS_DIR / f"PLUGIN_INVENTORY_{vendor.replace(' ','_').upper()}_{TS}.csv"
        with open(out, 'w', newline='') as f:
            w = csv.DictWriter(f, fieldnames=["type","name","path","bundle_id","version","manufacturer","cf_bundle_name","vendor_detected"])
            w.writeheader()
            for r in rows:
                if r.get("vendor_detected") == vendor:
                    w.writerow(r)


def main():
    rows = scan_plugins()
    write_reports(rows)
    print(f"[MASTER] {MASTER_CSV}")
    print(f"[SUMMARY] {SUMMARY_JSON}")
    # Print quick summary
    print("[COUNTS] total:", len(rows))
    by_type = {}
    for r in rows:
        by_type[r['type']] = by_type.get(r['type'], 0) + 1
    for t, c in sorted(by_type.items(), key=lambda x: x[0]):
        print(f"  {t}: {c}")

    wanted = REQUESTED_VENDORS
    counts = {v:0 for v in wanted}
    for r in rows:
        v = r.get('vendor_detected')
        if v in counts:
            counts[v]+=1
    print("[VENDORS]")
    for v,c in counts.items():
        print(f"  {v}: {c}")

if __name__ == "__main__":
    main()
