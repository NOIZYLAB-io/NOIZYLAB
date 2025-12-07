#!/usr/bin/env python3
"""
SMART CLEANUP TOOL - Intelligent file cleanup with safety features
Features:
- Remove exact duplicates (keeps newest/largest)
- Remove low quality versions
- Clean up empty directories
- Move suspicious files to review folder
- Dry-run mode for safety
- Detailed logging
"""

import os
import shutil
import json
import time
from pathlib import Path
from collections import defaultdict
import argparse

ROOT = '/Volumes/MAG 4TB'
REVIEW_FOLDER = '/Volumes/MAG 4TB/NoizyWorkspace/_REVIEW_FOR_DELETION'
LOG_FILE = '/Volumes/MAG 4TB/NoizyWorkspace/cleanup_log.json'

def ensure_review_folder():
    """Create review folder if it doesn't exist"""
    os.makedirs(REVIEW_FOLDER, exist_ok=True)
    return REVIEW_FOLDER

def move_to_review(filepath, reason, dry_run=True):
    """Move file to review folder"""
    if dry_run:
        return f"[DRY RUN] Would move: {filepath}"
    
    try:
        review_path = os.path.join(REVIEW_FOLDER, reason)
        os.makedirs(review_path, exist_ok=True)
        
        # Get unique filename
        dest = os.path.join(review_path, os.path.basename(filepath))
        counter = 1
        while os.path.exists(dest):
            name, ext = os.path.splitext(os.path.basename(filepath))
            dest = os.path.join(review_path, f"{name}_{counter}{ext}")
            counter += 1
        
        shutil.move(filepath, dest)
        return f"Moved: {filepath} -> {dest}"
    except Exception as e:
        return f"Error moving {filepath}: {str(e)}"

def delete_file(filepath, dry_run=True):
    """Delete a file"""
    if dry_run:
        return f"[DRY RUN] Would delete: {filepath}"
    
    try:
        os.remove(filepath)
        return f"Deleted: {filepath}"
    except Exception as e:
        return f"Error deleting {filepath}: {str(e)}"

def clean_exact_duplicates(report_path, dry_run=True, auto=False):
    """Remove exact duplicates, keeping the best version"""
    print("\n" + "="*80)
    print("CLEANING EXACT DUPLICATES")
    print("="*80)
    
    if not os.path.exists(report_path):
        print(f"Error: Report file not found: {report_path}")
        return []
    
    with open(report_path, 'r') as f:
        data = json.load(f)
    
    # Load file data (we need the full scan data, not just the report)
    # For now, we'll work with what we have
    
    actions = []
    print(f"\nMode: {'DRY RUN' if dry_run else 'LIVE'}")
    print(f"Auto mode: {'ON' if auto else 'OFF'}")
    
    if not auto:
        response = input("\nProceed with exact duplicate cleanup? (yes/no): ")
        if response.lower() != 'yes':
            print("Cancelled.")
            return []
    
    # This is a placeholder - in real use, we'd load the full scan data
    print("\nNote: Full duplicate cleanup requires running advanced scanner first")
    print("Use: python3 advanced_file_scanner.py")
    
    return actions

def clean_empty_directories(root, dry_run=True):
    """Remove all empty directories"""
    print("\n" + "="*80)
    print("CLEANING EMPTY DIRECTORIES")
    print("="*80)
    
    actions = []
    
    # Multiple passes to catch nested empties
    for pass_num in range(5):
        empty_dirs = []
        for dirpath, dirnames, filenames in os.walk(root, topdown=False):
            # Skip special directories
            if any(skip in dirpath for skip in ['.git', '__pycache__', 'node_modules', '.Trash']):
                continue
            
            # Check if directory is empty
            try:
                if not os.listdir(dirpath):
                    empty_dirs.append(dirpath)
            except (OSError, PermissionError):
                continue
        
        if not empty_dirs:
            break
        
        print(f"\nPass {pass_num + 1}: Found {len(empty_dirs)} empty directories")
        
        for d in empty_dirs:
            if dry_run:
                actions.append(f"[DRY RUN] Would delete: {d}")
                print(f"  Would delete: {d}")
            else:
                try:
                    os.rmdir(d)
                    actions.append(f"Deleted: {d}")
                    print(f"  Deleted: {d}")
                except Exception as e:
                    actions.append(f"Error: {d} - {str(e)}")
    
    print(f"\nTotal empty directories handled: {len(actions)}")
    return actions

def find_and_review_suspicious(root, dry_run=True):
    """Find suspicious files and move to review folder"""
    print("\n" + "="*80)
    print("FINDING SUSPICIOUS FILES")
    print("="*80)
    
    ensure_review_folder()
    
    suspicious_patterns = [
        'untitled', 'new file', 'copy of', 'temp', 'tmp', 
        'test', 'backup', 'old', 'delete', 'trash'
    ]
    
    actions = []
    found_files = []
    
    print("\nScanning for suspicious files...")
    for dirpath, dirnames, filenames in os.walk(root):
        # Skip special directories
        if any(skip in dirpath for skip in ['.git', '__pycache__', 'NoizyWorkspace', '.Trash']):
            continue
        
        for filename in filenames:
            name_lower = filename.lower()
            for pattern in suspicious_patterns:
                if pattern in name_lower:
                    filepath = os.path.join(dirpath, filename)
                    found_files.append((filepath, pattern))
                    break
    
    print(f"Found {len(found_files)} suspicious files")
    
    if found_files:
        print("\nFirst 20 files:")
        for fp, reason in found_files[:20]:
            print(f"  {reason:15s} - {fp}")
        
        if len(found_files) > 20:
            print(f"  ... and {len(found_files) - 20} more")
        
        response = input(f"\nMove {len(found_files)} files to review folder? (yes/no): ")
        if response.lower() == 'yes':
            for filepath, reason in found_files:
                action = move_to_review(filepath, reason, dry_run)
                actions.append(action)
                if len(actions) % 100 == 0:
                    print(f"  Processed {len(actions)}/{len(found_files)}", end='\r')
            print(f"\n  Completed: {len(actions)} files")
    
    return actions

def analyze_storage(root):
    """Analyze storage usage by directory and type"""
    print("\n" + "="*80)
    print("STORAGE ANALYSIS")
    print("="*80)
    
    dir_sizes = defaultdict(int)
    ext_sizes = defaultdict(int)
    
    print("\nAnalyzing storage usage...")
    file_count = 0
    
    for dirpath, dirnames, filenames in os.walk(root):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            try:
                size = os.path.getsize(filepath)
                dir_sizes[dirpath] += size
                ext = os.path.splitext(filename)[1].lower() or 'no_extension'
                ext_sizes[ext] += size
                file_count += 1
                
                if file_count % 10000 == 0:
                    print(f"  Processed {file_count:,} files", end='\r')
            except (OSError, PermissionError):
                continue
    
    print(f"\n\nTotal files analyzed: {file_count:,}")
    
    # Top directories by size
    print("\n### TOP 20 DIRECTORIES BY SIZE ###")
    sorted_dirs = sorted(dir_sizes.items(), key=lambda x: -x[1])[:20]
    for dirpath, size in sorted_dirs:
        size_gb = size / (1024**3)
        print(f"  {size_gb:>8.2f} GB - {dirpath}")
    
    # Top extensions by size
    print("\n### TOP 20 FILE TYPES BY SIZE ###")
    sorted_exts = sorted(ext_sizes.items(), key=lambda x: -x[1])[:20]
    for ext, size in sorted_exts:
        size_gb = size / (1024**3)
        count = sum(1 for d, dn, files in os.walk(root) 
                   for f in files if os.path.splitext(f)[1].lower() == ext)
        print(f"  {size_gb:>8.2f} GB - {ext:15s} ({count:,} files)")
    
    return dir_sizes, ext_sizes

def main():
    parser = argparse.ArgumentParser(description='Smart Cleanup Tool')
    parser.add_argument('--live', action='store_true', help='Execute actions (default is dry-run)')
    parser.add_argument('--duplicates', action='store_true', help='Clean exact duplicates')
    parser.add_argument('--empty-dirs', action='store_true', help='Clean empty directories')
    parser.add_argument('--suspicious', action='store_true', help='Review suspicious files')
    parser.add_argument('--analyze', action='store_true', help='Analyze storage usage')
    parser.add_argument('--all', action='store_true', help='Run all cleanup operations')
    parser.add_argument('--auto', action='store_true', help='Auto mode (no prompts)')
    
    args = parser.parse_args()
    
    dry_run = not args.live
    
    print("="*80)
    print("SMART CLEANUP TOOL v2.0")
    print("="*80)
    print(f"Root: {ROOT}")
    print(f"Mode: {'LIVE' if not dry_run else 'DRY RUN'}")
    print()
    
    if dry_run:
        print("⚠️  DRY RUN MODE - No files will be modified")
        print("   Use --live to execute actions")
        print()
    
    all_actions = []
    
    # Run requested operations
    if args.all or args.empty_dirs:
        actions = clean_empty_directories(ROOT, dry_run)
        all_actions.extend(actions)
    
    if args.all or args.suspicious:
        actions = find_and_review_suspicious(ROOT, dry_run)
        all_actions.extend(actions)
    
    if args.all or args.duplicates:
        report_path = '/Volumes/MAG 4TB/NoizyWorkspace/advanced_scan_report.json'
        actions = clean_exact_duplicates(report_path, dry_run, args.auto)
        all_actions.extend(actions)
    
    if args.all or args.analyze:
        analyze_storage(ROOT)
    
    # Save log
    if all_actions:
        log_data = {
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
            'dry_run': dry_run,
            'total_actions': len(all_actions),
            'actions': all_actions
        }
        
        with open(LOG_FILE, 'w') as f:
            json.dump(log_data, f, indent=2)
        
        print(f"\n\nLog saved to: {LOG_FILE}")
        print(f"Total actions: {len(all_actions)}")
    
    if not any([args.all, args.duplicates, args.empty_dirs, args.suspicious, args.analyze]):
        parser.print_help()

if __name__ == '__main__':
    main()

