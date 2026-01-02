import re
import subprocess
import pyperclip
import sys

def strip_code(text):
    # remove triple-backtick code blocks
    return re.sub(r"```.*?```", "", text, flags=re.DOTALL)

def speak(text):
    clean = strip_code(text).strip()
    if clean:
        subprocess.run(["say", clean])

if __name__ == "__main__":
    # Use clipboard if no stdin
    if sys.stdin.isatty():
        text = pyperclip.paste()
        if not text.strip():
            print("Clipboard is empty. Copy some text and try again.")
        else:
            speak(text)
    else:
        text = sys.stdin.read()
        speak(text)
