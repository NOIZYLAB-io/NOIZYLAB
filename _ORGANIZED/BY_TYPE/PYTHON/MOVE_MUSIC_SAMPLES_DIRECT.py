#!/usr/bin/env python3
"""
DIRECT MOVE - Executes immediately
Moves Music Samples to disk16s2
"""

import os
import shutil
import subprocess
from pathlib import Path

SOURCE = Path("/Volumes/4TB Big Fish/Music Samples")

def find_disk16s2():
    """Find disk16s2 mount point"""
    try:
        result = subprocess.run(['df', '-h'], capture_output=True, text=True)
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
            if 'disk16' in vol.name.lower() or vol.name == 'disk16s2':
                return vol
    
    return None

def move_now():
    """Execute move immediately"""
    print("=" * 80)
    print("MOVING MUSIC SAMPLES TO disk16s2")
    print("=" * 80)
    print()
    
    if not SOURCE.exists():
        print(f"❌ Source not found: {SOURCE}")
        return False
    
    dest_base = find_disk16s2()
    
    if not dest_base:
        print("❌ disk16s2 not found!")
        print("\nAvailable volumes:")
        for vol in Path("/Volumes").iterdir():
            if vol.is_dir() and not vol.name.startswith('.'):
                print(f"  • {vol.name}")
        return False
    
    dest = dest_base / "Music_Samples"
    
    print(f"Source: {SOURCE}")
    print(f"Destination: {dest}")
    print()
    
    # Check space
    try:
        stat = os.statvfs(dest_base)
        free_gb = (stat.f_bavail * stat.f_frsize) / (1024**3)
        print(f"Free space: {free_gb:.1f} GB")
    except:
        pass
    
    # Check if exists
    if dest.exists():
        print(f"\n⚠️  Destination exists!")
        print(f"Removing existing...")
        shutil.rmtree(dest)
    
    # Create parent
    dest.parent.mkdir(parents=True, exist_ok=True)
    
    # MOVE NOW
    print(f"\n🚀 MOVING NOW...")
    print(f"This may take a while...\n")
    
    try:
        shutil.move(str(SOURCE), str(dest))
        print("✅ MOVE COMPLETE!")
        print(f"New location: {dest}")
        return True
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

if __name__ == "__main__":
    move_now()

