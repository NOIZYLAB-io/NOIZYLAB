#!/usr/bin/env python3
"""
Quick Stats Viewer - Fast overview of your WAV collection
"""

from pathlib import Path
from collections import defaultdict

def get_quick_stats():
    """Get quick statistics"""
    source = Path("WAVES TO MOVE")
    
    if not source.exists():
        print(f"❌ Source not found: {source}")
        return
    
    print("="*80)
    print("📊 QUICK STATS - WAV COLLECTION OVERVIEW")
    print("="*80 + "\n")
    
    # Count files
    wav_files = list(source.rglob('*.wav')) + list(source.rglob('*.WAV'))
    
    print(f"📁 Source: {source.absolute()}")
    print(f"📊 Total WAV files: {len(wav_files)}\n")
    
    # Size analysis
    total_size = sum(f.stat().st_size for f in wav_files)
    print(f"💾 Total size: {total_size/(1024**3):.2f} GB ({total_size/(1024**2):.1f} MB)\n")
    
    # By folder
    by_folder = defaultdict(int)
    by_folder_size = defaultdict(int)
    
    for f in wav_files:
        folder = f.parent.name
        by_folder[folder] += 1
        by_folder_size[folder] += f.stat().st_size
    
    print("📂 Files by folder:")
    print("-"*80)
    for folder, count in sorted(by_folder.items(), key=lambda x: x[1], reverse=True)[:15]:
        size_mb = by_folder_size[folder] / (1024**2)
        print(f"  {folder:40s} {count:4d} files ({size_mb:6.1f} MB)")
    
    if len(by_folder) > 15:
        print(f"  ... and {len(by_folder) - 15} more folders")
    
    # Potential originals (no obvious commercial patterns)
    print("\n" + "="*80)
    print("⭐ POTENTIAL ORIGINAL COMPOSITIONS (Quick Scan)")
    print("="*80)
    print("Files that DON'T match known commercial patterns:\n")
    
    commercial_keywords = ['mirage', 'kawaii', 'dx100', 'manjira', 'dholak', 
                          'sys100', 'sh5', 'ambient', 'beat', 'loop', 'hit']
    
    potential_originals = []
    for f in wav_files:
        name_lower = f.name.lower()
        if not any(kw in name_lower for kw in commercial_keywords):
            potential_originals.append(f)
    
    print(f"Found {len(potential_originals)} potential originals")
    print("(Final determination requires metadata scan)\n")
    
    if potential_originals:
        print("Sample files:")
        for f in sorted(potential_originals, key=lambda x: x.name)[:20]:
            size_mb = f.stat().st_size / (1024**2)
            print(f"  ⭐ {f.name:50s} ({size_mb:.2f} MB)")
        if len(potential_originals) > 20:
            print(f"  ... and {len(potential_originals) - 20} more")
    
    print("\n" + "="*80)
    print("💡 To get accurate identification, run:")
    print("   python3 MEGA_ULTIMATE_ORGANIZER.py")
    print("="*80 + "\n")

if __name__ == '__main__':
    get_quick_stats()

