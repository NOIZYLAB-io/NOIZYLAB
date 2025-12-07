#!/usr/bin/env python3
"""
Move Music Samples to SAMPLE_MASTER
Preserves original directory structure
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

SOURCE = Path("/Volumes/4TB Big Fish/Music Samples")
DEST_BASE = None

# Try to find SAMPLE_MASTER volume
SAMPLE_MASTER_CANDIDATES = [
    "/Volumes/SAMPLE_MASTER",
    "/Volumes/Sample Master",
    "/Volumes/SAMPLE MASTER",
]

def find_sample_master():
    """Find SAMPLE_MASTER volume"""
    # Check common mount points
    for candidate in SAMPLE_MASTER_CANDIDATES:
        if Path(candidate).exists():
            return Path(candidate)
    
    # Check all volumes
    volumes_dir = Path("/Volumes")
    if volumes_dir.exists():
        for item in volumes_dir.iterdir():
            if "sample" in item.name.lower() and "master" in item.name.lower():
                return item
    
    return None

def verify_source():
    """Verify source directory exists"""
    if not SOURCE.exists():
        print(f"❌ Source directory not found: {SOURCE}")
        return False
    
    # Check for expected libraries
    expected_libs = [
        "MS Ethnic Drum Ensembles",
        "Deeper Tech-House",
        "Earth Moments Indian Street Drummers"
    ]
    
    found_libs = [lib for lib in expected_libs if (SOURCE / lib).exists()]
    
    if not found_libs:
        print(f"⚠️  Warning: No expected libraries found in {SOURCE}")
        return False
    
    print(f"✅ Source verified: {SOURCE}")
    print(f"   Found libraries: {', '.join(found_libs)}")
    return True

def move_library(lib_name, source_dir, dest_dir, dry_run=True):
    """Move a library preserving structure"""
    source_path = source_dir / lib_name
    dest_path = dest_dir / lib_name
    
    if not source_path.exists():
        print(f"⚠️  Library not found: {lib_name}")
        return False
    
    # Calculate size
    total_size = 0
    file_count = 0
    
    for root, dirs, files in os.walk(source_path):
        for file in files:
            file_path = Path(root) / file
            try:
                total_size += file_path.stat().st_size
                file_count += 1
            except:
                pass
    
    size_gb = total_size / (1024**3)
    
    print(f"\n📦 Library: {lib_name}")
    print(f"   Files: {file_count:,}")
    print(f"   Size: {size_gb:.2f} GB")
    print(f"   Source: {source_path}")
    print(f"   Destination: {dest_path}")
    
    if dry_run:
        print(f"   [DRY RUN] Would move library")
        return True
    
    # Create destination directory
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    # Check if destination already exists
    if dest_path.exists():
        print(f"   ⚠️  Destination already exists!")
        response = input(f"   Overwrite? (yes/no): ").strip().lower()
        if response != "yes":
            print(f"   ⏭️  Skipping {lib_name}")
            return False
        # Remove existing
        shutil.rmtree(dest_path)
    
    # Move (copy then remove source)
    print(f"   📥 Moving...")
    try:
        shutil.move(str(source_path), str(dest_path))
        print(f"   ✅ Moved successfully!")
        return True
    except Exception as e:
        print(f"   ❌ Error moving: {e}")
        return False

def main():
    import sys
    
    dry_run = '--live' not in sys.argv
    
    print("=" * 80)
    print(" " * 20 + "MOVE MUSIC SAMPLES TO SAMPLE_MASTER")
    print("=" * 80)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Find destination
    dest_base = find_sample_master()
    
    if not dest_base:
        print("❌ SAMPLE_MASTER volume not found!")
        print()
        print("Looking for volume with 'sample' and 'master' in name.")
        print("Available volumes:")
        
        volumes_dir = Path("/Volumes")
        if volumes_dir.exists():
            for item in sorted(volumes_dir.iterdir()):
                if item.is_dir() and not item.name.startswith('.'):
                    try:
                        stat = os.statvfs(item)
                        free_gb = (stat.f_bavail * stat.f_frsize) / (1024**3)
                        total_gb = (stat.f_blocks * stat.f_frsize) / (1024**3)
                        print(f"   • {item.name:30s} - {free_gb:.1f} GB free of {total_gb:.1f} GB")
                    except:
                        print(f"   • {item.name}")
        
        print()
        dest_input = input("Enter destination path (or press Enter to cancel): ").strip()
        if not dest_input:
            print("❌ Cancelled")
            return
        dest_base = Path(dest_input)
    
    if not dest_base.exists():
        print(f"❌ Destination not found: {dest_base}")
        return
    
    # Check disk space
    try:
        stat = os.statvfs(dest_base)
        free_gb = (stat.f_bavail * stat.f_frsize) / (1024**3)
        total_gb = (stat.f_blocks * stat.f_frsize) / (1024**3)
        print(f"✅ Destination found: {dest_base}")
        print(f"   Free space: {free_gb:.1f} GB")
        print(f"   Total space: {total_gb:.1f} GB")
    except Exception as e:
        print(f"⚠️  Could not check disk space: {e}")
    
    print()
    
    # Verify source
    if not verify_source():
        print("❌ Source verification failed")
        return
    
    print()
    
    # Destination structure
    dest_dir = dest_base / "Music Samples"
    
    print(f"📁 Destination: {dest_dir}")
    print()
    
    if dry_run:
        print("⚠️  DRY RUN MODE - No files will be moved")
        print("   Add --live to actually move files\n")
    else:
        confirm = input("⚠️  This will move files from source to destination. Continue? (yes/no): ")
        if confirm.lower() != "yes":
            print("❌ Cancelled")
            return
    
    # Libraries to move
    libraries = [
        "MS Ethnic Drum Ensembles",
        "Deeper Tech-House",
        "Earth Moments Indian Street Drummers"
    ]
    
    # Move each library
    results = []
    for lib in libraries:
        result = move_library(lib, SOURCE, dest_dir, dry_run=dry_run)
        results.append((lib, result))
    
    # Summary
    print("\n" + "=" * 80)
    print("📊 MOVE SUMMARY")
    print("=" * 80)
    
    successful = sum(1 for _, result in results if result)
    total = len(results)
    
    for lib, result in results:
        status = "✅" if result else "❌"
        print(f"   {status} {lib}")
    
    print()
    print(f"Libraries processed: {successful}/{total}")
    
    if dry_run:
        print("\n💡 This was a DRY RUN. Run with --live to actually move files.")
    else:
        print("\n✅ Move operation complete!")
    
    print()

if __name__ == "__main__":
    main()

