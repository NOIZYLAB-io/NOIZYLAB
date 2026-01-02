import os

base_path = "/Volumes/4TB BLK/_2025 KTK MASTER/ BLURRED EMOTIONS"

header = """
╔════════════════════════════════════════════════════════╗
║           Ernest Folder Creator - Palatino Style      ║
╚════════════════════════════════════════════════════════╝
"""

print(header)

# List all .wav files in the base directory (not in SAMPLES)
for filename in os.listdir(base_path):
    if filename.lower().endswith('.wav') and os.path.isfile(os.path.join(base_path, filename)):
        folder_name = os.path.splitext(filename)[0]
        folder_path = os.path.join(base_path, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        print(f"  • Created folder: {folder_name}")

print("\nAll folders created with style!\n")