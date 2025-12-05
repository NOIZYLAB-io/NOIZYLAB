def simple_text(text: str):
    """
    Converts technical explanations into ultra-simple language.
    Example:
    'Your SSD is failing' -> 'Your computer's storage part is breaking.'
    """
    replacements = {
        "SSD": "storage part",
        "CPU": "computer brain",
        "RAM": "short-term memory",
        "GPU": "graphics part",
        "network": "internet connection"
    }

    out = text
    for k, v in replacements.items():
        out = out.replace(k, v)

    return out

