import os
import shutil
import re

# Source directory to organize
source_dir = "/Volumes/12TB/Wave"

# Destination directory for organized files
organized_dir = os.path.join(source_dir, "Organized")
os.makedirs(organized_dir, exist_ok=True)

def get_group_name(filename):
    # Use the part before the first dot, space, or underscore as the group name
    match = re.match(r"([^. _-]+)", filename)
    group = match.group(1) if match else "Other"
    # Make 'CDCK' lowercase and fix 'ImpaCT' to 'impact'
    group = group.replace('CDCK', 'cdck').replace('ImpaCT', 'impact')
    return group

for fname in os.listdir(source_dir):
    fpath = os.path.join(source_dir, fname)
    if os.path.isfile(fpath):
        group = get_group_name(fname)
        group_folder = os.path.join(organized_dir, group)
        os.makedirs(group_folder, exist_ok=True)
        shutil.move(fpath, os.path.join(group_folder, fname))

print(f"Files organized in: {organized_dir}")
