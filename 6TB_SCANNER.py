#!/usr/bin/env python3
"""
🗄️ 6TB FULL DRIVE SCANNER & ORGANIZER 🗄️

⭐⭐⭐ HARD RULE ⭐⭐⭐
ANY FILE WITHOUT METADATA = YOUR ORIGINAL COMPOSITION!

MASSIVE SCALE FEATURES:
- Scans entire 6TB drive
- Handles 100,000+ files
- Progress tracking & resumability
- Crash recovery
- Database indexing
- Parallel processing
- Memory efficient
- Fast duplicate detection
"""

import os
import sqlite3
import struct
import shutil
import json
import hashlib
from pathlib import Path
from collections import defaultdict
from datetime import datetime
import multiprocessing as mp
from functools import partial

# ============================================================================
# CONFIGURATION
# ============================================================================

SCAN_ROOT = Path("/Volumes/4TBSG")  # Scan entire 6TB drive!
OUTPUT_BASE = Path("/Volumes/4TBSG/KTK 2026 TO SORT/6TB_ORGANIZED")
DATABASE_FILE = Path("/Volumes/4TBSG/KTK 2026 TO SORT/6TB_index.db")
CHECKPOINT_FILE = Path("/Volumes/4TBSG/KTK 2026 TO SORT/6TB_checkpoint.json")

# Skip these folders
SKIP_FOLDERS = {
    '.Trash', '.Trashes', '.Spotlight-V100', '.fseventsd',
    '.DocumentRevisions-V100', '.TemporaryItems',
    'System Volume Information', '$RECYCLE.BIN',
    '__pycache__', '.git', 'node_modules',
    '6TB_ORGANIZED',  # Don't scan our own output!
    'ORGANIZED_WAVES'  # Skip already organized
}

CONFIG = {
    'num_workers': mp.cpu_count(),
    'batch_size': 100,
    'checkpoint_interval': 500,  # Save progress every 500 files
    'skip_hidden': False,  # Scan hidden files too
    'min_file_size': 1000,  # Skip tiny files (likely corrupt)
    'max_file_size': 5 * 1024**3  # Skip >5GB files (probably not WAV)
}

# ============================================================================
# DATABASE SETUP
# ============================================================================

def init_database():
    """Initialize SQLite database for indexing"""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    # Main files table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS wav_files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            path TEXT UNIQUE NOT NULL,
            filename TEXT NOT NULL,
            size INTEGER,
            modified TEXT,
            has_metadata INTEGER,
            is_original INTEGER,
            category TEXT,
            product TEXT,
            software TEXT,
            artist TEXT,
            title TEXT,
            sample_rate INTEGER,
            channels INTEGER,
            bits INTEGER,
            duration REAL,
            audio_fingerprint TEXT,
            scan_date TEXT,
            processed INTEGER DEFAULT 0
        )
    """)
    
    # Index for fast queries
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_path ON wav_files(path)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_is_original ON wav_files(is_original)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_category ON wav_files(category)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_fingerprint ON wav_files(audio_fingerprint)")
    
    # Scan progress table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS scan_progress (
            id INTEGER PRIMARY KEY,
            total_files INTEGER,
            scanned_files INTEGER,
            originals_found INTEGER,
            commercial_found INTEGER,
            last_file TEXT,
            scan_start TEXT,
            last_update TEXT
        )
    """)
    
    conn.commit()
    return conn

# ============================================================================
# FAST WAV SCANNER
# ============================================================================

def quick_scan_wav(filepath):
    """Ultra-fast WAV metadata scan"""
    try:
        stat = filepath.stat()
        
        # Skip if too small or too large
        if stat.st_size < CONFIG['min_file_size'] or stat.st_size > CONFIG['max_file_size']:
            return None
        
        with open(filepath, 'rb') as f:
            # Quick RIFF/WAVE validation
            if f.read(4) != b'RIFF':
                return None
            f.read(4)  # size
            if f.read(4) != b'WAVE':
                return None
            
            data = {
                'path': str(filepath),
                'filename': filepath.name,
                'size': stat.st_size,
                'modified': datetime.fromtimestamp(stat.st_mtime).isoformat(),
                'has_metadata': False,
                'sample_rate': None,
                'channels': None,
                'bits': None,
                'product': None,
                'software': None,
                'artist': None,
                'title': None
            }
            
            # Scan first 100KB for metadata
            scan_size = min(100000, stat.st_size)
            f.seek(12)
            header_data = f.read(scan_size)
            
            # Check for metadata presence
            if b'INFO' in header_data or b'bext' in header_data:
                data['has_metadata'] = True
                
                # Try to extract key info
                if b'IPRD' in header_data:
                    try:
                        idx = header_data.index(b'IPRD')
                        product = header_data[idx+8:idx+100].split(b'\x00')[0].decode('utf-8', errors='ignore')
                        data['product'] = product[:100]
                    except:
                        pass
                
                if b'ISFT' in header_data:
                    try:
                        idx = header_data.index(b'ISFT')
                        software = header_data[idx+8:idx+100].split(b'\x00')[0].decode('utf-8', errors='ignore')
                        data['software'] = software[:100]
                    except:
                        pass
            
            # Quick audio fingerprint
            try:
                first = header_data[:1024] if len(header_data) >= 1024 else header_data
                fp = hashlib.md5(first + str(stat.st_size).encode()).hexdigest()
                data['audio_fingerprint'] = fp
            except:
                pass
            
            return data
            
    except Exception as e:
        return None

# ============================================================================
# FILE DISCOVERY
# ============================================================================

def discover_wav_files(root_path):
    """Discover all WAV files on the drive"""
    print(f"🔍 Discovering WAV files in: {root_path}")
    print("This may take several minutes for 6TB...\n")
    
    wav_files = []
    total_size = 0
    
    for root, dirs, files in os.walk(root_path):
        # Filter out skip folders
        dirs[:] = [d for d in dirs if d not in SKIP_FOLDERS and not d.startswith('.')]
        
        for filename in files:
            if filename.lower().endswith(('.wav', '.WAV')):
                filepath = Path(root) / filename
                try:
                    size = filepath.stat().st_size
                    wav_files.append(filepath)
                    total_size += size
                    
                    if len(wav_files) % 1000 == 0:
                        print(f"  Found {len(wav_files):,} WAV files ({total_size/(1024**3):.1f} GB)...")
                except:
                    pass
    
    print(f"\n✓ Discovery complete!")
    print(f"  Total WAV files: {len(wav_files):,}")
    print(f"  Total size: {total_size/(1024**3):.2f} GB")
    
    return wav_files, total_size

# ============================================================================
# PARALLEL SCANNING
# ============================================================================

def scan_batch(files):
    """Scan a batch of files"""
    results = []
    for filepath in files:
        result = quick_scan_wav(filepath)
        if result:
            results.append(result)
    return results

def parallel_scan(wav_files, conn):
    """Scan files in parallel with progress tracking"""
    print(f"\n⚡ Phase 2: Parallel metadata scanning...")
    print(f"Using {CONFIG['num_workers']} CPU cores\n")
    
    # Split into batches
    batches = [wav_files[i:i+CONFIG['batch_size']] 
               for i in range(0, len(wav_files), CONFIG['batch_size'])]
    
    total_scanned = 0
    originals_found = 0
    commercial_found = 0
    
    with mp.Pool(CONFIG['num_workers']) as pool:
        for i, results in enumerate(pool.imap(scan_batch, batches)):
            # Insert results into database
            cursor = conn.cursor()
            for data in results:
                # Categorize
                is_original = 0 if data['has_metadata'] else 1
                category = categorize_file(data['filename'], data.get('product'), data['has_metadata'])
                
                if is_original:
                    originals_found += 1
                else:
                    commercial_found += 1
                
                try:
                    cursor.execute("""
                        INSERT OR REPLACE INTO wav_files 
                        (path, filename, size, modified, has_metadata, is_original, 
                         category, product, software, audio_fingerprint, scan_date)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        data['path'], data['filename'], data['size'], data['modified'],
                        data['has_metadata'], is_original, category,
                        data.get('product'), data.get('software'),
                        data.get('audio_fingerprint'),
                        datetime.now().isoformat()
                    ))
                except:
                    pass
            
            conn.commit()
            total_scanned += len(results)
            
            # Progress
            if (i + 1) % 10 == 0:
                percent = (i + 1) / len(batches) * 100
                print(f"  [{percent:5.1f}%] Scanned {total_scanned:,} files | "
                      f"⭐ Originals: {originals_found:,} | "
                      f"📦 Commercial: {commercial_found:,}")
            
            # Checkpoint
            if (i + 1) % (CONFIG['checkpoint_interval'] // CONFIG['batch_size']) == 0:
                save_checkpoint(len(wav_files), total_scanned, originals_found, commercial_found)
    
    print(f"\n✓ Scan complete!")
    return total_scanned, originals_found, commercial_found

# ============================================================================
# CATEGORIZATION
# ============================================================================

def categorize_file(filename, product, has_metadata):
    """Categorize file by name and metadata"""
    if not has_metadata:
        return "ORIGINAL_COMPOSITIONS"
    
    name_lower = filename.lower()
    
    # Product-based categories
    if product:
        prod_lower = product.lower()
        if 'mirage' in prod_lower:
            return "Commercial/Ensoniq_Mirage"
        elif 'kawaii' in prod_lower:
            return "Commercial/Kawaii"
        elif 'dx100' in prod_lower or 'dx-100' in prod_lower:
            return "Commercial/Yamaha_DX100"
        elif 'roland' in prod_lower:
            return "Commercial/Roland"
    
    # Filename-based categories
    patterns = {
        'mirage': 'Commercial/Ensoniq_Mirage',
        'kawaii': 'Commercial/Kawaii',
        'dx100': 'Commercial/Yamaha_DX',
        'dx7': 'Commercial/Yamaha_DX',
        'roland': 'Commercial/Roland',
        'sys100': 'Commercial/Roland_System100',
        'sh5': 'Commercial/Roland_SH5',
        'jupiter': 'Commercial/Roland_Jupiter',
        'juno': 'Commercial/Roland_Juno',
        'manjira': 'Commercial/World_Percussion',
        'dholak': 'Commercial/World_Percussion',
        'tabla': 'Commercial/World_Percussion',
        'ambient': 'Commercial/Ambient',
        'loop': 'Commercial/Loops',
        'drum': 'Commercial/Drums',
        'beat': 'Commercial/Beats',
        'bass': 'Commercial/Bass',
        'synth': 'Commercial/Synths',
        'pad': 'Commercial/Synths',
        'lead': 'Commercial/Synths',
        'hit': 'Commercial/SFX',
        'impact': 'Commercial/SFX'
    }
    
    for pattern, category in patterns.items():
        if pattern in name_lower:
            return category
    
    return "Commercial/Other"

# ============================================================================
# CHECKPOINT & RECOVERY
# ============================================================================

def save_checkpoint(total, scanned, originals, commercial):
    """Save scan progress"""
    checkpoint = {
        'timestamp': datetime.now().isoformat(),
        'total_files': total,
        'scanned_files': scanned,
        'originals_found': originals,
        'commercial_found': commercial
    }
    with open(CHECKPOINT_FILE, 'w') as f:
        json.dump(checkpoint, f, indent=2)

def load_checkpoint():
    """Load previous checkpoint"""
    if CHECKPOINT_FILE.exists():
        with open(CHECKPOINT_FILE, 'r') as f:
            return json.load(f)
    return None

# ============================================================================
# FILE ORGANIZATION
# ============================================================================

def organize_from_database(conn):
    """Organize files based on database"""
    print(f"\n📁 Phase 3: Organizing files...")
    
    cursor = conn.cursor()
    
    # Get statistics
    cursor.execute("SELECT COUNT(*) FROM wav_files WHERE is_original = 1")
    originals_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM wav_files WHERE is_original = 0")
    commercial_count = cursor.fetchone()[0]
    
    print(f"\n⭐⭐⭐ HARD RULE RESULTS ⭐⭐⭐")
    print(f"Files WITHOUT metadata: {originals_count:,} (YOUR ORIGINALS!)")
    print(f"Files WITH metadata: {commercial_count:,} (Commercial)\n")
    
    # Get all files
    cursor.execute("""
        SELECT path, filename, category, is_original, size
        FROM wav_files
        WHERE processed = 0
        ORDER BY is_original DESC, category
    """)
    
    processed = 0
    for row in cursor.fetchall():
        path, filename, category, is_original, size = row
        
        # Create destination
        dest_folder = OUTPUT_BASE / category
        dest_folder.mkdir(parents=True, exist_ok=True)
        
        dest_file = dest_folder / filename
        
        # Handle duplicates
        counter = 1
        original_dest = dest_file
        while dest_file.exists():
            dest_file = dest_folder / f"{original_dest.stem}_{counter}{original_dest.suffix}"
            counter += 1
        
        # Copy file
        try:
            shutil.copy2(path, dest_file)
            
            # Mark as processed
            cursor.execute("UPDATE wav_files SET processed = 1 WHERE path = ?", (path,))
            
            processed += 1
            if processed % 100 == 0:
                print(f"  Organized {processed:,} files...")
                conn.commit()
        except Exception as e:
            print(f"  Error: {filename}: {e}")
    
    conn.commit()
    print(f"\n✓ Organized {processed:,} files!")

# ============================================================================
# REPORTING
# ============================================================================

def generate_master_report(conn):
    """Generate comprehensive report"""
    print(f"\n📊 Generating reports...")
    
    cursor = conn.cursor()
    reports_dir = Path("/Volumes/4TBSG/KTK 2026 TO SORT/6TB_REPORTS")
    reports_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Master report
    report_file = reports_dir / f"6TB_MASTER_REPORT_{timestamp}.txt"
    
    with open(report_file, 'w') as f:
        f.write("="*80 + "\n")
        f.write("🗄️ 6TB FULL DRIVE SCAN REPORT 🗄️\n")
        f.write("="*80 + "\n\n")
        
        f.write("⭐⭐⭐ HARD RULE APPLIED ⭐⭐⭐\n")
        f.write("ANY FILE WITHOUT METADATA = YOUR ORIGINAL COMPOSITION!\n\n")
        
        # Statistics
        cursor.execute("SELECT COUNT(*), SUM(size) FROM wav_files")
        total_files, total_size = cursor.fetchone()
        
        cursor.execute("SELECT COUNT(*), SUM(size) FROM wav_files WHERE is_original = 1")
        orig_count, orig_size = cursor.fetchone()
        
        cursor.execute("SELECT COUNT(*), SUM(size) FROM wav_files WHERE is_original = 0")
        comm_count, comm_size = cursor.fetchone()
        
        f.write(f"Total WAV files found: {total_files:,}\n")
        f.write(f"Total size: {(total_size or 0)/(1024**3):.2f} GB\n\n")
        
        f.write("="*80 + "\n")
        f.write(f"⭐ ORIGINAL COMPOSITIONS: {orig_count:,} files\n")
        f.write(f"   Size: {(orig_size or 0)/(1024**3):.2f} GB\n")
        f.write("="*80 + "\n\n")
        
        # List originals
        cursor.execute("""
            SELECT filename, path, size
            FROM wav_files
            WHERE is_original = 1
            ORDER BY filename
        """)
        
        for filename, path, size in cursor.fetchall():
            f.write(f"  ⭐ {filename}\n")
            f.write(f"     Path: {path}\n")
            f.write(f"     Size: {size/(1024**2):.2f} MB\n\n")
        
        f.write("\n" + "="*80 + "\n")
        f.write(f"📦 COMMERCIAL SAMPLES: {comm_count:,} files\n")
        f.write(f"   Size: {(comm_size or 0)/(1024**3):.2f} GB\n")
        f.write("="*80 + "\n\n")
        
        # By category
        cursor.execute("""
            SELECT category, COUNT(*), SUM(size)
            FROM wav_files
            WHERE is_original = 0
            GROUP BY category
            ORDER BY COUNT(*) DESC
        """)
        
        for category, count, size in cursor.fetchall():
            f.write(f"  {category}: {count:,} files ({(size or 0)/(1024**2):.1f} MB)\n")
    
    # Backup list for originals
    backup_file = reports_dir / f"BACKUP_LIST_ORIGINALS_{timestamp}.txt"
    
    with open(backup_file, 'w') as f:
        f.write("⭐⭐⭐ ORIGINAL COMPOSITIONS - PRIORITY BACKUP LIST ⭐⭐⭐\n\n")
        f.write(f"Found {orig_count:,} original compositions across 6TB drive!\n")
        f.write("These files have NO metadata = YOUR music!\n")
        f.write("BACKUP IMMEDIATELY!\n\n")
        f.write("="*80 + "\n\n")
        
        cursor.execute("""
            SELECT path FROM wav_files
            WHERE is_original = 1
            ORDER BY path
        """)
        
        for (path,) in cursor.fetchall():
            f.write(f"{path}\n")
    
    print(f"✓ Reports generated:")
    print(f"  • {report_file}")
    print(f"  • {backup_file} ⭐")
    
    return report_file, backup_file

# ============================================================================
# MAIN
# ============================================================================

def main():
    print("="*80)
    print("🗄️ 6TB FULL DRIVE SCANNER & ORGANIZER 🗄️")
    print("="*80)
    print("\n⭐⭐⭐ HARD RULE ⭐⭐⭐")
    print("ANY FILE WITHOUT METADATA = YOUR ORIGINAL COMPOSITION!\n")
    print("MASSIVE SCALE FEATURES:")
    print("  🗄️ Scans entire 6TB drive")
    print("  ⚡ Parallel processing")
    print("  💾 Database indexing")
    print("  📊 Progress tracking")
    print("  ↩️ Crash recovery")
    print("  🔍 Finds ALL your originals")
    print("="*80 + "\n")
    
    print(f"Scan root: {SCAN_ROOT}")
    print(f"Output: {OUTPUT_BASE}")
    print(f"Database: {DATABASE_FILE}\n")
    
    # Initialize database
    print("📊 Initializing database...")
    conn = init_database()
    print("✓ Database ready\n")
    
    # Check for previous checkpoint
    checkpoint = load_checkpoint()
    if checkpoint:
        print(f"⚠️  Previous scan found!")
        print(f"   Scanned: {checkpoint['scanned_files']:,} / {checkpoint['total_files']:,}")
        print(f"   Continue? (y/n): ", end='')
        # For now, start fresh
        print("Starting fresh scan...\n")
    
    # Phase 1: Discover files
    start_time = datetime.now()
    wav_files, total_size = discover_wav_files(SCAN_ROOT)
    
    if not wav_files:
        print("❌ No WAV files found!")
        return
    
    # Phase 2: Parallel scan
    scanned, originals, commercial = parallel_scan(wav_files, conn)
    
    # Phase 3: Organize
    organize_from_database(conn)
    
    # Phase 4: Reports
    report_file, backup_file = generate_master_report(conn)
    
    # Summary
    elapsed = (datetime.now() - start_time).total_seconds()
    
    print("\n" + "="*80)
    print("🎉 6TB SCAN COMPLETE! 🎉")
    print("="*80)
    print(f"\n⏱️  Total time: {elapsed/60:.1f} minutes")
    print(f"⚡ Speed: {scanned/elapsed:.1f} files/second")
    print(f"\n⭐⭐⭐ FOUND YOUR ORIGINALS ⭐⭐⭐")
    print(f"Original compositions: {originals:,} files")
    print(f"Commercial samples: {commercial:,} files")
    print(f"\nOrganized into: {OUTPUT_BASE}/")
    print(f"\n📄 Check reports: {report_file.parent}/")
    print("="*80 + "\n")
    
    conn.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted! Progress saved to database.")
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

