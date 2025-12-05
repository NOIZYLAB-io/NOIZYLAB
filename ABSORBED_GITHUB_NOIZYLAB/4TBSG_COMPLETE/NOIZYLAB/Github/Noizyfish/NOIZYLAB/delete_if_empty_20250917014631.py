#!/usr/bin/env python3
import os
import shutil

# Set the folder to check
FOLDER_TO_DELETE = "/Users/rsp_ms/Documents/THE_NEW_WORLD/_2025_PROJECTS/VSCodeMaster/TrackFilter/FolderToDelete"

if os.path.exists(FOLDER_TO_DELETE):
    # Check if folder is empty (no files or subfolders)
    if not os.listdir(FOLDER_TO_DELETE):
        try:
            shutil.rmtree(FOLDER_TO_DELETE)
            print(f"Deleted empty folder: {FOLDER_TO_DELETE}")
        except Exception as e:
            print(f"Failed to delete {FOLDER_TO_DELETE}: {e}")
    else:
        print(f"Folder is not empty: {FOLDER_TO_DELETE}")
else:
    print(f"Folder does not exist: {FOLDER_TO_DELETE}")
