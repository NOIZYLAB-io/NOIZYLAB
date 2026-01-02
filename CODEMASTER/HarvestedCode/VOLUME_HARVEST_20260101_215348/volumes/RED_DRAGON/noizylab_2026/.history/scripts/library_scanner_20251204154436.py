#!/usr/bin/env python3
"""
NoizyLab Audio Library Scanner
Scans and indexes audio files across connected drives.
"""

import os
import json
import hashlib
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, asdict
from typing import Optional, List
import subprocess

AUDIO_EXTENSIONS = {'.wav', '.mp3', '.aif', '.aiff', '.flac', '.ogg', '.m4a'}

@dataclass
class AudioFile:
    path: str
    name: str
    extension: str
    size_bytes: int
    modified: str
    category: Optional[str] = None
    hash_md5: Optional[str] = None
    
def get_audio_category(filename: str) -> str:
    """Categorize audio file based on filename patterns."""
    name_lower = filename.lower()
    
    categories = {
        'Drums': ['drum', 'kick', 'snare', 'hat', 'hihat', 'cymbal', 'perc', 'tom', 'clap'],
        'Bass': ['bass', 'sub', '808'],
        'Synths': ['synth', 'lead', 'pad', 'keys', 'arp', 'pluck'],
        'Vocals': ['vocal', 'vox', 'voice', 'acapella', 'choir'],
        'SFX': ['fx', 'sfx', 'effect', 'riser', 'impact', 'whoosh', 'sweep'],
        'Loops': ['loop', 'break', 'groove'],
        'Guitars': ['guitar', 'gtr', 'acoustic'],
        'Strings': ['string', 'violin', 'cello', 'orchestra'],
    }
    
    for category, keywords in categories.items():
        if any(kw in name_lower for kw in keywords):
            return category
    
    return 'Uncategorized'

def calculate_md5(filepath: Path, chunk_size: int = 8192) -> str:
    """Calculate MD5 hash of a file."""
    md5 = hashlib.md5()
    with open(filepath, 'rb') as f:
        while chunk := f.read(chunk_size):
            md5.update(chunk)
    return md5.hexdigest()

def scan_directory(root_path: str, include_hash: bool = False) -> List[AudioFile]:
    """Scan directory for audio files."""
    audio_files = []
    root = Path(root_path)
    
    if not root.exists():
        print(f"⚠️  Path not found: {root_path}")
        return audio_files
    
    print(f"🔍 Scanning: {root_path}")
    
    for filepath in root.rglob('*'):
        if filepath.is_file() and filepath.suffix.lower() in AUDIO_EXTENSIONS:
            try:
                stat = filepath.stat()
                audio_file = AudioFile(
                    path=str(filepath),
                    name=filepath.name,
                    extension=filepath.suffix.lower(),
                    size_bytes=stat.st_size,
                    modified=datetime.fromtimestamp(stat.st_mtime).isoformat(),
                    category=get_audio_category(filepath.name),
                    hash_md5=calculate_md5(filepath) if include_hash else None
                )
                audio_files.append(audio_file)
            except (PermissionError, OSError) as e:
                print(f"⚠️  Error reading: {filepath} - {e}")
    
    return audio_files

def find_duplicates(audio_files: List[AudioFile]) -> dict:
    """Find duplicate files by size and optionally hash."""
    size_groups = {}
    
    for af in audio_files:
        key = (af.size_bytes, af.name)
        if key not in size_groups:
            size_groups[key] = []
        size_groups[key].append(af)
    
    duplicates = {k: v for k, v in size_groups.items() if len(v) > 1}
    return duplicates

def generate_report(audio_files: List[AudioFile], output_path: str = 'library_report.json'):
    """Generate library report as JSON."""
    
    # Statistics
    total_size = sum(af.size_bytes for af in audio_files)
    by_extension = {}
    by_category = {}
    
    for af in audio_files:
        by_extension[af.extension] = by_extension.get(af.extension, 0) + 1
        by_category[af.category] = by_category.get(af.category, 0) + 1
    
    report = {
        'generated': datetime.now().isoformat(),
        'statistics': {
            'total_files': len(audio_files),
            'total_size_bytes': total_size,
            'total_size_gb': round(total_size / (1024**3), 2),
            'by_extension': by_extension,
            'by_category': by_category,
        },
        'files': [asdict(af) for af in audio_files[:1000]]  # Limit for performance
    }
    
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"📊 Report saved: {output_path}")
    return report

def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='NoizyLab Audio Library Scanner')
    parser.add_argument('paths', nargs='+', help='Paths to scan')
    parser.add_argument('--hash', action='store_true', help='Calculate MD5 hashes')
    parser.add_argument('--duplicates', action='store_true', help='Find duplicates')
    parser.add_argument('--output', default='library_report.json', help='Output file')
    
    args = parser.parse_args()
    
    all_files = []
    for path in args.paths:
        files = scan_directory(path, include_hash=args.hash)
        all_files.extend(files)
        print(f"  Found {len(files)} audio files")
    
    print(f"\n📁 Total: {len(all_files)} audio files")
    
    if args.duplicates:
        dupes = find_duplicates(all_files)
        print(f"🔄 Potential duplicates: {len(dupes)} groups")
    
    report = generate_report(all_files, args.output)
    
    print(f"\n📊 Summary:")
    print(f"   Total size: {report['statistics']['total_size_gb']} GB")
    print(f"   By category:")
    for cat, count in sorted(report['statistics']['by_category'].items(), key=lambda x: -x[1]):
        print(f"      {cat}: {count}")

if __name__ == '__main__':
    main()
