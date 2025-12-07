#!/usr/bin/env python3
"""
AUTO ORGANIZER - Intelligently organize files into proper structure
"""

import os
import shutil
import json
from pathlib import Path
from datetime import datetime

WORKSPACE = Path("/Volumes/4TBSG/KTK 2026 TO SORT")
ORGANIZED_DIR = WORKSPACE / "ORGANIZED_2026"
REPORT_FILE = WORKSPACE / "organization_report.json"
ORGANIZE_LOG = WORKSPACE / "organization_log.json"

# Enhanced organization structure
ORGANIZATION_STRUCTURE = {
    'Kontakt_Libraries': {
        'Instruments': ['.nki', '.nkm', '.nkc', '.nkr'],
        'Samples': ['.ncw', '.nkx']
    },
    'Audio_Samples': {
        'WAV': ['.wav'],
        'AIFF': ['.aif', '.aiff'],
        'Other': ['.mp3', '.flac', '.ogg']
    },
    'Sampler_Instruments': {
        'EXS24': ['.exs'],
        'Kontakt': ['.nki', '.nkm'],
        'SFZ': ['.sfz'],
        'Other': ['.sxt']
    },
    'Presets': {
        'VST': ['.fxp', '.fxb'],
        'Native': ['.nka', '.nksn', '.nkp']
    },
    'Documentation': {
        'PDFs': ['.pdf'],
        'Text': ['.txt', '.rtf', '.doc', '.docx'],
        'Manuals': []  # Will use smart detection
    },
    'Archives': {
        'Compressed': ['.zip', '.rar', '.7z', '.tar', '.gz']
    },
    'Data': {
        'Metadata': ['.csv', '.json', '.xml', '.nfo']
    }
}

def get_vendor_from_path(filepath):
    """Extract vendor/brand name from path"""
    path_parts = Path(filepath).parts
    
    # Known vendors
    vendors = [
        'Spitfire', 'Native Instruments', 'Kontakt', 'Output', 
        'Soundiron', 'ProjectSam', 'CineSamples', '8Dio',
        'Audiobro', 'EastWest', 'Big Fish Audio', 'Samples From Mars',
        'Akai', 'Roland', 'Best Service', 'Auddict'
    ]
    
    for part in path_parts:
        for vendor in vendors:
            if vendor.lower() in part.lower():
                return vendor
    
    return 'Unknown_Vendor'

def get_instrument_type(filepath, filename):
    """Determine instrument type from path and name"""
    path_lower = filepath.lower()
    name_lower = filename.lower()
    
    types = {
        'Strings': ['string', 'violin', 'cello', 'viola', 'bass', 'orchestra'],
        'Brass': ['brass', 'trumpet', 'trombone', 'horn', 'tuba'],
        'Woodwinds': ['woodwind', 'flute', 'clarinet', 'oboe', 'bassoon', 'sax'],
        'Percussion': ['percussion', 'drum', 'cymbal', 'kick', 'snare', 'hit'],
        'Keyboards': ['piano', 'keys', 'organ', 'synth', 'pad'],
        'Guitars': ['guitar', 'bass', 'banjo', 'mandolin'],
        'Vocals': ['vocal', 'voice', 'choir', 'vox'],
        'Ethnic': ['ethnic', 'world', 'exotic', 'tribal'],
        'SFX': ['sfx', 'sound effect', 'ambience', 'texture', 'cinematic']
    }
    
    for category, keywords in types.items():
        if any(kw in path_lower or kw in name_lower for kw in keywords):
            return category
    
    return 'Other'

def smart_organize_path(filepath):
    """Determine the best organized path for a file"""
    filename = os.path.basename(filepath)
    ext = os.path.splitext(filename)[1].lower()
    
    # Get vendor
    vendor = get_vendor_from_path(filepath)
    
    # Get instrument type
    inst_type = get_instrument_type(filepath, filename)
    
    # Determine category
    if ext in ['.nki', '.nkm', '.nkc', '.nkr']:
        category = 'Kontakt_Libraries'
        subcategory = 'Instruments'
        organized_path = ORGANIZED_DIR / category / vendor / inst_type / subcategory / filename
        
    elif ext in ['.ncw', '.nkx']:
        category = 'Kontakt_Libraries'
        subcategory = 'Samples'
        # Keep samples close to their instruments
        organized_path = ORGANIZED_DIR / category / vendor / inst_type / subcategory / filename
        
    elif ext in ['.wav', '.aif', '.aiff']:
        category = 'Audio_Samples'
        subcategory = 'WAV' if ext == '.wav' else 'AIFF'
        organized_path = ORGANIZED_DIR / category / inst_type / subcategory / filename
        
    elif ext in ['.exs', '.sfz', '.sxt']:
        category = 'Sampler_Instruments'
        subcategory = {'exs': 'EXS24', 'sfz': 'SFZ', 'sxt': 'Other'}.get(ext[1:], 'Other')
        organized_path = ORGANIZED_DIR / category / subcategory / vendor / filename
        
    elif ext in ['.fxp', '.fxb', '.nka', '.nksn']:
        category = 'Presets'
        subcategory = 'VST' if ext in ['.fxp', '.fxb'] else 'Native'
        organized_path = ORGANIZED_DIR / category / subcategory / vendor / filename
        
    elif ext in ['.pdf', '.txt', '.rtf', '.doc', '.docx']:
        category = 'Documentation'
        subcategory = 'PDFs' if ext == '.pdf' else 'Text'
        organized_path = ORGANIZED_DIR / category / vendor / subcategory / filename
        
    elif ext in ['.zip', '.rar', '.7z']:
        category = 'Archives'
        organized_path = ORGANIZED_DIR / category / filename
        
    else:
        category = 'Other'
        organized_path = ORGANIZED_DIR / category / filename
    
    return organized_path

def organize_files(dry_run=True, limit=None):
    """Organize files into structured folders"""
    
    print("\n" + "="*70)
    print("📁 AUTO ORGANIZER")
    print("="*70)
    
    if dry_run:
        print("\n⚠️  DRY RUN MODE - No files will be moved")
        print("Set dry_run=False to actually organize files\n")
    else:
        print("\n🔴 LIVE MODE - Files will be moved!")
        ORGANIZED_DIR.mkdir(exist_ok=True)
    
    # Load file list from report
    with open(REPORT_FILE, 'r') as f:
        report = json.load(f)
    
    files_to_organize = []
    
    # Collect files from report
    for category, info in report['categories'].items():
        if 'sample_files' in info:
            files_to_organize.extend(info['sample_files'])
    
    print(f"📊 Found {len(files_to_organize)} sample files in report")
    print(f"⚠️  Note: Report only contains samples. Scanning workspace for all files...\n")
    
    # Full scan
    all_files = []
    for root, dirs, files in os.walk(WORKSPACE):
        # Skip organized directory and temp directories
        if 'ORGANIZED_2026' in root or '_DUPLICATES_' in root:
            continue
        
        for filename in files:
            if filename.startswith('.') or filename.endswith(('.py', '.json', '.txt', '.log')):
                continue
            
            filepath = os.path.join(root, filename)
            all_files.append(filepath)
    
    if limit:
        all_files = all_files[:limit]
    
    print(f"📂 Processing {len(all_files)} files...")
    
    organized_count = 0
    errors = []
    moves = []
    
    for i, filepath in enumerate(all_files, 1):
        try:
            new_path = smart_organize_path(filepath)
            
            if i <= 20:  # Show first 20 moves
                print(f"\n[{i}] {os.path.basename(filepath)}")
                print(f"  FROM: {filepath}")
                print(f"  TO:   {new_path}")
            elif i == 21:
                print(f"\n... processing remaining files ...")
            
            if not dry_run:
                new_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(filepath, new_path)
            
            moves.append({
                'original': str(filepath),
                'organized': str(new_path),
                'timestamp': datetime.now().isoformat()
            })
            
            organized_count += 1
            
            if i % 100 == 0:
                print(f"  Progress: {i}/{len(all_files)} files processed...", end='\r')
            
        except Exception as e:
            errors.append({'file': filepath, 'error': str(e)})
    
    print("\n\n" + "="*70)
    print("📊 ORGANIZATION SUMMARY")
    print("="*70)
    print(f"Files organized: {organized_count}")
    print(f"Errors: {len(errors)}")
    
    if not dry_run:
        # Save log
        log_data = {
            'timestamp': datetime.now().isoformat(),
            'files_organized': organized_count,
            'errors': errors,
            'moves': moves[:100]  # Save first 100 as samples
        }
        
        with open(ORGANIZE_LOG, 'w') as f:
            json.dump(log_data, f, indent=2)
        
        print(f"\n✓ Organization log saved to: {ORGANIZE_LOG}")
    
    print(f"\n📁 Organized directory: {ORGANIZED_DIR}")

def main():
    print("\n" + "📁"*35)
    print("  INTELLIGENT AUTO ORGANIZER")
    print("📁"*35 + "\n")
    
    if not REPORT_FILE.exists():
        print("❌ No scan report found!")
        print("Please run fast_organizer.py first to scan your files.")
        return
    
    # Run organization in dry-run mode
    organize_files(dry_run=True, limit=1000)  # Limit to first 1000 for preview
    
    print("\n💡 To actually organize files:")
    print("   Edit this script and set dry_run=False")
    print("\n⚠️  ALWAYS backup your files before organizing!")

if __name__ == "__main__":
    main()

