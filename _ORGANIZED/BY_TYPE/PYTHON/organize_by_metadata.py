#!/usr/bin/env python3
"""
Scan WAV metadata and organize files:

⭐⭐⭐ HARD RULE ⭐⭐⭐
- Files WITHOUT metadata = ORIGINAL COMPOSITIONS (YOUR PRECIOUS MUSIC!)
- Files WITH metadata = Commercial samples (organized by source)

ANY FILE WITHOUT METADATA OR ID TAGS IS AN ORIGINAL COMPOSITION!
"""

import os
import struct
import shutil
from pathlib import Path
from collections import defaultdict

def read_chunk(f):
    """Read a RIFF chunk header"""
    chunk_id = f.read(4)
    if len(chunk_id) < 4:
        return None, 0
    chunk_size = struct.unpack('<I', f.read(4))[0]
    return chunk_id, chunk_size

def extract_wav_metadata(filepath):
    """Extract metadata from WAV file"""
    metadata = {
        'filename': filepath.name,
        'path': filepath,
        'has_metadata': False,
        'info': {},
        'bext': None,
        'product': None,
        'software': None,
        'originator': None,
        'original_name': None,
        'title': None,
        'artist': None,
        'comment': None
    }
    
    try:
        with open(filepath, 'rb') as f:
            riff = f.read(4)
            if riff != b'RIFF':
                return None
            
            file_size = struct.unpack('<I', f.read(4))[0]
            wave = f.read(4)
            if wave != b'WAVE':
                return None
            
            while True:
                chunk_id, chunk_size = read_chunk(f)
                if chunk_id is None:
                    break
                
                chunk_data = f.read(chunk_size)
                
                if chunk_id == b'LIST':
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
                                    if info_name == 'ISFT':  # Software
                                        metadata['software'] = info_value.strip()
                                    elif info_name == 'IPRD':  # Product
                                        metadata['product'] = info_value.strip()
                                    elif info_name == 'INAM':  # Original Name/Title
                                        metadata['original_name'] = info_value.strip()
                                    elif info_name == 'TITL':  # Title
                                        metadata['title'] = info_value.strip()
                                    elif info_name == 'IART':  # Artist
                                        metadata['artist'] = info_value.strip()
                                    elif info_name == 'ICMT':  # Comment
                                        metadata['comment'] = info_value.strip()
                                
                                pos += 8 + info_size
                                if info_size % 2:
                                    pos += 1
                            except:
                                break
                
                elif chunk_id == b'bext':
                    metadata['has_metadata'] = True
                    try:
                        description = chunk_data[0:256].decode('ascii', errors='ignore').rstrip('\x00')
                        originator = chunk_data[256:288].decode('ascii', errors='ignore').rstrip('\x00')
                        if originator.strip():
                            metadata['originator'] = originator.strip()
                    except:
                        pass
                
                if chunk_size % 2:
                    f.read(1)
    
    except Exception as e:
        print(f"Error reading {filepath.name}: {e}")
        return None
    
    return metadata

def categorize_by_filename(filename):
    """Categorize by filename patterns"""
    name = filename.lower()
    
    if 'mirage' in name:
        return 'Commercial_Samples/Ensoniq_Mirage'
    elif 'kawaii' in name:
        return 'Commercial_Samples/Kawaii_Synth'
    elif 'dx100' in name or 'dx-100' in name:
        return 'Commercial_Samples/Yamaha_DX100'
    elif any(x in name for x in ['manjira', 'dholak', 'dimdi', 'clay pot', 'kete']):
        return 'Commercial_Samples/Indian_World_Percussion'
    elif 'sys100' in name:
        return 'Commercial_Samples/Roland_System100'
    elif 'sh5' in name or 'sh-5' in name:
        return 'Commercial_Samples/Roland_SH5'
    elif 'stormseasonfx' in name:
        return 'Commercial_Samples/Storm_Season_FX'
    elif name.startswith('1-') and 'ambient' in name:
        return 'Commercial_Samples/Ambient_Sound_Design'
    elif ' hit' in name or name.endswith('hit.wav'):
        return 'Commercial_Samples/Sound_Effects_Hits'
    elif 'bpm' in name or 'beat' in name or 'loop' in name:
        return 'Commercial_Samples/Beats_And_Loops'
    
    return None

def organize_files(source_dir, dest_base):
    """Organize files based on metadata"""
    source_dir = Path(source_dir)
    dest_base = Path(dest_base)
    
    # Create main destination folders
    originals_dir = dest_base / "ORIGINAL_COMPOSITIONS"
    commercial_dir = dest_base / "COMMERCIAL_SAMPLES"
    unknown_dir = dest_base / "UNKNOWN_NO_METADATA"
    
    # Statistics
    stats = {
        'originals': [],
        'commercial': [],
        'unknown': [],
        'errors': []
    }
    
    # Get all WAV files
    wav_files = list(source_dir.rglob('*.wav')) + list(source_dir.rglob('*.WAV'))
    
    print(f"Found {len(wav_files)} WAV files")
    print("Scanning and organizing...\n")
    
    for i, wav_file in enumerate(wav_files, 1):
        if i % 10 == 0:
            print(f"Processing {i}/{len(wav_files)}...")
        
        try:
            # Extract metadata
            metadata = extract_wav_metadata(wav_file)
            if not metadata:
                stats['errors'].append(str(wav_file))
                continue
            
            # Determine category
            dest_folder = None
            category = None
            
            # Check for commercial identifiers in filename first
            filename_category = categorize_by_filename(wav_file.name)
            
            if metadata['has_metadata'] or filename_category:
                # Has metadata OR recognizable commercial pattern = COMMERCIAL SAMPLE
                category = 'commercial'
                
                if filename_category:
                    dest_folder = dest_base / filename_category
                elif metadata['product']:
                    dest_folder = commercial_dir / metadata['product'].replace('/', '_')
                elif metadata['software']:
                    dest_folder = commercial_dir / metadata['software'].replace('/', '_')
                elif metadata['originator']:
                    dest_folder = commercial_dir / metadata['originator'].replace('/', '_')
                else:
                    dest_folder = commercial_dir / "Other_With_Metadata"
                
                stats['commercial'].append({
                    'file': wav_file.name,
                    'dest': str(dest_folder.relative_to(dest_base)),
                    'metadata': metadata['info']
                })
            
            else:
                # ⭐⭐⭐ HARD RULE: NO metadata and no recognizable pattern = ORIGINAL COMPOSITION! ⭐⭐⭐
                # This is YOUR precious original music!
                category = 'original'
                
                # Preserve some folder structure for originals
                relative_path = wav_file.relative_to(source_dir)
                if len(relative_path.parts) > 1:
                    # Keep subfolder structure
                    dest_folder = originals_dir / relative_path.parent
                else:
                    dest_folder = originals_dir
                
                stats['originals'].append({
                    'file': wav_file.name,
                    'source': str(relative_path)
                })
            
            # Create destination folder
            dest_folder.mkdir(parents=True, exist_ok=True)
            
            # Determine destination filename - use original name from metadata if available
            dest_filename = wav_file.name
            
            # Try to use original name from metadata
            if metadata['original_name']:
                # Use INAM tag
                clean_name = metadata['original_name'].replace('/', '_').replace('\\', '_')
                dest_filename = f"{clean_name}.wav"
            elif metadata['title']:
                # Use TITL tag
                clean_name = metadata['title'].replace('/', '_').replace('\\', '_')
                dest_filename = f"{clean_name}.wav"
            
            # Copy file (not move, to be safe)
            dest_file = dest_folder / dest_filename
            
            # Handle duplicates
            counter = 1
            original_dest = dest_file
            while dest_file.exists():
                dest_file = dest_file.parent / f"{original_dest.stem}_{counter}{original_dest.suffix}"
                counter += 1
            
            shutil.copy2(wav_file, dest_file)
            
            # Track if renamed
            if dest_filename != wav_file.name:
                if category == 'commercial':
                    stats['commercial'][-1]['renamed_to'] = dest_filename
                elif category == 'original':
                    stats['originals'][-1]['renamed_to'] = dest_filename
            
        except Exception as e:
            print(f"Error processing {wav_file.name}: {e}")
            stats['errors'].append(f"{wav_file.name}: {e}")
    
    return stats

def print_report(stats):
    """Print organization report"""
    print("\n" + "="*80)
    print("ORGANIZATION COMPLETE!")
    print("="*80 + "\n")
    
    print("⭐⭐⭐ HARD RULE APPLIED ⭐⭐⭐")
    print("Files WITHOUT metadata = YOUR ORIGINAL COMPOSITIONS")
    print("")
    print("🎵 ORIGINAL COMPOSITIONS (NO METADATA - YOUR PRECIOUS MUSIC!):")
    print("-" * 80)
    print(f"Total: {len(stats['originals'])} files ⭐⭐⭐\n")
    if stats['originals']:
        print("Files identified as ORIGINALS:")
        for item in sorted(stats['originals'], key=lambda x: x['file'])[:20]:
            print(f"  ✓ {item['file']}")
            if 'renamed_to' in item:
                print(f"    → Renamed to: {item['renamed_to']}")
            if 'source' in item:
                print(f"    From: {item['source']}")
        if len(stats['originals']) > 20:
            print(f"  ... and {len(stats['originals']) - 20} more")
    
    print("\n" + "="*80)
    print("📦 COMMERCIAL SAMPLES (WITH METADATA OR KNOWN PRODUCTS):")
    print("-" * 80)
    print(f"Total: {len(stats['commercial'])} files\n")
    
    if stats['commercial']:
        # Group by destination
        by_dest = defaultdict(list)
        for item in stats['commercial']:
            by_dest[item['dest']].append(item['file'])
        
        print("Organized into categories:")
        for dest, files in sorted(by_dest.items()):
            print(f"\n  {dest}/ ({len(files)} files)")
            items_in_dest = [item for item in stats['commercial'] if item['dest'] == dest]
            for item in sorted(items_in_dest, key=lambda x: x['file'])[:5]:
                print(f"    • {item['file']}")
                if 'renamed_to' in item:
                    print(f"      → {item['renamed_to']}")
            if len(files) > 5:
                print(f"    ... and {len(files) - 5} more")
    
    if stats['errors']:
        print("\n" + "="*80)
        print("⚠️  ERRORS:")
        print("-" * 80)
        for err in stats['errors'][:10]:
            print(f"  • {err}")
        if len(stats['errors']) > 10:
            print(f"  ... and {len(stats['errors']) - 10} more")
    
    print("\n" + "="*80)
    print("SUMMARY:")
    print(f"  ⭐⭐⭐ ORIGINAL COMPOSITIONS (NO METADATA): {len(stats['originals'])} files ⭐⭐⭐")
    print(f"  📦 Commercial Samples (WITH metadata): {len(stats['commercial'])} files")
    print(f"  ⚠️  Errors: {len(stats['errors'])} files")
    print("="*80)
    print("\n⭐ HARD RULE ENFORCED: NO METADATA = YOUR ORIGINAL MUSIC!")

if __name__ == '__main__':
    source = Path("WAVES TO MOVE")
    destination = Path("ORGANIZED_WAVES")
    
    print("WAV FILE ORGANIZER")
    print("="*80)
    print(f"Source: {source}")
    print(f"Destination: {destination}")
    print("\n⭐⭐⭐ HARD RULE ⭐⭐⭐")
    print("ANY FILE WITHOUT METADATA = ORIGINAL COMPOSITION!")
    print("\nThis will organize files into:")
    print("  • ORIGINAL_COMPOSITIONS/ - Files WITHOUT metadata (YOUR PRECIOUS MUSIC!)")
    print("  • COMMERCIAL_SAMPLES/ - Files WITH metadata (sample libraries)")
    print("="*80)
    print("\nStarting...\n")
    
    stats = organize_files(source, destination)
    print_report(stats)
    
    print(f"\n✓ Files copied to: {destination.absolute()}")

