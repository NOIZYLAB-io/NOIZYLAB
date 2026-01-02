import speech_recognition as sr
import os

def main():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say a Bobby Mission Control command (e.g. 'build dashboard', 'start backend'):")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            if "build dashboard" in command:
                os.system("cd ~/bobby-mission-control && npm run tauri build")
            elif "start backend" in command:
                os.system("cd ~/bobby-mission-control/backend && source .venv/bin/activate && uvicorn backend:app --reload --port 8000")
            elif "run dashboard" in command or "launch dashboard" in command:
                os.system("cd ~/bobby-mission-control && npm run tauri dev")
            else:
                print("Command not recognized. Try: 'build dashboard', 'start backend', or 'run dashboard'.")
        except Exception as e:
            print(f"Could not understand audio: {e}")

if __name__ == "__main__":
    main()
