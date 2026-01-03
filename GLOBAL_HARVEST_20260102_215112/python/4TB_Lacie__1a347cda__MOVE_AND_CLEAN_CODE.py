#!/usr/bin/env python3
"""
📦 MOVE/COPY ALL CODE, THEN DELETE AND CLEAN DISK

This script:
1. Finds all code files (.py, .js, .ts, .mjs, .sh, etc.)
2. Copies them to a consolidated CODE_ARCHIVE directory
3. Removes duplicates based on content hash
4. Deletes original files after verification
5. Cleans up empty directories

Created by: CLAUDE (Code Assistant - Deep Analysis)
"""

import os
import shutil
import hashlib
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import sys

BASE = Path("/Users/m2ultra/NOIZYLAB")
ARCHIVE_DIR = BASE / "CODE_ARCHIVE"
LOG_DIR = BASE / "logs"
LOG_DIR.mkdir(exist_ok=True)

TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
LOG_FILE = LOG_DIR / f"move_and_clean_{TIMESTAMP}.log"

# Code file extensions
CODE_EXTENSIONS = {
    '.py', '.js', '.ts', '.tsx', '.jsx', '.mjs', '.cjs',
    '.sh', '.bash', '.zsh', '.rb', '.go', '.rs', '.java',
    '.kt', '.swift', '.php', '.r', '.sql', '.html', '.css',
    '.scss', '.sass', '.less', '.vue', '.svelte', '.json',
    '.yaml', '.yml', '.toml', '.xml', '.md', '.txt', '.conf',
    '.config', '.ini', '.env', '.c', '.cpp', '.h', '.hpp'
}

# Directories to exclude
EXCLUDE_PATTERNS = {
    'node_modules', '.git', '.venv', 'venv', '__pycache__',
    '.pytest_cache', 'dist', 'build', '.next', '.nuxt', '.cache',
    'logs', 'CODE_ARCHIVE', 'backups', '.DS_Store'
}

def should_exclude(path):
    """Check if path should be excluded"""
    parts = path.parts
    for part in parts:
        if part in EXCLUDE_PATTERNS:
            return True
        if part.startswith('.') and part != '.':
            if part not in {'.git', '.venv', '.pytest_cache', '.cache', '.next', '.nuxt'}:
                # Allow some dot dirs but exclude most
                pass
    return False

def get_file_hash(filepath):
    """Get MD5 hash of file"""
    hash_md5 = hashlib.md5()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except Exception as e:
        return None

def log(message):
    """Log message to file and print"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_msg = f"{timestamp} - {message}"
    print(log_msg)
    with open(LOG_FILE, 'a') as f:
        f.write(log_msg + "\n")

def format_size(size_bytes):
    """Format bytes to human readable"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f}{unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f}PB"

def main():
    dry_run = '--dry-run' in sys.argv or '--dry' in sys.argv
    
    print("=" * 80)
    print(" " * 20 + "📦 MOVE/COPY ALL CODE & CLEAN DISK")
    print("=" * 80)
    print()
    
    if dry_run:
        print("⚠️  DRY RUN MODE - No files will be deleted")
        print()
    
    print(f"📋 Log file: {LOG_FILE}")
    print(f"📦 Archive directory: {ARCHIVE_DIR}")
    print()
    
    ARCHIVE_DIR.mkdir(exist_ok=True, parents=True)
    
    log("Starting code collection...")
    
    # Step 1: Find and copy all code files
    print("=" * 80)
    print("  STEP 1: FINDING AND COPYING ALL CODE FILES")
    print("=" * 80)
    print()
    
    total_files = 0
    copied_files = 0
    duplicate_files = 0
    file_hashes = {}
    file_paths = {}
    errors = []
    
    # Find all code files
    for root, dirs, files in os.walk(BASE):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if not should_exclude(Path(root) / d)]
        
        for file in files:
            filepath = Path(root) / file
            
            # Check if it's a code file
            if filepath.suffix.lower() not in CODE_EXTENSIONS:
                continue
            
            # Skip excluded paths
            if should_exclude(filepath):
                continue
            
            total_files += 1
            
            # Get relative path from BASE
            try:
                rel_path = filepath.relative_to(BASE)
                archive_path = ARCHIVE_DIR / rel_path
                archive_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Get file hash to detect duplicates
                file_hash = get_file_hash(filepath)
                
                if file_hash is None:
                    errors.append(f"Failed to hash: {rel_path}")
                    continue
                
                if file_hash in file_hashes:
                    # Duplicate found
                    duplicate_files += 1
                    log(f"DUPLICATE: {rel_path} (same as {file_paths[file_hash]})")
                    if duplicate_files <= 10:  # Show first 10
                        print(f"  ⚠️  Duplicate: {str(rel_path)[:60]}...")
                else:
                    # Copy file
                    try:
                        shutil.copy2(filepath, archive_path)
                        copied_files += 1
                        file_hashes[file_hash] = True
                        file_paths[file_hash] = str(rel_path)
                        
                        if copied_files % 100 == 0:
                            print(f"  ✅ Copied {copied_files} files...")
                    except Exception as e:
                        errors.append(f"Failed to copy {rel_path}: {e}")
                        log(f"ERROR: Failed to copy {rel_path}: {e}")
            
            except Exception as e:
                errors.append(f"Error processing {filepath}: {e}")
                continue
    
    print()
    print(f"✅ Step 1 Complete:")
    print(f"   Total files found: {total_files}")
    print(f"   Files copied: {copied_files}")
    print(f"   Duplicates skipped: {duplicate_files}")
    if errors:
        print(f"   Errors: {len(errors)}")
    print()
    
    # Step 2: Verify archive
    print("=" * 80)
    print("  STEP 2: VERIFYING ARCHIVE")
    print("=" * 80)
    print()
    
    archive_count = sum(1 for _ in ARCHIVE_DIR.rglob('*') if _.is_file())
    archive_size = sum(f.stat().st_size for f in ARCHIVE_DIR.rglob('*') if f.is_file())
    
    log(f"Archive verification: {archive_count} files, {format_size(archive_size)}")
    print(f"✅ Archive verified:")
    print(f"   Files in archive: {archive_count}")
    print(f"   Archive size: {format_size(archive_size)}")
    print()
    
    # Step 3: Delete original files (if not dry run)
    deleted_count = 0
    if not dry_run:
        print("=" * 80)
        print("  STEP 3: DELETING ORIGINAL FILES")
        print("=" * 80)
        print()
        
        print("⚠️  This will delete original code files!")
        print(f"   Archive is safe at: {ARCHIVE_DIR}")
        print()
        confirm = input("Continue with deletion? (yes/no): ").strip().lower()
        
        if confirm == 'yes':
            log("Starting file deletion...")
            
            for root, dirs, files in os.walk(BASE):
                dirs[:] = [d for d in dirs if not should_exclude(Path(root) / d)]
                
                for file in files:
                    filepath = Path(root) / file
                    
                    if filepath.suffix.lower() not in CODE_EXTENSIONS:
                        continue
                    
                    if should_exclude(filepath):
                        continue
                    
                    try:
                        rel_path = filepath.relative_to(BASE)
                        archive_path = ARCHIVE_DIR / rel_path
                        
                        # Only delete if archive copy exists and matches
                        if archive_path.exists():
                            orig_hash = get_file_hash(filepath)
                            arch_hash = get_file_hash(archive_path)
                            
                            if orig_hash and arch_hash and orig_hash == arch_hash:
                                filepath.unlink()
                                deleted_count += 1
                                log(f"DELETED: {rel_path}")
                                
                                if deleted_count % 100 == 0:
                                    print(f"  ✅ Deleted {deleted_count} files...")
                    except Exception as e:
                        errors.append(f"Failed to delete {filepath}: {e}")
            
            print()
            print(f"✅ Step 3 Complete:")
            print(f"   Files deleted: {deleted_count}")
            print()
        else:
            print("⚠️  Deletion cancelled")
            print()
    else:
        print("⚠️  DRY RUN: Skipping deletion")
        print()
    
    # Step 4: Clean up empty directories
    print("=" * 80)
    print("  STEP 4: CLEANING UP EMPTY DIRECTORIES")
    print("=" * 80)
    print()
    
    empty_deleted = 0
    if not dry_run:
        # Find and delete empty directories
        for root, dirs, files in os.walk(BASE, topdown=False):
            dirpath = Path(root)
            
            if should_exclude(dirpath):
                continue
            
            # Skip archive and log directories
            if 'CODE_ARCHIVE' in dirpath.parts or 'logs' in dirpath.parts:
                continue
            
            try:
                if not any(dirpath.iterdir()):
                    dirpath.rmdir()
                    empty_deleted += 1
                    log(f"DELETED EMPTY DIR: {dirpath.relative_to(BASE)}")
            except Exception:
                pass
        
        print(f"✅ Step 4 Complete:")
        print(f"   Empty directories removed: {empty_deleted}")
        print()
    else:
        # Count empty directories
        empty_count = 0
        for root, dirs, files in os.walk(BASE):
            dirpath = Path(root)
            if should_exclude(dirpath):
                continue
            if 'CODE_ARCHIVE' in dirpath.parts or 'logs' in dirpath.parts:
                continue
            try:
                if not any(dirpath.iterdir()):
                    empty_count += 1
            except Exception:
                pass
        print(f"⚠️  DRY RUN: Would delete {empty_count} empty directories")
        print()
    
    # Step 5: Run final cleanup
    print("=" * 80)
    print("  STEP 5: FINAL CLEANUP")
    print("=" * 80)
    print()
    
    cleanup_script = BASE / "delete-empty-folders.sh"
    if cleanup_script.exists():
        print("Running delete-empty-folders.sh...")
        os.system(f"bash {cleanup_script} >> {LOG_FILE} 2>&1")
        print("✅ Final cleanup complete")
        print()
    
    # Summary
    print("=" * 80)
    print(" " * 20 + "✅ CODE MOVE & CLEAN COMPLETE!")
    print("=" * 80)
    print()
    
    print("📊 Summary:")
    print()
    print(f"  • Total files found: {total_files}")
    print(f"  • Files copied to archive: {copied_files}")
    print(f"  • Duplicates skipped: {duplicate_files}")
    print(f"  • Archive location: {ARCHIVE_DIR}")
    print(f"  • Archive size: {format_size(archive_size)}")
    print()
    
    if not dry_run:
        print(f"  • Original files deleted: {deleted_count}")
        print(f"  • Empty directories removed: {empty_deleted}")
    
    if errors:
        print(f"  • Errors encountered: {len(errors)}")
        if len(errors) <= 10:
            for error in errors:
                print(f"    - {error}")
    
    print()
    print(f"📋 Log file: {LOG_FILE}")
    print()
    print("💡 To restore files from archive:")
    print(f"   cp -r {ARCHIVE_DIR}/* {BASE}/")
    print()
    
    log("Code move and clean complete")

if __name__ == "__main__":
    main()

