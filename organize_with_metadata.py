#!/usr/bin/env python3
"""
Advanced WAV File Organization System with Comprehensive Metadata Extraction
Extracts metadata from filenames, creates organized folder structure, embeds metadata,
and moves files to SAMPLE_MASTER directory.
"""

import os
import re
import json
import csv
import shutil
from pathlib import Path
from collections import defaultdict
from datetime import datetime
import mutagen
from mutagen.wave import WAVE
from mutagen.id3 import ID3NoHeaderError

class AudioFileOrganizer:
    def __init__(self, source_dir, sample_master_dir=None):
        self.source_dir = Path(source_dir)
        self.sample_master_dir = Path(sample_master_dir) if sample_master_dir else None
        self.metadata_list = []
        self.stats = {
            'total_files': 0,
            'processed': 0,
            'errors': 0,
            'categories': defaultdict(int),
            'locations': defaultdict(int),
            'types': defaultdict(int),
            'subcategories': defaultdict(int)
        }
        
        # Enhanced category definitions with subcategories
        self.categories = {
            'Crowd': {
                'keywords': ['crowd', 'audience', 'applause', 'chant', 'cheering', 'murmur'],
                'subcategories': {
                    'Indoor': ['indoor', 'interior', 'mall', 'market', 'studio', 'arena', 'hall'],
                    'Outdoor': ['outdoor', 'exterior', 'street', 'park'],
                    'Size': ['small', 'medium', 'large'],
                    'Activity': ['busy', 'idle', 'angry', 'cheering', 'applause']
                }
            },
            'Traffic': {
                'keywords': ['traffic', 'car', 'vehicle', 'motorcycle', 'bus', 'scooter', 'truck'],
                'subcategories': {
                    'Type': ['car', 'motorcycle', 'bus', 'truck', 'scooter'],
                    'Speed': ['slow', 'medium', 'fast'],
                    'Action': ['pass by', 'idle', 'start', 'running']
                }
            },
            'Footsteps': {
                'keywords': ['footsteps', 'footstep', 'walking'],
                'subcategories': {
                    'Surface': ['stone', 'cobblestone', 'sand', 'snow', 'wood', 'concrete'],
                    'Gender': ['male', 'female'],
                    'Speed': ['slow', 'medium', 'fast', 'jogging', 'running']
                }
            },
            'Aircraft': {
                'keywords': ['aircraft', 'airplane', 'airport', 'jet', 'prop', 'gnat', 'beechcraft', 'twin prop'],
                'subcategories': {
                    'Type': ['jet', 'prop', 'twin prop', 'gnat', 'beechcraft'],
                    'Action': ['start', 'idle', 'taxi', 'pass by', 'takeoff', 'landing'],
                    'Location': ['interior', 'exterior', 'airport']
                }
            },
            'Ambience': {
                'keywords': ['ambience', 'ambiance', 'atmosphere', 'room tone', 'roomtone', 'amb'],
                'subcategories': {
                    'Type': ['room tone', 'atmosphere', 'ambience'],
                    'Location': ['coffee shop', 'room', 'hall', 'theatre', 'office'],
                    'Size': ['small', 'medium', 'large']
                }
            },
            'Water': {
                'keywords': ['water', 'falls', 'ocean', 'seashore', 'wave', 'splash'],
                'subcategories': {
                    'Type': ['falls', 'ocean', 'seashore', 'wave', 'splash'],
                    'Intensity': ['light', 'medium', 'heavy']
                }
            },
            'Nature': {
                'keywords': ['forest', 'bird', 'nature', 'wildlife', 'animal'],
                'subcategories': {
                    'Type': ['forest', 'bird', 'animal', 'wildlife'],
                    'Mood': ['happy', 'peaceful', 'active']
                }
            },
            'City': {
                'keywords': ['city', 'urban', 'street', 'downtown'],
                'subcategories': {
                    'Type': ['traffic', 'pedestrians', 'construction', 'general'],
                    'Size': ['small', 'medium', 'large']
                }
            },
            'Restaurant': {
                'keywords': ['restaurant', 'bar', 'pub', 'cafe', 'dining'],
                'subcategories': {
                    'Type': ['restaurant', 'bar', 'pub', 'cafe'],
                    'Crowd': ['small', 'medium', 'large', 'busy']
                }
            },
            'Music': {
                'keywords': ['music', 'percussion', 'bell tree', 'instrument', 'musical'],
                'subcategories': {
                    'Type': ['percussion', 'bell tree', 'instrument'],
                    'Action': ['ascending', 'descending', 'short', 'medium', 'long']
                }
            },
            'Industry': {
                'keywords': ['industry', 'machine', 'air system', 'factory', 'mechanical'],
                'subcategories': {
                    'Type': ['air system', 'machine', 'factory'],
                    'Intensity': ['light', 'medium', 'heavy']
                }
            },
            'Party': {
                'keywords': ['party', 'social gathering', 'celebration'],
                'subcategories': {
                    'Type': ['party', 'social gathering', 'celebration'],
                    'Size': ['small', 'medium', 'large']
                }
            },
            'Sports': {
                'keywords': ['baseball', 'sport', 'stadium', 'game'],
                'subcategories': {
                    'Type': ['baseball', 'sport', 'stadium'],
                    'Action': ['hit', 'cheer', 'applause']
                }
            }
        }
        
        # Enhanced location keywords
        self.locations = {
            'Paris': ['paris', 'france'],
            'Venice': ['venice', 'italy'],
            'Vienna': ['vienna', 'austria'],
            'Mexico': ['mexico', 'mexico city'],
            'Germany': ['germany', 'berlin', 'munich'],
            'Australia': ['australia', 'melbourne'],
            'Spain': ['spain', 'puerto st. maria']
        }
        
        # Enhanced characteristics
        self.characteristics = {
            'Speed': ['slow', 'medium', 'fast', 'jogging', 'running'],
            'Size': ['small', 'medium', 'large'],
            'Intensity': ['light', 'medium', 'heavy'],
            'Distance': ['close', 'medium', 'distant', 'far'],
            'Volume': ['quiet', 'medium', 'loud'],
            'Activity': ['busy', 'idle', 'active', 'passive'],
            'Mood': ['happy', 'angry', 'peaceful', 'tense'],
            'Quality': ['clean', 'dirty', 'reverb', 'echo']
        }

    def extract_metadata_from_filename(self, filename):
        """Extract comprehensive structured metadata from filename."""
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
            'keywords': []
        }
        
        name = os.path.splitext(filename)[0]
        name_lower = name.lower()
        
        # Extract category with subcategory
        best_match = None
        best_score = 0
        
        for category, cat_data in self.categories.items():
            for keyword in cat_data['keywords']:
                if keyword in name_lower:
                    score = len(keyword)
                    if score > best_score:
                        best_score = score
                        best_match = category
                        metadata['category'] = category
                        
                        # Extract subcategory
                        for subcat_type, subcat_keywords in cat_data['subcategories'].items():
                            for subcat_keyword in subcat_keywords:
                                if subcat_keyword in name_lower:
                                    metadata['subcategory'] = subcat_keyword.title()
                                    metadata['subcategory_type'] = subcat_type
                                    break
                            if metadata['subcategory']:
                                break
                        break
        
        # Extract location
        for location, keywords in self.locations.items():
            for keyword in keywords:
                if keyword in name_lower:
                    metadata['location'] = location
                    break
            if metadata['location']:
                break
        
        # Extract characteristics
        for char_type, char_list in self.characteristics.items():
            for char in char_list:
                if char in name_lower:
                    metadata['characteristics'].append(f"{char_type}:{char.title()}")
        
        # Determine type (Indoor/Outdoor)
        if any(word in name_lower for word in ['indoor', 'interior', 'inside']):
            metadata['type'] = 'Indoor'
        elif any(word in name_lower for word in ['outdoor', 'exterior', 'outside']):
            metadata['type'] = 'Outdoor'
        
        # Extract detailed description
        # Remove common prefixes like "01", "02-", etc.
        clean_name = re.sub(r'^\d+[\s\-\.]+', '', name)
        clean_name = re.sub(r'^\*\*', '', clean_name)
        metadata['description'] = clean_name.strip()
        
        # Extract keywords (all significant words)
        words = re.findall(r'\b[a-z]{3,}\b', name_lower)
        metadata['keywords'] = [w for w in words if w not in ['the', 'and', 'or', 'with', 'for', 'from', 'that', 'this']]
        
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
        metadata['tags'].extend([c.split(':')[1] if ':' in c else c for c in metadata['characteristics']])
        
        return metadata

    def get_audio_file_info(self, filepath):
        """Get comprehensive technical information from audio file."""
        info = {
            'file_size': os.path.getsize(filepath),
            'file_size_mb': round(os.path.getsize(filepath) / (1024 * 1024), 2),
            'duration': None,
            'duration_formatted': None,
            'sample_rate': None,
            'channels': None,
            'bit_depth': None,
            'bitrate': None,
            'format': 'WAV'
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
        except Exception as e:
            print(f"Warning: Could not read audio metadata for {filepath}: {e}")
        
        return info

    def embed_metadata_in_file(self, filepath, metadata):
        """Embed metadata into WAV file using ID3 tags."""
        try:
            audio = WAVE(str(filepath))
            
            # Try to load existing tags, or create new ones
            try:
                audio.add_tags()
            except mutagen.id3.error:
                # Tags already exist, we'll update them
                pass
            
            # Add or update metadata tags
            try:
                audio.tags['TIT2'] = mutagen.id3.TIT2(encoding=3, text=[metadata['description']])
            except:
                pass
            
            if metadata['category']:
                try:
                    audio.tags['TCON'] = mutagen.id3.TCON(encoding=3, text=[metadata['category']])
                except:
                    pass
                    
            if metadata['location']:
                try:
                    audio.tags['TXXX:Location'] = mutagen.id3.TXXX(encoding=3, desc='Location', text=[metadata['location']])
                except:
                    pass
                    
            if metadata['tags']:
                try:
                    audio.tags['TXXX:Tags'] = mutagen.id3.TXXX(encoding=3, desc='Tags', text=[', '.join(metadata['tags'])])
                except:
                    pass
                    
            if metadata['keywords']:
                try:
                    audio.tags['TXXX:Keywords'] = mutagen.id3.TXXX(encoding=3, desc='Keywords', text=[', '.join(metadata['keywords'][:10])])
                except:
                    pass
            
            audio.save()
            return True
        except Exception as e:
            # Silently fail - metadata embedding is optional
            return False

    def sanitize_filename(self, filename):
        """Sanitize filename for filesystem compatibility."""
        filename = re.sub(r'[<>:"|?*\x00-\x1f]', '_', filename)
        filename = filename.strip('. ')
        # Limit length
        if len(filename) > 200:
            name, ext = os.path.splitext(filename)
            filename = name[:200] + ext
        return filename

    def organize_files(self, move_to_master=True):
        """Main function to organize files with metadata."""
        print(f"Scanning files in: {self.source_dir}")
        
        # Find all WAV files
        wav_files = list(self.source_dir.glob('*.wav')) + \
                    list(self.source_dir.glob('*.WAV')) + \
                    list(self.source_dir.glob('*.Wav'))
        
        self.stats['total_files'] = len(wav_files)
        print(f"Found {self.stats['total_files']} WAV files")
        
        # Determine destination
        if move_to_master and self.sample_master_dir:
            organized_base = self.sample_master_dir
            print(f"Files will be moved to: {organized_base}")
        else:
            organized_base = self.source_dir / 'Organized'
            print(f"Files will be organized in: {organized_base}")
        
        organized_base = Path(organized_base)
        organized_base.mkdir(parents=True, exist_ok=True)
        
        # Process each file
        for idx, filepath in enumerate(wav_files, 1):
            if idx % 50 == 0:
                print(f"Processing file {idx}/{len(wav_files)}... ({self.stats['processed']} processed, {self.stats['errors']} errors)")
            
            try:
                filename = filepath.name
                metadata = self.extract_metadata_from_filename(filename)
                audio_info = self.get_audio_file_info(filepath)
                
                # Merge metadata
                full_metadata = {
                    **metadata,
                    **audio_info,
                    'file_path': str(filepath),
                    'file_name': filename,
                    'extension': filepath.suffix,
                    'processed_date': datetime.now().isoformat(),
                    'organized_path': None
                }
                
                # Organize file
                category = metadata['category'] or 'Uncategorized'
                dest_dir = organized_base / 'By_Category' / category
                
                # Add subcategory folder if available
                if metadata['subcategory']:
                    dest_dir = dest_dir / metadata['subcategory']
                
                dest_dir.mkdir(parents=True, exist_ok=True)
                
                # Create sanitized destination filename
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
                
                # Embed metadata
                self.embed_metadata_in_file(dest_path, metadata)
                
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
                
                # Also organize by location if available
                if metadata['location']:
                    location_dir = organized_base / 'By_Location' / metadata['location']
                    location_dir.mkdir(parents=True, exist_ok=True)
                    location_dest = location_dir / dest_filename
                    if not location_dest.exists():
                        if move_to_master and self.sample_master_dir:
                            shutil.copy2(str(dest_path), str(location_dest))
                        else:
                            shutil.copy2(str(filepath), str(location_dest))
                
            except Exception as e:
                print(f"Error processing {filepath}: {e}")
                self.stats['errors'] += 1
        
        return self.metadata_list

    def save_metadata(self, output_dir=None):
        """Save comprehensive metadata to multiple formats."""
        if output_dir is None:
            output_dir = self.source_dir / 'Metadata'
        else:
            output_dir = Path(output_dir)
        
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Create summary
        summary = {
            'total_files': self.stats['total_files'],
            'processed': self.stats['processed'],
            'errors': self.stats['errors'],
            'categories': dict(self.stats['categories']),
            'locations': dict(self.stats['locations']),
            'types': dict(self.stats['types']),
            'subcategories': dict(self.stats['subcategories']),
            'processed_date': datetime.now().isoformat(),
            'organization_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        # Save JSON (full metadata)
        json_path = output_dir / 'metadata_full.json'
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump({
                'summary': summary,
                'files': self.metadata_list
            }, f, indent=2, ensure_ascii=False)
        print(f"Saved full metadata to: {json_path}")
        
        # Save CSV
        csv_path = output_dir / 'metadata.csv'
        if self.metadata_list:
            fieldnames = list(self.metadata_list[0].keys())
            with open(csv_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.metadata_list)
            print(f"Saved CSV metadata to: {csv_path}")
        
        # Save summary
        summary_path = output_dir / 'summary.json'
        with open(summary_path, 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        print(f"Saved summary to: {summary_path}")
        
        # Save searchable index
        index_path = output_dir / 'search_index.json'
        search_index = {
            'by_category': {},
            'by_location': {},
            'by_type': {},
            'by_keyword': defaultdict(list)
        }
        
        for meta in self.metadata_list:
            cat = meta.get('category', 'Uncategorized')
            if cat not in search_index['by_category']:
                search_index['by_category'][cat] = []
            search_index['by_category'][cat].append({
                'file': meta['file_name'],
                'path': meta.get('organized_path', meta['file_path']),
                'description': meta.get('description', '')
            })
            
            if meta.get('location'):
                loc = meta['location']
                if loc not in search_index['by_location']:
                    search_index['by_location'][loc] = []
                search_index['by_location'][loc].append(meta['file_name'])
            
            if meta.get('type'):
                typ = meta['type']
                if typ not in search_index['by_type']:
                    search_index['by_type'][typ] = []
                search_index['by_type'][typ].append(meta['file_name'])
            
            for keyword in meta.get('keywords', []):
                search_index['by_keyword'][keyword].append(meta['file_name'])
        
        search_index['by_keyword'] = dict(search_index['by_keyword'])
        
        with open(index_path, 'w', encoding='utf-8') as f:
            json.dump(search_index, f, indent=2, ensure_ascii=False)
        print(f"Saved search index to: {index_path}")
        
        return summary

    def print_summary(self, summary):
        """Print comprehensive organization summary."""
        print("\n" + "=" * 80)
        print("ORGANIZATION SUMMARY")
        print("=" * 80)
        print(f"Total files found: {summary['total_files']}")
        print(f"Successfully processed: {summary['processed']}")
        print(f"Errors: {summary['errors']}")
        
        print(f"\n{'='*80}")
        print("FILES BY CATEGORY")
        print(f"{'='*80}")
        for cat, count in sorted(summary['categories'].items(), key=lambda x: x[1], reverse=True):
            percentage = (count / summary['processed'] * 100) if summary['processed'] > 0 else 0
            print(f"  {cat:30s}: {count:4d} ({percentage:5.1f}%)")
        
        if summary['locations']:
            print(f"\n{'='*80}")
            print("FILES BY LOCATION")
            print(f"{'='*80}")
            for loc, count in sorted(summary['locations'].items(), key=lambda x: x[1], reverse=True):
                percentage = (count / summary['processed'] * 100) if summary['processed'] > 0 else 0
                print(f"  {loc:30s}: {count:4d} ({percentage:5.1f}%)")
        
        if summary['types']:
            print(f"\n{'='*80}")
            print("FILES BY TYPE")
            print(f"{'='*80}")
            for typ, count in sorted(summary['types'].items(), key=lambda x: x[1], reverse=True):
                percentage = (count / summary['processed'] * 100) if summary['processed'] > 0 else 0
                print(f"  {typ:30s}: {count:4d} ({percentage:5.1f}%)")
        
        print(f"\n{'='*80}")
        print("ORGANIZATION COMPLETE")
        print(f"{'='*80}")
        if self.sample_master_dir:
            print(f"Files moved to: {self.sample_master_dir}")
        else:
            print(f"Files organized in: {self.source_dir / 'Organized'}")
        print(f"Metadata saved to: {self.source_dir / 'Metadata'}")
        print("=" * 80)


def main():
    """Main execution function."""
    source_dir = "/Volumes/4TB_Utility/Waves To Sort"
    
    # Check for SAMPLE_MASTER directory
    possible_master_dirs = [
        "/Volumes/4TB_Utility/SAMPLE_MASTER",
        "/Volumes/4TB_Utility/Sample Master",
        "/Volumes/4TB_Utility/sample_master",
        source_dir + "/SAMPLE_MASTER"
    ]
    
    sample_master_dir = None
    for dir_path in possible_master_dirs:
        if os.path.exists(dir_path):
            sample_master_dir = dir_path
            break
    
    # If not found, create it
    if sample_master_dir is None:
        sample_master_dir = "/Volumes/4TB_Utility/SAMPLE_MASTER"
        os.makedirs(sample_master_dir, exist_ok=True)
        print(f"Created SAMPLE_MASTER directory: {sample_master_dir}")
    
    print("=" * 80)
    print("ADVANCED WAV FILE ORGANIZATION SYSTEM")
    print("=" * 80)
    print(f"Source directory: {source_dir}")
    print(f"Destination: {sample_master_dir}")
    print("=" * 80)
    
    # Create organizer
    organizer = AudioFileOrganizer(source_dir, sample_master_dir)
    
    # Organize files
    organizer.organize_files(move_to_master=True)
    
    # Save metadata
    summary = organizer.save_metadata()
    
    # Print summary
    organizer.print_summary(summary)


if __name__ == "__main__":
    main()
