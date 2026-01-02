#!/usr/bin/env python3
"""
voice_to_osc.py
Voice command to OSC bridge for DAW control and NGR integration.
- Listens to microphone
- Converts speech to text
- Maps natural language to OSC messages
- Sends OSC to DAW
"""
import socket, struct, time, sys
from pathlib import Path

try:
    import speech_recognition as sr
except ImportError:
    print("[ERROR] speech_recognition not installed. Please run bootstrap_voice.py or install manually.")
    sys.exit(1)
try:
    import sounddevice as sd
    import numpy as np
except ImportError:
    print("[ERROR] sounddevice or numpy not installed. Please run bootstrap_voice.py or install manually.")
    sys.exit(1)

# --- OSC helpers ---
def osc_pack_string(s: str) -> bytes:
    b = s.encode("utf-8") + b'\x00'
    pad = (4 - (len(b) % 4)) % 4
    return b + (b'\x00' * pad)

def osc_message(addr: str, args: list) -> bytes:
    types = ','
    payload = b''
    for a in args:
        if isinstance(a, str):
            types += 's'; payload += osc_pack_string(a)
        elif isinstance(a, float):
            types += 'f'; payload += struct.pack('>f', a)
        elif isinstance(a, int):
            types += 'i'; payload += struct.pack('>i', a)
        else:
            raise ValueError("Unsupported OSC arg type")
    return osc_pack_string(addr) + osc_pack_string(types) + payload

# --- Command mapping ---
COMMANDS = {
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

# --- Voice to OSC loop ---
def voice_to_osc(osc_host: str, osc_port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print(f"[VOICE-OSC] Listening for voice commands. Speak clearly...")
    while True:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Say a command:")
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio).lower()
            print(f"[VOICE] Recognized: {text}")
            if text in COMMANDS:
                addr, args = COMMANDS[text]
                msg = osc_message(addr, args)
                sock.sendto(msg, (osc_host, osc_port))
                print(f"[OSC] Sent {addr} {args} to {osc_host}:{osc_port}")
            else:
                print(f"[VOICE] Command not recognized. Try again.")
        except sr.UnknownValueError:
            print("[VOICE] Could not understand audio.")
        except sr.RequestError as e:
            print(f"[VOICE] Recognition error: {e}")
        time.sleep(0.5)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Voice to OSC for DAW control")
    parser.add_argument('--osc_host', type=str, default='127.0.0.1', help='OSC target host')
    parser.add_argument('--osc_port', type=int, default=9000, help='OSC target port')
    args = parser.parse_args()
    voice_to_osc(args.osc_host, args.osc_port)
