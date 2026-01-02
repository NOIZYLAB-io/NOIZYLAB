import os

for dirpath, dirnames, filenames in os.walk("/"):
    for filename in filenames:
        if filename.endswith(".py"):
            print(os.path.join(dirpath, filename))