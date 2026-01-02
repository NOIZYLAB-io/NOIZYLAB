import os
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

EXTENSION_MAP = {
    '.txt': 'TEXT_FILES',
    '.md': 'MARKDOWN_FILES',
    '.pdf': 'PDF_FILES',
    '.py': 'PYTHON_FILES',
    '.docx': 'WORD_FILES',
    '.csv': 'CSV_FILES',
    '.jpg': 'IMAGE_FILES',
    '.jpeg': 'IMAGE_FILES',
    '.png': 'IMAGE_FILES',
    '.gif': 'IMAGE_FILES',
    '.wav': 'AUDIO_FILES',
    '.mp3': 'AUDIO_FILES',
    '.zip': 'ZIP_FILES',
    '.json': 'JSON_FILES',
    '.log': 'LOG_FILES',
    '.save': 'SAVE_FILES',
    '.profraw': 'PROFILE_FILES',
    '.pimport': 'IMPORT_FILES',
    # Add more as needed
}

def get_folder_name(ext):
    return EXTENSION_MAP.get(ext, f"{ext[1:].upper()}_FILES")

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

print("Done organizing files by extension with uppercase folder names.")
