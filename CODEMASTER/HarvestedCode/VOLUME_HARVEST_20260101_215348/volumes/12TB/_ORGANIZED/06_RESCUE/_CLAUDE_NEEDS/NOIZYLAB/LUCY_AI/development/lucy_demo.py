#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎸 LUCY DEMO - Interactive Voice Player 🎸                         ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import subprocess
import sys
from pathlib import Path


def play_audio(file_path):
    """Play an audio file."""
    subprocess.run(["afplay", str(file_path)])


def main():
    """Interactive Lucy demo."""

    print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎸 LUCY DEMO - Interactive Voice Player 🎸                         ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝

🎸 LUCY's Available Voices:

1. Greeting  - "Bonjour, darling! Ready to sort..."
2. Code      - "I absolutely adore writing clean code..."
3. Apple     - "With my forty-eight years of Apple knowledge..."
4. French    - "Bonjour! Comment allez-vous?..."
5. Cheerio   - "Cheerio, darling! Keep being brilliant!"
6. Play All
7. Exit

    """)

    base_path = Path(__file__).parent

    voices = {
        "1": base_path / "lucy_greeting.wav",
        "2": base_path / "lucy_code.wav",
        "3": base_path / "lucy_apple.wav",
        "4": base_path / "lucy_french.wav",
        "5": base_path / "lucy_cheerio.wav",
    }

    while True:
        try:
            choice = input("Choose a voice (1-7): ").strip()

            if choice == "7":
                print("\n👋 Cheerio, darling!")
                break

            if choice == "6":
                print("\n🎸 Playing all Lucy's voices...\n")
                for num in ["1", "2", "3", "4", "5"]:
                    if voices[num].exists():
                        print(f"▶️  Playing voice {num}...")
                        play_audio(voices[num])
                    else:
                        print(f"⚠️  Voice file not found: {voices[num]}")
                print()
                continue

            if choice in voices:
                if voices[choice].exists():
                    print(f"\n🎤 Playing LUCY's voice...\n")
                    play_audio(voices[choice])
                    print()
                else:
                    print(f"\n⚠️  Voice file not found: {voices[choice]}")
                    print("Run: tts_env/bin/python lucy_tts_advanced.py\n")
            else:
                print("\n❌ Invalid choice. Please choose 1-7.\n")

        except KeyboardInterrupt:
            print("\n\n👋 Cheerio, darling!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
