#!/usr/bin/env python3
"""
noizy_find.py
Recursive file search in Python with auto-logging.

- Searches a starting folder for files matching a pattern.
- Skips over folders it cannot access (avoids 'Permission denied').
- Always writes results into a .txt file inside "Python_Script_Logs"
  in the current working directory.
"""

import os
import fnmatch
from datetime import datetime

def safe_walk(top):
    """Like os.walk, but skips folders without permission."""
    for root, dirs, files in os.walk(top, topdown=True):
        # Remove dirs we can't access
        accessible_dirs = []
        for d in dirs:
            try:
                os.listdir(os.path.join(root, d))
                accessible_dirs.append(d)
            except PermissionError:
                continue
        dirs[:] = accessible_dirs
        yield root, dirs, files

def find_files(start_dir, pattern="*.py"):
    matches = []
    for root, dirs, files in safe_walk(start_dir):
        for filename in fnmatch.filter(files, pattern):
            matches.append(os.path.join(root, filename))
    return matches

def save_log(content, log_dir="Python_Script_Logs", base_name="noizy_find"):
    os.makedirs(log_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(log_dir, f"{base_name}_{timestamp}.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    return file_path

if __name__ == "__main__":
    # --- CONFIGURE HERE ---
    start_dir = os.path.expanduser("~/Documents/Noizyfish_Aquarium/Noizy_Workspace")  # search your workspace
    pattern = "noizy_car_wash.py"  # e.g. "*.wav", "*.txt", "noizy_car_wash.py"

    results = find_files(start_dir, pattern)

    if results:
        output = "[NOIZY] Found these matches:\n" + "\n".join(results)
    else:
        output = "[NOIZY] No matches found."

    print(output)
    log_file = save_log(output)
    print(f"[NOIZY] Log saved to {log_file}")

