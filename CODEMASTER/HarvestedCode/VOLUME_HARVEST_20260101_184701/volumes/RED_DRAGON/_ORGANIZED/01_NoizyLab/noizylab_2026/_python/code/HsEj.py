import os

def save_script_as_txt(code_str, filename="scan_and_move_code_files.txt"):
    folder = "/Users/rsp_ms/Documents/_2026_WDC/Noizyfish_Aquarium"
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code_str)
    print(f"✅ Script saved as {file_path}")

# Example usage: save your scan and move script as a .txt file
code = '''
import os
import shutil

aquarium_folder = "/Users/rsp_ms/Documents/_2026_WDC/Noizyfish_Aquarium"
os.makedirs(aquarium_folder, exist_ok=True)
extensions = [".py", ".md", ".sh"]

def scan_and_move(root_folder):
    for dirpath, dirnames, filenames in os.walk(root_folder):
        for filename in filenames:
            ext = os.path.splitext(filename)[1].lower()
            if ext in extensions:
                src = os.path.join(dirpath, filename)
                dst = os.path.join(aquarium_folder, filename)
                if os.path.exists(dst):
                    base, ext = os.path.splitext(filename)
                    i = 1
                    while os.path.exists(os.path.join(aquarium_folder, f"{base}_{i}{ext}")):
                        i += 1
                    dst = os.path.join(aquarium_folder, f"{base}_{i}{ext}")
                shutil.move(src, dst)
                print(f"📦 Moved {filename} from {dirpath} to Noizyfish_Aquarium")

scan_and_move(os.path.expanduser("~/Documents"))
scan_and_move(os.path.expanduser("~/Desktop"))
scan_and_move("/Volumes/NoizyWind")

print("🎉 All .py, .md, and .sh files have been moved to Noizyfish_Aquarium.")
'''
save_script_as_txt(code)