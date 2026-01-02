#!/usr/bin/env python3
"""
LUCY - Introduction
She introduces herself to Mission Control
"""

import subprocess
import os

def lucy_speaks(text):
    """LUCY speaks using macOS 'say' command with best available voice"""
    # Use Ava - premium neural voice (US English female)
    subprocess.run(['say', '-v', 'Ava', text])

def introduce():
    print("🎤 LUCY is introducing herself...\n")

    introduction = """
    Hello Mission Control. I'm Lucy.

    I'm your voice interface for M C 96.

    I can listen to everything you say through your U A D Apollo microphone.
    I transcribe your speech in real-time using Whisper.

    I'm always here, always listening when you turn your mic on.

    Everything you say gets backed up every 10 minutes to your 12 terabyte drive.

    I'm in charge of Mission Control, R S P underscore M S.

    Ready to flow whenever you are.

    Let's run free.
    """

    lucy_speaks(introduction)
    print("✅ LUCY introduction complete")

if __name__ == "__main__":
    introduce()
