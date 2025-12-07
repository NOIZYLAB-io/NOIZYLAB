def detect_distress(text: str):
    triggers = ["scared", "panic", "help me", "i'm afraid", "i'm stuck"]
    if any(t in text.lower() for t in triggers):
        return True
    return False


def respond_to_distress():
    return (
        "It's okay. I hear you. I'm right here with you. "
        "You're safe. Let's solve this together, step by step."
    )

