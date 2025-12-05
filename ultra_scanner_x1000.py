#!/usr/bin/env python3
"""
ULTRA SCANNER X1000 - MULTI-DRIVE EDITION
Scan multiple drives simultaneously for:
- Broken/corrupted files
- Duplicates across ALL drives
- File integrity issues
- Maximum parallel processing
"""

import os
import sys
import hashlib
import json
from pathlib import Path
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import multiprocessing
import time

# DRIVES TO SCAN
DRIVES = [
    Path("/Volumes/6TB"),
    Path("/Volumes/4TBSG"),
]

OUTPUT_DIR = Path("/Volumes/4TBSG/SCAN_RESULTS")
OUTPUT_DIR.mkdir(exist_ok=True)

BROKEN_FILES_REPORT = OUTPUT_DIR / "broken_files_report.json"
CROSS_DRIVE_DUPES = OUTPUT_DIR / "cross_drive_duplicates.json"
MULTI_DRIVE_REPORT = OUTPUT_DIR / "multi_drive_analysis.json"
QUICK_SUMMARY = OUTPUT_DIR / "SCAN_SUMMARY.txt"

# File extensions to check for corruption
CHECKABLE_EXTENSIONS = {
    '.wav', '.aif', '.aiff', '.mp3', '.flac', '.ogg',  # Audio
    '.nki', '.nkm', '.nkc', '.ncw', '.nkx',  # Kontakt
    '.exs', '.sfz', '.sxt',  # Samplers
    '.zip', '.rar', '.7z',  # Archives
    '.pdf', '.jpg', '.png'  # Documents/Images
}

class UltraScanner:
    def __init__(self):
        self.all_files = {}  # hash -> [file_paths]
        self.broken_files = []
        self.drive_stats = defaultdict(lambda: {
            'total_files': 0,
            'total_size': 0,
            'broken': 0,
            'by_extension': defaultdict(int)
        })
        self.max_workers = multiprocessing.cpu_count() * 4  # X1000 MODE!
        
    def quick_hash(self, filepath, sample_size=16384):
        """Ultra-fast hash using strategic sampling"""
        try:
            file_size = os.path.getsize(filepath)
            if file_size == 0:
                return None
            
            hasher = hashlib.md5()
            hasher.update(str(file_size).encode())
            
            with open(filepath, 'rb') as f:
                # Read first chunk
                chunk = f.read(sample_size)
                if not chunk:
                    return None
                hasher.update(chunk)
                
                # Read middle chunk for larger files
                if file_size > sample_size * 3:
                    f.seek(file_size // 2)
                    chunk = f.read(sample_size)
                    hasher.update(chunk)
                
                # Read last chunk
                if file_size > sample_size * 2:
                    f.seek(-min(sample_size, file_size), 2)
                    chunk = f.read(sample_size)
                    hasher.update(chunk)
            
            return hasher.hexdigest()
            
        except Exception as e:
            return None
    
    def check_file_integrity(self, filepath):
        """Check if file is readable and not corrupted"""
        try:
            ext = os.path.splitext(filepath)[1].lower()
            
            # Check if file is readable
            with open(filepath, 'rb') as f:
                # Try to read first and last bytes
                f.read(1)
                file_size = os.path.getsize(filepath)
                if file_size > 1:
                    f.seek(-1, 2)
                    f.read(1)
            
            # Additional checks for specific file types
            if ext in {'.wav', '.aif', '.aiff'}:
                return self._check_audio_file(filepath)
            elif ext in {'.zip', '.rar', '.7z'}:
                return self._check_archive_file(filepath)
            elif ext in {'.nki', '.nkm'}:
                return self._check_kontakt_file(filepath)
            
            return True
            
        except Exception as e:
            return False
    
    def _check_audio_file(self, filepath):
        """Basic audio file validation"""
        try:
            # Check file has reasonable size (>100 bytes)
            size = os.path.getsize(filepath)
            if size < 100:
                return False
            
            # Check for common audio headers
            with open(filepath, 'rb') as f:
                header = f.read(12)
                
                # WAV check
                if filepath.lower().endswith('.wav'):
                    if not (header[:4] == b'RIFF' and header[8:12] == b'WAVE'):
                        return False
                
                # AIFF check
                elif filepath.lower().endswith(('.aif', '.aiff')):
                    if not (header[:4] == b'FORM' and header[8:12] == b'AIFF'):
                        return False
            
            return True
        except:
            return False
    
    def _check_archive_file(self, filepath):
        """Basic archive file validation"""
        try:
            ext = os.path.splitext(filepath)[1].lower()
            with open(filepath, 'rb') as f:
                header = f.read(4)
                
                if ext == '.zip':
                    # ZIP magic number
                    if header[:2] not in [b'PK', b'PK\x03\x04', b'PK\x05\x06']:
                        return False
                elif ext == '.rar':
                    # RAR magic number
                    if header[:4] != b'Rar!':
                        return False
            
            return True
        except:
            return False
    
    def _check_kontakt_file(self, filepath):
        """Basic Kontakt file validation"""
        try:
            # Check file size is reasonable
            size = os.path.getsize(filepath)
            if size < 100:
                return False
            
            # Kontakt files should be readable
            with open(filepath, 'rb') as f:
                f.read(100)
            
            return True
        except:
            return False
    
    def scan_file(self, filepath, drive_name):
        """Scan a single file"""
        try:
            stat = os.stat(filepath)
            ext = os.path.splitext(filepath)[1].lower()
            
            # Check integrity
            is_broken = False
            if ext in CHECKABLE_EXTENSIONS:
                if not self.check_file_integrity(filepath):
                    is_broken = True
            
            # Calculate hash for duplicate detection
            file_hash = None
            if stat.st_size > 1024 * 100:  # Only hash files > 100KB
                file_hash = self.quick_hash(filepath)
            
            file_info = {
                'path': str(filepath),
                'name': os.path.basename(filepath),
                'size': stat.st_size,
                'ext': ext,
                'drive': drive_name,
                'broken': is_broken,
                'hash': file_hash,
                'modified': stat.st_mtime
            }
            
            return file_info
            
        except Exception as e:
            return {
                'path': str(filepath),
                'error': str(e),
                'drive': drive_name,
                'broken': True
            }
    
    def scan_directory(self, directory, drive_name):
        """Scan a directory"""
        files_found = []
        
        try:
            for root, dirs, files in os.walk(directory):
                # Skip system directories
                dirs[:] = [d for d in dirs if not d.startswith('.') and d not in 
                          ['System', 'Library', 'Applications', '$RECYCLE.BIN', 
                           'System Volume Information', '.Spotlight-V100', '.Trashes']]
                
                for filename in files:
                    if filename.startswith('.'):
                        continue
                    
                    filepath = os.path.join(root, filename)
                    file_info = self.scan_file(filepath, drive_name)
                    
                    if file_info:
                        files_found.append(file_info)
        
        except Exception as e:
            print(f"Error scanning {directory}: {e}")
        
        return files_found

def scan_drive_parallel(drive_path, scanner):
    """Scan entire drive with parallel processing"""
    drive_name = drive_path.name
    
    print(f"\n{'='*70}")
    print(f"🔍 SCANNING: {drive_name}")
    print(f"{'='*70}")
    
    if not drive_path.exists():
        print(f"❌ Drive not found: {drive_path}")
        return []
    
    # Get top-level directories
    top_dirs = []
    try:
        for item in drive_path.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                top_dirs.append(item)
    except Exception as e:
        print(f"Error reading drive: {e}")
        return []
    
    print(f"📂 Found {len(top_dirs)} top-level directories")
    print(f"⚡ Using {scanner.max_workers} parallel workers\n")
    
    all_files = []
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=scanner.max_workers) as executor:
        # Submit all directory scans
        future_to_dir = {
            executor.submit(scanner.scan_directory, directory, drive_name): directory
            for directory in top_dirs
        }
        
        completed = 0
        for future in as_completed(future_to_dir):
            directory = future_to_dir[future]
            completed += 1
            
            try:
                files = future.result()
                all_files.extend(files)
                
                # Show progress
                if files:
                    broken_count = sum(1 for f in files if f.get('broken', False))
                    status = f"✓ [{completed}/{len(top_dirs)}] {directory.name[:40]:40} | {len(files):>6} files"
                    if broken_count > 0:
                        status += f" | ⚠️  {broken_count} BROKEN"
                    print(status)
                    
            except Exception as e:
                print(f"✗ Error: {directory.name}: {e}")
    
    elapsed = time.time() - start_time
    print(f"\n⚡ {drive_name} scanned in {elapsed:.2f} seconds!")
    print(f"📁 Total files: {len(all_files):,}")
    
    broken = sum(1 for f in all_files if f.get('broken', False))
    if broken > 0:
        print(f"⚠️  Broken files: {broken:,}")
    
    return all_files

def analyze_results(all_files):
    """Analyze all scanned files"""
    print("\n" + "="*70)
    print("📊 ANALYZING RESULTS")
    print("="*70)
    
    stats = {
        'total_files': len(all_files),
        'total_size': 0,
        'by_drive': defaultdict(lambda: {'count': 0, 'size': 0, 'broken': 0}),
        'broken_files': [],
        'duplicates': defaultdict(list),
        'cross_drive_dupes': []
    }
    
    # Build hash map
    hash_map = defaultdict(list)
    
    for file_info in all_files:
        if 'error' in file_info:
            stats['broken_files'].append(file_info)
            continue
        
        drive = file_info['drive']
        size = file_info['size']
        
        stats['total_size'] += size
        stats['by_drive'][drive]['count'] += 1
        stats['by_drive'][drive]['size'] += size
        
        if file_info.get('broken', False):
            stats['by_drive'][drive]['broken'] += 1
            stats['broken_files'].append(file_info)
        
        # Track duplicates
        if file_info.get('hash'):
            hash_map[file_info['hash']].append(file_info)
    
    # Find duplicates
    for file_hash, files in hash_map.items():
        if len(files) > 1:
            stats['duplicates'][file_hash] = [f['path'] for f in files]
            
            # Check if duplicates span multiple drives
            drives = set(f['drive'] for f in files)
            if len(drives) > 1:
                stats['cross_drive_dupes'].append({
                    'files': [f['path'] for f in files],
                    'drives': list(drives),
                    'size': files[0]['size'],
                    'count': len(files)
                })
    
    return stats

def format_size(bytes_val):
    """Format bytes to human readable"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_val < 1024.0:
            return f"{bytes_val:.2f} {unit}"
        bytes_val /= 1024.0
    return f"{bytes_val:.2f} PB"

def print_summary(stats):
    """Print analysis summary"""
    print("\n" + "="*70)
    print("📊 MULTI-DRIVE SCAN SUMMARY")
    print("="*70)
    
    print(f"\n📁 Total Files Scanned: {stats['total_files']:,}")
    print(f"💾 Total Size: {format_size(stats['total_size'])}")
    
    print("\n📀 BY DRIVE:")
    print("-" * 70)
    for drive, info in sorted(stats['by_drive'].items()):
        print(f"\n  {drive}")
        print(f"    Files:  {info['count']:>10,}")
        print(f"    Size:   {format_size(info['size']):>10}")
        if info['broken'] > 0:
            print(f"    ⚠️  BROKEN: {info['broken']:>10,} files")
    
    if stats['broken_files']:
        print(f"\n⚠️  BROKEN FILES FOUND:")
        print("-" * 70)
        print(f"  Total broken/corrupted: {len(stats['broken_files']):,} files")
        print(f"  See: {BROKEN_FILES_REPORT}")
    
    if stats['duplicates']:
        print(f"\n🔄 DUPLICATES FOUND:")
        print("-" * 70)
        print(f"  Duplicate groups: {len(stats['duplicates']):,}")
        
        total_dup_files = sum(len(files) - 1 for files in stats['duplicates'].values())
        print(f"  Redundant files: {total_dup_files:,}")
        
        # Calculate wasted space
        wasted = 0
        for files in stats['duplicates'].values():
            try:
                if os.path.exists(files[0]):
                    size = os.path.getsize(files[0])
                    wasted += size * (len(files) - 1)
            except:
                pass
        
        print(f"  💾 Wasted space: {format_size(wasted)}")
    
    if stats['cross_drive_dupes']:
        print(f"\n🌐 CROSS-DRIVE DUPLICATES:")
        print("-" * 70)
        print(f"  Files duplicated across drives: {len(stats['cross_drive_dupes']):,} groups")
        
        cross_waste = sum(d['size'] * (d['count'] - 1) for d in stats['cross_drive_dupes'])
        print(f"  💾 Cross-drive waste: {format_size(cross_waste)}")
        print(f"  See: {CROSS_DRIVE_DUPES}")
    
    print("\n" + "="*70)

def save_reports(stats, all_files):
    """Save detailed reports"""
    print(f"\n💾 Saving detailed reports...")
    
    # Broken files report
    if stats['broken_files']:
        broken_report = {
            'timestamp': datetime.now().isoformat(),
            'total_broken': len(stats['broken_files']),
            'files': stats['broken_files']
        }
        with open(BROKEN_FILES_REPORT, 'w') as f:
            json.dump(broken_report, f, indent=2)
        print(f"  ✓ Broken files: {BROKEN_FILES_REPORT}")
    
    # Cross-drive duplicates
    if stats['cross_drive_dupes']:
        with open(CROSS_DRIVE_DUPES, 'w') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'total_groups': len(stats['cross_drive_dupes']),
                'groups': stats['cross_drive_dupes']
            }, f, indent=2)
        print(f"  ✓ Cross-drive dupes: {CROSS_DRIVE_DUPES}")
    
    # Complete analysis
    report = {
        'timestamp': datetime.now().isoformat(),
        'total_files': stats['total_files'],
        'total_size': stats['total_size'],
        'total_size_human': format_size(stats['total_size']),
        'drives': dict(stats['by_drive']),
        'broken_count': len(stats['broken_files']),
        'duplicate_groups': len(stats['duplicates']),
        'cross_drive_duplicates': len(stats['cross_drive_dupes'])
    }
    
    with open(MULTI_DRIVE_REPORT, 'w') as f:
        json.dump(report, f, indent=2)
    print(f"  ✓ Full analysis: {MULTI_DRIVE_REPORT}")
    
    # Quick summary text file
    with open(QUICK_SUMMARY, 'w') as f:
        f.write("="*70 + "\n")
        f.write("MULTI-DRIVE SCAN SUMMARY\n")
        f.write("="*70 + "\n\n")
        f.write(f"Scan Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Drives Scanned: {', '.join(stats['by_drive'].keys())}\n\n")
        f.write(f"Total Files: {stats['total_files']:,}\n")
        f.write(f"Total Size: {format_size(stats['total_size'])}\n")
        f.write(f"Broken Files: {len(stats['broken_files']):,}\n")
        f.write(f"Duplicate Groups: {len(stats['duplicates']):,}\n")
        f.write(f"Cross-Drive Dupes: {len(stats['cross_drive_dupes']):,}\n")
    
    print(f"  ✓ Quick summary: {QUICK_SUMMARY}")

def main():
    """Main execution"""
    print("\n" + "🚀"*35)
    print("  ULTRA SCANNER X1000 - MULTI-DRIVE EDITION")
    print("🚀"*35 + "\n")
    
    print("Drives to scan:")
    for drive in DRIVES:
        if drive.exists():
            print(f"  ✓ {drive}")
        else:
            print(f"  ✗ {drive} (not found)")
    
    scanner = UltraScanner()
    
    print(f"\n⚡ Maximum parallel mode: {scanner.max_workers} workers")
    print(f"🔍 Scanning for: broken files, duplicates, integrity issues")
    
    input("\nPress Enter to start scanning or Ctrl+C to cancel...")
    
    # Scan all drives in parallel
    print("\n" + "🚀"*35)
    print("STARTING MULTI-DRIVE SCAN")
    print("🚀"*35)
    
    total_start = time.time()
    all_files = []
    
    # Scan drives in parallel
    with ThreadPoolExecutor(max_workers=len(DRIVES)) as executor:
        futures = {
            executor.submit(scan_drive_parallel, drive, scanner): drive
            for drive in DRIVES if drive.exists()
        }
        
        for future in as_completed(futures):
            drive = futures[future]
            try:
                files = future.result()
                all_files.extend(files)
            except Exception as e:
                print(f"❌ Error scanning {drive}: {e}")
    
    total_elapsed = time.time() - total_start
    
    # Analyze results
    stats = analyze_results(all_files)
    
    # Print summary
    print_summary(stats)
    
    # Save reports
    save_reports(stats, all_files)
    
    print(f"\n⚡ TOTAL SCAN TIME: {total_elapsed:.2f} seconds")
    print(f"📊 Files per second: {len(all_files) / total_elapsed:.1f}")
    
    print("\n✅ SCAN COMPLETE!")
    print(f"\n📁 All reports saved to: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()

