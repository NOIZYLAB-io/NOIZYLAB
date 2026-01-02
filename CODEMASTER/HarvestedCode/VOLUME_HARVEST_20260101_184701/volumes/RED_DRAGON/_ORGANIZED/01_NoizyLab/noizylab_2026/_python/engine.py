\
from __future__ import annotations
import os, sys, hashlib, json, time
from pathlib import Path
from typing import Dict, List, Tuple, Iterable, Optional
from dataclasses import dataclass, asdict

# Minimal deps; optional audio handling is kept simple.
AUDIO_EXT = {".wav", ".aiff", ".aif", ".mp3", ".m4a", ".flac", ".ogg"}

@dataclass
class FileInfo:
    path: str
    size: int
    mtime: float
    sha1_head: Optional[str] = None
    sha1_full: Optional[str] = None

@dataclass
class DupeGroup:
    size: int
    files: List[FileInfo]

def iter_files(root: Path, min_size: int = 1, include_hidden=False) -> Iterable[Path]:
    for dirpath, dirnames, filenames in os.walk(root):
        if not include_hidden:
            dirnames[:] = [d for d in dirnames if not d.startswith(".")]
            filenames = [f for f in filenames if not f.startswith(".")]
        for name in filenames:
            p = Path(dirpath) / name
            try:
                st = p.stat()
            except FileNotFoundError:
                continue
            if st.st_size >= min_size:
                yield p

def quick_head_sha1(path: Path, bytes_n: int = 262144) -> str:
    h = hashlib.sha1()
    with open(path, "rb") as f:
        chunk = f.read(bytes_n)
        h.update(chunk)
    return h.hexdigest()

def full_sha1(path: Path, chunk: int = 1024 * 1024) -> str:
    h = hashlib.sha1()
    with open(path, "rb") as f:
        while True:
            buf = f.read(chunk)
            if not buf:
                break
            h.update(buf)
    return h.hexdigest()

def group_by_size(paths: Iterable[Path]) -> Dict[int, List[Path]]:
    buckets: Dict[int, List[Path]] = {}
    for p in paths:
        try:
            s = p.stat().st_size
        except FileNotFoundError:
            continue
        buckets.setdefault(s, []).append(p)
    return {k: v for k, v in buckets.items() if len(v) > 1}

def scan(root: Path, min_size: int = 1, head_bytes: int = 262144) -> List[DupeGroup]:
    # 1) group by size
    size_groups = group_by_size(iter_files(root, min_size=min_size))
    results: List[DupeGroup] = []

    for size, paths in size_groups.items():
        # 2) head hash pass
        head_map: Dict[str, List[Path]] = {}
        for p in paths:
            try:
                h = quick_head_sha1(p, head_bytes)
            except PermissionError:
                continue
            head_map.setdefault(h, []).append(p)

        for _hh, hh_group in head_map.items():
            if len(hh_group) < 2:
                continue
            # 3) full hash pass
            full_map: Dict[str, List[Path]] = {}
            for p in hh_group:
                try:
                    fh = full_sha1(p)
                except PermissionError:
                    continue
                full_map.setdefault(fh, []).append(p)

            for fh, files in full_map.items():
                if len(files) < 2:
                    continue
                infos = []
                for p in files:
                    st = p.stat()
                    infos.append(FileInfo(
                        path=str(p),
                        size=st.st_size,
                        mtime=st.st_mtime,
                        sha1_head=_hh,
                        sha1_full=fh
                    ))
                results.append(DupeGroup(size=size, files=infos))
    return results
