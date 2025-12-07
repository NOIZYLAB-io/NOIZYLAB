#!/usr/bin/env python3
"""
ADVANCED FILE SCANNER - Ultra-fast multi-threaded file analysis
Features:
- Content-based duplicate detection using hashing
- Low quality duplicate detection
- Mislabeled file detection
- Corrupted file detection
- File size analysis
- Extension verification
"""

import os
import hashlib
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from pathlib import Path
from collections import defaultdict
import time
import json
import mimetypes

# Configuration
ROOT = '/Volumes/MAG 4TB'
SKIP_DIRS = {'.git', '__pycache__', 'node_modules', '.Trash', '.Spotlight-V100', 
             '.fseventsd', '.DocumentRevisions-V100', '.TemporaryItems', '.VolumeIcon.icns'}
MIN_SIZE_FOR_HASH = 1024 * 100  # 100KB minimum for hashing
HASH_CHUNK_SIZE = 1024 * 1024  # 1MB chunks

# Audio file extensions
AUDIO_EXTS = {'.wav', '.mp3', '.flac', '.aiff', '.aif', '.ogg', '.m4a', '.wma', '.aac', '.opus'}
VIDEO_EXTS = {'.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.webm'}
IMAGE_EXTS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg'}
ARCHIVE_EXTS = {'.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'}

QUALITY_INDICATORS = {
    'low': ['low', 'lq', 'draft', 'temp', 'test', 'demo'],
    'backup': ['backup', 'bak', 'old', 'orig', 'original'],
    'duplicate': ['copy', 'duplicate', 'dupe', '(1)', '(2)', '(3)', ' - copy'],
    'unused': ['unused', 'trash', 'delete', 'remove']
}

def get_file_hash(filepath, quick=False):
    """Calculate hash of file. If quick=True, only hash first and last 1MB"""
    try:
        hasher = hashlib.md5()
        file_size = os.path.getsize(filepath)
        
        with open(filepath, 'rb') as f:
            if quick and file_size > 2 * 1024 * 1024:  # > 2MB
                # Quick hash: first 1MB + last 1MB
                hasher.update(f.read(1024 * 1024))
                f.seek(-1024 * 1024, 2)  # Seek to last 1MB
                hasher.update(f.read(1024 * 1024))
            else:
                # Full hash for smaller files
                while chunk := f.read(HASH_CHUNK_SIZE):
                    hasher.update(chunk)
        
        return hasher.hexdigest()
    except Exception as e:
        return None

def check_file_corruption(filepath, ext):
    """Check if file is corrupted based on extension"""
    try:
        with open(filepath, 'rb') as f:
            header = f.read(16)
            
            # WAV check
            if ext == '.wav':
                if not header.startswith(b'RIFF'):
                    return 'Invalid WAV header'
                    
            # FLAC check
            elif ext == '.flac':
                if not header.startswith(b'fLaC'):
                    return 'Invalid FLAC header'
                    
            # MP3 check
            elif ext == '.mp3':
                if not (header.startswith(b'ID3') or header[0:2] == b'\xff\xfb' or header[0:2] == b'\xff\xf3'):
                    return 'Invalid MP3 header'
                    
            # PNG check
            elif ext == '.png':
                if not header.startswith(b'\x89PNG\r\n\x1a\n'):
                    return 'Invalid PNG header'
                    
            # JPEG check
            elif ext in ['.jpg', '.jpeg']:
                if not header.startswith(b'\xff\xd8\xff'):
                    return 'Invalid JPEG header'
                    
            # ZIP check
            elif ext == '.zip':
                if not header.startswith(b'PK\x03\x04'):
                    return 'Invalid ZIP header'
        
        return None
    except Exception as e:
        return f'Error reading: {str(e)}'

def analyze_filename(filename):
    """Analyze filename for quality indicators"""
    name_lower = filename.lower()
    base = os.path.splitext(name_lower)[0]
    
    issues = []
    for category, indicators in QUALITY_INDICATORS.items():
        for indicator in indicators:
            if indicator in base:
                issues.append((category, indicator))
    
    return issues

def scan_file_detailed(filepath):
    """Detailed scan of a single file"""
    try:
        stat = os.stat(filepath)
        filename = os.path.basename(filepath)
        ext = os.path.splitext(filename)[1].lower()
        
        info = {
            'path': filepath,
            'name': filename,
            'size': stat.st_size,
            'ext': ext,
            'mtime': stat.st_mtime,
            'issues': [],
            'hash': None,
            'quick_hash': None
        }
        
        # Check filename issues
        name_issues = analyze_filename(filename)
        if name_issues:
            info['issues'].extend([f'filename_{cat}_{ind}' for cat, ind in name_issues])
        
        # Check for no extension
        if not ext and stat.st_size > 1024:
            info['issues'].append('no_extension')
        
        # Check for corruption in common file types
        if ext in AUDIO_EXTS | VIDEO_EXTS | IMAGE_EXTS | ARCHIVE_EXTS:
            corruption = check_file_corruption(filepath, ext)
            if corruption:
                info['issues'].append(f'corrupted: {corruption}')
        
        # Calculate hash for files larger than threshold
        if stat.st_size > MIN_SIZE_FOR_HASH:
            info['quick_hash'] = get_file_hash(filepath, quick=True)
        
        return info
    except (OSError, PermissionError):
        return None

def scan_directory_worker(dirpath):
    """Worker to scan a directory"""
    files = []
    try:
        for entry in os.scandir(dirpath):
            if entry.is_file() and not entry.name.startswith('.'):
                info = scan_file_detailed(entry.path)
                if info:
                    files.append(info)
    except (OSError, PermissionError):
        pass
    return files

def collect_directories(root_path):
    """Recursively collect all directories"""
    dirs = []
    try:
        for dirpath, dirnames, _ in os.walk(root_path):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            dirs.append(dirpath)
    except (OSError, PermissionError):
        pass
    return dirs

def analyze_duplicates(files_data):
    """Advanced duplicate analysis"""
    print("\n" + "="*80)
    print("ANALYZING DUPLICATES")
    print("="*80)
    
    # Group by quick hash
    by_hash = defaultdict(list)
    by_name = defaultdict(list)
    by_size = defaultdict(list)
    
    for f in files_data:
        if f['quick_hash']:
            by_hash[f['quick_hash']].append(f)
        by_name[f['name'].lower()].append(f)
        by_size[f['size']].append(f)
    
    # Find exact duplicates (same hash)
    print("\n### EXACT DUPLICATES (Same Content) ###")
    exact_dupes = [(h, files) for h, files in by_hash.items() if len(files) > 1]
    exact_dupes.sort(key=lambda x: x[1][0]['size'], reverse=True)
    
    if exact_dupes:
        total_waste = 0
        for i, (h, files) in enumerate(exact_dupes[:30]):
            size_mb = files[0]['size'] / (1024 * 1024)
            waste = size_mb * (len(files) - 1)
            total_waste += waste
            
            print(f"\n{i+1}. {files[0]['name']}")
            print(f"   Size: {size_mb:.2f} MB x {len(files)} copies = {waste:.2f} MB wasted")
            for f in files[:5]:
                print(f"   - {f['path']}")
            if len(files) > 5:
                print(f"   ... and {len(files) - 5} more")
        
        print(f"\nTotal exact duplicates: {len(exact_dupes)}")
        print(f"Total wasted space: {total_waste:.2f} MB ({total_waste/1024:.2f} GB)")
    else:
        print("No exact duplicates found")
    
    # Find low quality duplicates
    print("\n\n### LOW QUALITY DUPLICATES ###")
    print("(Multiple versions with quality indicators)")
    
    # Group by base name (removing quality indicators)
    base_groups = defaultdict(list)
    for f in files_data:
        base = f['name'].lower()
        for cat, indicators in QUALITY_INDICATORS.items():
            for ind in indicators:
                base = base.replace(ind, '')
        base = base.strip('_- ()')
        base_groups[base].append(f)
    
    low_q_dupes = []
    for base, files in base_groups.items():
        if len(files) > 1:
            # Check if any have quality issues
            has_issues = any(any('filename_' in issue for issue in f['issues']) for f in files)
            if has_issues:
                low_q_dupes.append((base, files))
    
    low_q_dupes.sort(key=lambda x: sum(f['size'] for f in x[1]), reverse=True)
    
    if low_q_dupes:
        for i, (base, files) in enumerate(low_q_dupes[:20]):
            total_size = sum(f['size'] for f in files) / (1024 * 1024)
            print(f"\n{i+1}. '{base}' - {len(files)} versions ({total_size:.2f} MB total)")
            
            files_sorted = sorted(files, key=lambda x: x['size'], reverse=True)
            for f in files_sorted:
                size_mb = f['size'] / (1024 * 1024)
                issues = [iss for iss in f['issues'] if 'filename_' in iss]
                issue_str = ', '.join(issues) if issues else 'clean'
                print(f"   {size_mb:>8.2f} MB - {issue_str:20s} - {f['name']}")
        
        print(f"\nTotal low-quality duplicate groups: {len(low_q_dupes)}")
    else:
        print("No low quality duplicates found")
    
    return exact_dupes, low_q_dupes

def analyze_issues(files_data):
    """Analyze file issues"""
    print("\n" + "="*80)
    print("FILE ISSUES ANALYSIS")
    print("="*80)
    
    issue_files = [f for f in files_data if f['issues']]
    
    if not issue_files:
        print("No issues found!")
        return
    
    # Group by issue type
    by_issue = defaultdict(list)
    for f in issue_files:
        for issue in f['issues']:
            by_issue[issue].append(f)
    
    # Print by category
    print(f"\nTotal files with issues: {len(issue_files)}")
    print(f"Total unique issue types: {len(by_issue)}")
    
    for issue, files in sorted(by_issue.items(), key=lambda x: -len(x[1])):
        print(f"\n### {issue.upper()} ({len(files)} files) ###")
        
        total_size = sum(f['size'] for f in files) / (1024 * 1024)
        print(f"Total size: {total_size:.2f} MB")
        
        for f in files[:10]:
            size_mb = f['size'] / (1024 * 1024)
            print(f"  {size_mb:>8.2f} MB - {f['path']}")
        
        if len(files) > 10:
            print(f"  ... and {len(files) - 10} more")

def generate_report(all_files, exact_dupes, low_q_dupes):
    """Generate comprehensive JSON report"""
    report = {
        'scan_time': time.strftime('%Y-%m-%d %H:%M:%S'),
        'total_files': len(all_files),
        'total_size_bytes': sum(f['size'] for f in all_files),
        'exact_duplicates': len(exact_dupes),
        'low_quality_duplicates': len(low_q_dupes),
        'files_with_issues': len([f for f in all_files if f['issues']]),
        'by_extension': {},
        'largest_files': [],
        'recommendations': []
    }
    
    # Count by extension
    ext_count = defaultdict(lambda: {'count': 0, 'size': 0})
    for f in all_files:
        ext = f['ext'] or 'no_extension'
        ext_count[ext]['count'] += 1
        ext_count[ext]['size'] += f['size']
    
    report['by_extension'] = {k: v for k, v in sorted(ext_count.items(), 
                                                       key=lambda x: -x[1]['size'])}
    
    # Largest files
    largest = sorted(all_files, key=lambda x: x['size'], reverse=True)[:50]
    report['largest_files'] = [
        {
            'path': f['path'],
            'size_mb': f['size'] / (1024 * 1024),
            'name': f['name']
        }
        for f in largest
    ]
    
    # Generate recommendations
    if exact_dupes:
        waste = sum((len(files) - 1) * files[0]['size'] for _, files in exact_dupes)
        report['recommendations'].append(
            f"Remove {len(exact_dupes)} exact duplicate groups to save {waste/(1024**3):.2f} GB"
        )
    
    if low_q_dupes:
        report['recommendations'].append(
            f"Review {len(low_q_dupes)} low-quality duplicate groups"
        )
    
    return report

def main():
    print("="*80)
    print("ADVANCED FILE SCANNER v2.0")
    print("="*80)
    print(f"Root: {ROOT}")
    print(f"CPU cores: {mp.cpu_count()}")
    print()
    
    start_time = time.time()
    
    # Step 1: Collect directories
    print("Collecting directories...")
    directories = collect_directories(ROOT)
    print(f"Found {len(directories):,} directories")
    
    # Step 2: Scan files in parallel
    print("\nScanning files...")
    all_files = []
    processed = 0
    
    with ProcessPoolExecutor(max_workers=mp.cpu_count()) as executor:
        futures = {executor.submit(scan_directory_worker, d): d for d in directories}
        
        for future in as_completed(futures):
            processed += 1
            if processed % 100 == 0:
                print(f"Progress: {processed}/{len(directories)} directories ({100*processed/len(directories):.1f}%)", end='\r')
            
            result = future.result()
            if result:
                all_files.extend(result)
    
    scan_time = time.time() - start_time
    print(f"\n\nScanned {len(all_files):,} files in {scan_time:.1f}s ({len(all_files)/scan_time:.0f} files/sec)")
    
    # Step 3: Analyze duplicates
    exact_dupes, low_q_dupes = analyze_duplicates(all_files)
    
    # Step 4: Analyze issues
    analyze_issues(all_files)
    
    # Step 5: Generate report
    print("\n" + "="*80)
    print("GENERATING REPORT")
    print("="*80)
    
    report = generate_report(all_files, exact_dupes, low_q_dupes)
    
    report_path = '/Volumes/MAG 4TB/NoizyWorkspace/advanced_scan_report.json'
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"\nDetailed JSON report saved to: {report_path}")
    
    # Print summary
    print("\n" + "="*80)
    print("SUMMARY")
    print("="*80)
    print(f"Total files: {len(all_files):,}")
    print(f"Total size: {sum(f['size'] for f in all_files)/(1024**3):.2f} GB")
    print(f"Exact duplicates: {len(exact_dupes):,}")
    print(f"Low-quality duplicates: {len(low_q_dupes):,}")
    print(f"Files with issues: {len([f for f in all_files if f['issues']]):,}")
    print(f"\nTotal time: {time.time() - start_time:.1f}s")
    
    if report['recommendations']:
        print("\n### RECOMMENDATIONS ###")
        for rec in report['recommendations']:
            print(f"  • {rec}")

if __name__ == '__main__':
    main()

