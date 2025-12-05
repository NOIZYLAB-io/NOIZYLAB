"""FrontDesk: Voice Handler"""
from datetime import datetime

CALLS = {}
GREETINGS = {
    "morning": "Good morning! Thank you for calling NoizyLab. I'm Noizy, your AI assistant.",
    "afternoon": "Good afternoon! Thank you for calling NoizyLab. I'm Noizy, your AI assistant.",
    "evening": "Good evening! Thank you for calling NoizyLab. I'm Noizy, your AI assistant.",
}

def respond(message, context=None):
    """Generate response to customer message"""
    msg = message.lower()
    if any(w in msg for w in ["book", "schedule", "appointment"]): return {"intent": "booking", "response": "I'd be happy to help you book! What device needs service?"}
    if any(w in msg for w in ["price", "cost", "how much"]): return {"intent": "pricing", "response": "Our diagnostics start at $50. Can you tell me about your device?"}
    if any(w in msg for w in ["help", "problem", "broken"]): return {"intent": "support", "response": "I'm sorry to hear that! What device and what's the issue?"}
    if any(w in msg for w in ["hours", "open", "location"]): return {"intent": "info", "response": "We're open Mon-Fri 9-5, Sat 10-2. We offer in-home and remote support!"}
    return {"intent": "general", "response": "Thanks for reaching out! How can I help you today?"}

def handle_call(caller_id, caller_number=None):
    """Handle incoming call"""
    hour = datetime.now().hour
    greeting = GREETINGS["morning"] if hour < 12 else GREETINGS["afternoon"] if hour < 17 else GREETINGS["evening"]
    call = {"id": caller_id, "number": caller_number, "started": datetime.now().isoformat(), "transcript": [{"speaker": "ai", "text": greeting}]}
    CALLS[caller_id] = call
    return {"call_id": caller_id, "greeting": greeting}

def add_to_transcript(call_id, speaker, text):
    if call_id in CALLS: CALLS[call_id]["transcript"].append({"speaker": speaker, "text": text, "time": datetime.now().isoformat()})

