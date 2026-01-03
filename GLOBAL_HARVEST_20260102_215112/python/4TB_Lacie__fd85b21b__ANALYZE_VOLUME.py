#!/usr/bin/env python3
"""
Volume Analyzer
Analyzes any mounted volume to see what's on it
"""

import os
import subprocess
from pathlib import Path
from datetime import datetime

def analyze_volume(volume_path):
    """Analyze a volume and report what's on it"""
    volume = Path(volume_path)
    
    if not volume.exists():
        print(f"❌ Volume not found: {volume_path}")
        return
    
    print("=" * 80)
    print(" " * 25 + "VOLUME ANALYZER")
    print("=" * 80)
    print(f"Volume: {volume_path}")
    print()
    
    # Get disk space
    try:
        result = subprocess.run(
            ['df', '-h', str(volume)],
            capture_output=True,
            text=True
        )
        lines = result.stdout.strip().split('\n')
        if len(lines) > 1:
            parts = lines[1].split()
            if len(parts) >= 4:
                size = parts[1]
                used = parts[2]
                available = parts[3]
                usage = parts[4] if len(parts) > 4 else "N/A"
                print(f"📊 Disk Space:")
                print(f"   Size: {size}")
                print(f"   Used: {used}")
                print(f"   Available: {available}")
                print(f"   Usage: {usage}")
                print()
    except:
        pass
    
    # List top-level items
    print("📁 Top-level contents:")
    print("-" * 80)
    
    items = []
    for item in sorted(volume.iterdir()):
        try:
            if item.is_dir():
                # Try to get size
                try:
                    size_result = subprocess.run(
                        ['du', '-sh', str(item)],
                        capture_output=True,
                        text=True,
                        timeout=10
                    )
                    size = size_result.stdout.split()[0]
                except:
                    size = "?"
                
                items.append(('DIR', item.name, size))
            else:
                try:
                    size_mb = item.stat().st_size / (1024 * 1024)
                    size = f"{size_mb:.1f} MB"
                except:
                    size = "?"
                items.append(('FILE', item.name, size))
        except:
            pass
    
    if not items:
        print("   (Empty or only system files)")
    else:
        for item_type, name, size in items[:30]:
            icon = "📁" if item_type == "DIR" else "📄"
            print(f"   {icon} {name:40s} ({size:>10})")
    
    # Check for hidden/system files only
    visible_items = [item for item in items if not item[1].startswith('.')]
    
    if not visible_items:
        print()
        print("⚠️  Volume appears to be empty or only contains system files:")
        print("   • .DS_Store - macOS metadata")
        print("   • .fseventsd - File system events")
        print("   • .TemporaryItems - Temporary files")
        print("   • .Spotlight-V100 - Spotlight index")
        print()
        print("💡 This volume may be:")
        print("   • A freshly formatted drive")
        print("   • An empty external drive")
        print("   • A drive with only hidden/system files")
    else:
        print()
        print(f"✅ Found {len(visible_items)} visible items")
    
    # Check for large files deeper in the structure
    print()
    print("🔍 Searching for large files (>10MB)...")
    try:
        result = subprocess.run(
            ['find', str(volume), '-type', 'f', '-size', '+10M'],
            capture_output=True,
            text=True,
            timeout=30
        )
        large_files = [f for f in result.stdout.strip().split('\n') if f]
        
        if large_files:
            print(f"   Found {len(large_files)} large files:")
            for file_path in large_files[:10]:
                print(f"   • {file_path}")
        else:
            print("   No large files found")
    except:
        print("   (Could not scan for large files)")
    
    print()
    print("=" * 80)

def main():
    import sys
    
    if len(sys.argv) > 1:
        volume_path = sys.argv[1]
    else:
        volume_path = "/Volumes/Untitled"
    
    analyze_volume(volume_path)

if __name__ == "__main__":
    main()

