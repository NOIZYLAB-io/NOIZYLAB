#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🐠 FISHY STORYS - Voice Character Generator 🐠                    ║
║                                                                           ║
║  Generate custom voices for interactive children's storytelling         ║
║  Part of VOX - Voice Control Application                                 ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import sys
from pathlib import Path
from typing import Dict, List

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent.parent))


class FishyStorysVoiceGenerator:
    """Generate voices for FISHY STORYS characters."""

    def __init__(self):
        self.base_path = Path("/Users/rsp_ms/MC96_MobileApp")
        self.tts_env = self.base_path / "LUCY" / "tts_env" / "bin" / "python"
        self.output_dir = self.base_path / "VOX" / "characters" / "FISHY_STORYS"

        # Story characters with voice models
        self.characters = {
            "captain_finn": {
                "name": "Captain Finn",
                "description": "Wise old fish captain, deep soothing voice",
                "speaker": "male-en-2",
                "icon": "🎣",
                "color": "#1E90FF",
                "phrases": [
                    "Ahoy there, young sailors! Welcome aboard the S.S. Fishy!",
                    "Let me tell you a tale from the deep blue sea...",
                    "In my many years sailing these waters, I've learned that every fish has a story.",
                    "Gather 'round, children, and I'll share the wisdom of the ocean.",
                    "The sea teaches us patience, courage, and friendship!",
                ]
            },
            "bubbles": {
                "name": "Bubbles",
                "description": "Cheerful little goldfish, bubbly high voice",
                "speaker": "female-en-5",
                "icon": "🐟",
                "color": "#FFD700",
                "phrases": [
                    "Hi hi! I'm Bubbles and I LOVE making new friends!",
                    "Ooh ooh! This is so exciting! Let's go on an adventure!",
                    "Did you know? Fish can see colors that humans can't!",
                    "Wheee! Swimming through the coral is my favorite thing ever!",
                    "Let's learn something new together! Learning is fun!",
                ]
            },
            "professor_scales": {
                "name": "Professor Scales",
                "description": "Smart academic fish, clear teaching voice",
                "speaker": "male-en-2",
                "icon": "🎓",
                "color": "#4B0082",
                "phrases": [
                    "Good day, students! Professor Scales here, ready to teach!",
                    "Today's lesson is about the wonderful world beneath the waves.",
                    "Fascinating! Did you know that some fish can breathe both water and air?",
                    "Let's explore the science of swimming and buoyancy!",
                    "Remember: Knowledge is like the ocean - vast and full of wonders!",
                ]
            },
            "marina_melody": {
                "name": "Marina Melody",
                "description": "Musical fish singer, melodic voice",
                "speaker": "female-en-5",
                "icon": "🎵",
                "color": "#FF69B4",
                "phrases": [
                    "♪ Hello my dear friends, let's sing and play! ♪",
                    "Music makes the ocean brighter! Let me teach you a sea shanty!",
                    "♪ La la la, swimming free, in the deep blue sea! ♪",
                    "Every fish has their own song. What's yours?",
                    "Let's learn about rhythm and melody together!",
                ]
            },
            "reef_the_explorer": {
                "name": "Reef the Explorer",
                "description": "Adventurous young fish, excited voice",
                "speaker": "male-en-2",
                "icon": "🗺️",
                "color": "#20B2AA",
                "phrases": [
                    "Woah! Look at that! There's SO much to discover!",
                    "Come on, let's explore this reef together!",
                    "I wonder what's beyond that coral castle? Let's find out!",
                    "Every day is a new adventure in the ocean!",
                    "Being brave doesn't mean not being scared - it means swimming forward anyway!",
                ]
            },
            "grandma_pearl": {
                "name": "Grandma Pearl",
                "description": "Loving grandma fish, warm gentle voice",
                "speaker": "female-en-5",
                "icon": "👵",
                "color": "#C0C0C0",
                "phrases": [
                    "Oh my dear little fishies, come here and let me tell you a story.",
                    "When I was just a tiny guppy, we used to play in these very waters.",
                    "Remember sweethearts, kindness makes the biggest waves.",
                    "There there, everything will be alright. Grandma's here.",
                    "The ocean keeps all our memories, just like I keep you in my heart.",
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
║        🐠 FISHY STORYS - Generating Character Voices 🐠                  ║
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
    generator = FishyStorysVoiceGenerator()

    print("🐠 FISHY STORYS Voice Generator")
    print("=" * 60)
    print("\nCharacters:")
    for char_id, char in generator.characters.items():
        print(f"  {char['icon']} {char['name']} - {char['description']}")

    print("\n\nGenerating all voices...")
    generator.generate_all_character_voices()

    return 0


if __name__ == "__main__":
    sys.exit(main())
