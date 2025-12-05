#!/usr/bin/env python3
"""
🎵 AI MUSIC GENERATOR - FISH MUSIC INC
Generate music using FREE AI models - MusicGen, Riffusion, AudioCraft
"""

import requests
import json
import time
import os
from pathlib import Path

class AIMusicGenerator:
    """Generate music using AI - multiple free providers"""
    
    def __init__(self):
        self.replicate_token = os.getenv('REPLICATE_API_TOKEN')
        self.huggingface_token = os.getenv('HUGGINGFACE_API_TOKEN')
        
    # REPLICATE API - PAY PER USE (CENTS!)
    
    def generate_with_musicgen(self, prompt, duration=8, model_version="stereo-large"):
        """
        Generate music with Meta's MusicGen
        
        Examples:
        - "80s pop with heavy drums and bass"
        - "90s rock with electric guitar"
        - "lo-fi slow BPM electro chill with organic samples"
        """
        if not self.replicate_token:
            print("⚠️  Set REPLICATE_API_TOKEN environment variable")
            return None
        
        print(f"🎵 Generating music with MusicGen...")
        print(f"   Prompt: {prompt}")
        print(f"   Duration: {duration}s")
        
        url = "https://api.replicate.com/v1/predictions"
        
        headers = {
            "Authorization": f"Token {self.replicate_token}",
            "Content-Type": "application/json"
        }
        
        data = {
            "version": "stereo-melody-large" if model_version == "stereo-large" else "melody",
            "input": {
                "prompt": prompt,
                "duration": duration,
                "model_version": model_version,
                "output_format": "wav",
                "normalization_strategy": "loudness"
            }
        }
        
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 201:
            prediction_url = response.json()['urls']['get']
            
            # Poll for completion
            while True:
                result = requests.get(prediction_url, headers=headers)
                status = result.json()['status']
                
                if status == 'succeeded':
                    output_url = result.json()['output']
                    print(f"✅ Music generated!")
                    print(f"   Download: {output_url}")
                    return output_url
                
                elif status == 'failed':
                    print(f"❌ Generation failed: {result.json().get('error')}")
                    return None
                
                print(f"   ⏳ Status: {status}...")
                time.sleep(2)
        
        else:
            print(f"❌ API error: {response.text}")
            return None
    
    def generate_with_riffusion(self, prompt_start, prompt_end=None, duration=5):
        """
        Generate music with Riffusion (spectrogram-based)
        
        Good for: beats, loops, electronic music
        """
        if not self.replicate_token:
            print("⚠️  Set REPLICATE_API_TOKEN environment variable")
            return None
        
        print(f"🎵 Generating with Riffusion...")
        print(f"   Start: {prompt_start}")
        if prompt_end:
            print(f"   End: {prompt_end}")
        
        url = "https://api.replicate.com/v1/predictions"
        
        headers = {
            "Authorization": f"Token {self.replicate_token}",
            "Content-Type": "application/json"
        }
        
        data = {
            "version": "riffusion/riffusion:8cf61ea6c56afd61d8f5b9ffd14d7c216c0a93844ce2d82ac1c9ecc9c7f24e05",
            "input": {
                "prompt_a": prompt_start,
                "prompt_b": prompt_end or prompt_start,
                "denoising": 0.75,
                "duration": duration
            }
        }
        
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 201:
            prediction_url = response.json()['urls']['get']
            
            # Poll for completion
            while True:
                result = requests.get(prediction_url, headers=headers)
                status = result.json()['status']
                
                if status == 'succeeded':
                    output_url = result.json()['output']['audio']
                    print(f"✅ Music generated!")
                    return output_url
                elif status == 'failed':
                    print(f"❌ Failed: {result.json().get('error')}")
                    return None
                
                time.sleep(2)
        
        return None
    
    # HUGGING FACE - 100% FREE!
    
    def generate_with_musicgen_hf(self, prompt, duration=10):
        """
        Generate music using Hugging Face (FREE!)
        
        Uses Facebook's MusicGen model hosted on HF
        """
        if not self.huggingface_token:
            print("⚠️  Set HUGGINGFACE_API_TOKEN environment variable")
            print("   Get it FREE at: https://huggingface.co/settings/tokens")
            return None
        
        print(f"🎵 Generating with Hugging Face MusicGen (FREE!)...")
        
        api_url = "https://api-inference.huggingface.co/models/facebook/musicgen-small"
        
        headers = {
            "Authorization": f"Bearer {self.huggingface_token}"
        }
        
        payload = {
            "inputs": prompt,
            "parameters": {"max_new_tokens": duration * 50}
        }
        
        response = requests.post(api_url, headers=headers, json=payload)
        
        if response.status_code == 200:
            # Save audio
            output_file = f"generated_{int(time.time())}.wav"
            with open(output_file, 'wb') as f:
                f.write(response.content)
            
            print(f"✅ Music generated!")
            print(f"   Saved to: {output_file}")
            return output_file
        
        else:
            print(f"❌ Generation failed: {response.text}")
            return None
    
    # STEM SEPARATION (FREE!)
    
    def separate_stems(self, audio_file):
        """
        Separate audio into stems using Spleeter
        
        Returns: vocals, drums, bass, other
        """
        print(f"🎸 Separating stems from: {audio_file}")
        print(f"   Using Spleeter (FREE!)")
        
        # Install spleeter if needed
        try:
            from spleeter.separator import Separator
        except ImportError:
            print("Installing Spleeter...")
            os.system("pip install spleeter --quiet")
            from spleeter.separator import Separator
        
        separator = Separator('spleeter:4stems')
        separator.separate_to_file(audio_file, '.')
        
        print("✅ Stems separated!")
        return True
    
    # TEXT TO SPEECH (FREE!)
    
    def text_to_speech(self, text, voice_preset="announcer"):
        """
        Generate voiceover using Bark (FREE!)
        
        Perfect for: video narration, announcements
        """
        print(f"🗣️  Generating speech: '{text[:50]}...'")
        
        if not self.huggingface_token:
            print("⚠️  Set HUGGINGFACE_API_TOKEN for best results")
            return None
        
        api_url = "https://api-inference.huggingface.co/models/suno/bark"
        
        headers = {
            "Authorization": f"Bearer {self.huggingface_token}"
        }
        
        response = requests.post(api_url, headers=headers, json={"inputs": text})
        
        if response.status_code == 200:
            output_file = f"speech_{int(time.time())}.wav"
            with open(output_file, 'wb') as f:
                f.write(response.content)
            
            print(f"✅ Speech generated: {output_file}")
            return output_file
        
        return None

# CLI INTERFACE
if __name__ == "__main__":
    import sys
    
    print("🎵 AI MUSIC GENERATOR - FISH MUSIC INC")
    print("=" * 60)
    print()
    
    gen = AIMusicGenerator()
    
    if len(sys.argv) < 2:
        print("""
USAGE:
  Generate music with MusicGen (Replicate - paid but cheap):
    python3 AI_MUSIC_GENERATOR.py musicgen "80s pop with heavy drums"
  
  Generate music with Hugging Face (FREE!):
    python3 AI_MUSIC_GENERATOR.py musicgen-free "chill lo-fi beats"
  
  Generate with Riffusion:
    python3 AI_MUSIC_GENERATOR.py riffusion "trap beat with 808s"
  
  Separate stems from audio:
    python3 AI_MUSIC_GENERATOR.py stems <audio_file.wav>
  
  Text to speech:
    python3 AI_MUSIC_GENERATOR.py speak "Welcome to Fish Music Inc"

SETUP:
  Replicate (pay per use, ~$0.01-0.10 per generation):
    export REPLICATE_API_TOKEN="your_token"
  
  Hugging Face (100% FREE!):
    export HUGGINGFACE_API_TOKEN="your_token"
    Get FREE token at: https://huggingface.co/settings/tokens

FEATURES:
  ✅ Generate music from text descriptions
  ✅ Separate vocals/drums/bass/other
  ✅ Text to speech for voiceovers
  ✅ Multiple AI models available
  ✅ FREE and paid options
        """)
        sys.exit(0)
    
    command = sys.argv[1]
    
    if command == "musicgen":
        prompt = " ".join(sys.argv[2:])
        gen.generate_with_musicgen(prompt)
    
    elif command == "musicgen-free":
        prompt = " ".join(sys.argv[2:])
        gen.generate_with_musicgen_hf(prompt)
    
    elif command == "riffusion":
        prompt = " ".join(sys.argv[2:])
        gen.generate_with_riffusion(prompt)
    
    elif command == "stems":
        audio_file = sys.argv[2]
        gen.separate_stems(audio_file)
    
    elif command == "speak":
        text = " ".join(sys.argv[2:])
        gen.text_to_speech(text)
    
    else:
        print(f"❌ Unknown command: {command}")

