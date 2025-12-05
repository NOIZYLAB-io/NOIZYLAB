#!/usr/bin/env python3
"""
PREVIEW what will be organized - shows which files have NO metadata (your originals!)

⭐⭐⭐ HARD RULE ⭐⭐⭐
ANY FILE WITHOUT METADATA = ORIGINAL COMPOSITION!
"""

import struct
from pathlib import Path

def has_metadata(filepath):
    """Quick check if WAV has INFO metadata"""
    try:
        with open(filepath, 'rb') as f:
            riff = f.read(4)
            if riff != b'RIFF':
                return None
            f.read(4)  # file size
            wave = f.read(4)
            if wave != b'WAVE':
                return None
            
            while True:
                chunk_id = f.read(4)
                if len(chunk_id) < 4:
                    break
                chunk_size = struct.unpack('<I', f.read(4))[0]
                
                if chunk_id == b'LIST':
                    chunk_data = f.read(min(chunk_size, 1000))
                    if b'INFO' in chunk_data:
                        return True
                elif chunk_id == b'bext':
                    return True
                else:
                    f.seek(chunk_size, 1)
                
                if chunk_size % 2:
                    f.read(1)
        
        return False
    except:
        return None

def is_commercial_pattern(filename):
    """Check if filename suggests commercial sample"""
    name = filename.lower()
    patterns = ['mirage', 'kawaii', 'dx100', 'manjira', 'dholak', 
                'sys100', 'sh5', 'sh-5', 'stormseasonfx']
    return any(p in name for p in patterns)

# Scan files
source = Path("WAVES TO MOVE")
wav_files = list(source.rglob('*.wav')) + list(source.rglob('*.WAV'))

print("="*80)
print("PREVIEW: Identifying YOUR ORIGINAL COMPOSITIONS")
print("="*80)
print("\n⭐⭐⭐ HARD RULE ⭐⭐⭐")
print("ANY FILE WITHOUT METADATA = YOUR ORIGINAL COMPOSITION!")
print("="*80 + "\n")
print(f"Scanning {len(wav_files)} files...\n")

originals = []
commercial = []
checking = []

for i, wav_file in enumerate(wav_files):
    if i % 50 == 0 and i > 0:
        print(f"  Scanned {i}/{len(wav_files)}...")
    
    has_meta = has_metadata(wav_file)
    is_commercial = is_commercial_pattern(wav_file.name)
    
    if has_meta or is_commercial:
        commercial.append(wav_file)
    elif has_meta is False:  # Explicitly no metadata
        originals.append(wav_file)
    else:
        checking.append(wav_file)

print("\n" + "="*80)
print("🎵 YOUR ORIGINAL COMPOSITIONS (NO METADATA):")
print("="*80)
print(f"Found {len(originals)} files WITHOUT metadata - likely YOUR originals!\n")

if originals:
    print("Sample files identified as YOURS:")
    for f in sorted(originals, key=lambda x: x.name)[:30]:
        print(f"  ⭐ {f.name}")
        print(f"     Path: {f.relative_to(source)}")
    if len(originals) > 30:
        print(f"\n  ... and {len(originals) - 30} more original files!")

print("\n" + "="*80)
print("📦 COMMERCIAL SAMPLES (WITH METADATA OR KNOWN PRODUCTS):")
print("="*80)
print(f"Found {len(commercial)} files with metadata/commercial patterns\n")

print("\n" + "="*80)
print("SUMMARY:")
print(f"  ⭐⭐⭐ ORIGINAL COMPOSITIONS (NO METADATA): {len(originals)} files ⭐⭐⭐")
print(f"  📦 Commercial Samples (WITH metadata): {len(commercial)} files")
if checking:
    print(f"  ❓ Unclear: {len(checking)} files")
print("="*80)
print("\n⭐ HARD RULE: NO METADATA = YOUR ORIGINAL MUSIC!")
print("\n✓ Ready to run full organizer: python3 organize_by_metadata.py")

