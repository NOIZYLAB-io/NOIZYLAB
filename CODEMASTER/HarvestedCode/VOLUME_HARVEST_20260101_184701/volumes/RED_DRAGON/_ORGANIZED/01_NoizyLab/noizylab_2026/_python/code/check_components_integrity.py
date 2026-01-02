import os
import subprocess
import shutil

COMPONENTS_DIR = '/Library/Audio/Plug-Ins/Components'
report = []

for item in os.listdir(COMPONENTS_DIR):
    path = os.path.join(COMPONENTS_DIR, item)
    if os.path.isdir(path):
        # Check main binary inside .component bundle
        binary_path = os.path.join(path, 'Contents', 'MacOS')
        if os.path.exists(binary_path):
            for binary in os.listdir(binary_path):
                bin_file = os.path.join(binary_path, binary)
                try:
                    result = subprocess.run(['codesign', '--verify', '--verbose=2', bin_file], capture_output=True, text=True)
                    if result.returncode == 0:
                        status = 'OK'
                    else:
                        status = f'ERROR: {result.stderr.strip()}'
                except Exception as e:
                    status = f'EXCEPTION: {e}'
                report.append((item, bin_file, status))
        else:
            report.append((item, 'NO_BINARY_FOUND', 'SKIPPED'))

# Save report
with open('/Volumes/4TBSG/2025_NOIZYFISH/Python_Codes/components_integrity_report.txt', 'w') as f:
    for item, bin_file, status in report:
        f.write(f'{item}: {bin_file}: {status}\n')

print('Component file integrity check complete. See components_integrity_report.txt for details.')

def narrate(text):
    subprocess.run(["say", "-v", "Siri_British_Female", text])  # Replace with the exact Siri voice name

response = "This is an OpenAI response narrated with British Siri Female 1."
narrate(response)

# Step 1: Set up your workspace folder
workspace_folder = "MyWebadorSite"
if not os.path.exists(workspace_folder):
    os.makedirs(workspace_folder)
print(f"Workspace folder created: {workspace_folder}")

# Step 2: Move downloaded files into workspace
# Manually download your site files (HTML, CSS, JS, images) and place them in a folder called 'Downloaded_Webador'
downloaded_folder = "Downloaded_Webador"
# Example: Move all files from 'Downloaded_Webador' to 'MyWebadorSite'
if os.path.exists(downloaded_folder):
    for fname in os.listdir(downloaded_folder):
        src = os.path.join(downloaded_folder, fname)
        dst = os.path.join(workspace_folder, fname)
        shutil.move(src, dst)
    print(f"Moved files from {downloaded_folder} to {workspace_folder}")
else:
    print(f"Please download your site files and place them in the '{downloaded_folder}' folder.")

# Step 3: Organize assets (optional)
# You can create subfolders for images, CSS, JS, etc.
assets = {
    "images": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "css": [".css"],
    "js": [".js"]
}
for subfolder, exts in assets.items():
    subfolder_path = os.path.join(workspace_folder, subfolder)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    for fname in os.listdir(workspace_folder):
        if any(fname.lower().endswith(ext) for ext in exts):
            shutil.move(os.path.join(workspace_folder, fname), os.path.join(subfolder_path, fname))
    print(f"Organized {subfolder} files.")

# Step 4: Open workspace in VS Code
print("Open the 'MyWebadorSite' folder in VS Code to start editing your website.")

# Step 5: (Optional) Install Live Server extension in VS Code for preview
print("Tip: Install the 'Live Server' extension in VS Code for real-time preview of your site.")

# Step 6: Edit, enhance, and automate!
print("You can now edit HTML, CSS, JS, and assets. Add new features, optimize code, and integrate AI or automation as needed.")
