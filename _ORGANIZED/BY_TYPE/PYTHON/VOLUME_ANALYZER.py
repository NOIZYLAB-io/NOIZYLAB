#!/usr/bin/env python3
"""
Volume Analyzer - Check what's on a volume
"""

import os
from pathlib import Path

def analyze_volume(volume_path="/Volumes/Untitled"):
    """Analyze volume contents"""
    volume = Path(volume_path)
    
    print("=" * 80)
    print(" " * 25 + "VOLUME ANALYZER")
    print("=" * 80)
    print(f"Analyzing: {volume_path}")
    print()
    
    if not volume.exists():
        print(f"❌ Volume not found: {volume_path}")
        return
    
    # Get all items
    items = []
    for item in volume.iterdir():
        items.append(item.name)
    
    print(f"📁 Found {len(items)} items:")
    print("-" * 80)
    
    system_files = []
    visible_files = []
    
    for item_name in sorted(items):
        item_path = volume / item_name
        
        # Get size info
        try:
            if item_path.is_dir():
                size = "[DIR]"
            else:
                size_bytes = item_path.stat().st_size
                if size_bytes > 1024*1024:
                    size = f"{size_bytes/(1024*1024):.1f} MB"
                elif size_bytes > 1024:
                    size = f"{size_bytes/1024:.1f} KB"
                else:
                    size = f"{size_bytes} B"
        except:
            size = "?"
        
        # Categorize
        if item_name.startswith('.'):
            system_files.append((item_name, size))
        else:
            visible_files.append((item_name, size))
    
    # Show visible files first
    if visible_files:
        print("\n📄 Visible Files/Directories:")
        for name, size in visible_files:
            icon = "📁" if (volume / name).is_dir() else "📄"
            print(f"   {icon} {name:40s} {size}")
    
    # Show system files
    if system_files:
        print("\n🔧 System Files (macOS):")
        for name, size in system_files:
            icon = "📁" if (volume / name).is_dir() else "📄"
            print(f"   {icon} {name:40s} {size}")
    
    # Summary
    print()
    print("=" * 80)
    print("📊 SUMMARY")
    print("=" * 80)
    print(f"Visible items: {len(visible_files)}")
    print(f"System items: {len(system_files)}")
    print()
    
    if not visible_files:
        print("⚠️  VOLUME APPEARS EMPTY!")
        print()
        print("This volume only contains macOS system files:")
        print("   • .DS_Store - macOS metadata file")
        print("   • .fseventsd/ - File System Events database")
        print("   • .TemporaryItems/ - Temporary files")
        print("   • .Spotlight-V100/ - Spotlight search index")
        print()
        print("💡 This means:")
        print("   • The drive is likely empty or newly formatted")
        print("   • macOS has created its system directories")
        print("   • No user data is stored on this volume")
        print()
        print("✅ Safe to use for storage!")
    
    # Try to get disk info
    print()
    print("💾 Disk Information:")
    try:
        import subprocess
        result = subprocess.run(['df', '-h', str(volume)], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')
            if len(lines) > 1:
                parts = lines[1].split()
                print(f"   Filesystem: {parts[0] if parts else 'N/A'}")
                if len(parts) >= 5:
                    print(f"   Size: {parts[1]}")
                    print(f"   Used: {parts[2]}")
                    print(f"   Available: {parts[3]}")
                    print(f"   Usage: {parts[4]}")
    except:
        pass
    
    print()

if __name__ == "__main__":
    import sys
    volume = sys.argv[1] if len(sys.argv) > 1 else "/Volumes/Untitled"
    analyze_volume(volume)

