import os
import shutil

# Path to main NoizyFish folder
desktop_noizyfish = os.path.expanduser("~/Desktop/NoizyFish")

# List to store found items
found = []

# Walk all volumes (root '/')
for root, dirs, files in os.walk("/"):
    # Skip the Desktop/NoizyFish folder
    if desktop_noizyfish in root:
        continue
    for name in dirs + files:
        if "noizyfish" in name.lower():
            full_path = os.path.join(root, name)
            found.append(full_path)

# Print and optionally move found items
if found:
    print("Found items named 'noizyfish' outside Desktop/NoizyFish:")
    for item in found:
        print(item)
        # Uncomment the next two lines to move items automatically
        # dest = os.path.join(desktop_noizyfish, os.path.basename(item))
        # shutil.move(item, dest)
else:
    print("No items named 'noizyfish' found outside Desktop/NoizyFish.")
