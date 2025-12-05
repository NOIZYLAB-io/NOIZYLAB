import os

# ✅ Your true master folder
projects_folder = r"/Users/rsp_ms/Documents/THE_NEW_WORLD/_2025 PROJECTS/MusicMaster"

# Define the folder structure with instructions for README files
structure = {
    "Originals": "Drop raw master audio files here (WAV/AIFF, uncompressed).",
    "CoverArt": "Store album/single artwork here (JPG or PNG).",
    "Metadata": "Keep your master metadata sheet here (Excel/CSV/Google Sheets export).",
    "Exports": {
        "SoundCloud": "Platform-ready MP3s + metadata for SoundCloud uploads.",
        "Bandcamp": "Platform-ready FLACs + metadata for Bandcamp uploads.",
        "Spotify": "Platform-ready WAVs + metadata for Spotify distributors.",
        "AppleMusic": "Platform-ready WAVs + metadata for Apple Music distributors."
    }
}

def create_structure(base_path, struct):
    for folder, subfolders in struct.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)

        # If subfolders is a dict, recurse deeper
        if isinstance(subfolders, dict):
            create_structure(folder_path, subfolders)
        else:
            # If subfolders is a string, it's a README instruction
            readme_path = os.path.join(folder_path, "README.txt")
            if not os.path.exists(readme_path):
                with open(readme_path, "w") as f:
                    f.write(subfolders)

def print_tree(startpath, prefix=""):
    """Prints a folder tree view in the terminal."""
    items = sorted(os.listdir(startpath))
    for i, item in enumerate(items):
        path = os.path.join(startpath, item)
        connector = "└── " if i == len(items) - 1 else "├── "
        print(prefix + connector + item)
        if os.path.isdir(path):
            extension = "    " if i == len(items) - 1 else "│   "
            print_tree(path, prefix + extension)

# Create the hierarchy
create_structure(projects_folder, structure)

print(f"\n✅ Folder hierarchy ensured in: {projects_folder}\n")
print("Here’s what it looks like:\n")
print_tree(projects_folder)
