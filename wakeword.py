import re

WAKEWORD = "noizy"


def detect_wakeword(text: str):
    text = text.lower().strip()
    if WAKEWORD in text:
        return True
    return False

