import os
import shutil
from pathlib import Path

# -----------------------
# CONFIG: Modify as needed
# -----------------------
# Define categories (extension -> folder)
EXTENSIONS = {
    'audio': ['.wav', '.aiff', '.mp3'],
    'images': ['.png', '.jpg', '.jpeg', '.gif'],
    'scripts': ['.py', '.sh'],
    'documents': ['.txt', '.md', '.pdf'],
}

# -----------------------
# MAIN FUNCTION
# -----------------------
def organize_folder(source_path, destination_path):
    source = Path(source_path)
    destination = Path(destination_path)
    destination.mkdir(parents=True, exist_ok=True)

    # Walk through all files in source folder
    for root, dirs, files in os.walk(source):
        for file in files:
            file_path = Path(root) / file
            # Determine file category
            category_found = False
            for category, extensions in EXTENSIONS.items():
                if file_path.suffix.lower() in extensions:
                    dest_folder = destination / category
                    dest_folder.mkdir(exist_ok=True)
                    shutil.copy2(file_path, dest_folder / file_path.name)
                    category_found = True
                    break
            if not category_found:
                # Put uncategorized files in 'misc'
                dest_folder = destination / 'misc'
                dest_folder.mkdir(exist_ok=True)
                shutil.copy2(file_path, dest_folder / file_path.name)
    
    print(f"All files from {source} have been organized into {destination}")

# -----------------------
# USAGE EXAMPLE
# -----------------------
if __name__ == "__main__":
    # Ask user for source folder
    src = input("Drag or type the path of the folder you want to organize: ").strip()
    # Ask for destination folder name
    dest = input("Type the path for the cleaned-up destination folder: ").strip()

    organize_folder(src, dest)
