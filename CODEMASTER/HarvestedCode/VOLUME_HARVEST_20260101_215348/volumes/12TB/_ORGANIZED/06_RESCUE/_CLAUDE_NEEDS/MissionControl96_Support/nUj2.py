import sys
import os

def select_volume(default=None):
    if len(sys.argv) > 1:
        try:
            vol = int(sys.argv[1])
            if 0 <= vol <= 100:
                print(f"Volume set to {vol}")
                return vol
            else:
                print("Please enter a number between 0 and 100.")
                return select_volume(default)
        except ValueError:
            print("Invalid input. Please enter a number.")
            return select_volume(default)
    while True:
        try:
            prompt = f"Enter volume (0-100){' [' + str(default) + ']' if default is not None else ''}: "
            inp = input(prompt)
            vol = int(inp) if inp else default
            if vol is not None and 0 <= vol <= 100:
                print(f"Volume set to {vol}")
                return vol
            else:
                print("Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def scan_directory(root_dir):
    sound_files = []
    extensions = set()
    docs = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            ext = os.path.splitext(file)[1].lower()
            extensions.add(ext)
            full_path = os.path.join(dirpath, file)
            sound_files.append(full_path)
            if file.lower().startswith(('readme', 'license', 'manual', 'doc')):
                docs.append(full_path)
    print(f"\nScanned: {root_dir}")
    print(f"Total files: {len(sound_files)}")
    print(f"Unique extensions: {sorted(list(extensions))}")
    print("Documentation files found:")
    for d in docs:
        print(f"  {d}")
    print("Sample sound files:")
    for f in sound_files[:10]:
        print(f"  {f}")
    return sound_files, extensions, docs

if __name__ == "__main__":
    print("Welcome to the NoizyFish Big Giant Fish Net!")
    vol = select_volume(default=50)
    root = input("\nEnter the root directory to scan (e.g., ./instruments): ")
    scan_directory(root) OKVendors who create a virtual instruments VST is an AU's I'm gonna take a snapshot of