#!/usr/bin/env python3
"""
Music Analyzer - Fish Music Inc
Intelligent music file analysis, metadata scanning, quality assessment
"""

import os
import sys
import librosa
import soundfile as sf
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.progress import track
import numpy as np
import json

console = Console()

class MusicAnalyzer:
    """Analyze audio files for quality, characteristics, and properties"""
    
    def __init__(self, audio_path):
        self.audio_path = Path(audio_path)
        self.analysis = {}
        
    def analyze_file(self):
        """Perform complete analysis on audio file"""
        console.print(f"\n[bold cyan]🎵 Analyzing: {self.audio_path.name}[/bold cyan]\n")
        
        try:
            # Load audio
            y, sr = librosa.load(str(self.audio_path), sr=None)
            duration = librosa.get_duration(y=y, sr=sr)
            
            # Basic properties
            self.analysis['basic'] = {
                'filename': self.audio_path.name,
                'path': str(self.audio_path),
                'duration': round(duration, 2),
                'sample_rate': sr,
                'channels': 'stereo' if len(y.shape) > 1 else 'mono',
                'samples': len(y)
            }
            
            # Audio quality metrics
            self.analysis['quality'] = self._analyze_quality(y, sr)
            
            # Musical characteristics
            self.analysis['music'] = self._analyze_music(y, sr)
            
            # Spectral analysis
            self.analysis['spectral'] = self._analyze_spectral(y, sr)
            
            # Display results
            self._display_results()
            
            return self.analysis
            
        except Exception as e:
            console.print(f"[red]❌ Error analyzing file: {e}[/red]")
            return None
    
    def _analyze_quality(self, y, sr):
        """Analyze audio quality metrics"""
        # RMS energy
        rms = librosa.feature.rms(y=y)[0]
        rms_mean = float(np.mean(rms))
        rms_max = float(np.max(rms))
        
        # Dynamic range
        db = librosa.amplitude_to_db(np.abs(y), ref=np.max)
        dynamic_range = float(np.max(db) - np.min(db))
        
        # Peak level
        peak_level = float(20 * np.log10(np.max(np.abs(y))))
        
        # Clipping detection
        clipping_count = int(np.sum(np.abs(y) >= 0.99))
        clipping_percentage = float((clipping_count / len(y)) * 100)
        
        return {
            'rms_mean': round(rms_mean, 6),
            'rms_max': round(rms_max, 6),
            'dynamic_range_db': round(dynamic_range, 2),
            'peak_level_db': round(peak_level, 2),
            'clipping_samples': clipping_count,
            'clipping_percentage': round(clipping_percentage, 4)
        }
    
    def _analyze_music(self, y, sr):
        """Analyze musical characteristics"""
        # Tempo estimation
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
        
        # Key estimation (chromagram)
        chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
        
        # Spectral centroid (brightness)
        spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
        
        return {
            'tempo_bpm': round(float(tempo), 2),
            'beat_count': len(beats),
            'brightness_hz': round(float(np.mean(spectral_centroid)), 2)
        }
    
    def _analyze_spectral(self, y, sr):
        """Analyze spectral characteristics"""
        # Spectral rolloff
        rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)[0]
        
        # Zero crossing rate
        zcr = librosa.feature.zero_crossing_rate(y)[0]
        
        # Spectral bandwidth
        bandwidth = librosa.feature.spectral_bandwidth(y=y, sr=sr)[0]
        
        return {
            'rolloff_hz': round(float(np.mean(rolloff)), 2),
            'zero_crossing_rate': round(float(np.mean(zcr)), 6),
            'bandwidth_hz': round(float(np.mean(bandwidth)), 2)
        }
    
    def _display_results(self):
        """Display analysis results in beautiful format"""
        # Basic info
        basic_table = Table(title="📊 Basic Properties")
        basic_table.add_column("Property", style="cyan")
        basic_table.add_column("Value", style="magenta")
        
        for key, value in self.analysis['basic'].items():
            if key not in ['filename', 'path']:
                basic_table.add_row(key.replace('_', ' ').title(), str(value))
        
        console.print(basic_table)
        console.print()
        
        # Quality metrics
        quality_table = Table(title="✨ Quality Metrics")
        quality_table.add_column("Metric", style="cyan")
        quality_table.add_column("Value", style="magenta")
        
        for key, value in self.analysis['quality'].items():
            quality_table.add_row(key.replace('_', ' ').title(), str(value))
        
        console.print(quality_table)
        console.print()
        
        # Musical characteristics
        music_table = Table(title="🎵 Musical Characteristics")
        music_table.add_column("Characteristic", style="cyan")
        music_table.add_column("Value", style="magenta")
        
        for key, value in self.analysis['music'].items():
            music_table.add_row(key.replace('_', ' ').title(), str(value))
        
        console.print(music_table)
        console.print()


def main():
    if len(sys.argv) < 2:
        console.print("[red]Usage: python analyze.py <audio_file_path>[/red]")
        console.print("\nExample:")
        console.print("  python analyze.py /path/to/audio.wav")
        sys.exit(1)
    
    audio_path = sys.argv[1]
    
    if not os.path.exists(audio_path):
        console.print(f"[red]Error: File not found: {audio_path}[/red]")
        sys.exit(1)
    
    analyzer = MusicAnalyzer(audio_path)
    results = analyzer.analyze_file()
    
    if results:
        # Save results
        output_file = Path(audio_path).stem + '_analysis.json'
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        console.print(f"\n[green]✅ Analysis saved to: {output_file}[/green]\n")


if __name__ == '__main__':
    main()

