#!/usr/bin/env python3
"""
FXpansion Drum Library Manager
Test, Scan, Heal, Optimize, Deep Scan, Rename & Re-organize

Processes BFD/FXpansion audio samples and organizes them into a master drum library.
"""

import os
import sys
import wave
import struct
import hashlib
import shutil
import json
import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
import subprocess

# Configuration
FXPANSION_SOURCE = "/Volumes/6TB/_ORGANIZED/BFD_FXpansion"
MASTER_DRUM_LIBRARY = "/Volumes/SAMPLE_MASTER/06_Drums_Percussion/Drums_Master_Library"
REPORT_OUTPUT = "/Users/m2ultra/fxpansion_report"

# Category mapping for organizing files
CATEGORY_MAPPING = {
    'kick': 'Kicks',
    'bd': 'Kicks',
    'bass_drum': 'Kicks',
    'snare': 'Snares',
    'sd': 'Snares',
    'sn': 'Snares',
    'hihat': 'Hi_Hats',
    'hh': 'Hi_Hats',
    'hi_hat': 'Hi_Hats',
    'hat': 'Hi_Hats',
    'tom': 'Toms',
    'floor': 'Toms',
    'rack': 'Toms',
    'cymbal': 'Cymbals',
    'crash': 'Cymbals',
    'ride': 'Cymbals',
    'china': 'Cymbals',
    'splash': 'Cymbals',
    'percussion': 'Percussion',
    'perc': 'Percussion',
    'room': 'Room_Mics',
    'overhead': 'Overheads',
    'oh': 'Overheads',
    'ambient': 'Ambience',
    'master': 'Full_Kits',
}

# Articulation mapping
ARTICULATION_MAPPING = {
    'hit': 'Hit',
    'rim': 'Rimshot',
    'rimshot': 'Rimshot',
    'ss': 'Sidestick',
    'sidestick': 'Sidestick',
    'drag': 'Drag',
    'flam': 'Flam',
    'roll': 'Roll',
    'ghost': 'Ghost',
    'nosnare': 'Snares_Off',
    'felt': 'Felt',
    'rubber': 'Rubber',
    'wood': 'Wood',
    'brush': 'Brush',
    'mallet': 'Mallet',
    'closed': 'Closed',
    'open': 'Open',
    'pedal': 'Pedal',
    'half': 'Half_Open',
    'choke': 'Choke',
    'bell': 'Bell',
    'edge': 'Edge',
    'bow': 'Bow',
}


class AudioFile:
    """Represents an audio file with metadata."""
    
    def __init__(self, path: str):
        self.path = Path(path)
        self.filename = self.path.name
        self.extension = self.path.suffix.lower()
        self.size = 0
        self.duration = 0.0
        self.sample_rate = 0
        self.channels = 0
        self.bit_depth = 0
        self.is_valid = False
        self.error_message = ""
        self.md5_hash = ""
        self.category = "Uncategorized"
        self.subcategory = ""
        self.kit_name = ""
        self.articulation = ""
        self.velocity_layer = ""
        self.new_filename = ""
        
    def to_dict(self):
        return {
            'path': str(self.path),
            'filename': self.filename,
            'extension': self.extension,
            'size': self.size,
            'duration': round(self.duration, 3),
            'sample_rate': self.sample_rate,
            'channels': self.channels,
            'bit_depth': self.bit_depth,
            'is_valid': self.is_valid,
            'error_message': self.error_message,
            'category': self.category,
            'subcategory': self.subcategory,
            'kit_name': self.kit_name,
            'articulation': self.articulation,
            'velocity_layer': self.velocity_layer,
            'new_filename': self.new_filename,
        }


class DrumLibraryManager:
    """Main class for managing drum library operations."""
    
    def __init__(self, source_path: str, target_path: str, report_path: str):
        self.source_path = Path(source_path)
        self.target_path = Path(target_path)
        self.report_path = Path(report_path)
        self.audio_files = []
        self.stats = {
            'total_files': 0,
            'valid_files': 0,
            'corrupted_files': 0,
            'healed_files': 0,
            'organized_files': 0,
            'total_size_bytes': 0,
            'total_duration_seconds': 0,
            'categories': defaultdict(int),
            'sample_rates': defaultdict(int),
            'bit_depths': defaultdict(int),
            'channels': defaultdict(int),
            'errors': [],
            'duplicates': [],
        }
        self.report_path.mkdir(parents=True, exist_ok=True)
        
    def print_header(self, text: str):
        """Print a formatted header."""
        print(f"\n{'='*60}")
        print(f"  {text}")
        print(f"{'='*60}\n")
        
    def print_progress(self, current: int, total: int, prefix: str = ""):
        """Print progress bar."""
        bar_length = 40
        progress = current / total if total > 0 else 0
        filled = int(bar_length * progress)
        bar = '█' * filled + '░' * (bar_length - filled)
        percent = progress * 100
        print(f"\r{prefix} [{bar}] {percent:.1f}% ({current}/{total})", end='', flush=True)
        
    def scan_files(self) -> list:
        """Scan source directory for audio files."""
        self.print_header("SCANNING FOR AUDIO FILES")
        
        audio_extensions = {'.wav', '.aif', '.aiff', '.flac', '.mp3', '.ogg'}
        audio_files = []
        
        print(f"Scanning: {self.source_path}")
        
        for root, dirs, files in os.walk(self.source_path):
            for file in files:
                if Path(file).suffix.lower() in audio_extensions:
                    file_path = Path(root) / file
                    audio_file = AudioFile(str(file_path))
                    audio_files.append(audio_file)
                    
        self.audio_files = audio_files
        self.stats['total_files'] = len(audio_files)
        
        print(f"✓ Found {len(audio_files)} audio files")
        return audio_files
        
    def test_file(self, audio_file: AudioFile) -> AudioFile:
        """Test a single audio file for validity and extract metadata."""
        try:
            audio_file.size = audio_file.path.stat().st_size
            
            if audio_file.extension == '.wav':
                audio_file = self._test_wav(audio_file)
            elif audio_file.extension in ['.aif', '.aiff']:
                audio_file = self._test_aiff(audio_file)
            else:
                # For other formats, just check if file is readable
                audio_file.is_valid = audio_file.size > 0
                if not audio_file.is_valid:
                    audio_file.error_message = "Empty file"
                    
        except Exception as e:
            audio_file.is_valid = False
            audio_file.error_message = str(e)
            
        return audio_file
        
    def _test_wav(self, audio_file: AudioFile) -> AudioFile:
        """Test WAV file integrity."""
        try:
            with wave.open(str(audio_file.path), 'rb') as wav:
                audio_file.sample_rate = wav.getframerate()
                audio_file.channels = wav.getnchannels()
                audio_file.bit_depth = wav.getsampwidth() * 8
                frames = wav.getnframes()
                audio_file.duration = frames / audio_file.sample_rate if audio_file.sample_rate > 0 else 0
                
                # Try to read a sample of the data to verify integrity
                wav.readframes(min(1000, frames))
                
            audio_file.is_valid = True
        except Exception as e:
            audio_file.is_valid = False
            audio_file.error_message = f"WAV Error: {str(e)}"
            
        return audio_file
        
    def _test_aiff(self, audio_file: AudioFile) -> AudioFile:
        """Test AIFF file integrity using basic header parsing."""
        try:
            with open(audio_file.path, 'rb') as f:
                # Read FORM header
                header = f.read(12)
                if len(header) < 12:
                    raise ValueError("File too small for AIFF")
                    
                form_id = header[0:4]
                aiff_id = header[8:12]
                
                if form_id != b'FORM' or aiff_id not in [b'AIFF', b'AIFC']:
                    raise ValueError("Not a valid AIFF file")
                    
                # Parse chunks to find COMM and SSND
                file_size = struct.unpack('>I', header[4:8])[0]
                
                while f.tell() < file_size:
                    chunk_header = f.read(8)
                    if len(chunk_header) < 8:
                        break
                        
                    chunk_id = chunk_header[0:4]
                    chunk_size = struct.unpack('>I', chunk_header[4:8])[0]
                    
                    if chunk_id == b'COMM':
                        comm_data = f.read(min(chunk_size, 18))
                        if len(comm_data) >= 18:
                            audio_file.channels = struct.unpack('>h', comm_data[0:2])[0]
                            num_frames = struct.unpack('>I', comm_data[2:6])[0]
                            audio_file.bit_depth = struct.unpack('>h', comm_data[6:8])[0]
                            # Extended precision for sample rate (simplified)
                            exp = struct.unpack('>H', comm_data[8:10])[0]
                            mant = struct.unpack('>Q', comm_data[10:18])[0]
                            if exp != 0:
                                audio_file.sample_rate = int(mant * (2 ** (exp - 16383 - 63)))
                            audio_file.duration = num_frames / audio_file.sample_rate if audio_file.sample_rate > 0 else 0
                    else:
                        f.seek(chunk_size + (chunk_size % 2), 1)  # Skip chunk + padding
                        
            audio_file.is_valid = True
        except Exception as e:
            audio_file.is_valid = False
            audio_file.error_message = f"AIFF Error: {str(e)}"
            
        return audio_file
        
    def test_all_files(self):
        """Test all scanned audio files."""
        self.print_header("TESTING AUDIO FILES")
        
        total = len(self.audio_files)
        valid = 0
        corrupted = 0
        
        for i, audio_file in enumerate(self.audio_files):
            self.print_progress(i + 1, total, "Testing")
            self.test_file(audio_file)
            
            if audio_file.is_valid:
                valid += 1
                self.stats['total_size_bytes'] += audio_file.size
                self.stats['total_duration_seconds'] += audio_file.duration
                self.stats['sample_rates'][audio_file.sample_rate] += 1
                self.stats['bit_depths'][audio_file.bit_depth] += 1
                self.stats['channels'][audio_file.channels] += 1
            else:
                corrupted += 1
                self.stats['errors'].append({
                    'file': str(audio_file.path),
                    'error': audio_file.error_message
                })
                
        print()  # New line after progress
        
        self.stats['valid_files'] = valid
        self.stats['corrupted_files'] = corrupted
        
        print(f"\n✓ Valid files: {valid}")
        print(f"✗ Corrupted files: {corrupted}")
        
    def deep_scan(self):
        """Perform deep analysis including hash calculation and duplicate detection."""
        self.print_header("DEEP SCANNING AUDIO FILES")
        
        total = len(self.audio_files)
        hash_to_files = defaultdict(list)
        
        for i, audio_file in enumerate(self.audio_files):
            self.print_progress(i + 1, total, "Deep Scanning")
            
            if audio_file.is_valid:
                try:
                    # Calculate MD5 hash
                    md5 = hashlib.md5()
                    with open(audio_file.path, 'rb') as f:
                        for chunk in iter(lambda: f.read(8192), b''):
                            md5.update(chunk)
                    audio_file.md5_hash = md5.hexdigest()
                    hash_to_files[audio_file.md5_hash].append(audio_file)
                except Exception as e:
                    pass
                    
        print()  # New line after progress
        
        # Find duplicates
        for hash_val, files in hash_to_files.items():
            if len(files) > 1:
                self.stats['duplicates'].append({
                    'hash': hash_val,
                    'files': [str(f.path) for f in files],
                    'count': len(files)
                })
                
        print(f"✓ Deep scan complete")
        print(f"  Duplicates found: {len(self.stats['duplicates'])} groups")
        
    def analyze_and_categorize(self):
        """Analyze file paths and categorize based on naming conventions."""
        self.print_header("ANALYZING & CATEGORIZING FILES")
        
        for audio_file in self.audio_files:
            if not audio_file.is_valid:
                continue
                
            # Parse path components
            rel_path = audio_file.path.relative_to(self.source_path)
            path_parts = [p.lower() for p in rel_path.parts]
            filename_lower = audio_file.filename.lower()
            
            # Extract kit name (usually first directory after source)
            if len(path_parts) > 1:
                kit_part = path_parts[1] if path_parts[0] == 'audio' else path_parts[0]
                audio_file.kit_name = kit_part.replace('dlx_', 'DLX_').replace('_', ' ').title()
                
            # Determine category
            all_text = ' '.join(path_parts + [filename_lower])
            
            for keyword, category in CATEGORY_MAPPING.items():
                if keyword in all_text:
                    audio_file.category = category
                    break
                    
            # Determine articulation
            for keyword, articulation in ARTICULATION_MAPPING.items():
                if keyword in all_text:
                    audio_file.articulation = articulation
                    break
                    
            # Extract velocity layer from filename (e.g., MASTER127, V75)
            vel_match = re.search(r'(?:master|v)(\d+)', filename_lower)
            if vel_match:
                vel = int(vel_match.group(1))
                if vel <= 127:
                    audio_file.velocity_layer = f"V{vel:03d}"
                    
            # Generate new filename
            parts = []
            if audio_file.kit_name:
                parts.append(audio_file.kit_name.replace(' ', '_'))
            if audio_file.category != 'Uncategorized':
                parts.append(audio_file.category.rstrip('s'))  # Singular form
            if audio_file.articulation:
                parts.append(audio_file.articulation)
            if audio_file.velocity_layer:
                parts.append(audio_file.velocity_layer)
                
            if parts:
                base_name = '_'.join(parts)
                audio_file.new_filename = f"{base_name}{audio_file.extension}"
            else:
                audio_file.new_filename = audio_file.filename
                
            self.stats['categories'][audio_file.category] += 1
            
        print("✓ Categorization complete")
        print("\nCategory Distribution:")
        for cat, count in sorted(self.stats['categories'].items(), key=lambda x: -x[1]):
            print(f"  {cat}: {count} files")
            
    def heal_files(self):
        """Attempt to heal/repair corrupted files."""
        self.print_header("ATTEMPTING TO HEAL CORRUPTED FILES")
        
        corrupted = [f for f in self.audio_files if not f.is_valid]
        
        if not corrupted:
            print("✓ No corrupted files to heal")
            return
            
        healed = 0
        
        for audio_file in corrupted:
            print(f"\nAttempting to heal: {audio_file.filename}")
            print(f"  Error: {audio_file.error_message}")
            
            # Try using ffmpeg to repair if available
            try:
                result = subprocess.run(
                    ['which', 'ffmpeg'], 
                    capture_output=True, 
                    text=True
                )
                
                if result.returncode == 0:
                    temp_path = audio_file.path.with_suffix('.repaired' + audio_file.extension)
                    
                    repair_result = subprocess.run([
                        'ffmpeg', '-y', '-i', str(audio_file.path),
                        '-acodec', 'pcm_s16le' if audio_file.extension == '.wav' else 'pcm_s16be',
                        str(temp_path)
                    ], capture_output=True, text=True, timeout=30)
                    
                    if repair_result.returncode == 0 and temp_path.exists():
                        # Verify the repaired file
                        test_audio = AudioFile(str(temp_path))
                        self.test_file(test_audio)
                        
                        if test_audio.is_valid:
                            # Backup original and replace
                            backup_path = audio_file.path.with_suffix('.backup' + audio_file.extension)
                            shutil.move(str(audio_file.path), str(backup_path))
                            shutil.move(str(temp_path), str(audio_file.path))
                            
                            audio_file.is_valid = True
                            audio_file.error_message = ""
                            healed += 1
                            print(f"  ✓ Healed successfully")
                        else:
                            temp_path.unlink()
                            print(f"  ✗ Repair failed - file still invalid")
                    else:
                        if temp_path.exists():
                            temp_path.unlink()
                        print(f"  ✗ FFmpeg repair failed")
                else:
                    print(f"  ⚠ FFmpeg not available for repair")
                    
            except subprocess.TimeoutExpired:
                print(f"  ✗ Repair timed out")
            except Exception as e:
                print(f"  ✗ Repair error: {str(e)}")
                
        self.stats['healed_files'] = healed
        print(f"\n✓ Healed {healed} of {len(corrupted)} corrupted files")
        
    def optimize_structure(self):
        """Optimize the library structure - preview the reorganization."""
        self.print_header("OPTIMIZATION PREVIEW")
        
        # Group files by target category
        category_files = defaultdict(list)
        
        for audio_file in self.audio_files:
            if audio_file.is_valid:
                category_files[audio_file.category].append(audio_file)
                
        print("Proposed Directory Structure:")
        print(f"\n{self.target_path}/")
        print("├── Samples/")
        print("│   └── FXpansion_BFD/")
        
        for category, files in sorted(category_files.items()):
            print(f"│       ├── {category}/ ({len(files)} files)")
            
            # Group by kit
            kit_files = defaultdict(list)
            for f in files:
                kit_files[f.kit_name or 'Unknown'].append(f)
                
            for kit, kit_file_list in sorted(kit_files.items()):
                print(f"│       │   └── {kit}/ ({len(kit_file_list)} files)")
                
        # Calculate optimization stats
        total_size_mb = self.stats['total_size_bytes'] / (1024 * 1024)
        total_duration_min = self.stats['total_duration_seconds'] / 60
        
        print(f"\nOptimization Statistics:")
        print(f"  Total size: {total_size_mb:.2f} MB")
        print(f"  Total duration: {total_duration_min:.2f} minutes")
        print(f"  Unique samples: {self.stats['valid_files'] - len(self.stats['duplicates'])}")
        print(f"  Duplicate groups: {len(self.stats['duplicates'])}")
        
    def reorganize(self, dry_run: bool = True):
        """Reorganize files into the master drum library."""
        self.print_header(f"REORGANIZING FILES {'(DRY RUN)' if dry_run else ''}")
        
        target_base = self.target_path / "Samples" / "FXpansion_BFD"
        
        total = len([f for f in self.audio_files if f.is_valid])
        organized = 0
        
        for i, audio_file in enumerate([f for f in self.audio_files if f.is_valid]):
            self.print_progress(i + 1, total, "Reorganizing")
            
            # Determine target path
            category_dir = target_base / audio_file.category
            if audio_file.kit_name:
                category_dir = category_dir / audio_file.kit_name.replace(' ', '_')
                
            target_file = category_dir / audio_file.new_filename
            
            # Handle duplicates by adding number suffix
            counter = 1
            original_target = target_file
            while target_file.exists():
                stem = original_target.stem
                target_file = original_target.with_name(f"{stem}_{counter:03d}{original_target.suffix}")
                counter += 1
                
            if dry_run:
                # Just track what would be done
                organized += 1
            else:
                try:
                    # Create directory if needed
                    category_dir.mkdir(parents=True, exist_ok=True)
                    
                    # Copy file (preserve original)
                    shutil.copy2(str(audio_file.path), str(target_file))
                    organized += 1
                except Exception as e:
                    self.stats['errors'].append({
                        'file': str(audio_file.path),
                        'error': f"Copy failed: {str(e)}"
                    })
                    
        print()  # New line after progress
        
        self.stats['organized_files'] = organized
        
        if dry_run:
            print(f"\n✓ Would organize {organized} files")
            print("  Run with --execute to perform actual reorganization")
        else:
            print(f"\n✓ Organized {organized} files")
            
    def generate_report(self):
        """Generate comprehensive report."""
        self.print_header("GENERATING REPORT")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # JSON report
        json_report = {
            'timestamp': timestamp,
            'source_path': str(self.source_path),
            'target_path': str(self.target_path),
            'statistics': {
                'total_files': self.stats['total_files'],
                'valid_files': self.stats['valid_files'],
                'corrupted_files': self.stats['corrupted_files'],
                'healed_files': self.stats['healed_files'],
                'organized_files': self.stats['organized_files'],
                'total_size_mb': round(self.stats['total_size_bytes'] / (1024 * 1024), 2),
                'total_duration_minutes': round(self.stats['total_duration_seconds'] / 60, 2),
                'categories': dict(self.stats['categories']),
                'sample_rates': dict(self.stats['sample_rates']),
                'bit_depths': dict(self.stats['bit_depths']),
                'channels': dict(self.stats['channels']),
            },
            'errors': self.stats['errors'],
            'duplicates': self.stats['duplicates'],
            'files': [f.to_dict() for f in self.audio_files],
        }
        
        json_path = self.report_path / f"fxpansion_report_{timestamp}.json"
        with open(json_path, 'w') as f:
            json.dump(json_report, f, indent=2)
            
        # Text summary report
        summary_path = self.report_path / f"fxpansion_summary_{timestamp}.txt"
        with open(summary_path, 'w') as f:
            f.write("=" * 60 + "\n")
            f.write("  FXpansion Drum Library Manager Report\n")
            f.write("=" * 60 + "\n\n")
            
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Source: {self.source_path}\n")
            f.write(f"Target: {self.target_path}\n\n")
            
            f.write("-" * 40 + "\n")
            f.write("  STATISTICS\n")
            f.write("-" * 40 + "\n")
            f.write(f"Total files scanned: {self.stats['total_files']}\n")
            f.write(f"Valid files: {self.stats['valid_files']}\n")
            f.write(f"Corrupted files: {self.stats['corrupted_files']}\n")
            f.write(f"Healed files: {self.stats['healed_files']}\n")
            f.write(f"Total size: {self.stats['total_size_bytes'] / (1024*1024):.2f} MB\n")
            f.write(f"Total duration: {self.stats['total_duration_seconds'] / 60:.2f} minutes\n\n")
            
            f.write("-" * 40 + "\n")
            f.write("  CATEGORIES\n")
            f.write("-" * 40 + "\n")
            for cat, count in sorted(self.stats['categories'].items(), key=lambda x: -x[1]):
                f.write(f"{cat}: {count} files\n")
            f.write("\n")
            
            f.write("-" * 40 + "\n")
            f.write("  AUDIO SPECIFICATIONS\n")
            f.write("-" * 40 + "\n")
            f.write("Sample Rates:\n")
            for rate, count in sorted(self.stats['sample_rates'].items()):
                f.write(f"  {rate} Hz: {count} files\n")
            f.write("\nBit Depths:\n")
            for depth, count in sorted(self.stats['bit_depths'].items()):
                f.write(f"  {depth}-bit: {count} files\n")
            f.write("\nChannels:\n")
            for ch, count in sorted(self.stats['channels'].items()):
                f.write(f"  {ch} channel(s): {count} files\n")
            f.write("\n")
            
            if self.stats['duplicates']:
                f.write("-" * 40 + "\n")
                f.write("  DUPLICATES FOUND\n")
                f.write("-" * 40 + "\n")
                for dup in self.stats['duplicates'][:20]:  # First 20
                    f.write(f"\nDuplicate group ({dup['count']} files):\n")
                    for filepath in dup['files'][:5]:  # First 5 of each
                        f.write(f"  - {filepath}\n")
                    if len(dup['files']) > 5:
                        f.write(f"  ... and {len(dup['files']) - 5} more\n")
                f.write("\n")
                
            if self.stats['errors']:
                f.write("-" * 40 + "\n")
                f.write("  ERRORS\n")
                f.write("-" * 40 + "\n")
                for err in self.stats['errors'][:50]:  # First 50
                    f.write(f"\n{err['file']}:\n")
                    f.write(f"  {err['error']}\n")
                f.write("\n")
                
        print(f"✓ Reports generated:")
        print(f"  JSON: {json_path}")
        print(f"  Summary: {summary_path}")
        
        return json_path, summary_path


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description='FXpansion Drum Library Manager')
    parser.add_argument('--source', default=FXPANSION_SOURCE,
                        help='Source FXpansion directory')
    parser.add_argument('--target', default=MASTER_DRUM_LIBRARY,
                        help='Target master drum library')
    parser.add_argument('--report', default=REPORT_OUTPUT,
                        help='Report output directory')
    parser.add_argument('--execute', action='store_true',
                        help='Execute reorganization (default is dry-run)')
    parser.add_argument('--skip-deep-scan', action='store_true',
                        help='Skip deep scan (faster but no duplicate detection)')
    parser.add_argument('--skip-heal', action='store_true',
                        help='Skip healing corrupted files')
    parser.add_argument('--skip-reorganize', action='store_true',
                        help='Skip reorganization step')
    
    args = parser.parse_args()
    
    # Verify paths exist
    if not Path(args.source).exists():
        print(f"Error: Source path does not exist: {args.source}")
        sys.exit(1)
        
    if not Path(args.target).exists():
        print(f"Error: Target path does not exist: {args.target}")
        sys.exit(1)
        
    print("""
╔══════════════════════════════════════════════════════════════╗
║         FXpansion Drum Library Manager v1.0                  ║
║     Test • Scan • Heal • Optimize • Deep Scan • Reorganize   ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    manager = DrumLibraryManager(args.source, args.target, args.report)
    
    # 1. Scan for audio files
    manager.scan_files()
    
    # 2. Test all files
    manager.test_all_files()
    
    # 3. Deep scan (optional)
    if not args.skip_deep_scan:
        manager.deep_scan()
    
    # 4. Analyze and categorize
    manager.analyze_and_categorize()
    
    # 5. Heal corrupted files (optional)
    if not args.skip_heal:
        manager.heal_files()
    
    # 6. Optimize structure preview
    manager.optimize_structure()
    
    # 7. Reorganize (dry-run by default)
    if not args.skip_reorganize:
        manager.reorganize(dry_run=not args.execute)
    
    # 8. Generate report
    manager.generate_report()
    
    print("""
╔══════════════════════════════════════════════════════════════╗
║                    PROCESS COMPLETE                          ║
╚══════════════════════════════════════════════════════════════╝
    """)


if __name__ == '__main__':
    main()
