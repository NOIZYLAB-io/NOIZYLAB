#!/usr/bin/env python3
"""
VOLUME HARVEST - TURBO EDITION
==============================
Extracts all custom Python code from local volumes before Mac Pro reformat.
Creates a timestamped backup with FTS index integration.

USAGE:
  python volume_harvest.py                    # Harvest all priority volumes
  python volume_harvest.py /Volumes/RED\ DRAGON  # Harvest specific volume
"""

import os
import sys
import shutil
import sqlite3
import hashlib
from datetime import datetime
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import re

# Configuration
HARVEST_DIR = Path("/Users/m2ultra/NOIZYLAB/CODEMASTER/HarvestedCode")
FTS_DB = HARVEST_DIR / "global_fts.db"

# Priority volumes for pre-reformat extraction
PRIORITY_VOLUMES = [
    ("/Volumes/RED DRAGON", "RED_DRAGON"),
    ("/Volumes/12TB", "12TB"),
    ("/Volumes/6TB", "6TB"),
    ("/Volumes/RSP", "RSP"),
]

# Exclude patterns (venvs, site-packages, etc.)
EXCLUDE_PATTERNS = [
    r'/site-packages/',
    r'/__pycache__/',
    r'/\.venv/',
    r'/venv/',
    r'/lib/python\d',
    r'/\.git/',
    r'/node_modules/',
    r'\.pyc$',
]

def should_exclude(filepath: str) -> bool:
    """Check if file should be excluded."""
    for pattern in EXCLUDE_PATTERNS:
        if re.search(pattern, filepath):
            return True
    return False

def get_file_hash(filepath: str) -> str:
    """Calculate MD5 hash of file."""
    try:
        with open(filepath, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except:
        return "error"

def init_harvest_db(run_dir: Path):
    """Initialize harvest metadata database."""
    db_path = run_dir / "harvest_meta.db"
    conn = sqlite3.connect(str(db_path))
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS harvested_files (
        id INTEGER PRIMARY KEY,
        original_path TEXT,
        harvested_path TEXT,
        volume TEXT,
        file_hash TEXT,
        size_bytes INTEGER,
        harvested_at TEXT,
        UNIQUE(file_hash)
    )''')
    conn.commit()
    return conn

def scan_volume(volume_path: str, volume_name: str) -> list:
    """Scan volume for Python files, excluding venvs."""
    python_files = []
    print(f"🔍 Scanning {volume_name}...")
    
    for root, dirs, files in os.walk(volume_path):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if not should_exclude(os.path.join(root, d))]
        
        for file in files:
            if file.endswith('.py'):
                filepath = os.path.join(root, file)
                if not should_exclude(filepath):
                    python_files.append(filepath)
    
    print(f"   Found {len(python_files)} Python files")
    return python_files

def harvest_file(filepath: str, volume_name: str, run_dir: Path) -> dict:
    """Copy a single file to harvest directory."""
    try:
        # Create relative path structure
        rel_path = filepath.replace("/Volumes/", "").replace(" ", "_")
        dest_path = run_dir / "volumes" / rel_path
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Copy file
        shutil.copy2(filepath, dest_path)
        
        # Get metadata
        stat = os.stat(filepath)
        file_hash = get_file_hash(filepath)
        
        return {
            "original_path": filepath,
            "harvested_path": str(dest_path),
            "volume": volume_name,
            "file_hash": file_hash,
            "size_bytes": stat.st_size,
            "success": True
        }
    except Exception as e:
        return {
            "original_path": filepath,
            "error": str(e),
            "success": False
        }

def add_to_fts(run_dir: Path, harvested_files: list):
    """Add harvested files to global FTS index."""
    print("\n📚 Indexing into FTS...")
    
    conn = sqlite3.connect(str(FTS_DB))
    c = conn.cursor()
    
    # Ensure FTS table exists
    c.execute('''CREATE VIRTUAL TABLE IF NOT EXISTS code_fts USING fts5(
        filename, filepath, content, repo, language
    )''')
    
    indexed = 0
    for f in harvested_files:
        if not f.get("success"):
            continue
        try:
            with open(f["harvested_path"], 'r', encoding='utf-8', errors='ignore') as fp:
                content = fp.read()
            
            c.execute('''INSERT INTO code_fts (filename, filepath, content, repo, language)
                        VALUES (?, ?, ?, ?, ?)''',
                     (os.path.basename(f["original_path"]),
                      f["original_path"],
                      content,
                      f"VOLUME:{f['volume']}",
                      "python"))
            indexed += 1
        except Exception as e:
            pass
    
    conn.commit()
    conn.close()
    print(f"   Indexed {indexed} files into FTS")

def harvest_volumes(volumes: list = None):
    """Main harvest function."""
    if volumes is None:
        volumes = PRIORITY_VOLUMES
    
    # Create run directory
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = HARVEST_DIR / f"VOLUME_HARVEST_{timestamp}"
    run_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"""
╔══════════════════════════════════════════════════════════╗
║     🔥 VOLUME HARVEST - TURBO EDITION 🔥                 ║
║                                                          ║
║     Pre-Reformat Code Extraction System                  ║
╚══════════════════════════════════════════════════════════╝

📁 Output: {run_dir}
""")
    
    # Initialize database
    db_conn = init_harvest_db(run_dir)
    
    all_harvested = []
    total_files = 0
    total_size = 0
    
    for volume_path, volume_name in volumes:
        if not os.path.exists(volume_path):
            print(f"⏭️  Skipping {volume_name} (not mounted)")
            continue
        
        # Scan for Python files
        python_files = scan_volume(volume_path, volume_name)
        
        if not python_files:
            print(f"   No Python files found")
            continue
        
        # Harvest files with progress
        print(f"📦 Harvesting {len(python_files)} files from {volume_name}...")
        harvested = []
        
        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = {executor.submit(harvest_file, f, volume_name, run_dir): f 
                      for f in python_files}
            
            for i, future in enumerate(as_completed(futures)):
                result = future.result()
                harvested.append(result)
                
                if result["success"]:
                    total_files += 1
                    total_size += result.get("size_bytes", 0)
                    
                    # Save to database
                    try:
                        db_conn.execute('''INSERT OR IGNORE INTO harvested_files 
                            (original_path, harvested_path, volume, file_hash, size_bytes, harvested_at)
                            VALUES (?, ?, ?, ?, ?, ?)''',
                            (result["original_path"], result["harvested_path"],
                             result["volume"], result["file_hash"], result["size_bytes"],
                             datetime.now().isoformat()))
                    except:
                        pass
                
                if (i + 1) % 500 == 0:
                    print(f"   Progress: {i+1}/{len(python_files)}")
        
        db_conn.commit()
        all_harvested.extend(harvested)
        
        success_count = sum(1 for h in harvested if h["success"])
        print(f"   ✅ Harvested {success_count}/{len(python_files)} files")
    
    # Add to FTS index
    add_to_fts(run_dir, all_harvested)
    
    # Write summary
    summary = {
        "timestamp": timestamp,
        "total_files": total_files,
        "total_size_mb": round(total_size / 1024 / 1024, 2),
        "volumes_processed": [v[1] for v in volumes if os.path.exists(v[0])],
        "output_dir": str(run_dir)
    }
    
    with open(run_dir / "harvest_summary.json", 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"""
╔══════════════════════════════════════════════════════════╗
║     🎉 HARVEST COMPLETE 🎉                               ║
╠══════════════════════════════════════════════════════════╣
║  Total Files: {total_files:>10}                                ║
║  Total Size:  {summary['total_size_mb']:>10.2f} MB                         ║
║  Volumes:     {', '.join(summary['volumes_processed']):<20}         ║
╠══════════════════════════════════════════════════════════╣
║  Output: {str(run_dir):<40} ║
╚══════════════════════════════════════════════════════════╝

🔍 Search with: sqlite3 {FTS_DB}
   SELECT * FROM code_fts WHERE code_fts MATCH 'your_search_term';
""")
    
    db_conn.close()
    return summary

def search_fts(query: str, limit: int = 20):
    """Search the global FTS index."""
    conn = sqlite3.connect(str(FTS_DB))
    c = conn.cursor()
    
    c.execute('''SELECT filename, filepath, repo, 
                 snippet(code_fts, 2, '>>>', '<<<', '...', 50) as snippet
                 FROM code_fts 
                 WHERE code_fts MATCH ?
                 LIMIT ?''', (query, limit))
    
    results = c.fetchall()
    conn.close()
    
    print(f"\n🔍 Search results for '{query}':\n")
    for filename, filepath, repo, snippet in results:
        print(f"📄 {filename} [{repo}]")
        print(f"   {filepath}")
        print(f"   {snippet}\n")
    
    return results

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "search":
            # Search mode
            query = " ".join(sys.argv[2:])
            search_fts(query)
        else:
            # Harvest specific volume
            vol_path = sys.argv[1]
            vol_name = os.path.basename(vol_path).replace(" ", "_")
            harvest_volumes([(vol_path, vol_name)])
    else:
        # Harvest all priority volumes
        harvest_volumes()
