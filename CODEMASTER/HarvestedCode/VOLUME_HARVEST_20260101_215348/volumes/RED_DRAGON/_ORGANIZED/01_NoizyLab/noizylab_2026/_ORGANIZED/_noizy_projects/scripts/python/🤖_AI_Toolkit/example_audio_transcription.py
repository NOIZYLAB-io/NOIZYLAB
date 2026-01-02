# 🎵 Example: Transcribe and Analyze Audio

import sys
import os
sys.path.append('/Users/rsp_ms/NoizyFish_Aquarium/🤖 AI_Toolkit/02_Audio_Transcription')
from audio_transcriber import AudioTranscriber

def example_transcribe_music():
    """Example: Transcribe a music file from your archive"""
    
    # Initialize transcriber
    transcriber = AudioTranscriber()
    
    # Example with a file from your music archive
    audio_file = "/Users/rsp_ms/NoizyFish_Aquarium/🎵 Original_Music_Archive/00_The_FLAP_4.wav"
    
    try:
        print("🎵 Transcribing audio file...")
        result = transcriber.transcribe_audio(audio_file)
        
        print(f"\n{'='*60}")
        print("TRANSCRIPTION RESULT")
        print(f"{'='*60}")
        print(f"File: {result['file']}")
        print(f"Language: {result['language']}")
        print(f"Duration: {result['duration']} seconds")
        print(f"\nTranscription:\n{result['text']}")
        
        # Analyze lyrics if text found
        if result['text'].strip():
            print(f"\n{'='*60}")
            print("LYRICAL ANALYSIS")
            print(f"{'='*60}")
            
            analysis = transcriber.analyze_lyrics(result['text'])
            print(analysis)
            
            print(f"\n{'='*60}")
            print("IMPROVEMENT SUGGESTIONS")
            print(f"{'='*60}")
            
            suggestions = transcriber.suggest_improvements(result['text'])
            print(suggestions)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    example_transcribe_music()