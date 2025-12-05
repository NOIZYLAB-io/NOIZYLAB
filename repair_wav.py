#!/usr/bin/env python3
"""
WAV Header Repair Tool
Repairs WAV files with corrupted headers by using a template from a working file.
"""

import os
import struct
import shutil
from pathlib import Path

def read_wav_header(filepath):
    """Read and parse WAV header from a file."""
    with open(filepath, 'rb') as f:
        # RIFF header (12 bytes)
        riff_id = f.read(4)
        file_size = struct.unpack('<I', f.read(4))[0]
        wave_id = f.read(4)
        
        if riff_id != b'RIFF' or wave_id != b'WAVE':
            raise ValueError("Not a valid WAV file")
            
        # Find fmt chunk
        while True:
            chunk_id = f.read(4)
            if len(chunk_id) < 4:
                break
            chunk_size = struct.unpack('<I', f.read(4))[0]
            
            if chunk_id == b'fmt ':
                fmt_data = f.read(chunk_size)
                audio_format = struct.unpack('<H', fmt_data[0:2])[0]
                num_channels = struct.unpack('<H', fmt_data[2:4])[0]
                sample_rate = struct.unpack('<I', fmt_data[4:8])[0]
                byte_rate = struct.unpack('<I', fmt_data[8:12])[0]
                block_align = struct.unpack('<H', fmt_data[12:14])[0]
                bits_per_sample = struct.unpack('<H', fmt_data[14:16])[0]
                
                return {
                    'audio_format': audio_format,
                    'num_channels': num_channels,
                    'sample_rate': sample_rate,
                    'byte_rate': byte_rate,
                    'block_align': block_align,
                    'bits_per_sample': bits_per_sample
                }
            else:
                f.seek(chunk_size + (chunk_size % 2), 1)  # Skip chunk
                
    raise ValueError("fmt chunk not found")


def create_wav_header(params, data_size):
    """Create a minimal WAV header."""
    header = bytearray()
    
    # Calculate sizes
    fmt_chunk_size = 16
    file_size = 36 + data_size
    
    # RIFF header
    header.extend(b'RIFF')
    header.extend(struct.pack('<I', file_size))
    header.extend(b'WAVE')
    
    # fmt chunk
    header.extend(b'fmt ')
    header.extend(struct.pack('<I', fmt_chunk_size))
    header.extend(struct.pack('<H', params['audio_format']))
    header.extend(struct.pack('<H', params['num_channels']))
    header.extend(struct.pack('<I', params['sample_rate']))
    header.extend(struct.pack('<I', params['byte_rate']))
    header.extend(struct.pack('<H', params['block_align']))
    header.extend(struct.pack('<H', params['bits_per_sample']))
    
    # data chunk header
    header.extend(b'data')
    header.extend(struct.pack('<I', data_size))
    
    return bytes(header)


def find_audio_data_start(filepath, header_size_estimate=100):
    """Find where the actual audio data might start in a corrupted file."""
    with open(filepath, 'rb') as f:
        data = f.read()
        
    # Look for the first non-zero byte after initial zeros
    for i in range(len(data)):
        if data[i] != 0:
            return i
            
    return len(data)


def repair_wav(corrupted_path, template_path, output_path=None):
    """Repair a corrupted WAV file using a template for header info."""
    corrupted_path = Path(corrupted_path)
    template_path = Path(template_path)
    
    if output_path is None:
        output_path = corrupted_path.with_suffix('.repaired.wav')
    output_path = Path(output_path)
    
    print(f"Corrupted file: {corrupted_path}")
    print(f"Template file: {template_path}")
    print(f"Output file: {output_path}")
    
    # Get header info from template
    try:
        params = read_wav_header(template_path)
        print(f"\nTemplate parameters:")
        print(f"  Sample Rate: {params['sample_rate']} Hz")
        print(f"  Channels: {params['num_channels']}")
        print(f"  Bits/Sample: {params['bits_per_sample']}")
    except Exception as e:
        print(f"Error reading template: {e}")
        return False
        
    # Read corrupted file
    with open(corrupted_path, 'rb') as f:
        corrupted_data = f.read()
        
    file_size = len(corrupted_data)
    print(f"\nCorrupted file size: {file_size} bytes")
    
    # Find where audio data might start
    data_start = find_audio_data_start(corrupted_path)
    print(f"First non-zero byte at: {data_start}")
    
    # Estimate standard header size (44 bytes for minimal WAV, but BFD has extra chunks)
    # Let's look at the template to find data offset
    with open(template_path, 'rb') as f:
        template_data = f.read()
        
    # Find 'data' chunk in template
    data_marker = template_data.find(b'data')
    if data_marker > 0:
        template_header_size = data_marker + 8  # 'data' + size field
        print(f"Template header size: {template_header_size} bytes")
    else:
        template_header_size = 44
        print(f"Using default header size: {template_header_size} bytes")
        
    # For BFD files, the header is larger due to custom chunks
    # Let's assume the audio data starts after the null bytes
    # and the file originally had the same structure as the template
    
    # Calculate audio data size based on file structure
    # The corrupted file appears to have null bytes where the header should be
    audio_data_start = min(data_start, template_header_size)
    audio_data = corrupted_data[audio_data_start:]
    
    # Find actual audio by looking for non-zero patterns
    actual_start = 0
    for i in range(len(audio_data) - 4):
        if audio_data[i] != 0 or audio_data[i+1] != 0:
            actual_start = i
            break
            
    if actual_start > 0:
        audio_data = audio_data[actual_start:]
        print(f"Actual audio data starts at offset: {audio_data_start + actual_start}")
        
    audio_data_size = len(audio_data)
    print(f"Audio data size: {audio_data_size} bytes")
    
    # Create new header
    new_header = create_wav_header(params, audio_data_size)
    print(f"New header size: {len(new_header)} bytes")
    
    # Write repaired file
    with open(output_path, 'wb') as f:
        f.write(new_header)
        f.write(audio_data)
        
    print(f"\n✓ Repaired file written to: {output_path}")
    
    # Verify the repaired file
    try:
        import wave
        with wave.open(str(output_path), 'rb') as w:
            print(f"  Verification: Valid WAV file")
            print(f"  Duration: {w.getnframes() / w.getframerate():.2f} seconds")
    except Exception as e:
        print(f"  Verification failed: {e}")
        return False
        
    return True


if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: repair_wav.py <corrupted_file> <template_file> [output_file]")
        sys.exit(1)
        
    corrupted = sys.argv[1]
    template = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) > 3 else None
    
    success = repair_wav(corrupted, template, output)
    sys.exit(0 if success else 1)
