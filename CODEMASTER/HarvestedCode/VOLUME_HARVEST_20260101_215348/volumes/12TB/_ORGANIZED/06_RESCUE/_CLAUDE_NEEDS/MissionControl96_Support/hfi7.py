import requests
import subprocess
import threading
import time
import sys
import termios
import tty
import os

# --- 11 Labs Sarah TTS ---
def sarah_11labs_speak(text):
    api_key = "YOUR_11LABS_API_KEY"  # Replace with your actual API key
    voice_id = "YOUR_SARAH_VOICE_ID"  # Replace with your actual Sarah voice ID
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {"xi-api-key": api_key}
    data = {"text": text, "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}}
    try:
        response = requests.post(url, json=data, headers=headers)
        if response.ok:
            with open("sarah_output.mp3", "wb") as f:
                f.write(response.content)
            player = threading.Thread(target=subprocess.run, args=(["afplay", "sarah_output.mp3"],))
            player.start()
            return player
        else:
            print("Error with 11 Labs TTS:", response.text)
    except Exception as e:
        print("TTS execution failed:", e)
    return None

# --- Keyboard listener for spacebar ---
def wait_for_spacebar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        while True:
            ch = sys.stdin.read(1)
            if ch == ' ':
                return
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

# --- VS Code Automation Functions ---
def open_vscode():
    subprocess.run(["open", "-a", "Visual Studio Code"])
    sarah_11labs_speak("VS Code is now open.")

def run_vscode_command(command):
    subprocess.run(["code", "--command", command])
    sarah_11labs_speak(f"Ran VS Code command: {command}")

def read_file_with_sarah(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            content = f.read()
        sarah_11labs_speak(content)
    else:
        sarah_11labs_speak(f"File {filepath} not found.")

def announce_status():
    status = "All accessibility features are active. You can control VS Code, read files, and get spoken feedback. Press space to read the current status again."
    sarah_11labs_speak(status)

# --- Main Accessibility Dashboard ---
def main():
    announce_status()
    while True:
        print("Press SPACE to read status, 'o' to open VS Code, 'r' to read a file, 'c' to run a VS Code command, 'q' to quit.")
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
            if ch == ' ':
                announce_status()
            elif ch == 'o':
                open_vscode()
            elif ch == 'r':
                sarah_11labs_speak("Enter file path to read.")
                path = input("File path: ")
                read_file_with_sarah(path)
            elif ch == 'c':
                sarah_11labs_speak("Enter VS Code command to run.")
                cmd = input("VS Code command: ")
                run_vscode_command(cmd)
            elif ch == 'q':
                sarah_11labs_speak("Goodbye. Accessibility dashboard closed.")
                break
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

if __name__ == "__main__":
    main()
