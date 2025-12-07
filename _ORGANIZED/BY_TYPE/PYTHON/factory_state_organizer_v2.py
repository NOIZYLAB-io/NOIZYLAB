#!/usr/bin/env python3
"""
🏭 FACTORY STATE ORGANIZER V2.0 - ULTIMATE EDITION
Advanced library organization system with intelligent categorization
Reorganizes sample libraries to professional factory standards
"""

import os
import sys
import json
import shutil
import hashlib
import sqlite3
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import multiprocessing
from typing import Dict, List, Set, Tuple
import re

# ==================== CONFIGURATION ====================

WORKSPACE = Path("/Volumes/4TBSG/KTK 2026 TO SORT")
SFX_WORKSPACE = Path("/Volumes/4TBSG/2026_SFX")
OUTPUT_BASE = Path("/Volumes/4TBSG/FACTORY_ORGANIZED_2026")
DATABASE_PATH = Path("/Volumes/4TBSG/NOIZYLAB/library_master.db")
REPORT_DIR = Path("/Volumes/4TBSG/NOIZYLAB/REPORTS")

# Create output directories
ORGANIZED_DIRS = {
    'drums': OUTPUT_BASE / "01_DRUMS_&_PERCUSSION",
    'orchestral': OUTPUT_BASE / "02_ORCHESTRAL",
    'ethnic': OUTPUT_BASE / "03_ETHNIC_&_WORLD",
    'synths': OUTPUT_BASE / "04_SYNTHS_&_ELECTRONIC",
    'guitars': OUTPUT_BASE / "05_GUITARS_&_BASS",
    'keys': OUTPUT_BASE / "06_KEYS_&_PIANO",
    'brass_winds': OUTPUT_BASE / "07_BRASS_&_WOODWINDS",
    'strings': OUTPUT_BASE / "08_STRINGS",
    'sfx': OUTPUT_BASE / "09_SFX_&_SOUND_DESIGN",
    'vocals': OUTPUT_BASE / "10_VOCALS_&_CHOIR",
    'loops': OUTPUT_BASE / "11_LOOPS_&_CONSTRUCTION_KITS",
    'kontakt_factory': OUTPUT_BASE / "12_KONTAKT_LIBRARIES",
    'presets': OUTPUT_BASE / "13_PRESETS_&_PATCHES",
    'documents': OUTPUT_BASE / "14_DOCUMENTATION",
    'uncategorized': OUTPUT_BASE / "99_UNCATEGORIZED"
}

# ==================== INTELLIGENT CATEGORIZATION ====================

CATEGORY_PATTERNS = {
    'drums': [
        'drum', 'percussion', 'perc', 'kick', 'snare', 'hihat', 'cymbal',
        'tom', 'clap', 'battery', 'groove', 'beat', 'acoustic drum',
        'electric drum', 'drum kit', 'djembe', 'conga', 'bongo',
        'timpani', 'taiko', 'tabla', 'crash', 'ride', 'splash'
    ],
    'orchestral': [
        'orchestra', 'symphonic', 'cinematic', 'epic', 'chamber',
        'philharmonic', 'ensemble', 'scoring', 'film score',
        'hollywood', 'spitfire', 'cinesamples', 'project sam'
    ],
    'ethnic': [
        'ethnic', 'world', 'africa', 'asia', 'india', 'middle east',
        'latin', 'celtic', 'tribal', 'traditional', 'folk',
        'sitar', 'oud', 'koto', 'erhu', 'duduk', 'shakuhachi',
        'worldbeat', 'mediterranean', 'oriental'
    ],
    'synths': [
        'synth', 'analog', 'digital', 'modular', 'massive', 'serum',
        'sylenth', 'omnisphere', 'electro', 'edm', 'trance', 'house',
        'techno', 'dubstep', 'bass music', 'synthesizer',
        'moog', 'arp', 'minimoog', 'prophet'
    ],
    'guitars': [
        'guitar', 'bass', 'acoustic guitar', 'electric guitar',
        'acoustic bass', 'electric bass', 'banjo', 'mandolin',
        'ukulele', 'lute', 'les paul', 'stratocaster', 'telecaster',
        'fingerstyle', 'strum', 'picked'
    ],
    'keys': [
        'piano', 'keyboard', 'keys', 'electric piano', 'rhodes',
        'wurlitzer', 'clavinet', 'organ', 'hammond', 'grand piano',
        'upright', 'felt piano', 'prepared piano', 'toy piano',
        'keyscape', 'alicia keys', 'giant'
    ],
    'brass_winds': [
        'brass', 'trumpet', 'trombone', 'horn', 'tuba', 'sax',
        'saxophone', 'clarinet', 'flute', 'oboe', 'bassoon',
        'french horn', 'brass section', 'wind', 'woodwind',
        'brass ensemble', 'big band'
    ],
    'strings': [
        'strings', 'violin', 'viola', 'cello', 'contrabass', 'double bass',
        'string section', 'string ensemble', 'pizzicato', 'arco',
        'tremolo', 'legato strings', 'staccato strings'
    ],
    'sfx': [
        'sfx', 'sound effect', 'foley', 'ambience', 'atmosphere',
        'transition', 'impact', 'whoosh', 'riser', 'hit',
        'stinger', 'ui', 'ux', 'game audio', 'sci-fi',
        'horror', 'cartoon', 'cinematic fx'
    ],
    'vocals': [
        'vocal', 'voice', 'choir', 'chorus', 'singer', 'ahh', 'ohh',
        'vox', 'acapella', 'harmony', 'soprano', 'alto', 'tenor', 'bass',
        'male voice', 'female voice', 'vocal phrase'
    ],
    'loops': [
        'loop', 'construction kit', 'rex', 'apple loop', 'acidized',
        'tempo', 'bpm', 'groove', 'phrase', 'pattern'
    ]
}

KONTAKT_KEYWORDS = [
    'kontakt', 'nki', 'nkm', 'native instruments', 'ni', 'komplete',
    'library', 'instrument'
]

# File extensions mapping
AUDIO_EXTENSIONS = {'.wav', '.aif', '.aiff', '.mp3', '.flac', '.ogg', '.m4a'}
KONTAKT_INSTRUMENTS = {'.nki', '.nkm', '.nkc', '.nkr'}
KONTAKT_SAMPLES = {'.ncw', '.nkx'}
PRESET_EXTENSIONS = {'.fxp', '.fxb', '.nka', '.nksn', '.vstpreset'}
SAMPLER_EXTENSIONS = {'.exs', '.sxt', '.sfz', '.gig', '.nki'}
DOCUMENT_EXTENSIONS = {'.pdf', '.txt', '.rtf', '.doc', '.docx', '.md'}
DATA_EXTENSIONS = {'.csv', '.json', '.xml', '.yml', '.yaml'}
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tif', '.tiff'}

# ==================== DATABASE MANAGEMENT ====================

class LibraryDatabase:
    """SQLite database for master library index"""
    
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.conn = None
        self.init_database()
    
    def init_database(self):
        """Initialize database schema"""
        self.conn = sqlite3.connect(str(self.db_path))
        cursor = self.conn.cursor()
        
        # Libraries table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS libraries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                category TEXT NOT NULL,
                original_path TEXT,
                new_path TEXT,
                total_files INTEGER DEFAULT 0,
                total_size INTEGER DEFAULT 0,
                has_kontakt BOOLEAN DEFAULT 0,
                has_samples BOOLEAN DEFAULT 0,
                has_presets BOOLEAN DEFAULT 0,
                manufacturer TEXT,
                version TEXT,
                date_organized TIMESTAMP,
                notes TEXT
            )
        """)
        
        # Files table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                library_id INTEGER,
                filename TEXT NOT NULL,
                file_path TEXT NOT NULL,
                file_hash TEXT,
                file_size INTEGER,
                file_type TEXT,
                category TEXT,
                is_duplicate BOOLEAN DEFAULT 0,
                date_indexed TIMESTAMP,
                FOREIGN KEY (library_id) REFERENCES libraries(id)
            )
        """)
        
        # Duplicates table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS duplicates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                file_hash TEXT NOT NULL,
                file_paths TEXT NOT NULL,
                file_count INTEGER,
                wasted_space INTEGER,
                date_detected TIMESTAMP
            )
        """)
        
        # Search index
        cursor.execute("""
            CREATE VIRTUAL TABLE IF NOT EXISTS search_index 
            USING fts5(library_name, filename, category, tags)
        """)
        
        self.conn.commit()
    
    def add_library(self, library_data: dict) -> int:
        """Add library to database"""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT OR REPLACE INTO libraries 
            (name, category, original_path, new_path, total_files, total_size,
             has_kontakt, has_samples, has_presets, manufacturer, date_organized)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            library_data.get('name'),
            library_data.get('category'),
            library_data.get('original_path'),
            library_data.get('new_path'),
            library_data.get('total_files', 0),
            library_data.get('total_size', 0),
            library_data.get('has_kontakt', False),
            library_data.get('has_samples', False),
            library_data.get('has_presets', False),
            library_data.get('manufacturer'),
            datetime.now().isoformat()
        ))
        self.conn.commit()
        return cursor.lastrowid
    
    def add_file(self, file_data: dict):
        """Add file to database"""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO files 
            (library_id, filename, file_path, file_hash, file_size, 
             file_type, category, date_indexed)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            file_data.get('library_id'),
            file_data.get('filename'),
            file_data.get('file_path'),
            file_data.get('file_hash'),
            file_data.get('file_size'),
            file_data.get('file_type'),
            file_data.get('category'),
            datetime.now().isoformat()
        ))
        self.conn.commit()
    
    def add_duplicate(self, hash_val: str, paths: List[str], wasted_space: int):
        """Log duplicate files"""
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO duplicates 
            (file_hash, file_paths, file_count, wasted_space, date_detected)
            VALUES (?, ?, ?, ?, ?)
        """, (
            hash_val,
            json.dumps(paths),
            len(paths),
            wasted_space,
            datetime.now().isoformat()
        ))
        self.conn.commit()
    
    def search_libraries(self, query: str) -> List[dict]:
        """Search libraries by name or category"""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT * FROM libraries 
            WHERE name LIKE ? OR category LIKE ? OR manufacturer LIKE ?
        """, (f'%{query}%', f'%{query}%', f'%{query}%'))
        
        results = []
        for row in cursor.fetchall():
            results.append(dict(zip([d[0] for d in cursor.description], row)))
        return results
    
    def get_stats(self) -> dict:
        """Get database statistics"""
        cursor = self.conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM libraries")
        total_libraries = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM files")
        total_files = cursor.fetchone()[0]
        
        cursor.execute("SELECT SUM(total_size) FROM libraries")
        total_size = cursor.fetchone()[0] or 0
        
        cursor.execute("SELECT COUNT(*) FROM duplicates")
        duplicate_groups = cursor.fetchone()[0]
        
        cursor.execute("SELECT SUM(wasted_space) FROM duplicates")
        wasted_space = cursor.fetchone()[0] or 0
        
        return {
            'total_libraries': total_libraries,
            'total_files': total_files,
            'total_size': total_size,
            'duplicate_groups': duplicate_groups,
            'wasted_space': wasted_space
        }
    
    def close(self):
        """Close database connection"""
        if self.conn:
            self.conn.close()

# ==================== INTELLIGENT CATEGORIZER ====================

class IntelligentCategorizer:
    """AI-like categorization using pattern matching"""
    
    @staticmethod
    def categorize_library(library_name: str, library_path: str = None) -> str:
        """Determine library category based on name and contents"""
        library_lower = library_name.lower()
        
        # Score each category
        scores = defaultdict(int)
        
        for category, patterns in CATEGORY_PATTERNS.items():
            for pattern in patterns:
                if pattern.lower() in library_lower:
                    scores[category] += 1
        
        # Check for Kontakt-specific libraries
        if any(kw in library_lower for kw in KONTAKT_KEYWORDS):
            scores['kontakt_factory'] += 2
        
        # If we have a path, check directory structure
        if library_path:
            path_lower = str(library_path).lower()
            for category, patterns in CATEGORY_PATTERNS.items():
                for pattern in patterns:
                    if pattern.lower() in path_lower:
                        scores[category] += 0.5
        
        # Return highest scoring category or uncategorized
        if scores:
            return max(scores.items(), key=lambda x: x[1])[0]
        return 'uncategorized'
    
    @staticmethod
    def detect_manufacturer(library_name: str) -> str:
        """Detect library manufacturer"""
        manufacturers = {
            'Native Instruments': ['ni', 'native instruments', 'komplete', 'kontakt'],
            'Spitfire Audio': ['spitfire', 'albion', 'bbc', 'chamber'],
            'Output': ['output', 'arcade', 'exhale', 'signal'],
            'Heavyocity': ['heavyocity', 'damage', 'master sessions'],
            'CineSamples': ['cinesamples', 'cinebrass', 'cinewinds', 'cinestrings'],
            'ProjectSAM': ['project sam', 'symphobia', 'true strike'],
            'EastWest': ['eastwest', 'ew', 'hollywood', 'quantum leap'],
            'Toontrack': ['toontrack', 'superior drummer', 'ezdrummer', 'sd3'],
            'Big Fish Audio': ['big fish', 'bfa'],
            'Loopmasters': ['loopmasters'],
            'Sample Logic': ['sample logic', 'samplelogic', 'cinemorphx'],
            'Soundiron': ['soundiron'],
            'Audio Imperia': ['audio imperia', 'nucleus'],
            'Embertone': ['embertone']
        }
        
        library_lower = library_name.lower()
        for manufacturer, keywords in manufacturers.items():
            if any(kw in library_lower for kw in keywords):
                return manufacturer
        
        return 'Unknown'

# ==================== FILE OPERATIONS ====================

class FileOrganizer:
    """Handles file operations and organization"""
    
    def __init__(self, dry_run=False):
        self.dry_run = dry_run
        self.stats = {
            'libraries_processed': 0,
            'files_moved': 0,
            'duplicates_removed': 0,
            'space_saved': 0,
            'errors': []
        }
        self.categorizer = IntelligentCategorizer()
        self.db = LibraryDatabase(DATABASE_PATH)
        self.file_hashes = {}
    
    def quick_hash(self, filepath: Path, sample_size=8192) -> str:
        """Fast file hash for duplicate detection"""
        try:
            file_size = filepath.stat().st_size
            if file_size == 0:
                return None
            
            hasher = hashlib.md5()
            
            with open(filepath, 'rb') as f:
                # First chunk
                hasher.update(f.read(sample_size))
                
                # Last chunk if file is large
                if file_size > sample_size * 2:
                    f.seek(-sample_size, 2)
                    hasher.update(f.read(sample_size))
                
                hasher.update(str(file_size).encode())
            
            return hasher.hexdigest()
        except Exception as e:
            return None
    
    def analyze_library(self, library_path: Path) -> dict:
        """Analyze a library directory"""
        library_name = library_path.name
        category = self.categorizer.categorize_library(library_name, str(library_path))
        manufacturer = self.categorizer.detect_manufacturer(library_name)
        
        total_files = 0
        total_size = 0
        has_kontakt = False
        has_samples = False
        has_presets = False
        
        try:
            for root, dirs, files in os.walk(library_path):
                for file in files:
                    if file.startswith('.'):
                        continue
                    
                    filepath = Path(root) / file
                    try:
                        size = filepath.stat().st_size
                        total_size += size
                        total_files += 1
                        
                        ext = filepath.suffix.lower()
                        if ext in KONTAKT_INSTRUMENTS:
                            has_kontakt = True
                        if ext in AUDIO_EXTENSIONS or ext in KONTAKT_SAMPLES:
                            has_samples = True
                        if ext in PRESET_EXTENSIONS:
                            has_presets = True
                    except:
                        continue
        except Exception as e:
            self.stats['errors'].append(f"Error analyzing {library_name}: {e}")
        
        return {
            'name': library_name,
            'category': category,
            'original_path': str(library_path),
            'total_files': total_files,
            'total_size': total_size,
            'has_kontakt': has_kontakt,
            'has_samples': has_samples,
            'has_presets': has_presets,
            'manufacturer': manufacturer
        }
    
    def organize_library(self, library_path: Path, library_data: dict):
        """Organize a single library"""
        category = library_data['category']
        target_base = ORGANIZED_DIRS.get(category, ORGANIZED_DIRS['uncategorized'])
        
        manufacturer = library_data['manufacturer']
        if manufacturer != 'Unknown':
            target_base = target_base / manufacturer
        
        # Clean library name for filesystem
        clean_name = re.sub(r'[^\w\s-]', '', library_data['name'])
        clean_name = re.sub(r'[-\s]+', '_', clean_name)
        
        target_path = target_base / clean_name
        
        if self.dry_run:
            print(f"[DRY RUN] Would move: {library_path} -> {target_path}")
            library_data['new_path'] = str(target_path)
        else:
            try:
                target_path.parent.mkdir(parents=True, exist_ok=True)
                
                if target_path.exists():
                    # Handle existing directory
                    target_path = target_base / f"{clean_name}_{int(datetime.now().timestamp())}"
                
                shutil.move(str(library_path), str(target_path))
                library_data['new_path'] = str(target_path)
                self.stats['files_moved'] += library_data['total_files']
                print(f"✓ Moved: {library_data['name']} -> {category}/{manufacturer}")
            except Exception as e:
                self.stats['errors'].append(f"Error moving {library_data['name']}: {e}")
                print(f"✗ Error: {library_data['name']}: {e}")
                return
        
        # Add to database
        library_id = self.db.add_library(library_data)
        self.stats['libraries_processed'] += 1
    
    def process_workspace(self, workspace: Path):
        """Process entire workspace"""
        print(f"\n🔍 Scanning workspace: {workspace}")
        
        # Get all top-level directories
        libraries = [d for d in workspace.iterdir() 
                    if d.is_dir() and not d.name.startswith('.') 
                    and d.name not in ['Organized_Libraries', 'DOCUMENT_FILES']]
        
        print(f"📊 Found {len(libraries)} libraries to organize\n")
        
        # Process each library
        for i, library_path in enumerate(libraries, 1):
            print(f"[{i}/{len(libraries)}] Processing: {library_path.name}")
            
            # Analyze library
            library_data = self.analyze_library(library_path)
            
            # Organize library
            self.organize_library(library_path, library_data)
            
            # Progress update
            if i % 10 == 0:
                print(f"\n📈 Progress: {i}/{len(libraries)} libraries processed\n")
    
    def generate_report(self):
        """Generate final organization report"""
        REPORT_DIR.mkdir(parents=True, exist_ok=True)
        
        report_file = REPORT_DIR / f"organization_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        db_stats = self.db.get_stats()
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'dry_run': self.dry_run,
            'statistics': {
                'libraries_processed': self.stats['libraries_processed'],
                'files_moved': self.stats['files_moved'],
                'duplicates_removed': self.stats['duplicates_removed'],
                'space_saved_bytes': self.stats['space_saved'],
                'space_saved_human': self.format_size(self.stats['space_saved']),
                'errors': len(self.stats['errors'])
            },
            'database_stats': db_stats,
            'errors': self.stats['errors'][:100]  # Limit errors in report
        }
        
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n📄 Report saved: {report_file}")
        return report
    
    @staticmethod
    def format_size(bytes_size):
        """Format bytes to human readable"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_size < 1024.0:
                return f"{bytes_size:.2f} {unit}"
            bytes_size /= 1024.0
        return f"{bytes_size:.2f} PB"
    
    def print_summary(self):
        """Print organization summary"""
        print("\n" + "="*80)
        print("🏭 FACTORY STATE ORGANIZATION SUMMARY")
        print("="*80)
        
        print(f"\n✓ Libraries Processed: {self.stats['libraries_processed']:,}")
        print(f"✓ Files Moved: {self.stats['files_moved']:,}")
        print(f"✓ Duplicates Removed: {self.stats['duplicates_removed']:,}")
        print(f"✓ Space Saved: {self.format_size(self.stats['space_saved'])}")
        
        if self.stats['errors']:
            print(f"\n⚠️  Errors: {len(self.stats['errors'])}")
        
        db_stats = self.db.get_stats()
        print(f"\n📊 DATABASE STATS:")
        print(f"   Total Libraries: {db_stats['total_libraries']:,}")
        print(f"   Total Files Indexed: {db_stats['total_files']:,}")
        print(f"   Total Size: {self.format_size(db_stats['total_size'])}")
        print(f"   Duplicate Groups: {db_stats['duplicate_groups']:,}")
        print(f"   Wasted Space: {self.format_size(db_stats['wasted_space'])}")
        
        print("\n" + "="*80)
    
    def close(self):
        """Cleanup"""
        self.db.close()

# ==================== MAIN EXECUTION ====================

def main():
    """Main execution"""
    print("\n" + "🏭" * 40)
    print("  FACTORY STATE ORGANIZER V2.0 - ULTIMATE EDITION")
    print("  Intelligent Library Organization System")
    print("🏭" * 40 + "\n")
    
    # Parse arguments
    dry_run = '--execute' not in sys.argv
    
    if dry_run:
        print("🔍 DRY RUN MODE - No files will be moved")
        print("   Add --execute flag to perform actual organization\n")
    else:
        print("⚠️  EXECUTION MODE - Files will be moved!")
        print("   Press Ctrl+C within 5 seconds to cancel...")
        import time
        try:
            for i in range(5, 0, -1):
                print(f"   Starting in {i}...", end='\r')
                time.sleep(1)
            print("\n")
        except KeyboardInterrupt:
            print("\n\n❌ Cancelled by user")
            sys.exit(0)
    
    # Create output directories
    for dir_path in ORGANIZED_DIRS.values():
        dir_path.mkdir(parents=True, exist_ok=True)
    
    # Initialize organizer
    organizer = FileOrganizer(dry_run=dry_run)
    
    try:
        # Process KTK workspace
        if WORKSPACE.exists():
            print(f"\n📦 Processing: {WORKSPACE.name}")
            organizer.process_workspace(WORKSPACE)
        
        # Process SFX workspace
        if SFX_WORKSPACE.exists():
            print(f"\n🔊 Processing: {SFX_WORKSPACE.name}")
            organizer.process_workspace(SFX_WORKSPACE)
        
        # Generate reports
        organizer.generate_report()
        organizer.print_summary()
        
        print("\n✅ ORGANIZATION COMPLETE!")
        print(f"\n📁 Organized libraries location: {OUTPUT_BASE}")
        print(f"📊 Database location: {DATABASE_PATH}")
        print(f"📄 Reports location: {REPORT_DIR}")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Critical error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        organizer.close()

if __name__ == "__main__":
    main()

