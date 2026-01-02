#!/usr/bin/env python3
"""
Audio Transcription Tool - NoizyFish Music Archive Edition
Transcribe audio files using OpenAI Whisper API
Perfect for transcribing vocals, lyrics, and audio notes
"""

import os
import openai
from pathlib import Path
import argparse
from datetime import datetime
import json
from typing import List, Dict, Optional
import mimetypes

class AudioTranscriber:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the Audio Transcriber"""
        self.client = openai.OpenAI(
            api_key=api_key or os.getenv('OPENAI_API_KEY')
        )
        self.supported_formats = {
            '.mp3', '.mp4', '.mpeg', '.mpga', '.m4a', '.wav', '.webm'
        }
        
    def transcribe_audio(self, audio_path: str, language: Optional[str] = None, 
                        prompt: Optional[str] = None) -> Dict:
        """Transcribe audio file to text"""
        audio_file = Path(audio_path)
        
        if not audio_file.exists():
            raise FileNotFoundError(f"Audio file not found: {audio_path}")
        
        if audio_file.suffix.lower() not in self.supported_formats:
            raise ValueError(f"Unsupported format. Supported: {self.supported_formats}")
        
        print(f"Transcribing: {audio_file.name}")
        
        with open(audio_path, 'rb') as audio:
            response = self.client.audio.transcriptions.create(
                model="whisper-1",
                file=audio,
                language=language,
                prompt=prompt,
                response_format="verbose_json"
            )
        
        return {
            'file': audio_file.name,
            'text': response.text,
            'language': response.language,
            'duration': response.duration,
            'segments': response.segments if hasattr(response, 'segments') else None
        }
    
    def translate_audio(self, audio_path: str, prompt: Optional[str] = None) -> Dict:
        """Translate audio to English"""
        audio_file = Path(audio_path)
        
        if not audio_file.exists():
            raise FileNotFoundError(f"Audio file not found: {audio_path}")
        
        print(f"Translating: {audio_file.name}")
        
        with open(audio_path, 'rb') as audio:
            response = self.client.audio.translations.create(
                model="whisper-1",
                file=audio,
                prompt=prompt,
                response_format="verbose_json"
            )
        
        return {
            'file': audio_file.name,
            'text': response.text,
            'duration': response.duration,
            'original_language': 'auto-detected',
            'target_language': 'English'
        }
    
    def batch_transcribe(self, audio_dir: str, output_dir: str = None, 
                        language: Optional[str] = None) -> List[Dict]:
        """Transcribe all audio files in a directory"""
        audio_path = Path(audio_dir)
        
        if not audio_path.exists():
            raise FileNotFoundError(f"Directory not found: {audio_dir}")
        
        if output_dir:
            output_path = Path(output_dir)
            output_path.mkdir(exist_ok=True)
        else:
            output_path = audio_path / "transcriptions"
            output_path.mkdir(exist_ok=True)
        
        audio_files = []
        for ext in self.supported_formats:
            audio_files.extend(audio_path.glob(f"*{ext}"))
        
        results = []
        
        for audio_file in audio_files:
            try:
                result = self.transcribe_audio(str(audio_file), language)
                results.append(result)
                
                # Save individual transcription
                output_file = output_path / f"{audio_file.stem}_transcription.json"
                with open(output_file, 'w') as f:
                    json.dump(result, f, indent=2)
                
                # Save text file
                text_file = output_path / f"{audio_file.stem}_transcription.txt"
                with open(text_file, 'w') as f:
                    f.write(f"File: {result['file']}\n")
                    f.write(f"Language: {result['language']}\n")
                    f.write(f"Duration: {result['duration']} seconds\n")
                    f.write(f"Transcription:\n\n{result['text']}")
                
                print(f"✅ Completed: {audio_file.name}")
                
            except Exception as e:
                print(f"❌ Error processing {audio_file.name}: {e}")
                results.append({
                    'file': audio_file.name,
                    'error': str(e)
                })
        
        # Save batch summary
        summary_file = output_path / f"batch_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(summary_file, 'w') as f:
            json.dump({
                'timestamp': datetime.now().isoformat(),
                'total_files': len(audio_files),
                'successful': len([r for r in results if 'error' not in r]),
                'failed': len([r for r in results if 'error' in r]),
                'results': results
            }, f, indent=2)
        
        return results
    
    def analyze_lyrics(self, transcription: str) -> str:
        """Analyze transcribed lyrics using GPT"""
        prompt = f"""
        Analyze these lyrics and provide:
        1. Theme and mood analysis
        2. Lyrical structure (verses, chorus, bridge)
        3. Rhyme scheme and patterns
        4. Emotional tone
        5. Key phrases and metaphors
        6. Genre suggestions
        
        Lyrics:
        {transcription}
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a music industry expert and lyrical analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )
        
        return response.choices[0].message.content
    
    def suggest_improvements(self, transcription: str) -> str:
        """Suggest improvements to lyrics"""
        prompt = f"""
        Review these lyrics and suggest improvements for:
        1. Flow and rhythm
        2. Rhyme consistency
        3. Emotional impact
        4. Clarity and meaning
        5. Word choice and imagery
        6. Overall structure
        
        Provide specific suggestions and alternative lines where appropriate.
        
        Lyrics:
        {transcription}
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a professional songwriter and lyricist."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5
        )
        
        return response.choices[0].message.content

def main():
    parser = argparse.ArgumentParser(description="Audio Transcription Tool")
    parser.add_argument("--file", help="Audio file to transcribe")
    parser.add_argument("--dir", help="Directory of audio files to batch process")
    parser.add_argument("--output", help="Output directory for results")
    parser.add_argument("--language", help="Source language (optional)")
    parser.add_argument("--translate", action="store_true", help="Translate to English")
    parser.add_argument("--analyze", action="store_true", help="Analyze lyrics with AI")
    parser.add_argument("--improve", action="store_true", help="Suggest lyric improvements")
    parser.add_argument("--prompt", help="Custom prompt for better transcription")
    
    args = parser.parse_args()
    
    transcriber = AudioTranscriber()
    
    try:
        if args.file:
            # Single file processing
            if args.translate:
                result = transcriber.translate_audio(args.file, args.prompt)
            else:
                result = transcriber.transcribe_audio(args.file, args.language, args.prompt)
            
            print(f"\n{'='*60}")
            print(f"TRANSCRIPTION RESULT")
            print(f"{'='*60}")
            print(f"File: {result['file']}")
            if 'language' in result:
                print(f"Language: {result['language']}")
            if 'duration' in result:
                print(f"Duration: {result['duration']} seconds")
            print(f"\nText:\n{result['text']}")
            
            # Save result
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"transcription_{timestamp}.json"
            with open(output_file, 'w') as f:
                json.dump(result, f, indent=2)
            print(f"\nSaved to: {output_file}")
            
            # AI Analysis
            if args.analyze:
                print(f"\n{'='*60}")
                print("LYRICAL ANALYSIS")
                print(f"{'='*60}")
                analysis = transcriber.analyze_lyrics(result['text'])
                print(analysis)
                
                with open(f"analysis_{timestamp}.md", 'w') as f:
                    f.write(f"# Lyrical Analysis\n\n")
                    f.write(f"**File:** {result['file']}\n\n")
                    f.write(analysis)
            
            # Improvement Suggestions
            if args.improve:
                print(f"\n{'='*60}")
                print("IMPROVEMENT SUGGESTIONS")
                print(f"{'='*60}")
                suggestions = transcriber.suggest_improvements(result['text'])
                print(suggestions)
                
                with open(f"suggestions_{timestamp}.md", 'w') as f:
                    f.write(f"# Lyric Improvement Suggestions\n\n")
                    f.write(f"**File:** {result['file']}\n\n")
                    f.write(suggestions)
        
        elif args.dir:
            # Batch processing
            results = transcriber.batch_transcribe(args.dir, args.output, args.language)
            
            print(f"\n{'='*60}")
            print("BATCH TRANSCRIPTION COMPLETE")
            print(f"{'='*60}")
            successful = len([r for r in results if 'error' not in r])
            failed = len([r for r in results if 'error' in r])
            print(f"Successful: {successful}")
            print(f"Failed: {failed}")
            print(f"Total: {len(results)}")
        
        else:
            print("Please specify either --file or --dir")
            parser.print_help()
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()