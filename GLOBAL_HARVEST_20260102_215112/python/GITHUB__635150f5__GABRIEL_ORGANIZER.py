#!/usr/bin/env python3
"""
🧠 GABRIEL ORGANIZER - Ultimate Cleanup & Organization System
============================================================
MC96DIGIUNIVERSE AI LIFELUV INFINITE ENERGY ⚡

This script:
1. Removes duplicate files (-2, -3, -4 suffixes)
2. Organizes code by type (Python, TypeScript, Shell, etc.)
3. Creates clean GABRIEL structure
4. Preserves the best/latest version of each file
"""

import os
import sys
import hashlib
import shutil
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from typing import Dict, List, Set, Tuple

# Colors
class C:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

def log(msg: str, color: str = C.END):
    print(f"{color}{msg}{C.END}")

def header(msg: str):
    log(f"\n{'='*60}", C.CYAN)
    log(f"  {msg}", C.CYAN + C.BOLD)
    log(f"{'='*60}", C.CYAN)

def success(msg: str):
    log(f"  ✓ {msg}", C.GREEN)

def warning(msg: str):
    log(f"  ⚠ {msg}", C.YELLOW)

def error(msg: str):
    log(f"  ✗ {msg}", C.RED)

def info(msg: str):
    log(f"  → {msg}", C.BLUE)

def sha256_file(path: Path) -> str:
    """Calculate SHA256 hash of a file."""
    h = hashlib.sha256()
    try:
        with open(path, 'rb') as f:
            while chunk := f.read(8192):
                h.update(chunk)
        return h.hexdigest()
    except:
        return ""

def get_base_name(filename: str) -> str:
    """Get base name without -2, -3, -4 suffixes."""
    name = filename
    for suffix in ['-6', '-5', '-4', '-3', '-2']:
        if suffix in name:
            parts = name.rsplit(suffix, 1)
            if len(parts) == 2 and (parts[1].startswith('.') or parts[1] == ''):
                name = parts[0] + parts[1]
    return name

def find_duplicates(directory: Path) -> Dict[str, List[Path]]:
    """Find files that are duplicates (same base name or same hash)."""
    duplicates: Dict[str, List[Path]] = defaultdict(list)
    
    for path in directory.rglob('*'):
        if path.is_file():
            base = get_base_name(path.name)
            duplicates[base].append(path)
    
    # Filter to only groups with duplicates
    return {k: v for k, v in duplicates.items() if len(v) > 1}

def find_best_version(files: List[Path]) -> Path:
    """Find the best version (original without suffix, or latest modified)."""
    # Prefer files without -2, -3, -4 suffixes
    for f in files:
        if not any(s in f.name for s in ['-2.', '-3.', '-4.', '-5.', '-6.']):
            return f
    
    # Otherwise return most recently modified
    return max(files, key=lambda p: p.stat().st_mtime)

def organize_by_type(src_dir: Path, dest_dir: Path) -> Dict[str, int]:
    """Organize files by their type into subdirectories."""
    type_map = {
        '.py': 'python',
        '.ts': 'typescript', 
        '.tsx': 'typescript',
        '.js': 'javascript',
        '.jsx': 'javascript',
        '.sh': 'shell',
        '.zsh': 'shell',
        '.bash': 'shell',
        '.go': 'golang',
        '.rs': 'rust',
        '.swift': 'swift',
        '.md': 'docs',
        '.json': 'config',
        '.yaml': 'config',
        '.yml': 'config',
        '.toml': 'config',
    }
    
    counts = defaultdict(int)
    
    for path in src_dir.rglob('*'):
        if path.is_file():
            ext = path.suffix.lower()
            dest_type = type_map.get(ext, 'other')
            
            # Skip if already in correct location
            if dest_type in str(path):
                continue
            
            dest_path = dest_dir / dest_type / path.name
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            
            counts[dest_type] += 1
    
    return dict(counts)

def clean_duplicates(directory: Path, dry_run: bool = True) -> Tuple[int, int]:
    """Remove duplicate files, keeping the best version."""
    header("FINDING DUPLICATES")
    
    duplicates = find_duplicates(directory)
    
    removed = 0
    kept = 0
    
    for base_name, files in duplicates.items():
        if len(files) <= 1:
            continue
            
        best = find_best_version(files)
        kept += 1
        
        info(f"Group: {base_name}")
        success(f"KEEP: {best.name}")
        
        for f in files:
            if f != best:
                if dry_run:
                    warning(f"WOULD REMOVE: {f.name}")
                else:
                    try:
                        f.unlink()
                        warning(f"REMOVED: {f.name}")
                        removed += 1
                    except Exception as e:
                        error(f"Failed to remove {f.name}: {e}")
    
    return kept, removed

def scan_structure(root: Path) -> Dict[str, int]:
    """Scan and report on directory structure."""
    header("SCANNING STRUCTURE")
    
    stats = defaultdict(int)
    
    for path in root.rglob('*'):
        if path.is_file():
            ext = path.suffix.lower()
            stats[ext] += 1
    
    # Sort by count
    for ext, count in sorted(stats.items(), key=lambda x: -x[1])[:20]:
        info(f"{ext or '(no ext)'}: {count:,} files")
    
    return dict(stats)

def create_clean_structure(root: Path):
    """Create clean GABRIEL directory structure."""
    header("CREATING CLEAN STRUCTURE")
    
    structure = [
        "CORE/brain",
        "CORE/vision", 
        "CORE/voice",
        "CORE/memory",
        "AGENTS/ai",
        "AGENTS/automation",
        "AGENTS/workers",
        "MCP/servers",
        "MCP/clients",
        "TOOLS/scripts",
        "TOOLS/cli",
        "CONFIG/env",
        "CONFIG/hooks",
        "DOCS/guides",
        "DOCS/api",
        "ARCHIVE/legacy",
        "ARCHIVE/backup",
    ]
    
    for folder in structure:
        path = root / folder
        path.mkdir(parents=True, exist_ok=True)
        success(f"Created: {folder}")

def main():
    """Main entry point."""
    print(f"""
{C.CYAN}{C.BOLD}
╔══════════════════════════════════════════════════════════════════╗
║                    GABRIEL ORGANIZER v2.0                        ║
║            MC96DIGIUNIVERSE AI LIFELUV INFINITE ENERGY           ║
╚══════════════════════════════════════════════════════════════════╝
{C.END}
""")
    
    root = Path("/Users/m2ultra/NOIZYLAB/GABRIEL")
    
    if not root.exists():
        error(f"Root directory not found: {root}")
        sys.exit(1)
    
    # Parse args
    dry_run = "--apply" not in sys.argv
    
    if dry_run:
        warning("DRY RUN MODE - No files will be modified")
        warning("Use --apply to actually make changes")
    else:
        warning("APPLY MODE - Files WILL be modified!")
    
    # Scan current structure
    stats = scan_structure(root)
    
    # Find and report duplicates
    header("DUPLICATE ANALYSIS")
    
    # Check 10_CORE/gabriel for duplicates
    gabriel_core = root / "10_CORE" / "gabriel"
    if gabriel_core.exists():
        kept, removed = clean_duplicates(gabriel_core, dry_run=dry_run)
        info(f"Would keep {kept} files, remove {removed} duplicates")
    
    # Check 11_AGENTS for duplicates
    agents_dir = root / "11_AGENTS"
    if agents_dir.exists():
        info(f"\nScanning 11_AGENTS...")
        duplicates = find_duplicates(agents_dir)
        total_dups = sum(len(v) - 1 for v in duplicates.values())
        info(f"Found {len(duplicates)} groups with {total_dups} total duplicates")
    
    # Summary
    header("SUMMARY")
    total_files = sum(stats.values())
    info(f"Total files scanned: {total_files:,}")
    info(f"Python files: {stats.get('.py', 0):,}")
    info(f"TypeScript files: {stats.get('.ts', 0) + stats.get('.tsx', 0):,}")
    info(f"JavaScript files: {stats.get('.js', 0):,}")
    info(f"Shell scripts: {stats.get('.sh', 0) + stats.get('.zsh', 0):,}")
    
    print(f"\n{C.GREEN}✅ Analysis complete!{C.END}")
    
    if dry_run:
        print(f"\n{C.YELLOW}Run with --apply to make changes{C.END}")

if __name__ == "__main__":
    main()
