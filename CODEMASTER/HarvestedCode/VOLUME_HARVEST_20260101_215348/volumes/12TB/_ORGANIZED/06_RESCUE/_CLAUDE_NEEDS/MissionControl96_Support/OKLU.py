import os

def check_volume(volume_path, expected_dirs):
    print(f"\n--- Checking: {volume_path} ---")
    missing = []
    for d in expected_dirs:
        if not os.path.exists(os.path.join(volume_path, d)):
            missing.append(d)
    print(f"Missing directories: {missing if missing else 'None'}")
    total_files = 0
    total_dirs = 0
    for root, dirs, files in os.walk(volume_path):
        total_files += len(files)
        total_dirs += len(dirs)
    print(f"Total files: {total_files}")
    print(f"Total directories: {total_dirs}")
    print("Quick shine complete.\n")

if __name__ == "__main__":
    system_dirs = [
        "etc", "bin", "sbin", "usr", "var", "opt", "private", "System", "Library", "Users", "Applications"
    ]
    user_dirs = [
        "Desktop", "Documents", "Downloads", "Library", "Movies", "Music", "Pictures", "Public"
    ]
    check_volume("/Volumes/DaFixer", system_dirs)
    check_volume("/Volumes/rsp_13", user_dirs)