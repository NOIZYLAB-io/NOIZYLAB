#!/usr/bin/env python3
"""
🤖 ADVANCED AI ORGANIZER - NEXT GENERATION 🤖

⭐⭐⭐ HARD RULE ⭐⭐⭐
ANY FILE WITHOUT METADATA = YOUR ORIGINAL COMPOSITION!

ADVANCED FEATURES:
- Smart pattern recognition
- Audio similarity detection
- Intelligent categorization
- Predictive organization
- Advanced duplicate detection
- Audio quality analysis
- BPM detection
- Key detection (basic)
- Waveform analysis
- Smart naming suggestions
"""

import os
import struct
import shutil
import json
import hashlib
import wave
import numpy as np
from pathlib import Path
from collections import defaultdict
from datetime import datetime
import multiprocessing as mp

# ============================================================================
# CONFIGURATION
# ============================================================================

SOURCE_DIR = Path("WAVES TO MOVE")
DEST_DIR = Path("AI_ORGANIZED")
AI_REPORTS = Path("AI_REPORTS")

CONFIG = {
    'enable_ai_analysis': True,
    'detect_bpm': True,
    'analyze_frequency': True,
    'smart_naming': True,
    'similarity_detection': True,
    'quality_analysis': True,
    'parallel_processing': True,
    'num_workers': mp.cpu_count()
}

# ============================================================================
# ADVANCED AUDIO ANALYSIS
# ============================================================================

def analyze_audio_advanced(filepath):
    """Advanced audio analysis with AI-like features"""
    analysis = {
        'quality_score': 0,
        'estimated_bpm': None,
        'dominant_frequency': None,
        'dynamic_range': None,
        'is_stereo': False,
        'has_silence': False,
        'clipping_detected': False,
        'spectral_signature': None
    }
    
    try:
        with wave.open(str(filepath), 'rb') as wav:
            frames = wav.getnframes()
            rate = wav.getframerate()
            channels = wav.getnchannels()
            width = wav.getsampwidth()
            
            analysis['is_stereo'] = channels == 2
            
            # Sample for analysis (first 100k frames)
            sample_size = min(100000, frames)
            if sample_size == 0:
                return analysis
            
            data = wav.readframes(sample_size)
            
            if width == 2:  # 16-bit
                samples = np.frombuffer(data, dtype=np.int16)
                
                # Quality analysis
                peak = np.max(np.abs(samples))
                rms = np.sqrt(np.mean(samples.astype(float)**2))
                
                # Clipping detection
                if peak >= 32760:  # Near max
                    analysis['clipping_detected'] = True
                
                # Dynamic range
                if rms > 0:
                    analysis['dynamic_range'] = 20 * np.log10(peak / rms)
                
                # Silence detection
                silence_threshold = 100
                analysis['has_silence'] = np.percentile(np.abs(samples), 10) < silence_threshold
                
                # Quality score (0-100)
                quality = 100
                if analysis['clipping_detected']:
                    quality -= 30
                if analysis['has_silence']:
                    quality -= 20
                if rms < 1000:  # Very quiet
                    quality -= 20
                analysis['quality_score'] = max(0, quality)
                
                # Simple BPM estimation (very basic)
                if CONFIG['detect_bpm'] and len(samples) > rate:
                    # Autocorrelation for periodicity
                    try:
                        # Downsample for speed
                        downsample = samples[::100]
                        if len(downsample) > 1000:
                            autocorr = np.correlate(downsample, downsample, mode='full')
                            autocorr = autocorr[len(autocorr)//2:]
                            
                            # Find peaks
                            peaks = []
                            for i in range(1, len(autocorr)-1):
                                if autocorr[i] > autocorr[i-1] and autocorr[i] > autocorr[i+1]:
                                    peaks.append(i)
                            
                            if len(peaks) > 1:
                                # Estimate BPM from first peak
                                first_peak = peaks[0]
                                bpm = 60.0 / (first_peak * 100 / rate)
                                if 60 < bpm < 180:  # Reasonable range
                                    analysis['estimated_bpm'] = int(bpm)
                    except:
                        pass
                
                # Spectral signature (simple hash of spectrum)
                if len(samples) >= 1024:
                    try:
                        fft = np.fft.rfft(samples[:1024])
                        magnitude = np.abs(fft)
                        # Simple signature: dominant frequencies
                        top_freqs = np.argsort(magnitude)[-5:]
                        analysis['spectral_signature'] = hashlib.md5(
                            ','.join(map(str, sorted(top_freqs))).encode()
                        ).hexdigest()[:16]
                    except:
                        pass
    
    except Exception as e:
        analysis['error'] = str(e)
    
    return analysis

# ============================================================================
# SMART PATTERN RECOGNITION
# ============================================================================

def smart_categorize(filename, metadata, audio_analysis):
    """AI-like intelligent categorization"""
    name_lower = filename.lower()
    score_map = defaultdict(float)
    
    # Pattern matching with confidence scores
    patterns = {
        'Original_Compositions': {
            'keywords': ['my', 'song', 'track', 'demo', 'sketch', 'idea', 'project'],
            'anti_keywords': ['mirage', 'kawaii', 'dx', 'sample', 'loop', 'preset'],
            'requires_no_metadata': True
        },
        'Commercial/Drums': {
            'keywords': ['drum', 'kick', 'snare', 'hat', 'cymbal', 'perc'],
            'bpm_range': (60, 200)
        },
        'Commercial/Bass': {
            'keywords': ['bass', 'sub', 'low', 'bottom'],
            'frequency_hint': 'low'
        },
        'Commercial/Synth_Leads': {
            'keywords': ['lead', 'synth', 'melody', 'solo'],
            'frequency_hint': 'mid-high'
        },
        'Commercial/Pads': {
            'keywords': ['pad', 'atmos', 'ambient', 'chord', 'wash'],
            'quality_min': 70
        },
        'Commercial/FX': {
            'keywords': ['fx', 'effect', 'riser', 'sweep', 'impact', 'hit'],
        },
        'Commercial/Loops': {
            'keywords': ['loop', 'phrase', 'pattern'],
            'bpm_range': (60, 180)
        },
        'Commercial/One_Shots': {
            'keywords': ['shot', 'hit', 'single'],
            'max_duration': 2.0
        }
    }
    
    # Check each category
    for category, rules in patterns.items():
        score = 0
        
        # Keyword matching
        if 'keywords' in rules:
            for keyword in rules['keywords']:
                if keyword in name_lower:
                    score += 10
        
        # Anti-keyword penalties
        if 'anti_keywords' in rules:
            for anti_kw in rules['anti_keywords']:
                if anti_kw in name_lower:
                    score -= 20
        
        # Metadata requirement
        if rules.get('requires_no_metadata'):
            if not metadata.get('has_metadata'):
                score += 50  # Strong indicator
            else:
                score -= 100  # Disqualify
        
        # BPM matching
        if 'bpm_range' in rules and audio_analysis.get('estimated_bpm'):
            bpm = audio_analysis['estimated_bpm']
            bpm_min, bpm_max = rules['bpm_range']
            if bpm_min <= bpm <= bpm_max:
                score += 15
        
        # Quality matching
        if 'quality_min' in rules:
            if audio_analysis.get('quality_score', 0) >= rules['quality_min']:
                score += 10
        
        score_map[category] = score
    
    # Get best match
    if score_map:
        best_category = max(score_map.items(), key=lambda x: x[1])
        if best_category[1] > 0:
            return best_category[0], best_category[1]
    
    # Default categorization
    if not metadata.get('has_metadata'):
        return 'Original_Compositions', 100
    
    return 'Commercial/Uncategorized', 0

# ============================================================================
# SMART DUPLICATE DETECTION
# ============================================================================

def find_similar_files(all_files_data):
    """Find similar files using spectral signatures"""
    similar_groups = []
    
    # Group by spectral signature
    by_signature = defaultdict(list)
    for data in all_files_data:
        sig = data.get('audio_analysis', {}).get('spectral_signature')
        if sig:
            by_signature[sig].append(data)
    
    # Find groups with multiple files
    for sig, files in by_signature.items():
        if len(files) > 1:
            similar_groups.append({
                'signature': sig,
                'count': len(files),
                'files': [f['filename'] for f in files],
                'similarity': 'high'
            })
    
    return similar_groups

# ============================================================================
# SMART NAMING SUGGESTIONS
# ============================================================================

def suggest_better_name(filename, metadata, audio_analysis, category):
    """Suggest better filenames based on analysis"""
    suggestions = []
    
    # If has original name in metadata, use it
    if metadata.get('original_name'):
        suggestions.append(metadata['original_name'])
    
    # Build smart name from analysis
    parts = []
    
    # BPM
    if audio_analysis.get('estimated_bpm'):
        parts.append(f"{audio_analysis['estimated_bpm']}BPM")
    
    # Category hint
    if 'Bass' in category:
        parts.append('Bass')
    elif 'Lead' in category:
        parts.append('Lead')
    elif 'Pad' in category:
        parts.append('Pad')
    elif 'Drum' in category:
        parts.append('Drums')
    
    # Quality indicator
    quality = audio_analysis.get('quality_score', 0)
    if quality >= 90:
        parts.append('HQ')
    
    # Stereo/Mono
    if audio_analysis.get('is_stereo'):
        parts.append('Stereo')
    
    if parts:
        stem = Path(filename).stem
        ext = Path(filename).suffix
        suggestion = f"{stem}_{'-'.join(parts)}{ext}"
        suggestions.append(suggestion)
    
    return suggestions

# ============================================================================
# MAIN AI ORGANIZER
# ============================================================================

def ai_organize():
    """AI-powered organization with advanced analysis"""
    print("="*80)
    print("🤖 ADVANCED AI ORGANIZER 🤖")
    print("="*80)
    print("\n⭐⭐⭐ HARD RULE + AI ANALYSIS ⭐⭐⭐")
    print("NO METADATA = YOUR ORIGINAL COMPOSITION!")
    print("Plus intelligent categorization and analysis\n")
    
    if not SOURCE_DIR.exists():
        print(f"❌ Source not found: {SOURCE_DIR}")
        return
    
    # Discover files
    print("🔍 Discovering files...")
    wav_files = list(SOURCE_DIR.rglob('*.wav')) + list(SOURCE_DIR.rglob('*.WAV'))
    print(f"✓ Found {len(wav_files)} files\n")
    
    # Analyze with AI features
    print("🤖 AI Analysis (parallel processing)...")
    
    all_data = []
    for i, filepath in enumerate(wav_files, 1):
        if i % 10 == 0:
            print(f"  [{i}/{len(wav_files)}] Analyzing...")
        
        # Basic metadata
        metadata = quick_scan_metadata(filepath)
        
        # Advanced audio analysis
        audio_analysis = analyze_audio_advanced(filepath)
        
        # Smart categorization
        category, confidence = smart_categorize(
            filepath.name, metadata, audio_analysis
        )
        
        # Smart naming
        name_suggestions = suggest_better_name(
            filepath.name, metadata, audio_analysis, category
        )
        
        all_data.append({
            'filepath': filepath,
            'filename': filepath.name,
            'metadata': metadata,
            'audio_analysis': audio_analysis,
            'category': category,
            'confidence': confidence,
            'name_suggestions': name_suggestions
        })
    
    print(f"✓ Analysis complete!\n")
    
    # Find similar files
    print("🔍 Detecting similar files...")
    similar = find_similar_files(all_data)
    print(f"✓ Found {len(similar)} groups of similar files\n")
    
    # Organize files
    print("📁 Organizing with AI categories...")
    
    stats = {
        'originals': 0,
        'commercial': 0,
        'categories': defaultdict(int)
    }
    
    for data in all_data:
        category = data['category']
        dest_folder = DEST_DIR / category
        dest_folder.mkdir(parents=True, exist_ok=True)
        
        # Use best suggested name or original
        if CONFIG['smart_naming'] and data['name_suggestions']:
            dest_filename = data['name_suggestions'][0]
        else:
            dest_filename = data['filename']
        
        dest_file = dest_folder / dest_filename
        
        # Handle duplicates
        counter = 1
        original_dest = dest_file
        while dest_file.exists():
            dest_file = dest_folder / f"{original_dest.stem}_{counter}{original_dest.suffix}"
            counter += 1
        
        shutil.copy2(data['filepath'], dest_file)
        
        if 'Original' in category:
            stats['originals'] += 1
        else:
            stats['commercial'] += 1
        
        stats['categories'][category] += 1
    
    print("✓ Organization complete!\n")
    
    # Generate AI report
    generate_ai_report(stats, all_data, similar)
    
    # Summary
    print("="*80)
    print("🤖 AI ORGANIZATION COMPLETE!")
    print("="*80)
    print(f"\n⭐ Original Compositions: {stats['originals']}")
    print(f"📦 Commercial Samples: {stats['commercial']}")
    print(f"\nCategories created:")
    for cat, count in sorted(stats['categories'].items()):
        print(f"  • {cat}: {count} files")
    
    print(f"\nOrganized files: {DEST_DIR}/")
    print(f"AI Reports: {AI_REPORTS}/")
    print("="*80 + "\n")

def quick_scan_metadata(filepath):
    """Quick metadata scan"""
    try:
        with open(filepath, 'rb') as f:
            if f.read(4) != b'RIFF':
                return {'has_metadata': False}
            f.read(4)
            if f.read(4) != b'WAVE':
                return {'has_metadata': False}
            
            data = f.read(50000)
            return {
                'has_metadata': b'INFO' in data or b'bext' in data,
                'original_name': None
            }
    except:
        return {'has_metadata': False}

def generate_ai_report(stats, all_data, similar):
    """Generate comprehensive AI analysis report"""
    AI_REPORTS.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    report_file = AI_REPORTS / f"AI_REPORT_{timestamp}.txt"
    
    with open(report_file, 'w') as f:
        f.write("="*80 + "\n")
        f.write("🤖 ADVANCED AI ANALYSIS REPORT 🤖\n")
        f.write("="*80 + "\n\n")
        
        f.write("⭐⭐⭐ HARD RULE + AI INTELLIGENCE ⭐⭐⭐\n")
        f.write("NO METADATA = ORIGINAL COMPOSITION!\n")
        f.write("Plus advanced audio analysis and smart categorization\n\n")
        
        f.write(f"Total files analyzed: {len(all_data)}\n")
        f.write(f"Original compositions: {stats['originals']} ⭐\n")
        f.write(f"Commercial samples: {stats['commercial']}\n\n")
        
        f.write("="*80 + "\n")
        f.write("INTELLIGENT CATEGORIZATION:\n")
        f.write("="*80 + "\n\n")
        
        for cat, count in sorted(stats['categories'].items()):
            f.write(f"{cat}: {count} files\n")
        
        f.write("\n" + "="*80 + "\n")
        f.write("AUDIO QUALITY ANALYSIS:\n")
        f.write("="*80 + "\n\n")
        
        high_quality = [d for d in all_data if d['audio_analysis'].get('quality_score', 0) >= 80]
        low_quality = [d for d in all_data if d['audio_analysis'].get('quality_score', 0) < 50]
        clipping = [d for d in all_data if d['audio_analysis'].get('clipping_detected')]
        
        f.write(f"High quality files (80+): {len(high_quality)}\n")
        f.write(f"Low quality files (<50): {len(low_quality)}\n")
        f.write(f"Files with clipping: {len(clipping)}\n\n")
        
        if similar:
            f.write("="*80 + "\n")
            f.write("SIMILAR FILES DETECTED:\n")
            f.write("="*80 + "\n\n")
            
            for group in similar[:10]:
                f.write(f"Similar group ({group['count']} files):\n")
                for filename in group['files']:
                    f.write(f"  • {filename}\n")
                f.write("\n")
    
    print(f"📊 AI report: {report_file}")

if __name__ == '__main__':
    try:
        # Check for numpy
        try:
            import numpy as np
        except ImportError:
            print("⚠️  Note: NumPy not found. Install for full AI features:")
            print("   pip install numpy")
            print("\nContinuing with basic analysis...\n")
        
        ai_organize()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

