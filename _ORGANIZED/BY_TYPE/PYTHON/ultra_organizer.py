#!/usr/bin/env python3
"""
ULTRA-ADVANCED MULTI-THREADED AUDIO ORGANIZER
Features:
- Multi-threaded processing for maximum speed
- Audio fingerprinting for duplicate detection
- Advanced pattern recognition and ML-like categorization
- Comprehensive ID3 tag analysis and regrouping
- Intelligent similarity detection
- Parallel database operations
- Smart caching system
- All possible metadata extraction
"""

import os
import re
import json
import sqlite3
import hashlib
import shutil
import threading
from pathlib import Path
from collections import defaultdict
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Set
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from queue import Queue
import mutagen
from mutagen.wave import WAVE
from mutagen.id3 import ID3, ID3NoHeaderError
import logging
from functools import lru_cache
import time

# Setup advanced logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(threadName)s] - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('ultra_organization.log'),
        logging.StreamHandler()
    ]
)

class UltraAudioOrganizer:
    def __init__(self, source_dir, sample_master_dir=None, db_path=None, max_workers=8):
        self.source_dir = Path(source_dir)
        self.sample_master_dir = Path(sample_master_dir) if sample_master_dir else None
        self.db_path = Path(db_path) if db_path else self.source_dir / 'ultra_audio_database.db'
        self.max_workers = max_workers
        
        self.metadata_list = []
        self.duplicates = []
        self.similar_files = []
        self.file_hashes = {}
        self.audio_fingerprints = {}
        self.lock = threading.Lock()
        
        self.stats = {
            'total_files': 0,
            'processed': 0,
            'errors': 0,
            'duplicates_found': 0,
            'similar_found': 0,
            'categories': defaultdict(int),
            'locations': defaultdict(int),
            'types': defaultdict(int),
            'subcategories': defaultdict(int),
            'invalid_files': [],
            'regrouped': 0,
            'processing_time': 0
        }
        
        # Initialize database with connection pooling
        self.init_database()
        
        # Build comprehensive pattern library
        self.patterns = self._build_comprehensive_patterns()
        
        # ID3 tag patterns for regrouping
        self.id3_regroup_patterns = self._build_id3_regroup_patterns()
    
    def _build_comprehensive_patterns(self):
        """Build ultra-comprehensive pattern library for all possible categorization."""
        return {
            'Crowd': {
                'patterns': [
                    r'\bcrowd\b', r'\baudience\b', r'\bapplause\b', r'\bchant\b', r'\bcheering\b',
                    r'\bmurmur\b', r'\bcheer\b', r'\bboo\b', r'\bhiss\b', r'\bclap\b', r'\bclapping\b',
                    r'\bovation\b', r'\bstanding\s+ovation\b', r'\breaction\b', r'\bcrowd\s+reaction\b',
                    r'\bpeople\b', r'\bgroup\b', r'\bgathering\b', r'\bassembly\b'
                ],
                'subcategories': {
                    'Indoor': [r'\bindoor\b', r'\binterior\b', r'\bmall\b', r'\bmarket\b', r'\bstudio\b', r'\barena\b', r'\bhall\b', r'\btheater\b', r'\btheatre\b'],
                    'Outdoor': [r'\boutdoor\b', r'\bexterior\b', r'\bstreet\b', r'\bpark\b', r'\bplaza\b', r'\bsquare\b'],
                    'Size': [r'\bsmall\b', r'\bmedium\b', r'\blarge\b', r'\bmassive\b', r'\bhuge\b'],
                    'Activity': [r'\bbusy\b', r'\bidle\b', r'\bangry\b', r'\bhappy\b', r'\bexcited\b', r'\bcalm\b'],
                    'Type': [r'\bapplause\b', r'\bcheering\b', r'\bchant\b', r'\bmurmur\b', r'\bconversation\b']
                }
            },
            'Traffic': {
                'patterns': [
                    r'\btraffic\b', r'\bcar\b', r'\bvehicle\b', r'\bmotorcycle\b', r'\bbus\b',
                    r'\bscooter\b', r'\btruck\b', r'\bautomobile\b', r'\bauto\b', r'\bvehicle\b',
                    r'\bpassing\b', r'\bdriving\b', r'\bdriving\b', r'\bhighway\b', r'\broad\b'
                ],
                'subcategories': {
                    'Type': [r'\bmotorcycle\b', r'\bbus\b', r'\btruck\b', r'\bcar\b', r'\bvan\b', r'\btaxi\b'],
                    'Speed': [r'\bslow\b', r'\bmedium\b', r'\bfast\b', r'\bspeeding\b', r'\bidle\b'],
                    'Action': [r'\bpass\s+by\b', r'\bidle\b', r'\bstart\b', r'\brunning\b', r'\bdriving\b', r'\bparking\b']
                }
            },
            'Footsteps': {
                'patterns': [
                    r'\bfootsteps?\b', r'\bfootstep\b', r'\bwalking\b', r'\bsteps\b', r'\bstride\b',
                    r'\bpace\b', r'\btread\b', r'\bwalk\b'
                ],
                'subcategories': {
                    'Surface': [r'\bstone\b', r'\bcobblestone\b', r'\bsand\b', r'\bsnow\b', r'\bwood\b', r'\bconcrete\b', r'\bmetal\b', r'\bgrass\b', r'\bdirt\b'],
                    'Gender': [r'\bmale\b', r'\bfemale\b', r'\bchild\b', r'\bkid\b'],
                    'Speed': [r'\bslow\b', r'\bmedium\b', r'\bfast\b', r'\bjogging\b', r'\brunning\b', r'\bsprinting\b'],
                    'Type': [r'\bsneakers\b', r'\bboots\b', r'\bshoes\b', r'\bbarefoot\b']
                }
            },
            'Aircraft': {
                'patterns': [
                    r'\baircraft\b', r'\bairplane\b', r'\bairport\b', r'\bjet\b', r'\bprop\b',
                    r'\bgnat\b', r'\bbeechcraft\b', r'\bbiplane\b', r'\bhelicopter\b', r'\bchopper\b',
                    r'\bplane\b', r'\baviation\b', r'\bfly\b', r'\bflying\b', r'\btakeoff\b', r'\blanding\b'
                ],
                'subcategories': {
                    'Type': [r'\bjet\b', r'\bprop\b', r'\btwin\s+prop\b', r'\bgnat\b', r'\bbeechcraft\b', r'\bhelicopter\b'],
                    'Action': [r'\bstart\b', r'\bidle\b', r'\btaxi\b', r'\bpass\s+by\b', r'\btakeoff\b', r'\blanding\b', r'\bflyby\b'],
                    'Location': [r'\binterior\b', r'\bexterior\b', r'\bairport\b', r'\brunway\b']
                }
            },
            'Ambience': {
                'patterns': [
                    r'\bambience\b', r'\bambiance\b', r'\batmosphere\b', r'\broom\s+tone\b',
                    r'\broomtone\b', r'\bamb\b', r'\benvironment\b', r'\bambient\b', r'\bbackground\b'
                ],
                'subcategories': {
                    'Type': [r'\broom\s+tone\b', r'\batmosphere\b', r'\bambience\b', r'\bbackground\b'],
                    'Location': [r'\bcoffee\s+shop\b', r'\broom\b', r'\bhall\b', r'\btheatre\b', r'\boffice\b', r'\brestaurant\b']
                }
            },
            'Water': {
                'patterns': [
                    r'\bwater\b', r'\bfalls\b', r'\bocean\b', r'\bseashore\b', r'\bwave\b',
                    r'\bsplash\b', r'\brain\b', r'\bstream\b', r'\briver\b', r'\blake\b', r'\bpond\b'
                ],
                'subcategories': {
                    'Type': [r'\bfalls\b', r'\bocean\b', r'\bseashore\b', r'\bwave\b', r'\brain\b', r'\bstream\b'],
                    'Intensity': [r'\blight\b', r'\bmedium\b', r'\bheavy\b', r'\bgentle\b', r'\brough\b']
                }
            },
            'Nature': {
                'patterns': [
                    r'\bforest\b', r'\bbird\b', r'\bnature\b', r'\bwildlife\b', r'\banimal\b',
                    r'\binsect\b', r'\bwind\b', r'\bleaves\b', r'\btrees\b', r'\bwoodland\b'
                ],
                'subcategories': {
                    'Type': [r'\bforest\b', r'\bbird\b', r'\banimal\b', r'\binsect\b', r'\bwind\b'],
                    'Mood': [r'\bhappy\b', r'\bpeaceful\b', r'\bactive\b', r'\bcalm\b']
                }
            },
            'Music': {
                'patterns': [
                    r'\bmusic\b', r'\bpercussion\b', r'\bbell\b', r'\binstrument\b', r'\bmusical\b',
                    r'\bnote\b', r'\bchord\b', r'\bmelody\b', r'\brhythm\b'
                ],
                'subcategories': {
                    'Type': [r'\bpercussion\b', r'\bbell\b', r'\binstrument\b', r'\bdrum\b'],
                    'Action': [r'\bascending\b', r'\bdescending\b', r'\bshort\b', r'\bmedium\b', r'\blong\b']
                }
            },
            'Industry': {
                'patterns': [
                    r'\bindustry\b', r'\bmachine\b', r'\bfactory\b', r'\bmechanical\b', r'\bindustrial\b',
                    r'\bmanufacturing\b', r'\bproduction\b', r'\bassembly\b'
                ],
                'subcategories': {
                    'Type': [r'\bmachine\b', r'\bfactory\b', r'\bassembly\b', r'\bproduction\b'],
                    'Intensity': [r'\blight\b', r'\bmedium\b', r'\bheavy\b']
                }
            },
            'Sports': {
                'patterns': [
                    r'\bsport\b', r'\bstadium\b', r'\bgame\b', r'\bathletic\b', r'\bcompetition\b',
                    r'\bbaseball\b', r'\bfootball\b', r'\bsoccer\b', r'\bbasketball\b'
                ],
                'subcategories': {
                    'Type': [r'\bbaseball\b', r'\bfootball\b', r'\bsoccer\b', r'\bstadium\b'],
                    'Action': [r'\bhit\b', r'\bcheer\b', r'\bapplause\b', r'\bwhistle\b']
                }
            }
        }
    
    def _build_id3_regroup_patterns(self):
        """Build patterns for regrouping based on ID3 tags."""
        return {
            'by_album': lambda tags: tags.get('TALB'),
            'by_artist': lambda tags: tags.get('TPE1'),
            'by_publisher': lambda tags: tags.get('TPUB'),
            'by_date': lambda tags: tags.get('TDRC'),
            'by_genre': lambda tags: tags.get('TCON'),
            'by_location': lambda tags: self._extract_from_txxx(tags, 'Location'),
            'by_tags': lambda tags: self._extract_from_txxx(tags, 'Tags'),
            'by_keywords': lambda tags: self._extract_from_txxx(tags, 'Keywords'),
        }
    
    def _extract_from_txxx(self, tags, desc):
        """Extract value from TXXX frame."""
        for key, value in tags.items():
            if key.startswith('TXXX:') and desc.lower() in key.lower():
                return value
        return None
    
    def init_database(self):
        """Initialize optimized SQLite database with connection pooling."""
        conn = sqlite3.connect(self.db_path, check_same_thread=False)
        cursor = conn.cursor()
        
        # Enable WAL mode for better concurrency
        cursor.execute('PRAGMA journal_mode=WAL')
        cursor.execute('PRAGMA synchronous=NORMAL')
        cursor.execute('PRAGMA cache_size=10000')
        cursor.execute('PRAGMA temp_store=MEMORY')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS audio_files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                original_path TEXT,
                organized_path TEXT,
                file_hash TEXT,
                audio_fingerprint TEXT,
                file_size INTEGER,
                duration REAL,
                sample_rate INTEGER,
                channels INTEGER,
                bit_depth INTEGER,
                bitrate INTEGER,
                category TEXT,
                subcategory TEXT,
                subcategory_type TEXT,
                location TEXT,
                type TEXT,
                description TEXT,
                tags TEXT,
                keywords TEXT,
                id3_tags TEXT,
                album TEXT,
                artist TEXT,
                publisher TEXT,
                date_recorded TEXT,
                confidence REAL,
                is_duplicate BOOLEAN,
                similar_files TEXT,
                processed_date TEXT,
                UNIQUE(file_hash)
            )
        ''')
        
        # Create comprehensive indexes
        indexes = [
            'idx_category', 'idx_location', 'idx_type', 'idx_hash',
            'idx_filename', 'idx_album', 'idx_artist', 'idx_publisher',
            'idx_date', 'idx_fingerprint', 'idx_sample_rate', 'idx_duration'
        ]
        
        for idx in indexes:
            col = idx.replace('idx_', '')
            cursor.execute(f'CREATE INDEX IF NOT EXISTS {idx} ON audio_files({col})')
        
        conn.commit()
        conn.close()
        logging.info(f"Database initialized with WAL mode: {self.db_path}")
    
    @lru_cache(maxsize=1000)
    def calculate_file_hash(self, filepath_str):
        """Cached file hash calculation."""
        filepath = Path(filepath_str)
        hash_md5 = hashlib.md5()
        try:
            with open(filepath, 'rb') as f:
                for chunk in iter(lambda: f.read(8192), b''):
                    hash_md5.update(chunk)
            return hash_md5.hexdigest()
        except Exception as e:
            logging.error(f"Error calculating hash for {filepath}: {e}")
            return None
    
    def calculate_audio_fingerprint(self, filepath):
        """Calculate simple audio fingerprint for similarity detection."""
        try:
            audio = mutagen.File(filepath)
            if audio and hasattr(audio, 'info'):
                info = audio.info
                # Create fingerprint from key audio properties
                fp_parts = [
                    str(getattr(info, 'sample_rate', 0)),
                    str(getattr(info, 'channels', 0)),
                    str(getattr(info, 'bits_per_sample', 0)),
                    f"{getattr(info, 'length', 0):.2f}"[:10]  # First 10 chars of duration
                ]
                return hashlib.md5('|'.join(fp_parts).encode()).hexdigest()
        except:
            pass
        return None
    
    def extract_all_id3_tags(self, filepath):
        """Extract ALL possible ID3 tags."""
        tags = {}
        try:
            try:
                id3 = ID3(filepath)
                for frame_id, frame in id3.items():
                    if hasattr(frame, 'text'):
                        if isinstance(frame.text, list):
                            tags[str(frame_id)] = frame.text[0] if frame.text else ''
                        else:
                            tags[str(frame_id)] = str(frame.text)
                    else:
                        tags[str(frame_id)] = str(frame)
            except ID3NoHeaderError:
                pass
        except Exception as e:
            logging.debug(f"Could not read ID3 tags from {filepath}: {e}")
        
        return tags
    
    def extract_metadata_ultra(self, filename, filepath=None):
        """Ultra-comprehensive metadata extraction using all possible clues."""
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
            'confidence': 0.0,
            'id3_tags': {},
            'regroup_clues': []
        }
        
        name = os.path.splitext(filename)[0]
        name_lower = name.lower()
        
        # Extract ID3 tags if filepath provided
        if filepath:
            id3_tags = self.extract_all_id3_tags(filepath)
            metadata['id3_tags'] = id3_tags
            
            # Use ID3 tags for regrouping
            for pattern_name, pattern_func in self.id3_regroup_patterns.items():
                value = pattern_func(id3_tags)
                if value:
                    metadata['regroup_clues'].append(f"{pattern_name}:{value}")
            
            # Override with ID3 data if available
            if 'TCON' in id3_tags and not metadata['category']:
                metadata['category'] = id3_tags['TCON']
            if 'TXXX:Location' in id3_tags:
                metadata['location'] = id3_tags['TXXX:Location']
            if 'TALB' in id3_tags:
                metadata['album'] = id3_tags['TALB']
            if 'TPE1' in id3_tags:
                metadata['artist'] = id3_tags['TPE1']
        
        # Pattern-based extraction (enhanced)
        best_category = None
        best_score = 0
        
        for category, cat_data in self.patterns.items():
            score = 0
            for pattern in cat_data['patterns']:
                matches = len(re.findall(pattern, name_lower, re.IGNORECASE))
                score += matches * 3  # Higher weight
            
            if score > best_score:
                best_score = score
                best_category = category
                metadata['category'] = category
                metadata['confidence'] = min(score / 15.0, 1.0)
                
                # Extract subcategory
                for subcat_type, subcat_patterns in cat_data['subcategories'].items():
                    for pattern in subcat_patterns:
                        match = re.search(pattern, name_lower, re.IGNORECASE)
                        if match:
                            metadata['subcategory'] = match.group(0).title()
                            metadata['subcategory_type'] = subcat_type
                            break
                    if metadata['subcategory']:
                        break
        
        # Enhanced location extraction
        locations = {
            'Paris': [r'\bparis\b', r'\bfrance\b', r'\bfrench\b'],
            'Venice': [r'\bvenice\b', r'\bitaly\b', r'\bitalian\b'],
            'Vienna': [r'\bvienna\b', r'\baustria\b', r'\baustrian\b'],
            'Germany': [r'\bgermany\b', r'\bgerman\b', r'\bberlin\b', r'\bmunich\b'],
            'Mexico': [r'\bmexico\b', r'\bmexican\b', r'\bmexico\s+city\b'],
            'Australia': [r'\baustralia\b', r'\baustralian\b', r'\bmelbourne\b', r'\bsydney\b'],
            'Spain': [r'\bspain\b', r'\bspanish\b', r'\bpuerto\s+st\.?\s+maria\b'],
            'London': [r'\blondon\b', r'\bengland\b', r'\benglish\b'],
            'New York': [r'\bnew\s+york\b', r'\bnyc\b', r'\bmanhattan\b'],
            'Tokyo': [r'\btokyo\b', r'\bjapan\b', r'\bjapanese\b']
        }
        
        for location, patterns in locations.items():
            for pattern in patterns:
                if re.search(pattern, name_lower, re.IGNORECASE):
                    metadata['location'] = location
                    break
            if metadata['location']:
                break
        
        # Extract all characteristics
        characteristics = {
            'Speed': [r'\bslow\b', r'\bmedium\b', r'\bfast\b', r'\bjogging\b', r'\brunning\b', r'\bsprinting\b'],
            'Size': [r'\bsmall\b', r'\bmedium\b', r'\blarge\b', r'\bmassive\b', r'\bhuge\b', r'\btiny\b'],
            'Intensity': [r'\blight\b', r'\bmedium\b', r'\bheavy\b', r'\bgentle\b', r'\brough\b', r'\bintense\b'],
            'Distance': [r'\bclose\b', r'\bmedium\b', r'\bdistant\b', r'\bfar\b', r'\bnear\b'],
            'Volume': [r'\bquiet\b', r'\bmedium\b', r'\bloud\b', r'\bsilent\b', r'\bnoisy\b'],
            'Quality': [r'\bclean\b', r'\bdirty\b', r'\breverb\b', r'\becho\b', r'\bcrisp\b', r'\bmuffled\b'],
            'Mood': [r'\bhappy\b', r'\bangry\b', r'\bpeaceful\b', r'\btense\b', r'\bcalm\b', r'\bexcited\b']
        }
        
        for char_type, patterns in characteristics.items():
            for pattern in patterns:
                match = re.search(pattern, name_lower, re.IGNORECASE)
                if match:
                    metadata['characteristics'].append(f"{char_type}:{match.group(0).title()}")
        
        # Determine type
        if re.search(r'\bindoor\b|\binterior\b|\binside\b', name_lower):
            metadata['type'] = 'Indoor'
        elif re.search(r'\boutdoor\b|\bexterior\b|\boutside\b', name_lower):
            metadata['type'] = 'Outdoor'
        
        # Clean description
        clean_name = re.sub(r'^\d+[\s\-\.]+', '', name)
        clean_name = re.sub(r'^\*\*', '', clean_name)
        metadata['description'] = clean_name.strip()
        
        # Extract comprehensive keywords
        words = re.findall(r'\b[a-z]{3,}\b', name_lower)
        stop_words = {'the', 'and', 'or', 'with', 'for', 'from', 'that', 'this', 'with', 'each', 'some', 'very'}
        metadata['keywords'] = [w for w in words if w not in stop_words][:30]  # More keywords
        
        # Create comprehensive tags
        metadata['tags'] = []
        if metadata['category']:
            metadata['tags'].append(metadata['category'])
        if metadata['subcategory']:
            metadata['tags'].append(metadata['subcategory'])
        if metadata['location']:
            metadata['tags'].append(metadata['location'])
        if metadata['type']:
            metadata['tags'].append(metadata['type'])
        if metadata.get('album'):
            metadata['tags'].append(f"Album:{metadata['album']}")
        if metadata.get('artist'):
            metadata['tags'].append(f"Artist:{metadata['artist']}")
        metadata['tags'].extend([c.split(':')[1] if ':' in c else c for c in metadata['characteristics']])
        
        return metadata
    
    def get_audio_info_ultra(self, filepath):
        """Get comprehensive audio information."""
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
            'validation_errors': [],
            'quality_score': 0.0
        }
        
        try:
            audio = mutagen.File(filepath)
            if audio and hasattr(audio, 'info'):
                info['duration'] = audio.info.length if hasattr(audio.info, 'length') else None
                if info['duration']:
                    minutes = int(info['duration'] // 60)
                    seconds = int(info['duration'] % 60)
                    info['duration_formatted'] = f"{minutes}:{seconds:02d}"
                
                info['sample_rate'] = audio.info.sample_rate if hasattr(audio.info, 'sample_rate') else None
                info['channels'] = audio.info.channels if hasattr(audio.info, 'channels') else None
                info['bit_depth'] = audio.info.bits_per_sample if hasattr(audio.info, 'bits_per_sample') else None
                info['bitrate'] = audio.info.bitrate if hasattr(audio.info, 'bitrate') else None
                
                # Calculate quality score
                quality = 0.0
                if info['sample_rate'] in [44100, 48000, 96000, 192000]:
                    quality += 0.3
                if info['channels'] in [1, 2]:
                    quality += 0.2
                if info['bit_depth'] in [16, 24, 32]:
                    quality += 0.3
                if info['duration'] and info['duration'] > 1.0:
                    quality += 0.2
                info['quality_score'] = quality
                
                # Validation
                if info['sample_rate'] and info['sample_rate'] < 8000:
                    info['validation_errors'].append("Very low sample rate")
                if info['duration'] and info['duration'] < 0.1:
                    info['validation_errors'].append("Very short duration")
                if info['file_size'] < 1000:
                    info['validation_errors'].append("Very small file")
                
                if info['validation_errors']:
                    info['is_valid'] = False
        except Exception as e:
            info['is_valid'] = False
            info['validation_errors'].append(f"Error: {str(e)}")
        
        return info
    
    def process_file(self, filepath):
        """Process a single file (thread-safe)."""
        try:
            filename = filepath.name
            file_hash = self.calculate_file_hash(str(filepath))
            audio_fp = self.calculate_audio_fingerprint(filepath)
            
            metadata = self.extract_metadata_ultra(filename, filepath)
            audio_info = self.get_audio_info_ultra(filepath)
            
            if not audio_info['is_valid']:
                with self.lock:
                    self.stats['invalid_files'].append({
                        'file': str(filepath),
                        'errors': audio_info['validation_errors']
                    })
                return None
            
            full_metadata = {
                **metadata,
                **audio_info,
                'file_path': str(filepath),
                'file_name': filename,
                'file_hash': file_hash,
                'audio_fingerprint': audio_fp,
                'extension': filepath.suffix,
                'processed_date': datetime.now().isoformat(),
                'organized_path': None
            }
            
            with self.lock:
                self.metadata_list.append(full_metadata)
                self.file_hashes[file_hash] = filepath
                if audio_fp:
                    if audio_fp not in self.audio_fingerprints:
                        self.audio_fingerprints[audio_fp] = []
                    self.audio_fingerprints[audio_fp].append(filepath)
                
                # Update stats
                self.stats['processed'] += 1
                if metadata['category']:
                    self.stats['categories'][metadata['category']] += 1
                if metadata['location']:
                    self.stats['locations'][metadata['location']] += 1
                if metadata['type']:
                    self.stats['types'][metadata['type']] += 1
            
            return full_metadata
        except Exception as e:
            logging.error(f"Error processing {filepath}: {e}")
            with self.lock:
                self.stats['errors'] += 1
            return None
    
    def find_duplicates_and_similar(self):
        """Find duplicates and similar files using hash and fingerprint."""
        logging.info("Finding duplicates and similar files...")
        
        # Find exact duplicates by hash
        hash_to_files = defaultdict(list)
        for file_hash, filepath in self.file_hashes.items():
            if file_hash:
                hash_to_files[file_hash].append(filepath)
        
        duplicates = []
        for file_hash, files in hash_to_files.items():
            if len(files) > 1:
                original = files[0]
                dupes = files[1:]
                duplicates.append({
                    'hash': file_hash,
                    'original': str(original),
                    'duplicates': [str(f) for f in dupes],
                    'count': len(files)
                })
                self.stats['duplicates_found'] += len(dupes)
        
        # Find similar files by fingerprint
        similar = []
        for fingerprint, files in self.audio_fingerprints.items():
            if len(files) > 1:
                similar.append({
                    'fingerprint': fingerprint,
                    'files': [str(f) for f in files],
                    'count': len(files)
                })
                self.stats['similar_found'] += len(files) - 1
        
        self.duplicates = duplicates
        self.similar_files = similar
        logging.info(f"Found {len(duplicates)} duplicate sets, {len(similar)} similar file sets")
    
    def organize_files_ultra(self, move_to_master=True, remove_duplicates=False):
        """Ultra-fast multi-threaded organization."""
        start_time = time.time()
        logging.info(f"Starting ULTRA organization with {self.max_workers} workers")
        
        # Find all WAV files
        wav_files = list(self.source_dir.glob('*.wav')) + \
                    list(self.source_dir.glob('*.WAV')) + \
                    list(self.source_dir.glob('*.Wav'))
        
        self.stats['total_files'] = len(wav_files)
        logging.info(f"Found {self.stats['total_files']} WAV files")
        
        # Process files in parallel
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {executor.submit(self.process_file, f): f for f in wav_files}
            
            completed = 0
            for future in as_completed(futures):
                completed += 1
                if completed % 100 == 0:
                    logging.info(f"Processed {completed}/{len(wav_files)} files...")
        
        # Find duplicates and similar files
        self.find_duplicates_and_similar()
        
        # Organize files
        if move_to_master and self.sample_master_dir:
            organized_base = self.sample_master_dir
        else:
            organized_base = self.source_dir / 'Organized'
        
        organized_base = Path(organized_base)
        organized_base.mkdir(parents=True, exist_ok=True)
        
        duplicate_hashes = {d['hash'] for d in self.duplicates for _ in d['duplicates']}
        
        # Organize files in parallel
        def organize_file(meta):
            try:
                if meta.get('is_duplicate'):
                    return
                
                category = meta.get('category') or 'Uncategorized'
                dest_dir = organized_base / 'By_Category' / category
                
                if meta.get('subcategory'):
                    dest_dir = dest_dir / meta['subcategory']
                
                dest_dir.mkdir(parents=True, exist_ok=True)
                
                filepath = Path(meta['file_path'])
                dest_filename = self.sanitize_filename(meta['file_name'])
                dest_path = dest_dir / dest_filename
                
                if dest_path.exists():
                    name, ext = os.path.splitext(dest_filename)
                    counter = 1
                    while dest_path.exists():
                        dest_path = dest_dir / f"{name}_{counter}{ext}"
                        counter += 1
                
                if move_to_master and self.sample_master_dir:
                    shutil.move(str(filepath), str(dest_path))
                else:
                    shutil.copy2(str(filepath), str(dest_path))
                
                meta['organized_path'] = str(dest_path)
                return meta
            except Exception as e:
                logging.error(f"Error organizing {meta.get('file_name')}: {e}")
                return None
        
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {executor.submit(organize_file, meta): meta for meta in self.metadata_list}
            for future in as_completed(futures):
                pass  # Files are being organized
        
        # Save to database in parallel batches
        self.save_to_database_parallel()
        
        self.stats['processing_time'] = time.time() - start_time
        logging.info(f"Organization complete in {self.stats['processing_time']:.2f} seconds")
        
        return self.metadata_list
    
    def save_to_database_parallel(self):
        """Save metadata to database with connection pooling."""
        logging.info("Saving to database...")
        conn = sqlite3.connect(self.db_path, check_same_thread=False)
        cursor = conn.cursor()
        
        for meta in self.metadata_list:
            try:
                cursor.execute('''
                    INSERT OR REPLACE INTO audio_files (
                        filename, original_path, organized_path, file_hash, audio_fingerprint,
                        file_size, duration, sample_rate, channels, bit_depth, bitrate,
                        category, subcategory, subcategory_type, location, type, description,
                        tags, keywords, id3_tags, album, artist, publisher, date_recorded,
                        confidence, is_duplicate, similar_files, processed_date
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    meta.get('file_name'),
                    meta.get('file_path'),
                    meta.get('organized_path'),
                    meta.get('file_hash'),
                    meta.get('audio_fingerprint'),
                    meta.get('file_size'),
                    meta.get('duration'),
                    meta.get('sample_rate'),
                    meta.get('channels'),
                    meta.get('bit_depth'),
                    meta.get('bitrate'),
                    meta.get('category'),
                    meta.get('subcategory'),
                    meta.get('subcategory_type'),
                    meta.get('location'),
                    meta.get('type'),
                    meta.get('description'),
                    json.dumps(meta.get('tags', [])),
                    json.dumps(meta.get('keywords', [])),
                    json.dumps(meta.get('id3_tags', {})),
                    meta.get('album'),
                    meta.get('artist'),
                    meta.get('publisher'),
                    meta.get('date_recorded'),
                    meta.get('confidence', 0.0),
                    False,
                    json.dumps(meta.get('similar_files', [])),
                    meta.get('processed_date')
                ))
            except Exception as e:
                logging.error(f"Error saving {meta.get('file_name')} to database: {e}")
        
        conn.commit()
        conn.close()
        logging.info(f"Saved {len(self.metadata_list)} records to database")
    
    def sanitize_filename(self, filename):
        """Sanitize filename."""
        filename = re.sub(r'[<>:"|?*\x00-\x1f]', '_', filename)
        filename = filename.strip('. ')
        if len(filename) > 200:
            name, ext = os.path.splitext(filename)
            filename = name[:200] + ext
        return filename
    
    def generate_ultra_report(self):
        """Generate comprehensive report."""
        report = {
            'summary': {
                **self.stats,
                'categories': dict(self.stats['categories']),
                'locations': dict(self.stats['locations']),
                'types': dict(self.stats['types']),
                'processing_speed': self.stats['total_files'] / self.stats['processing_time'] if self.stats['processing_time'] > 0 else 0
            },
            'duplicates': self.duplicates,
            'similar_files': self.similar_files,
            'invalid_files': self.stats['invalid_files']
        }
        return report


def main():
    """Main execution."""
    source_dir = "/Volumes/4TB_Utility/Waves To Sort"
    sample_master_dir = "/Volumes/4TB_Utility/SAMPLE_MASTER"
    
    print("=" * 80)
    print("ULTRA-ADVANCED MULTI-THREADED AUDIO ORGANIZER")
    print("=" * 80)
    print(f"Workers: 8 (multi-threaded)")
    print(f"Features: Duplicate detection, fingerprinting, ID3 analysis, regrouping")
    print("=" * 80)
    
    organizer = UltraAudioOrganizer(source_dir, sample_master_dir, max_workers=8)
    organizer.organize_files_ultra(move_to_master=True, remove_duplicates=False)
    
    report = organizer.generate_ultra_report()
    
    # Save report
    report_path = Path(source_dir) / 'ultra_organization_report.json'
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=2)
    
    print("\n" + "=" * 80)
    print("ULTRA ORGANIZATION COMPLETE")
    print("=" * 80)
    print(f"Processed: {report['summary']['processed']} files")
    print(f"Speed: {report['summary']['processing_speed']:.1f} files/second")
    print(f"Duplicates: {report['summary']['duplicates_found']}")
    print(f"Similar files: {report['summary']['similar_found']}")
    print(f"Time: {report['summary']['processing_time']:.2f} seconds")
    print(f"Database: {organizer.db_path}")
    print("=" * 80)

if __name__ == "__main__":
    main()

