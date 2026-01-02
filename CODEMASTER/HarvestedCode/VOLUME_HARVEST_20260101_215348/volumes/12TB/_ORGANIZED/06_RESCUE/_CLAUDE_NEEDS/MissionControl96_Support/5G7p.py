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


def speak_with_elevenlabs(
    text, api_key,
    voice_id=None, model_id=None,
    stability=None, similarity_boost=None, style=None, speaker_boost=None, speed=None
):
    try:
        client = ElevenLabs(api_key=api_key)
        # Use environment variables or defaults for all settings
        voice_id = voice_id or os.getenv("BOBBY_VOICE_ID", "Rachel")
        model_id = model_id or os.getenv("BOBBY_MODEL_ID", "eleven_multilingual_v2")
        stability = float(os.getenv("BOBBY_STABILITY", stability if stability is not None else 0.5))
        similarity_boost = float(os.getenv("BOBBY_SIMILARITY_BOOST", similarity_boost if similarity_boost is not None else 0.75))
        style = float(os.getenv("BOBBY_STYLE", style if style is not None else 0.0))
        speaker_boost = bool(int(os.getenv("BOBBY_SPEAKER_BOOST", int(speaker_boost) if speaker_boost is not None else 1)))
        speed = float(os.getenv("BOBBY_SPEED", speed if speed is not None else 1.0))

        # Print current settings for user
        print(f"[Bobby] ElevenLabs voice settings: voice_id={voice_id}, model_id={model_id}, stability={stability}, similarity_boost={similarity_boost}, style={style}, speaker_boost={speaker_boost}, speed={speed}")

        audio_gen = client.text_to_speech.convert(
            voice_id=voice_id,
            model_id=model_id,
            text=text,
            stability=stability,
            similarity_boost=similarity_boost,
            style=style,
            speaker_boost=speaker_boost,
            speed=speed
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
