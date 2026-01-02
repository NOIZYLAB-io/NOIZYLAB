import os

BFD_PATH = "/Volumes/4TB Big Fish/BFD"

all_dirs = []
for root, dirs, files in os.walk(BFD_PATH):
    for d in dirs:
        full_path = os.path.join(root, d)
        rel_path = os.path.relpath(full_path, BFD_PATH)
        all_dirs.append(rel_path)

print(f"Found {len(all_dirs)} directories under BFD:")
for d in sorted(all_dirs):
    print(d)

with open(os.path.expanduser('~/Desktop/bfd_all_directories.txt'), 'w') as f:
    for d in sorted(all_dirs):
        f.write(d + '\n')
print("Full directory list saved to Desktop as bfd_all_directories.txt")
