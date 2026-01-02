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
    # TODO: Detect manufacturer, library, fix names, generate report, move/copy
    report_path = os.path.join(REPORTS_DIR, 'last_report.txt')
    with open(report_path, 'w') as f:
        f.write(f"Cleaned: {folder}\n")
        f.write("Removed files:\n")
        for r in removed:
            f.write(r + '\n')
    messagebox.showinfo("Perfectionist", f"Cleaning complete! Report saved to {report_path}")

if __name__ == "__main__":
    main()
