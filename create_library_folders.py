import os
from pathlib import Path

KTK_REBUILDS = Path.home() / "Desktop" / "KTK_Rebuilds"
NEW_LIBRARIES = Path.home() / "Desktop" / "KTK_Libraries_New"

def detect_library_names(root):
    # Library names are assumed to be the first-level subfolders in KTK_Rebuilds
    return [f.name for f in root.iterdir() if f.is_dir()]

def create_library_folders(library_names, dest_root):
    dest_root.mkdir(exist_ok=True)
    created = []
    for name in library_names:
        lib_folder = dest_root / name
        if not lib_folder.exists():
            lib_folder.mkdir()
            created.append(str(lib_folder))
    return created

if __name__ == "__main__":
    library_names = detect_library_names(KTK_REBUILDS)
    created = create_library_folders(library_names, NEW_LIBRARIES)
    print(f"✅ Created {len(created)} new library folders in {NEW_LIBRARIES}")
    for folder in created:
        print(f"  - {folder}")