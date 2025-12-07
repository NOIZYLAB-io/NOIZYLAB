#!/usr/bin/env python3
"""
Search and extract all ID3 tags and metadata from WAV files.
Scans both source directory and SAMPLE_MASTER directory.
"""

import os
import json
from pathlib import Path
from collections import defaultdict
import mutagen
from mutagen.wave import WAVE
from mutagen.id3 import ID3, ID3NoHeaderError

def extract_all_tags(filepath):
    """Extract all tags from an audio file."""
    tags_info = {
        'file': str(filepath),
        'filename': os.path.basename(filepath),
        'has_tags': False,
        'has_id3': False,
        'tags': {},
        'raw_tags': {},
        'file_info': {},
        'errors': []
    }
    
    try:
        # First, try to get ID3 tags directly
        try:
            id3 = ID3(filepath)
            tags_info['has_id3'] = True
            tags_info['has_tags'] = True
            
            # Extract all ID3 frames
            for frame_id, frame in id3.items():
                tag_name = str(frame_id)
                
                # Get the text value
                if hasattr(frame, 'text'):
                    if isinstance(frame.text, list):
                        value = [str(v) for v in frame.text]
                    else:
                        value = [str(frame.text)]
                elif hasattr(frame, '__str__'):
                    value = [str(frame)]
                else:
                    value = [repr(frame)]
                
                tags_info['tags'][tag_name] = value
                tags_info['raw_tags'][tag_name] = {
                    'frame_id': str(frame_id),
                    'frame_type': type(frame).__name__,
                    'value': value,
                    'raw': repr(frame)
                }
                    
        except ID3NoHeaderError:
            tags_info['has_id3'] = False
            # Continue to try mutagen.File
        except Exception as e:
            tags_info['has_id3'] = False
            tags_info['errors'].append(f'ID3 error: {str(e)}')
        
        # Also try mutagen.File for other metadata
        try:
            audio = mutagen.File(filepath)
            if audio:
                tags_info['has_tags'] = True
                
                # Get file info
                if hasattr(audio, 'info'):
                    info = audio.info
                    tags_info['file_info'] = {
                        'length': getattr(info, 'length', None),
                        'sample_rate': getattr(info, 'sample_rate', None),
                        'channels': getattr(info, 'channels', None),
                        'bitrate': getattr(info, 'bitrate', None),
                        'bits_per_sample': getattr(info, 'bits_per_sample', None),
                        'codec': getattr(info, 'codec', None),
                        'codec_name': getattr(info, 'codec_name', None),
                    }
                
                # Try to get any other tags (for formats other than ID3)
                if hasattr(audio, 'tags') and audio.tags:
                    for tag_key, tag_value in audio.tags.items():
                        if tag_key not in tags_info['tags']:
                            if isinstance(tag_value, list):
                                tags_info['tags'][tag_key] = [str(v) for v in tag_value]
                            else:
                                tags_info['tags'][tag_key] = [str(tag_value)]
                            
        except Exception as e:
            if not tags_info['errors']:  # Only add if we don't have ID3 errors
                tags_info['errors'].append(f'Mutagen error: {str(e)}')
                            
    except Exception as e:
        tags_info['errors'].append(f'File error: {str(e)}')
    
    return tags_info

def scan_directory(directory):
    """Scan all WAV files in a directory."""
    print(f"Scanning directory: {directory}")
    
    wav_files = list(Path(directory).glob('**/*.wav')) + \
                list(Path(directory).glob('**/*.WAV')) + \
                list(Path(directory).glob('**/*.Wav'))
    
    print(f"Found {len(wav_files)} WAV files")
    
    all_tags = []
    tag_statistics = {
        'total_files': len(wav_files),
        'files_with_tags': 0,
        'files_with_id3': 0,
        'unique_tag_types': set(),
        'tag_frequency': defaultdict(int),
        'tag_values': defaultdict(set)
    }
    
    for idx, filepath in enumerate(wav_files, 1):
        if idx % 100 == 0:
            print(f"Processing {idx}/{len(wav_files)}...")
        
        tags_info = extract_all_tags(filepath)
        all_tags.append(tags_info)
        
        if tags_info['has_tags']:
            tag_statistics['files_with_tags'] += 1
        
        if tags_info.get('has_id3', False):
            tag_statistics['files_with_id3'] += 1
        
        # Collect tag statistics
        for tag_name, tag_value in tags_info['tags'].items():
            tag_statistics['unique_tag_types'].add(tag_name)
            tag_statistics['tag_frequency'][tag_name] += 1
            for val in tag_value:
                tag_statistics['tag_values'][tag_name].add(str(val))
    
    # Convert sets to lists for JSON serialization
    tag_statistics['unique_tag_types'] = sorted(list(tag_statistics['unique_tag_types']))
    tag_statistics['tag_values'] = {
        k: sorted(list(v))[:100]  # Limit to 100 values per tag
        for k, v in tag_statistics['tag_values'].items()
    }
    
    return all_tags, tag_statistics

def main():
    """Main execution function."""
    source_dir = "/Volumes/4TB_Utility/Waves To Sort"
    sample_master_dir = "/Volumes/4TB_Utility/SAMPLE_MASTER"
    
    print("=" * 80)
    print("ID3 TAG SEARCH AND EXTRACTION")
    print("=" * 80)
    
    results = {
        'source_directory': {},
        'sample_master_directory': {},
        'combined': {}
    }
    
    # Scan source directory
    if os.path.exists(source_dir):
        print("\n" + "=" * 80)
        print("SCANNING SOURCE DIRECTORY")
        print("=" * 80)
        source_tags, source_stats = scan_directory(source_dir)
        results['source_directory'] = {
            'tags': source_tags,
            'statistics': source_stats
        }
    
    # Scan SAMPLE_MASTER directory
    if os.path.exists(sample_master_dir):
        print("\n" + "=" * 80)
        print("SCANNING SAMPLE_MASTER DIRECTORY")
        print("=" * 80)
        master_tags, master_stats = scan_directory(sample_master_dir)
        results['sample_master_directory'] = {
            'tags': master_tags,
            'statistics': master_stats
        }
    
    # Combined statistics
    if results['source_directory'] and results['sample_master_directory']:
        combined_stats = {
            'total_files': results['source_directory']['statistics']['total_files'] + \
                          results['sample_master_directory']['statistics']['total_files'],
            'files_with_tags': results['source_directory']['statistics']['files_with_tags'] + \
                              results['sample_master_directory']['statistics']['files_with_tags'],
            'files_with_id3': results['source_directory']['statistics']['files_with_id3'] + \
                             results['sample_master_directory']['statistics']['files_with_id3'],
            'unique_tag_types': sorted(list(
                set(results['source_directory']['statistics']['unique_tag_types']) |
                set(results['sample_master_directory']['statistics']['unique_tag_types'])
            )),
            'tag_frequency': defaultdict(int),
            'tag_values': defaultdict(set)
        }
        
        # Combine tag frequencies
        for tag in combined_stats['unique_tag_types']:
            freq1 = results['source_directory']['statistics']['tag_frequency'].get(tag, 0)
            freq2 = results['sample_master_directory']['statistics']['tag_frequency'].get(tag, 0)
            combined_stats['tag_frequency'][tag] = freq1 + freq2
        
        # Combine tag values
        for tag in combined_stats['unique_tag_types']:
            vals1 = results['source_directory']['statistics']['tag_values'].get(tag, [])
            vals2 = results['sample_master_directory']['statistics']['tag_values'].get(tag, [])
            # Convert to sets for union, then back to sorted list
            combined_vals = set(vals1) | set(vals2)
            combined_stats['tag_values'][tag] = sorted(list(combined_vals))[:100]
        
        combined_stats['tag_frequency'] = dict(combined_stats['tag_frequency'])
        combined_stats['tag_values'] = dict(combined_stats['tag_values'])
        
        results['combined'] = {'statistics': combined_stats}
    
    # Save results
    output_dir = Path(source_dir) / 'ID3_Tag_Analysis'
    output_dir.mkdir(exist_ok=True)
    
    # Save full results
    json_path = output_dir / 'all_id3_tags.json'
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nSaved full results to: {json_path}")
    
    # Save statistics summary
    stats_path = output_dir / 'tag_statistics.json'
    stats_data = {
        'source': results.get('source_directory', {}).get('statistics', {}),
        'sample_master': results.get('sample_master_directory', {}).get('statistics', {}),
        'combined': results.get('combined', {}).get('statistics', {})
    }
    with open(stats_path, 'w', encoding='utf-8') as f:
        json.dump(stats_data, f, indent=2, ensure_ascii=False)
    print(f"Saved statistics to: {stats_path}")
    
    # Print summary
    print("\n" + "=" * 80)
    print("TAG SEARCH SUMMARY")
    print("=" * 80)
    
    if results.get('source_directory'):
        stats = results['source_directory']['statistics']
        print(f"\nSource Directory:")
        print(f"  Total files: {stats['total_files']}")
        print(f"  Files with tags: {stats['files_with_tags']}")
        print(f"  Files with ID3: {stats['files_with_id3']}")
        print(f"  Unique tag types: {len(stats['unique_tag_types'])}")
        print(f"\n  Most common tags:")
        for tag, count in sorted(stats['tag_frequency'].items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"    {tag}: {count} files")
    
    if results.get('sample_master_directory'):
        stats = results['sample_master_directory']['statistics']
        print(f"\nSAMPLE_MASTER Directory:")
        print(f"  Total files: {stats['total_files']}")
        print(f"  Files with tags: {stats['files_with_tags']}")
        print(f"  Files with ID3: {stats['files_with_id3']}")
        print(f"  Unique tag types: {len(stats['unique_tag_types'])}")
        print(f"\n  Most common tags:")
        for tag, count in sorted(stats['tag_frequency'].items(), key=lambda x: x[1], reverse=True)[:10]:
            print(f"    {tag}: {count} files")
    
    if results.get('combined'):
        stats = results['combined']['statistics']
        print(f"\nCombined Statistics:")
        print(f"  Total files: {stats['total_files']}")
        print(f"  Files with tags: {stats['files_with_tags']}")
        print(f"  Files with ID3: {stats['files_with_id3']}")
        print(f"  Unique tag types: {len(stats['unique_tag_types'])}")
        print(f"\n  All unique tag types found:")
        for tag in stats['unique_tag_types']:
            print(f"    - {tag}")
    
    print("\n" + "=" * 80)
    print(f"Results saved to: {output_dir}")
    print("=" * 80)

if __name__ == "__main__":
    main()

