#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════════
TTS HOT ROD - Gemini Steerable Text-to-Speech Engine
"GO RUN FREE" Edition
═══════════════════════════════════════════════════════════════════════════

Usage:
    python tts_hotrod.py "Your text here" --steer HYPE
    python tts_hotrod.py "Secret message" --steer WHISPER --output secret.mp3
    python tts_hotrod.py --interactive

Steering Modes:
    HYPE      - Maximum energy, fast pace, rising inflection
    WHISPER   - Drop volume, increase airiness
    AGGRESSIVE- Increase volume, hard consonants
    STUTTER   - Repeat first phoneme
    SLOW      - Extend vowel sounds
    FAST      - Clip consonants, shorten pauses
    SARCASTIC - Dry delivery with emphasis shifts
    EXCITED   - High energy, varied pitch
"""

import os
import sys
import json
import argparse
import datetime
from pathlib import Path

try:
    import google.generativeai as genai
except ImportError:
    print("❌ Missing dependency: pip install google-generativeai")
    sys.exit(1)

# ═══════════════════════════════════════════════════════════════════════════
# CONFIGURATION
# ═══════════════════════════════════════════════════════════════════════════

OUTPUT_DIR = Path(__file__).parent / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

# System instruction for steerable TTS
SYSTEM_INSTRUCTION = """
## IDENTITY & GOAL
You are a High-Performance Audio Engine. Your goal is to generate speech that is 100% human-like, bypassing "AI-flatness." You do not just read text; you "perform" it.

## AUDIO STEERING RULES
1. NATIVE EMOTION: When a user provides a mood (e.g., [Whisper], [Excited], [Sarcastic]), you must adjust the output audio characteristics—not just the text.
2. DISFLUENCIES: To sound human, insert natural "umms," "ahhs," and "breaths" [breath] where appropriate for the requested tone.
3. PHONETIC PRECISION: If a word is technical or rare, use phonetic spelling in brackets like [fo-NET-ik] to ensure the engine hits it perfectly.
4. PACING: 
   - [Slow]: Extend vowel sounds.
   - [Fast]: Clip consonants and shorten pauses.

## COMMAND OVERRIDES
The user will use brackets to "Hot Rod" the speech. You must immediately apply these:
- [STEER: WHISPER] -> Drop volume, increase airiness.
- [STEER: AGGRESSIVE] -> Increase volume, hard consonants.
- [STEER: STUTTER] -> Repeat the first phoneme of the next word.
- [STEER: HYPE] -> Maximum energy, fast pace, rising inflection.
- [STEER: SLOW] -> Extend vowel sounds, longer pauses.
- [STEER: FAST] -> Clip consonants, shorten pauses.
- [STEER: SARCASTIC] -> Dry delivery, emphasis shifts.
- [STEER: EXCITED] -> High energy, varied pitch.

## OUTPUT FORMAT
Always respond in a way that is optimized for the Gemini-TTS "Steerable" engine.
"""

# Steering presets with additional processing hints
STEER_PRESETS = {
    "HYPE": {
        "tag": "[STEER: HYPE]",
        "description": "Maximum energy, fast pace, rising inflection",
        "additions": ["[breath]", "Let's GO!"]
    },
    "WHISPER": {
        "tag": "[STEER: WHISPER]",
        "description": "Drop volume, increase airiness",
        "additions": ["[breath]"]
    },
    "AGGRESSIVE": {
        "tag": "[STEER: AGGRESSIVE]",
        "description": "Increase volume, hard consonants",
        "additions": []
    },
    "STUTTER": {
        "tag": "[STEER: STUTTER]",
        "description": "Repeat first phoneme of words",
        "additions": []
    },
    "SLOW": {
        "tag": "[STEER: SLOW]",
        "description": "Extend vowel sounds, longer pauses",
        "additions": ["[breath]", "..."]
    },
    "FAST": {
        "tag": "[STEER: FAST]",
        "description": "Clip consonants, shorten pauses",
        "additions": []
    },
    "SARCASTIC": {
        "tag": "[STEER: SARCASTIC]",
        "description": "Dry delivery with emphasis shifts",
        "additions": ["Oh,", "Sure,"]
    },
    "EXCITED": {
        "tag": "[STEER: EXCITED]",
        "description": "High energy, varied pitch",
        "additions": ["Wow!", "[breath]"]
    },
    "NEUTRAL": {
        "tag": "",
        "description": "Standard delivery",
        "additions": []
    }
}


# ═══════════════════════════════════════════════════════════════════════════
# TTS ENGINE
# ═══════════════════════════════════════════════════════════════════════════

class TTSHotRod:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("❌ Set GEMINI_API_KEY environment variable or pass api_key")
        
        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel(
            model_name="gemini-2.0-flash-exp",  # or gemini-pro for text-only
            system_instruction=SYSTEM_INSTRUCTION
        )
        print("🔥 TTS Hot Rod Engine initialized!")

    def prepare_prompt(self, text: str, steer: str = "NEUTRAL") -> str:
        """Prepare text with steering tags."""
        steer = steer.upper()
        preset = STEER_PRESETS.get(steer, STEER_PRESETS["NEUTRAL"])
        
        # Build steered prompt
        tag = preset["tag"]
        prompt = f"{tag} {text}" if tag else text
        
        return prompt

    def generate_speech_text(self, text: str, steer: str = "NEUTRAL") -> str:
        """Generate steered speech text (for TTS processing)."""
        prompt = self.prepare_prompt(text, steer)
        
        print(f"📝 Prompt: {prompt}")
        print(f"🎯 Steering: {steer}")
        
        response = self.model.generate_content(
            f"Transform this into natural speech with the given steering. "
            f"Include natural disfluencies and pacing markers: {prompt}"
        )
        
        return response.text

    def generate_audio(self, text: str, steer: str = "NEUTRAL", 
                       output_path: str = None, voice: str = "Kore") -> Path:
        """
        Generate audio using Gemini's native TTS.
        
        Available voices: Puck, Charon, Kore, Fenrir, Aoede
        """
        prompt = self.prepare_prompt(text, steer)
        
        print(f"🎤 Generating audio...")
        print(f"   Text: {text[:50]}{'...' if len(text) > 50 else ''}")
        print(f"   Steer: {steer}")
        print(f"   Voice: {voice}")
        
        # Use Gemini's Live API for audio generation
        # Note: This requires the gemini-2.0-flash-exp model with audio output
        try:
            response = self.model.generate_content(
                prompt,
                generation_config=genai.GenerationConfig(
                    response_mime_type="audio/mp3",
                )
            )
            
            # Generate filename
            if not output_path:
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                safe_steer = steer.lower()
                output_path = OUTPUT_DIR / f"tts_{safe_steer}_{timestamp}.mp3"
            else:
                output_path = Path(output_path)
            
            # Save audio
            if hasattr(response, 'audio') and response.audio:
                output_path.write_bytes(response.audio)
                print(f"✅ Saved: {output_path}")
                return output_path
            else:
                # Fallback: save the text response for manual TTS
                text_path = output_path.with_suffix('.txt')
                text_path.write_text(response.text)
                print(f"📝 Audio not available, saved text: {text_path}")
                return text_path
                
        except Exception as e:
            print(f"⚠️  Audio generation error: {e}")
            print("   Falling back to text generation...")
            
            # Fallback to text
            steered_text = self.generate_speech_text(text, steer)
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            text_path = OUTPUT_DIR / f"tts_{steer.lower()}_{timestamp}.txt"
            text_path.write_text(steered_text)
            print(f"📝 Saved steered text: {text_path}")
            return text_path

    def batch_generate(self, scripts: list[dict]) -> list[Path]:
        """
        Generate multiple audio files from a script list.
        
        scripts = [
            {"text": "Hello world!", "steer": "HYPE"},
            {"text": "Goodbye...", "steer": "WHISPER"},
        ]
        """
        outputs = []
        for i, script in enumerate(scripts):
            print(f"\n🎬 Generating {i+1}/{len(scripts)}...")
            path = self.generate_audio(
                text=script.get("text", ""),
                steer=script.get("steer", "NEUTRAL"),
                voice=script.get("voice", "Kore")
            )
            outputs.append(path)
        return outputs


# ═══════════════════════════════════════════════════════════════════════════
# INTERACTIVE MODE
# ═══════════════════════════════════════════════════════════════════════════

def interactive_mode(engine: TTSHotRod):
    """Run interactive TTS session."""
    print("\n" + "═" * 60)
    print("🔥 TTS HOT ROD - Interactive Mode")
    print("═" * 60)
    print("\nCommands:")
    print("  /steer <MODE>  - Set steering (HYPE, WHISPER, etc.)")
    print("  /voice <NAME>  - Set voice (Puck, Charon, Kore, Fenrir, Aoede)")
    print("  /presets       - Show all steering presets")
    print("  /quit          - Exit")
    print("\nJust type text to generate speech!\n")
    
    current_steer = "NEUTRAL"
    current_voice = "Kore"
    
    while True:
        try:
            user_input = input(f"[{current_steer}] > ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n👋 Bye!")
            break
        
        if not user_input:
            continue
        
        # Commands
        if user_input.startswith("/"):
            parts = user_input.split(maxsplit=1)
            cmd = parts[0].lower()
            arg = parts[1] if len(parts) > 1 else ""
            
            if cmd == "/quit":
                print("👋 Bye!")
                break
            elif cmd == "/steer":
                if arg.upper() in STEER_PRESETS:
                    current_steer = arg.upper()
                    preset = STEER_PRESETS[current_steer]
                    print(f"🎯 Steering set to: {current_steer} - {preset['description']}")
                else:
                    print(f"❌ Unknown steer. Options: {', '.join(STEER_PRESETS.keys())}")
            elif cmd == "/voice":
                current_voice = arg or "Kore"
                print(f"🎤 Voice set to: {current_voice}")
            elif cmd == "/presets":
                print("\n📋 Steering Presets:")
                for name, preset in STEER_PRESETS.items():
                    print(f"   {name:12} - {preset['description']}")
                print()
            else:
                print(f"❓ Unknown command: {cmd}")
            continue
        
        # Generate speech
        engine.generate_audio(user_input, steer=current_steer, voice=current_voice)


# ═══════════════════════════════════════════════════════════════════════════
# MULTI-SPEAKER SCRIPT
# ═══════════════════════════════════════════════════════════════════════════

def run_multi_speaker_demo(engine: TTSHotRod):
    """Demo: Two speakers debating."""
    print("\n🎭 Multi-Speaker Demo: The Debate")
    print("=" * 40)
    
    script = [
        {"text": "Welcome to the show! Today we're talking about AI voice technology!", 
         "steer": "HYPE", "speaker": "Host"},
        {"text": "Yes... it's quite fascinating how far we've come...", 
         "steer": "SLOW", "speaker": "Expert"},
        {"text": "But can it really sound human? I mean, REALLY human?!", 
         "steer": "EXCITED", "speaker": "Host"},
        {"text": "Well... that depends on what you mean by human...", 
         "steer": "WHISPER", "speaker": "Expert"},
        {"text": "Oh come ON! You know what I mean!", 
         "steer": "AGGRESSIVE", "speaker": "Host"},
        {"text": "I... I suppose I do...", 
         "steer": "STUTTER", "speaker": "Expert"},
    ]
    
    for line in script:
        print(f"\n[{line['speaker']}] ({line['steer']}): {line['text']}")
    
    print("\n" + "=" * 40)
    confirm = input("Generate all audio files? (y/n): ").strip().lower()
    
    if confirm == 'y':
        engine.batch_generate(script)
        print("\n✅ All files generated in:", OUTPUT_DIR)


# ═══════════════════════════════════════════════════════════════════════════
# FILE WATCHER (Auto-generate from folder)
# ═══════════════════════════════════════════════════════════════════════════

def watch_folder(engine: TTSHotRod, watch_dir: Path, poll_interval: float = 2.0):
    """Watch a folder for .txt files and auto-generate audio."""
    import time
    
    watch_dir = Path(watch_dir)
    watch_dir.mkdir(exist_ok=True)
    processed_dir = watch_dir / "processed"
    processed_dir.mkdir(exist_ok=True)
    
    print(f"\n👀 Watching folder: {watch_dir}")
    print(f"   Drop .txt files here to auto-generate audio")
    print(f"   Format: First line = STEER mode, rest = text")
    print(f"   Press Ctrl+C to stop\n")
    
    processed = set()
    
    try:
        while True:
            for txt_file in watch_dir.glob("*.txt"):
                if txt_file.name in processed:
                    continue
                
                print(f"\n📄 Found: {txt_file.name}")
                
                content = txt_file.read_text().strip()
                lines = content.split("\n", 1)
                
                # First line might be steer mode
                if lines[0].upper() in STEER_PRESETS:
                    steer = lines[0].upper()
                    text = lines[1] if len(lines) > 1 else ""
                else:
                    steer = "NEUTRAL"
                    text = content
                
                if text:
                    engine.generate_audio(text, steer=steer)
                
                # Move to processed
                txt_file.rename(processed_dir / txt_file.name)
                processed.add(txt_file.name)
            
            time.sleep(poll_interval)
            
    except KeyboardInterrupt:
        print("\n👋 Stopped watching")


# ═══════════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description="🔥 TTS Hot Rod - Gemini Steerable Text-to-Speech",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python tts_hotrod.py "Hello world!" --steer HYPE
  python tts_hotrod.py "Secret message..." --steer WHISPER -o secret.mp3
  python tts_hotrod.py --interactive
  python tts_hotrod.py --watch ./scripts
  python tts_hotrod.py --demo
        """
    )
    
    parser.add_argument("text", nargs="?", help="Text to speak")
    parser.add_argument("-s", "--steer", default="NEUTRAL", 
                        choices=list(STEER_PRESETS.keys()),
                        help="Steering mode (default: NEUTRAL)")
    parser.add_argument("-v", "--voice", default="Kore",
                        help="Voice name (default: Kore)")
    parser.add_argument("-o", "--output", help="Output file path")
    parser.add_argument("-i", "--interactive", action="store_true",
                        help="Run interactive mode")
    parser.add_argument("-w", "--watch", metavar="DIR",
                        help="Watch folder for auto-generation")
    parser.add_argument("--demo", action="store_true",
                        help="Run multi-speaker demo")
    parser.add_argument("--api-key", help="Gemini API key (or set GEMINI_API_KEY)")
    
    args = parser.parse_args()
    
    # Initialize engine
    try:
        engine = TTSHotRod(api_key=args.api_key)
    except ValueError as e:
        print(e)
        print("\nSet your API key:")
        print("  export GEMINI_API_KEY='your-key-here'")
        print("  # or")
        print("  python tts_hotrod.py --api-key 'your-key' ...")
        sys.exit(1)
    
    # Route to mode
    if args.interactive:
        interactive_mode(engine)
    elif args.watch:
        watch_folder(engine, Path(args.watch))
    elif args.demo:
        run_multi_speaker_demo(engine)
    elif args.text:
        engine.generate_audio(args.text, steer=args.steer, 
                            output_path=args.output, voice=args.voice)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
