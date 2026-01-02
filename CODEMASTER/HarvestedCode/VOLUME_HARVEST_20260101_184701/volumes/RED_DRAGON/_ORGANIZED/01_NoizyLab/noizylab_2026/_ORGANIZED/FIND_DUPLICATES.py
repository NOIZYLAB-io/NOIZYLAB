#!/usr/bin/env python3
"""
Find Duplicate Projects and Files in _ORGANIZED
"""

import os
import hashlib
from pathlib import Path
from collections import defaultdict
from datetime import datetime

ORGANIZED = Path("/Volumes/RED DRAGON/noizylab_2026/_ORGANIZED")

def calculate_hash(file_path, chunk_size=8192):
    """Calculate SHA256 hash of file"""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(chunk_size):
                sha256.update(chunk)
        return sha256.hexdigest()
    except:
        return None

def find_duplicate_names():
    """Find projects with duplicate names across categories"""
    print("🔍 Finding projects with duplicate names...")
    print("=" * 80)
    
    project_names = defaultdict(list)
    
    for category in ORGANIZED.iterdir():
        if category.is_dir() and not category.name.startswith('.'):
            for project in category.iterdir():
                if project.is_dir():
                    project_names[project.name].append({
                        'category': category.name,
                        'path': str(project)
                    })
    
    duplicates = {name: paths for name, paths in project_names.items() if len(paths) > 1}
    
    if duplicates:
        print(f"\n⚠️  Found {len(duplicates)} duplicate project names:\n")
        for name, paths in sorted(duplicates.items()):
            print(f"📦 {name}")
            for path_info in paths:
                print(f"   → {path_info['category']}/")
            print()
    else:
        print("✅ No duplicate project names found!")
    
    return duplicates

def find_large_files(min_size_mb=50):
    """Find large files"""
    print(f"\n🔍 Finding large files (>{min_size_mb}MB)...")
    print("=" * 80)
    
    large_files = []
    min_bytes = min_size_mb * 1024 * 1024
    
    for category in ORGANIZED.iterdir():
        if category.is_dir() and not category.name.startswith('.'):
            for root, dirs, files in os.walk(category):
                # Skip common large directories
                dirs[:] = [d for d in dirs if d not in ['node_modules', '.git', 'venv', '.venv']]
                
                for file in files:
                    file_path = Path(root) / file
                    try:
                        size = file_path.stat().st_size
                        if size >= min_bytes:
                            large_files.append({
                                'path': str(file_path.relative_to(ORGANIZED)),
                                'size': size
                            })
                    except:
                        pass
    
    if large_files:
        # Sort by size
        large_files.sort(key=lambda x: x['size'], reverse=True)
        
        print(f"\n📊 Found {len(large_files)} large files:\n")
        for i, file_info in enumerate(large_files[:20], 1):
            size_mb = file_info['size'] / (1024 * 1024)
            print(f"  {i:2}. {size_mb:8.1f} MB  →  {file_info['path']}")
        
        if len(large_files) > 20:
            print(f"\n  ... and {len(large_files) - 20} more")
    else:
        print("✅ No large files found!")
    
    return large_files

def find_empty_directories():
    """Find empty project directories"""
    print("\n🔍 Finding empty directories...")
    print("=" * 80)
    
    empty_dirs = []
    
    for category in ORGANIZED.iterdir():
        if category.is_dir() and not category.name.startswith('.'):
            for project in category.iterdir():
                if project.is_dir():
                    # Check if directory is empty or only contains .git/.DS_Store
                    items = list(project.iterdir())
                    if not items or all(item.name in ['.git', '.DS_Store', '.gitignore'] for item in items):
                        empty_dirs.append({
                            'category': category.name,
                            'project': project.name,
                            'path': str(project.relative_to(ORGANIZED))
                        })
    
    if empty_dirs:
        print(f"\n⚠️  Found {len(empty_dirs)} empty/almost-empty directories:\n")
        for dir_info in empty_dirs:
            print(f"  📁 {dir_info['category']}/{dir_info['project']}")
    else:
        print("✅ No empty directories found!")
    
    return empty_dirs

def find_orphaned_files():
    """Find files in root that should be in categories"""
    print("\n🔍 Finding orphaned files...")
    print("=" * 80)
    
    orphaned = []
    
    for item in ORGANIZED.iterdir():
        if item.is_file() and item.name not in ['.catalog.json', '.DS_Store']:
            orphaned.append({
                'name': item.name,
                'path': str(item.relative_to(ORGANIZED)),
                'size': item.stat().st_size
            })
    
    if orphaned:
        print(f"\n⚠️  Found {len(orphaned)} orphaned files in root:\n")
        for file_info in orphaned:
            size_kb = file_info['size'] / 1024
            print(f"  📄 {file_info['name']} ({size_kb:.1f} KB)")
    else:
        print("✅ No orphaned files found!")
    
    return orphaned

def main():
    print("=" * 80)
    print(" " * 25 + "DUPLICATE FINDER")
    print("=" * 80)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Run all checks
    duplicates = find_duplicate_names()
    large_files = find_large_files()
    empty_dirs = find_empty_directories()
    orphaned = find_orphaned_files()
    
    # Summary
    print("\n" + "=" * 80)
    print("📊 SUMMARY")
    print("=" * 80)
    print(f"Duplicate names: {len(duplicates)}")
    print(f"Large files (>50MB): {len(large_files)}")
    print(f"Empty directories: {len(empty_dirs)}")
    print(f"Orphaned files: {len(orphaned)}")
    print("=" * 80)
    
    # Save report
    report_file = ORGANIZED / ".duplicates_report.txt"
    with open(report_file, 'w') as f:
        f.write(f"Duplicate Finder Report - {datetime.now().isoformat()}\n")
        f.write("=" * 80 + "\n\n")
        
        if duplicates:
            f.write("DUPLICATE PROJECT NAMES:\n")
            for name, paths in duplicates.items():
                f.write(f"{name}\n")
                for p in paths:
                    f.write(f"  → {p['category']}/\n")
                f.write("\n")
        
        if large_files:
            f.write("\nLARGE FILES:\n")
            for file_info in large_files[:50]:
                size_mb = file_info['size'] / (1024 * 1024)
                f.write(f"{size_mb:.1f} MB - {file_info['path']}\n")
        
        if empty_dirs:
            f.write("\nEMPTY DIRECTORIES:\n")
            for dir_info in empty_dirs:
                f.write(f"{dir_info['path']}\n")
        
        if orphaned:
            f.write("\nORPHANED FILES:\n")
            for file_info in orphaned:
                f.write(f"{file_info['path']}\n")
    
    print(f"\n💾 Report saved: {report_file}")
    print("\n✅ Analysis complete!")

if __name__ == "__main__":
    main()

