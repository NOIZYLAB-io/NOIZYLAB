#!/usr/bin/env python3
"""
Disk Usage Analyzer for /Users/m2ultra
Helps identify what's consuming 260GB+ of space
"""

import os
import subprocess
from pathlib import Path
from collections import defaultdict
from datetime import datetime

def run_command(cmd):
    """Run shell command and return output"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {e}"

def analyze_directory(path, top_n=30):
    """Analyze disk usage for a directory"""
    print(f"\n{'='*80}")
    print(f"📊 Analyzing: {path}")
    print(f"{'='*80}\n")
    
    # Get directory sizes
    print("Top directories by size:")
    print("-" * 80)
    cmd = f"du -h -d 1 '{path}' 2>/dev/null | sort -rh | head -{top_n}"
    output = run_command(cmd)
    for line in output.split('\n')[:top_n]:
        if line.strip():
            parts = line.split('\t')
            if len(parts) == 2:
                size, dir_path = parts
                print(f"  {size:>10}  →  {dir_path}")
    
    # Find large files
    print(f"\n{'='*80}")
    print("Large files (>100MB):")
    print("-" * 80)
    cmd = f"find '{path}' -type f -size +100M -exec ls -lh {{}} \\; 2>/dev/null | awk '{{print $5, $9}}' | sort -rh | head -20"
    output = run_command(cmd)
    if output and not output.startswith("Error"):
        for line in output.split('\n')[:20]:
            if line.strip():
                parts = line.split(' ', 1)
                if len(parts) == 2:
                    size, file_path = parts
                    print(f"  {size:>10}  →  {file_path}")
    else:
        print("  No large files found or error occurred")
    
    # File type distribution
    print(f"\n{'='*80}")
    print("File type distribution:")
    print("-" * 80)
    cmd = f"find '{path}' -type f -name '*.*' 2>/dev/null | sed 's/.*\\.//' | sort | uniq -c | sort -rn | head -15"
    output = run_command(cmd)
    if output and not output.startswith("Error"):
        for line in output.split('\n')[:15]:
            if line.strip():
                parts = line.split()
                if len(parts) >= 2:
                    count = parts[0]
                    ext = parts[1]
                    print(f"  {ext:>10}  →  {count:>6} files")

def analyze_noizylab():
    """Analyze NOIZYLAB specifically"""
    noizylab = Path("/Users/m2ultra/NOIZYLAB")
    
    if not noizylab.exists():
        print(f"NOIZYLAB not found at {noizylab}")
        return
    
    print(f"\n{'='*80}")
    print("NOIZYLAB Structure Analysis")
    print(f"{'='*80}\n")
    
    # Count directories
    dirs = [d for d in noizylab.iterdir() if d.is_dir()]
    files = [f for f in noizylab.iterdir() if f.is_file()]
    
    print(f"Directories: {len(dirs)}")
    print(f"Files in root: {len(files)}")
    
    # Show root files
    if files:
        print(f"\n{'='*80}")
        print("Files in NOIZYLAB root:")
        print("-" * 80)
        for f in sorted(files)[:30]:
            size = f.stat().st_size if f.exists() else 0
            size_str = f"{size / 1024 / 1024:.1f} MB" if size > 1024*1024 else f"{size / 1024:.1f} KB"
            print(f"  {size_str:>12}  →  {f.name}")

def main():
    """Main analysis"""
    print("="*80)
    print(" " * 25 + "DISK USAGE ANALYZER")
    print("="*80)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Analyze /Users/m2ultra
    analyze_directory("/Users/m2ultra", top_n=30)
    
    # Analyze NOIZYLAB specifically
    analyze_noizylab()
    
    print(f"\n{'='*80}")
    print("Analysis complete!")
    print(f"{'='*80}\n")
    
    print("💡 Recommendations:")
    print("  1. Run: cd /Users/m2ultra/NOIZYLAB && ./MASTER_CLEANUP_ORGANIZER.sh --analyze-only")
    print("  2. For media files: ./media_offload.sh --audit \"/Users/m2ultra\" \"/Volumes/12TB\"")
    print("  3. Check Library/Caches and Library/CloudStorage for large files")

if __name__ == "__main__":
    main()

