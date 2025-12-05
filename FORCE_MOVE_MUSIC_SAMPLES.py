#!/usr/bin/env python3
"""
FORCE MOVE - Executes immediately, no prompts
Moves Music Samples to disk16s2 NOW
"""

import os
import shutil
import subprocess
from pathlib import Path

SOURCE = Path("/Volumes/4TB Big Fish/Music Samples")

def find_disk16s2():
    """Find disk16s2 mount point"""
    try:
        result = subprocess.run(['df', '-h'], capture_output=True, text=True, timeout=5)
        for line in result.stdout.split('\n'):
            if 'disk16s2' in line:
                parts = line.split()
                if parts:
                    mount = Path(parts[-1])
                    if mount.exists():
                        return mount
    except:
        pass
    
    # Check /Volumes
    volumes = Path("/Volumes")
    if volumes.exists():
        for vol in volumes.iterdir():
            if vol.is_dir() and 'disk16' in vol.name.lower():
                try:
                    # Verify it's actually mounted
                    os.listdir(vol)
                    return vol
                except:
                    pass
    
    return None

def force_move():
    """FORCE MOVE - Execute immediately"""
    print("=" * 80)
    print("FORCE MOVE - Music Samples → disk16s2")
    print("=" * 80)
    print()
    
    if not SOURCE.exists():
        print(f"❌ Source not found: {SOURCE}")
        return False
    
    print(f"✅ Source found: {SOURCE}")
    
    dest_base = find_disk16s2()
    
    if not dest_base:
        print("❌ disk16s2 not found!")
        print("\nListing all volumes:")
        for vol in sorted(Path("/Volumes").iterdir()):
            if vol.is_dir() and not vol.name.startswith('.'):
                print(f"  • {vol.name}")
        return False
    
    print(f"✅ Found disk16s2 at: {dest_base}")
    
    dest = dest_base / "Music_Samples"
    
    print(f"Destination: {dest}")
    print()
    
    # Check space
    try:
        stat = os.statvfs(dest_base)
        free_gb = (stat.f_bavail * stat.f_frsize) / (1024**3)
        print(f"Free space: {free_gb:.1f} GB")
    except:
        pass
    
    # Remove existing if present
    if dest.exists():
        print(f"⚠️  Removing existing destination...")
        try:
            shutil.rmtree(dest)
            print("   ✅ Removed")
        except Exception as e:
            print(f"   ⚠️  Error removing: {e}")
    
    # Create parent
    dest.parent.mkdir(parents=True, exist_ok=True)
    
    # FORCE MOVE NOW
    print()
    print("🚀 FORCE MOVING NOW...")
    print("   This may take a while...")
    print()
    
    try:
        shutil.move(str(SOURCE), str(dest))
        print()
        print("=" * 80)
        print("✅ FORCE MOVE COMPLETE!")
        print("=" * 80)
        print(f"New location: {dest}")
        return True
    except Exception as e:
        print()
        print("=" * 80)
        print(f"❌ ERROR: {e}")
        print("=" * 80)
        return False

if __name__ == "__main__":
    force_move()

