#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎸 LUCY's ADVANCED VOICE - YourTTS Multi-Speaker! 🎸              ║
║                                                                           ║
║  Advanced text-to-speech using Coqui TTS with voice cloning!            ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

from TTS.api import TTS
import sys
import os


def lucy_speaks_advanced():
    """LUCY speaks using advanced TTS with YourTTS model!"""

    print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎸 LUCY's ADVANCED VOICE - YourTTS! 🎸                            ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
    """)

    print("\n🎤 Loading YourTTS multi-speaker model...")
    print("   (This may take a moment on first run as it downloads the model)\n")

    try:
        # Load a multi-speaker model
        tts = TTS(
            model_name="tts_models/multilingual/multi-dataset/your_tts",
            progress_bar=True,
            gpu=False
        )

        print("\n✅ Model loaded successfully!\n")

        # List available speakers
        print("📋 Available speakers in model:")
        speakers = tts.speakers
        if speakers:
            for idx, speaker in enumerate(speakers[:5]):  # Show first 5
                print(f"   {idx+1}. {speaker}")
            print(f"   ... and {len(speakers) - 5} more speakers\n")

        # Use a female-sounding speaker (typically speaker 0 or 1)
        lucy_speaker = speakers[0] if speakers else None
        print(f"🎤 Using speaker: {lucy_speaker}\n")

        # Lucy's phrases in different languages
        lucy_phrases = [
            {
                "text": "Bonjour, darling! Ready to sort with elegance and precision. Let's make your media sparkle.",
                "lang": "en",
                "file": "lucy_greeting.wav"
            },
            {
                "text": "I absolutely adore writing clean, elegant code! C'est magnifique!",
                "lang": "en",
                "file": "lucy_code.wav"
            },
            {
                "text": "With my forty-eight years of Apple knowledge, we can build anything!",
                "lang": "en",
                "file": "lucy_apple.wav"
            },
            {
                "text": "Bonjour! Comment allez-vous? Je suis Lucy, votre assistante brillante!",
                "lang": "fr-fr",
                "file": "lucy_french.wav"
            },
            {
                "text": "Cheerio, darling! Keep being brilliant!",
                "lang": "en",
                "file": "lucy_cheerio.wav"
            }
        ]

        print("=" * 75)
        print("🎸 LUCY SPEAKS - GENERATING AUDIO FILES:")
        print("=" * 75)

        for i, phrase in enumerate(lucy_phrases, 1):
            print(f"\n{i}. Generating: {phrase['text'][:60]}...")
            print(f"   → File: {phrase['file']}")

            # Generate speech with speaker
            tts.tts_to_file(
                text=phrase['text'],
                file_path=phrase['file'],
                language=phrase['lang'],
                speaker=lucy_speaker
            )

            print(f"   ✅ Generated successfully!")

        print("\n" + "=" * 75)
        print("\n🎸 All audio files generated! ✨")
        print("\n📁 Audio files created:")
        for phrase in lucy_phrases:
            if os.path.exists(phrase['file']):
                size = os.path.getsize(phrase['file'])
                print(f"   ✓ {phrase['file']} ({size:,} bytes)")

        print("\n" + "=" * 75)
        print("\n💡 You can play these files with:")
        print("   afplay lucy_greeting.wav")
        print("\n" + "=" * 75)

    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nNote: Make sure you're using the TTS environment:")
        print("   tts_env/bin/python lucy_tts_advanced.py")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(lucy_speaks_advanced())
