"""NoizySynth Audio Generator"""
import base64
import struct
import math

def generate_audio(prompt):
    # Generate simple tone based on prompt
    sample_rate = 44100
    duration = 1.0
    freq = 440 if "alert" in prompt.lower() else 220
    samples = int(sample_rate * duration)
    audio_data = bytes()
    for i in range(samples):
        value = int(32767 * 0.3 * math.sin(2 * math.pi * freq * i / sample_rate))
        audio_data += struct.pack('<h', value)
    return base64.b64encode(audio_data).decode()

def generate_ambient(prompt):
    return generate_audio(prompt)

def generate_alert(prompt):
    return generate_audio("alert " + prompt)

