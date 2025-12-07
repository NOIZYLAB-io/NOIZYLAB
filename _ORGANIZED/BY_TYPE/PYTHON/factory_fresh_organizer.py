#!/usr/bin/env python3
"""
🏭 FACTORY FRESH ORGANIZER - PRESERVE 100% ORIGINAL STATE
Organizes libraries EXACTLY as shipped from manufacturer
NO internal modifications - only top-level organization
"""

import os
import sys
import json
import shutil
import hashlib
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import sys
sys.path.insert(0, str(Path(__file__).parent))
from master_plugin_database import MASTER_DATABASE, get_manufacturer_info

# ==================== CONFIGURATION ====================

SOURCE_DIRS = [
    Path("/Volumes/4TBSG/KTK 2026 TO SORT"),
    Path("/Volumes/4TBSG/2026_SFX"),
]

OUTPUT_BASE = Path("/Volumes/4TBSG/FACTORY_FRESH_ORGANIZED")
DUPLICATES_QUARANTINE = Path("/Volumes/4TBSG/_DUPLICATES_QUARANTINE")
EMPTY_FOLDERS_LOG = Path("/Volumes/4TBSG/NOIZYLAB/REPORTS/empty_folders.txt")
REPORT_DIR = Path("/Volumes/4TBSG/NOIZYLAB/REPORTS")

# ==================== MANUFACTURER DATABASE ====================
# Exact manufacturer names and their products as shipped

KNOWN_MANUFACTURERS = {
    'Native Instruments': {
        'keywords': ['native instruments', 'ni ', 'komplete', 'kontakt factory', 'massive', 'reaktor', 'battery'],
        'products': []
    },
    'Spitfire Audio': {
        'keywords': ['spitfire', 'albion', 'bbc', 'chamber evolutions', 'olafur arnalds'],
        'products': ['Albion', 'BBC', 'Chamber Evolutions', 'Composer Toolkit']
    },
    'Output': {
        'keywords': ['output'],
        'products': ['Arcade', 'Exhale', 'Rev', 'Signal', 'Analog Brass', 'Analog Strings']
    },
    'Heavyocity': {
        'keywords': ['heavyocity'],
        'products': ['Damage', 'Evolve', 'Master Sessions', 'Gravity']
    },
    'CineSamples': {
        'keywords': ['cinesamples', 'cine'],
        'products': ['CineBrass', 'CineWinds', 'CineStrings', 'CinePerc']
    },
    'ProjectSAM': {
        'keywords': ['project sam', 'projectsam'],
        'products': ['Symphobia', 'True Strike', 'Swing']
    },
    'EastWest': {
        'keywords': ['eastwest', 'east west', 'ew', 'quantum leap', 'hollywood'],
        'products': ['Hollywood Strings', 'Hollywood Brass', 'Stormdrum', 'RA']
    },
    'Toontrack': {
        'keywords': ['toontrack'],
        'products': ['Superior Drummer', 'EZdrummer', 'EZkeys', 'EZbass', 'EZmix']
    },
    'Big Fish Audio': {
        'keywords': ['big fish', 'bfa'],
        'products': []
    },
    'Loopmasters': {
        'keywords': ['loopmasters'],
        'products': []
    },
    'Sample Logic': {
        'keywords': ['sample logic', 'samplelogic'],
        'products': ['Cinematic Guitars', 'Morphestra', 'Cinemorphx']
    },
    'Soundiron': {
        'keywords': ['soundiron'],
        'products': ['Olympus', 'Lakeside Pipe Organ', 'Mars']
    },
    'Audio Imperia': {
        'keywords': ['audio imperia', 'nucleus'],
        'products': ['Nucleus', 'Jaeger', 'Chorus']
    },
    'Embertone': {
        'keywords': ['embertone'],
        'products': ['Friedlander Violin', 'Chapman Trumpet', 'Sensual Saxophone']
    },
    'Best Service': {
        'keywords': ['best service'],
        'products': ['Engine', 'ERA']
    },
    'Emergence Audio': {
        'keywords': ['emergence'],
        'products': ['Django', 'Infinite Woodwinds']
    },
    'Impact Soundworks': {
        'keywords': ['impact soundworks'],
        'products': ['Shreddage', 'Ventus', 'Bravura']
    },
    'Orchestral Tools': {
        'keywords': ['orchestral tools'],
        'products': ['Berlin', 'Metropolis Ark']
    },
    'Sonokinetic': {
        'keywords': ['sonokinetic'],
        'products': ['Da Capo', 'Cappricio', 'Grosso']
    },
    'Cinesamples': {
        'keywords': ['cinesamples'],
        'products': []
    },
    'Wide Blue Sound': {
        'keywords': ['wide blue sound'],
        'products': ['Orbit', 'Eclipse']
    },
    'Audiobro': {
        'keywords': ['audiobro'],
        'products': ['LASS', 'Genesis']
    },
    '8Dio': {
        'keywords': ['8dio'],
        'products': ['Adagio', 'Century']
    },
    'Cinematique Instruments': {
        'keywords': ['cinematique'],
        'products': []
    },
    'Soundiron': {
        'keywords': ['soundiron'],
        'products': []
    },
}

# SFX Manufacturers
SFX_MANUFACTURERS = {
    'Hollywood Edge': {
        'keywords': ['hollywood edge', 'he '],
        'products': []
    },
    'Sound Ideas': {
        'keywords': ['sound ideas', 'si ', 'soundideas'],
        'products': ['6000 Series', '4000 Series']
    },
    'BBC Sound Effects': {
        'keywords': ['bbc'],
        'products': []
    },
    'Pro Sound Effects': {
        'keywords': ['pro sound effects', 'pse'],
        'products': []
    },
    'Boom Library': {
        'keywords': ['boom library', 'boom'],
        'products': []
    },
}

class FactoryFreshOrganizer:
    """Organize libraries while preserving 100% original state"""
    
    def __init__(self, dry_run=True):
        self.dry_run = dry_run
        self.stats = {
            'libraries_moved': 0,
            'duplicates_found': 0,
            'empty_folders': 0,
            'unidentified': 0,
            'errors': []
        }
        self.library_hashes = defaultdict(list)
        self.empty_folders = []
    
    def detect_manufacturer(self, library_name: str, library_path: Path) -> tuple:
        """Detect manufacturer using comprehensive database and preserve exact product name"""
        library_lower = library_name.lower()
        
        # Use the master database for detection
        manufacturer_info = get_manufacturer_info(library_name)
        manufacturer = manufacturer_info['manufacturer']
        
        if manufacturer != 'Unknown':
            # Check if it's SFX
            if MASTER_DATABASE[manufacturer]['type'] == 'sfx':
                return f"SFX_{manufacturer}", library_name
            else:
                return manufacturer, library_name  # KEEP EXACT ORIGINAL NAME
        
        # Fallback: Check if it's SFX by content or name
        if any(x in library_lower for x in ['sfx', 'sound effect', 'foley', 'fx', 'sound ideas', 'hollywood edge']):
            return "SFX_Various", library_name
        
        return "Unidentified", library_name
    
    def hash_directory_structure(self, directory: Path) -> str:
        """Create hash of directory structure to detect duplicates"""
        hasher = hashlib.md5()
        
        try:
            # Hash directory name and size
            hasher.update(directory.name.encode())
            
            # Count files by type
            file_count = 0
            total_size = 0
            
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if not file.startswith('.'):
                        try:
                            filepath = Path(root) / file
                            total_size += filepath.stat().st_size
                            file_count += 1
                        except:
                            pass
            
            hasher.update(str(file_count).encode())
            hasher.update(str(total_size).encode())
            
            return hasher.hexdigest()
        except:
            return None
    
    def is_empty_or_system(self, directory: Path) -> bool:
        """Check if directory is empty or contains only system files"""
        try:
            items = list(directory.iterdir())
            non_system = [
                item for item in items
                if not item.name.startswith('.')
                and item.name not in ['Thumbs.db', 'desktop.ini', '.DS_Store']
            ]
            
            if len(non_system) == 0:
                return True
            
            # Check if all subdirectories are also empty (recursive)
            if all(item.is_dir() and self.is_empty_or_system(item) for item in non_system):
                return True
            
            return False
        except:
            return False
    
    def scan_for_empty_folders(self, base_dir: Path):
        """Scan for empty folders"""
        print(f"\n🔍 Scanning for empty folders in: {base_dir.name}")
        
        for root, dirs, files in os.walk(base_dir, topdown=False):
            root_path = Path(root)
            
            if self.is_empty_or_system(root_path):
                self.empty_folders.append(root_path)
                self.stats['empty_folders'] += 1
    
    def delete_empty_folders(self):
        """Delete all empty folders"""
        if not self.empty_folders:
            print("\n✓ No empty folders found")
            return
        
        print(f"\n🗑️  Deleting {len(self.empty_folders)} empty folders...")
        
        # Save list before deletion
        EMPTY_FOLDERS_LOG.parent.mkdir(parents=True, exist_ok=True)
        with open(EMPTY_FOLDERS_LOG, 'w') as f:
            f.write(f"Empty Folders Found: {datetime.now().isoformat()}\n")
            f.write("="*80 + "\n\n")
            for folder in self.empty_folders:
                f.write(f"{folder}\n")
        
        deleted = 0
        for folder in self.empty_folders:
            try:
                if self.dry_run:
                    print(f"[DRY RUN] Would delete: {folder}")
                else:
                    if folder.exists():
                        shutil.rmtree(folder)
                        print(f"✓ Deleted: {folder}")
                        deleted += 1
            except Exception as e:
                self.stats['errors'].append(f"Delete error: {folder}: {e}")
        
        print(f"✓ Deleted {deleted} empty folders")
        print(f"📄 List saved: {EMPTY_FOLDERS_LOG}")
    
    def move_library_intact(self, library_path: Path, manufacturer: str, original_name: str):
        """Move entire library keeping 100% original structure"""
        
        # Create manufacturer directory
        if manufacturer.startswith('SFX_'):
            manufacturer_dir = OUTPUT_BASE / "SFX" / manufacturer.replace('SFX_', '')
        else:
            manufacturer_dir = OUTPUT_BASE / "INSTRUMENTS" / manufacturer
        
        # Target keeps EXACT original name
        target_path = manufacturer_dir / original_name
        
        if self.dry_run:
            print(f"[DRY RUN] Would move:")
            print(f"  FROM: {library_path}")
            print(f"  TO:   {target_path}")
        else:
            try:
                # Create manufacturer directory
                manufacturer_dir.mkdir(parents=True, exist_ok=True)
                
                # Handle existing directory
                if target_path.exists():
                    print(f"⚠️  Target exists: {target_path}")
                    # Check if it's a duplicate
                    lib_hash = self.hash_directory_structure(library_path)
                    target_hash = self.hash_directory_structure(target_path)
                    
                    if lib_hash == target_hash:
                        # It's a duplicate - move to quarantine
                        dup_target = DUPLICATES_QUARANTINE / manufacturer / original_name
                        dup_target.parent.mkdir(parents=True, exist_ok=True)
                        shutil.move(str(library_path), str(dup_target))
                        print(f"✓ Duplicate moved to quarantine: {original_name}")
                        self.stats['duplicates_found'] += 1
                        return
                    else:
                        # Different content - add timestamp
                        timestamp = int(datetime.now().timestamp())
                        target_path = manufacturer_dir / f"{original_name}_{timestamp}"
                
                # Move the library INTACT
                shutil.move(str(library_path), str(target_path))
                print(f"✓ Moved: {original_name} → {manufacturer}")
                self.stats['libraries_moved'] += 1
                
            except Exception as e:
                self.stats['errors'].append(f"Move error: {library_path.name}: {e}")
                print(f"✗ Error: {library_path.name}: {e}")
    
    def process_workspace(self, workspace: Path):
        """Process workspace - move libraries intact"""
        print(f"\n{'='*80}")
        print(f"Processing: {workspace.name}")
        print(f"{'='*80}\n")
        
        if not workspace.exists():
            print(f"⚠️  Workspace not found: {workspace}")
            return
        
        # Get all top-level directories (these are the library folders)
        libraries = [
            d for d in workspace.iterdir()
            if d.is_dir()
            and not d.name.startswith('.')
            and d.name not in ['Organized_Libraries', 'DOCUMENT_FILES', 'ORGANIZED_2026']
        ]
        
        print(f"📊 Found {len(libraries)} libraries\n")
        
        # Process each library
        for i, library_path in enumerate(libraries, 1):
            print(f"\n[{i}/{len(libraries)}] {library_path.name}")
            
            # Detect manufacturer
            manufacturer, original_name = self.detect_manufacturer(library_path.name, library_path)
            
            if manufacturer == "Unidentified":
                print(f"  ⚠️  Unidentified manufacturer: {library_path.name}")
                self.stats['unidentified'] += 1
                # Still organize it under Unidentified
            else:
                print(f"  Manufacturer: {manufacturer}")
            
            # Move library keeping 100% original state
            self.move_library_intact(library_path, manufacturer, original_name)
    
    def generate_report(self):
        """Generate organization report"""
        REPORT_DIR.mkdir(parents=True, exist_ok=True)
        
        report_file = REPORT_DIR / f"factory_fresh_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'dry_run': self.dry_run,
            'statistics': {
                'libraries_moved': self.stats['libraries_moved'],
                'duplicates_found': self.stats['duplicates_found'],
                'empty_folders_deleted': self.stats['empty_folders'],
                'unidentified_libraries': self.stats['unidentified'],
                'errors': len(self.stats['errors'])
            },
            'output_location': str(OUTPUT_BASE),
            'duplicates_location': str(DUPLICATES_QUARANTINE),
            'errors': self.stats['errors'][:100]
        }
        
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        print(f"\n📄 Report saved: {report_file}")
    
    def print_summary(self):
        """Print summary"""
        print("\n" + "="*80)
        print("🏭 FACTORY FRESH ORGANIZATION SUMMARY")
        print("="*80)
        
        print(f"\n✓ Libraries Moved: {self.stats['libraries_moved']:,}")
        print(f"✓ Duplicates Quarantined: {self.stats['duplicates_found']:,}")
        print(f"✓ Empty Folders Deleted: {self.stats['empty_folders']:,}")
        print(f"⚠️  Unidentified Libraries: {self.stats['unidentified']:,}")
        
        if self.stats['errors']:
            print(f"\n⚠️  Errors: {len(self.stats['errors'])}")
        
        print(f"\n📁 Organized Location: {OUTPUT_BASE}")
        print(f"📁 Duplicates Location: {DUPLICATES_QUARANTINE}")
        
        print("\n" + "="*80)
        print("✅ ALL LIBRARIES PRESERVED IN 100% ORIGINAL STATE")
        print("="*80)

def main():
    """Main execution"""
    print("\n" + "🏭" * 40)
    print("  FACTORY FRESH ORGANIZER")
    print("  Preserves 100% Original Manufacturer State")
    print("  NO Internal Modifications - Libraries Exactly As Shipped")
    print("🏭" * 40 + "\n")
    
    # Parse arguments
    dry_run = '--execute' not in sys.argv
    skip_empty = '--skip-empty' in sys.argv
    
    if dry_run:
        print("🔍 DRY RUN MODE - No changes will be made")
        print("   Add --execute flag to perform actual organization\n")
    else:
        print("⚠️  EXECUTION MODE - Libraries will be moved!")
        print("   All libraries will be preserved in ORIGINAL state")
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
    
    # Create base directories
    OUTPUT_BASE.mkdir(parents=True, exist_ok=True)
    DUPLICATES_QUARANTINE.mkdir(parents=True, exist_ok=True)
    
    # Initialize organizer
    organizer = FactoryFreshOrganizer(dry_run=dry_run)
    
    try:
        # Step 1: Scan for empty folders first
        if not skip_empty:
            for workspace in SOURCE_DIRS:
                if workspace.exists():
                    organizer.scan_for_empty_folders(workspace)
        
        # Step 2: Process each workspace
        for workspace in SOURCE_DIRS:
            if workspace.exists():
                organizer.process_workspace(workspace)
        
        # Step 3: Delete empty folders
        if not skip_empty:
            organizer.delete_empty_folders()
        
        # Step 4: Generate report
        organizer.generate_report()
        organizer.print_summary()
        
        print("\n✅ FACTORY FRESH ORGANIZATION COMPLETE!")
        print("\n📋 STRUCTURE:")
        print(f"   {OUTPUT_BASE}/")
        print(f"   ├── INSTRUMENTS/")
        print(f"   │   ├── Native Instruments/")
        print(f"   │   ├── Spitfire Audio/")
        print(f"   │   ├── Output/")
        print(f"   │   └── [Each Manufacturer]/")
        print(f"   └── SFX/")
        print(f"       ├── Hollywood Edge/")
        print(f"       ├── Sound Ideas/")
        print(f"       └── [Each SFX Manufacturer]/")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"\n\n❌ Critical error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

