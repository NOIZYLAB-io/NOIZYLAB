#!/usr/bin/env python3
"""
NoizyLab Duplicate Finder
Finds duplicate audio files using content hashing.
"""

import hashlib
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple
import json
from datetime import datetime

AUDIO_EXTENSIONS = {'.wav', '.mp3', '.aif', '.aiff', '.flac', '.ogg', '.m4a'}

def get_file_hash(filepath: Path, chunk_size: int = 65536) -> str:
    """Calculate SHA256 hash of file content."""
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(chunk_size):
            sha256.update(chunk)
    return sha256.hexdigest()

def get_quick_hash(filepath: Path, sample_size: int = 4096) -> Tuple[int, str]:
    """Get quick hash using file size + first/last bytes."""
    size = filepath.stat().st_size
    
    with open(filepath, 'rb') as f:
        first = f.read(sample_size)
        if size > sample_size * 2:
            f.seek(-sample_size, 2)
        last = f.read(sample_size)
    
    quick_hash = hashlib.md5(first + last).hexdigest()
    return (size, quick_hash)

def find_duplicates(root_paths: List[str], full_hash: bool = False) -> Dict[str, List[str]]:
    """Find duplicate files across multiple paths."""
    
    # Phase 1: Group by size
    print("📊 Phase 1: Grouping by file size...")
    size_groups: Dict[int, List[Path]] = defaultdict(list)
    total_files = 0
    
    for root_path in root_paths:
        root = Path(root_path)
        if not root.exists():
            print(f"⚠️  Path not found: {root_path}")
            continue
            
        for filepath in root.rglob('*'):
            if filepath.is_file() and filepath.suffix.lower() in AUDIO_EXTENSIONS:
                try:
                    size = filepath.stat().st_size
                    size_groups[size].append(filepath)
                    total_files += 1
                except (PermissionError, OSError):
                    pass
    
    print(f"   Found {total_files} audio files")
    
    # Phase 2: Quick hash files with same size
    print("🔍 Phase 2: Quick hashing potential duplicates...")
    quick_hash_groups: Dict[Tuple[int, str], List[Path]] = defaultdict(list)
    potential_dupes = 0
    
    for size, files in size_groups.items():
        if len(files) > 1:
            for filepath in files:
                try:
                    quick_hash = get_quick_hash(filepath)
                    quick_hash_groups[quick_hash].append(filepath)
                    potential_dupes += 1
                except (PermissionError, OSError):
                    pass
    
    print(f"   Potential duplicates: {potential_dupes}")
    
    # Phase 3: Full hash verification (optional)
    duplicates: Dict[str, List[str]] = {}
    
    if full_hash:
        print("🔐 Phase 3: Full hash verification...")
        for quick_key, files in quick_hash_groups.items():
            if len(files) > 1:
                full_hash_groups: Dict[str, List[str]] = defaultdict(list)
                for filepath in files:
                    try:
                        full = get_file_hash(filepath)
                        full_hash_groups[full].append(str(filepath))
                    except (PermissionError, OSError):
                        pass
                
                for hash_key, paths in full_hash_groups.items():
                    if len(paths) > 1:
                        duplicates[hash_key] = paths
    else:
        # Use quick hash results
        for quick_key, files in quick_hash_groups.items():
            if len(files) > 1:
                key = f"size_{quick_key[0]}_hash_{quick_key[1]}"
                duplicates[key] = [str(f) for f in files]
    
    return duplicates

def calculate_savings(duplicates: Dict[str, List[str]]) -> Tuple[int, int]:
    """Calculate potential disk space savings."""
    total_waste = 0
    total_files = 0
    
    for hash_key, paths in duplicates.items():
        if paths:
            file_size = Path(paths[0]).stat().st_size
            # Keep one, count the rest as waste
            duplicate_count = len(paths) - 1
            total_waste += file_size * duplicate_count
            total_files += duplicate_count
    
    return total_files, total_waste

def generate_report(duplicates: Dict[str, List[str]], output_path: str):
    """Generate duplicate report."""
    
    files_to_remove, bytes_to_save = calculate_savings(duplicates)
    
    report = {
        'generated': datetime.now().isoformat(),
        'summary': {
            'duplicate_groups': len(duplicates),
            'files_to_remove': files_to_remove,
            'bytes_to_save': bytes_to_save,
            'gb_to_save': round(bytes_to_save / (1024**3), 2),
        },
        'duplicates': duplicates
    }
    
    with open(output_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    return report

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='NoizyLab Duplicate Finder')
    parser.add_argument('paths', nargs='+', help='Paths to scan for duplicates')
    parser.add_argument('--full-hash', action='store_true', help='Use full SHA256 hash (slower)')
    parser.add_argument('--output', default='duplicates_report.json', help='Output file')
    parser.add_argument('--dry-run', action='store_true', help='Show what would be deleted')
    
    args = parser.parse_args()
    
    print("🎵 NoizyLab Duplicate Finder\n")
    
    duplicates = find_duplicates(args.paths, full_hash=args.full_hash)
    
    print(f"\n✅ Found {len(duplicates)} duplicate groups")
    
    if duplicates:
        report = generate_report(duplicates, args.output)
        
        print("\n📊 Summary:")
        print(f"   Duplicate groups: {report['summary']['duplicate_groups']}")
        print(f"   Files to remove: {report['summary']['files_to_remove']}")
        print(f"   Space to save: {report['summary']['gb_to_save']} GB")
        print(f"\n📄 Report saved: {args.output}")
        
        if args.dry_run:
            print("\n🔍 Dry run - duplicates found:")
            for i, (hash_key, paths) in enumerate(list(duplicates.items())[:10]):
                print(f"\n   Group {i+1}:")
                for path in paths:
                    print(f"      - {path}")
            if len(duplicates) > 10:
                print(f"\n   ... and {len(duplicates) - 10} more groups")
    else:
        print("   No duplicates found! 🎉")

if __name__ == '__main__':
    main()
