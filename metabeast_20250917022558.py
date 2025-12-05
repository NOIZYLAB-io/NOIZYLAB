def main():
    library_name = "Kirk Hunter Orchestral Collection"
    search_dir = "/Volumes"
    target_dir = "/Volumes/4TBSG/METABEAST_LIBRARIES"
    print(f"🔎 Scanning for '{library_name}' across {search_dir}...")
    grouped = find_and_group_library(library_name, search_dir)
    if not grouped:
        print(f"❌ No files found for '{library_name}'.")
        return
    print(f"📦 Moving files to {target_dir}/{library_name}...")
    move_files_to_unified_library(library_name, grouped, target_dir)
    print("✅ All files moved and organized!")
if __name__ == "__main__":
    response = input("Start Meta Beast? (yes/no): ").strip().lower()
    if response == "yes":
        main()
    else:
        print("Meta Beast not started.")
from typing import List, Dict, Optional

# --- Library Amalgamation and Organization ---
def find_and_group_library(library_name: str, search_dir: str) -> Dict[str, List[str]]:
    """
    Find all files and folders related to a specific library name across drives.
    Returns a mapping of subfolder names to file paths.
    """
    grouped = {}
    for root, dirs, files in os.walk(search_dir):
        if library_name.lower() in root.lower():
            subfolder = os.path.relpath(root, search_dir)
            grouped.setdefault(subfolder, [])
            for file in files:
                if file.lower().endswith((".wav", ".aiff")):
                    grouped[subfolder].append(os.path.join(root, file))
    return grouped

def move_files_to_unified_library(library_name: str, grouped: Dict[str, List[str]], target_dir: str):
    """
    Move all grouped files into a unified library folder, preserving subfolder structure.
    """
    for subfolder, files in grouped.items():
        dest_folder = os.path.join(target_dir, library_name, subfolder)
        os.makedirs(dest_folder, exist_ok=True)
        for file_path in files:
            dest_path = os.path.join(dest_folder, os.path.basename(file_path))
            if not os.path.exists(dest_path):
                os.rename(file_path, dest_path)
# --- Scanning and Metadata Extraction ---
def scan_local_libraries(search_dir: str, min_duration: float = 2.0) -> List["Library"]:
    """
    Scan local directories for sample libraries and extract metadata.
    """
    libraries = []
    for root, dirs, files in os.walk(search_dir):
        folder = Folder(name=os.path.basename(root))
        for file in files:
            if not file.lower().endswith((".wav", ".aiff")):
                continue
            import os
            import subprocess
            import csv
            from typing import List, Dict, Optional
            from rapidfuzz import fuzz

            # ---------- CONFIG ----------
            SEARCH_DIR = "/Volumes"   # top-level location of your sound libs
            CATALOG_FILE = "vendor_catalog.csv"  # CSV with vendor filenames + durations
            REPORT_FILE = "metabeast_report.csv"
            MIN_DURATION = 2.0  # ignore tiny files (seconds)
            # ----------------------------

            class Sample:
                def __init__(self, filename: str, duration: float, path: str, metadata: Optional[Dict] = None):
                    self.filename = filename
                    self.duration = duration
                    self.path = path
                    self.metadata = metadata or {}

            class Folder:
                def __init__(self, name: str, samples: Optional[List['Sample']] = None, subfolders: Optional[List['Folder']] = None):
                    self.name = name
                    self.samples = samples or []
                    self.subfolders = subfolders or []

            class Library:
                def __init__(self, name: str, root_folder: 'Folder', vendor: Optional[str] = None, metadata: Optional[Dict] = None):
                    self.name = name
                    self.root_folder = root_folder
                    self.vendor = vendor
                    self.metadata = metadata or {}

            def find_and_group_library(library_name: str, search_dir: str) -> Dict[str, List[str]]:
                """
                Find all files and folders related to a specific library name across drives.
                Returns a mapping of subfolder names to file paths.
                """
                grouped = {}
                for root, dirs, files in os.walk(search_dir):
                    if library_name.lower() in root.lower():
                        subfolder = os.path.relpath(root, search_dir)
                        grouped.setdefault(subfolder, [])
                        for file in files:
                            if file.lower().endswith((".wav", ".aiff")):
                                grouped[subfolder].append(os.path.join(root, file))
                return grouped

            def move_files_to_unified_library(library_name: str, grouped: Dict[str, List[str]], target_dir: str):
                """
                Move all grouped files into a unified library folder, preserving subfolder structure.
                """
                for subfolder, files in grouped.items():
                    dest_folder = os.path.join(target_dir, library_name, subfolder)
                    os.makedirs(dest_folder, exist_ok=True)
                    for file_path in files:
                        dest_path = os.path.join(dest_folder, os.path.basename(file_path))
                        if not os.path.exists(dest_path):
                            os.rename(file_path, dest_path)

            def scan_local_libraries(search_dir: str, min_duration: float = 2.0) -> List["Library"]:
                """
                Scan local directories for sample libraries and extract metadata.
                """
                libraries = []
                for root, dirs, files in os.walk(search_dir):
                    folder = Folder(name=os.path.basename(root))
                    for file in files:
                        if not file.lower().endswith((".wav", ".aiff")):
                            continue
                        filepath = os.path.join(root, file)
                        duration = get_duration(filepath)
                        if duration < min_duration:
                            continue
                        sample = Sample(filename=file, duration=duration, path=filepath)
                        folder.samples.append(sample)
                    if folder.samples:
                        lib = Library(name=folder.name, root_folder=folder)
                        libraries.append(lib)
                return libraries

            def get_duration(filepath):
                """Use ffprobe to get audio duration in seconds."""
                try:
                    result = subprocess.run(
                        ["ffprobe", "-v", "error", "-show_entries",
                         "format=duration", "-of",
                         "default=noprint_wrappers=1:nokey=1", filepath],
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True
                    )
                    return float(result.stdout.strip())
                except Exception:
                    return 0.0

            def load_catalog():
                """Load vendor catalog: expected_filename,duration"""
                catalog = {}
                if not os.path.exists(CATALOG_FILE):
                    print(f"⚠️ Catalog file '{CATALOG_FILE}' not found.")
                    return catalog
                with open(CATALOG_FILE, newline='', encoding='utf-8') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        name = row['filename'].strip().lower()
                        dur = float(row['duration'])
                        catalog[name] = dur
                return catalog

            def scan_library(catalog):
                matches, mismatches, missing = [], [], list(catalog.keys())
                for root, _, files in os.walk(SEARCH_DIR):
                    for file in files:
                        if not file.lower().endswith((".wav", ".aiff")):
                            continue
                        filepath = os.path.join(root, file)
                        duration = get_duration(filepath)
                        if duration < MIN_DURATION:
                            continue

                        fname = file.lower()
                        if fname in catalog:
                            expected = catalog[fname]
                            if abs(expected - duration) < 0.5:
                                matches.append((file, "OK", duration, filepath))
                            else:
                                mismatches.append((file, "Duration mismatch", duration, filepath))
                            if fname in missing:
                                missing.remove(fname)
                        else:
                            # try fuzzy match
                            best = max(catalog.keys(), key=lambda x: fuzz.ratio(fname, x))
                            score = fuzz.ratio(fname, best)
                            if score > 80:
                                mismatches.append((file, f"Fuzzy match {best}", duration, filepath))
                            else:
                                mismatches.append((file, "Not in catalog", duration, filepath))

                return matches, mismatches, missing

            def write_report(matches, mismatches, missing):
                with open(REPORT_FILE, "w", newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    writer.writerow(["Filename", "Status", "Duration", "Path"])
                    for row in matches + mismatches:
                        writer.writerow(row)
                    for miss in missing:
                        writer.writerow([miss, "Missing", "", ""])
                print(f"✅ Report saved to {REPORT_FILE}")

            def main():
                library_name = "Kirk Hunter Orchestral Collection"
                search_dir = "/Volumes"
                target_dir = "/Volumes/4TBSG/METABEAST_LIBRARIES"
                print(f"🔎 Scanning for '{library_name}' across {search_dir}...")
                grouped = find_and_group_library(library_name, search_dir)
                if not grouped:
                    print(f"❌ No files found for '{library_name}'.")
                    return
                print(f"📦 Moving files to {target_dir}/{library_name}...")
                move_files_to_unified_library(library_name, grouped, target_dir)
                print("✅ All files moved and organized!")

            if __name__ == "__main__":
                response = input("Start Meta Beast? (yes/no): ").strip().lower()
                if response == "yes":
                    main()
                else:
                    print("Meta Beast not started.")
