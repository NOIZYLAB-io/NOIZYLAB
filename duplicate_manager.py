#!/usr/bin/env python3
"""
INTELLIGENT DUPLICATE MANAGER
Safely remove duplicates while preserving the best versions
"""

import os
import json
import shutil
from pathlib import Path
from datetime import datetime

WORKSPACE = Path("/Volumes/4TBSG/KTK 2026 TO SORT")
DUPLICATES_FILE = WORKSPACE / "duplicates_report.txt"
REPORT_FILE = WORKSPACE / "organization_report.json"
DUPLICATES_DIR = WORKSPACE / "_DUPLICATES_BACKUP"
REMOVED_LOG = WORKSPACE / "duplicates_removed.log"

def load_duplicates_from_report():
    """Load duplicate information from JSON report"""
    print("📂 Loading scan report...")
    
    # For now, we'll scan again with full hashing
    # In production, you'd parse the duplicates_report.txt
    from collections import defaultdict
    import hashlib
    
    print("🔍 Scanning for duplicates with full file hashing...")
    
    duplicates = defaultdict(list)
    file_count = 0
    
    for root, dirs, files in os.walk(WORKSPACE):
        # Skip certain directories
        if any(skip in root for skip in ['_DUPLICATES_', 'ORGANIZED_2026', '.git']):
            continue
            
        for filename in files:
            if filename.startswith('.') or filename.endswith('.py'):
                continue
                
            filepath = os.path.join(root, filename)
            
            try:
                file_size = os.path.getsize(filepath)
                
                # Only check files > 100KB
                if file_size < 100 * 1024:
                    continue
                
                # Calculate full hash for files > 1MB
                if file_size > 1024 * 1024:
                    hasher = hashlib.md5()
                    with open(filepath, 'rb') as f:
                        # Read in chunks
                        while chunk := f.read(8192):
                            hasher.update(chunk)
                    file_hash = hasher.hexdigest()
                    
                    duplicates[file_hash].append(filepath)
                    file_count += 1
                    
                    if file_count % 100 == 0:
                        print(f"  Processed {file_count} files...", end='\r')
                        
            except Exception as e:
                continue
    
    print(f"\n✓ Scanned {file_count} files")
    
    # Filter to only actual duplicates
    real_duplicates = {h: paths for h, paths in duplicates.items() if len(paths) > 1}
    
    return real_duplicates

def score_file_path(filepath):
    """Score a file path to determine which duplicate to keep
    Higher score = better file to keep
    """
    score = 0
    path_lower = filepath.lower()
    
    # Prefer files in organized directories
    if 'organized' in path_lower:
        score += 100
    
    # Avoid backup/duplicate directories
    if any(bad in path_lower for bad in ['duplicate', 'backup', 'copy', 'old', 'temp', 'trash']):
        score -= 50
    
    # Prefer shorter paths (usually more organized)
    score -= len(filepath.split(os.sep))
    
    # Prefer files not in numbered directories (like "Copy 2")
    if any(marker in filepath for marker in [' (1)', ' (2)', ' copy', 'Copy of']):
        score -= 30
    
    # Bonus for being in main library folders
    if any(lib in path_lower for lib in ['kontakt', 'library', 'libraries', 'instruments']):
        score += 20
    
    return score

def choose_best_duplicate(file_paths):
    """Choose which duplicate file to keep"""
    scored = [(path, score_file_path(path)) for path in file_paths]
    scored.sort(key=lambda x: x[1], reverse=True)
    
    best = scored[0][0]
    to_remove = [path for path, _ in scored[1:]]
    
    return best, to_remove

def format_size(bytes):
    """Format bytes to human readable"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            return f"{bytes:.2f} {unit}"
        bytes /= 1024.0
    return f"{bytes:.2f} PB"

def remove_duplicates(duplicates, dry_run=True, backup=True):
    """Remove duplicate files"""
    
    print("\n" + "="*70)
    print("🗑️  DUPLICATE REMOVAL")
    print("="*70)
    
    if dry_run:
        print("\n⚠️  DRY RUN MODE - No files will be deleted")
        print("Set dry_run=False to actually remove files\n")
    else:
        print("\n🔴 LIVE MODE - Files will be deleted!")
        if backup:
            print(f"📦 Backups will be saved to: {DUPLICATES_DIR}\n")
            DUPLICATES_DIR.mkdir(exist_ok=True)
    
    total_removed = 0
    total_saved_space = 0
    removal_log = []
    
    for i, (file_hash, paths) in enumerate(duplicates.items(), 1):
        if len(paths) < 2:
            continue
        
        # Choose best file to keep
        keep, remove = choose_best_duplicate(paths)
        
        print(f"\n[{i}/{len(duplicates)}] Processing duplicate group...")
        print(f"  ✓ KEEPING: {keep}")
        
        for filepath in remove:
            try:
                file_size = os.path.getsize(filepath)
                
                print(f"  ✗ REMOVE:  {filepath} ({format_size(file_size)})")
                
                if not dry_run:
                    if backup:
                        # Backup to duplicates folder
                        rel_path = os.path.relpath(filepath, WORKSPACE)
                        backup_path = DUPLICATES_DIR / rel_path
                        backup_path.parent.mkdir(parents=True, exist_ok=True)
                        shutil.move(filepath, backup_path)
                    else:
                        os.remove(filepath)
                    
                    removal_log.append({
                        'removed': filepath,
                        'kept': keep,
                        'size': file_size,
                        'timestamp': datetime.now().isoformat()
                    })
                
                total_removed += 1
                total_saved_space += file_size
                
            except Exception as e:
                print(f"  ⚠️  Error removing {filepath}: {e}")
    
    print("\n" + "="*70)
    print("📊 SUMMARY")
    print("="*70)
    print(f"Files that would be removed: {total_removed}")
    print(f"Space that would be saved: {format_size(total_saved_space)}")
    
    if not dry_run and removal_log:
        # Save removal log
        with open(REMOVED_LOG, 'w') as f:
            json.dump(removal_log, f, indent=2)
        print(f"\n✓ Removal log saved to: {REMOVED_LOG}")
    
    return total_removed, total_saved_space

def interactive_mode(duplicates):
    """Interactive mode to review duplicates"""
    print("\n" + "="*70)
    print("🎯 INTERACTIVE DUPLICATE REVIEW")
    print("="*70)
    
    for i, (file_hash, paths) in enumerate(duplicates.items(), 1):
        if len(paths) < 2:
            continue
        
        keep, remove = choose_best_duplicate(paths)
        
        print(f"\n[{i}/{len(duplicates)}] Duplicate Group:")
        print(f"  Files: {len(paths)}")
        
        try:
            file_size = os.path.getsize(paths[0])
            print(f"  Size: {format_size(file_size)} each")
            print(f"  Waste: {format_size(file_size * (len(paths) - 1))}")
        except:
            pass
        
        print(f"\n  SUGGESTED TO KEEP:")
        print(f"    {keep}")
        print(f"\n  SUGGESTED TO REMOVE:")
        for path in remove[:5]:  # Show max 5
            print(f"    {path}")
        if len(remove) > 5:
            print(f"    ... and {len(remove) - 5} more")
        
        # Show only first 10 groups in interactive mode
        if i >= 10:
            print(f"\n... and {len(duplicates) - 10} more duplicate groups")
            break
        
        print("-" * 70)

def main():
    print("\n" + "🗑️ "*35)
    print("  INTELLIGENT DUPLICATE MANAGER")
    print("🗑️ "*35 + "\n")
    
    # Load duplicates
    duplicates = load_duplicates_from_report()
    
    print(f"\n📊 Found {len(duplicates)} duplicate groups")
    
    if not duplicates:
        print("✓ No duplicates found!")
        return
    
    # Calculate potential savings
    total_files = sum(len(paths) for paths in duplicates.values())
    print(f"📁 Total duplicate files: {total_files}")
    
    # Interactive preview
    print("\n" + "="*70)
    print("Choose an option:")
    print("="*70)
    print("1. Preview duplicates (dry run)")
    print("2. Interactive review (first 10 groups)")
    print("3. Remove duplicates with backup")
    print("4. Remove duplicates permanently (no backup)")
    print("\nFor now, running preview mode...")
    print("="*70)
    
    # Run in dry run mode by default
    remove_duplicates(duplicates, dry_run=True, backup=True)
    
    print("\n💡 To actually remove duplicates:")
    print("   Edit this script and set dry_run=False in the remove_duplicates call")
    print("\n⚠️  ALWAYS backup your files before removing duplicates!")

if __name__ == "__main__":
    main()

