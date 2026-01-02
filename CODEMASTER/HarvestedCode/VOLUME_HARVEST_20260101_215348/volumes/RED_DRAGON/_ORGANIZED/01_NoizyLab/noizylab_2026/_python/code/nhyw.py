#!/usr/bin/env python3
"""
cha_cha_read_chat.py
Cha-Cha reads the current ChatGPT conversation from clipboard.
Facts-only: strips code blocks and system junk.
"""

import subprocess
import re

VOICE = "Siri Voice 1"


def get_clipboard():
    try:
        return subprocess.check_output("pbpaste", text=True)
    except (subprocess.CalledProcessError, OSError) as err:
        print(f"Clipboard error: {err}")
        return ""


def clean_text(text):
    # Remove code blocks
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    # Remove extra spaces/newlines
    text = re.sub(r"\n{2,}", "\n", text)
    return text.strip()


def speak(text):
    if text:
        try:
            subprocess.run(["say", "-v", VOICE, text], check=False)
        except (subprocess.SubprocessError, OSError) as err:
            print(f"Voice error: {err}")


def main():
    raw = get_clipboard()
    cleaned = clean_text(raw)
    if not cleaned:
        print("❌ Nothing to read. Copy chat text to clipboard first.")
        return
    print("✅ Cha-Cha reading ChatGPT conversation...")
    speak(cleaned)


if __name__ == "__main__":
    main()