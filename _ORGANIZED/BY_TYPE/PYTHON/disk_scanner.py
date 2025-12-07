#!/usr/bin/env python3
"""
Disk Scanner, Healer, Optimizer & Mover
Scans disk4s2 (/Volumes/4TB_Utility), heals files, optimizes metadata, and moves to NOIZYLAB
Handles all file types with intelligent organization
"""

import os
import shutil
import hashlib
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
import logging
import mutagen
from mutagen.wave import WAVE
from mutagen.id3 import ID3, ID3NoHeaderError
import sys

# Add NOIZYLAB to path
sys.path.insert(0, str(Path.home() / 'NOIZYLAB'))
try:
    from claude_integration import get_api_key
    from unified_config import get_config
    CONFIG_AVAILABLE = True
except ImportError:
    CONFIG_AVAILABLE = False

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('disk_scan.log'),
        logging.StreamHandler()
    ]
)

class DiskScanner:
    def __init__(self, disk_path=None, destination_dir=None, max_workers=8):
        self.disk_path = Path(disk_path) if disk_path else Path('/Volumes/4TB_Utility')
        self.destination_dir = Path(destination_dir) if destination_dir else Path.home() / 'NOIZYLAB'
        self.max_workers = max_workers
        
        if CONFIG_AVAILABLE:
            config = get_config()
            self.destination_dir = Path(config.get_workspace_path())
        
        self.stats = {
            'total_files': 0,
            'audio_files': 0,
            'video_files': 0,
            'image_files': 0,
            'document_files': 0,
            'code_files': 0,
            'archive_files': 0,
            'other_files': 0,
            'healed': 0,
            'optimized': 0,
            'moved': 0,
            'errors': 0,
            'skipped': 0,
            'corrupted': 0,
            'file_types': defaultdict(int)
        }
        
        self.found_files = []
        self.corrupted_files = []
        self.duplicate_files = []
        self.file_hashes = {}
        
        # File type categories
        self.audio_extensions = {'.wav', '.WAV', '.mp3', '.MP3', '.aiff', '.AIFF', '.flac', '.FLAC',
                                '.m4a', '.M4A', '.aac', '.AAC', '.ogg', '.OGG', '.wma', '.WMA'}
        self.video_extensions = {'.mp4', '.MP4', '.avi', '.AVI', '.mov', '.MOV', '.mkv', '.MKV',
                                '.webm', '.WEBM', '.flv', '.FLV', '.m4v', '.M4V'}
        self.image_extensions = {'.jpg', '.JPG', '.jpeg', '.JPEG', '.png', '.PNG', '.gif', '.GIF',
                                '.svg', '.SVG', '.webp', '.WEBP', '.bmp', '.BMP', '.tiff', '.TIFF'}
        self.document_extensions = {'.pdf', '.PDF', '.doc', '.DOC', '.docx', '.DOCX', '.xls', '.XLS',
                                   '.xlsx', '.XLSX', '.ppt', '.PPT', '.pptx', '.PPTX', '.txt', '.TXT',
                                   '.rtf', '.RTF', '.odt', '.ODT'}
        self.code_extensions = {'.py', '.js', '.ts', '.java', '.cpp', '.c', '.h', '.go', '.rs', '.rb',
                               '.php', '.swift', '.kt', '.sh', '.bash', '.zsh'}
        self.archive_extensions = {'.zip', '.ZIP', '.tar', '.TAR', '.gz', '.GZ', '.bz2', '.BZ2',
                                  '.7z', '.7Z', '.rar', '.RAR', '.dmg', '.DMG', '.iso', '.ISO'}
    
    def categorize_file(self, filepath):
        """Categorize file by extension."""
        ext = filepath.suffix.lower()
        
        if ext in self.audio_extensions:
            return 'audio'
        elif ext in self.video_extensions:
            return 'video'
        elif ext in self.image_extensions:
            return 'image'
        elif ext in self.document_extensions:
            return 'document'
        elif ext in self.code_extensions:
            return 'code'
        elif ext in self.archive_extensions:
            return 'archive'
        else:
            return 'other'
    
    def calculate_file_hash(self, filepath, chunk_size=8192):
        """Calculate MD5 hash for duplicate detection."""
        hash_md5 = hashlib.md5()
        try:
            with open(filepath, 'rb') as f:
                for chunk in iter(lambda: f.read(chunk_size), b''):
                    hash_md5.update(chunk)
            return hash_md5.hexdigest()
        except Exception as e:
            logging.error(f"Error calculating hash for {filepath}: {e}")
            return None
    
    def heal_file(self, filepath, file_type):
        """Heal/validate file based on type."""
        try:
            if file_type == 'audio':
                audio = mutagen.File(filepath)
                if audio is None:
                    return {'status': 'corrupted', 'error': 'Cannot read audio file'}
                
                if hasattr(audio, 'info'):
                    info = audio.info
                    if hasattr(info, 'length') and info.length <= 0:
                        return {'status': 'corrupted', 'error': 'Invalid duration'}
                
                return {'status': 'ok', 'has_tags': True}
            
            elif file_type == 'image':
                # Try to open as image
                try:
                    from PIL import Image
                    img = Image.open(filepath)
                    img.verify()
                    return {'status': 'ok'}
                except ImportError:
                    # PIL not available, skip validation
                    return {'status': 'ok', 'note': 'PIL not available'}
                except Exception as e:
                    return {'status': 'corrupted', 'error': str(e)}
            
            elif file_type == 'video':
                # Basic check - file exists and has size
                if filepath.stat().st_size == 0:
                    return {'status': 'corrupted', 'error': 'Empty file'}
                return {'status': 'ok'}
            
            else:
                # For other types, just check if readable
                if filepath.stat().st_size == 0:
                    return {'status': 'corrupted', 'error': 'Empty file'}
                return {'status': 'ok'}
        
        except Exception as e:
            return {'status': 'corrupted', 'error': str(e)}
    
    def optimize_audio_file(self, filepath):
        """Optimize audio file metadata."""
        try:
            filename = filepath.stem
            metadata = self.extract_metadata_from_filename(filename)
            
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
                return {'status': 'skipped', 'reason': f'ID3 not supported: {e}'}
        except Exception as e:
            return {'status': 'error', 'error': str(e)}
    
    def extract_metadata_from_filename(self, filename):
        """Extract metadata from filename."""
        import re
        
        metadata = {
            'title': filename,
            'description': filename,
            'category': None,
            'keywords': []
        }
        
        clean_name = re.sub(r'^\d+[\s\-\.]+', '', filename)
        clean_name = re.sub(r'[_-]', ' ', clean_name)
        
        metadata['title'] = clean_name[:100]
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
        
        return metadata
    
    def scan_disk(self):
        """Scan entire disk for files."""
        logging.info(f"Scanning disk: {self.disk_path}")
        logging.info("This may take a while for large disks...")
        
        # Skip system directories
        skip_dirs = {'.Trash', '.Spotlight-V100', '.fseventsd', '.DocumentRevisions-V100',
                    '.TemporaryItems', '.DS_Store', 'System', 'Library', '.git'}
        
        all_files = []
        
        for root, dirs, files in os.walk(self.disk_path):
            # Filter out system directories
            dirs[:] = [d for d in dirs if d not in skip_dirs and not d.startswith('.')]
            
            for file in files:
                if file.startswith('.'):
                    continue
                
                filepath = Path(root) / file
                
                try:
                    if not filepath.exists() or not filepath.is_file():
                        continue
                    
                    file_type = self.categorize_file(filepath)
                    ext = filepath.suffix.lower()
                    
                    file_info = {
                        'path': filepath,
                        'name': file,
                        'extension': ext,
                        'type': file_type,
                        'size': filepath.stat().st_size,
                        'modified': datetime.fromtimestamp(filepath.stat().st_mtime).isoformat()
                    }
                    
                    all_files.append(file_info)
                    self.stats['file_types'][ext] += 1
                    
                    # Count by type
                    if file_type == 'audio':
                        self.stats['audio_files'] += 1
                    elif file_type == 'video':
                        self.stats['video_files'] += 1
                    elif file_type == 'image':
                        self.stats['image_files'] += 1
                    elif file_type == 'document':
                        self.stats['document_files'] += 1
                    elif file_type == 'code':
                        self.stats['code_files'] += 1
                    elif file_type == 'archive':
                        self.stats['archive_files'] += 1
                    else:
                        self.stats['other_files'] += 1
                
                except Exception as e:
                    logging.debug(f"Error scanning {filepath}: {e}")
                    continue
        
        self.found_files = all_files
        self.stats['total_files'] = len(all_files)
        
        logging.info(f"Found {self.stats['total_files']} files")
        logging.info(f"  Audio: {self.stats['audio_files']}")
        logging.info(f"  Video: {self.stats['video_files']}")
        logging.info(f"  Images: {self.stats['image_files']}")
        logging.info(f"  Documents: {self.stats['document_files']}")
        logging.info(f"  Code: {self.stats['code_files']}")
        logging.info(f"  Archives: {self.stats['archive_files']}")
        logging.info(f"  Other: {self.stats['other_files']}")
        
        return all_files
    
    def find_duplicates(self):
        """Find duplicate files by hash."""
        logging.info("Finding duplicates...")
        
        hash_to_files = defaultdict(list)
        
        for file_info in self.found_files:
            file_hash = self.calculate_file_hash(file_info['path'])
            if file_hash:
                hash_to_files[file_hash].append(file_info)
                self.file_hashes[file_hash] = file_info
        
        duplicates = []
        for file_hash, files in hash_to_files.items():
            if len(files) > 1:
                original = files[0]
                dupes = files[1:]
                duplicates.append({
                    'hash': file_hash,
                    'original': original,
                    'duplicates': dupes,
                    'count': len(files)
                })
        
        self.duplicate_files = duplicates
        logging.info(f"Found {len(duplicates)} sets of duplicates")
    
    def process_file(self, file_info, heal=True, optimize=True):
        """Process a single file."""
        try:
            filepath = file_info['path']
            file_type = file_info['type']
            
            # Heal file
            if heal:
                heal_result = self.heal_file(filepath, file_type)
                if heal_result['status'] == 'ok':
                    self.stats['healed'] += 1
                elif heal_result['status'] == 'corrupted':
                    self.corrupted_files.append({
                        'file': str(filepath),
                        'error': heal_result.get('error', 'Unknown')
                    })
                    self.stats['corrupted'] += 1
                    return {'status': 'corrupted', 'file_info': file_info}
            
            # Optimize audio files
            if optimize and file_type == 'audio':
                opt_result = self.optimize_audio_file(filepath)
                if opt_result['status'] == 'optimized':
                    self.stats['optimized'] += 1
            
            return {'status': 'ok', 'file_info': file_info}
        
        except Exception as e:
            logging.error(f"Error processing {file_info['name']}: {e}")
            self.stats['errors'] += 1
            return {'status': 'error', 'error': str(e)}
    
    def organize_and_move_file(self, file_info):
        """Organize and move file to NOIZYLAB."""
        try:
            source_path = file_info['path']
            file_type = file_info['type']
            
            if not source_path.exists():
                return {'status': 'error', 'error': 'File not found'}
            
            # Determine destination based on type
            if file_type == 'audio':
                metadata = self.extract_metadata_from_filename(file_info['name'])
                category = metadata.get('category', 'Uncategorized')
                dest_dir = self.destination_dir / 'Audio' / category
            elif file_type == 'video':
                dest_dir = self.destination_dir / 'Video'
            elif file_type == 'image':
                dest_dir = self.destination_dir / 'Images'
            elif file_type == 'document':
                dest_dir = self.destination_dir / 'Documents'
            elif file_type == 'code':
                dest_dir = self.destination_dir / 'Code'
            elif file_type == 'archive':
                dest_dir = self.destination_dir / 'Archives'
            else:
                ext = file_info['extension'].lstrip('.')
                if not ext:
                    ext = 'Other'
                dest_dir = self.destination_dir / 'Files' / ext.upper()
            
            dest_dir.mkdir(parents=True, exist_ok=True)
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
            self.stats['moved'] += 1
            
            return {
                'status': 'moved',
                'source': str(source_path),
                'destination': str(dest_path),
                'type': file_type
            }
        
        except Exception as e:
            logging.error(f"Error moving {file_info['name']}: {e}")
            self.stats['errors'] += 1
            return {'status': 'error', 'error': str(e)}
    
    def process_all(self, heal=True, optimize=True, move=True):
        """Process all files: scan, heal, optimize, move."""
        logging.info("=" * 80)
        logging.info("DISK SCANNER - SCAN, HEAL, OPTIMIZE & MOVE")
        logging.info("=" * 80)
        logging.info(f"Disk: {self.disk_path}")
        logging.info(f"Destination: {self.destination_dir}")
        logging.info("=" * 80)
        
        # Step 1: Scan
        files = self.scan_disk()
        
        if not files:
            logging.info("No files found on disk")
            return
        
        # Step 2: Find duplicates
        self.find_duplicates()
        
        # Step 3: Heal and optimize
        if heal or optimize:
            logging.info("\nHealing and optimizing files...")
            
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                futures = {executor.submit(self.process_file, f, heal, optimize): f for f in files}
                
                completed = 0
                for future in as_completed(futures):
                    completed += 1
                    if completed % 100 == 0:
                        logging.info(f"Processed {completed}/{len(files)} files...")
        
        # Step 4: Move files
        if move:
            logging.info("\nMoving files to NOIZYLAB...")
            
            # Skip corrupted files
            valid_files = [f for f in files if f not in [cf.get('file_info') for cf in self.corrupted_files if 'file_info' in cf]]
            
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                futures = {executor.submit(self.organize_and_move_file, f): f for f in valid_files}
                
                completed = 0
                for future in as_completed(futures):
                    completed += 1
                    result = future.result()
                    if completed % 100 == 0:
                        logging.info(f"Moved {completed}/{len(valid_files)} files...")
        
        # Generate report
        self.generate_report()
    
    def generate_report(self):
        """Generate processing report."""
        report = {
            'scan_date': datetime.now().isoformat(),
            'disk_path': str(self.disk_path),
            'destination': str(self.destination_dir),
            'statistics': dict(self.stats),
            'corrupted_files': self.corrupted_files,
            'duplicates': len(self.duplicate_files),
            'file_types': dict(self.stats['file_types'])
        }
        
        report_path = self.destination_dir.parent / 'disk_scan_report.json'
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        logging.info("\n" + "=" * 80)
        logging.info("PROCESSING COMPLETE")
        logging.info("=" * 80)
        logging.info(f"Total files scanned: {self.stats['total_files']}")
        logging.info(f"Audio files: {self.stats['audio_files']}")
        logging.info(f"Video files: {self.stats['video_files']}")
        logging.info(f"Image files: {self.stats['image_files']}")
        logging.info(f"Document files: {self.stats['document_files']}")
        logging.info(f"Code files: {self.stats['code_files']}")
        logging.info(f"Archive files: {self.stats['archive_files']}")
        logging.info(f"Healed: {self.stats['healed']}")
        logging.info(f"Optimized: {self.stats['optimized']}")
        logging.info(f"Moved: {self.stats['moved']}")
        logging.info(f"Corrupted: {self.stats['corrupted']}")
        logging.info(f"Duplicates found: {len(self.duplicate_files)}")
        logging.info(f"Errors: {self.stats['errors']}")
        logging.info(f"Destination: {self.destination_dir}")
        logging.info(f"Report: {report_path}")
        logging.info("=" * 80)


def main():
    """Main execution."""
    disk_path = '/Volumes/4TB_Utility'
    destination_dir = Path.home() / 'NOIZYLAB'
    
    scanner = DiskScanner(disk_path, destination_dir, max_workers=8)
    scanner.process_all(heal=True, optimize=True, move=True)

if __name__ == '__main__':
    main()

