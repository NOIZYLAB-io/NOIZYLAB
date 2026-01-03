#!/usr/bin/env python3
"""
QUICK NOIZYLAB ORGANIZER - Fast & Lightweight
Organizes files without heavy scanning operations
"""

import os
import shutil
from pathlib import Path
from datetime import datetime

NOIZYLAB = Path("/Users/m2ultra/NOIZYLAB")
SCRIPTS_DIR = NOIZYLAB / "scripts"
DOCS_DIR = NOIZYLAB / "docs"
ARCHIVE_DIR = NOIZYLAB / ".archive"

def quick_organize():
    """Fast organization without heavy operations"""
    print("🚀 QUICK NOIZYLAB ORGANIZER")
    print("=" * 60)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Create directories
    SCRIPTS_DIR.mkdir(exist_ok=True)
    DOCS_DIR.mkdir(exist_ok=True)
    ARCHIVE_DIR.mkdir(exist_ok=True)
    
    moved = 0
    
    # Move shell scripts
    print("📦 Organizing scripts...")
    for file in NOIZYLAB.glob("*.sh"):
        if file.name not in ["MASTER_CLEANUP_ORGANIZER.sh", "media_offload.sh"]:
            try:
                dest = SCRIPTS_DIR / file.name
                if not dest.exists():
                    shutil.move(str(file), str(dest))
                    print(f"  ✓ {file.name} → scripts/")
                    moved += 1
            except Exception as e:
                print(f"  ✗ {file.name}: {e}")
    
    # Move Python scripts (root level)
    print("\n📦 Organizing Python scripts...")
    for file in NOIZYLAB.glob("*.py"):
        if file.name not in ["QUICK_ORGANIZE.py", "disk_usage_analyzer.py"]:
            try:
                dest = SCRIPTS_DIR / file.name
                if not dest.exists():
                    shutil.move(str(file), str(dest))
                    print(f"  ✓ {file.name} → scripts/")
                    moved += 1
            except Exception as e:
                print(f"  ✗ {file.name}: {e}")
    
    # Move documentation
    print("\n📄 Organizing documentation...")
    for file in NOIZYLAB.glob("*.md"):
        if file.name not in ["README.md", "STRUCTURE.md"]:
            try:
                dest = DOCS_DIR / file.name
                if not dest.exists():
                    shutil.move(str(file), str(dest))
                    print(f"  ✓ {file.name} → docs/")
                    moved += 1
            except Exception as e:
                print(f"  ✗ {file.name}: {e}")
    
    # Archive old versioned scripts
    print("\n📦 Archiving versioned scripts...")
    versioned = list(NOIZYLAB.glob("*_V*.sh")) + list(NOIZYLAB.glob("*_V*.py"))
    versioned = [f for f in versioned if f.is_file()]
    
    if versioned:
        archive_versions = ARCHIVE_DIR / "old-versions"
        archive_versions.mkdir(exist_ok=True)
        
        for file in versioned:
            try:
                dest = archive_versions / file.name
                if not dest.exists():
                    shutil.move(str(file), str(dest))
                    print(f"  ✓ {file.name} → .archive/old-versions/")
                    moved += 1
            except Exception as e:
                print(f"  ✗ {file.name}: {e}")
    
    # Remove .DS_Store
    print("\n🧹 Cleaning .DS_Store files...")
    dsstore_count = 0
    for dsstore in NOIZYLAB.rglob(".DS_Store"):
        try:
            dsstore.unlink()
            dsstore_count += 1
        except:
            pass
    print(f"  ✓ Removed {dsstore_count} .DS_Store files")
    
    print("\n" + "=" * 60)
    print(f"✅ COMPLETE! Moved {moved} files")
    print(f"Finished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

if __name__ == "__main__":
    quick_organize()

