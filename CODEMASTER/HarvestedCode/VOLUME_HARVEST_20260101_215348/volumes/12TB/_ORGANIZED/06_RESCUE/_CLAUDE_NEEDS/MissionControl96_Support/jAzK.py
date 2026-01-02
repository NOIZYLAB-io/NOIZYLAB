import os
from pathlib import Path
from send2trash import send2trash

KTK_REBUILDS = Path.home() / "Desktop" / "KTK_Rebuilds"

def trash_copy_files(root):
    trashed = 0
    for dirpath, dirnames, filenames in os.walk(root):
        for fname in filenames:
            if "copy" in fname.lower():
                file_path = Path(dirpath) / fname
                try:
                    send2trash(str(file_path))
                    print(f"Trashed: {file_path}")
                    trashed += 1
                except Exception as e:
                    print(f"Failed to trash {file_path}: {e}")
    print(f"\n✅ Done! {trashed} files with 'copy' in the name moved to Trash.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        root_path = Path(sys.argv[1])
        if root_path.exists() and root_path.is_dir():
            trash_copy_files(root_path)
        else:
            print(f"Provided path '{root_path}' is not a valid directory.")
    else:
        trash_copy_files(KTK_REBUILDS)