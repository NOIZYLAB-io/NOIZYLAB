import os

try:
    import enchant
except ImportError:
    print("pyenchant is not installed. Please run 'pip install pyenchant' in your virtual environment.")
    exit(1)

base_path = "/Volumes/4TB BLK/_2025 KTK MASTER/ BLURRED EMOTIONS"
dictionary = enchant.Dict("en_US")

header = """
╔════════════════════════════════════════════════════════╗
║           Ernest Folder Creator - Palatino Style      ║
╚════════════════════════════════════════════════════════╝
"""

def correct_name(name):
    # Split camel case and underscores, then check each word
    words = []
    word = ''
    for char in name:
        if char.isupper() and word:
            words.append(word)
            word = char
        elif char == '_':
            if word:
                words.append(word)
            word = ''
        else:
            word += char
    if word:
        words.append(word)
    # Correct each word
    corrected = []
    for w in words:
        if dictionary.check(w):
            corrected.append(w)
        else:
            suggestions = dictionary.suggest(w)
            corrected.append(suggestions[0] if suggestions else w)
    return '_'.join(corrected)

print(header)

# List all .wav files in the base directory (not in SAMPLES)
for filename in os.listdir(base_path):
    if filename.lower().endswith('.wav') and os.path.isfile(os.path.join(base_path, filename)):
        base_name = os.path.splitext(filename)[0]
        corrected_name = correct_name(base_name)
        folder_path = os.path.join(base_path, corrected_name)
        os.makedirs(folder_path, exist_ok=True)
        print(f"  • Created folder: {corrected_name}")

print("\nAll folders created with style!\n")