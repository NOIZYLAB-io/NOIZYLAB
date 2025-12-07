def clean_voice_input(text: str):
    text = text.lower()
    text = text.replace("umm", "")
    text = text.replace("uhhh", "")
    text = text.strip()
    return text

