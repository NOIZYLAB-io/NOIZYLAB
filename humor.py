"""NoizyMeme++ Humor Engine"""
import random

JOKES = ["Why do programmers prefer dark mode? Because light attracts bugs!", "I told my computer I needed a break, it said 'Ctrl+C'", "There are 10 types of people: those who understand binary and those who don't", "A SQL query walks into a bar, walks up to two tables and asks 'Can I join you?'"]

def generate_humor(context=None):
    return random.choice(JOKES)

def get_comedic_timing(emotion, energy):
    if energy > 0.7: return "quick_wit"
    if emotion == "stressed": return "gentle_humor"
    return "balanced"

def rob_mode_response(input_text):
    return f"Alright Rob, {input_text}... but let's be real, we both know you're gonna do it YOUR way anyway! 😎"

