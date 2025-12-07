#!/usr/bin/env python3
import os, shutil, re
from pathlib import Path
from datetime import datetime

# === CONFIG ===
ROOT = Path.home() / "Desktop" / "NoizyFish"
LOG = ROOT / f"_reconnection_log_{datetime.now().strftime('%Y%m%d-%H%M%S')}.txt"
DRY_RUN = False  # Set to True to preview without moving files

# === Helpers ===
def log(msg):
    print(msg)
    with LOG.open("a") as f:
        f.write(msg + "\n")

def infer_project(name):
    base = name.lower()
    match = re.match(r"([a-zA-Z0-9]+)[_\-\s]", base)
    if match:
        return match.group(1).capitalize()
    return "Misc"

def organize():
    log(f"🔄 Noizy Reconnection started in: {ROOT}")
    files = [f for f in ROOT.iterdir() if f.is_file() and not f.name.startswith("_reconnection_log")]
    log(f"Found {len(files)} files to reconnect.")

    for f in files:
        ext = f.suffix.lower().lstrip(".") or "unknown"
        proj = infer_project(f.stem)
        target_dir = ROOT / proj / ext
        target_dir.mkdir(parents=True, exist_ok=True)
        target_path = target_dir / f.name

        if target_path.exists():
            log(f"⚠️ Skipping (already exists): {f.name}")
            continue

        log(f"📁 Moving: {f.name} → {target_path.relative_to(ROOT)}")
        if not DRY_RUN:
            shutil.move(str(f), str(target_path))

    log("✅ Reconnection complete.")

# === Multi-mode launcher ===
def reconnect():
    organize()

def launch(mode):
    modes = {
        "organize": organize,
        "reconnect": reconnect
    }
    func = modes.get(mode)
    if func:
        func()
    else:
        print(f"❌ Unknown mode: {mode}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        launch(sys.argv[1])
    else:
        print("⚠️ No mode specified. Try: python3 noizy_reconnection.py organize")

