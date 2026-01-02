#!/usr/bin/env python3
"""
perfectionist_artwork_finder.py
Find Perfectionist artwork assets and auto-log results to Python_Script_Logs.
Now with robust error handling and exception logging.
"""

import os, fnmatch, traceback
from pathlib import Path
from datetime import datetime

PATTERNS = ["*.png","*.jpg","*.jpeg","*.icns","*.svg","*.webp","*.pdf"]
KEYWORDS = ["perfectionist","perfectionist.app"]

SEARCH_ROOTS = [
    Path("/Applications/Perfectionist.app"),
    Path.home() / "Library" / "Application Support",
    Path.home() / "Library" / "Containers",
    Path.home() / "Desktop",
    Path.home() / "Downloads"
]

def save_log(content, base="perfectionist_artwork"):
    log_dir = Path(__file__).parent / "Python_Script_Logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fp = log_dir / f"{base}_{ts}.txt"
    fp.write_text(content, encoding="utf-8")
    return fp

def looks_relevant(path: Path) -> bool:
    name = path.name.lower()
    return any(k in name for k in KEYWORDS)

def scan():
    hits = []
    errors = []
    for root in SEARCH_ROOTS:
        if not root.exists():
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            # skip giant caches quickly
            if "Cache" in dirpath or "Caches" in dirpath:
                continue
            for pat in PATTERNS:
                try:
                    for fname in fnmatch.filter(filenames, pat):
                        p = Path(dirpath) / fname
                        if looks_relevant(p) or "Perfectionist.app" in str(p):
                            hits.append(str(p))
                except Exception as e:
                    errors.append(f"Error in {dirpath}: {e}\n{traceback.format_exc()}")
    return sorted(set(hits)), errors

if __name__ == "__main__":
    results, errors = scan()
    out = "[NOIZY] Perfectionist artwork candidates:\n" + "\n".join(results) if results else "[NOIZY] No obvious artwork found. Try Spotlight (mdfind) or add more roots."
    if errors:
        out += "\n\n[NOIZY] Errors encountered during scan:\n" + "\n".join(errors)
    print(out)
    log_file = save_log(out)
    print(f"[NOIZY] Log saved to {log_file}")
