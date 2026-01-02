#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🏝️ MUSIC ISLAND - Interactive Learning Voice Generator 🏝️        ║
║                                                                           ║
║  Generate custom voices for interactive children's music education       ║
║  Part of VOX - Voice Control Application                                 ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import sys
from pathlib import Path
from typing import Dict, List

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent.parent))


class MusicIslandVoiceGenerator:
    """Generate voices for MUSIC ISLAND interactive learning."""

    def __init__(self):
        self.base_path = Path("/Users/rsp_ms/MC96_MobileApp")
        self.tts_env = self.base_path / "LUCY" / "tts_env" / "bin" / "python"
        self.output_dir = self.base_path / "VOX" / "characters" / "MUSIC_ISLAND"

        # Music education characters
        self.characters = {
            "maestro_melody": {
                "name": "Maestro Melody",
                "description": "Wise music teacher, encouraging voice",
                "speaker": "male-en-2",
                "icon": "🎼",
                "color": "#8B4513",
                "phrases": [
                    "Welcome to Music Island, where every sound is an adventure!",
                    "Let's learn about rhythm together! Can you clap along with me?",
                    "Music is the universal language - everyone can speak it!",
                    "Wonderful! You're becoming a true musician!",
                    "Remember: Practice makes progress, not perfect!",
                ]
            },
            "rhythm_ray": {
                "name": "Rhythm Ray",
                "description": "Energetic percussion teacher, upbeat voice",
                "speaker": "male-en-2",
                "icon": "🥁",
                "color": "#FF4500",
                "phrases": [
                    "Hey hey! Let's get that rhythm going! Boom-chick-boom-chick!",
                    "Drums are the heartbeat of music! Feel it in your chest!",
                    "Can you stomp your feet? Clap your hands? That's rhythm!",
                    "Fast or slow, loud or soft - rhythm controls the flow!",
                    "You've got the beat! Keep practicing!",
                ]
            },
            "harmony_hana": {
                "name": "Harmony Hana",
                "description": "Gentle piano teacher, sweet melodic voice",
                "speaker": "female-en-5",
                "icon": "🎹",
                "color": "#DDA0DD",
                "phrases": [
                    "Hello dear students! Let's explore the beautiful world of harmony!",
                    "When notes play together, they create something magical called harmony.",
                    "Can you hear how these notes fit together like puzzle pieces?",
                    "Piano keys are like friends - each one has their special place!",
                    "Beautiful playing! You're making such lovely music!",
                ]
            },
            "tempo_tim": {
                "name": "Tempo Tim",
                "description": "Speed-focused teacher, dynamic voice",
                "speaker": "male-en-2",
                "icon": "⏱️",
                "color": "#4169E1",
                "phrases": [
                    "Hey there, speedsters! Ready to learn about tempo?",
                    "Tempo means how fast or slow we play. Let's experiment!",
                    "Slow like a turtle... or fast like a cheetah! You control the speed!",
                    "Different speeds create different feelings in music!",
                    "Excellent tempo control! You're really getting it!",
                ]
            },
            "note_nancy": {
                "name": "Note Nancy",
                "description": "Note-reading specialist, clear teaching voice",
                "speaker": "female-en-5",
                "icon": "🎵",
                "color": "#32CD32",
                "phrases": [
                    "Hi musicians! I'm Note Nancy, and I love teaching about musical notes!",
                    "Notes are like letters in music - they tell us what sounds to make!",
                    "See how the notes climb up and down? That's the melody!",
                    "Every note has a name: Do, Re, Mi, Fa, So, La, Ti, Do!",
                    "You're reading notes like a pro! Keep learning!",
                ]
            },
            "scale_sam": {
                "name": "Scale Sam",
                "description": "Scale teacher, patient voice",
                "speaker": "male-en-2",
                "icon": "🎚️",
                "color": "#FFD700",
                "phrases": [
                    "Good day! I'm Scale Sam, and scales are my specialty!",
                    "Scales are like musical staircases - step by step!",
                    "Let's practice going up and down together!",
                    "Major scales sound happy! Minor scales sound thoughtful!",
                    "Great work! Your scales are getting stronger every day!",
                ]
            },
            "dynamics_dana": {
                "name": "Dynamics Dana",
                "description": "Volume teacher, expressive voice",
                "speaker": "female-en-5",
                "icon": "🔊",
                "color": "#FF1493",
                "phrases": [
                    "Hello everyone! Let's learn about loud and soft in music!",
                    "Dynamics means how loud or quiet we play - it adds emotion!",
                    "Whisper quiet... or shout loud! Music has all the volumes!",
                    "Piano means soft, Forte means loud - these are Italian words!",
                    "Fantastic expression! You're bringing the music to life!",
                ]
            },
            "instrument_izzy": {
                "name": "Instrument Izzy",
                "description": "Instrument expert, enthusiastic voice",
                "speaker": "female-en-5",
                "icon": "🎸",
                "color": "#FF6347",
                "phrases": [
                    "Hey music lovers! Ready to learn about amazing instruments?",
                    "Every instrument has its own special sound and personality!",
                    "Strings, woodwinds, brass, and percussion - there's so much to explore!",
                    "What instrument would you like to play? Let's find your perfect match!",
                    "Wonderful! Keep discovering new sounds!",
                ]
            },
        }

    def generate_character_voice(self, character_id: str, phrase: str, filename: str):
        """Generate a single voice file for a character."""
        if character_id not in self.characters:
            print(f"❌ Character '{character_id}' not found")
            return False

        character = self.characters[character_id]
        output_file = self.output_dir / filename

        # Ensure output directory exists
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Create TTS script
        tts_script = f"""
from TTS.api import TTS
import sys

# Initialize TTS
tts = TTS(
    model_name="tts_models/multilingual/multi-dataset/your_tts",
    progress_bar=True,
    gpu=False
)

# Get speakers
speakers = tts.speakers
speaker = "{character['speaker']}"

# Generate voice
try:
    tts.tts_to_file(
        text='''{phrase}''',
        file_path="{output_file}",
        language="en",
        speaker=speaker
    )
    print(f"✅ Generated: {filename}")
except Exception as e:
    print(f"❌ Error: {{e}}")
    sys.exit(1)
"""

        # Save temporary script
        temp_script = self.output_dir / "_temp_tts.py"
        with open(temp_script, 'w') as f:
            f.write(tts_script)

        # Run TTS
        import subprocess
        try:
            result = subprocess.run(
                [str(self.tts_env), str(temp_script)],
                capture_output=True,
                text=True,
                timeout=60
            )

            if result.returncode == 0:
                print(f"✅ {character['name']}: {filename}")
                temp_script.unlink()  # Clean up
                return True
            else:
                print(f"❌ Failed: {result.stderr}")
                return False

        except Exception as e:
            print(f"❌ Error generating voice: {e}")
            return False

    def generate_all_character_voices(self):
        """Generate all voices for all characters."""
        print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🏝️ MUSIC ISLAND - Generating Teaching Voices 🏝️                  ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
        """)

        total = 0
        success = 0

        for character_id, character in self.characters.items():
            print(f"\n{character['icon']} Generating voices for {character['name']}...")

            for i, phrase in enumerate(character['phrases'], 1):
                filename = f"{character_id}_{i}.wav"
                total += 1

                if self.generate_character_voice(character_id, phrase, filename):
                    success += 1

        print(f"\n\n✨ Generation complete: {success}/{total} voices created!")
        print(f"📁 Output: {self.output_dir}")

    def get_character_manifest(self) -> Dict:
        """Get manifest of all characters."""
        return {
            character_id: {
                "name": character["name"],
                "description": character["description"],
                "icon": character["icon"],
                "color": character["color"],
                "voice_count": len(character["phrases"])
            }
            for character_id, character in self.characters.items()
        }


def main():
    """Main entry point."""
    generator = MusicIslandVoiceGenerator()

    print("🏝️ MUSIC ISLAND Voice Generator")
    print("=" * 60)
    print("\nTeachers:")
    for char_id, char in generator.characters.items():
        print(f"  {char['icon']} {char['name']} - {char['description']}")

    print("\n\nGenerating all voices...")
    generator.generate_all_character_voices()

    return 0


if __name__ == "__main__":
    sys.exit(main())
