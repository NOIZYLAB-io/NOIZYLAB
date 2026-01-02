import os
import re
import threading
from datetime import datetime

# Configuration: List of folders to process
FOLDERS = [
    # Add absolute paths to folders you want to rename files in
    '/Users/rsp_ms/Pictures',
    '/Users/rsp_ms/Music',
    # ...add more as needed
]

# Naming pattern: customize as needed
# Example: 'IMG_{date}_{num:03d}{ext}'
NAMING_PATTERN = 'FILE_{date}_{num:03d}{ext}'

# File filter: regex for file types (e.g., images, audio)
FILE_REGEX = re.compile(r'.*\.(jpg|jpeg|png|mp3|wav|mov|mp4|zip|db)$', re.IGNORECASE)

# Thread worker for each folder
def rename_files_in_folder(folder, pattern, file_regex):
    files = [f for f in os.listdir(folder) if file_regex.match(f)]
    date_str = datetime.now().strftime('%Y%m%d')
    for idx, filename in enumerate(files, 1):
        ext = os.path.splitext(filename)[1]
        new_name = pattern.format(date=date_str, num=idx, ext=ext)
        src = os.path.join(folder, filename)
        dst = os.path.join(folder, new_name)
        try:
            os.rename(src, dst)
            print(f'Renamed: {src} -> {dst}')
        except Exception as e:
            print(f'Error renaming {src}: {e}')

# Launch threads for parallel renaming
threads = []
for folder in FOLDERS:
    if os.path.exists(folder):
        t = threading.Thread(target=rename_files_in_folder, args=(folder, NAMING_PATTERN, FILE_REGEX))
        t.start()
        threads.append(t)
    else:
        print(f'Folder not found: {folder}')

for t in threads:
    t.join()

print('Batch renaming complete!')
