#!/usr/bin/env python3
"""
NoizyLab File Organizer
Organizes audio files into categorized folders.
"""

import shutil
from pathlib import Path
from typing import Dict, List, Optional
import re

AUDIO_EXTENSIONS = {'.wav', '.mp3', '.aif', '.aiff', '.flac', '.ogg', '.m4a'}

CATEGORY_PATTERNS: Dict[str, List[str]] = {
    'Drums/Kicks': ['kick', '808'],
    'Drums/Snares': ['snare', 'snr', 'clap'],
    'Drums/Hi-Hats': ['hat', 'hihat', 'hh', 'open hat', 'closed hat'],
    'Drums/Cymbals': ['cymbal', 'crash', 'ride'],
    'Drums/Percussion': ['perc', 'shaker', 'tamb', 'conga', 'bongo'],
    'Drums/Toms': ['tom'],
    'Bass': ['bass', 'sub', '808 bass'],
    'Synths/Leads': ['lead', 'synth lead'],
    'Synths/Pads': ['pad', 'atmosphere', 'ambient'],
    'Synths/Arps': ['arp', 'arpeggio'],
    'Synths/Plucks': ['pluck'],
    'Keys': ['piano', 'keys', 'organ', 'rhodes', 'wurli'],
    'Guitars': ['guitar', 'gtr', 'acoustic'],
    'Strings': ['string', 'violin', 'cello', 'viola', 'orchestr'],
    'Brass': ['brass', 'trumpet', 'horn', 'trombone', 'sax'],
    'Vocals': ['vocal', 'vox', 'voice', 'acapella', 'choir', 'adlib'],
    'FX/Risers': ['riser', 'build', 'uplifter'],
    'FX/Impacts': ['impact', 'hit', 'downlifter'],
    'FX/Transitions': ['transition', 'sweep', 'whoosh'],
    'FX/Textures': ['texture', 'noise', 'foley'],
    'Loops': ['loop', 'break', 'groove'],
}


def categorize_file(filename: str) -> str:
    """Determine the category for a file based on filename patterns."""
    name_lower = filename.lower()
    
    for category, patterns in CATEGORY_PATTERNS.items():
        for pattern in patterns:
            if pattern in name_lower:
                return category
    
    return 'Uncategorized'


def get_bpm_from_filename(filename: str) -> Optional[int]:
    """Extract BPM from filename if present."""
    patterns = [
        r'(\d{2,3})\s*bpm',
        r'bpm\s*(\d{2,3})',
        r'_(\d{2,3})_',
        r'-(\d{2,3})-',
    ]
    
    for pattern in patterns:
        match = re.search(pattern, filename.lower())
        if match:
            bpm = int(match.group(1))
            if 60 <= bpm <= 200:
                return bpm
    
    return None


def get_key_from_filename(filename: str) -> Optional[str]:
    """Extract musical key from filename if present."""
    pattern = r'\b([A-Ga-g])[#b]?\s*(min|maj|minor|major|m)?\b'
    match = re.search(pattern, filename)
    if match:
        return match.group(0).strip()
    return None


def organize_files(
    source_path: str,
    dest_path: str,
    dry_run: bool = True,
    move_files: bool = False
) -> Dict[str, int]:
    """Organize audio files into categorized folders."""
    source = Path(source_path)
    dest = Path(dest_path)
    
    if not source.exists():
        print(f"❌ Source path not found: {source_path}")
        return {}
    
    stats: Dict[str, int] = {'processed': 0, 'skipped': 0, 'errors': 0}
    category_counts: Dict[str, int] = {}
    
    print(f"🎵 Organizing files from: {source_path}")
    print(f"📁 Destination: {dest_path}")
    print(f"{'🔍 DRY RUN' if dry_run else '⚡ LIVE'}")
    print()
    
    for filepath in source.rglob('*'):
        if not filepath.is_file():
            continue
        if filepath.suffix.lower() not in AUDIO_EXTENSIONS:
            continue
        
        try:
            category = categorize_file(filepath.name)
            category_counts[category] = category_counts.get(category, 0) + 1
            
            # Build destination path
            dest_dir = dest / category
            dest_file = dest_dir / filepath.name
            
            if dry_run:
                print(f"  {filepath.name} → {category}/")
            else:
                dest_dir.mkdir(parents=True, exist_ok=True)
                
                if dest_file.exists():
                    # Add suffix to avoid overwrite
                    base = dest_file.stem
                    suffix = dest_file.suffix
                    counter = 1
                    while dest_file.exists():
                        dest_file = dest_dir / f"{base}_{counter}{suffix}"
                        counter += 1
                
                if move_files:
                    shutil.move(str(filepath), str(dest_file))
                else:
                    shutil.copy2(str(filepath), str(dest_file))
            
            stats['processed'] += 1
            
        except Exception as e:
            print(f"❌ Error: {filepath.name} - {e}")
            stats['errors'] += 1
    
    print("\n📊 Summary:")
    print(f"   Processed: {stats['processed']}")
    print(f"   Errors: {stats['errors']}")
    print("\n📁 By Category:")
    for cat, count in sorted(category_counts.items(), key=lambda x: -x[1]):
        print(f"   {cat}: {count}")
    
    return stats


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='NoizyLab File Organizer')
    parser.add_argument('source', help='Source directory to organize')
    parser.add_argument('dest', help='Destination directory for organized files')
    parser.add_argument('--live', action='store_true', 
                        help='Actually move/copy files (default: dry run)')
    parser.add_argument('--move', action='store_true',
                        help='Move files instead of copy')
    
    args = parser.parse_args()
    
    print("🎵 NoizyLab File Organizer\n")
    
    organize_files(
        args.source,
        args.dest,
        dry_run=not args.live,
        move_files=args.move
    )


if __name__ == '__main__':
    main()
