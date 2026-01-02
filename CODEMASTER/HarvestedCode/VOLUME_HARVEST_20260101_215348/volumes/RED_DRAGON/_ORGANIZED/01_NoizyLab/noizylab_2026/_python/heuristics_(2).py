\
from __future__ import annotations
from pathlib import Path
from typing import List, Tuple
from .engine import DupeGroup, FileInfo

def pick_keepers(groups: List[DupeGroup]) -> List[Tuple[FileInfo, List[FileInfo]]]:
    """
    For each dupe group, choose one 'keeper' (latest mtime) and mark others as duplicates.
    Returns list of (keeper, [dupes]).
    """
    decisions = []
    for g in groups:
        sorted_files = sorted(g.files, key=lambda f: (f.mtime, -len(f.path)), reverse=True)
        keeper = sorted_files[0]
        dupes = sorted_files[1:]
        decisions.append((keeper, dupes))
    return decisions
