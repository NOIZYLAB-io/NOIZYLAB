import os

search_root = "/Volumes/12TB"
search_term = "talespin"

for dirpath, dirnames, filenames in os.walk(search_root):
    # Check if "talespin" is in the folder path
    in_talespin_folder = search_term.lower() in dirpath.lower()
    for filename in filenames:
        if filename.lower().endswith(".wav"):
            # Check if "talespin" is in the filename or folder path
            if search_term.lower() in filename.lower() or in_talespin_folder:
                print(os.path.join(dirpath, filename))
