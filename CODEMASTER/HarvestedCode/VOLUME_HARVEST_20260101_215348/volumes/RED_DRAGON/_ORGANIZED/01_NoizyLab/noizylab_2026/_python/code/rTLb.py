import os
from pathlib import Path

# Folders to scan (Mission Control Drum Core)
FOLDERS = [
    "/Library/Application Support/EZDrummer",
    "/Library/Application Support/Superior Drummer",
    "/Library/Application Support/Toontrack",
    "/Library/Application Support/XLN Audio",
    "/Library/Application Support/FXpansion",
    "/Library/Application Support/Logic"
]

def check_file_integrity(file_path: Path):
    problems = []
    if not file_path.exists():
        problems.append("Missing")
    elif not file_path.is_file():
        problems.append("Not a file")
    elif file_path.stat().st_size == 0:
        problems.append("Zero-byte file")
    else:
        try:
            with open(file_path, "rb") as f:
                f.read(1)  # Try to read first byte
        except Exception as e:
            problems.append(f"Unreadable: {e}")
    return problems

def scan_and_report():
    total_files = 0
    problem_files = []
    for folder in FOLDERS:
        for root, _, files in os.walk(folder):
            for f in files:
                file_path = Path(root) / f
                total_files += 1
                problems = check_file_integrity(file_path)
                if problems:
                    problem_files.append((str(file_path), problems))
    print(f"Scanned {total_files} files.")
    if problem_files:
        print(f"Found {len(problem_files)} problematic files:")
        for path, issues in problem_files:
            print(f"{path}: {', '.join(issues)}")
    else:
        print("All files passed integrity checks.")

if __name__ == "__main__":
    scan_and_report()
