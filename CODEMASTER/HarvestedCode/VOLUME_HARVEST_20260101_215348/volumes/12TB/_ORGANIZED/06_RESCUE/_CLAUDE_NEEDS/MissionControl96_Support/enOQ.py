import os
import sys
from core.cleaner import PerfectionistCleaner
from core.utils import timestamp, ensure_dir

RULES_PATH = os.path.join(os.path.dirname(__file__), '../core/rules.yaml')
REPORTS_DIR = os.path.join(os.path.dirname(__file__), '../reports')
LOGS_DIR = os.path.join(os.path.dirname(__file__), '../logs')
ensure_dir(REPORTS_DIR)
ensure_dir(LOGS_DIR)

def main():
    if len(sys.argv) < 2:
        print("Usage: perfectionist_cli.py <parent_folder>")
        sys.exit(1)
    folders = sys.argv[1]
    if not os.path.exists(folders):
        print("No folder found.")
        sys.exit(1)
    subfolders = [os.path.join(folders, d) for d in os.listdir(folders) if os.path.isdir(os.path.join(folders, d))][:10]
    if not subfolders:
        print("No subfolders found.")
        sys.exit(1)
    cleaner = PerfectionistCleaner(RULES_PATH)
    for folder in subfolders:
        removed = cleaner.clean_folder(folder)
        missing = cleaner.validate_structure(folder)
        unwanted_found = False
        for root_dir, dirs, files in os.walk(folder):
            for file in files:
                ext = os.path.splitext(file)[1]
                if ext in cleaner.rules['cleaning']['remove_extensions']:
                    unwanted_found = True
                    break
            if unwanted_found:
                break
        dest_root = "/Volumes/6TB/_NI_2026/"
        dest_path = os.path.join(dest_root, os.path.basename(folder))
        new_count, new_size = cleaner.get_file_count_and_size(folder)
        action = ""
        old_count = old_size = None
        if not unwanted_found and not missing:
            if not os.path.exists(dest_root):
                os.makedirs(dest_root)
            if os.path.exists(dest_path):
                old_count, old_size = cleaner.get_file_count_and_size(dest_path)
                if new_count >= old_count and new_size >= old_size:
                    shutil.rmtree(dest_path)
                    shutil.move(folder, dest_path)
                    action = f"Replaced existing folder with new version at {dest_path}"
                else:
                    action = f"New folder NOT better. Existing folder kept at {dest_path}"
            else:
                shutil.move(folder, dest_path)
                action = f"Folder moved to: {dest_path}"
        else:
            action = "Cleaning complete, but issues found. Folder not moved."
        # Report generation would go here

if __name__ == "__main__":
    main()
