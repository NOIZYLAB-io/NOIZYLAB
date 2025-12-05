#!/usr/bin/env python3
import os
import shutil

# Usage: Set these to your folder names
ORIGINAL_FOLDER = "/Users/rsp_ms/Documents/THE_NEW_WORLD/_2025_PROJECTS/VSCodeMaster/TrackFilter/OldFolderName"
NEW_FOLDER = "/Users/rsp_ms/Documents/THE_NEW_WORLD/_2025_PROJECTS/VSCodeMaster/TrackFilter/NewFolderName"

# Delete the original folder after new one is created
if os.path.exists(NEW_FOLDER):
    if os.path.exists(ORIGINAL_FOLDER):
        try:
            shutil.rmtree(ORIGINAL_FOLDER)
            print(f"Deleted original folder: {ORIGINAL_FOLDER}")
        except Exception as e:
            print(f"Failed to delete {ORIGINAL_FOLDER}: {e}")
    else:
        print(f"Original folder not found: {ORIGINAL_FOLDER}")
else:
    print(f"New folder does not exist: {NEW_FOLDER}")
