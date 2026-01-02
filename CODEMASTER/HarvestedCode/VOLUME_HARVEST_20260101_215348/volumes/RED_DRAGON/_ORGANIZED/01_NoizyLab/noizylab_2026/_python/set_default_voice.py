import subprocess
import os

def set_default_voice():
    voice_name = "Siri (United Kingdom)"
    try:
        subprocess.run([
            "defaults", "write", "com.apple.speech.voice.prefs", "SelectedVoiceName", voice_name
        ], check=True)
        subprocess.run([
            "killall", "-u", os.getlogin(), "cfprefsd"
        ], check=True)
        print(f"Default system voice set to: {voice_name}")
        subprocess.run([
            "say", "-v", voice_name, "Hello Rob, I am now your British Siri voice."
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error setting voice: {e}")

if __name__ == "__main__":
    set_default_voice()
