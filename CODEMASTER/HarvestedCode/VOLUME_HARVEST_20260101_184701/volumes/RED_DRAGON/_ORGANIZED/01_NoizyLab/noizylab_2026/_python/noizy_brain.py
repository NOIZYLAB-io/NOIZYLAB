#!/usr/bin/env python3
"""
noizy_brain.py
Minimal Noizy Brain stub, identical to Super Brain for Bubba integration.
Accepts a prompt and replies with a thoughtful placeholder.
"""

import sys
from datetime import datetime
from pathlib import Path

WORKSPACE = Path.home() / "Documents" / "Noizyfish_Aquarium" / "Noizy_Workspace"
SAVE_DIR = WORKSPACE / "Saved_Notes"
SAVE_DIR.mkdir(parents=True, exist_ok=True)

def save_log(prompt, reply):
    """Save conversation into a timestamped log."""
    log_file = SAVE_DIR / f"noizy_brain_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    content = f"PROMPT:\n{prompt}\n\nREPLY:\n{reply}\n"
    log_file.write_text(content, encoding="utf-8")
    return log_file

def generate_reply(prompt: str) -> str:
    """Very simple placeholder response."""
    # Later this can call OpenAI API, 11Labs, etc.
    if "pitch" in prompt.lower():
        return "Noizy Brain Draft Pitch: NoizyFish is building the future of music with AI, legacy voices, and cross-platform tools."
    elif "hello" in prompt.lower():
        return "Hello, my dear Bubba. I'm always listening."
    else:
        return f"I've received your request: '{prompt}'. Processing complete."

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 noizy_brain.py <prompt>")
        sys.exit(1)

    prompt = " ".join(sys.argv[1:])
    reply = generate_reply(prompt)
    save_log(prompt, reply)
    print(reply)

if __name__ == "__main__":
    main()
