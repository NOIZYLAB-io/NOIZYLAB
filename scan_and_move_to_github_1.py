#!/usr/bin/env python3
"""
Scan and move all code files from MAG 4TB workspace to GitHub/Noizyfish/NOIZYLAB
Maintains directory structure and handles conflicts intelligently.
"""

import os
import shutil
from pathlib import Path

# Source and target directories
SOURCE_ROOT = "/Volumes/MAG 4TB/NoizyWorkspace"
TARGET_ROOT = "/Users/m2ultra/Github/Noizyfish/NOIZYLAB"

# Code file extensions to move (including all text-based files)
CODE_EXTENSIONS = {".py", ".sh", ".md", ".js", ".ts", ".json", ".txt", ".yaml", ".yml", ".log", ".cfg", ".conf", ".ini", ".xml", ".csv"}

# Files/directories to skip
SKIP_PATTERNS = {
    ".git",
    ".DS_Store",
    "__pycache__",
    ".pyc",
    ".history",
    "node_modules",
    ".env",
    ".gitignore"
}

def should_skip(path):
    """Check if file/directory should be skipped."""
    path_str = str(path)
    for pattern in SKIP_PATTERNS:
        if pattern in path_str:
            return True
    return False

def get_relative_path(source_path, source_root):
    """Get relative path from source root."""
    try:
        return os.path.relpath(source_path, source_root)
    except ValueError:
        # Handle case where paths are on different drives
        return os.path.basename(source_path)

def move_file(src, dst):
    """Move file with conflict handling."""
    if os.path.exists(dst):
        # File exists, create backup name
        base, ext = os.path.splitext(dst)
        counter = 1
        while os.path.exists(f"{base}_{counter}{ext}"):
            counter += 1
        dst = f"{base}_{counter}{ext}"
        print(f"⚠️  Conflict: Renaming to {os.path.basename(dst)}")
    
    # Create target directory if needed
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    
    # Move file
    shutil.copy2(src, dst)
    print(f"✅ Copied: {os.path.basename(src)} → {os.path.relpath(dst, TARGET_ROOT)}")
    return dst

def scan_and_move():
    """Scan source directory and move all code files."""
    moved_count = 0
    skipped_count = 0
    
    print(f"🔍 Scanning: {SOURCE_ROOT}")
    print(f"📦 Target: {TARGET_ROOT}\n")
    
    # Ensure target exists
    os.makedirs(TARGET_ROOT, exist_ok=True)
    
    # Walk through source directory
    for root, dirs, files in os.walk(SOURCE_ROOT):
        # Skip hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and not should_skip(os.path.join(root, d))]
        
        for filename in files:
            src_path = os.path.join(root, filename)
            
            # Skip if should be skipped
            if should_skip(src_path):
                skipped_count += 1
                continue
            
            # Check if it's a code file
            ext = os.path.splitext(filename)[1].lower()
            if ext not in CODE_EXTENSIONS:
                skipped_count += 1
                continue
            
            # Calculate target path maintaining structure
            rel_path = get_relative_path(src_path, SOURCE_ROOT)
            dst_path = os.path.join(TARGET_ROOT, rel_path)
            
            try:
                move_file(src_path, dst_path)
                moved_count += 1
            except Exception as e:
                print(f"❌ Error moving {filename}: {e}")
    
    print(f"\n🎉 Complete!")
    print(f"   ✅ Moved: {moved_count} files")
    print(f"   ⏭️  Skipped: {skipped_count} files")
    return moved_count

if __name__ == "__main__":
    print("=" * 70)
    print("🚀 NOIZY CODE MIGRATION TO GITHUB")
    print("=" * 70)
    print()
    
    moved = scan_and_move()
    
    if moved > 0:
        print(f"\n💡 Next steps:")
        print(f"   1. Review files in: {TARGET_ROOT}")
        print(f"   2. Commit: cd {TARGET_ROOT} && git add . && git commit -m 'Add code from MAG 4TB workspace'")
        print(f"   3. Push: git push origin main")

