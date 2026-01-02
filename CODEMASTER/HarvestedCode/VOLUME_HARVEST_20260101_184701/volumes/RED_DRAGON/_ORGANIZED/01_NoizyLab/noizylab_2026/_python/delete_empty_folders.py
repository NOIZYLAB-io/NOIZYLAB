import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def delete_empty_dirs(root):
    for dirpath, dirnames, filenames in os.walk(root, topdown=False):
        # Skip the root folder itself
        if dirpath == root:
            continue
        if not dirnames and not filenames:
            try:
                os.rmdir(dirpath)
                print(f"Deleted empty folder: {dirpath}")
            except Exception as e:
                print(f"Failed to delete {dirpath}: {e}")

if __name__ == "__main__":
    delete_empty_dirs(ROOT)
    print("Done deleting empty folders.")
