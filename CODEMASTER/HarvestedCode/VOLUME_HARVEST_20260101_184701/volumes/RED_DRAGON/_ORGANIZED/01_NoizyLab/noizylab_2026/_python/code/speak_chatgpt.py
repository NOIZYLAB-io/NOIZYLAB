import re
import subprocess
import pyperclip
import sys

def strip_code(input_text):
    # remove triple-backtick code blocks
    return re.sub(r"```.*?```", "", input_text, flags=re.DOTALL)

def speak(input_text):
    clean = strip_code(input_text).strip()
    if clean:
        subprocess.run(["say", clean], check=True)

if __name__ == "__main__":
    # Use clipboard if no stdin
    if sys.stdin.isatty():
        clipboard_text = pyperclip.paste()
        if not clipboard_text.strip():
            print("Clipboard is empty. Copy some text and try again.")
        else:
            speak(clipboard_text)
    else:
        stdin_text = sys.stdin.read()
        speak(stdin_text)
