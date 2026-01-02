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

# Example usage for your improved "super saver"
from noizy_saver import save_to_noizy

success, path = save_to_noizy(
    text="This is my test export.",
    filename="session_log",
    folder="NoizyAI_Documents",  # Or any folder name you prefer
    append=False                 # Set True to append instead of overwrite
)

if success:
    print(f"File saved at: {path}")
else:
    print("Failed to save file.")