import logging
from datetime import datetime
from pathlib import Path
from typing import Optional, Tuple

logging.basicConfig(level=logging.INFO)

INVALID_CHARS = set(r'<>:"/\\|?*')

def sanitize_filename(filename: str) -> str:
    """
    Remove invalid characters from filename for cross-platform safety.
    """
    return ''.join(c for c in filename if c not in INVALID_CHARS)

def save_to_noizy(
    text: str,
    filename: Optional[str] = None,
    folder: str = "NoizyAI_Documents",
    append: bool = False
) -> Tuple[bool, Optional[Path]]:
    """
    Saves given text into ~/Documents/<folder>/<filename>.txt
    - text: the string content to save
    - filename: optional; if None, uses timestamp
    - folder: default = "NoizyAI_Documents" but you can change to "Noizy_Documents"
    - append: if True, appends to file; else overwrites
    Returns (success, file_path)
    """
    base = Path.home() / "Documents" / folder
    try:
        base.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        logging.error("Failed to create folder %s: %s", base, e)
        return False, None

    if not filename:
        filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = sanitize_filename(filename)
    if not filename.endswith(".txt"):
        filename += ".txt"
    file_path = base / filename

    mode = "a" if append else "w"
    try:
        with open(file_path, mode, encoding="utf-8") as f:
            f.write(text)
        logging.info("Saved to %s", file_path)
        return True, file_path
    except OSError as e:
        logging.error("Failed to save file %s: %s", file_path, e)
        return False, None

def read_noizy_file(
    filename: str,
    folder: str = "NoizyAI_Documents"
) -> Optional[str]:
    """
    Reads and returns the contents of ~/Documents/<folder>/<filename>.txt
    Returns None if file not found or error occurs.
    """
    filename = sanitize_filename(filename)
    if not filename.endswith(".txt"):
        filename += ".txt"
    file_path = Path.home() / "Documents" / folder / filename
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except OSError as e:
        logging.error("Failed to read file %s: %s", file_path, e)
        return None

def list_noizy_files(
    folder: str = "NoizyAI_Documents"
) -> list:
    """
    Lists all .txt files in ~/Documents/<folder>
    Returns a list of filenames.
    """
    base = Path.home() / "Documents" / folder
    try:
        return [f.name for f in base.glob("*.txt") if f.is_file()]
    except OSError as e:
        logging.error("Failed to list files in %s: %s", base, e)
        return []

def delete_noizy_file(
    filename: str,
    folder: str = "NoizyAI_Documents"
) -> bool:
    """
    Deletes ~/Documents/<folder>/<filename>.txt
    Returns True if deleted, False if not found or error.
    """
    filename = sanitize_filename(filename)
    if not filename.endswith(".txt"):
        filename += ".txt"
    file_path = Path.home() / "Documents" / folder / filename
    try:
        file_path.unlink()
        logging.info("Deleted file %s", file_path)
        return True
    except FileNotFoundError:
        logging.warning("File not found: %s", file_path)
        return False
    except OSError as e:
        logging.error("Failed to delete file %s: %s", file_path, e)
        return False

def search_noizy_files(
    keyword: str,
    folder: str = "NoizyAI_Documents"
) -> list:
    """
    Returns a list of filenames in ~/Documents/<folder> containing the keyword.
    """
    base = Path.home() / "Documents" / folder
    matches = []
    try:
        for f in base.glob("*.txt"):
            if f.is_file():
                try:
                    with open(f, "r", encoding="utf-8") as file:
                        if keyword in file.read():
                            matches.append(f.name)
                except OSError:
                    continue
        return matches
    except OSError as e:
        logging.error("Failed to search files in %s: %s", base, e)
        return []

def rename_noizy_file(
    old_filename: str,
    new_filename: str,
    folder: str = "NoizyAI_Documents"
) -> bool:
    """
    Renames ~/Documents/<folder>/<old_filename>.txt to <new_filename>.txt
    Returns True if successful, False otherwise.
    """
    old_filename = sanitize_filename(old_filename)
    new_filename = sanitize_filename(new_filename)
    if not old_filename.endswith(".txt"):
        old_filename += ".txt"
    if not new_filename.endswith(".txt"):
        new_filename += ".txt"
    base = Path.home() / "Documents" / folder
    old_path = base / old_filename
    new_path = base / new_filename
    try:
        old_path.rename(new_path)
        logging.info("Renamed file %s to %s", old_path, new_path)
        return True
    except FileNotFoundError:
        logging.warning("File not found: %s", old_path)
        return False
    except OSError as e:
        logging.error("Failed to rename file %s: %s", old_path, e)
        return False

def get_noizy_file_info(
    filename: str,
    folder: str = "NoizyAI_Documents"
) -> Optional[dict]:
    """
    Returns info dict for ~/Documents/<folder>/<filename>.txt:
    {'size': bytes, 'modified': datetime}
    Returns None if file not found or error.
    """
    filename = sanitize_filename(filename)
    if not filename.endswith(".txt"):
        filename += ".txt"
    file_path = Path.home() / "Documents" / folder / filename
    try:
        stat = file_path.stat()
        return {
            "size": stat.st_size,
            "modified": datetime.fromtimestamp(stat.st_mtime)
        }
    except OSError as e:
        logging.error("Failed to get info for file %s: %s", file_path, e)
        return None

def bulk_delete_noizy_files(
    keyword: str,
    folder: str = "NoizyAI_Documents"
) -> int:
    """
    Deletes all .txt files in ~/Documents/<folder> containing the keyword.
    Returns the number of files deleted.
    """
    base = Path.home() / "Documents" / folder
    count = 0
    try:
        for f in base.glob("*.txt"):
            if f.is_file():
                try:
                    with open(f, "r", encoding="utf-8") as file:
                        if keyword in file.read():
                            f.unlink()
                            logging.info("Deleted file %s", f)
                            count += 1
                except OSError:
                    continue
        return count
    except OSError as e:
        logging.error("Failed to bulk delete files in %s: %s", base, e)
        return 0

def export_noizy_file(
    filename: str,
    target_folder: str,
    source_folder: str = "NoizyAI_Documents"
) -> bool:
    """
    Copies ~/Documents/<source_folder>/<filename>.txt to ~/Documents/<target_folder>/<filename>.txt
    Returns True if successful, False otherwise.
    """
    filename = sanitize_filename(filename)
    if not filename.endswith(".txt"):
        filename += ".txt"
    source_path = Path.home() / "Documents" / source_folder / filename
    target_base = Path.home() / "Documents" / target_folder
    target_base.mkdir(parents=True, exist_ok=True)
    target_path = target_base / filename
    try:
        with open(source_path, "r", encoding="utf-8") as src, open(target_path, "w", encoding="utf-8") as dst:
            dst.write(src.read())
        logging.info("Exported file %s to %s", source_path, target_path)
        return True
    except OSError as e:
        logging.error("Failed to export file %s: %s", source_path, e)
        return False