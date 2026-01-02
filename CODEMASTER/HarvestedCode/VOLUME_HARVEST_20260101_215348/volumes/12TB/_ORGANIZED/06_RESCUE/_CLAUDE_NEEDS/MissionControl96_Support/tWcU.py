#!/usr/bin/env python3
"""
Auto-add 'Noizy.ai Demo Portal' to Firefox bookmarks.

• Works on Windows (default Firefox profile: 'default-release')
• Designed to run automatically when you open your VS Code workspace
• Safe: Creates a backup of the bookmarks file before modification
"""

import json, os, shutil
from datetime import datetime
from pathlib import Path

BOOKMARK_NAME = "Noizy.ai Demo Portal"
BOOKMARK_URL = "https://noizy.ai/portal"

def find_firefox_bookmarks():
    base = Path(os.getenv("APPDATA", "")) / "Mozilla" / "Firefox" / "Profiles"
    if not base.exists():
        raise FileNotFoundError("Firefox profile not found. Make sure Firefox has been opened once.")
    profile = next(base.glob("*.default-release"), None)
    if profile is None:
        raise FileNotFoundError("Default Firefox profile not found.")
    return profile / "bookmarks.json"

def load_bookmarks(bookmark_file):
    with open(bookmark_file, "r", encoding="utf-8") as f:
        return json.load(f)

def save_bookmarks(bookmark_file, data):
    with open(bookmark_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def add_bookmark():
    bookmark_file = find_firefox_bookmarks()
    backup = bookmark_file.with_name(f"bookmarks_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json")
    shutil.copy(bookmark_file, backup)
    print(f"🪣 Backup created: {backup}")

    data = load_bookmarks(bookmark_file)
    new_bm = {
        "id": "999999",
        "type": "url",
        "url": BOOKMARK_URL,
        "title": BOOKMARK_NAME,
        "dateAdded": str(int(datetime.now().timestamp() * 1000000)),
        "guid": BOOKMARK_NAME.lower().replace(" ", "_")
    }

    if any(bm.get("url") == BOOKMARK_URL for bm in data.get("roots", {}).get("bookmark_bar", {}).get("children", [])):
        print(f"✅ Bookmark already exists: {BOOKMARK_URL}")
    else:
        data["roots"]["bookmark_bar"]["children"].append(new_bm)
        save_bookmarks(bookmark_file, data)
        print(f"🌐 Added bookmark: {BOOKMARK_NAME}")

if __name__ == "__main__":
    try:
        add_bookmark()
    except Exception as e:
        print(f"⚠️ Error: {e}")
~/add_noizy_ai_bookmark_firefox.sh
