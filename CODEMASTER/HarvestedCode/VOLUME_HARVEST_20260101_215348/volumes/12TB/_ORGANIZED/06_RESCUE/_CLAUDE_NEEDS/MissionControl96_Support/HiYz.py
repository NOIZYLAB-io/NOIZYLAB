#!/usr/bin/env python3
"""
Voice Analysis Tool - NoizyFish Audio Edition
Analyze audio files for voice characteristics, emotions, and musical elements
"""

import os
import openai
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import librosa
import numpy as np
import matplotlib.pyplot as plt

class VoiceAnalyzer:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the Voice Analyzer"""
        self.client = openai.OpenAI(
            api_key=api_key or os.getenv('OPENAI_API_KEY')
        )
        self.supported_formats = {'.wav', '.mp3', '.m4a', '.flac', '.aif', '.aiff'}
        
    def extract_audio_features(self, audio_path: str) -> Dict:
        """Extract technical audio features from file"""
        try:
            # Load audio file
            y, sr = librosa.load(audio_path, sr=None)
            duration = librosa.get_duration(y=y, sr=sr)
            
            # Basic features
            features = {
                'file': Path(audio_path).name,
                'duration': duration,
                'sample_rate': sr,
                'channels': 1 if y.ndim == 1 else y.shape[0],
                'length_samples': len(y)
            }
            
            # Spectral features
            spectral_centroids = librosa.feature.spectral_centroid(y=y, sr=sr)[0]
            features['spectral_centroid_mean'] = np.mean(spectral_centroids)
            features['spectral_centroid_std'] = np.std(spectral_centroids)
            
            # Zero crossing rate (voice activity indicator)
            zcr = librosa.feature.zero_crossing_rate(y)[0]
            features['zero_crossing_rate_mean'] = np.mean(zcr)
            
            # MFCC features (voice characteristics)
            mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
            for i in range(13):
                features[f'mfcc_{i+1}_mean'] = np.mean(mfccs[i])
                features[f'mfcc_{i+1}_std'] = np.std(mfccs[i])
            
            # Tempo and rhythm
            tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
            features['tempo'] = tempo
            features['beats_count'] = len(beats)
            
            # Harmonic and percussive components
            y_harmonic, y_percussive = librosa.effects.hpss(y)
            features['harmonic_ratio'] = np.mean(np.abs(y_harmonic)) / (np.mean(np.abs(y)) + 1e-8)
            features['percussive_ratio'] = np.mean(np.abs(y_percussive)) / (np.mean(np.abs(y)) + 1e-8)
            
            # Pitch analysis
            pitches, magnitudes = librosa.piptrack(y=y, sr=sr, fmin=80, fmax=400)
            # Get the pitch with highest magnitude at each time
            pitch_values = []
            for t in range(pitches.shape[1]):
                index = magnitudes[:, t].argmax()
                pitch = pitches[index, t]
                if pitch > 0:
                    pitch_values.append(pitch)
            
            if pitch_values:
                features['fundamental_freq_mean'] = np.mean(pitch_values)
                features['fundamental_freq_std'] = np.std(pitch_values)
                features['pitch_range'] = max(pitch_values) - min(pitch_values)
            else:
                features['fundamental_freq_mean'] = 0
                features['fundamental_freq_std'] = 0
                features['pitch_range'] = 0
            
            # Energy and dynamics
            rms = librosa.feature.rms(y=y)[0]
            features['rms_energy_mean'] = np.mean(rms)
            features['rms_energy_std'] = np.std(rms)
            features['dynamic_range'] = np.max(rms) - np.min(rms)
            
            return features
            
        except Exception as e:
            return {'error': str(e), 'file': Path(audio_path).name}
    
    def transcribe_and_analyze(self, audio_path: str) -> Dict:
        """Transcribe audio and analyze the content"""
        try:
            # Transcribe using Whisper
            with open(audio_path, 'rb') as audio_file:
                transcript = self.client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                    response_format="verbose_json"
                )
            
            return {
                'transcription': transcript.text,
                'language': transcript.language,
                'duration': transcript.duration,
                'segments': transcript.segments if hasattr(transcript, 'segments') else None
            }
            
        except Exception as e:
            return {'error': str(e)}
    
    def analyze_vocal_characteristics(self, audio_features: Dict, transcription: str = "") -> str:
        """Analyze vocal characteristics using AI"""
        
        # Create a comprehensive prompt with technical features
        technical_summary = f"""
        Audio Analysis Data:
        - Duration: {audio_features.get('duration', 'unknown')} seconds
        - Fundamental frequency (pitch): {audio_features.get('fundamental_freq_mean', 0):.2f} Hz (avg)
        - Pitch range: {audio_features.get('pitch_range', 0):.2f} Hz
        - Tempo: {audio_features.get('tempo', 'unknown')} BPM
        - Zero crossing rate: {audio_features.get('zero_crossing_rate_mean', 0):.4f}
        - Spectral centroid: {audio_features.get('spectral_centroid_mean', 0):.2f} Hz
        - RMS energy: {audio_features.get('rms_energy_mean', 0):.4f}
        - Dynamic range: {audio_features.get('dynamic_range', 0):.4f}
        - Harmonic ratio: {audio_features.get('harmonic_ratio', 0):.2f}
        """
        
        if transcription:
            technical_summary += f"\n- Transcribed content: {transcription[:200]}..."
        
        prompt = f"""
        Analyze this audio based on the technical features extracted:
        
        {technical_summary}
        
        Provide analysis for:
        1. **Vocal Characteristics** (if voice is present):
           - Voice type (tenor, bass, soprano, etc.)
           - Vocal quality and timbre
           - Emotional expression
           - Speaking/singing style
           
        2. **Musical Elements**:
           - Key musical characteristics
           - Rhythm and tempo analysis
           - Harmonic content
           - Genre suggestions
           
        3. **Technical Quality**:
           - Recording quality assessment
           - Dynamic range evaluation
           - Frequency balance
           - Potential improvements
           
        4. **Creative Suggestions**:
           - Mixing recommendations
           - Style enhancement ideas
           - Potential uses in music production
           
        Be specific and provide actionable insights based on the numerical data.
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert audio engineer and vocal coach with deep knowledge of music production and voice analysis."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )
        
        return response.choices[0].message.content
    
    def analyze_emotion_and_mood(self, transcription: str, audio_features: Dict) -> str:
        """Analyze emotional content and mood"""
        
        prompt = f"""
        Analyze the emotional content and mood of this audio:
        
        Transcribed text: {transcription}
        
        Audio characteristics:
        - Pitch variation: {audio_features.get('fundamental_freq_std', 0):.2f} Hz
        - Energy level: {audio_features.get('rms_energy_mean', 0):.4f}
        - Dynamic range: {audio_features.get('dynamic_range', 0):.4f}
        - Tempo: {audio_features.get('tempo', 'unknown')} BPM
        
        Provide analysis for:
        1. **Emotional Tone**: Primary emotions detected
        2. **Mood Assessment**: Overall mood and atmosphere  
        3. **Energy Level**: High/medium/low energy classification
        4. **Sentiment**: Positive, negative, or neutral sentiment
        5. **Vocal Stress Indicators**: Signs of tension, relaxation, excitement
        6. **Musical Mood**: How the audio would fit in different contexts
        7. **Recommendations**: Suggestions for enhancing emotional impact
        
        Consider both lyrical content and vocal delivery patterns.
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a music psychologist and emotion recognition expert."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5
        )
        
        return response.choices[0].message.content
    
    def compare_vocal_performances(self, audio_files: List[str]) -> str:
        """Compare multiple vocal performances"""
        if len(audio_files) < 2:
            return "Need at least 2 audio files for comparison"
        
        comparisons = []
        
        for audio_file in audio_files[:5]:  # Limit to 5 files
            features = self.extract_audio_features(audio_file)
            transcription_data = self.transcribe_and_analyze(audio_file)
            
            comparison_data = {
                'file': Path(audio_file).name,
                'features': features,
                'transcription': transcription_data.get('transcription', ''),
                'duration': features.get('duration', 0),
                'pitch_mean': features.get('fundamental_freq_mean', 0),
                'pitch_range': features.get('pitch_range', 0),
                'energy': features.get('rms_energy_mean', 0),
                'tempo': features.get('tempo', 0)
            }
            comparisons.append(comparison_data)
        
        # Create comparison prompt
        comparison_summary = "Vocal Performance Comparison:\n\n"
        for i, comp in enumerate(comparisons, 1):
            comparison_summary += f"**Performance {i}: {comp['file']}**\n"
            comparison_summary += f"- Duration: {comp['duration']:.1f}s\n"
            comparison_summary += f"- Average pitch: {comp['pitch_mean']:.1f} Hz\n"
            comparison_summary += f"- Pitch range: {comp['pitch_range']:.1f} Hz\n"
            comparison_summary += f"- Energy level: {comp['energy']:.4f}\n"
            comparison_summary += f"- Tempo: {comp['tempo']:.1f} BPM\n"
            comparison_summary += f"- Content preview: {comp['transcription'][:100]}...\n\n"
        
        prompt = f"""
        Compare these vocal performances and provide detailed analysis:
        
        {comparison_summary}
        
        Analyze and compare:
        1. **Vocal Quality**: Tone, timbre, and technical execution
        2. **Emotional Expression**: Which performance is most emotionally compelling
        3. **Technical Metrics**: Pitch control, energy, consistency
        4. **Performance Style**: Different approaches and techniques used
        5. **Strengths and Weaknesses**: What each performance does well/poorly
        6. **Recommendations**: Which performance to develop further and why
        7. **Improvement Suggestions**: Specific advice for each performance
        
        Rank the performances and explain your reasoning.
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional vocal coach and music producer with expertise in performance evaluation."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )
        
        return response.choices[0].message.content
    
    def generate_vocal_coaching_advice(self, audio_path: str) -> str:
        """Generate personalized vocal coaching advice"""
        features = self.extract_audio_features(audio_path)
        transcription_data = self.transcribe_and_analyze(audio_path)
        
        prompt = f"""
        Provide professional vocal coaching advice based on this analysis:
        
        File: {features.get('file', 'unknown')}
        
        Technical Analysis:
        - Average pitch: {features.get('fundamental_freq_mean', 0):.1f} Hz
        - Pitch stability (std): {features.get('fundamental_freq_std', 0):.1f} Hz
        - Vocal range used: {features.get('pitch_range', 0):.1f} Hz
        - Energy consistency: {features.get('rms_energy_std', 0):.4f}
        - Dynamic control: {features.get('dynamic_range', 0):.4f}
        
        Content: {transcription_data.get('transcription', 'No transcription available')[:200]}...
        
        Provide specific coaching advice for:
        1. **Pitch Control**: Techniques to improve intonation and stability
        2. **Breath Support**: Exercises for better breathing and sustain
        3. **Tone Quality**: Methods to enhance vocal timbre
        4. **Dynamic Range**: Exercises for volume and expression control
        5. **Articulation**: Clarity and pronunciation improvements
        6. **Style Development**: Genre-specific technique recommendations
        7. **Practice Routine**: Specific exercises and daily practice suggestions
        8. **Technical Issues**: Address any detected problems
        
        Make recommendations specific to the detected vocal characteristics and skill level.
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional vocal coach with 20 years of experience teaching singers of all skill levels."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )
        
        return response.choices[0].message.content
    
    def create_audio_report(self, audio_path: str, output_dir: str = None) -> str:
        """Create comprehensive audio analysis report"""
        if output_dir is None:
            output_dir = Path.cwd() / "audio_reports"
        else:
            output_dir = Path(output_dir)
        
        output_dir.mkdir(exist_ok=True)
        
        # Extract all data
        features = self.extract_audio_features(audio_path)
        transcription_data = self.transcribe_and_analyze(audio_path)
        
        if 'error' in features:
            return f"Error analyzing audio: {features['error']}"
        
        # Generate AI analyses
        vocal_analysis = self.analyze_vocal_characteristics(
            features, transcription_data.get('transcription', '')
        )
        
        emotion_analysis = self.analyze_emotion_and_mood(
            transcription_data.get('transcription', ''), features
        )
        
        coaching_advice = self.generate_vocal_coaching_advice(audio_path)
        
        # Create comprehensive report
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = Path(audio_path).stem
        report_file = output_dir / f"{filename}_analysis_report_{timestamp}.md"
        
        report_content = f"""# Voice Analysis Report
        
**File:** {features['file']}  
**Generated:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}  
**Duration:** {features.get('duration', 0):.2f} seconds

---

## 🎵 Audio Transcription

**Language:** {transcription_data.get('language', 'Unknown')}

**Content:**
{transcription_data.get('transcription', 'No transcription available')}

---

## 📊 Technical Features

| Metric | Value |
|--------|-------|
| Sample Rate | {features.get('sample_rate', 'N/A')} Hz |
| Duration | {features.get('duration', 0):.2f} seconds |
| Average Pitch | {features.get('fundamental_freq_mean', 0):.1f} Hz |
| Pitch Range | {features.get('pitch_range', 0):.1f} Hz |
| Tempo | {features.get('tempo', 0):.1f} BPM |
| RMS Energy | {features.get('rms_energy_mean', 0):.4f} |
| Dynamic Range | {features.get('dynamic_range', 0):.4f} |
| Harmonic Ratio | {features.get('harmonic_ratio', 0):.2f} |

---

## 🎤 Vocal Characteristics Analysis

{vocal_analysis}

---

## 😊 Emotional & Mood Analysis

{emotion_analysis}

---

## 🎯 Vocal Coaching Recommendations

{coaching_advice}

---

## 📈 Raw Feature Data

```json
{json.dumps(features, indent=2)}
```

---

*Report generated by NoizyFish Voice Analysis Tool*
"""
        
        with open(report_file, 'w') as f:
            f.write(report_content)
        
        return str(report_file)

def main():
    parser = argparse.ArgumentParser(description="Voice Analysis Tool")
    parser.add_argument("--file", help="Audio file to analyze")
    parser.add_argument("--dir", help="Directory of audio files to batch analyze")
    parser.add_argument("--compare", nargs='+', help="Multiple files to compare")
    parser.add_argument("--output", help="Output directory for reports")
    parser.add_argument("--mode", choices=["full", "features", "transcribe", "vocal", "emotion", "coaching"], 
                       default="full", help="Analysis mode")
    
    args = parser.parse_args()
    
    analyzer = VoiceAnalyzer()
    
    try:
        if args.compare:
            # Compare multiple files
            comparison = analyzer.compare_vocal_performances(args.compare)
            print(f"\n{'='*60}")
            print("VOCAL PERFORMANCE COMPARISON")
            print(f"{'='*60}")
            print(comparison)
            
            # Save comparison report
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            with open(f"vocal_comparison_{timestamp}.md", 'w') as f:
                f.write(f"# Vocal Performance Comparison\n\n")
                f.write(f"**Generated:** {datetime.now()}\n\n")
                f.write(comparison)
        
        elif args.file:
            # Single file analysis
            if args.mode == "full":
                report_file = analyzer.create_audio_report(args.file, args.output)
                print(f"✅ Comprehensive report saved: {report_file}")
            
            elif args.mode == "features":
                features = analyzer.extract_audio_features(args.file)
                print(json.dumps(features, indent=2))
            
            elif args.mode == "transcribe":
                result = analyzer.transcribe_and_analyze(args.file)
                print(f"Transcription: {result.get('transcription', 'Error')}")
            
            elif args.mode == "vocal":
                features = analyzer.extract_audio_features(args.file)
                transcription = analyzer.transcribe_and_analyze(args.file)
                analysis = analyzer.analyze_vocal_characteristics(
                    features, transcription.get('transcription', '')
                )
                print(analysis)
            
            elif args.mode == "emotion":
                features = analyzer.extract_audio_features(args.file)
                transcription = analyzer.transcribe_and_analyze(args.file)
                analysis = analyzer.analyze_emotion_and_mood(
                    transcription.get('transcription', ''), features
                )
                print(analysis)
            
            elif args.mode == "coaching":
                advice = analyzer.generate_vocal_coaching_advice(args.file)
                print(advice)
        
        elif args.dir:
            # Batch processing
            audio_dir = Path(args.dir)
            if not audio_dir.exists():
                print(f"Directory not found: {args.dir}")
                return
            
            audio_files = []
            for ext in analyzer.supported_formats:
                audio_files.extend(audio_dir.glob(f"*{ext}"))
            
            print(f"Found {len(audio_files)} audio files")
            
            for audio_file in audio_files:
                try:
                    print(f"Analyzing: {audio_file.name}")
                    report_file = analyzer.create_audio_report(str(audio_file), args.output)
                    print(f"✅ Report saved: {report_file}")
                except Exception as e:
                    print(f"❌ Error analyzing {audio_file.name}: {e}")
        
        else:
            print("Please specify --file, --dir, or --compare")
            parser.print_help()
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()