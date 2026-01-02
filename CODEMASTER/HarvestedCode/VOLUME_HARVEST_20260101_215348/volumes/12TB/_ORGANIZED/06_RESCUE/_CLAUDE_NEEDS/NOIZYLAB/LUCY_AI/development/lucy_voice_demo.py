#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎸 LUCY's VOICE - Text-to-Speech Demo! 🎸                         ║
║                                                                           ║
║  Hear LUCY speak using macOS text-to-speech!                             ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

import pyttsx3
import time


def lucy_speaks():
    """LUCY speaks using text-to-speech!"""

    print("""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        🎸 LUCY's VOICE - DEMO! 🎸                                        ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
    """)

    # Initialize the TTS engine
    engine = pyttsx3.init()

    # Get available voices
    voices = engine.getProperty('voices')

    # Try to find a female British voice (for Lucy)
    # On macOS, look for Samantha, Kate, or other female voices
    british_voice = None
    for voice in voices:
        if 'female' in voice.name.lower() or 'kate' in voice.name.lower() or 'samantha' in voice.name.lower():
            british_voice = voice.id
            print(f"\n🎤 Using voice: {voice.name}")
            break

    if british_voice:
        engine.setProperty('voice', british_voice)

    # Set speech rate (slower for Lucy's warm style)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 30)  # Slower, more elegant

    # Set volume
    engine.setProperty('volume', 0.9)

    # Lucy's greetings and phrases
    lucy_phrases = [
        "Bonjour, darling! I'm Lucy!",
        "Ready to create something brilliant together?",
        "I absolutely adore writing clean, elegant code!",
        "Magnifique! Let's make some magic!",
        "With my forty-eight years of Apple knowledge, we can build anything!",
        "Cheerio, darling! Keep being brilliant!"
    ]

    print("\n" + "="*75)
    print("🎸 LUCY SPEAKS:")
    print("="*75)

    for i, phrase in enumerate(lucy_phrases, 1):
        print(f"\n{i}. {phrase}")
        engine.say(phrase)
        engine.runAndWait()
        time.sleep(0.5)

    print("\n" + "="*75)
    print("\n🎸 That's Lucy's voice! Isn't it lovely? ✨")
    print("\n" + "="*75)


if __name__ == "__main__":
    try:
        lucy_speaks()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nNote: Make sure pyttsx3 is installed: pip3 install pyttsx3")
