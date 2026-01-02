import os
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Helper to create folder names with capitalized words
EXTENSION_MAP = {
    '.txt': 'Text_Files',
    '.md': 'Markdown_Files',
    '.pdf': 'PDF_Files',
    '.py': 'Python_Files',
    '.docx': 'Word_Files',
    '.csv': 'CSV_Files',
    '.jpg': 'Image_Files',
    '.jpeg': 'Image_Files',
    '.png': 'Image_Files',
    '.gif': 'Image_Files',
    '.wav': 'Audio_Files',
    '.mp3': 'Audio_Files',
    '.zip': 'Zip_Files',
    '.json': 'JSON_Files',
    '.log': 'Log_Files',
    '.save': 'Save_Files',
    '.profraw': 'Profile_Files',
    '.pimport': 'Import_Files',
    # Add more as needed
}

def get_folder_name(ext):
    return EXTENSION_MAP.get(ext, f"{ext[1:].capitalize()}_Files")

for fname in os.listdir(ROOT):
    fpath = os.path.join(ROOT, fname)
    if os.path.isfile(fpath):
        ext = os.path.splitext(fname)[1].lower()
        folder_name = get_folder_name(ext)
        target_folder = os.path.join(ROOT, folder_name)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        shutil.move(fpath, os.path.join(target_folder, fname))
        print(f"Moved {fname} to {folder_name}")

print("Done organizing files by extension.")
