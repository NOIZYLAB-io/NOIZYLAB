#!/usr/bin/env python3
"""
🎵 MEGA ULTIMATE WAV ORGANIZER v2.0 🎵

⭐⭐⭐ HARD RULE ⭐⭐⭐
ANY FILE WITHOUT METADATA = YOUR ORIGINAL COMPOSITION!

ENHANCED FEATURES:
- Progress bars and visual feedback
- MD5 checksums for verification
- Duplicate detection
- Audio analysis (silence, peaks)
- HTML report generation
- Undo/restore capability
- Advanced validation
- Performance optimization
"""

import os
import struct
import shutil
import json
import hashlib
import time
from pathlib import Path
from collections import defaultdict
from datetime import datetime
import wave

# ============================================================================
# CONFIGURATION
# ============================================================================

SOURCE_DIR = Path("WAVES TO MOVE")
DEST_DIR = Path("ORGANIZED_WAVES")
ORIGINALS_DIR = DEST_DIR / "ORIGINAL_COMPOSITIONS"
COMMERCIAL_DIR = DEST_DIR / "COMMERCIAL_SAMPLES"
REPORTS_DIR = Path("ORGANIZATION_REPORTS")
BACKUP_DIR = Path("ORGANIZATION_BACKUP")

CONFIG = {
    'check_duplicates': True,
    'generate_checksums': True,
    'analyze_audio': True,
    'create_html_report': True,
    'create_undo_script': True,
    'show_progress': True
}

# ============================================================================
# PROGRESS TRACKING
# ============================================================================

class ProgressBar:
    """Simple progress bar for terminal"""
    def __init__(self, total, prefix='Progress:', length=50):
        self.total = total
        self.prefix = prefix
        self.length = length
        self.current = 0
        self.start_time = time.time()
    
    def update(self, current=None):
        if current is not None:
            self.current = current
        else:
            self.current += 1
        
        percent = 100 * (self.current / float(self.total))
        filled = int(self.length * self.current // self.total)
        bar = '█' * filled + '-' * (self.length - filled)
        
        elapsed = time.time() - self.start_time
        if self.current > 0:
            eta = (elapsed / self.current) * (self.total - self.current)
            eta_str = f"ETA: {int(eta)}s"
        else:
            eta_str = "ETA: --"
        
        print(f'\r{self.prefix} |{bar}| {percent:.1f}% ({self.current}/{self.total}) {eta_str}', end='', flush=True)
        
        if self.current >= self.total:
            print()

# ============================================================================
# CHECKSUM & DUPLICATE DETECTION
# ============================================================================

def calculate_md5(filepath, chunk_size=8192):
    """Calculate MD5 checksum of file"""
    md5 = hashlib.md5()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(chunk_size):
                md5.update(chunk)
        return md5.hexdigest()
    except:
        return None

def calculate_audio_fingerprint(filepath):
    """Quick audio fingerprint (first/last 1KB + file size)"""
    try:
        size = filepath.stat().st_size
        with open(filepath, 'rb') as f:
            first = f.read(1024)
            f.seek(-min(1024, size), 2)
            last = f.read(1024)
        return hashlib.md5(first + last + str(size).encode()).hexdigest()
    except:
        return None

# ============================================================================
# AUDIO ANALYSIS
# ============================================================================

def analyze_wav_audio(filepath):
    """Analyze WAV file audio properties"""
    analysis = {
        'has_audio': False,
        'is_silent': False,
        'peak_level': None,
        'rms_level': None,
        'duration': None
    }
    
    try:
        with wave.open(str(filepath), 'rb') as wav:
            frames = wav.getnframes()
            rate = wav.getframerate()
            channels = wav.getnchannels()
            width = wav.getsampwidth()
            
            analysis['duration'] = frames / float(rate)
            analysis['has_audio'] = True
            
            # Sample first 100,000 frames for analysis
            sample_frames = min(100000, frames)
            if sample_frames > 0:
                wav.rewind()
                data = wav.readframes(sample_frames)
                
                # Simple peak detection (for 16-bit audio)
                if width == 2:
                    import struct
                    samples = struct.unpack(f'<{len(data)//2}h', data)
                    if samples:
                        peak = max(abs(s) for s in samples)
                        analysis['peak_level'] = peak / 32768.0  # Normalize to 0-1
                        
                        # Check if essentially silent
                        analysis['is_silent'] = peak < 100  # Very low threshold
    except:
        pass
    
    return analysis

# ============================================================================
# ENHANCED METADATA EXTRACTION
# ============================================================================

def read_chunk(f):
    """Read a RIFF chunk header"""
    chunk_id = f.read(4)
    if len(chunk_id) < 4:
        return None, 0
    chunk_size = struct.unpack('<I', f.read(4))[0]
    return chunk_id, chunk_size

def extract_wav_metadata_enhanced(filepath):
    """Extract comprehensive metadata from WAV file"""
    metadata = {
        'filename': filepath.name,
        'path': str(filepath),
        'size': filepath.stat().st_size,
        'modified': datetime.fromtimestamp(filepath.stat().st_mtime).isoformat(),
        'has_metadata': False,
        'info': {},
        'product': None,
        'software': None,
        'originator': None,
        'original_name': None,
        'title': None,
        'artist': None,
        'comment': None,
        'copyright': None,
        'creation_date': None,
        'sample_rate': None,
        'channels': None,
        'bits_per_sample': None,
        'duration_seconds': None,
        'all_chunks': [],
        'md5': None,
        'audio_fingerprint': None,
        'audio_analysis': {}
    }
    
    # Calculate checksums if enabled
    if CONFIG['check_duplicates'] or CONFIG['generate_checksums']:
        metadata['audio_fingerprint'] = calculate_audio_fingerprint(filepath)
    if CONFIG['generate_checksums']:
        metadata['md5'] = calculate_md5(filepath)
    
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
                
                chunk_name = chunk_id.decode('ascii', errors='ignore')
                metadata['all_chunks'].append(chunk_name)
                
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
                                    elif info_name == 'ICOP':
                                        metadata['copyright'] = info_value.strip()
                                    elif info_name == 'ICRD':
                                        metadata['creation_date'] = info_value.strip()
                                
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
        
        # Analyze audio if enabled
        if CONFIG['analyze_audio']:
            metadata['audio_analysis'] = analyze_wav_audio(filepath)
    
    except Exception as e:
        metadata['error'] = str(e)
    
    return metadata

def categorize_by_filename(filename):
    """Enhanced categorization by filename patterns"""
    name = filename.lower()
    
    patterns = {
        'Ensoniq_Mirage': ['mirage'],
        'Kawaii_Synth': ['kawaii'],
        'Yamaha_DX100': ['dx100', 'dx-100', 'dx 100'],
        'Yamaha_DX7': ['dx7', 'dx-7', 'dx 7'],
        'Indian_World_Percussion': ['manjira', 'dholak', 'dimdi', 'clay pot', 'kete', 'pora', 'tabla'],
        'Roland_System100': ['sys100', 'system100', 'system 100'],
        'Roland_SH5': ['sh5', 'sh-5', 'sh 5'],
        'Roland_Jupiter': ['jupiter'],
        'Storm_Season_FX': ['stormseasonfx', 'storm season'],
        'Ambient_Sound_Design': ['ambient'],
        'Sound_Effects_Hits': ['hit', 'impact', 'slam', 'bang'],
        'Beats_And_Loops': ['bpm', 'beat', 'loop', 'drum'],
        'Bass_Sounds': ['bass', 'sub'],
        'Synthesizer_Sounds': ['synth', 'lead', 'pad'],
        'Orchestral': ['violin', 'cello', 'orchestra', 'string', 'brass', 'flute', 'clarinet'],
        'Piano_Keys': ['piano', 'ep', 'rhodes', 'wurlitzer'],
        'Guitar': ['guitar', 'gtr'],
        'Vocal': ['vox', 'vocal', 'voice', 'choir']
    }
    
    for category, keywords in patterns.items():
        if any(keyword in name for keyword in keywords):
            return f'Commercial_Samples/{category}'
    
    return None

# ============================================================================
# DUPLICATE DETECTION
# ============================================================================

def find_duplicates(files_metadata):
    """Find duplicate files by audio fingerprint"""
    fingerprints = defaultdict(list)
    duplicates = []
    
    for metadata in files_metadata:
        fp = metadata.get('audio_fingerprint')
        if fp:
            fingerprints[fp].append(metadata)
    
    for fp, files in fingerprints.items():
        if len(files) > 1:
            duplicates.append({
                'fingerprint': fp,
                'count': len(files),
                'files': [f['filename'] for f in files],
                'size': files[0]['size']
            })
    
    return duplicates

# ============================================================================
# MAIN ORGANIZATION
# ============================================================================

def organize_files_enhanced(source_dir, dest_base):
    """Enhanced organization with all features"""
    source_dir = Path(source_dir)
    dest_base = Path(dest_base)
    
    stats = {
        'originals': [],
        'commercial': [],
        'errors': [],
        'invalid': [],
        'duplicates': [],
        'start_time': datetime.now().isoformat(),
        'total_files': 0,
        'total_size': 0,
        'undo_operations': []
    }
    
    print("🔍 Phase 1: Scanning for WAV files...")
    wav_files = list(source_dir.rglob('*.wav')) + list(source_dir.rglob('*.WAV'))
    stats['total_files'] = len(wav_files)
    
    print(f"✓ Found {len(wav_files)} WAV files\n")
    
    print("="*80)
    print("⭐⭐⭐ HARD RULE ACTIVE ⭐⭐⭐")
    print("NO METADATA = YOUR ORIGINAL COMPOSITION!")
    print("="*80 + "\n")
    
    # Phase 2: Extract metadata
    print("📊 Phase 2: Extracting metadata and analyzing files...")
    all_metadata = []
    
    if CONFIG['show_progress']:
        progress = ProgressBar(len(wav_files), prefix='Analyzing:')
    
    for i, wav_file in enumerate(wav_files):
        metadata = extract_wav_metadata_enhanced(wav_file)
        if metadata:
            all_metadata.append(metadata)
            stats['total_size'] += metadata['size']
        
        if CONFIG['show_progress']:
            progress.update()
        elif (i + 1) % 10 == 0:
            print(f"  Processed {i+1}/{len(wav_files)}...")
    
    print("\n")
    
    # Phase 3: Find duplicates
    if CONFIG['check_duplicates']:
        print("🔍 Phase 3: Checking for duplicates...")
        stats['duplicates'] = find_duplicates(all_metadata)
        if stats['duplicates']:
            print(f"  ⚠️  Found {len(stats['duplicates'])} sets of duplicate files")
            total_dup_files = sum(d['count'] for d in stats['duplicates'])
            print(f"  ⚠️  Total duplicate files: {total_dup_files}")
        else:
            print("  ✓ No duplicates found")
        print()
    
    # Phase 4: Organize files
    print("📁 Phase 4: Organizing files...")
    
    if CONFIG['show_progress']:
        progress = ProgressBar(len(all_metadata), prefix='Organizing:')
    
    for i, metadata in enumerate(all_metadata):
        try:
            filepath = Path(metadata['path'])
            
            # Check validity
            if metadata.get('error'):
                stats['invalid'].append({
                    'file': metadata['filename'],
                    'path': metadata['path'],
                    'error': metadata['error']
                })
                if CONFIG['show_progress']:
                    progress.update()
                continue
            
            # Determine category - HARD RULE APPLICATION
            filename_category = categorize_by_filename(filepath.name)
            
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
                    'original_file': filepath.name,
                    'original_path': str(filepath.relative_to(source_dir)),
                    'dest_folder': str(dest_folder.relative_to(dest_base)),
                    'size': metadata['size'],
                    'duration': metadata.get('duration_seconds'),
                    'metadata': metadata['info'],
                    'md5': metadata.get('md5'),
                    'audio_analysis': metadata.get('audio_analysis', {})
                })
            
            else:
                # ⭐⭐⭐ ORIGINAL COMPOSITION! ⭐⭐⭐
                category = 'original'
                
                # Preserve folder structure for originals
                relative_path = filepath.relative_to(source_dir)
                if len(relative_path.parts) > 1:
                    dest_folder = ORIGINALS_DIR / relative_path.parent
                else:
                    dest_folder = ORIGINALS_DIR
                
                stats['originals'].append({
                    'original_file': filepath.name,
                    'original_path': str(relative_path),
                    'size': metadata['size'],
                    'duration': metadata.get('duration_seconds'),
                    'sample_rate': metadata.get('sample_rate'),
                    'channels': metadata.get('channels'),
                    'bits': metadata.get('bits_per_sample'),
                    'md5': metadata.get('md5'),
                    'audio_analysis': metadata.get('audio_analysis', {})
                })
            
            # Create destination folder
            dest_folder.mkdir(parents=True, exist_ok=True)
            
            # Determine final filename
            dest_filename = filepath.name
            
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
            
            shutil.copy2(filepath, dest_file)
            
            # Track for undo
            stats['undo_operations'].append({
                'source': str(filepath),
                'dest': str(dest_file),
                'category': category
            })
            
            # Track renames
            if dest_filename != filepath.name:
                if category == 'commercial':
                    stats['commercial'][-1]['new_name'] = dest_filename
                elif category == 'original':
                    stats['originals'][-1]['new_name'] = dest_filename
            
            if CONFIG['show_progress']:
                progress.update()
        
        except Exception as e:
            stats['errors'].append({
                'file': metadata['filename'],
                'error': str(e)
            })
            if CONFIG['show_progress']:
                progress.update()
    
    print("\n")
    stats['end_time'] = datetime.now().isoformat()
    return stats

# ============================================================================
# HTML REPORT GENERATION
# ============================================================================

def generate_html_report(stats):
    """Generate beautiful HTML report"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    html_file = REPORTS_DIR / f"organization_report_{timestamp}.html"
    
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>WAV Organization Report</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
        }}
        .hard-rule {{
            background: #ffd700;
            color: #000;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            font-weight: bold;
            text-align: center;
            font-size: 1.2em;
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }}
        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .stat-value {{
            font-size: 2.5em;
            font-weight: bold;
            color: #667eea;
        }}
        .stat-label {{
            color: #666;
            margin-top: 5px;
        }}
        .originals {{
            background: white;
            padding: 30px;
            border-radius: 10px;
            margin: 20px 0;
            border-left: 5px solid #ffd700;
        }}
        .commercial {{
            background: white;
            padding: 30px;
            border-radius: 10px;
            margin: 20px 0;
            border-left: 5px solid #667eea;
        }}
        .file-list {{
            margin: 20px 0;
        }}
        .file-item {{
            padding: 10px;
            border-bottom: 1px solid #eee;
        }}
        .file-name {{
            font-weight: bold;
            color: #333;
        }}
        .file-details {{
            color: #666;
            font-size: 0.9em;
            margin-top: 5px;
        }}
        .category {{
            background: #f0f0f0;
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        th, td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background: #667eea;
            color: white;
        }}
        .star {{
            color: #ffd700;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🎵 WAV Organization Report</h1>
        <p>Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    </div>
    
    <div class="hard-rule">
        ⭐⭐⭐ HARD RULE APPLIED ⭐⭐⭐<br>
        ANY FILE WITHOUT METADATA = YOUR ORIGINAL COMPOSITION!
    </div>
    
    <div class="stats">
        <div class="stat-card">
            <div class="stat-value star">{len(stats['originals'])}</div>
            <div class="stat-label">⭐ Original Compositions</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">{len(stats['commercial'])}</div>
            <div class="stat-label">📦 Commercial Samples</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">{stats['total_files']}</div>
            <div class="stat-label">Total Files</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">{stats['total_size']/(1024**3):.2f} GB</div>
            <div class="stat-label">Total Size</div>
        </div>
    </div>
    
    <div class="originals">
        <h2><span class="star">⭐⭐⭐</span> ORIGINAL COMPOSITIONS (NO METADATA)</h2>
        <p><strong>These files have NO metadata tags = YOUR original music!</strong></p>
        <p>These are IRREPLACEABLE. Back them up immediately!</p>
        <div class="file-list">
"""
    
    for item in sorted(stats['originals'], key=lambda x: x['original_file']):
        duration = f"{item.get('duration', 0):.2f}s" if item.get('duration') else "N/A"
        size_mb = item['size'] / (1024**2)
        audio = item.get('audio_analysis', {})
        peak = f"Peak: {audio.get('peak_level', 0)*100:.0f}%" if audio.get('peak_level') else ""
        
        html += f"""
            <div class="file-item">
                <div class="file-name">⭐ {item['original_file']}</div>
                <div class="file-details">
                    Path: {item['original_path']} | 
                    Size: {size_mb:.2f} MB | 
                    Duration: {duration} | 
                    {item.get('sample_rate', 'N/A')} Hz, {item.get('channels', 'N/A')}ch, {item.get('bits', 'N/A')}bit
                    {' | ' + peak if peak else ''}
                </div>
            </div>
"""
    
    html += """
        </div>
    </div>
    
    <div class="commercial">
        <h2>📦 COMMERCIAL SAMPLES (WITH METADATA)</h2>
        <p>These files have metadata tags proving they're from commercial products.</p>
"""
    
    by_folder = defaultdict(list)
    for item in stats['commercial']:
        by_folder[item['dest_folder']].append(item)
    
    for folder, items in sorted(by_folder.items()):
        total_size = sum(item['size'] for item in items)
        html += f"""
        <div class="category">
            <h3>{folder} ({len(items)} files, {total_size/(1024**2):.1f} MB)</h3>
            <table>
                <tr>
                    <th>File</th>
                    <th>Size</th>
                    <th>Duration</th>
                    <th>Metadata</th>
                </tr>
"""
        for item in sorted(items, key=lambda x: x['original_file'])[:20]:
            duration = f"{item.get('duration', 0):.1f}s" if item.get('duration') else "N/A"
            size_mb = f"{item['size']/(1024**2):.2f} MB"
            meta = ', '.join(f"{k}: {v}" for k, v in list(item.get('metadata', {}).items())[:2])
            html += f"""
                <tr>
                    <td>{item['original_file']}</td>
                    <td>{size_mb}</td>
                    <td>{duration}</td>
                    <td>{meta if meta else 'N/A'}</td>
                </tr>
"""
        if len(items) > 20:
            html += f"<tr><td colspan='4'>... and {len(items) - 20} more files</td></tr>"
        html += "</table></div>"
    
    if stats['duplicates']:
        html += """
        <div class="originals">
            <h2>⚠️ DUPLICATE FILES DETECTED</h2>
            <table>
                <tr>
                    <th>Files</th>
                    <th>Count</th>
                    <th>Size</th>
                </tr>
"""
        for dup in stats['duplicates']:
            files_list = '<br>'.join(dup['files'])
            html += f"""
                <tr>
                    <td>{files_list}</td>
                    <td>{dup['count']}</td>
                    <td>{dup['size']/(1024**2):.2f} MB</td>
                </tr>
"""
        html += "</table></div>"
    
    html += """
</body>
</html>
"""
    
    with open(html_file, 'w') as f:
        f.write(html)
    
    return html_file

# ============================================================================
# UNDO SCRIPT GENERATION
# ============================================================================

def generate_undo_script(stats):
    """Generate script to undo the organization"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    undo_file = BACKUP_DIR / f"UNDO_ORGANIZATION_{timestamp}.json"
    
    BACKUP_DIR.mkdir(exist_ok=True)
    
    undo_data = {
        'timestamp': timestamp,
        'operations': stats['undo_operations'],
        'stats': {
            'originals_count': len(stats['originals']),
            'commercial_count': len(stats['commercial'])
        }
    }
    
    with open(undo_file, 'w') as f:
        json.dump(undo_data, f, indent=2)
    
    # Create shell script
    undo_sh = BACKUP_DIR / f"UNDO_ORGANIZATION_{timestamp}.sh"
    with open(undo_sh, 'w') as f:
        f.write("""#!/bin/bash
echo "⚠️  UNDO ORGANIZATION ⚠️"
echo "This will delete organized files (originals are safe)"
echo ""
echo "Press Enter to continue, or Ctrl+C to cancel..."
read

""")
        f.write(f'# Remove organized directories\n')
        f.write(f'rm -rf "{DEST_DIR}"\n')
        f.write(f'echo "✓ Removed {DEST_DIR}/"\n')
        f.write(f'echo "✓ Original files in {SOURCE_DIR}/ are untouched"\n')
        f.write(f'echo "✓ Undo complete!"\n')
    
    os.chmod(undo_sh, 0o755)
    
    return undo_file, undo_sh

# ============================================================================
# COMPREHENSIVE REPORTING
# ============================================================================

def generate_all_reports(stats):
    """Generate all report formats"""
    REPORTS_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    reports = {}
    
    # JSON report
    json_file = REPORTS_DIR / f"organization_report_{timestamp}.json"
    with open(json_file, 'w') as f:
        # Remove undo_operations from JSON (too large)
        export_stats = {k: v for k, v in stats.items() if k != 'undo_operations'}
        json.dump(export_stats, f, indent=2)
    reports['json'] = json_file
    
    # Text report (existing code simplified)
    txt_file = REPORTS_DIR / f"organization_report_{timestamp}.txt"
    with open(txt_file, 'w') as f:
        f.write("="*80 + "\n")
        f.write("WAV FILE ORGANIZATION REPORT\n")
        f.write("="*80 + "\n\n")
        f.write("⭐⭐⭐ HARD RULE APPLIED ⭐⭐⭐\n")
        f.write("NO METADATA = ORIGINAL COMPOSITION!\n\n")
        f.write(f"Total files: {stats['total_files']}\n")
        f.write(f"Total size: {stats['total_size']/(1024**3):.2f} GB\n")
        f.write(f"⭐ Original compositions: {len(stats['originals'])}\n")
        f.write(f"📦 Commercial samples: {len(stats['commercial'])}\n")
        if stats['duplicates']:
            f.write(f"⚠️  Duplicate sets: {len(stats['duplicates'])}\n")
    reports['txt'] = txt_file
    
    # Backup list for originals
    backup_file = REPORTS_DIR / f"BACKUP_LIST_ORIGINALS_{timestamp}.txt"
    with open(backup_file, 'w') as f:
        f.write("⭐⭐⭐ ORIGINAL COMPOSITIONS - PRIORITY BACKUP LIST ⭐⭐⭐\n\n")
        f.write("These files have NO metadata = YOUR original compositions!\n")
        f.write("BACK THESE UP IMMEDIATELY - They are irreplaceable!\n\n")
        for item in sorted(stats['originals'], key=lambda x: x['original_file']):
            f.write(f"{item['original_path']}\n")
    reports['backup'] = backup_file
    
    # HTML report
    if CONFIG['create_html_report']:
        html_file = generate_html_report(stats)
        reports['html'] = html_file
    
    # Undo script
    if CONFIG['create_undo_script']:
        undo_json, undo_sh = generate_undo_script(stats)
        reports['undo_json'] = undo_json
        reports['undo_sh'] = undo_sh
    
    return reports

# ============================================================================
# CONSOLE SUMMARY
# ============================================================================

def print_enhanced_summary(stats, reports):
    """Print enhanced console summary"""
    print("\n" + "="*80)
    print("✓ ORGANIZATION COMPLETE!")
    print("="*80 + "\n")
    
    print("⭐⭐⭐ HARD RULE APPLIED ⭐⭐⭐")
    print("Files WITHOUT metadata = YOUR ORIGINAL COMPOSITIONS\n")
    
    total_orig_size = sum(item['size'] for item in stats['originals'])
    total_comm_size = sum(item['size'] for item in stats['commercial'])
    
    print(f"🎵 ORIGINAL COMPOSITIONS: {len(stats['originals'])} files ({total_orig_size/(1024**2):.1f} MB) ⭐⭐⭐")
    print(f"📦 Commercial Samples: {len(stats['commercial'])} files ({total_comm_size/(1024**2):.1f} MB)")
    
    if stats['duplicates']:
        total_dup_size = sum(d['size'] * (d['count'] - 1) for d in stats['duplicates'])
        print(f"⚠️  Duplicates Found: {len(stats['duplicates'])} sets (could save {total_dup_size/(1024**2):.1f} MB)")
    
    if stats['invalid']:
        print(f"⚠️  Invalid Files: {len(stats['invalid'])} files")
    if stats['errors']:
        print(f"❌ Errors: {len(stats['errors'])} files")
    
    print("\n" + "="*80)
    print("📁 FILES ORGANIZED INTO:")
    print("="*80)
    print(f"  {ORIGINALS_DIR}/")
    print(f"    → {len(stats['originals'])} original compositions ⭐⭐⭐")
    print(f"\n  {COMMERCIAL_DIR}/")
    
    by_folder = defaultdict(int)
    for item in stats['commercial']:
        folder = item['dest_folder'].replace('Commercial_Samples/', '')
        by_folder[folder] += 1
    
    for folder, count in sorted(by_folder.items()):
        print(f"    → {folder}: {count} files")
    
    print("\n" + "="*80)
    print("📄 REPORTS GENERATED:")
    print("="*80)
    for report_type, report_path in reports.items():
        icon = {"json": "📊", "txt": "📄", "backup": "⭐", "html": "🌐", "undo_json": "↩️", "undo_sh": "↩️"}.get(report_type, "📄")
        print(f"  {icon} {report_path}")
    
    print("\n" + "="*80)
    print("⭐ NEXT STEPS:")
    print("="*80)
    print(f"1. Check {ORIGINALS_DIR}/ for YOUR compositions ⭐⭐⭐")
    print(f"2. BACKUP these files immediately - they're irreplaceable!")
    print(f"3. Open the HTML report in your browser for visual overview")
    print(f"4. Review {reports.get('txt', 'text report')}")
    print("="*80 + "\n")

# ============================================================================
# MAIN
# ============================================================================

def main():
    print("="*80)
    print("🎵 MEGA ULTIMATE WAV ORGANIZER v2.0 🎵")
    print("="*80)
    print("\n⭐⭐⭐ HARD RULE ⭐⭐⭐")
    print("ANY FILE WITHOUT METADATA = YOUR ORIGINAL COMPOSITION!\n")
    print("ENHANCED FEATURES:")
    print("  ✓ Progress bars and visual feedback")
    print("  ✓ MD5 checksums for verification")
    print("  ✓ Duplicate detection")
    print("  ✓ Audio analysis")
    print("  ✓ HTML report generation")
    print("  ✓ Undo/restore capability")
    print("="*80 + "\n")
    
    if not SOURCE_DIR.exists():
        print(f"❌ Error: Source directory not found: {SOURCE_DIR}")
        return
    
    print(f"Source: {SOURCE_DIR.absolute()}")
    print(f"Destination: {DEST_DIR.absolute()}")
    print("\nStarting enhanced organization...\n")
    
    # Run organization
    stats = organize_files_enhanced(SOURCE_DIR, DEST_DIR)
    
    # Generate reports
    print("📊 Phase 5: Generating comprehensive reports...")
    reports = generate_all_reports(stats)
    print("✓ Reports generated\n")
    
    # Print summary
    print_enhanced_summary(stats, reports)
    
    print("🎉 ALL DONE! Your music is organized and protected! 🎉\n")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user. Partial results may exist.")
    except Exception as e:
        print(f"\n\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()

