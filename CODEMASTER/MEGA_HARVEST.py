#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║  🔥🔥🔥 MEGA HARVEST - THE ULTIMATE CODE EXTRACTION MACHINE 🔥🔥🔥                         ║
║══════════════════════════════════════════════════════════════════════════════════════════║
║  THERE'S A NEW CLAUDE IN TOWN - WE TAKE SHIT FROM NO ONE!!                               ║
║  ALL CODE → NOIZYLAB/CODEMASTER/HarvestedCode/ ORGANIZED BY PROJECT THEN DATE            ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝

Structure:
  HarvestedCode/
  ├── BY_PROJECT/
  │   ├── ProjectName_1/
  │   │   ├── 2024-01-15/
  │   │   │   ├── file1.py
  │   │   │   └── file2.py
  │   │   └── 2024-03-20/
  │   └── ProjectName_2/
  └── BY_VOLUME/
      ├── RED_DRAGON/
      ├── 12TB/
      └── 6TB/
"""

import os
import sys
import json
import sqlite3
import shutil
import hashlib
import re
from pathlib import Path
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict
import threading
import time

# ═══════════════════════════════════════════════════════════════════════════════
# CONFIGURATION - MAXIMUM POWER
# ═══════════════════════════════════════════════════════════════════════════════

CODEMASTER = Path("/Users/m2ultra/NOIZYLAB/CODEMASTER")
HARVESTED = CODEMASTER / "HarvestedCode"
BY_PROJECT = HARVESTED / "BY_PROJECT"
BY_VOLUME = HARVESTED / "BY_VOLUME"
FTS_DB = HARVESTED / "mega_code_search.db"

# 24 CORES = 24 WORKERS! MAXIMUM PARALLELISM!
MAX_WORKERS = 24

# Code extensions - COMPREHENSIVE
CODE_EXTENSIONS = {
    # Python
    '.py', '.pyx', '.pxd', '.pyi', '.ipynb',
    # JavaScript/TypeScript
    '.js', '.jsx', '.ts', '.tsx', '.mjs', '.cjs', '.vue', '.svelte',
    # Web
    '.html', '.htm', '.css', '.scss', '.sass', '.less',
    # Systems
    '.c', '.cpp', '.cc', '.cxx', '.h', '.hpp', '.hxx', '.rs', '.go',
    # JVM
    '.java', '.kt', '.kts', '.scala', '.clj', '.groovy',
    # Apple
    '.swift', '.m', '.mm',
    # .NET
    '.cs', '.fs', '.vb',
    # Scripting
    '.rb', '.php', '.pl', '.pm', '.lua', '.r', '.R', '.jl',
    # Shell
    '.sh', '.bash', '.zsh', '.fish', '.ps1', '.bat', '.cmd',
    # Data/Config
    '.json', '.yaml', '.yml', '.toml', '.xml', '.ini', '.cfg', '.conf',
    # Database
    '.sql', '.prisma', '.graphql', '.gql',
    # Other
    '.ex', '.exs', '.erl', '.hrl', '.hs', '.ml', '.mli', '.f90', '.f95',
    '.proto', '.thrift', '.avsc',
    # Docs
    '.md', '.rst', '.txt', '.tex',
    # Build/Config
    'Dockerfile', 'Makefile', 'Rakefile', 'Gemfile', 'Vagrantfile',
}

# Project markers - detect project roots
PROJECT_MARKERS = {
    '.git': 'git',
    'package.json': 'node',
    'Cargo.toml': 'rust',
    'go.mod': 'go',
    'requirements.txt': 'python',
    'setup.py': 'python',
    'pyproject.toml': 'python',
    'Gemfile': 'ruby',
    'pom.xml': 'java-maven',
    'build.gradle': 'java-gradle',
    '.xcodeproj': 'xcode',
    '.xcworkspace': 'xcode',
    'CMakeLists.txt': 'cmake',
    'Makefile': 'make',
    'docker-compose.yml': 'docker',
    '.sln': 'dotnet',
    'mix.exs': 'elixir',
    'stack.yaml': 'haskell',
    'dune-project': 'ocaml',
}

# Skip these
EXCLUDED_DIRS = {
    'node_modules', '__pycache__', '.git', 'venv', '.venv', 'env',
    '.env', 'site-packages', 'dist', 'build', '.tox', '.nox',
    '.pytest_cache', '.mypy_cache', '.ruff_cache', 'egg-info',
    '.eggs', 'htmlcov', '.coverage', 'coverage', '.idea', '.vscode',
    'vendor', 'deps', '_build', 'target', 'out', 'bin', 'obj',
    '.Spotlight-V100', '.fseventsd', '.Trashes', '.TemporaryItems',
    'Library', 'Photos Library.photoslibrary', '.Trash',
}

EXCLUDED_VOLUMES = {
    'Macintosh HD', 'Macintosh HD - Data', 'Recovery', 'VM', 'Preboot',
    'Update', 'com.apple', 'TimeMachine'
}

# Colors
class C:
    FIRE = '\033[38;5;196m'
    GOLD = '\033[38;5;220m'
    GREEN = '\033[38;5;46m'
    CYAN = '\033[38;5;51m'
    PURPLE = '\033[38;5;135m'
    BLUE = '\033[38;5;33m'
    WHITE = '\033[97m'
    DIM = '\033[2m'
    BOLD = '\033[1m'
    END = '\033[0m'

def c(text, color): return f"{color}{text}{C.END}"

# ═══════════════════════════════════════════════════════════════════════════════
# DATABASE - FTS5 FULL TEXT SEARCH
# ═══════════════════════════════════════════════════════════════════════════════

def init_db():
    """Initialize FTS5 database for lightning-fast code search"""
    HARVESTED.mkdir(parents=True, exist_ok=True)
    BY_PROJECT.mkdir(parents=True, exist_ok=True)
    BY_VOLUME.mkdir(parents=True, exist_ok=True)
    
    conn = sqlite3.connect(FTS_DB, check_same_thread=False)
    cur = conn.cursor()
    
    cur.executescript("""
        -- Main files table
        CREATE TABLE IF NOT EXISTS code_files (
            id INTEGER PRIMARY KEY,
            filepath TEXT UNIQUE,
            filename TEXT,
            extension TEXT,
            project_name TEXT,
            project_type TEXT,
            source_volume TEXT,
            file_date TEXT,
            size INTEGER,
            hash TEXT,
            harvested_path TEXT,
            harvested_at TEXT,
            lines INTEGER
        );
        
        -- Projects table
        CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY,
            name TEXT,
            path TEXT UNIQUE,
            type TEXT,
            source_volume TEXT,
            file_count INTEGER,
            total_size INTEGER,
            discovered_at TEXT
        );
        
        -- FTS5 virtual table for content search
        CREATE VIRTUAL TABLE IF NOT EXISTS code_fts USING fts5(
            filepath,
            filename,
            project_name,
            content,
            tokenize='porter unicode61'
        );
        
        -- Harvest log
        CREATE TABLE IF NOT EXISTS harvest_log (
            id INTEGER PRIMARY KEY,
            timestamp TEXT,
            volume TEXT,
            files_harvested INTEGER,
            projects_found INTEGER,
            total_size INTEGER,
            duration_seconds REAL
        );
        
        -- Indexes
        CREATE INDEX IF NOT EXISTS idx_files_project ON code_files(project_name);
        CREATE INDEX IF NOT EXISTS idx_files_volume ON code_files(source_volume);
        CREATE INDEX IF NOT EXISTS idx_files_ext ON code_files(extension);
        CREATE INDEX IF NOT EXISTS idx_files_hash ON code_files(hash);
        CREATE INDEX IF NOT EXISTS idx_projects_type ON projects(type);
    """)
    
    conn.commit()
    return conn

DB_LOCK = threading.Lock()

# ═══════════════════════════════════════════════════════════════════════════════
# UTILITIES
# ═══════════════════════════════════════════════════════════════════════════════

def get_file_hash(filepath, quick=True):
    """Fast file hash using xxhash if available, else md5"""
    try:
        import xxhash
        h = xxhash.xxh64()
    except ImportError:
        h = hashlib.md5()
    
    try:
        with open(filepath, 'rb') as f:
            if quick:
                h.update(f.read(65536))  # First 64KB
            else:
                for chunk in iter(lambda: f.read(8192), b''):
                    h.update(chunk)
        return h.hexdigest()
    except:
        return None

def get_file_date(filepath):
    """Get file modification date as YYYY-MM-DD"""
    try:
        mtime = os.path.getmtime(filepath)
        return datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
    except:
        return datetime.now().strftime('%Y-%m-%d')

def sanitize_name(name):
    """Sanitize name for filesystem"""
    name = re.sub(r'[<>:"/\\|?*]', '_', name)
    name = re.sub(r'\s+', '_', name)
    return name[:100]  # Limit length

def should_skip_dir(dirname):
    """Check if directory should be skipped"""
    return dirname in EXCLUDED_DIRS or dirname.startswith('.')

def is_code_file(filepath):
    """Check if file is a code file"""
    path = Path(filepath)
    return path.suffix.lower() in CODE_EXTENSIONS or path.name in CODE_EXTENSIONS

def count_lines(filepath):
    """Count lines in file"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            return sum(1 for _ in f)
    except:
        return 0

def get_volumes():
    """Get all mounted volumes"""
    volumes = []
    for vol in Path("/Volumes").iterdir():
        if vol.is_dir() and vol.name not in EXCLUDED_VOLUMES:
            try:
                # Test if accessible
                list(vol.iterdir())
                volumes.append(vol)
            except:
                pass
    return sorted(volumes, key=lambda x: x.name)

# ═══════════════════════════════════════════════════════════════════════════════
# PROJECT DETECTION
# ═══════════════════════════════════════════════════════════════════════════════

def detect_project(dirpath):
    """Detect if directory is a project root and return project info"""
    path = Path(dirpath)
    
    for marker, ptype in PROJECT_MARKERS.items():
        marker_path = path / marker
        if marker_path.exists():
            return {
                'name': path.name,
                'path': str(path),
                'type': ptype,
                'marker': marker
            }
    
    return None

def find_parent_project(filepath):
    """Find parent project for a file"""
    path = Path(filepath)
    
    for parent in path.parents:
        if str(parent) == '/':
            break
        
        project = detect_project(parent)
        if project:
            return project
    
    return None

# ═══════════════════════════════════════════════════════════════════════════════
# HARVESTING ENGINE
# ═══════════════════════════════════════════════════════════════════════════════

class MegaHarvester:
    def __init__(self, conn):
        self.conn = conn
        self.stats = defaultdict(int)
        self.projects = {}
        self.processed_hashes = set()
        self.lock = threading.Lock()
        
        # Load existing hashes
        cur = conn.cursor()
        cur.execute("SELECT hash FROM code_files WHERE hash IS NOT NULL")
        for row in cur.fetchall():
            self.processed_hashes.add(row[0])
    
    def harvest_file(self, filepath, volume_name):
        """Harvest a single code file"""
        try:
            path = Path(filepath)
            
            # Get file info
            stat = path.stat()
            file_hash = get_file_hash(filepath)
            
            # Skip duplicates
            if file_hash and file_hash in self.processed_hashes:
                with self.lock:
                    self.stats['duplicates'] += 1
                return None
            
            # Find parent project
            project = find_parent_project(filepath)
            project_name = project['name'] if project else 'STANDALONE'
            project_type = project['type'] if project else 'unknown'
            
            # Get file date
            file_date = get_file_date(filepath)
            
            # Create destination path: BY_PROJECT/ProjectName/YYYY-MM-DD/filename
            safe_project = sanitize_name(project_name)
            dest_dir = BY_PROJECT / safe_project / file_date
            dest_dir.mkdir(parents=True, exist_ok=True)
            
            # Handle filename conflicts
            dest_path = dest_dir / path.name
            counter = 1
            while dest_path.exists():
                stem = path.stem
                suffix = path.suffix
                dest_path = dest_dir / f"{stem}_{counter}{suffix}"
                counter += 1
            
            # Copy file
            shutil.copy2(filepath, dest_path)
            
            # Also copy to BY_VOLUME
            vol_dir = BY_VOLUME / sanitize_name(volume_name) / safe_project
            vol_dir.mkdir(parents=True, exist_ok=True)
            vol_dest = vol_dir / path.name
            if not vol_dest.exists():
                shutil.copy2(filepath, vol_dest)
            
            # Read content for FTS (limit to 100KB)
            content = ""
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read(102400)
            except:
                pass
            
            # Count lines
            lines = count_lines(filepath)
            
            # Update stats
            with self.lock:
                self.stats['files'] += 1
                self.stats['size'] += stat.st_size
                self.stats['lines'] += lines
                if file_hash:
                    self.processed_hashes.add(file_hash)
                
                # Track project
                if project:
                    if project['path'] not in self.projects:
                        self.projects[project['path']] = project
            
            return {
                'filepath': str(filepath),
                'filename': path.name,
                'extension': path.suffix.lower(),
                'project_name': project_name,
                'project_type': project_type,
                'source_volume': volume_name,
                'file_date': file_date,
                'size': stat.st_size,
                'hash': file_hash,
                'harvested_path': str(dest_path),
                'lines': lines,
                'content': content
            }
            
        except Exception as e:
            with self.lock:
                self.stats['errors'] += 1
            return None
    
    def harvest_volume(self, volume, progress_callback=None):
        """Harvest all code from a volume"""
        volume_name = volume.name
        start_time = time.time()
        
        # Collect files
        code_files = []
        scanned = 0
        
        for root, dirs, files in os.walk(volume, followlinks=False):
            # Filter excluded dirs
            dirs[:] = [d for d in dirs if not should_skip_dir(d)]
            
            scanned += 1
            if scanned % 1000 == 0 and progress_callback:
                progress_callback(volume_name, scanned, len(code_files))
            
            for f in files:
                filepath = os.path.join(root, f)
                if is_code_file(filepath):
                    code_files.append(filepath)
        
        print(f"\n  {c('📁', C.CYAN)} Found {c(str(len(code_files)), C.GOLD)} code files in {volume_name}")
        
        # Harvest with ThreadPool
        results = []
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = {
                executor.submit(self.harvest_file, fp, volume_name): fp 
                for fp in code_files
            }
            
            for i, future in enumerate(as_completed(futures)):
                result = future.result()
                if result:
                    results.append(result)
                
                if (i + 1) % 500 == 0:
                    print(f"\r  {c('⚡', C.FIRE)} Harvested: {c(str(len(results)), C.GREEN)} / {len(code_files)} ({len(results)/len(code_files)*100:.1f}%)", end='', flush=True)
        
        # Batch insert to database
        if results:
            with DB_LOCK:
                cur = self.conn.cursor()
                
                # Insert files
                cur.executemany("""
                    INSERT OR REPLACE INTO code_files 
                    (filepath, filename, extension, project_name, project_type, 
                     source_volume, file_date, size, hash, harvested_path, harvested_at, lines)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, [(
                    r['filepath'], r['filename'], r['extension'], r['project_name'],
                    r['project_type'], r['source_volume'], r['file_date'], r['size'],
                    r['hash'], r['harvested_path'], datetime.now().isoformat(), r['lines']
                ) for r in results])
                
                # Insert to FTS
                cur.executemany("""
                    INSERT OR REPLACE INTO code_fts (filepath, filename, project_name, content)
                    VALUES (?, ?, ?, ?)
                """, [(r['filepath'], r['filename'], r['project_name'], r['content']) for r in results])
                
                # Insert projects
                for proj in self.projects.values():
                    cur.execute("""
                        INSERT OR REPLACE INTO projects (name, path, type, source_volume, discovered_at)
                        VALUES (?, ?, ?, ?, ?)
                    """, (proj['name'], proj['path'], proj['type'], volume_name, datetime.now().isoformat()))
                
                # Log harvest
                duration = time.time() - start_time
                cur.execute("""
                    INSERT INTO harvest_log (timestamp, volume, files_harvested, projects_found, total_size, duration_seconds)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (datetime.now().isoformat(), volume_name, len(results), len(self.projects), self.stats['size'], duration))
                
                self.conn.commit()
        
        return len(results), len(self.projects)

# ═══════════════════════════════════════════════════════════════════════════════
# EMPTY FOLDER PURGE - NUCLEAR OPTION
# ═══════════════════════════════════════════════════════════════════════════════

def purge_empty_folders_nuclear():
    """DELETE ALL EMPTY FOLDERS - NO MERCY"""
    print(f"\n{c('🧹 NUCLEAR EMPTY FOLDER PURGE ACTIVATED!', C.FIRE + C.BOLD)}")
    print(c('═' * 70, C.DIM))
    
    volumes = get_volumes()
    total_deleted = 0
    
    for vol in volumes:
        print(f"\n{c('💣', C.FIRE)} Purging: {c(vol.name, C.GOLD)}")
        deleted = 0
        
        # Walk bottom-up
        for root, dirs, files in os.walk(vol, topdown=False, followlinks=False):
            # Skip system dirs
            if any(ex in root for ex in ['.Spotlight', '.fseventsd', '.Trashes', 'Library/Caches']):
                continue
            
            for d in dirs:
                dirpath = os.path.join(root, d)
                try:
                    # Check if empty
                    if not os.listdir(dirpath):
                        os.rmdir(dirpath)
                        deleted += 1
                        if deleted % 100 == 0:
                            print(f"\r  {c('✓', C.GREEN)} Deleted: {c(str(deleted), C.GOLD)}", end='', flush=True)
                except:
                    pass
        
        print(f"\r  {c('✓', C.GREEN)} Volume {vol.name}: {c(str(deleted), C.GOLD)} empty folders deleted")
        total_deleted += deleted
    
    print(f"\n{c('🎯 TOTAL DELETED:', C.FIRE + C.BOLD)} {c(str(total_deleted), C.GOLD)} empty folders")
    return total_deleted

# ═══════════════════════════════════════════════════════════════════════════════
# REPORTING
# ═══════════════════════════════════════════════════════════════════════════════

def generate_report(conn):
    """Generate comprehensive harvest report"""
    cur = conn.cursor()
    
    print(f"\n{c('📊 MEGA HARVEST REPORT', C.GOLD + C.BOLD)}")
    print(c('═' * 70, C.DIM))
    
    # Total stats
    cur.execute("SELECT COUNT(*), SUM(size), SUM(lines) FROM code_files")
    files, size, lines = cur.fetchone()
    files = files or 0
    size = size or 0
    lines = lines or 0
    
    print(f"\n{c('📁 TOTAL HARVESTED:', C.CYAN)}")
    print(f"  Files:  {c(f'{files:,}', C.GOLD)}")
    print(f"  Size:   {c(f'{size / (1024**3):.2f} GB', C.GOLD)}")
    print(f"  Lines:  {c(f'{lines:,}', C.GOLD)}")
    
    # By project type
    print(f"\n{c('🚀 BY PROJECT TYPE:', C.CYAN)}")
    cur.execute("""
        SELECT project_type, COUNT(*), SUM(size) 
        FROM code_files 
        GROUP BY project_type 
        ORDER BY COUNT(*) DESC
        LIMIT 15
    """)
    for ptype, count, psize in cur.fetchall():
        print(f"  {ptype:<15} {c(str(count), C.GREEN):>8} files  {(psize or 0) / (1024**2):>8.1f} MB")
    
    # By extension
    print(f"\n{c('📄 BY EXTENSION:', C.CYAN)}")
    cur.execute("""
        SELECT extension, COUNT(*), SUM(lines)
        FROM code_files 
        WHERE extension != ''
        GROUP BY extension 
        ORDER BY COUNT(*) DESC
        LIMIT 15
    """)
    for ext, count, elines in cur.fetchall():
        print(f"  {ext:<10} {c(str(count), C.GREEN):>8} files  {(elines or 0):>10,} lines")
    
    # By volume
    print(f"\n{c('💾 BY SOURCE VOLUME:', C.CYAN)}")
    cur.execute("""
        SELECT source_volume, COUNT(*), SUM(size)
        FROM code_files 
        GROUP BY source_volume 
        ORDER BY COUNT(*) DESC
    """)
    for vol, count, vsize in cur.fetchall():
        print(f"  {vol:<25} {c(str(count), C.GREEN):>8} files  {(vsize or 0) / (1024**2):>8.1f} MB")
    
    # Top projects
    print(f"\n{c('🏆 TOP 20 PROJECTS:', C.CYAN)}")
    cur.execute("""
        SELECT project_name, project_type, COUNT(*), SUM(lines)
        FROM code_files 
        WHERE project_name != 'STANDALONE'
        GROUP BY project_name 
        ORDER BY COUNT(*) DESC
        LIMIT 20
    """)
    for name, ptype, count, plines in cur.fetchall():
        print(f"  {name[:30]:<30} [{ptype}] {c(str(count), C.GREEN):>6} files  {(plines or 0):>8,} lines")
    
    # Output locations
    print(f"\n{c('📂 OUTPUT LOCATIONS:', C.CYAN)}")
    print(f"  BY_PROJECT: {BY_PROJECT}")
    print(f"  BY_VOLUME:  {BY_VOLUME}")
    print(f"  DATABASE:   {FTS_DB}")

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════

def print_banner():
    print(f"""
{c('╔══════════════════════════════════════════════════════════════════════════════════════════╗', C.FIRE)}
{c('║', C.FIRE)}  {c('🔥🔥🔥 MEGA HARVEST - THE ULTIMATE CODE EXTRACTION MACHINE 🔥🔥🔥', C.GOLD + C.BOLD)}                   {c('║', C.FIRE)}
{c('╠══════════════════════════════════════════════════════════════════════════════════════════╣', C.FIRE)}
{c('║', C.FIRE)}  {c("THERE'S A NEW CLAUDE IN TOWN - WE TAKE SHIT FROM NO ONE!!", C.WHITE + C.BOLD)}                         {c('║', C.FIRE)}
{c('║', C.FIRE)}  {c('ALL CODE → CODEMASTER/HarvestedCode/ BY PROJECT THEN DATE', C.CYAN)}                              {c('║', C.FIRE)}
{c('╠══════════════════════════════════════════════════════════════════════════════════════════╣', C.FIRE)}
{c('║', C.FIRE)}  Workers: {c('24', C.GREEN)} | Cores: {c('24', C.GREEN)} | RAM: {c('192GB', C.GREEN)} | FTS5: {c('ENABLED', C.GREEN)}                              {c('║', C.FIRE)}
{c('╚══════════════════════════════════════════════════════════════════════════════════════════╝', C.FIRE)}
""")

def main():
    print_banner()
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        
        if cmd == 'purge':
            purge_empty_folders_nuclear()
            return
        
        if cmd == 'report':
            conn = init_db()
            generate_report(conn)
            conn.close()
            return
        
        if cmd == 'search':
            query = ' '.join(sys.argv[2:])
            conn = init_db()
            cur = conn.cursor()
            cur.execute("""
                SELECT filepath, project_name, snippet(code_fts, 3, '>>>', '<<<', '...', 50)
                FROM code_fts WHERE content MATCH ?
                LIMIT 20
            """, (query,))
            results = cur.fetchall()
            print(f"\n{c(f'Found {len(results)} matches for:', C.CYAN)} {query}\n")
            for path, proj, snippet in results:
                print(f"{c(proj, C.GOLD)}: {path}")
                print(f"  {snippet[:200]}\n")
            conn.close()
            return
    
    # DEFAULT: MEGA HARVEST ALL VOLUMES!
    print(f"{c('🎯 MEGA HARVEST MODE: ALL VOLUMES!', C.FIRE + C.BOLD)}")
    
    conn = init_db()
    harvester = MegaHarvester(conn)
    
    volumes = get_volumes()
    print(f"\n{c('📀 VOLUMES TO HARVEST:', C.CYAN)} {len(volumes)}")
    for vol in volumes:
        print(f"  {c('•', C.GREEN)} {vol.name}")
    
    print(f"\n{c('⚡ STARTING MEGA HARVEST WITH 24 WORKERS!', C.FIRE + C.BOLD)}")
    print(c('─' * 70, C.DIM))
    
    total_files = 0
    total_projects = 0
    
    def progress(vol_name, scanned, found):
        print(f"\r  {c('🔍', C.CYAN)} {vol_name}: Scanned {scanned:,} dirs, found {found:,} code files", end='', flush=True)
    
    for vol in volumes:
        print(f"\n{c('🔥 HARVESTING:', C.FIRE)} {c(vol.name, C.GOLD + C.BOLD)}")
        
        try:
            files, projects = harvester.harvest_volume(vol, progress)
            total_files += files
            total_projects += projects
            print(f"\n  {c('✅', C.GREEN)} Harvested {c(str(files), C.GOLD)} files from {c(str(projects), C.GOLD)} projects")
        except Exception as e:
            print(f"\n  {c('❌', C.FIRE)} Error: {e}")
    
    # Final report
    print(f"\n\n{c('═' * 70, C.GOLD)}")
    print(f"{c('🏆 MEGA HARVEST COMPLETE!', C.GOLD + C.BOLD)}")
    print(f"{c('═' * 70, C.GOLD)}")
    print(f"  Total Files:    {c(f'{total_files:,}', C.GREEN)}")
    print(f"  Total Projects: {c(str(total_projects), C.GREEN)}")
    print(f"  Duplicates:     {c(str(harvester.stats.get('duplicates', 0)), C.CYAN)}")
    print(f"  Errors:         {c(str(harvester.stats.get('errors', 0)), C.FIRE)}")
    
    generate_report(conn)
    conn.close()
    
    print(f"\n{c('🔥 ALL CODE NOW IN CODEMASTER! 🔥', C.FIRE + C.BOLD)}")

if __name__ == "__main__":
    main()
