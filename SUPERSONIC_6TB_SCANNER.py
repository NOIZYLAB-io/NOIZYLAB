#!/usr/bin/env python3
"""
🔥 SUPER-SONIC 6TB DEEP SCANNER 🔥
CB_01 Maximum Velocity File Discovery & Analysis
"""

import os
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

print("=" * 100)
print("🔥 SUPER-SONIC 6TB DEEP SCANNER - MAXIMUM VELOCITY! 🔥")
print("=" * 100)
print(f"Started: {datetime.now()}")
print("=" * 100)

# Target drive
TARGET = "/Volumes/6TB"

# File categories
CODE_EXTENSIONS = {'.py', '.js', '.ts', '.jsx', '.tsx', '.sh', '.bash', '.zsh', 
                   '.rb', '.go', '.java', '.cpp', '.c', '.h', '.hpp', '.rs', '.swift'}
DOC_EXTENSIONS = {'.md', '.txt', '.pdf', '.doc', '.docx', '.rtf', '.tex'}
JSON_EXTENSIONS = {'.json', '.jsonl', '.geojson'}
AUDIO_CODE = {'.nki', '.nkm', '.nkc', '.exs', '.sfz', '.sf2'}
AUDIO_FILES = {'.wav', '.aif', '.aiff', '.mp3', '.flac', '.ogg', '.m4a'}
IMAGE_FILES = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'}
VIDEO_FILES = {'.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv'}

# Results storage
results = {
    'scan_date': str(datetime.now()),
    'target': TARGET,
    'code_files': [],
    'doc_files': [],
    'json_files': [],
    'audio_code_files': [],
    'stats': {
        'total_files': 0,
        'total_dirs': 0,
        'code_count': 0,
        'doc_count': 0,
        'json_count': 0,
        'audio_count': 0,
        'audio_code_count': 0,
        'by_extension': defaultdict(int),
        'by_directory': defaultdict(int)
    }
}

def scan_directory(root_path):
    """SUPER-SONIC recursive scanner"""
    try:
        for root, dirs, files in os.walk(root_path):
            # Skip hidden and system directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            results['stats']['total_dirs'] += len(dirs)
            
            for filename in files:
                # Skip hidden files
                if filename.startswith('.'):
                    continue
                
                filepath = os.path.join(root, filename)
                ext = Path(filename).suffix.lower()
                
                results['stats']['total_files'] += 1
                results['stats']['by_extension'][ext] += 1
                
                # Get relative path for cleaner output
                rel_path = os.path.relpath(filepath, TARGET)
                
                # Categorize files
                if ext in CODE_EXTENSIONS:
                    results['code_files'].append(rel_path)
                    results['stats']['code_count'] += 1
                
                if ext in DOC_EXTENSIONS:
                    results['doc_files'].append(rel_path)
                    results['stats']['doc_count'] += 1
                
                if ext in JSON_EXTENSIONS:
                    results['json_files'].append(rel_path)
                    results['stats']['json_count'] += 1
                
                if ext in AUDIO_FILES:
                    results['stats']['audio_count'] += 1
                
                if ext in AUDIO_CODE:
                    results['audio_code_files'].append(rel_path)
                    results['stats']['audio_code_count'] += 1
                
                # Progress indicator
                if results['stats']['total_files'] % 10000 == 0:
                    print(f"   🔄 Scanned {results['stats']['total_files']:,} files...")
    
    except PermissionError:
        pass
    except Exception as e:
        print(f"   ⚠️  Error in {root_path}: {e}")

# Scan main directories
print("\n🔍 Scanning Sample_Libraries...")
scan_directory(os.path.join(TARGET, "Sample_Libraries"))

print("\n🔍 Scanning _ORGANIZED...")
scan_directory(os.path.join(TARGET, "_ORGANIZED"))

# Print results
print("\n" + "=" * 100)
print("✅ SUPER-SONIC SCAN COMPLETE!")
print("=" * 100)

print(f"""
╔══════════════════════════════════════════════════════════════╗
║              🔥 6TB DEEP SCAN RESULTS 🔥                     ║
╠══════════════════════════════════════════════════════════════╣
║  TOTAL FILES:              {results['stats']['total_files']:>15,}        ║
║  TOTAL DIRECTORIES:        {results['stats']['total_dirs']:>15,}        ║
║                                                              ║
║  CODE FILES:               {results['stats']['code_count']:>15,}        ║
║  DOCUMENTATION:            {results['stats']['doc_count']:>15,}        ║
║  JSON FILES:               {results['stats']['json_count']:>15,}        ║
║  AUDIO FILES:              {results['stats']['audio_count']:>15,}        ║
║  AUDIO CODE FILES:         {results['stats']['audio_code_count']:>15,}        ║
╚══════════════════════════════════════════════════════════════╝
""")

# Show top file types
print("\n📊 TOP FILE TYPES:")
sorted_exts = sorted(results['stats']['by_extension'].items(), 
                     key=lambda x: x[1], reverse=True)[:20]
for ext, count in sorted_exts:
    ext_display = ext if ext else "(no extension)"
    print(f"   {ext_display:15s}: {count:>12,}")

# Show code files found
print(f"\n💻 CODE FILES FOUND ({len(results['code_files'])}):")
for cf in results['code_files'][:50]:
    print(f"   {cf}")
if len(results['code_files']) > 50:
    print(f"   ... and {len(results['code_files']) - 50} more")

# Show documentation files
print(f"\n📚 DOCUMENTATION FILES FOUND ({len(results['doc_files'])}):")
for df in results['doc_files'][:50]:
    print(f"   {df}")
if len(results['doc_files']) > 50:
    print(f"   ... and {len(results['doc_files']) - 50} more")

# Show JSON files
print(f"\n🗂️  JSON FILES FOUND ({len(results['json_files'])}):")
for jf in results['json_files'][:30]:
    print(f"   {jf}")
if len(results['json_files']) > 30:
    print(f"   ... and {len(results['json_files']) - 30} more")

# Save complete results
output_file = "/Users/m2ultra/6TB_SUPERSONIC_SCAN_RESULTS.json"
with open(output_file, 'w') as f:
    json.dump(results, f, indent=2)

print(f"\n✅ Complete results saved to: {output_file}")
print(f"Completed: {datetime.now()}")
print("=" * 100)
print("🔥 CB_01 SUPER-SONIC SCAN COMPLETE! 🔥")
print("=" * 100)

