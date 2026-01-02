#!/usr/bin/env python3
"""
cha_cha_read_chat.py
Cha-Cha reads the ChatGPT conversation from clipboard.
Facts-only: strips code blocks and system junk.
"""

import subprocess, re

VOICE = "Siri Voice 1"

def get_clipboard():
    try:
        return subprocess.check_output("pbpaste", text=True)
    except Exception:
        return ""

def clean_text(text):
    # Remove code blocks
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    # Remove extra spaces/newlines
    text = re.sub(r"\n{2,}", "\n", text)
    return text.strip()

def speak(text):
    if text:
        subprocess.run(["say", "-v", VOICE, text])

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
