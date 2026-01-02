import os
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 1. Move any remaining loose files into an 'OTHER_FILES' folder
other_folder = os.path.join(ROOT, 'OTHER_FILES')
if not os.path.exists(other_folder):
    os.makedirs(other_folder)

for fname in os.listdir(ROOT):
    fpath = os.path.join(ROOT, fname)
    if os.path.isfile(fpath):
        shutil.move(fpath, os.path.join(other_folder, fname))
        print(f"Moved {fname} to OTHER_FILES")

# 2. Delete any empty folders (except root)
def delete_empty_dirs(root):
    for dirpath, dirnames, filenames in os.walk(root, topdown=False):
        if dirpath == root:
            continue
        if not dirnames and not filenames:
            try:
                os.rmdir(dirpath)
                print(f"Deleted empty folder: {dirpath}")
            except Exception as e:
                print(f"Failed to delete {dirpath}: {e}")

delete_empty_dirs(ROOT)

print("Final cleanup complete.")
