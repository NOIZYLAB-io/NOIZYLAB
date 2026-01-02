import os
import shutil

try:
    import enchant
except ImportError:
    print("pyenchant is not installed. Please run 'pip install pyenchant' in your virtual environment.")
    exit(1)

header = """
╔════════════════════════════════════════════════════════╗
║           Ernest Audio Sorter - Palatino Style        ║
╚════════════════════════════════════════════════════════╝
"""

print(header)

# --- AUDIO FILE SORTING ---
base_path = "/Volumes/4TB BLK/_2025 KTK MASTER/ BLURRED EMOTIONS"
dictionary = enchant.Dict("en_US")

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

# List all .wav files in the base directory (not in SAMPLES)
for filename in os.listdir(base_path):
    if filename.lower().endswith('.wav') and os.path.isfile(os.path.join(base_path, filename)):
        base_name = os.path.splitext(filename)[0]
        corrected_name = correct_name(base_name)
        folder_path = os.path.join(base_path, corrected_name)
        os.makedirs(folder_path, exist_ok=True)
        print(f"  • Created folder: {corrected_name}")

print("\nAll audio folders created with style!\n")

# --- CODE FILE SCAN AND MOVE ---
aquarium_path = "/Users/rsp_ms/Documents/_2026_WDC/Noizyfish_Aquarium"
code_exts = ('.py', '.js', '.ts', '.json', '.ipynb', '.code-workspace')
volumes_root = "/Volumes"
exclude = {"Macintosh HD", "MacintoshHD", "Recovery", "Preboot", "VM", "Update", "com.apple.TimeMachine.localsnapshots"}

for volume in os.listdir(volumes_root):
    if volume in exclude:
        continue
    volume_path = os.path.join(volumes_root, volume)
    for root, dirs, files in os.walk(volume_path):
        # Skip system-sensitive folders
        if any(x in root for x in ["/System", "/Library", "/private", "/opt", "/cores", "/.Spotlight-V100", "/.Trashes"]):
            continue
        for file in files:
            if file.endswith(code_exts):
                src = os.path.join(root, file)
                dst = os.path.join(aquarium_path, file)
                try:
                    shutil.move(src, dst)
                    print(f"Moved: {src} -> {dst}")
                except Exception as e:
                    print(f"Error moving {src}: {e}")

print("\nScan and move complete. All code files are now in Noizyfish_Aquarium.\n")

tell application "Parallels Desktop"
    activate
    try
        open virtual machine "MightyWind"
    end try
end tell