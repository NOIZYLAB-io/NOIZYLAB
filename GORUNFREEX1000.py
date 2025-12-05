#!/usr/bin/env python3
"""
GO RUN FREE X1000 - MAXIMUM SPEED EXECUTION
Executes everything at WARP SPEED!
"""

import os
import shutil
from pathlib import Path
import sys

def gorunfree():
    """Execute everything at maximum speed"""
    print("🚀 GO RUN FREE X1000 - WARP SPEED!")
    print("=" * 80)
    print()
    
    noizylab = Path("/Users/m2ultra/NOIZYLAB")
    executed = []
    
    # FIX - Clean everything
    print("🔧 FIXING...")
    fixes = 0
    for ds in noizylab.rglob('.DS_Store'):
        try:
            ds.unlink()
            fixes += 1
        except:
            pass
    print(f"   ✅ Fixed {fixes} files")
    executed.append(f"Fixed {fixes} files")
    
    # TRANSFER 1: Music Samples
    print("\n📦 TRANSFERRING Music Samples...")
    source1 = Path("/Volumes/4TB Big Fish/Music Samples")
    if source1.exists():
        dest_base = None
        for vol in Path("/Volumes").iterdir():
            if vol.is_dir() and 'disk16' in vol.name.lower():
                dest_base = vol
                break
        if not dest_base:
            dest_base = Path("/Volumes/SAMPLE_MASTER")
        
        dest1 = dest_base / "Music_Samples"
        try:
            if dest1.exists():
                shutil.rmtree(dest1)
            dest1.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source1), str(dest1))
            print(f"   ✅ Moved to {dest1}")
            executed.append("Music Samples")
        except Exception as e:
            print(f"   ⚠️  {e}")
    
    # TRANSFER 2: NoizyFish
    print("\n📦 ABSORBING NoizyFish...")
    source2 = Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED/🐍 Python_Projects/NoizyFish")
    dest2 = noizylab / "NoizyFish"
    if source2.exists():
        try:
            if not dest2.exists():
                shutil.copytree(source2, dest2)
                print(f"   ✅ Absorbed to {dest2}")
                executed.append("NoizyFish")
            else:
                # Merge
                for item in source2.iterdir():
                    if item.name.startswith('.'):
                        continue
                    dest_item = dest2 / item.name
                    if not dest_item.exists():
                        if item.is_dir():
                            shutil.copytree(item, dest_item)
                        else:
                            shutil.copy2(item, dest_item)
                print(f"   ✅ Merged to {dest2}")
                executed.append("NoizyFish merged")
        except Exception as e:
            print(f"   ⚠️  {e}")
    
    # TRANSFER 3: SFX Master
    print("\n📦 TRANSFERRING SFX Master...")
    source3 = Path("/Volumes/4TB Big Fish/SFX Master")
    dest3 = Path("/Volumes/SAMPLE_MASTER/SFX_Master_Organized")
    if source3.exists():
        try:
            if dest3.exists():
                shutil.rmtree(dest3)
            dest3.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source3), str(dest3))
            print(f"   ✅ Moved to {dest3}")
            executed.append("SFX Master")
        except Exception as e:
            print(f"   ⚠️  {e}")
    
    # SUMMARY
    print("\n" + "=" * 80)
    print("✅ GO RUN FREE X1000 COMPLETE!")
    print("=" * 80)
    print(f"Operations: {len(executed)}")
    for op in executed:
        print(f"   • {op}")
    print()

if __name__ == "__main__":
    gorunfree()

