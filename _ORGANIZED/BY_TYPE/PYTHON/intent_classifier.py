import re


def classify_intent(inp: str):
    inp = inp.lower()

    if "fix" in inp or "repair" in inp: return "repair"
    if "diagnose" in inp or "scan" in inp: return "diagnostic"
    if "help" in inp or "i'm stressed" in inp or "worried" in inp: return "comfort"
    if "story" in inp or "tell me" in inp: return "story"
    if "hype" in inp or "pump me up" in inp: return "hype"

    return "general"

