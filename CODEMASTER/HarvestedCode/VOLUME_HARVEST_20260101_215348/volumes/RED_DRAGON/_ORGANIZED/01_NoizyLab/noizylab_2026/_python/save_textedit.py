#!/usr/bin/env python3
"""
save_textedit.py
- Reads text from clipboard
- Atomically writes to Saved_Notes as a timestamped .txt
- Opens the file in TextEdit (or preferred app from prefs)
- Respects cha_cha_prefs.json for auto-open behavior
"""

import subprocess
import tempfile
from pathlib import Path
from datetime import datetime
import json
import os
import sys

WORKSPACE = Path.home() / "Documents" / "Noizyfish_Aquarium/Noizy_Workspace"
SAVED = WORKSPACE / "Saved_Notes"
SAVED.mkdir(parents=True, exist_ok=True)
PREFS_PATH = WORKSPACE / "cha_cha_prefs.json"

DEFAULT_PREFS = {
    "auto_save_to_textedit": True,
    "default_voice": "Siri Voice 3",
    "open_with": "TextEdit"
}

def load_prefs():
    if PREFS_PATH.exists():
        try:
            return json.loads(PREFS_PATH.read_text(encoding="utf-8"))
        except Exception:
            return DEFAULT_PREFS.copy()
    return DEFAULT_PREFS.copy()

def get_clipboard_text():
    p = subprocess.run(["pbpaste"], capture_output=True, text=True)
    return p.stdout

def atomic_write(path: Path, content: str):
    # write to temp file then rename for atomicity
    fd, tmp_path = tempfile.mkstemp(dir=str(path.parent))
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(content)
    tmp = Path(tmp_path)
    tmp.replace(path)  # atomic on same filesystem

def save_and_open():
    prefs = load_prefs()
    text = get_clipboard_text()
    if not text or text.strip() == "":
        print("⚠️ Clipboard empty — nothing saved.")
        return None
    ts = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    fname = SAVED / f"cha_cha_saved_{ts}.txt"
    atomic_write(fname, text)
    print(f"✅ Saved to: {fname}")
    if prefs.get("auto_save_to_textedit", True):
        opener = prefs.get("open_with", "TextEdit")
        try:
            subprocess.run(["open", "-a", opener, str(fname)])
        except Exception as e:
            print("⚠️ Failed to open with", opener, ":", e)
    return str(fname)

if __name__ == "__main__":
    save_and_open()
