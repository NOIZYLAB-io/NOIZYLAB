import os
import shutil

BASE = '/Users/rsp_ms/Documents/Noizyfish_Aquarium/Noizy_Workspace'
EXT_MAP = {
    '.py': 'Projects/MusicApp/src/audio',
    '.jpg': 'images',
    '.jpeg': 'images',
    '.png': 'images',
    '.gif': 'images',
    '.csv': 'csv',
    '.docx': 'docx',
    '.txt': 'txt',
    '.rtf': 'rtf',
    '.wav': 'wav',
    '.ipynb': 'ipynb',
    '.md': 'MD',
    '.js': 'Projects/Website/scripts',
    '.html': 'Projects/Website/public',
    '.css': 'Projects/Website/styles',
}

# Ensure all target folders exist
for folder in set(EXT_MAP.values()):
    os.makedirs(os.path.join(BASE, folder), exist_ok=True)

def organize_by_extension():
    for root, dirs, files in os.walk(BASE):
        # Avoid moving files already in correct folders
        if any(folder in root for folder in EXT_MAP.values()):
            continue
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            if ext in EXT_MAP:
                src = os.path.join(root, f)
                dest_folder = os.path.join(BASE, EXT_MAP[ext])
                dest = os.path.join(dest_folder, f)
                if not os.path.exists(dest):
                    shutil.move(src, dest)

if __name__ == '__main__':
    organize_by_extension()
    print('Files organized by extension into appropriate folders.')
