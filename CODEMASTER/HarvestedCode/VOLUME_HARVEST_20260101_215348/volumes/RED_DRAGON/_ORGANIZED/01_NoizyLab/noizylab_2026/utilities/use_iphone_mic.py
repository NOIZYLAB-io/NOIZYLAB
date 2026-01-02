import sounddevice as sd
import speech_recognition as sr

def list_microphones():
    print("\nAvailable audio input devices:")
    devices = sd.query_devices()
    for i, dev in enumerate(devices):
        if dev['max_input_channels'] > 0:
            print(f"  [{i}] {dev['name']}")
    print()

def select_iphone_mic():
    print("Please connect your iPhone as a microphone (via Continuity Camera, WO Mic, or Bluetooth).")
    input("Press Enter when ready to list devices...")
    list_microphones()
    idx = int(input("Enter the device index for your iPhone mic: ").strip())
    print(f"Selected iPhone mic at index [{idx}]. Testing voice input...")
    recognizer = sr.Recognizer()
    mic = sr.Microphone(device_index=idx)
    with mic as source:
        print("🎙️ Listening for voice command from iPhone mic...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"🧠 Heard: {command}")
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Recognition error: {e}")

if __name__ == "__main__":
    select_iphone_mic()
