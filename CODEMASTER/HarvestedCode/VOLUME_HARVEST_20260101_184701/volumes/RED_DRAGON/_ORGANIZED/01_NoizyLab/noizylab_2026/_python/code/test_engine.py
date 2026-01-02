\
import json, tempfile, os
from pathlib import Path
from engine.dupeshark.engine import scan

def test_scan_basic(tmp_path: Path):
    a = tmp_path / "a.txt"
    b = tmp_path / "b.txt"
    b2 = tmp_path / "b (copy).txt"
    a.write_text("unique", encoding="utf-8")
    b.write_text("duplicate", encoding="utf-8")
    b2.write_text("duplicate", encoding="utf-8")

    groups = scan(tmp_path, min_size=1)
    # Expect one dupe group (the two 'duplicate' files)
    dup_groups = [g for g in groups if len(g.files) >= 2]
    assert len(dup_groups) == 1
