import os
import shutil

SOURCE_FOLDER = "/Users/rsp_ms/WORK_OF_TODAY"  # Update as needed
DEST_FOLDER = "/Users/rsp_ms/MainProject"      # Update as needed

def request_move():
    files = os.listdir(SOURCE_FOLDER)
    print(f"Found {len(files)} files in WORK OF TODAY:")
    for f in files:
        print(f"  - {f}")
    approve = input("Move all files to Main Project folder? (yes/no): ").strip().lower()
    if approve == "yes":
        for f in files:
            shutil.move(os.path.join(SOURCE_FOLDER, f), os.path.join(DEST_FOLDER, f))
        print("Files moved successfully.")
    else:
        print("Move cancelled.")

if __name__ == "__main__":
    request_move()
