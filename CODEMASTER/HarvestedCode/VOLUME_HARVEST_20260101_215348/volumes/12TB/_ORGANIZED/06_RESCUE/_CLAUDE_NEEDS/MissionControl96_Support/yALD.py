import os

BFD_PATH = "/Volumes/4TB Big Fish/BFD"

# List all top-level folders in BFD
folders = [name for name in os.listdir(BFD_PATH) if os.path.isdir(os.path.join(BFD_PATH, name))]

print("Top-level BFD folders:")
for folder in sorted(folders):
    print(folder)
