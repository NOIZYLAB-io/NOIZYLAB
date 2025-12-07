#!/usr/bin/env python3
"""
🎵 ULTIMATE WAV ORGANIZER 🎵

⭐⭐⭐ HARD RULE ⭐⭐⭐
ANY FILE WITHOUT METADATA = YOUR ORIGINAL COMPOSITION!

Features:
- Scans all WAV metadata
- Identifies YOUR original compositions (no metadata)
- Organizes commercial samples by source
- Restores original filenames from metadata
- Validates file integrity
- Creates detailed inventory report
- Generates backup list
"""

import os
import struct
import shutil
import json
import hashlib
from pathlib import Path
from collections import defaultdict
from datetime import datetime

# ============================================================================
# CONFIGURATION
# ============================================================================

SOURCE_DIR = Path("WAVES TO MOVE")
DEST_DIR = Path("ORGANIZED_WAVES")
ORIGINALS_DIR = DEST_DIR / "ORIGINAL_COMPOSITIONS"
COMMERCIAL_DIR = DEST_DIR / "COMMERCIAL_SAMPLES"
REPORTS_DIR = Path("ORGANIZATION_REPORTS")

# ============================================================================
# METADATA EXTRACTION
# ============================================================================

def read_chunk(f):
    """Read a RIFF chunk header"""
    chunk_id = f.read(4)
    if len(chunk_id) < 4:
        return None, 0
    chunk_size = struct.unpack('<I', f.read(4))[0]
    return chunk_id, chunk_size

def extract_wav_metadata(filepath):
    """Extract all metadata from WAV file"""
    metadata = {
        'filename': filepath.name,
        'path': str(filepath),
        'size': filepath.stat().st_size,
        'has_metadata': False,
        'info': {},
        'product': None,
        'software': None,
        'originator': None,
        'original_name': None,
        'title': None,
        'artist': None,
        'comment': None,
        'sample_rate': None,
        'channels': None,
        'bits_per_sample': None,
        'duration_seconds': None
    }
    
    try:
        with open(filepath, 'rb') as f:
            # Verify RIFF/WAVE
            riff = f.read(4)
            if riff != b'RIFF':
                metadata['error'] = 'Not a valid RIFF file'
                return metadata
            
            file_size = struct.unpack('<I', f.read(4))[0]
            wave = f.read(4)
            if wave != b'WAVE':
                metadata['error'] = 'Not a valid WAVE file'
                return metadata
            
            metadata['valid_wav'] = True
            data_size = 0
            
            # Read all chunks
            while True:
                chunk_id, chunk_size = read_chunk(f)
                if chunk_id is None:
                    break
                
                chunk_data = f.read(chunk_size)
                
                # Format chunk
                if chunk_id == b'fmt ':
                    if len(chunk_data) >= 16:
                        audio_format, channels, sample_rate, byte_rate, block_align, bits_per_sample = struct.unpack('<HHIIHH', chunk_data[:16])
                        metadata['sample_rate'] = sample_rate
                        metadata['channels'] = channels
                        metadata['bits_per_sample'] = bits_per_sample
                        metadata['audio_format'] = audio_format
                
                # Data chunk
                elif chunk_id == b'data':
                    data_size = chunk_size
                    if metadata['sample_rate'] and metadata['channels'] and metadata['bits_per_sample']:
                        bytes_per_second = metadata['sample_rate'] * metadata['channels'] * (metadata['bits_per_sample'] // 8)
                        if bytes_per_second > 0:
                            metadata['duration_seconds'] = data_size / bytes_per_second
                
                # LIST/INFO chunk
                elif chunk_id == b'LIST':
                    list_type = chunk_data[:4]
                    if list_type == b'INFO':
                        metadata['has_metadata'] = True
                        pos = 4
                        while pos < len(chunk_data) - 8:
                            try:
                                info_id = chunk_data[pos:pos+4]
                                info_size = struct.unpack('<I', chunk_data[pos+4:pos+8])[0]
                                info_data = chunk_data[pos+8:pos+8+info_size]
                                info_name = info_id.decode('ascii', errors='ignore')
                                info_value = info_data.decode('utf-8', errors='ignore').rstrip('\x00')
                                
                                if info_value.strip():
                                    metadata['info'][info_name] = info_value
                                    
                                    # Extract key identifiers
                                    if info_name == 'ISFT':
                                        metadata['software'] = info_value.strip()
                                    elif info_name == 'IPRD':
                                        metadata['product'] = info_value.strip()
                                    elif info_name == 'INAM':
                                        metadata['original_name'] = info_value.strip()
                                    elif info_name == 'TITL':
                                        metadata['title'] = info_value.strip()
                                    elif info_name == 'IART':
                                        metadata['artist'] = info_value.strip()
                                    elif info_name == 'ICMT':
                                        metadata['comment'] = info_value.strip()
                                
                                pos += 8 + info_size
                                if info_size % 2:
                                    pos += 1
                            except:
                                break
                
                # Broadcast Wave Format extension
                elif chunk_id == b'bext':
                    metadata['has_metadata'] = True
                    try:
                        description = chunk_data[0:256].decode('ascii', errors='ignore').rstrip('\x00')
                        originator = chunk_data[256:288].decode('ascii', errors='ignore').rstrip('\x00')
                        if originator.strip():
                            metadata['originator'] = originator.strip()
                        if description.strip():
                            metadata['description'] = description.strip()
                    except:
                        pass
                
                # Skip padding
                if chunk_size % 2:
                    f.read(1)
    
    except Exception as e:
        metadata['error'] = str(e)
    
    return metadata

def categorize_by_filename(filename):
    """Categorize by filename patterns"""
    name = filename.lower()
    
    patterns = {
        'Ensoniq_Mirage': ['mirage'],
        'Kawaii_Synth': ['kawaii'],
        'Yamaha_DX100': ['dx100', 'dx-100'],
        'Indian_World_Percussion': ['manjira', 'dholak', 'dimdi', 'clay pot', 'kete', 'pora'],
        'Roland_System100': ['sys100', 'system100', 'system 100'],
        'Roland_SH5': ['sh5', 'sh-5'],
        'Storm_Season_FX': ['stormseasonfx', 'storm season'],
        'Ambient_Sound_Design': ['ambient'],
        'Sound_Effects_Hits': ['hit'],
        'Beats_And_Loops': ['bpm', 'beat', 'loop']
    }
    
    for category, keywords in patterns.items():
        if any(keyword in name for keyword in keywords):
            return f'Commercial_Samples/{category}'
    
    return None

# ============================================================================
# FILE VALIDATION
# ============================================================================

def validate_wav_file(filepath):
    """Validate WAV file integrity"""
    issues = []
    
    try:
        metadata = extract_wav_metadata(filepath)
        
        if 'error' in metadata:
            issues.append(f"Error: {metadata['error']}")
        
        if not metadata.get('valid_wav'):
            issues.append("Invalid WAV format")
        
        if metadata.get('size', 0) < 1000:
            issues.append("File too small (possibly corrupt)")
        
        if not metadata.get('sample_rate'):
            issues.append("Missing sample rate")
        
        if not metadata.get('channels'):
            issues.append("Missing channel info")
        
        return len(issues) == 0, issues, metadata
    
    except Exception as e:
        return False, [f"Validation error: {str(e)}"], None

# ============================================================================
# FILE ORGANIZATION
# ============================================================================

def organize_files(source_dir, dest_base):
    """Main organization logic"""
    source_dir = Path(source_dir)
    dest_base = Path(dest_base)
    
    stats = {
        'originals': [],
        'commercial': [],
        'errors': [],
        'invalid': [],
        'start_time': datetime.now().isoformat(),
        'total_files': 0,
        'total_size': 0
    }
    
    # Get all WAV files
    print("🔍 Scanning for WAV files...")
    wav_files = list(source_dir.rglob('*.wav')) + list(source_dir.rglob('*.WAV'))
    stats['total_files'] = len(wav_files)
    
    print(f"Found {len(wav_files)} WAV files")
    print("\n" + "="*80)
    print("⭐⭐⭐ HARD RULE ACTIVE ⭐⭐⭐")
    print("NO METADATA = YOUR ORIGINAL COMPOSITION!")
    print("="*80 + "\n")
    
    print("Processing files...\n")
    
    for i, wav_file in enumerate(wav_files, 1):
        if i % 10 == 0 or i == 1:
            print(f"  [{i}/{len(wav_files)}] Processing...")
        
        try:
            # Validate file
            is_valid, issues, metadata = validate_wav_file(wav_file)
            
            if not is_valid:
                stats['invalid'].append({
                    'file': wav_file.name,
                    'path': str(wav_file),
                    'issues': issues
                })
                print(f"  ⚠️  INVALID: {wav_file.name}")
                continue
            
            stats['total_size'] += metadata['size']
            
            # Determine category
            filename_category = categorize_by_filename(wav_file.name)
            
            if metadata['has_metadata'] or filename_category:
                # COMMERCIAL SAMPLE
                category = 'commercial'
                
                if filename_category:
                    dest_folder = dest_base / filename_category
                elif metadata['product']:
                    dest_folder = COMMERCIAL_DIR / metadata['product'].replace('/', '_')
                elif metadata['software']:
                    dest_folder = COMMERCIAL_DIR / metadata['software'].replace('/', '_')
                elif metadata['originator']:
                    dest_folder = COMMERCIAL_DIR / metadata['originator'].replace('/', '_')
                else:
                    dest_folder = COMMERCIAL_DIR / "Other_With_Metadata"
                
                stats['commercial'].append({
                    'original_file': wav_file.name,
                    'original_path': str(wav_file.relative_to(source_dir)),
                    'dest_folder': str(dest_folder.relative_to(dest_base)),
                    'size': metadata['size'],
                    'duration': metadata.get('duration_seconds'),
                    'metadata': metadata['info']
                })
            
            else:
                # ⭐⭐⭐ ORIGINAL COMPOSITION! ⭐⭐⭐
                category = 'original'
                
                # Preserve folder structure for originals
                relative_path = wav_file.relative_to(source_dir)
                if len(relative_path.parts) > 1:
                    dest_folder = ORIGINALS_DIR / relative_path.parent
                else:
                    dest_folder = ORIGINALS_DIR
                
                stats['originals'].append({
                    'original_file': wav_file.name,
                    'original_path': str(relative_path),
                    'size': metadata['size'],
                    'duration': metadata.get('duration_seconds'),
                    'sample_rate': metadata.get('sample_rate'),
                    'channels': metadata.get('channels'),
                    'bits': metadata.get('bits_per_sample')
                })
                
                print(f"  ⭐ ORIGINAL: {wav_file.name}")
            
            # Create destination folder
            dest_folder.mkdir(parents=True, exist_ok=True)
            
            # Determine final filename
            dest_filename = wav_file.name
            
            if metadata['original_name']:
                clean_name = metadata['original_name'].replace('/', '_').replace('\\', '_')
                dest_filename = f"{clean_name}.wav"
            elif metadata['title']:
                clean_name = metadata['title'].replace('/', '_').replace('\\', '_')
                dest_filename = f"{clean_name}.wav"
            
            # Copy file
            dest_file = dest_folder / dest_filename
            
            # Handle duplicates
            counter = 1
            original_dest = dest_file
            while dest_file.exists():
                dest_file = dest_file.parent / f"{original_dest.stem}_{counter}{original_dest.suffix}"
                counter += 1
            
            shutil.copy2(wav_file, dest_file)
            
            # Track renames
            if dest_filename != wav_file.name:
                if category == 'commercial':
                    stats['commercial'][-1]['new_name'] = dest_filename
                elif category == 'original':
                    stats['originals'][-1]['new_name'] = dest_filename
        
        except Exception as e:
            print(f"  ❌ ERROR: {wav_file.name}: {str(e)}")
            stats['errors'].append({
                'file': wav_file.name,
                'error': str(e)
            })
    
    stats['end_time'] = datetime.now().isoformat()
    return stats

# ============================================================================
# REPORTING
# ============================================================================

def generate_reports(stats):
    """Generate comprehensive reports"""
    REPORTS_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # JSON report
    json_file = REPORTS_DIR / f"organization_report_{timestamp}.json"
    with open(json_file, 'w') as f:
        json.dump(stats, f, indent=2)
    
    # Text report
    txt_file = REPORTS_DIR / f"organization_report_{timestamp}.txt"
    with open(txt_file, 'w') as f:
        f.write("="*80 + "\n")
        f.write("WAV FILE ORGANIZATION REPORT\n")
        f.write("="*80 + "\n\n")
        
        f.write(f"Start Time: {stats['start_time']}\n")
        f.write(f"End Time: {stats['end_time']}\n\n")
        
        f.write("⭐⭐⭐ HARD RULE APPLIED ⭐⭐⭐\n")
        f.write("NO METADATA = ORIGINAL COMPOSITION!\n\n")
        
        f.write("="*80 + "\n")
        f.write(f"ORIGINAL COMPOSITIONS: {len(stats['originals'])} files ⭐⭐⭐\n")
        f.write("="*80 + "\n\n")
        
        for item in sorted(stats['originals'], key=lambda x: x['original_file']):
            f.write(f"  ⭐ {item['original_file']}\n")
            f.write(f"     Path: {item['original_path']}\n")
            f.write(f"     Size: {item['size']:,} bytes\n")
            if item.get('duration'):
                f.write(f"     Duration: {item['duration']:.2f} seconds\n")
            if item.get('new_name'):
                f.write(f"     Renamed to: {item['new_name']}\n")
            f.write("\n")
        
        f.write("\n" + "="*80 + "\n")
        f.write(f"COMMERCIAL SAMPLES: {len(stats['commercial'])} files\n")
        f.write("="*80 + "\n\n")
        
        by_folder = defaultdict(list)
        for item in stats['commercial']:
            by_folder[item['dest_folder']].append(item)
        
        for folder, items in sorted(by_folder.items()):
            f.write(f"\n{folder}/ ({len(items)} files)\n")
            for item in sorted(items, key=lambda x: x['original_file'])[:10]:
                f.write(f"  • {item['original_file']}\n")
                if item.get('new_name'):
                    f.write(f"    → {item['new_name']}\n")
            if len(items) > 10:
                f.write(f"  ... and {len(items) - 10} more\n")
        
        if stats['invalid']:
            f.write("\n" + "="*80 + "\n")
            f.write(f"INVALID FILES: {len(stats['invalid'])}\n")
            f.write("="*80 + "\n\n")
            for item in stats['invalid']:
                f.write(f"  ⚠️  {item['file']}\n")
                for issue in item['issues']:
                    f.write(f"      - {issue}\n")
        
        if stats['errors']:
            f.write("\n" + "="*80 + "\n")
            f.write(f"ERRORS: {len(stats['errors'])}\n")
            f.write("="*80 + "\n\n")
            for item in stats['errors']:
                f.write(f"  ❌ {item['file']}: {item['error']}\n")
        
        f.write("\n" + "="*80 + "\n")
        f.write("SUMMARY\n")
        f.write("="*80 + "\n")
        f.write(f"Total files processed: {stats['total_files']}\n")
        f.write(f"Total size: {stats['total_size'] / (1024**3):.2f} GB\n")
        f.write(f"⭐ Original compositions: {len(stats['originals'])} files\n")
        f.write(f"📦 Commercial samples: {len(stats['commercial'])} files\n")
        f.write(f"⚠️  Invalid files: {len(stats['invalid'])} files\n")
        f.write(f"❌ Errors: {len(stats['errors'])} files\n")
        f.write("="*80 + "\n")
    
    # Backup list for originals
    backup_file = REPORTS_DIR / f"BACKUP_LIST_ORIGINALS_{timestamp}.txt"
    with open(backup_file, 'w') as f:
        f.write("⭐⭐⭐ ORIGINAL COMPOSITIONS - PRIORITY BACKUP LIST ⭐⭐⭐\n\n")
        f.write("These files have NO metadata and are YOUR original compositions!\n")
        f.write("BACK THESE UP IMMEDIATELY - They are irreplaceable!\n\n")
        f.write("="*80 + "\n\n")
        
        for item in sorted(stats['originals'], key=lambda x: x['original_file']):
            f.write(f"{item['original_path']}\n")
    
    return json_file, txt_file, backup_file

def print_console_report(stats):
    """Print summary to console"""
    print("\n" + "="*80)
    print("✓ ORGANIZATION COMPLETE!")
    print("="*80 + "\n")
    
    print("⭐⭐⭐ HARD RULE APPLIED ⭐⭐⭐")
    print("Files WITHOUT metadata = YOUR ORIGINAL COMPOSITIONS")
    print("")
    
    total_orig_size = sum(item['size'] for item in stats['originals'])
    total_comm_size = sum(item['size'] for item in stats['commercial'])
    
    print(f"🎵 ORIGINAL COMPOSITIONS: {len(stats['originals'])} files ({total_orig_size/(1024**2):.1f} MB) ⭐⭐⭐")
    print(f"📦 Commercial Samples: {len(stats['commercial'])} files ({total_comm_size/(1024**2):.1f} MB)")
    if stats['invalid']:
        print(f"⚠️  Invalid Files: {len(stats['invalid'])} files")
    if stats['errors']:
        print(f"❌ Errors: {len(stats['errors'])} files")
    
    print("\n" + "="*80)
    print("FILES ORGANIZED INTO:")
    print("="*80)
    print(f"  {ORIGINALS_DIR}/")
    print(f"    → {len(stats['originals'])} original compositions ⭐")
    print(f"\n  {COMMERCIAL_DIR}/")
    
    by_folder = defaultdict(int)
    for item in stats['commercial']:
        by_folder[item['dest_folder']] += 1
    
    for folder, count in sorted(by_folder.items()):
        print(f"    → {folder.replace('Commercial_Samples/', '')}: {count} files")
    
    print("\n" + "="*80)

# ============================================================================
# MAIN
# ============================================================================

def main():
    print("="*80)
    print("🎵 ULTIMATE WAV ORGANIZER 🎵")
    print("="*80)
    print("\n⭐⭐⭐ HARD RULE ⭐⭐⭐")
    print("ANY FILE WITHOUT METADATA = YOUR ORIGINAL COMPOSITION!")
    print("\nThese are YOUR irreplaceable music files!")
    print("Commercial samples can be re-downloaded, but your originals cannot!")
    print("="*80 + "\n")
    
    if not SOURCE_DIR.exists():
        print(f"❌ Error: Source directory not found: {SOURCE_DIR}")
        return
    
    print(f"Source: {SOURCE_DIR.absolute()}")
    print(f"Destination: {DEST_DIR.absolute()}")
    print(f"Reports: {REPORTS_DIR.absolute()}")
    print("\nStarting organization...\n")
    
    # Run organization
    stats = organize_files(SOURCE_DIR, DEST_DIR)
    
    # Generate reports
    print("\n📊 Generating reports...")
    json_file, txt_file, backup_file = generate_reports(stats)
    
    # Print summary
    print_console_report(stats)
    
    print("\n📄 REPORTS GENERATED:")
    print(f"  • {json_file}")
    print(f"  • {txt_file}")
    print(f"  • {backup_file} ⭐ BACKUP THIS LIST!")
    
    print("\n" + "="*80)
    print("⭐ NEXT STEPS:")
    print("="*80)
    print(f"1. Check {ORIGINALS_DIR}/ for YOUR original compositions ⭐⭐⭐")
    print(f"2. BACKUP these files immediately - they're irreplaceable!")
    print(f"3. Review {txt_file}")
    print(f"4. Commercial samples in {COMMERCIAL_DIR}/ can be deleted if needed")
    print("="*80 + "\n")

if __name__ == '__main__':
    main()

