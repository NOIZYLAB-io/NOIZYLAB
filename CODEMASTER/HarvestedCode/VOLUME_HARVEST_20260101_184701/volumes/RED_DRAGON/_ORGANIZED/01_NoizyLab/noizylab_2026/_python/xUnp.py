import os
import re
import csv
from datetime import datetime
from typing import List

# --- CONFIGURATION ---
FOLDER = '/Users/rsp_ms/Pictures'  # Change to your target folder
FILE_REGEX = re.compile(r'.*\.(jpg|jpeg|png|mp3|wav|mov|mp4|zip|db|pdf|docx|txt)$', re.IGNORECASE)

# --- WORDLE BEAST FEATURES ---
def get_files(folder: str, file_regex: re.Pattern) -> List[str]:
    return [f for f in os.listdir(folder) if file_regex.match(f)]

def reorder_words(filename: str, order: List[int]) -> str:
    words = re.split(r'\W+', os.path.splitext(filename)[0])
    ext = os.path.splitext(filename)[1]
    reordered = [words[i] for i in order if i < len(words)]
    return '_'.join(reordered) + ext

def find_replace(filename: str, find: str, replace: str) -> str:
    name, ext = os.path.splitext(filename)
    return name.replace(find, replace) + ext

def add_prefix_suffix(filename: str, prefix: str = '', suffix: str = '') -> str:
    name, ext = os.path.splitext(filename)
    return f'{prefix}{name}{suffix}{ext}'

def change_case(filename: str, mode: str = 'title') -> str:
    name, ext = os.path.splitext(filename)
    if mode == 'upper':
        name = name.upper()
    elif mode == 'lower':
        name = name.lower()
    elif mode == 'title':
        name = name.title()
    return name + ext

def add_date(filename: str, date_format: str = '%Y%m%d') -> str:
    name, ext = os.path.splitext(filename)
    date_str = datetime.now().strftime(date_format)
    return f'{name}_{date_str}{ext}'

def preview_changes(files: List[str], func, *args, **kwargs):
    print('Preview:')
    for f in files:
        print(f'  {f} -> {func(f, *args, **kwargs)}')

def batch_rename(folder: str, files: List[str], func, *args, **kwargs):
    for f in files:
        src = os.path.join(folder, f)
        dst = os.path.join(folder, func(f, *args, **kwargs))
        try:
            os.rename(src, dst)
            print(f'Renamed: {src} -> {dst}')
        except Exception as e:
            print(f'Error renaming {src}: {e}')

def export_to_csv(files: List[str], out_path: str):
    with open(out_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Original', 'New'])
        for f in files:
            writer.writerow([f, f])
    print(f'Exported to {out_path}')

# --- EXAMPLE USAGE ---
if __name__ == '__main__':
    files = get_files(FOLDER, FILE_REGEX)
    # Preview renaming: reorder first two words
    preview_changes(files, reorder_words, [1, 0])
    # Actually rename
    batch_rename(FOLDER, files, reorder_words, [1, 0])
    # Add prefix and date
    preview_changes(files, add_prefix_suffix, 'IMG_', '')
    preview_changes(files, add_date)
    # Export to CSV
    export_to_csv(files, os.path.join(FOLDER, 'wordle_beast_log.csv'))
    print('Wordle Beast batch renaming complete!')
