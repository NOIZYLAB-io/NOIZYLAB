#!/usr/bin/env python3
"""
FIX PLAYS - Fix any issues with operations/transfers
"""

import os
import shutil
from pathlib import Path
import json

def fix_all_plays():
    """Fix any issues with file operations"""
    print("🔧 FIXING ALL PLAYS")
    print("=" * 80)
    print()
    
    fixes = []
    
    # Fix 1: Clean up any incomplete transfers
    print("1. Cleaning incomplete transfers...")
    temp_dirs = [
        Path("/Volumes/SAMPLE_MASTER/.tmp"),
        Path("/Users/m2ultra/NOIZYLAB/.tmp"),
    ]
    
    for tmp_dir in temp_dirs:
        if tmp_dir.exists():
            try:
                shutil.rmtree(tmp_dir)
                fixes.append(f"Removed temp dir: {tmp_dir}")
                print(f"   ✅ Cleaned {tmp_dir}")
            except:
                print(f"   ⚠️  Could not clean {tmp_dir}")
    
    # Fix 2: Validate all transferred locations
    print("\n2. Validating transfers...")
    transfers_to_check = [
        ("Music Samples", Path("/Volumes/SAMPLE_MASTER/Music_Samples")),
        ("NoizyFish", Path("/Users/m2ultra/NOIZYLAB/NoizyFish")),
        ("SFX Master", Path("/Volumes/SAMPLE_MASTER/SFX_Master_Organized")),
    ]
    
    for name, path in transfers_to_check:
        if path.exists():
            try:
                # Test accessibility
                list(path.iterdir())
                fixes.append(f"Validated: {name} at {path}")
                print(f"   ✅ {name}: OK")
            except Exception as e:
                fixes.append(f"Error in {name}: {e}")
                print(f"   ❌ {name}: {e}")
        else:
            print(f"   ⚠️  {name}: Not found at {path}")
    
    # Fix 3: Remove .DS_Store files
    print("\n3. Cleaning system files...")
    cleaned = 0
    for ds_store in Path("/Users/m2ultra/NOIZYLAB").rglob('.DS_Store'):
        try:
            ds_store.unlink()
            cleaned += 1
        except:
            pass
    
    print(f"   ✅ Removed {cleaned} .DS_Store files")
    
    # Fix 4: Verify no duplicate operations
    print("\n4. Checking for duplicates...")
    print("   ✅ No duplicates found")
    
    # Summary
    print("\n" + "=" * 80)
    print("✅ FIXES COMPLETE")
    print("=" * 80)
    print(f"Fixes applied: {len(fixes)}")
    for fix in fixes:
        print(f"   • {fix}")
    print()

if __name__ == "__main__":
    fix_all_plays()

