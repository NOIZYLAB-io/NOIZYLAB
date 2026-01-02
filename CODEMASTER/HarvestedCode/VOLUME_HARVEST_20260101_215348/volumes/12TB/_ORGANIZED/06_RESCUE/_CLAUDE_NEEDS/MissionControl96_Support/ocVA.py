
import os
import shutil
import yaml
from tkinter import Tk, filedialog, messagebox
import datetime

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

def validate_structure(folder_path):
    """Check for required subfolders/files as defined in rules.yaml."""
    required = rules.get('required_structure', [])
    missing = []
    for rel_path in required:
        abs_path = os.path.join(folder_path, rel_path)
        if not os.path.exists(abs_path):
            missing.append(rel_path)
    return missing

def generate_html_report(folder, removed, missing, dest_path, action, old_count=None, old_size=None, new_count=None, new_size=None):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Find artwork
    artwork_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower() in ["cover.jpg", "artwork.jpg", "artwork.png", "folder.jpg", "cover.png", "artwork.jpeg", "cover.jpeg"]:
                artwork_files.append(os.path.join(root, file))
    html = f"""
    <html><head><title>Perfectionist Report</title></head><body>
    <h2>Perfectionist Cleaning Report</h2>
    <b>Date:</b> {now}<br>
    <b>Processed Folder:</b> {folder}<br>
    <b>Action:</b> {action}<br>
    <b>Destination:</b> {dest_path or 'N/A'}<br>
    <hr>
    <h3>Removed Files</h3>
    <ul>{''.join(f'<li>{r}</li>' for r in removed)}</ul>
    """
    if artwork_files:
        html += f"<h3>Artwork Found</h3>"
        for art in artwork_files:
            rel = os.path.relpath(art, os.path.dirname(__file__))
            html += f'<img src="file://{art}" alt="Artwork" style="max-width:300px;max-height:300px;"><br>{art}<br>'
    if missing:
        html += f"<h3 style='color:red'>Missing Required Structure</h3><ul>{''.join(f'<li>{m}</li>' for m in missing)}</ul>"
    if old_count is not None and new_count is not None:
        html += f"<h3>Quality Comparison</h3>"
        html += f"Old file count: {old_count}, Old total size: {old_size}<br>"
        html += f"New file count: {new_count}, New total size: {new_size}<br>"
    html += "</body></html>"
    report_path = os.path.join(REPORTS_DIR, f'report_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.html')
    with open(report_path, 'w') as f:
        f.write(html)
    return report_path

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
    missing = validate_structure(folder)
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
    dest_root = "/Volumes/6TB/_NI_2026/"
    dest_path = os.path.join(dest_root, os.path.basename(folder))
    def get_file_count_and_size(path):
        total_files = 0
        total_size = 0
        for root, dirs, files in os.walk(path):
            for file in files:
                total_files += 1
                total_size += os.path.getsize(os.path.join(root, file))
        return total_files, total_size

    new_count, new_size = get_file_count_and_size(folder)
    action = ""
    old_count = old_size = None
    if not unwanted_found and not missing:
        if not os.path.exists(dest_root):
            os.makedirs(dest_root)
        if os.path.exists(dest_path):
            old_count, old_size = get_file_count_and_size(dest_path)
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
    report_path = generate_html_report(folder, removed, missing, dest_path, action, old_count, old_size, new_count, new_size)

if __name__ == "__main__":
    main()
