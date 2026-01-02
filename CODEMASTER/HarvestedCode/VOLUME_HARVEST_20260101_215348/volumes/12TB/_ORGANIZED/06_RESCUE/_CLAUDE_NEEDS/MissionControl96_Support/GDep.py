import os
import subprocess
import time
import speech_recognition as sr

# CONFIGURATION
FILE_PATH = "/Users/rsp_ms/Documents/rituals/my_script.py"
RUNTIME = "python3"
GIT_ENABLED = True
GIT_COMMIT_MSG = "🔁 Ritual Executed: Capsule Clean — Soul Synced to Legacy Grid"

def speak(message):
    os.system(f'say "{message}"')

def listen_for_command():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("🎙️ Listening for ritual command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"🧠 Heard: {command}")
        return command
    except sr.UnknownValueError:
        speak("I didn't catch that. Try again.")
        return None

def is_valid_python(file_path):
    try:
        subprocess.check_output([RUNTIME, "-m", "py_compile", file_path])
        return True
    except subprocess.CalledProcessError:
        return False

def auto_save_and_run():
    speak("Validating capsule...")
    if is_valid_python(FILE_PATH):
        speak("Code is clean. Executing ritual.")
        subprocess.run([RUNTIME, FILE_PATH])
        if GIT_ENABLED:
            git_sync()
    else:
        speak("Syntax error detected. Launching fallback overlay.")
        launch_debugger()

def git_sync():
    speak("Syncing soul to GitHub...")
    subprocess.run(["git", "add", FILE_PATH])
    subprocess.run(["git", "commit", "-m", GIT_COMMIT_MSG])
    subprocess.run(["git", "push"])

def launch_debugger():
    subprocess.run(["code", FILE_PATH])  # Opens file in VS Code

def run_noizylab():
    speak("NOIZYLAB is online. Awaiting command.")
    while True:
        command = listen_for_command()
        if command:
            if "run ritual" in command or "execute capsule" in command:
                auto_save_and_run()
            elif "sync soul" in command:
                git_sync()
            elif "open debugger" in command:
                launch_debugger()
            elif "shutdown" in command:
                speak("Shutting down NOIZYLAB. Ritual complete.")
                break
            else:
                speak("Unknown command. Try again.")

if __name__ == "__main__":
    run_noizylab()
