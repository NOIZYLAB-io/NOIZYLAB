import os
from pathlib import Path

KTK_REBUILDS = Path.home() / "Desktop" / "KTK_Rebuilds"

def delete_copy_files(root):
    deleted = 0
    for dirpath, dirnames, filenames in os.walk(root):
        for fname in filenames:
            if "copy" in fname.lower():
                file_path = Path(dirpath) / fname
                try:
                    file_path.unlink()
                    print(f"Deleted: {file_path}")
                    deleted += 1
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")
    print(f"\n✅ Done! {deleted} files with 'copy' in the name permanently deleted.")

if __name__ == "__main__":
    delete_copy_files(KTK_REBUILDS)