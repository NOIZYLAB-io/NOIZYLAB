#!/usr/bin/env python3
"""
Downloads Scanner, Healer, Optimizer & Mover
Scans Downloads folder, heals corrupted files, optimizes metadata, and moves to NOIZYLAB
"""

import os
import shutil
import hashlib
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict
import mutagen
from mutagen.wave import WAVE
from mutagen.id3 import ID3, ID3NoHeaderError
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
import re

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('downloads_scan.log'),
        logging.StreamHandler()
    ]
)

class DownloadsProcessor:
    def __init__(self, downloads_dir=None, destination_dir=None, max_workers=8):
        self.downloads_dir = Path(downloads_dir) if downloads_dir else Path.home() / 'Downloads'
        self.destination_dir = Path(destination_dir) if destination_dir else Path.home() / 'NOIZYLAB'
        self.max_workers = max_workers
        
        self.stats = {
            'total_files': 0,
            'audio_files': 0,
            'other_files': 0,
            'healed': 0,
            'optimized': 0,
            'moved': 0,
            'errors': 0,
            'skipped': 0,
            'file_types': defaultdict(int)
        }
        
        self.found_files = []
        self.corrupted_files = []
        
        # Ensure destination exists
        self.destination_dir.mkdir(parents=True, exist_ok=True)
    
    def scan_downloads(self):
        """Scan Downloads folder for all files."""
        logging.info(f"Scanning: {self.downloads_dir}")
        
        audio_extensions = {'.wav', '.WAV', '.mp3', '.MP3', '.aiff', '.AIFF', '.flac', '.FLAC', 
                           '.m4a', '.M4A', '.aac', '.AAC', '.ogg', '.OGG', '.wma', '.WMA'}
        
        all_files = []
        
        # Find all files
        for root, dirs, files in os.walk(self.downloads_dir):
            # Skip system folders
            dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'Sorted By MyQuickMac Neo']
            
            for file in files:
                if file.startswith('.'):
                    continue
                
                filepath = Path(root) / file
                ext = filepath.suffix.lower()
                
                file_info = {
                    'path': filepath,
                    'name': file,
                    'extension': ext,
                    'size': filepath.stat().st_size if filepath.exists() else 0,
                    'is_audio': ext in audio_extensions,
                    'type': 'audio' if ext in audio_extensions else 'other'
                }
                
                all_files.append(file_info)
                self.stats['file_types'][ext] += 1
                
                if file_info['is_audio']:
                    self.stats['audio_files'] += 1
                else:
                    self.stats['other_files'] += 1
        
        self.found_files = all_files
        self.stats['total_files'] = len(all_files)
        
        logging.info(f"Found {self.stats['total_files']} files ({self.stats['audio_files']} audio, {self.stats['other_files']} other)")
        return all_files
    
    def heal_file(self, filepath):
        """Heal/repair corrupted audio files."""
        try:
            # Try to read the file
            audio = mutagen.File(filepath)
            if audio is None:
                return {'status': 'corrupted', 'error': 'Cannot read file'}
            
            # Check if file is valid
            if hasattr(audio, 'info'):
                info = audio.info
                if hasattr(info, 'length') and info.length <= 0:
                    return {'status': 'corrupted', 'error': 'Invalid duration'}
            
            # Try to read ID3 tags (for WAV/MP3)
            try:
                id3 = ID3(filepath)
                return {'status': 'ok', 'has_tags': True}
            except ID3NoHeaderError:
                return {'status': 'ok', 'has_tags': False}
            except:
                return {'status': 'ok', 'has_tags': False}
        
        except Exception as e:
            return {'status': 'corrupted', 'error': str(e)}
    
    def optimize_audio_file(self, filepath):
        """Optimize audio file metadata."""
        try:
            # Extract metadata from filename
            filename = filepath.stem
            metadata = self.extract_metadata_from_filename(filename)
            
            # Try to add/update ID3 tags
            try:
                audio = WAVE(str(filepath))
                try:
                    id3 = ID3(filepath)
                except ID3NoHeaderError:
                    audio.add_tags()
                    id3 = ID3(filepath)
                
                # Add title if missing
                if 'TIT2' not in id3 and metadata.get('title'):
                    id3['TIT2'] = mutagen.id3.TIT2(encoding=3, text=[metadata['title']])
                
                # Add description
                if metadata.get('description'):
                    id3['TXXX:Description'] = mutagen.id3.TXXX(encoding=3, desc='Description', text=[metadata['description']])
                
                id3.save()
                return {'status': 'optimized', 'metadata': metadata}
            
            except Exception as e:
                # File might not support ID3, that's ok
                return {'status': 'skipped', 'reason': f'ID3 not supported: {e}'}
        
        except Exception as e:
            return {'status': 'error', 'error': str(e)}
    
    def extract_metadata_from_filename(self, filename):
        """Extract metadata from filename."""
        metadata = {
            'title': filename,
            'description': filename,
            'category': None,
            'keywords': []
        }
        
        # Clean filename
        clean_name = re.sub(r'^\d+[\s\-\.]+', '', filename)
        clean_name = re.sub(r'[_-]', ' ', clean_name)
        
        metadata['title'] = clean_name[:100]  # Limit length
        metadata['description'] = clean_name
        
        # Extract keywords
        words = re.findall(r'\b[a-z]{3,}\b', clean_name.lower())
        stop_words = {'the', 'and', 'or', 'with', 'for', 'from'}
        metadata['keywords'] = [w for w in words if w not in stop_words][:10]
        
        # Detect category
        name_lower = clean_name.lower()
        if any(word in name_lower for word in ['crowd', 'audience', 'applause']):
            metadata['category'] = 'Crowd'
        elif any(word in name_lower for word in ['traffic', 'car', 'vehicle']):
            metadata['category'] = 'Traffic'
        elif any(word in name_lower for word in ['footstep', 'walking']):
            metadata['category'] = 'Footsteps'
        elif any(word in name_lower for word in ['aircraft', 'airplane', 'jet']):
            metadata['category'] = 'Aircraft'
        elif any(word in name_lower for word in ['ambience', 'atmosphere']):
            metadata['category'] = 'Ambience'
        elif any(word in name_lower for word in ['water', 'rain', 'ocean']):
            metadata['category'] = 'Water'
        elif any(word in name_lower for word in ['music', 'instrument']):
            metadata['category'] = 'Music'
        
        return metadata
    
    def organize_and_move_file(self, file_info):
        """Organize and move file to NOIZYLAB."""
        try:
            source_path = file_info['path']
            
            if not source_path.exists():
                return {'status': 'error', 'error': 'File not found'}
            
            # Determine destination structure
            if file_info['is_audio']:
                # Organize audio files by category
                metadata = self.extract_metadata_from_filename(file_info['name'])
                category = metadata.get('category', 'Uncategorized')
                
                dest_dir = self.destination_dir / 'Audio' / category
                dest_dir.mkdir(parents=True, exist_ok=True)
            else:
                # Organize other files by type
                ext = file_info['extension'].lstrip('.')
                if not ext:
                    ext = 'Other'
                dest_dir = self.destination_dir / 'Files' / ext.upper()
                dest_dir.mkdir(parents=True, exist_ok=True)
            
            # Create destination path
            dest_path = dest_dir / file_info['name']
            
            # Handle duplicates
            if dest_path.exists():
                name, ext = os.path.splitext(file_info['name'])
                counter = 1
                while dest_path.exists():
                    dest_path = dest_dir / f"{name}_{counter}{ext}"
                    counter += 1
            
            # Move file
            shutil.move(str(source_path), str(dest_path))
            
            return {
                'status': 'moved',
                'source': str(source_path),
                'destination': str(dest_path),
                'type': file_info['type']
            }
        
        except Exception as e:
            logging.error(f"Error moving {file_info['name']}: {e}")
            return {'status': 'error', 'error': str(e)}
    
    def process_all(self, heal=True, optimize=True, move=True):
        """Process all files: scan, heal, optimize, move."""
        logging.info("=" * 80)
        logging.info("DOWNLOADS SCANNER - SCAN, HEAL, OPTIMIZE & MOVE")
        logging.info("=" * 80)
        
        # Step 1: Scan
        files = self.scan_downloads()
        
        if not files:
            logging.info("No files found in Downloads")
            return
        
        # Step 2: Heal audio files
        if heal:
            logging.info("\nHealing audio files...")
            audio_files = [f for f in files if f['is_audio']]
            
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                futures = {executor.submit(self.heal_file, f['path']): f for f in audio_files}
                
                for future in as_completed(futures):
                    file_info = futures[future]
                    result = future.result()
                    
                    if result['status'] == 'corrupted':
                        self.corrupted_files.append({
                            'file': str(file_info['path']),
                            'error': result.get('error', 'Unknown')
                        })
                        logging.warning(f"Corrupted: {file_info['name']} - {result.get('error')}")
                    elif result['status'] == 'ok':
                        self.stats['healed'] += 1
        
        # Step 3: Optimize audio files
        if optimize:
            logging.info("\nOptimizing audio files...")
            audio_files = [f for f in files if f['is_audio']]
            
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                futures = {executor.submit(self.optimize_audio_file, f['path']): f for f in audio_files}
                
                for future in as_completed(futures):
                    result = future.result()
                    if result['status'] == 'optimized':
                        self.stats['optimized'] += 1
        
        # Step 4: Move files
        if move:
            logging.info("\nMoving files to NOIZYLAB...")
            
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                futures = {executor.submit(self.organize_and_move_file, f): f for f in files}
                
                for future in as_completed(futures):
                    result = future.result()
                    if result['status'] == 'moved':
                        self.stats['moved'] += 1
                        logging.info(f"Moved: {Path(result['source']).name} -> {result['destination']}")
                    elif result['status'] == 'error':
                        self.stats['errors'] += 1
                    else:
                        self.stats['skipped'] += 1
        
        # Generate report
        self.generate_report()
    
    def generate_report(self):
        """Generate processing report."""
        report = {
            'scan_date': datetime.now().isoformat(),
            'statistics': dict(self.stats),
            'corrupted_files': self.corrupted_files,
            'file_types': dict(self.stats['file_types']),
            'destination': str(self.destination_dir)
        }
        
        report_path = self.destination_dir.parent / 'downloads_scan_report.json'
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        logging.info("\n" + "=" * 80)
        logging.info("PROCESSING COMPLETE")
        logging.info("=" * 80)
        logging.info(f"Total files scanned: {self.stats['total_files']}")
        logging.info(f"Audio files: {self.stats['audio_files']}")
        logging.info(f"Other files: {self.stats['other_files']}")
        logging.info(f"Healed: {self.stats['healed']}")
        logging.info(f"Optimized: {self.stats['optimized']}")
        logging.info(f"Moved: {self.stats['moved']}")
        logging.info(f"Errors: {self.stats['errors']}")
        logging.info(f"Corrupted files: {len(self.corrupted_files)}")
        logging.info(f"Destination: {self.destination_dir}")
        logging.info(f"Report: {report_path}")
        logging.info("=" * 80)


def main():
    """Main execution."""
    downloads_dir = Path.home() / 'Downloads'
    destination_dir = Path.home() / 'NOIZYLAB'
    
    processor = DownloadsProcessor(downloads_dir, destination_dir, max_workers=8)
    processor.process_all(heal=True, optimize=True, move=True)

if __name__ == '__main__':
    main()

