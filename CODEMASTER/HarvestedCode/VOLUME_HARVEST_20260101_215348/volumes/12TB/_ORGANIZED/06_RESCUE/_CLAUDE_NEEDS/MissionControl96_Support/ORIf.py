import os
import shutil
import yaml
from tkinter import Tk, filedialog, messagebox

# Load rules
RULES_PATH = os.path.join(os.path.dirname(__file__), 'rules.yaml')
with open(RULES_PATH, 'r') as f:
    rules = yaml.safe_load(f)

LOGS_DIR = os.path.join(os.path.dirname(__file__), 'logs')
REPORTS_DIR = os.path.join(os.path.dirname(__file__), 'reports')
os.makedirs(LOGS_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

def clean_folder(folder_path):
    # Remove unwanted files
    removed = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            ext = os.path.splitext(file)[1]
            if ext in rules['cleaning']['remove_extensions']:
                full_path = os.path.join(root, file)
                os.remove(full_path)
                removed.append(full_path)
    return removed

def main():
    root = Tk()
    root.withdraw()
    messagebox.showinfo("Perfectionist", "Select a folder to clean and organize.")
    folder = filedialog.askdirectory()
    if not folder:
        print("No folder selected.")
        return
    print(f"Selected: {folder}")
    removed = clean_folder(folder)
    # Check if any unwanted files remain
    unwanted_found = False
    for root, dirs, files in os.walk(folder):
        for file in files:
            ext = os.path.splitext(file)[1]
            if ext in rules['cleaning']['remove_extensions']:
                unwanted_found = True
                break
        if unwanted_found:
            break
    report_path = os.path.join(REPORTS_DIR, 'last_report.txt')
    with open(report_path, 'w') as f:
        f.write(f"Cleaned: {folder}\n")
        f.write("Removed files:\n")
        for r in removed:
            f.write(r + '\n')
    if not unwanted_found:
        # Move to NI_2026 on 6TB
        dest_root = "/Volumes/6TB/_NI_2026/"
        dest_path = os.path.join(dest_root, os.path.basename(folder))
        if not os.path.exists(dest_root):
            os.makedirs(dest_root)
        def get_file_count_and_size(path):
            total_files = 0
            total_size = 0
            for root, dirs, files in os.walk(path):
                for file in files:
                    total_files += 1
                    total_size += os.path.getsize(os.path.join(root, file))
            return total_files, total_size

        new_count, new_size = get_file_count_and_size(folder)
        if os.path.exists(dest_path):
            old_count, old_size = get_file_count_and_size(dest_path)
            with open(report_path, 'a') as f:
                f.write(f"\nExisting destination: {dest_path}\n")
                f.write(f"Old file count: {old_count}, Old total size: {old_size}\n")
                f.write(f"New file count: {new_count}, New total size: {new_size}\n")
            if new_count >= old_count and new_size >= old_size:
                shutil.rmtree(dest_path)
                shutil.move(folder, dest_path)
                with open(report_path, 'a') as f:
                    f.write(f"Replaced with new folder.\n")
                messagebox.showinfo("Perfectionist", f"Folder replaced with new version at {dest_path}\nReport saved to {report_path}")
            else:
                with open(report_path, 'a') as f:
                    f.write(f"New folder NOT better. Existing folder kept.\n")
                messagebox.showwarning("Perfectionist", f"New folder is not better than existing. Existing folder kept.\nReport saved to {report_path}")
        else:
            shutil.move(folder, dest_path)
            with open(report_path, 'a') as f:
                f.write(f"\nFolder moved to: {dest_path}\n")
            messagebox.showinfo("Perfectionist", f"Folder is 100% clean and has been moved to {dest_path}\nReport saved to {report_path}")
    else:
        messagebox.showinfo("Perfectionist", f"Cleaning complete! Report saved to {report_path}")

if __name__ == "__main__":
    main()
