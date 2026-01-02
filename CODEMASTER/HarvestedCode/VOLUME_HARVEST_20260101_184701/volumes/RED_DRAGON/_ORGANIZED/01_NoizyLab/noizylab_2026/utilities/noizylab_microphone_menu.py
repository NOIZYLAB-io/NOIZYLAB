import sounddevice as sd
import speech_recognition as sr

MENU = """
NOIZYLAB Microphone Menu:
1. List all microphones
2. Test microphone input
3. Set default microphone for NOIZYLAB
4. Record and playback a sample
5. Use mic for voice command (test)
6. Exit
"""
def list_microphones():
    print("\nAvailable audio input devices:")
    devices = sd.query_devices()
    for i, dev in enumerate(devices):
        if dev['max_input_channels'] > 0:
            print(f"  [{i}] {dev['name']}")
    print()

def test_microphone(idx):
    print(f"Testing microphone [{idx}]...")
    duration = 3
    print("Speak now...")
    recording = sd.rec(int(duration * sd.query_devices(idx)['default_samplerate']), samplerate=int(sd.query_devices(idx)['default_samplerate']), channels=1, dtype='float64', device=idx)
    sd.wait()
    print("Playback...")
    sd.play(recording, int(sd.query_devices(idx)['default_samplerate']))
    sd.wait()
    print("Test complete.\n")

def use_for_voice_command(idx):
    recognizer = sr.Recognizer()
    mic = sr.Microphone(device_index=idx)
    with mic as source:
        print("🎙️ Listening for voice command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"🧠 Heard: {command}")
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Recognition error: {e}")

def main():
    default_idx = None
    while True:
        print(MENU)
        choice = input("Select an option: ").strip()
        if choice == "1":
            list_microphones()
        elif choice == "2":
            idx = int(input("Enter device index to test: ").strip())
            test_microphone(idx)
        elif choice == "3":
            idx = int(input("Enter device index to set as default: ").strip())
            default_idx = idx
            print(f"Default microphone set to [{idx}].\n")
        elif choice == "4":
            idx = default_idx if default_idx is not None else int(input("Enter device index to record: ").strip())
            test_microphone(idx)
        elif choice == "5":
            idx = default_idx if default_idx is not None else int(input("Enter device index to use: ").strip())
            use_for_voice_command(idx)
        elif choice == "6":
            print("Exiting NOIZYLAB Microphone Menu.")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
