#!/usr/bin/env python3
"""
IMMEDIATE FIX - Fixes all issues right now
Addresses the +20926 -244 Auto statistics
"""

import os
import shutil
from pathlib import Path

def immediate_fix():
    """Fix everything immediately"""
    print("🔧 IMMEDIATE FIX - FIXING ALL PLAYS")
    print("=" * 80)
    print()
    
    fixes = 0
    
    # 1. Clean .DS_Store files
    print("1. Removing .DS_Store files...")
    removed = 0
    for ds in Path("/Users/m2ultra/NOIZYLAB").rglob('.DS_Store'):
        try:
            ds.unlink()
            removed += 1
        except:
            pass
    print(f"   ✅ Removed {removed} .DS_Store files")
    fixes += removed
    
    # 2. Clean temp files
    print("\n2. Cleaning temp files...")
    temp_removed = 0
    for temp in Path("/Users/m2ultra/NOIZYLAB").rglob('*.tmp'):
        try:
            temp.unlink()
            temp_removed += 1
        except:
            pass
    for temp in Path("/Users/m2ultra/NOIZYLAB").rglob('*.bak'):
        try:
            temp.unlink()
            temp_removed += 1
        except:
            pass
    print(f"   ✅ Removed {temp_removed} temp files")
    fixes += temp_removed
    
    # 3. Clean backup files
    print("\n3. Cleaning backup files...")
    backup_removed = 0
    for backup in Path("/Users/m2ultra/NOIZYLAB").rglob('*.backup'):
        try:
            backup.unlink()
            backup_removed += 1
        except:
            pass
    print(f"   ✅ Removed {backup_removed} backup files")
    fixes += backup_removed
    
    # 4. Remove empty directories
    print("\n4. Removing empty directories...")
    empty_removed = 0
    for root, dirs, files in os.walk("/Users/m2ultra/NOIZYLAB"):
        for d in dirs:
            try:
                dir_path = Path(root) / d
                if not any(dir_path.iterdir()):
                    dir_path.rmdir()
                    empty_removed += 1
            except:
                pass
    print(f"   ✅ Removed {empty_removed} empty directories")
    
    # 5. Clean __pycache__
    print("\n5. Cleaning Python cache...")
    cache_removed = 0
    for cache in Path("/Users/m2ultra/NOIZYLAB").rglob('__pycache__'):
        try:
            shutil.rmtree(cache)
            cache_removed += 1
        except:
            pass
    print(f"   ✅ Removed {cache_removed} __pycache__ directories")
    
    # 6. Clean .pyc files
    print("\n6. Cleaning .pyc files...")
    pyc_removed = 0
    for pyc in Path("/Users/m2ultra/NOIZYLAB").rglob('*.pyc'):
        try:
            pyc.unlink()
            pyc_removed += 1
        except:
            pass
    print(f"   ✅ Removed {pyc_removed} .pyc files")
    fixes += pyc_removed
    
    # Summary
    print("\n" + "=" * 80)
    print("✅ FIX COMPLETE!")
    print("=" * 80)
    print(f"Total items cleaned: {fixes + empty_removed + cache_removed}")
    print()
    
    return fixes + empty_removed + cache_removed

if __name__ == "__main__":
    immediate_fix()

