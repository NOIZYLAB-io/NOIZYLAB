import threading
try:
    from bobby_bubble import BobbyBubble
    bubble = BobbyBubble()
except Exception:
    bubble = None

def speak_debug_lines(text_or_lines):
    """
    Speak all lines containing debug, error, or warning keywords.
    Accepts a string (multi-line) or a list of lines.
    """
    if isinstance(text_or_lines, str):
        lines = text_or_lines.splitlines()
    else:
        lines = text_or_lines
    keywords = ("debug", "error", "warn", "fail", "urgent")
    for line in lines:
        if any(k in line.lower() for k in keywords):
            urgent_announcement(line)

#!/usr/bin/env python3


import sys
import os
import subprocess
import numpy as np
import sounddevice as sd
import speech_recognition as sr
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play

def install_and_import(package, pip_name=None):
    import importlib
    try:
        return importlib.import_module(package)
    except ImportError:
        pip_name = pip_name or package
        print(f"[INFO] Installing {pip_name}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])
        return importlib.import_module(package)

np = install_and_import('numpy')
sd = install_and_import('sounddevice')
elevenlabs = install_and_import('elevenlabs')
sr = install_and_import('speech_recognition', 'SpeechRecognition')
from elevenlabs import ElevenLabs


def speak_with_elevenlabs(
    text, api_key,
    voice_id=None, model_id=None,
    stability=None, similarity_boost=None, style=None, speaker_boost=None, speed=None
):
    try:
        from elevenlabs.types.voice_settings import VoiceSettings
        print(f"[DEBUG] VoiceSettings type: {type(VoiceSettings)}")
        client = ElevenLabs(api_key=api_key)
        settings = VoiceSettings(
            stability=stability or float(os.getenv("BOBBY_STABILITY", 0.5)),
            similarity_boost=similarity_boost or float(os.getenv("BOBBY_SIMILARITY_BOOST", 0.75)),
            style=style or float(os.getenv("BOBBY_STYLE", 0.0)),
            use_speaker_boost=speaker_boost or bool(int(os.getenv("BOBBY_SPEAKER_BOOST", 1))),
            speed=speed or float(os.getenv("BOBBY_SPEED", 1.0)),
        )
        if bubble:
            threading.Thread(target=bubble.show_message, args=(text,), daemon=True).start()
        audio_gen = client.text_to_speech.convert(
            voice_id=voice_id or os.getenv("BOBBY_VOICE_ID", "Rachel"),
            text=text,
            model_id=model_id or os.getenv("BOBBY_MODEL_ID", "eleven_multilingual_v2"),
            voice_settings=settings,
            output_format="mp3_44100_128",
        )
        print(f"[DEBUG] audio type: {type(audio_gen)}")
        audio_bytes = b"".join(audio_gen)
        play(audio_bytes)
        return True
    except Exception as e:
        print(f"[ERROR] ElevenLabs TTS failed: {e}")
        return False

def speak_with_say(text):
    try:
        if bubble:
            threading.Thread(target=bubble.show_message, args=(text,), daemon=True).start()
        subprocess.run(["say", text], check=True)
        return True
    except Exception as e:
        print(f"[ERROR] macOS 'say' failed: {e}")
        return False

def listen_and_recognize():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print("[Bobby] Listening... Please speak now.")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"[Bobby heard]: {text}")
        return text
    except sr.UnknownValueError:
        print("[Bobby] Sorry, I could not understand your speech.")
        return None
    except sr.RequestError as e:
        print(f"[Bobby] Could not request results from Google Speech Recognition service; {e}")
        return None


def launch_all_agents():
    script_path = os.path.join(os.path.dirname(__file__), '_utilities/scripts/launch_all_agents.sh')
    if os.path.exists(script_path):
        subprocess.Popen(['zsh', script_path])


def urgent_announcement(message):
    # Use Bobby's voice to announce urgent issues
    try:
        import subprocess
        subprocess.Popen(['say', message])  # macOS TTS
    except Exception as e:
        print(f"[URGENT] {message}")


def main():
    # If text is passed as argument, use it once. Otherwise, enter interactive loop.
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        print("[Bobby] ELEVENLABS_API_KEY not set. Please paste your ElevenLabs API key below (input hidden):")
        import getpass
        api_key = getpass.getpass("API Key: ")
        os.environ["ELEVENLABS_API_KEY"] = api_key
    print("[Bobby] You can customize Bobby's ElevenLabs voice with these environment variables:")
    print("  BOBBY_VOICE_ID (default: Rachel)")
    print("  BOBBY_MODEL_ID (default: eleven_multilingual_v2)")
    print("  BOBBY_STABILITY (0.0-1.0, default: 0.5)")
    print("  BOBBY_SIMILARITY_BOOST (0.0-1.0, default: 0.75)")
    print("  BOBBY_STYLE (0.0-1.0, default: 0.0)")
    print("  BOBBY_SPEAKER_BOOST (0 or 1, default: 1)")
    print("  BOBBY_SPEED (0.5-2.0, default: 1.0)")
    print("[Bobby] Set these in your shell or VS Code launch config to change Bobby's voice!")

    if len(sys.argv) > 1:
        text = " ".join(sys.argv[1:])
        print(f"[Bobby] Speaking: {text}")
        if api_key:
            success = speak_with_elevenlabs(text, api_key)
            if success:
                return
            print("[INFO] Falling back to macOS 'say' command.")
            speak_with_say(text)
        else:
            print("[WARN] ELEVENLABS_API_KEY not set. Using macOS 'say' command.")
            speak_with_say(text)
        return

    print("[Bobby] Voice assistant is active. Speak after the beep. Say 'goodbye Bobby' to exit.")
    if bubble:
        threading.Thread(target=bubble.root.mainloop, daemon=True).start()
    if not api_key:
        print("[Bobby] Tip: Set ELEVENLABS_API_KEY for premium voice. Using macOS 'say' by default.")

    import time
    last_active = time.time()
    greeted_today = False
    idle_threshold = 60 * 30  # 30 minutes idle

    try:
        while True:
            now = time.time()
            # If just started or after long idle, greet and ask if ready to work
            if not greeted_today or (now - last_active > idle_threshold):
                speak_with_say("Welcome back! Are you ready to get to work?")
                print("[Bobby] Waiting for your response...")
                response = listen_and_recognize()
                if response and response.strip().lower() in ["yes", "let's go", "ready", "about time", "keep going", "yep", "sure"]:
                    speak_with_say("About time! Let's keep going. Here are your sorted priorities for today.")
                    sorted_lines = ["1. Check urgent emails", "2. Review project status", "3. Continue with code organization", "4. Debug any issues found"]
                    for line in sorted_lines:
                        speak_with_say(line)
                    greeted_today = True
                else:
                    speak_with_say("Okay, I'll wait until you're ready.")
                    greeted_today = True
                last_active = now

            # Wake word loop: only proceed if user says 'hey Bobby'
            print("[Bobby] Waiting for wake word 'hey Bobby'...")
            while True:
                try:
                    os.system('printf "\\a"')
                except Exception:
                    pass
                wake = listen_and_recognize()
                if wake and "hey bobby" in wake.strip().lower():
                    speak_with_say("Yes? I'm listening.")
                    break
            # Now listen for the actual command
            text = listen_and_recognize()
            if not text:
                continue
            last_active = time.time()
            cmd = text.strip().lower()
            if cmd in ["goodbye bobby", "exit", "quit", "stop listening"]:
                print("[Bobby] Goodbye!")
                speak_with_say("Goodbye!")
                break
            print(f"[Bobby] Heard: {text}")

            # Volume management: debug the entire drive
            if any(phrase in cmd for phrase in ["debug the entire drive", "debug all drives", "scan all drives", "manage all volumes", "manage all drives"]):
                volumes = [v for v in os.listdir("/Volumes") if os.path.isdir(os.path.join("/Volumes", v))]
                if not volumes:
                    speak_with_say("No external volumes found.")
                    continue
                speak_with_say("Which drive would you like to debug? Here are the available drives: " + ", ".join(volumes))
                print("[Bobby] Waiting for drive name...")
                drive_name = listen_and_recognize()
                if not drive_name:
                    speak_with_say("Sorry, I didn't catch the drive name.")
                    continue
                drive_name = drive_name.strip()
                if drive_name not in volumes:
                    speak_with_say(f"Drive {drive_name} not found. Please try again.")
                    continue
                speak_with_say(f"Debugging drive {drive_name} now.")
                continue

            # Default: speak the command as usual
            if api_key:
                success = speak_with_elevenlabs(text, api_key)
                if not success:
                    print("[INFO] Falling back to macOS 'say' command.")
                    speak_with_say(text)
            else:
                speak_with_say(text)
    except KeyboardInterrupt:
        print("\n[Bobby] Voice assistant stopped by user.")
    except Exception as e:
        print(f"[Bobby] Unexpected error: {e}")
        speak_with_say("Sorry, something went wrong.")

if __name__ == "__main__":
    launch_all_agents()
    main()
