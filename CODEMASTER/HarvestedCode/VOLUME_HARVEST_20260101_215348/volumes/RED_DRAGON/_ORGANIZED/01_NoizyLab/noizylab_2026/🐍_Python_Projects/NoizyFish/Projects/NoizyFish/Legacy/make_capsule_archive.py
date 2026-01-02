import shutil
import os

# Expand ~ to full path
legacy_dir = os.path.expanduser("~/NoizyFish/Legacy/")
archive_path = os.path.expanduser("~/NoizyFish/Legacy/Capsule_2025")

shutil.make_archive(archive_path, 'zip', legacy_dir)
print(f"Archive created at {archive_path}.zip")
