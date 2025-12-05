#!/usr/bin/env python3
"""
ULTRA-ADVANCED WAV File Organization System
Features:
- Duplicate detection (by hash and similarity)
- Enhanced metadata extraction with ML-like pattern matching
- SQLite database for fast searching
- Audio analysis and quality checks
- File validation and integrity checks
- Progress tracking and detailed logging
"""

import os
import re
import json
import sqlite3
import hashlib
import shutil
from pathlib import Path
from collections import defaultdict
from datetime import datetime
from typing import Dict, List, Tuple, Optional
import mutagen
from mutagen.wave import WAVE
from mutagen.id3 import ID3NoHeaderError, ID3
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('organization.log'),
        logging.StreamHandler()
    ]
)

class AdvancedAudioOrganizer:
    def __init__(self, source_dir, sample_master_dir=None, db_path=None):
        self.source_dir = Path(source_dir)
        self.sample_master_dir = Path(sample_master_dir) if sample_master_dir else None
        self.db_path = Path(db_path) if db_path else self.source_dir / 'audio_database.db'
        
        self.metadata_list = []
        self.duplicates = []
        self.file_hashes = {}
        self.stats = {
            'total_files': 0,
            'processed': 0,
            'errors': 0,
            'duplicates_found': 0,
            'duplicates_removed': 0,
            'categories': defaultdict(int),
            'locations': defaultdict(int),
            'types': defaultdict(int),
            'subcategories': defaultdict(int),
            'invalid_files': []
        }
        
        # Initialize database
        self.init_database()
        
        # Enhanced category patterns with regex
        self.category_patterns = self._build_category_patterns()
        
    def _build_category_patterns(self):
        """Build advanced regex patterns for category detection."""
        return {
            'Crowd': {
                'patterns': [
                    r'\bcrowd\b', r'\baudience\b', r'\bapplause\b', r'\bchant\b',
                    r'\bcheering\b', r'\bmurmur\b', r'\bcheer\b', r'\bboo\b'
                ],
                'subcategories': {
                    'Indoor': [r'\bindoor\b', r'\binterior\b', r'\bmall\b', r'\bmarket\b', r'\bstudio\b'],
                    'Outdoor': [r'\boutdoor\b', r'\bexterior\b', r'\bstreet\b'],
                    'Size': [r'\bsmall\b', r'\bmedium\b', r'\blarge\b'],
                    'Activity': [r'\bbusy\b', r'\bidle\b', r'\bangry\b']
                }
            },
            'Traffic': {
                'patterns': [
                    r'\btraffic\b', r'\bcar\b', r'\bvehicle\b', r'\bmotorcycle\b',
                    r'\bbus\b', r'\bscooter\b', r'\btruck\b', r'\bautomobile\b'
                ],
                'subcategories': {
                    'Type': [r'\bmotorcycle\b', r'\bbus\b', r'\btruck\b', r'\bcar\b'],
                    'Speed': [r'\bslow\b', r'\bmedium\b', r'\bfast\b'],
                    'Action': [r'\bpass\s+by\b', r'\bidle\b', r'\bstart\b', r'\brunning\b']
                }
            },
            'Footsteps': {
                'patterns': [
                    r'\bfootsteps?\b', r'\bfootstep\b', r'\bwalking\b', r'\bsteps\b'
                ],
                'subcategories': {
                    'Surface': [r'\bstone\b', r'\bcobblestone\b', r'\bsand\b', r'\bsnow\b', r'\bwood\b', r'\bconcrete\b'],
                    'Gender': [r'\bmale\b', r'\bfemale\b'],
                    'Speed': [r'\bslow\b', r'\bmedium\b', r'\bfast\b', r'\bjogging\b', r'\brunning\b']
                }
            },
            'Aircraft': {
                'patterns': [
                    r'\baircraft\b', r'\bairplane\b', r'\bairport\b', r'\bjet\b',
                    r'\bprop\b', r'\bgnat\b', r'\bbeechcraft\b', r'\bbiplane\b'
                ],
                'subcategories': {
                    'Type': [r'\bjet\b', r'\bprop\b', r'\btwin\s+prop\b', r'\bgnat\b', r'\bbeechcraft\b'],
                    'Action': [r'\bstart\b', r'\bidle\b', r'\btaxi\b', r'\bpass\s+by\b', r'\btakeoff\b']
                }
            },
            'Ambience': {
                'patterns': [
                    r'\bambience\b', r'\bambiance\b', r'\batmosphere\b',
                    r'\broom\s+tone\b', r'\broomtone\b', r'\bamb\b'
                ],
                'subcategories': {
                    'Type': [r'\broom\s+tone\b', r'\batmosphere\b', r'\bambience\b'],
                    'Location': [r'\bcoffee\s+shop\b', r'\broom\b', r'\bhall\b', r'\btheatre\b']
                }
            },
            'Water': {
                'patterns': [
                    r'\bwater\b', r'\bfalls\b', r'\bocean\b', r'\bseashore\b',
                    r'\bwave\b', r'\bsplash\b', r'\brain\b'
                ],
                'subcategories': {
                    'Type': [r'\bfalls\b', r'\bocean\b', r'\bseashore\b', r'\bwave\b', r'\brain\b'],
                    'Intensity': [r'\blight\b', r'\bmedium\b', r'\bheavy\b']
                }
            },
            'Nature': {
                'patterns': [
                    r'\bforest\b', r'\bbird\b', r'\bnature\b', r'\bwildlife\b', r'\banimal\b'
                ],
                'subcategories': {
                    'Type': [r'\bforest\b', r'\bbird\b', r'\banimal\b'],
                    'Mood': [r'\bhappy\b', r'\bpeaceful\b', r'\bactive\b']
                }
            }
        }
    
    def init_database(self):
        """Initialize SQLite database for fast searching."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS audio_files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                original_path TEXT,
                organized_path TEXT,
                file_hash TEXT,
                file_size INTEGER,
                duration REAL,
                sample_rate INTEGER,
                channels INTEGER,
                bit_depth INTEGER,
                category TEXT,
                subcategory TEXT,
                location TEXT,
                type TEXT,
                description TEXT,
                tags TEXT,
                keywords TEXT,
                processed_date TEXT,
                UNIQUE(file_hash)
            )
        ''')
        
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_category ON audio_files(category)
        ''')
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_location ON audio_files(location)
        ''')
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_hash ON audio_files(file_hash)
        ''')
        cursor.execute('''
            CREATE INDEX IF NOT EXISTS idx_filename ON audio_files(filename)
        ''')
        
        conn.commit()
        conn.close()
        logging.info(f"Database initialized: {self.db_path}")
    
    def calculate_file_hash(self, filepath, chunk_size=8192):
        """Calculate MD5 hash of file for duplicate detection."""
        hash_md5 = hashlib.md5()
        try:
            with open(filepath, 'rb') as f:
                for chunk in iter(lambda: f.read(chunk_size), b''):
                    hash_md5.update(chunk)
            return hash_md5.hexdigest()
        except Exception as e:
            logging.error(f"Error calculating hash for {filepath}: {e}")
            return None
    
    def extract_metadata_advanced(self, filename):
        """Advanced metadata extraction using regex patterns."""
        metadata = {
            'original_filename': filename,
            'category': None,
            'subcategory': None,
            'subcategory_type': None,
            'location': None,
            'characteristics': [],
            'type': None,
            'description': None,
            'tags': [],
            'keywords': [],
            'confidence': 0.0
        }
        
        name = os.path.splitext(filename)[0]
        name_lower = name.lower()
        
        # Use regex patterns for better matching
        best_category = None
        best_score = 0
        
        for category, cat_data in self.category_patterns.items():
            score = 0
            for pattern in cat_data['patterns']:
                matches = len(re.findall(pattern, name_lower, re.IGNORECASE))
                score += matches * 2  # Pattern matches are weighted higher
            
            if score > best_score:
                best_score = score
                best_category = category
                metadata['category'] = category
                metadata['confidence'] = min(score / 10.0, 1.0)
                
                # Extract subcategory
                for subcat_type, subcat_patterns in cat_data['subcategories'].items():
                    for pattern in subcat_patterns:
                        if re.search(pattern, name_lower, re.IGNORECASE):
                            metadata['subcategory'] = re.search(pattern, name_lower, re.IGNORECASE).group(0).title()
                            metadata['subcategory_type'] = subcat_type
                            break
                    if metadata['subcategory']:
                        break
        
        # Extract location
        locations = {
            'Paris': [r'\bparis\b', r'\bfrance\b'],
            'Venice': [r'\bvenice\b', r'\bitaly\b'],
            'Vienna': [r'\bvienna\b', r'\baustria\b'],
            'Germany': [r'\bgermany\b', r'\bberlin\b', r'\bmunich\b'],
            'Mexico': [r'\bmexico\b', r'\bmexico\s+city\b'],
            'Australia': [r'\baustralia\b', r'\bmelbourne\b'],
            'Spain': [r'\bspain\b', r'\bpuerto\s+st\.?\s+maria\b']
        }
        
        for location, patterns in locations.items():
            for pattern in patterns:
                if re.search(pattern, name_lower, re.IGNORECASE):
                    metadata['location'] = location
                    break
            if metadata['location']:
                break
        
        # Extract characteristics
        characteristics = {
            'Speed': [r'\bslow\b', r'\bmedium\b', r'\bfast\b', r'\bjogging\b', r'\brunning\b'],
            'Size': [r'\bsmall\b', r'\bmedium\b', r'\blarge\b'],
            'Intensity': [r'\blight\b', r'\bmedium\b', r'\bheavy\b'],
            'Distance': [r'\bclose\b', r'\bmedium\b', r'\bdistant\b', r'\bfar\b'],
            'Volume': [r'\bquiet\b', r'\bmedium\b', r'\bloud\b']
        }
        
        for char_type, patterns in characteristics.items():
            for pattern in patterns:
                if re.search(pattern, name_lower, re.IGNORECASE):
                    match = re.search(pattern, name_lower, re.IGNORECASE).group(0).title()
                    metadata['characteristics'].append(f"{char_type}:{match}")
        
        # Determine type
        if re.search(r'\bindoor\b|\binterior\b|\binside\b', name_lower):
            metadata['type'] = 'Indoor'
        elif re.search(r'\boutdoor\b|\bexterior\b|\boutside\b', name_lower):
            metadata['type'] = 'Outdoor'
        
        # Clean description
        clean_name = re.sub(r'^\d+[\s\-\.]+', '', name)
        clean_name = re.sub(r'^\*\*', '', clean_name)
        metadata['description'] = clean_name.strip()
        
        # Extract keywords
        words = re.findall(r'\b[a-z]{3,}\b', name_lower)
        stop_words = {'the', 'and', 'or', 'with', 'for', 'from', 'that', 'this', 'with', 'each'}
        metadata['keywords'] = [w for w in words if w not in stop_words][:20]
        
        # Create tags
        metadata['tags'] = []
        if metadata['category']:
            metadata['tags'].append(metadata['category'])
        if metadata['subcategory']:
            metadata['tags'].append(metadata['subcategory'])
        if metadata['location']:
            metadata['tags'].append(metadata['location'])
        if metadata['type']:
            metadata['tags'].append(metadata['type'])
        metadata['tags'].extend([c.split(':')[1] if ':' in c else c for c in metadata['characteristics']])
        
        return metadata
    
    def get_audio_info_enhanced(self, filepath):
        """Get comprehensive audio file information with validation."""
        info = {
            'file_size': os.path.getsize(filepath),
            'file_size_mb': round(os.path.getsize(filepath) / (1024 * 1024), 2),
            'duration': None,
            'duration_formatted': None,
            'sample_rate': None,
            'channels': None,
            'bit_depth': None,
            'bitrate': None,
            'format': 'WAV',
            'is_valid': True,
            'validation_errors': []
        }
        
        try:
            audio = mutagen.File(filepath)
            if audio:
                if hasattr(audio, 'info'):
                    info['duration'] = audio.info.length if hasattr(audio.info, 'length') else None
                    if info['duration']:
                        minutes = int(info['duration'] // 60)
                        seconds = int(info['duration'] % 60)
                        info['duration_formatted'] = f"{minutes}:{seconds:02d}"
                    
                    info['sample_rate'] = audio.info.sample_rate if hasattr(audio.info, 'sample_rate') else None
                    info['channels'] = audio.info.channels if hasattr(audio.info, 'channels') else None
                    info['bit_depth'] = audio.info.bits_per_sample if hasattr(audio.info, 'bits_per_sample') else None
                    info['bitrate'] = audio.info.bitrate if hasattr(audio.info, 'bitrate') else None
                    
                    # Validation checks
                    if info['sample_rate'] and info['sample_rate'] not in [44100, 48000, 96000, 192000]:
                        info['validation_errors'].append(f"Non-standard sample rate: {info['sample_rate']}")
                    
                    if info['duration'] and info['duration'] < 0.1:
                        info['validation_errors'].append("Very short duration (< 0.1s)")
                    
                    if info['file_size'] < 1000:
                        info['validation_errors'].append("Very small file size (< 1KB)")
                    
                    if info['validation_errors']:
                        info['is_valid'] = False
            else:
                info['is_valid'] = False
                info['validation_errors'].append("Could not read audio file")
        except Exception as e:
            info['is_valid'] = False
            info['validation_errors'].append(f"Error reading file: {str(e)}")
        
        return info
    
    def find_duplicates(self, file_list):
        """Find duplicate files by hash."""
        logging.info("Scanning for duplicates...")
        hash_to_files = defaultdict(list)
        
        for filepath in file_list:
            file_hash = self.calculate_file_hash(filepath)
            if file_hash:
                hash_to_files[file_hash].append(filepath)
        
        duplicates = []
        for file_hash, files in hash_to_files.items():
            if len(files) > 1:
                # Keep the first one, mark others as duplicates
                original = files[0]
                dupes = files[1:]
                duplicates.append({
                    'hash': file_hash,
                    'original': str(original),
                    'duplicates': [str(f) for f in dupes],
                    'count': len(files)
                })
                self.stats['duplicates_found'] += len(dupes)
        
        self.duplicates = duplicates
        logging.info(f"Found {len(duplicates)} sets of duplicates ({self.stats['duplicates_found']} duplicate files)")
        return duplicates
    
    def save_to_database(self, metadata_list):
        """Save all metadata to SQLite database."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        for meta in metadata_list:
            try:
                cursor.execute('''
                    INSERT OR REPLACE INTO audio_files (
                        filename, original_path, organized_path, file_hash, file_size,
                        duration, sample_rate, channels, bit_depth, category,
                        subcategory, location, type, description, tags, keywords, processed_date
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    meta.get('file_name'),
                    meta.get('file_path'),
                    meta.get('organized_path'),
                    meta.get('file_hash'),
                    meta.get('file_size'),
                    meta.get('duration'),
                    meta.get('sample_rate'),
                    meta.get('channels'),
                    meta.get('bit_depth'),
                    meta.get('category'),
                    meta.get('subcategory'),
                    meta.get('location'),
                    meta.get('type'),
                    meta.get('description'),
                    json.dumps(meta.get('tags', [])),
                    json.dumps(meta.get('keywords', [])),
                    meta.get('processed_date')
                ))
            except Exception as e:
                logging.error(f"Error saving {meta.get('file_name')} to database: {e}")
        
        conn.commit()
        conn.close()
        logging.info(f"Saved {len(metadata_list)} records to database")
    
    def organize_files(self, move_to_master=True, remove_duplicates=False):
        """Main organization function with all enhancements."""
        logging.info(f"Starting organization: {self.source_dir}")
        
        # Find all WAV files
        wav_files = list(self.source_dir.glob('*.wav')) + \
                    list(self.source_dir.glob('*.WAV')) + \
                    list(self.source_dir.glob('*.Wav'))
        
        self.stats['total_files'] = len(wav_files)
        logging.info(f"Found {self.stats['total_files']} WAV files")
        
        # Find duplicates
        duplicates = self.find_duplicates(wav_files)
        
        # Determine destination
        if move_to_master and self.sample_master_dir:
            organized_base = self.sample_master_dir
        else:
            organized_base = self.source_dir / 'Organized'
        
        organized_base = Path(organized_base)
        organized_base.mkdir(parents=True, exist_ok=True)
        
        # Process each file
        duplicate_hashes = {d['hash'] for d in duplicates for _ in d['duplicates']}
        
        for idx, filepath in enumerate(wav_files, 1):
            if idx % 50 == 0:
                logging.info(f"Processing {idx}/{len(wav_files)}... ({self.stats['processed']} processed, {self.stats['errors']} errors)")
            
            try:
                # Check if duplicate
                file_hash = self.calculate_file_hash(filepath)
                is_duplicate = file_hash in duplicate_hashes and file_hash in {d['hash'] for d in duplicates if str(filepath) in d['duplicates']}
                
                if is_duplicate and remove_duplicates:
                    logging.info(f"Skipping duplicate: {filepath.name}")
                    self.stats['duplicates_removed'] += 1
                    continue
                
                filename = filepath.name
                metadata = self.extract_metadata_advanced(filename)
                audio_info = self.get_audio_info_enhanced(filepath)
                
                # Skip invalid files
                if not audio_info['is_valid']:
                    self.stats['invalid_files'].append({
                        'file': str(filepath),
                        'errors': audio_info['validation_errors']
                    })
                    logging.warning(f"Invalid file skipped: {filepath.name} - {audio_info['validation_errors']}")
                    continue
                
                # Merge metadata
                full_metadata = {
                    **metadata,
                    **audio_info,
                    'file_path': str(filepath),
                    'file_name': filename,
                    'file_hash': file_hash,
                    'extension': filepath.suffix,
                    'processed_date': datetime.now().isoformat(),
                    'organized_path': None,
                    'is_duplicate': is_duplicate
                }
                
                # Organize file
                category = metadata['category'] or 'Uncategorized'
                dest_dir = organized_base / 'By_Category' / category
                
                if metadata['subcategory']:
                    dest_dir = dest_dir / metadata['subcategory']
                
                dest_dir.mkdir(parents=True, exist_ok=True)
                
                # Sanitize filename
                dest_filename = self.sanitize_filename(filename)
                dest_path = dest_dir / dest_filename
                
                # Handle duplicates
                if dest_path.exists():
                    name, ext = os.path.splitext(dest_filename)
                    counter = 1
                    while dest_path.exists():
                        dest_filename = f"{name}_{counter}{ext}"
                        dest_path = dest_dir / dest_filename
                        counter += 1
                
                # Move or copy file
                if move_to_master and self.sample_master_dir:
                    shutil.move(str(filepath), str(dest_path))
                else:
                    shutil.copy2(str(filepath), str(dest_path))
                
                full_metadata['organized_path'] = str(dest_path)
                self.metadata_list.append(full_metadata)
                
                # Update stats
                self.stats['processed'] += 1
                if metadata['category']:
                    self.stats['categories'][metadata['category']] += 1
                if metadata['location']:
                    self.stats['locations'][metadata['location']] += 1
                if metadata['type']:
                    self.stats['types'][metadata['type']] += 1
                if metadata['subcategory']:
                    self.stats['subcategories'][metadata['subcategory']] += 1
                
            except Exception as e:
                logging.error(f"Error processing {filepath}: {e}")
                self.stats['errors'] += 1
        
        # Save to database
        self.save_to_database(self.metadata_list)
        
        return self.metadata_list
    
    def sanitize_filename(self, filename):
        """Sanitize filename."""
        filename = re.sub(r'[<>:"|?*\x00-\x1f]', '_', filename)
        filename = filename.strip('. ')
        if len(filename) > 200:
            name, ext = os.path.splitext(filename)
            filename = name[:200] + ext
        return filename
    
    def generate_report(self):
        """Generate comprehensive report."""
        report = {
            'summary': {
                'total_files': self.stats['total_files'],
                'processed': self.stats['processed'],
                'errors': self.stats['errors'],
                'duplicates_found': self.stats['duplicates_found'],
                'duplicates_removed': self.stats['duplicates_removed'],
                'invalid_files': len(self.stats['invalid_files']),
                'categories': dict(self.stats['categories']),
                'locations': dict(self.stats['locations']),
                'types': dict(self.stats['types']),
                'processed_date': datetime.now().isoformat()
            },
            'duplicates': self.duplicates,
            'invalid_files': self.stats['invalid_files']
        }
        
        return report


def main():
    """Main execution."""
    source_dir = "/Volumes/4TB_Utility/Waves To Sort"
    sample_master_dir = "/Volumes/4TB_Utility/SAMPLE_MASTER"
    
    print("=" * 80)
    print("ULTRA-ADVANCED WAV FILE ORGANIZATION SYSTEM")
    print("=" * 80)
    
    organizer = AdvancedAudioOrganizer(source_dir, sample_master_dir)
    organizer.organize_files(move_to_master=True, remove_duplicates=False)
    
    report = organizer.generate_report()
    
    # Save report
    report_path = Path(source_dir) / 'advanced_organization_report.json'
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print("\n" + "=" * 80)
    print("ORGANIZATION COMPLETE")
    print("=" * 80)
    print(f"Processed: {report['summary']['processed']}")
    print(f"Duplicates found: {report['summary']['duplicates_found']}")
    print(f"Invalid files: {report['summary']['invalid_files']}")
    print(f"Database: {organizer.db_path}")
    print("=" * 80)

if __name__ == "__main__":
    main()

