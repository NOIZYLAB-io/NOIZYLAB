"""
MagnificentTen: Robust text file and AI orchestration toolkit for ~/Documents/MagnificentTen_Documents.
Features: save, read, list, delete, search, rename, info, bulk delete, export, and more.
"""

from magnificent_ten import save_to_noizy
from typing import Optional, Tuple
from pathlib import Path

def save_to_noizy(
    text: str,
    filename: Optional[str] = None,
    folder: str = "MagnificentTen_Documents",
    append: bool = False
) -> Tuple[bool, Optional[Path]]:
    # ...existing code...