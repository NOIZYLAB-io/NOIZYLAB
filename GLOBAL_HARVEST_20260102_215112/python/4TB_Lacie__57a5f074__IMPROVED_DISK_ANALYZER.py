#!/usr/bin/env python3
"""
IMPROVED Disk Usage Analyzer - Fast & Efficient
Finds what's consuming space without being slow
"""

import os
import subprocess
from pathlib import Path
from collections import defaultdict
from datetime import datetime

def quick_analyze(path, max_depth=2, min_size_mb=50):
    """Fast analysis with depth limit"""
    print(f"\n{'='*80}")
    print(f"📊 Quick Analysis: {path}")
    print(f"{'='*80}\n")
    
    # Top directories (limited depth for speed)
    print("Top directories (limited to depth 2 for speed):")
    print("-" * 80)
    
    try:
        # Use du with depth limit
        cmd = f"du -h -d {max_depth} '{path}' 2>/dev/null | sort -rh | head -20"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
        
        for line in result.stdout.strip().split('\n')[:20]:
            if line.strip():
                parts = line.split('\t')
                if len(parts) == 2:
                    size, dir_path = parts
                    print(f"  {size:>10}  →  {dir_path}")
    except Exception as e:
        print(f"  Error: {e}")
    
    # Large files only (for speed)
    print(f"\n{'='*80}")
    print(f"Large files only (>={min_size_mb}MB):")
    print("-" * 80)
    
    try:
        min_bytes = min_size_mb * 1024 * 1024
        cmd = f"find '{path}' -type f -size +{min_bytes}c -exec ls -lh {{}} \\; 2>/dev/null | awk '{{print $5, $9}}' | sort -rh | head -30"
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=60)
        
        if result.stdout.strip():
            for line in result.stdout.strip().split('\n')[:30]:
                if line.strip():
                    parts = line.split(' ', 1)
                    if len(parts) == 2:
                        size, file_path = parts
                        print(f"  {size:>10}  →  {file_path[:70]}...")
        else:
            print("  No large files found")
    except Exception as e:
        print(f"  Error: {e}")

def analyze_noizylab_structure():
    """Quick structure analysis"""
    noizylab = Path("/Users/m2ultra/NOIZYLAB")
    
    if not noizylab.exists():
        print(f"NOIZYLAB not found at {noizylab}")
        return
    
    print(f"\n{'='*80}")
    print("NOIZYLAB Structure (Root Level)")
    print(f"{'='*80}\n")
    
    dirs = []
    files = []
    
    for item in noizylab.iterdir():
        if item.is_dir():
            try:
                size = sum(f.stat().st_size for f in item.rglob('*') if f.is_file())
                size_mb = size / (1024 * 1024)
                dirs.append((item.name, size_mb))
            except:
                dirs.append((item.name, 0))
        elif item.is_file():
            try:
                size_mb = item.stat().st_size / (1024 * 1024)
                files.append((item.name, size_mb))
            except:
                files.append((item.name, 0))
    
    # Sort by size
    dirs.sort(key=lambda x: x[1], reverse=True)
    files.sort(key=lambda x: x[1], reverse=True)
    
    print("Directories:")
    for name, size_mb in dirs[:15]:
        size_str = f"{size_mb:.1f} MB" if size_mb >= 1 else f"{size_mb * 1024:.1f} KB"
        print(f"  {size_str:>12}  →  {name}/")
    
    print("\nFiles:")
    for name, size_mb in files[:15]:
        size_str = f"{size_mb:.1f} MB" if size_mb >= 1 else f"{size_mb * 1024:.1f} KB"
        print(f"  {size_str:>12}  →  {name}")

def main():
    print("="*80)
    print(" " * 20 + "IMPROVED DISK USAGE ANALYZER")
    print("="*80)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("⚡ Fast mode: Limited depth for speed\n")
    
    # Quick analyze /Users/m2ultra
    quick_analyze("/Users/m2ultra", max_depth=2, min_size_mb=100)
    
    # Analyze NOIZYLAB structure
    analyze_noizylab_structure()
    
    print(f"\n{'='*80}")
    print("✅ Analysis complete!")
    print(f"{'='*80}\n")
    
    print("💡 Recommendations:")
    print("  1. For detailed analysis: python3 disk_usage_analyzer.py")
    print("  2. To organize: ./FAST_CLEANUP.sh")
    print("  3. To upgrade everything: ./MASTER_UPGRADE_ALL.sh")

if __name__ == "__main__":
    main()

