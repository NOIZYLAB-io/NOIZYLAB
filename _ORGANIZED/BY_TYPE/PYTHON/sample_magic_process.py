#!/usr/bin/env python3
"""Fast Sample_Magic processor - Deep scan, rename, move to 6TB"""
import os, hashlib, shutil, json, wave, struct
from pathlib import Path
from collections import defaultdict
from datetime import datetime

SOURCE = "/Volumes/6TB/Sample_Libraries/Sample_Magic"
TARGET = "/Volumes/6TB/_ORGANIZED/Sample_Magic"
REPORT = "/Users/m2ultra/sample_magic_report"

stats = {'total': 0, 'valid': 0, 'moved': 0, 'errors': [], 'categories': defaultdict(int), 'dupes': []}
hash_map = {}

CATEGORIES = {
    'bass': 'Bass', 'kick': 'Drums/Kicks', 'snare': 'Drums/Snares', 'hat': 'Drums/HiHats',
    'clap': 'Drums/Claps', 'perc': 'Drums/Percussion', 'drum': 'Drums', 'loop': 'Loops',
    'synth': 'Synths', 'pad': 'Pads', 'fx': 'FX', 'vocal': 'Vocals', 'chord': 'Chords',
    'lead': 'Leads', 'stab': 'Stabs', 'top': 'Tops', 'music': 'Musical', 'atmos': 'Atmospheres'
}

def categorize(filepath):
    name = filepath.lower()
    for key, cat in CATEGORIES.items():
        if key in name: return cat
    return 'Other'

def get_hash(path):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''): h.update(chunk)
    return h.hexdigest()

def process_file(src_path, target_base):
    global stats
    try:
        src = Path(src_path)
        if not src.suffix.lower() in ['.wav', '.aif', '.aiff', '.mp3']: return
        
        stats['total'] += 1
        file_hash = get_hash(src)
        
        # Check duplicate
        if file_hash in hash_map:
            stats['dupes'].append({'file': str(src), 'duplicate_of': hash_map[file_hash]})
            return
        hash_map[file_hash] = str(src)
        
        # Categorize
        cat = categorize(str(src))
        stats['categories'][cat] += 1
        
        # Clean filename
        name = src.stem
        name = name.replace('_', ' ').replace('-', ' ')
        name = ' '.join(name.split())
        new_name = f"SM_{name}{src.suffix}"
        
        # Target path
        target_dir = target_base / cat
        target_dir.mkdir(parents=True, exist_ok=True)
        target_file = target_dir / new_name
        
        # Handle conflicts
        counter = 1
        while target_file.exists():
            target_file = target_dir / f"SM_{name}_{counter:03d}{src.suffix}"
            counter += 1
        
        # Move file
        shutil.copy2(src, target_file)
        stats['valid'] += 1
        stats['moved'] += 1
        
    except Exception as e:
        stats['errors'].append({'file': str(src_path), 'error': str(e)})

def main():
    print("🚀 SAMPLE MAGIC - DEEP SCAN & ORGANIZE")
    print("=" * 50)
    
    target_base = Path(TARGET)
    target_base.mkdir(parents=True, exist_ok=True)
    
    # Collect all files
    files = []
    for root, _, filenames in os.walk(SOURCE):
        for f in filenames:
            files.append(os.path.join(root, f))
    
    total = len(files)
    print(f"📁 Found {total} files to process")
    
    # Process
    for i, f in enumerate(files):
        if i % 100 == 0: print(f"⚡ Processing: {i}/{total} ({i*100//total}%)")
        process_file(f, target_base)
    
    print(f"\n✅ COMPLETE!")
    print(f"   Total scanned: {stats['total']}")
    print(f"   Valid/Moved: {stats['moved']}")
    print(f"   Duplicates: {len(stats['dupes'])}")
    print(f"   Errors: {len(stats['errors'])}")
    print(f"\n📊 Categories:")
    for cat, count in sorted(stats['categories'].items(), key=lambda x: -x[1]):
        print(f"   {cat}: {count}")
    
    # Save report
    Path(REPORT).mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"{REPORT}/sample_magic_{ts}.json", 'w') as f:
        json.dump({'stats': dict(stats['categories']), 'dupes': stats['dupes'], 'errors': stats['errors']}, f, indent=2)
    print(f"\n📄 Report: {REPORT}/sample_magic_{ts}.json")

if __name__ == '__main__': main()
