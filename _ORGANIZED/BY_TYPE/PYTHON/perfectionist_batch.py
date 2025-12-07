import os, re, json, hashlib, shutil
from pathlib import Path
from datetime import datetime

SOURCE = Path("/Volumes/4TB Blue Fish/Native Instruments")
DEST = Path("/Volumes/4TB Blue Fish/Libraries")
LOGS = Path("./logs")
REPORTS = Path("./reports")
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

def hash_file(path):
    h = hashlib.sha1()
    with open(path, "rb") as f:
        while chunk := f.read(1048576):
            h.update(chunk)
    return h.hexdigest()

def guess_manufacturer(folder):
    name = folder.name.lower()
    for m in RULES["manufacturers"]:
        if any(k.lower() in name for k in RULES["manufacturers"][m]):
            return m
    if "cymatics" in name: return "Cymatics"
    return "Native Instruments"

def normalize_name(name):
    for pre in RULES["strip_prefixes"]:
        if name.startswith(pre):
            name = name[len(pre):]
    name = re.sub(r"[_-]+", " ", name).strip().title()
    return name

def scan_library(folder):
    files = list(folder.rglob("*"))
    samples = [f for f in files if f.suffix.lower() in [".wav", ".aif", ".aiff", ".ncw"]]
    instruments = [f for f in files if f.suffix.lower() in [".nki", ".nkm", ".nkr", ".nkc"]]
    completeness = "Complete" if samples and instruments else "Missing Samples" if not samples else "Missing Instruments"

    hashes, duplicates = {}, []
    for f in samples:
        try:
            h = hash_file(f)
            if h in hashes:
                duplicates.append((f, hashes[h]))
            else:
                hashes[h] = f
        except Exception:
            continue

    return {
        "path": str(folder),
        "files": len(files),
        "samples": len(samples),
        "instruments": len(instruments),
        "completeness": completeness,
        "duplicates": len(duplicates),
        "dup_examples": [str(duplicates[0][0])] if duplicates else []
    }

def perfectionist_run(execute=False, max_libraries=10):
    LOGS.mkdir(exist_ok=True)
    REPORTS.mkdir(exist_ok=True)
    report_data = []
    print(f"🔍 Scanning {SOURCE} ...")

    count = 0
    for item in SOURCE.iterdir():
        if count >= max_libraries:
            print(f"⚠️  Max of {max_libraries} libraries processed at a time. Stopping.")
            break
        if not item.is_dir():
            continue

        manu = guess_manufacturer(item)
        clean_name = normalize_name(item.name)
        dest_folder = DEST / manu / clean_name
        result = scan_library(item)
        result["manufacturer"] = manu
        result["library"] = clean_name
        report_data.append(result)

        print(f"🧩 {clean_name} → {manu} ({result['completeness']})")

        if execute:
            dest_folder.mkdir(parents=True, exist_ok=True)
            for f in item.rglob("*"):
                if f.is_file():
                    rel = f.relative_to(item)
                    out = dest_folder / rel
                    out.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(f, out)
            print(f"✅ Moved to {dest_folder}")
        else:
            print(f"📝 Would move to {dest_folder}")
        count += 1

    report_file = REPORTS / f"perfectionist_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(report_file, "w") as f:
        json.dump(report_data, f, indent=2)
    print(f"📄 Report written to {report_file}")

if __name__ == "__main__":
    perfectionist_run(execute=False, max_libraries=10)