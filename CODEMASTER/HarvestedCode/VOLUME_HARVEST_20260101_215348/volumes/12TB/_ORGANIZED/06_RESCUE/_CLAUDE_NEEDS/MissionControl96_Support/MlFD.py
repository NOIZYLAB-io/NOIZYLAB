##
import os, re, shutil, json, hashlib
from pathlib import Path
from datetime import datetime

# --- configuration ---
SOURCE = Path("/Volumes/4TB Blue Fish/Native Instruments")   # your test source
DEST   = Path("/Volumes/4TB Blue Fish/Libraries")            # where clean copies go
REPORT_DIR = Path("./reports")

RULES = {
    "strip_prefixes": ["NI_", "Cymatics - ", "Output - ", "Heavocity_", "Strezov_"],
    "manufacturers": {
        "Native Instruments": ["Kontakt", "Massive", "Battery", "Razor", "Reaktor"],
        "Output": ["REV"],
        "Cymatics": ["Chaos"],
        "Heavyocity": ["Forzo"],
        "Strezov Sampling": ["Storm Choir", "Wotan"]
    },
    "extensions": [".wav", ".aiff", ".nki", ".nicnt", ".nkr", ".nkc", ".nks"]
}

# --- helpers -------------------------------------------------
def ensure_dir(p): Path(p).mkdir(parents=True, exist_ok=True)

def hash_file(path):
    h = hashlib.sha1()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1048576), b""):
            h.update(chunk)
    return h.hexdigest()

def normalize_name(name):
    for pre in RULES["strip_prefixes"]:
        if name.startswith(pre):
            name = name[len(pre):]
    name = re.sub(r"[_-]+", " ", name).strip().title()
    return name

def guess_manufacturer(folder):
    low = folder.name.lower()
    for m, hints in RULES["manufacturers"].items():
        if any(h.lower() in low for h in hints):
            return m
    if "cymatics" in low: return "Cymatics"
    return "Native Instruments"

def scan_library(folder):
    exts = [p.suffix.lower() for p in folder.rglob("*") if p.is_file()]
    has_samples = any(e in (".wav",".aif",".aiff",".ncw") for e in exts)
    has_instruments = any(e in (".nki",".nkm",".nkr",".nkc") for e in exts)
    return "Complete" if has_samples and has_instruments else (
        "Missing Samples" if not has_samples else "Missing Instruments"
    )

# --- main ----------------------------------------------------
def perfectionist_run(execute=False):
    ensure_dir(REPORT_DIR)
    ensure_dir(DEST)
    report = []

    print(f"🔍 Scanning {SOURCE}")
    for item in SOURCE.iterdir():
        if not item.is_dir(): 
            continue

        manu  = guess_manufacturer(item)
        clean = normalize_name(item.name)
        dest_folder = DEST / manu / clean
        completeness = scan_library(item)

        entry = {
            "manufacturer": manu,
            "library": clean,
            "source": str(item),
            "destination": str(dest_folder),
            "completeness": completeness
        }
        report.append(entry)

        print(f"🧩 {clean} → {manu} ({completeness})")

        if execute:
            ensure_dir(dest_folder)
            for f in item.rglob("*"):
                if f.is_file():
                    rel = f.relative_to(item)
                    out = dest_folder / rel
                    ensure_dir(out.parent)
                    shutil.copy2(f, out)
            print(f"✅ Copied → {dest_folder}")
        else:
            print(f"📝 Would copy → {dest_folder}")

    out = REPORT_DIR / f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(out,"w") as f: json.dump(report,f,indent=2)
    print(f"📄 Report saved to {out}")

if __name__ == "__main__":
    perfectionist_run(execute=False)
