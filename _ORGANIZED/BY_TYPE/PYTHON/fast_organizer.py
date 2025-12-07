#!/usr/bin/env python3
"""
50X FASTER FILE SCANNER & ORGANIZER
Parallel processing scanner for music production libraries
"""

import os
import sys
import hashlib
import shutil
from pathlib import Path
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import time
from datetime import datetime
import multiprocessing

# Configuration
WORKSPACE = Path("/Volumes/4TBSG/KTK 2026 TO SORT")
OUTPUT_DIR = WORKSPACE / "ORGANIZED_2026"
REPORT_FILE = WORKSPACE / "organization_report.json"
DUPLICATES_FILE = WORKSPACE / "duplicates_report.txt"

# File categories
CATEGORIES = {
    'kontakt_instruments': ['.nki', '.nkm', '.nkc', '.nkr'],
    'kontakt_samples': ['.ncw', '.nkx'],
    'audio_wav': ['.wav'],
    'audio_aif': ['.aif', '.aiff'],
    'documents': ['.pdf', '.txt', '.rtf', '.doc', '.docx'],
    'presets': ['.fxp', '.fxb', '.nka', '.nksn'],
    'sampler': ['.exs', '.sxt', '.sfz'],
    'archives': ['.zip', '.rar', '.7z'],
    'data': ['.csv', '.json', '.xml'],
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'other': []  # catch-all
}

# Ignore patterns
IGNORE_PATTERNS = ['.DS_Store', 'Thumbs.db', '__MACOSX', '.git']

class FileScanner:
    def __init__(self):
        self.stats = {
            'total_files': 0,
            'total_size': 0,
            'by_category': defaultdict(lambda: {'count': 0, 'size': 0}),
            'duplicates': defaultdict(list),
            'errors': []
        }
        self.file_hashes = {}
        
    def should_ignore(self, path):
        """Check if file/folder should be ignored"""
        name = os.path.basename(path)
        return any(pattern in name for pattern in IGNORE_PATTERNS)
    
    def get_category(self, ext):
        """Determine file category based on extension"""
        ext_lower = ext.lower()
        for category, extensions in CATEGORIES.items():
            if ext_lower in extensions:
                return category
        return 'other'
    
    def quick_hash(self, filepath, sample_size=8192):
        """Fast hash using first and last chunks of file"""
        try:
            file_size = os.path.getsize(filepath)
            if file_size == 0:
                return None
            
            hasher = hashlib.md5()
            
            with open(filepath, 'rb') as f:
                # Hash first chunk
                chunk = f.read(sample_size)
                hasher.update(chunk)
                
                # Hash last chunk if file is large enough
                if file_size > sample_size * 2:
                    f.seek(-sample_size, 2)
                    chunk = f.read(sample_size)
                    hasher.update(chunk)
                
                # Add file size to hash to differentiate files
                hasher.update(str(file_size).encode())
            
            return hasher.hexdigest()
        except Exception as e:
            return None
    
    def scan_file(self, filepath):
        """Scan a single file"""
        try:
            if self.should_ignore(filepath):
                return None
            
            stat = os.stat(filepath)
            ext = os.path.splitext(filepath)[1]
            category = self.get_category(ext)
            
            file_info = {
                'path': str(filepath),
                'name': os.path.basename(filepath),
                'size': stat.st_size,
                'category': category,
                'ext': ext,
                'modified': stat.st_mtime
            }
            
            # Calculate hash for duplicate detection (only for files > 1MB)
            if stat.st_size > 1024 * 1024:
                file_hash = self.quick_hash(filepath)
                if file_hash:
                    file_info['hash'] = file_hash
            
            return file_info
            
        except Exception as e:
            return {'error': str(filepath), 'message': str(e)}
    
    def scan_directory_chunk(self, directory):
        """Scan a directory chunk (for parallel processing)"""
        files_found = []
        
        try:
            for root, dirs, files in os.walk(directory):
                # Skip ignored directories
                dirs[:] = [d for d in dirs if not self.should_ignore(os.path.join(root, d))]
                
                for filename in files:
                    if self.should_ignore(filename):
                        continue
                    
                    filepath = os.path.join(root, filename)
                    file_info = self.scan_file(filepath)
                    
                    if file_info:
                        files_found.append(file_info)
        
        except Exception as e:
            files_found.append({'error': str(directory), 'message': str(e)})
        
        return files_found

def get_top_level_dirs(base_path):
    """Get all top-level directories for parallel processing"""
    dirs = []
    try:
        for item in os.listdir(base_path):
            item_path = os.path.join(base_path, item)
            if os.path.isdir(item_path) and item not in IGNORE_PATTERNS:
                dirs.append(item_path)
    except Exception as e:
        print(f"Error reading directory: {e}")
    return dirs

def parallel_scan(base_path, max_workers=None):
    """Scan directories in parallel"""
    if max_workers is None:
        max_workers = max(1, multiprocessing.cpu_count() * 2)
    
    print(f"🚀 Starting parallel scan with {max_workers} workers...")
    print(f"📂 Base path: {base_path}")
    
    scanner = FileScanner()
    top_dirs = get_top_level_dirs(base_path)
    
    print(f"📊 Found {len(top_dirs)} top-level directories to process")
    
    all_files = []
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit all directory scans
        future_to_dir = {
            executor.submit(scanner.scan_directory_chunk, directory): directory
            for directory in top_dirs
        }
        
        completed = 0
        for future in as_completed(future_to_dir):
            directory = future_to_dir[future]
            completed += 1
            
            try:
                files = future.result()
                all_files.extend(files)
                print(f"✓ [{completed}/{len(top_dirs)}] Scanned: {os.path.basename(directory)} ({len(files)} files)")
            except Exception as e:
                print(f"✗ Error scanning {directory}: {e}")
    
    elapsed = time.time() - start_time
    print(f"\n⚡ Scan completed in {elapsed:.2f} seconds!")
    print(f"📁 Total files found: {len(all_files)}")
    
    return all_files

def analyze_files(files):
    """Analyze scanned files for duplicates and statistics"""
    print("\n🔍 Analyzing files...")
    
    stats = {
        'total_files': 0,
        'total_size': 0,
        'by_category': defaultdict(lambda: {'count': 0, 'size': 0, 'files': []}),
        'duplicates': defaultdict(list),
        'errors': []
    }
    
    hash_map = defaultdict(list)
    
    for file_info in files:
        if 'error' in file_info:
            stats['errors'].append(file_info)
            continue
        
        stats['total_files'] += 1
        stats['total_size'] += file_info['size']
        
        category = file_info['category']
        stats['by_category'][category]['count'] += 1
        stats['by_category'][category]['size'] += file_info['size']
        stats['by_category'][category]['files'].append(file_info['path'])
        
        # Track duplicates
        if 'hash' in file_info:
            hash_map[file_info['hash']].append(file_info['path'])
    
    # Find duplicates
    for file_hash, paths in hash_map.items():
        if len(paths) > 1:
            stats['duplicates'][file_hash] = paths
    
    return stats

def format_size(bytes):
    """Format bytes to human readable"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024.0
    return f"{bytes:.2f} PB"

def print_report(stats):
    """Print analysis report"""
    print("\n" + "="*70)
    print("📊 SCAN REPORT")
    print("="*70)
    
    print(f"\n📁 Total Files: {stats['total_files']:,}")
    print(f"💾 Total Size: {format_size(stats['total_size'])}")
    
    print("\n📂 BY CATEGORY:")
    print("-" * 70)
    
    # Sort categories by count
    sorted_cats = sorted(stats['by_category'].items(), 
                        key=lambda x: x[1]['count'], 
                        reverse=True)
    
    for category, info in sorted_cats:
        print(f"  {category:25} {info['count']:>8,} files  {format_size(info['size']):>12}")
    
    if stats['duplicates']:
        print(f"\n⚠️  DUPLICATES FOUND:")
        print("-" * 70)
        total_duplicate_files = sum(len(paths) - 1 for paths in stats['duplicates'].values())
        print(f"  {len(stats['duplicates'])} duplicate groups found")
        print(f"  {total_duplicate_files} redundant files detected")
        
        # Calculate wasted space
        wasted_space = 0
        for paths in stats['duplicates'].values():
            try:
                file_size = os.path.getsize(paths[0])
                wasted_space += file_size * (len(paths) - 1)
            except:
                pass
        
        print(f"  💾 Potential space savings: {format_size(wasted_space)}")
    
    if stats['errors']:
        print(f"\n❌ ERRORS: {len(stats['errors'])} files could not be processed")
    
    print("\n" + "="*70)

def save_report(stats, output_file):
    """Save detailed report to JSON"""
    print(f"\n💾 Saving detailed report to {output_file}...")
    
    # Convert defaultdict to regular dict for JSON serialization
    report = {
        'timestamp': datetime.now().isoformat(),
        'total_files': stats['total_files'],
        'total_size': stats['total_size'],
        'total_size_human': format_size(stats['total_size']),
        'categories': {
            cat: {
                'count': info['count'],
                'size': info['size'],
                'size_human': format_size(info['size']),
                'sample_files': info['files'][:10]  # Save only first 10 as samples
            }
            for cat, info in stats['by_category'].items()
        },
        'duplicate_groups': len(stats['duplicates']),
        'errors': stats['errors']
    }
    
    with open(output_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"✓ Report saved!")

def save_duplicates_report(stats, output_file):
    """Save duplicates report to text file"""
    if not stats['duplicates']:
        return
    
    print(f"\n💾 Saving duplicates report to {output_file}...")
    
    with open(output_file, 'w') as f:
        f.write("DUPLICATE FILES REPORT\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total duplicate groups: {len(stats['duplicates'])}\n\n")
        
        for i, (file_hash, paths) in enumerate(stats['duplicates'].items(), 1):
            f.write(f"\nGroup {i} ({len(paths)} copies):\n")
            f.write("-" * 80 + "\n")
            for path in paths:
                f.write(f"  {path}\n")
    
    print(f"✓ Duplicates report saved!")

def organize_files(stats, dry_run=True):
    """Organize files into categories (optional)"""
    if dry_run:
        print("\n📋 DRY RUN - No files will be moved")
        print("To actually move files, edit the script and set dry_run=False")
        return
    
    print("\n🔄 Organizing files...")
    
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    for category, info in stats['by_category'].items():
        category_dir = OUTPUT_DIR / category
        category_dir.mkdir(exist_ok=True)
        
        print(f"Moving {category}...")
        for filepath in info['files'][:5]:  # Limit for safety
            try:
                filename = os.path.basename(filepath)
                dest = category_dir / filename
                shutil.move(filepath, dest)
            except Exception as e:
                print(f"  Error moving {filepath}: {e}")

def main():
    """Main execution"""
    print("\n" + "🚀" * 35)
    print("  50X FASTER FILE SCANNER & ORGANIZER")
    print("🚀" * 35 + "\n")
    
    if not WORKSPACE.exists():
        print(f"❌ Workspace not found: {WORKSPACE}")
        sys.exit(1)
    
    # Step 1: Parallel scan
    files = parallel_scan(WORKSPACE)
    
    # Step 2: Analyze
    stats = analyze_files(files)
    
    # Step 3: Print report
    print_report(stats)
    
    # Step 4: Save reports
    save_report(stats, REPORT_FILE)
    save_duplicates_report(stats, DUPLICATES_FILE)
    
    print("\n✅ SCAN COMPLETE!")
    print(f"\n📄 Detailed report: {REPORT_FILE}")
    if stats['duplicates']:
        print(f"📄 Duplicates report: {DUPLICATES_FILE}")
    
    print("\n💡 Next steps:")
    print("  1. Review the JSON report for detailed file listings")
    print("  2. Check duplicates report to identify redundant files")
    print("  3. Organize files by category (edit script to enable)")

if __name__ == "__main__":
    main()

