#!/usr/bin/env python3
"""
SMART FILE ORGANIZER - Intelligent file organization
Features:
- Auto-organize by file type
- Consolidate scattered files
- Create logical folder structures
- Rename files with better conventions
- Handle duplicates intelligently
"""

import os
import shutil
from pathlib import Path
from collections import defaultdict
import re
import argparse

ROOT = '/Volumes/MAG 4TB'

# File type categories
FILE_CATEGORIES = {
    'Audio Samples': {
        'extensions': ['.wav', '.aiff', '.aif', '.flac', '.mp3', '.ogg', '.m4a'],
        'organize_by': ['instrument', 'type']
    },
    'MIDI': {
        'extensions': ['.mid', '.midi'],
        'organize_by': ['style', 'tempo']
    },
    'Presets': {
        'extensions': ['.preset', '.fxp', '.vstpreset', '.nksf'],
        'organize_by': ['plugin']
    },
    'Projects': {
        'extensions': ['.als', '.logic', '.flp', '.rpp', '.cpr', '.ptx'],
        'organize_by': ['daw', 'date']
    },
    'Loops': {
        'extensions': ['.rex', '.rx2', '.acid', '.aiff', '.wav'],
        'patterns': ['loop', 'loops'],
        'organize_by': ['bpm', 'key']
    },
    'Code': {
        'extensions': ['.py', '.js', '.sh', '.json', '.txt', '.md'],
        'organize_by': ['language']
    },
    'Documents': {
        'extensions': ['.pdf', '.doc', '.docx', '.txt', '.md'],
        'organize_by': ['type']
    },
    'Images': {
        'extensions': ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp'],
        'organize_by': ['purpose']
    }
}

def extract_metadata_from_filename(filename):
    """Extract metadata from filename"""
    metadata = {
        'bpm': None,
        'key': None,
        'instrument': None,
        'style': None
    }
    
    # Extract BPM
    bpm_match = re.search(r'(\d{2,3})\s*bpm', filename.lower())
    if bpm_match:
        metadata['bpm'] = bpm_match.group(1)
    
    # Extract key
    key_match = re.search(r'([A-G][#b]?)\s*(maj|min|major|minor)', filename.lower())
    if key_match:
        metadata['key'] = f"{key_match.group(1)}_{key_match.group(2)}"
    
    # Extract instruments
    instruments = ['kick', 'snare', 'hihat', 'bass', 'lead', 'pad', 'synth', 
                   'guitar', 'piano', 'drum', 'perc', 'vocal', 'fx']
    for inst in instruments:
        if inst in filename.lower():
            metadata['instrument'] = inst
            break
    
    return metadata

def suggest_organization(filepath):
    """Suggest where a file should be organized"""
    filename = os.path.basename(filepath)
    ext = os.path.splitext(filename)[1].lower()
    
    for category, config in FILE_CATEGORIES.items():
        if ext in config['extensions']:
            metadata = extract_metadata_from_filename(filename)
            
            # Build suggested path
            parts = [category]
            
            if 'organize_by' in config:
                for org_type in config['organize_by']:
                    if org_type == 'bpm' and metadata['bpm']:
                        parts.append(f"BPM_{metadata['bpm']}")
                    elif org_type == 'key' and metadata['key']:
                        parts.append(metadata['key'])
                    elif org_type == 'instrument' and metadata['instrument']:
                        parts.append(metadata['instrument'].title())
            
            return os.path.join(*parts)
    
    return None

def analyze_organization(root):
    """Analyze current file organization"""
    print("="*80)
    print("FILE ORGANIZATION ANALYSIS")
    print("="*80)
    
    files_by_category = defaultdict(list)
    scattered_files = []
    
    print("\nScanning files...")
    file_count = 0
    
    for dirpath, dirnames, filenames in os.walk(root):
        # Skip certain directories
        if any(skip in dirpath for skip in ['.git', '__pycache__', 'NoizyWorkspace', '.Trash']):
            continue
        
        for filename in filenames:
            if filename.startswith('.'):
                continue
            
            filepath = os.path.join(dirpath, filename)
            file_count += 1
            
            if file_count % 10000 == 0:
                print(f"  Processed {file_count:,} files", end='\r')
            
            # Categorize file
            ext = os.path.splitext(filename)[1].lower()
            category = None
            
            for cat, config in FILE_CATEGORIES.items():
                if ext in config['extensions']:
                    category = cat
                    break
            
            if category:
                files_by_category[category].append(filepath)
                
                # Check if file is in a scattered location
                if category.lower() not in dirpath.lower():
                    scattered_files.append((filepath, category))
    
    print(f"\n\nTotal files analyzed: {file_count:,}")
    
    # Print category summary
    print("\n### FILES BY CATEGORY ###")
    for category, files in sorted(files_by_category.items(), key=lambda x: -len(x[1])):
        total_size = sum(os.path.getsize(f) for f in files if os.path.exists(f))
        size_gb = total_size / (1024**3)
        print(f"  {len(files):>7,} files - {size_gb:>8.2f} GB - {category}")
    
    # Print scattered files summary
    print(f"\n### SCATTERED FILES ###")
    print(f"Total scattered files: {len(scattered_files):,}")
    
    scattered_by_cat = defaultdict(list)
    for fp, cat in scattered_files:
        scattered_by_cat[cat].append(fp)
    
    for category, files in sorted(scattered_by_cat.items(), key=lambda x: -len(x[1])):
        print(f"\n{category}: {len(files):,} scattered files")
        for fp in files[:5]:
            print(f"  {fp}")
        if len(files) > 5:
            print(f"  ... and {len(files) - 5} more")
    
    return files_by_category, scattered_files

def auto_organize(root, dry_run=True):
    """Auto-organize files into logical structure"""
    print("\n" + "="*80)
    print("AUTO ORGANIZATION")
    print("="*80)
    
    organize_root = os.path.join(root, '_ORGANIZED')
    
    if not dry_run:
        os.makedirs(organize_root, exist_ok=True)
    
    print(f"\nTarget: {organize_root}")
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
    
    actions = []
    
    print("\nScanning and organizing...")
    file_count = 0
    organized_count = 0
    
    for dirpath, dirnames, filenames in os.walk(root):
        # Skip organized folder and special directories
        if organize_root in dirpath or any(skip in dirpath for skip in ['.git', '__pycache__', '.Trash']):
            continue
        
        for filename in filenames:
            if filename.startswith('.'):
                continue
            
            filepath = os.path.join(dirpath, filename)
            file_count += 1
            
            # Get suggested organization
            suggested_path = suggest_organization(filepath)
            
            if suggested_path:
                new_location = os.path.join(organize_root, suggested_path)
                new_filepath = os.path.join(new_location, filename)
                
                if dry_run:
                    action = f"[DRY RUN] {filepath} -> {new_filepath}"
                    actions.append(action)
                    organized_count += 1
                else:
                    try:
                        os.makedirs(new_location, exist_ok=True)
                        
                        # Handle filename conflicts
                        if os.path.exists(new_filepath):
                            base, ext = os.path.splitext(filename)
                            counter = 1
                            while os.path.exists(new_filepath):
                                new_filepath = os.path.join(new_location, f"{base}_{counter}{ext}")
                                counter += 1
                        
                        shutil.copy2(filepath, new_filepath)
                        action = f"Organized: {filepath} -> {new_filepath}"
                        actions.append(action)
                        organized_count += 1
                    except Exception as e:
                        action = f"Error: {filepath} - {str(e)}"
                        actions.append(action)
            
            if file_count % 1000 == 0:
                print(f"  Processed: {file_count:,} | Organized: {organized_count:,}", end='\r')
    
    print(f"\n\nTotal files scanned: {file_count:,}")
    print(f"Files organized: {organized_count:,}")
    
    return actions

def rename_files_smartly(root, dry_run=True):
    """Rename files with better conventions"""
    print("\n" + "="*80)
    print("SMART RENAME")
    print("="*80)
    
    actions = []
    
    patterns_to_clean = [
        (r'\s+', '_'),  # Multiple spaces to underscore
        (r'_+', '_'),   # Multiple underscores to single
        (r'^[\s_-]+', ''),  # Leading whitespace/underscore
        (r'[\s_-]+$', ''),  # Trailing whitespace/underscore
        (r'[^\w\s\-\.]', ''),  # Remove special chars
    ]
    
    print("\nScanning for files to rename...")
    file_count = 0
    rename_count = 0
    
    for dirpath, dirnames, filenames in os.walk(root):
        if any(skip in dirpath for skip in ['.git', '__pycache__', '.Trash']):
            continue
        
        for filename in filenames:
            if filename.startswith('.'):
                continue
            
            filepath = os.path.join(dirpath, filename)
            file_count += 1
            
            # Apply cleaning patterns
            new_name = filename
            for pattern, replacement in patterns_to_clean:
                new_name = re.sub(pattern, replacement, new_name)
            
            # Check if name changed
            if new_name != filename:
                new_filepath = os.path.join(dirpath, new_name)
                
                if dry_run:
                    action = f"[DRY RUN] Rename: {filename} -> {new_name}"
                    actions.append(action)
                    rename_count += 1
                else:
                    try:
                        # Handle conflicts
                        if os.path.exists(new_filepath):
                            base, ext = os.path.splitext(new_name)
                            counter = 1
                            while os.path.exists(new_filepath):
                                new_filepath = os.path.join(dirpath, f"{base}_{counter}{ext}")
                                counter += 1
                        
                        os.rename(filepath, new_filepath)
                        action = f"Renamed: {filename} -> {os.path.basename(new_filepath)}"
                        actions.append(action)
                        rename_count += 1
                    except Exception as e:
                        action = f"Error renaming {filename}: {str(e)}"
                        actions.append(action)
            
            if file_count % 10000 == 0:
                print(f"  Scanned: {file_count:,} | To rename: {rename_count:,}", end='\r')
    
    print(f"\n\nTotal files scanned: {file_count:,}")
    print(f"Files to rename: {rename_count:,}")
    
    if rename_count > 0:
        print("\nFirst 20 renames:")
        for action in actions[:20]:
            print(f"  {action}")
    
    return actions

def main():
    parser = argparse.ArgumentParser(description='Smart File Organizer')
    parser.add_argument('--analyze', action='store_true', help='Analyze current organization')
    parser.add_argument('--organize', action='store_true', help='Auto-organize files')
    parser.add_argument('--rename', action='store_true', help='Smart rename files')
    parser.add_argument('--live', action='store_true', help='Execute actions (default is dry-run)')
    parser.add_argument('--all', action='store_true', help='Run all operations')
    
    args = parser.parse_args()
    
    dry_run = not args.live
    
    print("="*80)
    print("SMART FILE ORGANIZER v2.0")
    print("="*80)
    print(f"Root: {ROOT}")
    print(f"Mode: {'LIVE' if not dry_run else 'DRY RUN'}")
    print()
    
    if dry_run:
        print("⚠️  DRY RUN MODE - No files will be modified")
        print("   Use --live to execute actions")
        print()
    
    if args.all or args.analyze:
        analyze_organization(ROOT)
    
    if args.all or args.organize:
        auto_organize(ROOT, dry_run)
    
    if args.all or args.rename:
        rename_files_smartly(ROOT, dry_run)
    
    if not any([args.all, args.analyze, args.organize, args.rename]):
        parser.print_help()

if __name__ == '__main__':
    main()

