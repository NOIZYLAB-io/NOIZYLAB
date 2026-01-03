#!/usr/bin/env python3
"""
╔════════════════════════════════════════════════════════════════════════════════╗
║  🌾 GABRIEL HARVEST INVENTORY - Find All Code Without Copying                  ║
║  Creates searchable index for Cursor/Antigravity to process                    ║
║  MC96DIGIUNIVERSE // GORUNFREE PROTOCOL // INFINITE ENERGY ⚡                  ║
╚════════════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import json
import hashlib
import sqlite3
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Set
from concurrent.futures import ThreadPoolExecutor
import multiprocessing

# ════════════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ════════════════════════════════════════════════════════════════════════════════

GABRIEL_ROOT = Path(__file__).parent.parent.resolve()
DB_PATH = GABRIEL_ROOT / "inventory.db"
MAX_WORKERS = multiprocessing.cpu_count()

# Code extensions to harvest
CODE_EXTENSIONS = {
    '.py', '.ts', '.tsx', '.js', '.jsx', '.sh', '.bash', '.zsh',
    '.sql', '.swift', '.rs', '.go', '.c', '.cpp', '.h', '.hpp',
    '.java', '.kt', '.rb', '.php', '.vue', '.svelte', '.astro',
    '.toml', '.yaml', '.yml', '.json', '.md', '.txt'
}

# Directories to skip
SKIP_DIRS = {
    'node_modules', '.git', '__pycache__', '.venv', 'venv', 'env',
    'dist', 'build', '.next', '.nuxt', 'coverage', '.turbo',
    '.cache', 'cache', 'Caches', 'Library', 'Applications',
    '.Trash', 'Downloads', '.npm', '.yarn', '.pnpm',
    'HarvestedCode', 'GLOBAL_HARVEST', '_HARVEST'
}

# Skip these exact paths
SKIP_PATHS = {
    '/System', '/Library', '/private', '/usr', '/bin', '/sbin',
    '/opt/homebrew/Cellar', '/Applications'
}

# ════════════════════════════════════════════════════════════════════════════════
# DATABASE SETUP
# ════════════════════════════════════════════════════════════════════════════════

def init_db(db_path: Path) -> sqlite3.Connection:
    """Initialize the inventory database."""
    conn = sqlite3.connect(str(db_path))
    conn.execute('''
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            path TEXT UNIQUE NOT NULL,
            filename TEXT NOT NULL,
            extension TEXT,
            size INTEGER,
            modified TEXT,
            hash TEXT,
            first_lines TEXT,
            volume TEXT,
            project TEXT,
            scanned_at TEXT
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            path TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            type TEXT,
            has_git INTEGER,
            remote_url TEXT,
            file_count INTEGER,
            total_size INTEGER,
            scanned_at TEXT
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS duplicates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hash TEXT NOT NULL,
            path1 TEXT NOT NULL,
            path2 TEXT NOT NULL,
            size INTEGER
        )
    ''')
    conn.execute('CREATE INDEX IF NOT EXISTS idx_files_hash ON files(hash)')
    conn.execute('CREATE INDEX IF NOT EXISTS idx_files_ext ON files(extension)')
    conn.execute('CREATE INDEX IF NOT EXISTS idx_files_project ON files(project)')
    conn.execute('CREATE VIRTUAL TABLE IF NOT EXISTS files_fts USING fts5(path, filename, first_lines, content=files, content_rowid=id)')
    conn.commit()
    return conn


# ════════════════════════════════════════════════════════════════════════════════
# SCANNING FUNCTIONS
# ════════════════════════════════════════════════════════════════════════════════

def should_skip(path: Path) -> bool:
    """Check if path should be skipped."""
    path_str = str(path)
    
    # Skip exact paths
    for skip in SKIP_PATHS:
        if path_str.startswith(skip):
            return True
    
    # Skip directories
    for part in path.parts:
        if part in SKIP_DIRS:
            return True
        if part.startswith('.') and part not in {'.github', '.vscode'}:
            return True
    
    return False


def get_file_hash(file_path: Path, size_limit: int = 1024 * 1024) -> Optional[str]:
    """Get MD5 hash of file (first 1MB for large files)."""
    try:
        with open(file_path, 'rb') as f:
            content = f.read(size_limit)
            return hashlib.md5(content).hexdigest()
    except Exception:
        return None


def get_first_lines(file_path: Path, num_lines: int = 50) -> str:
    """Get first N lines of a file."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = []
            for i, line in enumerate(f):
                if i >= num_lines:
                    break
                lines.append(line.rstrip()[:200])  # Limit line length
            return '\n'.join(lines)
    except Exception:
        return ""


def detect_project(file_path: Path) -> Optional[str]:
    """Detect the project root for a file."""
    current = file_path.parent
    
    # Look for project markers
    markers = {'package.json', 'pyproject.toml', 'Cargo.toml', 'go.mod', '.git', 'Makefile'}
    
    for _ in range(10):  # Max 10 levels up
        if current == current.parent:
            break
        
        for marker in markers:
            if (current / marker).exists():
                return str(current)
        
        current = current.parent
    
    return None


def scan_file(file_path: Path) -> Optional[Dict]:
    """Scan a single file and return its metadata."""
    try:
        if not file_path.is_file():
            return None
        
        stat = file_path.stat()
        
        return {
            'path': str(file_path),
            'filename': file_path.name,
            'extension': file_path.suffix.lower(),
            'size': stat.st_size,
            'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
            'hash': get_file_hash(file_path),
            'first_lines': get_first_lines(file_path),
            'volume': file_path.parts[2] if len(file_path.parts) > 2 else 'root',
            'project': detect_project(file_path),
            'scanned_at': datetime.now().isoformat()
        }
    except Exception as e:
        return None


def scan_directory(root: Path, extensions: Set[str] = None) -> List[Path]:
    """Collect all code files in a directory."""
    if extensions is None:
        extensions = CODE_EXTENSIONS
    
    files = []
    
    try:
        for item in root.iterdir():
            if should_skip(item):
                continue
            
            if item.is_dir():
                files.extend(scan_directory(item, extensions))
            elif item.is_file() and item.suffix.lower() in extensions:
                files.append(item)
    except PermissionError:
        pass
    except Exception:
        pass
    
    return files


# ════════════════════════════════════════════════════════════════════════════════
# MAIN HARVEST FUNCTION
# ════════════════════════════════════════════════════════════════════════════════

def harvest_inventory(
    roots: List[Path],
    db_path: Path = DB_PATH,
    extensions: Set[str] = None
) -> Dict:
    """
    Harvest inventory of all code files.
    Does NOT copy files - only creates searchable index.
    """
    print()
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║  🌾 GABRIEL HARVEST INVENTORY                                 ║")
    print("║  Creating searchable index (no files copied)                  ║")
    print("╚═══════════════════════════════════════════════════════════════╝")
    print()
    
    conn = init_db(db_path)
    
    stats = {
        'total_files': 0,
        'total_size': 0,
        'by_extension': {},
        'by_volume': {},
        'projects_found': set(),
        'duplicates': 0,
        'errors': 0
    }
    
    # Collect all files
    all_files = []
    for root in roots:
        print(f"  📂 Scanning: {root}")
        if root.exists():
            files = scan_directory(root, extensions)
            all_files.extend(files)
            print(f"     Found: {len(files)} files")
    
    print()
    print(f"  📊 Total files to index: {len(all_files)}")
    print(f"  ⚡ Using {MAX_WORKERS} CPU cores")
    print()
    
    # Parallel scan
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        results = list(executor.map(scan_file, all_files))
    
    # Insert into database
    hashes = {}
    for result in results:
        if result is None:
            stats['errors'] += 1
            continue
        
        try:
            conn.execute('''
                INSERT OR REPLACE INTO files 
                (path, filename, extension, size, modified, hash, first_lines, volume, project, scanned_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                result['path'], result['filename'], result['extension'],
                result['size'], result['modified'], result['hash'],
                result['first_lines'], result['volume'], result['project'],
                result['scanned_at']
            ))
            
            stats['total_files'] += 1
            stats['total_size'] += result['size']
            
            ext = result['extension']
            stats['by_extension'][ext] = stats['by_extension'].get(ext, 0) + 1
            
            vol = result['volume']
            stats['by_volume'][vol] = stats['by_volume'].get(vol, 0) + 1
            
            if result['project']:
                stats['projects_found'].add(result['project'])
            
            # Track duplicates
            if result['hash']:
                if result['hash'] in hashes:
                    stats['duplicates'] += 1
                    conn.execute('''
                        INSERT INTO duplicates (hash, path1, path2, size)
                        VALUES (?, ?, ?, ?)
                    ''', (result['hash'], hashes[result['hash']], result['path'], result['size']))
                else:
                    hashes[result['hash']] = result['path']
                    
        except Exception as e:
            stats['errors'] += 1
    
    conn.commit()
    
    # Update FTS index
    conn.execute('INSERT INTO files_fts(files_fts) VALUES("rebuild")')
    conn.commit()
    conn.close()
    
    # Convert set to count for JSON serialization
    stats['projects_found'] = len(stats['projects_found'])
    
    # Print results
    print()
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║  ✅ HARVEST COMPLETE                                          ║")
    print("╠═══════════════════════════════════════════════════════════════╣")
    print(f"║  Total Files:    {stats['total_files']:,}".ljust(63) + "║")
    print(f"║  Total Size:     {stats['total_size'] / (1024*1024):.1f} MB".ljust(63) + "║")
    print(f"║  Projects Found: {stats['projects_found']}".ljust(63) + "║")
    print(f"║  Duplicates:     {stats['duplicates']}".ljust(63) + "║")
    print(f"║  Database:       {db_path}".ljust(63)[:63] + "║")
    print("╠═══════════════════════════════════════════════════════════════╣")
    print("║  Top Extensions:".ljust(63) + "║")
    
    sorted_ext = sorted(stats['by_extension'].items(), key=lambda x: -x[1])[:10]
    for ext, count in sorted_ext:
        print(f"║    {ext}: {count:,}".ljust(63) + "║")
    
    print("╚═══════════════════════════════════════════════════════════════╝")
    print()
    print(f"  💡 Search with: sqlite3 {db_path}")
    print("     SELECT * FROM files WHERE first_lines LIKE '%search_term%';")
    print("     SELECT * FROM files_fts WHERE files_fts MATCH 'query';")
    print()
    
    return stats


# ════════════════════════════════════════════════════════════════════════════════
# CLI
# ════════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="GABRIEL Harvest Inventory")
    parser.add_argument("paths", nargs="*", help="Paths to scan")
    parser.add_argument("--db", type=str, default=str(DB_PATH), help="Database path")
    parser.add_argument("--all", action="store_true", help="Scan all mounted volumes")
    
    args = parser.parse_args()
    
    if args.all:
        # Scan all volumes
        roots = [Path("/Volumes")]
        roots.append(Path("/Users/m2ultra"))
    elif args.paths:
        roots = [Path(p) for p in args.paths]
    else:
        # Default: scan NOIZYLAB
        roots = [Path("/Users/m2ultra/NOIZYLAB")]
    
    harvest_inventory(roots, Path(args.db))
