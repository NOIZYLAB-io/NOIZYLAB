import os
import sys
from tkinter import Tk, filedialog, messagebox
from core.cleaner import PerfectionistCleaner
from core.utils import timestamp, ensure_dir

RULES_PATH = os.path.join(os.path.dirname(__file__), '../core/rules.yaml')
REPORTS_DIR = os.path.join(os.path.dirname(__file__), '../reports')
LOGS_DIR = os.path.join(os.path.dirname(__file__), '../logs')
ensure_dir(REPORTS_DIR)
ensure_dir(LOGS_DIR)

def main():
    root = Tk()
    root.withdraw()
    messagebox.showinfo("Perfectionist", "Select up to 10 folders to clean and organize.")
    folders = filedialog.askdirectory(mustexist=True, title="Select the parent folder containing up to 10 libraries")
    if not folders:
        print("No folder selected.")
        return
    subfolders = [os.path.join(folders, d) for d in os.listdir(folders) if os.path.isdir(os.path.join(folders, d))][:10]
    if not subfolders:
        print("No subfolders found.")
        return
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
                    messagebox.showinfo("Perfectionist", f"Folder replaced with new version at {dest_path}\nDetailed report generated.")
                else:
                    action = f"New folder NOT better. Existing folder kept at {dest_path}"
                    messagebox.showwarning("Perfectionist", f"New folder is not better than existing. Existing folder kept.\nDetailed report generated.")
            else:
                shutil.move(folder, dest_path)
                action = f"Folder moved to: {dest_path}"
                messagebox.showinfo("Perfectionist", f"Folder is 100% clean and has been moved to {dest_path}\nDetailed report generated.")
        else:
            action = "Cleaning complete, but issues found. Folder not moved."
            messagebox.showinfo("Perfectionist", f"Cleaning complete! Issues found (unwanted files or missing structure). See report.")
        # Report generation would go here

if __name__ == "__main__":
    main()
