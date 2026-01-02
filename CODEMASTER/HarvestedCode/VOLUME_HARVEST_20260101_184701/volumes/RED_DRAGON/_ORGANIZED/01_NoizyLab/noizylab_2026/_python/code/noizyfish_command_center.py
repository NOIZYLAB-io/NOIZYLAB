#!/usr/bin/env python3
"""
noizyfish_command_center.py
Menu-driven orchestrator for NoizyFish AI, Cha-Cha voice, and automation.
"""
import subprocess
from pathlib import Path

WORKSPACE = Path.cwd()

# --- Cha-Cha Functions ---
def talk_to_chacha():
    try:
        import speech_recognition as sr
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("🎤 Cha-Cha is listening… speak now!")
            audio = r.listen(source)
        try:
            prompt = r.recognize_google(audio)
            print(f"🗣️ You said: {prompt}")
        except sr.UnknownValueError:
            print("⚠️ Could not understand audio.")
            return
        except sr.RequestError as e:
            print("⚠️ Speech recognition service error:", e)
            return
    except ImportError:
        print("⚠️ speech_recognition module not found. Please install it or type your message.")
        prompt = input("Type your message for Cha-Cha: ")
    except Exception as e:
        print("⚠️ Microphone or audio error:", e)
        prompt = input("Type your message for Cha-Cha: ")

    # Cha-Cha replies via assistant_bridge
    try:
        from assistant_bridge import AssistantBridge
        ab = AssistantBridge(model="gpt-4o-mini", voice="Siri Voice 1")
        response = ab.ask(
            f"You are Cha-Cha. Answer in your persona. The user said: {prompt}",
            save=True,
            speak=True
        )
        print("\n--- Cha-Cha ---\n")
        print(response)
    except ImportError:
        print("⚠️ assistant_bridge module not found. Please install it for Cha-Cha AI replies.")
        print("Cha-Cha (fallback):", prompt)

def chacha_read_clipboard():
    subprocess.run(["python3", str(WORKSPACE / "read_selection_cha_cha.py")], check=True)

def chacha_read_page():
    subprocess.run(["python3", str(WORKSPACE / "read_page_cha_cha.py")], check=True)

# --- Menu ---
def menu():
    print("\n=== NoizyFish Command Center ===")
    print("10) Talk to Cha-Cha (voice or text)")
    print("11) Cha-Cha read clipboard")
    print("12) Cha-Cha read current page")
    print("0) Exit")
    return input("Choose an option (0, 10-12): ").strip()

# --- Main ---
def main():
    while True:
        choice = menu()
        if choice == "10":
            talk_to_chacha()
        elif choice == "11":
            chacha_read_clipboard()
        elif choice == "12":
            chacha_read_page()
        elif choice == "0":
            print("👋 Exiting NoizyFish Command Center.")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
