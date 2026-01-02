#!/usr/bin/env python3
"""
voice_to_osc.py
Voice command to OSC bridge for DAW control and NGR integration.
- Listens to microphone
- Converts speech to text
- Fuzzy matches and learns user commands
- Maps natural language to OSC messages
- Sends OSC to DAW
- Remembers user custom commands
"""
import socket, struct, time, sys, json, random
from difflib import get_close_matches
from pathlib import Path

try:
    import speech_recognition as sr
except ImportError:
    print("[ERROR] speech_recognition not installed. Please run bootstrap_voice.py or install manually.")
    sys.exit(1)

PROFILE_PATH = Path.home() / ".ngr_voice_profile.json"

# --- OSC helpers ---
def osc_pack_string(s: str) -> bytes:
    b = s.encode("utf-8") + b'\x00'
    pad = (4 - (len(b) % 4)) % 4
    return b + (b'\x00' * pad)

def osc_message(addr: str, arguments: list) -> bytes:
    types = ','
    payload = b''
    for a in arguments:
        if isinstance(a, str):
            types += 's'; payload += osc_pack_string(a)
        elif isinstance(a, float):
            types += 'f'; payload += struct.pack('>f', a)
        elif isinstance(a, int):
            types += 'i'; payload += struct.pack('>i', a)
        else:
            raise ValueError("Unsupported OSC arg type")
    return osc_pack_string(addr) + osc_pack_string(types) + payload

# --- Default command mapping ---
DEFAULT_COMMANDS = {
    'mute track one': ('/mute', ['Track1', 1]),
    'unmute track one': ('/mute', ['Track1', 0]),
    'gain up track one': ('/gain', ['Track1', 1.5]),
    'gain down track one': ('/gain', ['Track1', 0.5]),
    'join room test': ('/join', ['Test', 'User']),
    'leave room test': ('/leave', ['Test', 'User']),
    'solo track one': ('/solo', ['Track1', 1]),
    'unsolo track one': ('/solo', ['Track1', 0]),
    'eq boost highs': ('/eq', ['Track1', 'high', 3]),
    'eq cut lows': ('/eq', ['Track1', 'low', -3]),
    # Add more mappings as needed
}

# --- Load and save user profile ---
def load_profile():
    if PROFILE_PATH.exists():
        with open(PROFILE_PATH, "r") as f:
            return json.load(f)
    return {}

def save_profile(profile):
    with open(PROFILE_PATH, "w") as f:
        json.dump(profile, f, indent=2)

# --- Voice to OSC loop ---
UNRECOGNIZED_RESPONSES = [
    "Hmm, I didn't catch that. Want to try again?",
    "Sorry, I couldn't match your command. Maybe rephrase?",
    "I'm still learning! Would you like to teach me this command?",
    "That one slipped by me. Can you say it differently?",
    "Not sure what you meant. Let's try another way!"
]

MISUNDERSTOOD_RESPONSES = [
    "Oops, I couldn't understand you. Please speak a bit clearer.",
    "Sorry, I missed that. Could you repeat?",
    "Didn't get that one. Let's try again.",
    "Can you say that one more time?",
    "I didn't quite hear you. Please try again."
]

def voice_to_osc(osc_host: str, osc_port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    profile = load_profile()
    commands = {**DEFAULT_COMMANDS, **profile.get("custom_commands", {})}
    print("👋 Welcome to NGR Voice Control! Speak naturally and I'll do my best to help you.")
    fail_count = 0
    while True:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            print("🎤 Ready for your command:")
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio).lower()
            print(f"🗣️ I heard: \"{text}\"")
            match = None
            if text in commands:
                match = text
                fail_count = 0
            else:
                close = get_close_matches(text, commands.keys(), n=1, cutoff=0.7)
                if close:
                    match = close[0]
                    print(f"🤔 I think you meant: \"{match}\"")
            if match:
                addr, arguments = commands[match]
                msg = osc_message(addr, arguments)
                sock.sendto(msg, (osc_host, osc_port))
                print(f"✅ Sent OSC: {addr} {arguments} to {osc_host}:{osc_port}")
                print("👍 Let me know if you need anything else!")
            else:
                fail_count += 1
                print(random.choice(UNRECOGNIZED_RESPONSES))
                if fail_count >= 3:
                    print("Would you like to teach me this command? (y/n)")
                    ans = input().strip().lower()
                    if ans == 'y':
                        print("🔧 Enter OSC address (e.g. /mute):")
                        addr = input().strip()
                        print("🔧 Enter OSC arguments as comma-separated values (e.g. Track1,1):")
                        argstr = input().strip()
                        arguments = [a if not a.isdigit() else int(a) for a in argstr.split(",")]
                        profile.setdefault("custom_commands", {})[text] = [addr, arguments]
                        save_profile(profile)
                        print(f"🎉 Learned new command: \"{text}\" -> {addr} {arguments}")
                        commands = {**DEFAULT_COMMANDS, **profile.get('custom_commands', {})}
                        fail_count = 0
        except sr.UnknownValueError:
            print(random.choice(MISUNDERSTOOD_RESPONSES))
        except sr.RequestError as e:
            print(f"⚠️ Recognition error: {e}")
        time.sleep(0.5)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Voice to OSC for DAW control")
    parser.add_argument('--osc_host', type=str, default='127.0.0.1', help='OSC target host')
    parser.add_argument('--osc_port', type=int, default=9000, help='OSC target port')
    args = parser.parse_args()
    voice_to_osc(args.osc_host, args.osc_port)