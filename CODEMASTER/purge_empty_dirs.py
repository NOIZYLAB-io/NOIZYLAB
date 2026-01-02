#!/usr/bin/env python3
"""
EMPTY FOLDER PURGE - NUCLEAR EDITION
=====================================
Deletes ALL empty directories from ALL mounted volumes.
"""
import os
import sys

def delete_empty_dirs(root_path):
    """Recursively delete empty directories bottom-up."""
    deleted = 0
    
    # Keep running until no more empty dirs found
    while True:
        found_empty = False
        for dirpath, dirnames, filenames in os.walk(root_path, topdown=False):
            # Skip system directories
            skip_patterns = ['.Spotlight', '.fseventsd', '.Trashes', 
                           '.DocumentRevisions', '.TemporaryItems', 
                           '/System/', '/private/', '/.vol/']
            if any(skip in dirpath for skip in skip_patterns):
                continue
                
            try:
                # Check if directory is empty (no files, no subdirs)
                if os.path.isdir(dirpath):
                    contents = os.listdir(dirpath)
                    # Filter out .DS_Store files
                    real_contents = [c for c in contents if c != '.DS_Store']
                    
                    if not real_contents:
                        # Delete .DS_Store if present, then remove dir
                        ds_store = os.path.join(dirpath, '.DS_Store')
                        if os.path.exists(ds_store):
                            os.remove(ds_store)
                        os.rmdir(dirpath)
                        print(f"🗑️  {dirpath}")
                        deleted += 1
                        found_empty = True
            except PermissionError:
                pass
            except OSError:
                pass
        
        if not found_empty:
            break
    
    return deleted

# Target ALL volumes
VOLUMES = [
    "/Volumes/RED DRAGON",
    "/Volumes/12TB", 
    "/Volumes/6TB",
    "/Volumes/RSP",
    "/Volumes/4TB Blue Fish",
    "/Volumes/4TB Big Fish",
    "/Volumes/4TB BLK",
    "/Volumes/4TB FISH SG",
    "/Volumes/4TB Lacie",
    "/Volumes/4TBSG",
    "/Volumes/EW",
    "/Volumes/FISH",
    "/Volumes/JOE",
    "/Volumes/MAG 4TB",
    "/Volumes/SAMPLE_MASTER",
    "/Volumes/SIDNEY",
    "/Volumes/SOUND_DESIGN",
    "/Users/m2ultra/NOIZYLAB",
    "/Users/m2ultra/Desktop",
    "/Users/m2ultra/Documents",
    "/Users/m2ultra/Downloads",
]

if __name__ == "__main__":
    print("🔥 EMPTY FOLDER PURGE - NUCLEAR EDITION 🔥")
    print("=" * 60)
    
    total_deleted = 0
    
    for vol in VOLUMES:
        if os.path.exists(vol):
            print(f"\n📀 Scanning: {vol}")
            deleted = delete_empty_dirs(vol)
            total_deleted += deleted
            if deleted > 0:
                print(f"   ✅ Removed {deleted} empty folders")
            else:
                print(f"   ✨ Clean - no empty folders")
    
    print(f"\n{'=' * 60}")
    print(f"🎉 TOTAL PURGED: {total_deleted} empty folders")
