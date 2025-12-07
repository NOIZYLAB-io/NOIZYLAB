import os
import shutil

SRC = "/Volumes/4TB Big Fish/BFD"
DST = "/Volumes/MAG 4TB/FXpansion"

# List all top-level BFD folders in source
src_folders = [name for name in os.listdir(SRC) if os.path.isdir(os.path.join(SRC, name))]
# List all top-level BFD folders in destination
existing_dst_folders = [name for name in os.listdir(DST) if os.path.isdir(os.path.join(DST, name))]

# Only consider BFD folders (those starting with 'BFD' or 'BFD_')
def is_bfd_folder(name):
    return name.upper().startswith('BFD')

src_bfd_folders = [f for f in src_folders if is_bfd_folder(f)]
dst_bfd_folders = [f for f in existing_dst_folders if is_bfd_folder(f)]

# Copy missing BFD folders from source to destination
for folder in src_bfd_folders:
    src_path = os.path.join(SRC, folder)
    dst_path = os.path.join(DST, folder)
    if not os.path.exists(dst_path):
        print(f"Copying: {folder}")
        shutil.copytree(src_path, dst_path)
    else:
        print(f"Already exists: {folder}")
print("Done.")
