#!/usr/bin/env python3
"""
Extract metadata from audio files in the media directory.
"""

import os
import wave
import json
from pathlib import Path
from datetime import datetime

def get_wav_metadata(file_path):
    """Extract metadata from WAV file."""
    try:
        with wave.open(str(file_path), 'rb') as wav_file:
            metadata = {
                'file_path': str(file_path),
                'file_name': os.path.basename(file_path),
                'file_size_bytes': os.path.getsize(file_path),
                'channels': wav_file.getnchannels(),
                'sample_width': wav_file.getsampwidth(),
                'framerate': wav_file.getframerate(),
                'nframes': wav_file.getnframes(),
                'comptype': wav_file.getcomptype(),
                'compname': wav_file.getcompname(),
            }
            
            # Calculate duration
            if metadata['framerate'] > 0:
                metadata['duration_seconds'] = metadata['nframes'] / metadata['framerate']
            else:
                metadata['duration_seconds'] = 0
            
            # Calculate bit depth
            metadata['bit_depth'] = metadata['sample_width'] * 8
            
            # Calculate bitrate (approximate)
            if metadata['duration_seconds'] > 0:
                metadata['bitrate_kbps'] = (metadata['file_size_bytes'] * 8) / (metadata['duration_seconds'] * 1000)
            else:
                metadata['bitrate_kbps'] = 0
            
            # Get file modification time
            mtime = os.path.getmtime(file_path)
            metadata['modified_time'] = datetime.fromtimestamp(mtime).isoformat()
            
            return metadata
    except Exception as e:
        return {
            'file_path': str(file_path),
            'file_name': os.path.basename(file_path),
            'error': str(e)
        }

def main():
    # Find all audio files
    media_dir = Path('/Users/m2ultra/NOIZYLAB/noizylab_2026/media')
    
    if not media_dir.exists():
        print(f"Media directory not found: {media_dir}")
        return
    
    audio_extensions = ['.wav', '.mp3', '.flac', '.m4a', '.aac']
    audio_files = []
    
    for ext in audio_extensions:
        audio_files.extend(media_dir.glob(f'*{ext}'))
    
    if not audio_files:
        print(f"No audio files found in {media_dir}")
        return
    
    print(f"Found {len(audio_files)} audio file(s)\n")
    print("=" * 80)
    
    all_metadata = []
    
    for audio_file in sorted(audio_files):
        print(f"\nProcessing: {audio_file.name}")
        print("-" * 80)
        
        if audio_file.suffix.lower() == '.wav':
            metadata = get_wav_metadata(audio_file)
        else:
            metadata = {
                'file_path': str(audio_file),
                'file_name': audio_file.name,
                'file_size_bytes': os.path.getsize(audio_file),
                'error': f'Format {audio_file.suffix} not yet supported (only WAV supported)'
            }
        
        all_metadata.append(metadata)
        
        # Print metadata
        if 'error' in metadata:
            print(f"ERROR: {metadata['error']}")
        else:
            print(f"Channels: {metadata.get('channels', 'N/A')}")
            print(f"Sample Rate: {metadata.get('framerate', 'N/A')} Hz")
            print(f"Bit Depth: {metadata.get('bit_depth', 'N/A')} bits")
            print(f"Sample Width: {metadata.get('sample_width', 'N/A')} bytes")
            print(f"Frames: {metadata.get('nframes', 'N/A')}")
            print(f"Duration: {metadata.get('duration_seconds', 0):.2f} seconds")
            print(f"File Size: {metadata.get('file_size_bytes', 0):,} bytes ({metadata.get('file_size_bytes', 0) / 1024:.2f} KB)")
            print(f"Bitrate: {metadata.get('bitrate_kbps', 0):.2f} kbps")
            print(f"Compression: {metadata.get('comptype', 'N/A')} ({metadata.get('compname', 'N/A')})")
            print(f"Modified: {metadata.get('modified_time', 'N/A')}")
    
    # Save to JSON file
    output_file = Path('/Users/m2ultra/NOIZYLAB/audio_metadata.json')
    with open(output_file, 'w') as f:
        json.dump(all_metadata, f, indent=2)
    
    print("\n" + "=" * 80)
    print(f"\nMetadata saved to: {output_file}")
    print(f"Total files processed: {len(audio_files)}")

if __name__ == '__main__':
    main()

