#!/usr/bin/env python3
"""
Extract metadata from WAV files to identify their source/origin
"""

import os
import struct
import sys
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
    """Extract all metadata from a WAV file"""
    metadata = {
        'filename': filepath.name,
        'size': filepath.stat().st_size,
        'chunks': [],
        'info': {},
        'ixml': None,
        'bext': None,
        'cart': None,
        'raw_data': {}
    }
    
    try:
        with open(filepath, 'rb') as f:
            # Read RIFF header
            riff = f.read(4)
            if riff != b'RIFF':
                return None
            
            file_size = struct.unpack('<I', f.read(4))[0]
            wave = f.read(4)
            if wave != b'WAVE':
                return None
            
            # Read all chunks
            while True:
                chunk_id, chunk_size = read_chunk(f)
                if chunk_id is None:
                    break
                
                chunk_name = chunk_id.decode('ascii', errors='ignore')
                metadata['chunks'].append(chunk_name)
                
                # Read chunk data
                chunk_data = f.read(chunk_size)
                
                # Handle specific chunk types
                if chunk_id == b'fmt ':
                    # Format chunk
                    if len(chunk_data) >= 16:
                        audio_format, channels, sample_rate, byte_rate, block_align, bits_per_sample = struct.unpack('<HHIIHH', chunk_data[:16])
                        metadata['audio_format'] = audio_format
                        metadata['channels'] = channels
                        metadata['sample_rate'] = sample_rate
                        metadata['bits_per_sample'] = bits_per_sample
                
                elif chunk_id == b'LIST':
                    # LIST chunk - may contain INFO data
                    list_type = chunk_data[:4]
                    if list_type == b'INFO':
                        # Parse INFO chunks
                        pos = 4
                        while pos < len(chunk_data) - 8:
                            try:
                                info_id = chunk_data[pos:pos+4]
                                info_size = struct.unpack('<I', chunk_data[pos+4:pos+8])[0]
                                info_data = chunk_data[pos+8:pos+8+info_size]
                                info_name = info_id.decode('ascii', errors='ignore')
                                info_value = info_data.decode('utf-8', errors='ignore').rstrip('\x00')
                                metadata['info'][info_name] = info_value
                                pos += 8 + info_size
                                if info_size % 2:  # Padding
                                    pos += 1
                            except:
                                break
                
                elif chunk_id == b'iXML':
                    # iXML metadata
                    metadata['ixml'] = chunk_data.decode('utf-8', errors='ignore')
                
                elif chunk_id == b'bext':
                    # Broadcast Wave Format extension
                    try:
                        description = chunk_data[0:256].decode('ascii', errors='ignore').rstrip('\x00')
                        originator = chunk_data[256:288].decode('ascii', errors='ignore').rstrip('\x00')
                        originator_ref = chunk_data[288:320].decode('ascii', errors='ignore').rstrip('\x00')
                        metadata['bext'] = {
                            'description': description,
                            'originator': originator,
                            'originator_reference': originator_ref
                        }
                    except:
                        pass
                
                elif chunk_id == b'cart':
                    # AES46 cart chunk
                    try:
                        version = chunk_data[0:4].decode('ascii', errors='ignore')
                        title = chunk_data[4:68].decode('ascii', errors='ignore').rstrip('\x00')
                        artist = chunk_data[68:132].decode('ascii', errors='ignore').rstrip('\x00')
                        metadata['cart'] = {
                            'version': version,
                            'title': title,
                            'artist': artist
                        }
                    except:
                        pass
                
                # Store first 100 bytes of other interesting chunks
                elif chunk_name not in ['data', 'fmt ', 'JUNK', 'PAD ']:
                    try:
                        preview = chunk_data[:100].decode('ascii', errors='ignore')
                        if preview.strip():
                            metadata['raw_data'][chunk_name] = preview
                    except:
                        pass
                
                # Skip padding byte if chunk size is odd
                if chunk_size % 2:
                    f.read(1)
    
    except Exception as e:
        metadata['error'] = str(e)
    
    return metadata

def scan_directory(directory):
    """Scan directory for WAV files and extract metadata"""
    directory = Path(directory)
    results = []
    
    # Get all WAV files recursively
    wav_files = list(directory.rglob('*.wav')) + list(directory.rglob('*.WAV'))
    
    print(f"Found {len(wav_files)} WAV files")
    print("Scanning metadata...\n")
    
    for i, wav_file in enumerate(wav_files, 1):
        if i % 10 == 0:
            print(f"Processed {i}/{len(wav_files)} files...")
        
        metadata = extract_wav_metadata(wav_file)
        if metadata:
            results.append(metadata)
    
    return results

def analyze_results(results):
    """Analyze and report findings"""
    print("\n" + "="*80)
    print("METADATA ANALYSIS REPORT")
    print("="*80 + "\n")
    
    # Collect all unique metadata fields
    all_info_keys = set()
    all_chunks = defaultdict(int)
    products = set()
    software = set()
    originators = set()
    
    files_with_metadata = 0
    
    for result in results:
        if result.get('info'):
            files_with_metadata += 1
            all_info_keys.update(result['info'].keys())
            
            # Look for product/software identifiers
            for key, value in result['info'].items():
                if key in ['ISFT', 'ISRC', 'IPRD', 'INAM', 'ICMT']:
                    if value.strip():
                        if 'ISFT' in key:  # Software
                            software.add(value.strip())
                        elif 'IPRD' in key:  # Product
                            products.add(value.strip())
        
        if result.get('bext'):
            files_with_metadata += 1
            if result['bext'].get('originator'):
                originators.add(result['bext']['originator'])
        
        for chunk in result.get('chunks', []):
            all_chunks[chunk] += 1
    
    print(f"Total files scanned: {len(results)}")
    print(f"Files with metadata: {files_with_metadata}\n")
    
    if products:
        print("PRODUCTS FOUND:")
        print("-" * 40)
        for product in sorted(products):
            print(f"  • {product}")
        print()
    
    if software:
        print("SOFTWARE/TOOLS FOUND:")
        print("-" * 40)
        for sw in sorted(software):
            print(f"  • {sw}")
        print()
    
    if originators:
        print("ORIGINATORS FOUND:")
        print("-" * 40)
        for orig in sorted(originators):
            print(f"  • {orig}")
        print()
    
    if all_info_keys:
        print("INFO CHUNK FIELDS FOUND:")
        print("-" * 40)
        for key in sorted(all_info_keys):
            count = sum(1 for r in results if key in r.get('info', {}))
            print(f"  • {key}: {count} files")
        print()
    
    # Show detailed metadata for a few sample files
    print("\nDETAILED SAMPLE METADATA:")
    print("=" * 80)
    
    samples_shown = 0
    for result in results:
        if result.get('info') or result.get('bext') or result.get('cart'):
            print(f"\nFile: {result['filename']}")
            print(f"Size: {result['size']:,} bytes")
            
            if result.get('audio_format'):
                print(f"Format: {result.get('channels')}ch, {result.get('sample_rate')}Hz, {result.get('bits_per_sample')}bit")
            
            if result.get('info'):
                print("INFO metadata:")
                for key, value in sorted(result['info'].items()):
                    print(f"  {key}: {value}")
            
            if result.get('bext'):
                print("Broadcast Wave metadata:")
                for key, value in result['bext'].items():
                    if value:
                        print(f"  {key}: {value}")
            
            if result.get('cart'):
                print("Cart metadata:")
                for key, value in result['cart'].items():
                    if value:
                        print(f"  {key}: {value}")
            
            if result.get('raw_data'):
                print("Other chunk data:")
                for key, value in result['raw_data'].items():
                    print(f"  {key}: {value[:100]}")
            
            samples_shown += 1
            if samples_shown >= 10:  # Show first 10 files with metadata
                break
    
    # Show files with interesting names that might indicate source
    print("\n\nFILENAME PATTERN ANALYSIS:")
    print("=" * 80)
    
    patterns = defaultdict(list)
    for result in results:
        name = result['filename'].lower()
        if 'mirage' in name:
            patterns['Ensoniq Mirage'].append(result['filename'])
        elif 'kawaii' in name:
            patterns['Kawaii'].append(result['filename'])
        elif 'dx100' in name or 'dx-100' in name:
            patterns['Yamaha DX100'].append(result['filename'])
        elif 'manjira' in name or 'dholak' in name or 'dimdi' in name:
            patterns['Indian Percussion'].append(result['filename'])
        elif 'ambient' in name:
            patterns['Ambient/Soundscape'].append(result['filename'])
        elif 'sys100' in name:
            patterns['Roland System 100'].append(result['filename'])
        elif 'sh5' in name or 'sh-5' in name:
            patterns['Roland SH-5'].append(result['filename'])
    
    for pattern, files in sorted(patterns.items()):
        print(f"\n{pattern}: {len(files)} files")
        for f in files[:5]:  # Show first 5
            print(f"  • {f}")
        if len(files) > 5:
            print(f"  ... and {len(files) - 5} more")

if __name__ == '__main__':
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'
    results = scan_directory(directory)
    analyze_results(results)

