#!/usr/bin/env python3


import sys
import os
import subprocess

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

def speak_with_elevenlabs(text, api_key, voice_id="Rachel", model_id="eleven_multilingual_v2"):
    try:
        client = ElevenLabs(api_key=api_key)
        audio_gen = client.text_to_speech.convert(
            voice_id=voice_id,
            model_id=model_id,
            text=text
        )
        audio_bytes = b"".join(audio_gen)
        sd.play(np.frombuffer(audio_bytes, dtype=np.int16), samplerate=44100)
        sd.wait()
        return True
    except Exception as e:
        print(f"[ERROR] ElevenLabs TTS failed: {e}")
        return False

def speak_with_say(text):
    try:
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


def main():
    # If text is passed as argument, use it once. Otherwise, enter interactive loop.
    api_key = os.getenv("ELEVENLABS_API_KEY")
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
    if not api_key:
        print("[Bobby] Tip: Set ELEVENLABS_API_KEY for premium voice. Using macOS 'say' by default.")
    try:
        while True:
            print("[Bobby] Ready for your command...")
            # Optional: play a beep to indicate listening
            try:
                import os
                os.system('printf "\\a"')
            except Exception:
                pass
            text = listen_and_recognize()
            if not text:
                continue
            if text.strip().lower() in ["goodbye bobby", "exit", "quit", "stop listening"]:
                print("[Bobby] Goodbye!")
                speak_with_say("Goodbye!")
                break
            print(f"[Bobby] Heard: {text}")
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
    main()
