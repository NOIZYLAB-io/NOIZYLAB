#!/usr/bin/env python3
import os, shutil, hashlib
from pathlib import Path

# Where to put the collected PDFs
DEST = Path("~/Desktop/RBC_Documents_Collected").expanduser()
DEST.mkdir(parents=True, exist_ok=True)

def sha256_file(p: Path):
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

def collect_rbc_pdfs():
    seen = set()
    roots = [Path.home(), Path("/Volumes")]
    count = 0
    for root in roots:
        if not root.exists(): continue
        for p in root.rglob("*.pdf"):
            try:
                if "rbc" in p.name.lower() or "rbc" in str(p.parent).lower():
                    cs = sha256_file(p)
                    if cs in seen: continue
                    seen.add(cs)
                    dest_file = DEST / p.name
                    # Avoid overwriting if same name
                    if dest_file.exists():
                        dest_file = DEST / f"{p.stem}_{cs[:8]}{p.suffix}"
                    shutil.move(p, dest_file)
                    count += 1
            except Exception:
                continue
    print(f"Collected {count} RBC-related PDFs into {DEST}")

if __name__ == "__main__":
    collect_rbc_pdfs()
