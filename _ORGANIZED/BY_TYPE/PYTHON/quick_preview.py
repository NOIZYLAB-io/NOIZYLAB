#!/usr/bin/env python3
"""
QUICK PREVIEW - See what's on each drive before deep scan
"""

import os
from pathlib import Path
from collections import defaultdict

DRIVES = [
    Path("/Volumes/6TB"),
    Path("/Volumes/4TBSG"),
]

def format_size(bytes_val):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_val < 1024.0:
            return f"{bytes_val:.2f} {unit}"
        bytes_val /= 1024.0
    return f"{bytes_val:.2f} PB"

def quick_scan_drive(drive_path):
    """Quick scan of drive top level"""
    print(f"\n{'='*70}")
    print(f"📀 DRIVE: {drive_path}")
    print(f"{'='*70}\n")
    
    if not drive_path.exists():
        print("❌ Drive not found!")
        return
    
    try:
        # Get total disk usage
        stat = os.statvfs(drive_path)
        total = stat.f_blocks * stat.f_frsize
        used = (stat.f_blocks - stat.f_bfree) * stat.f_frsize
        free = stat.f_bavail * stat.f_frsize
        
        print(f"💾 Capacity: {format_size(total)}")
        print(f"📊 Used:     {format_size(used)} ({used/total*100:.1f}%)")
        print(f"✨ Free:     {format_size(free)}")
        
        # List top-level directories
        print(f"\n📂 Top-Level Directories:\n")
        
        folders = []
        for item in drive_path.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                try:
                    # Quick estimate of folder size (just immediate files)
                    size = sum(f.stat().st_size for f in item.iterdir() 
                              if f.is_file() and not f.name.startswith('.'))
                    folders.append((item.name, size))
                except:
                    folders.append((item.name, 0))
        
        # Sort by name
        folders.sort()
        
        for name, size in folders[:50]:  # Show first 50
            size_str = format_size(size) if size > 0 else "..."
            print(f"  📁 {name:50} {size_str:>12}")
        
        if len(folders) > 50:
            print(f"\n  ... and {len(folders) - 50} more directories")
        
        print(f"\n  Total top-level directories: {len(folders)}")
        
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    print("\n" + "👀"*35)
    print("  QUICK PREVIEW - Multi-Drive Overview")
    print("👀"*35)
    
    for drive in DRIVES:
        quick_scan_drive(drive)
    
    print("\n" + "="*70)
    print("💡 Ready for deep scan? Run: python3 ultra_scanner_x1000.py")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()

