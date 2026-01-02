#!/usr/bin/env python3
"""
Auto-add 'Noizy.ai Demo Portal' to Microsoft Edge favorites.

• Works on Windows (default Edge profile: 'Default')
• Designed to run automatically when you open your VS Code workspace
• Safe: Creates a backup of the Bookmarks file before modification
"""

import json, os, shutil
from datetime import datetime
from pathlib import Path

BOOKMARK_NAME = "Noizy.ai Demo Portal"
BOOKMARK_URL = "https://noizy.ai/portal"

def find_edge_bookmarks():
    base = Path(os.getenv("LOCALAPPDATA", "")) / "Microsoft" / "Edge" / "User Data"
    if not base.exists():
        raise FileNotFoundError("Edge profile not found. Make sure Edge has been opened once.")
    return base / "Default" / "Bookmarks"

def load_bookmarks(bookmark_file):
    with open(bookmark_file, "r", encoding="utf-8") as f:
        return json.load(f)

def save_bookmarks(bookmark_file, data):
    with open(bookmark_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def add_bookmark():
    bookmark_file = find_edge_bookmarks()
    backup = bookmark_file.with_name(f"Bookmarks_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
    shutil.copy(bookmark_file, backup)
    print(f"🪣 Backup created: {backup}")

    data = load_bookmarks(bookmark_file)
    new_bm = {
        "date_added": str(int(datetime.now().timestamp() * 1000000)),
        "guid": BOOKMARK_NAME.lower().replace(" ", "_"),
        "id": "999999",
        "name": BOOKMARK_NAME,
        "type": "url",
        "url": BOOKMARK_URL
    }

    bar = data["roots"].get("bookmark_bar", {})
    children = bar.get("children", [])
    if any(c.get("url") == BOOKMARK_URL for c in children):
        print(f"✅ Bookmark already exists: {BOOKMARK_URL}")
    else:
        children.append(new_bm)
        bar["children"] = children
        data["roots"]["bookmark_bar"] = bar
        save_bookmarks(bookmark_file, data)
        print(f"🌐 Added bookmark: {BOOKMARK_NAME}")

if __name__ == "__main__":
    try:
        add_bookmark()
    except Exception as e:
        print(f"⚠️ Error: {e}")
