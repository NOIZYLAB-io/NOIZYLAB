#!/usr/bin/env python3
"""
🔥 NOIZY HARVEST - ULTRA CODE HARVESTER 🔥
Resumable multi-repo harvest + global search index
For M2 Ultra with 50TB+ storage across 21 volumes
"""
import argparse
import concurrent.futures as cf
import csv
import hashlib
import json
import os
import random
import re
import shutil
import sqlite3
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# ----------------------------
# Defaults (override via config)
# ----------------------------
DEFAULT_ROOT = Path("/Volumes/GABRIEL")
FALLBACK_ROOT = Path.cwd()

DEFAULT_EXCLUDE_DIRS = {
    ".git", "node_modules", "dist", "build", ".next", ".cache", "coverage",
    "venv", ".venv", "__pycache__", ".idea", ".vscode", "target", ".terraform"
}

DEFAULT_SKIP_EXT = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".ico", ".pdf", ".zip", ".7z", ".dmg",
    ".exe", ".dll", ".so", ".dylib", ".mp3", ".wav", ".aiff", ".mp4", ".mov", ".m4v",
    ".ttf", ".otf", ".woff", ".woff2", ".psd", ".ai", ".sketch"
}

TEXT_NULL = b"\x00"


@dataclass
class Config:
    out_root: Path
    run_name: str
    parallel: int
    full_history: bool
    shallow_depth: int
    all_branches: bool
    submodules: bool
    lfs: bool
    ctags: bool
    gitleaks: bool
    retries: int
    max_concat_file_mb: float
    chunk_mb: float
    exclude_dirs: set
    skip_ext: set
    visibility: str
    include_forks: bool
    include_archived: bool


def have(cmd: str) -> bool:
    return shutil.which(cmd) is not None


def run(cmd: List[str], cwd: Optional[Path] = None, quiet: bool = False, check: bool = True, timeout: Optional[int] = None) -> subprocess.CompletedProcess:
    if not quiet:
        print(">", " ".join(cmd))
    return subprocess.run(
        cmd,
        cwd=str(cwd) if cwd else None,
        stdout=subprocess.PIPE if quiet else None,
        stderr=subprocess.PIPE if quiet else None,
        text=True if quiet else False,
        check=check,
        timeout=timeout
    )


def ensure_dir(p: Path) -> None:
    p.mkdir(parents=True, exist_ok=True)


def stable_root() -> Path:
    return DEFAULT_ROOT if DEFAULT_ROOT.exists() else FALLBACK_ROOT


def load_config(config_path: Optional[Path]) -> Config:
    root = stable_root() / "HarvestedCode"
    cfg = {
        "parallel": 8,
        "full_history": True,
        "shallow_depth": 100,
        "all_branches": True,
        "submodules": True,
        "lfs": True,
        "ctags": True,
        "gitleaks": False,
        "retries": 2,
        "max_concat_file_mb": 2.0,
        "chunk_mb": 25.0,
        "exclude_dirs": sorted(DEFAULT_EXCLUDE_DIRS),
        "skip_ext": sorted(DEFAULT_SKIP_EXT),
        "run_name": time.strftime("RUN_GENIUS_%Y%m%d_%H%M%S"),
        "visibility": "all",  # gh: all|public|private|internal
        "include_forks": False,
        "include_archived": False
    }
    if config_path:
        data = json.loads(config_path.read_text(encoding="utf-8"))
        cfg.update(data)

    out_root = Path(cfg.get("out_root", str(root)))
    return Config(
        out_root=out_root,
        run_name=cfg["run_name"],
        parallel=int(cfg["parallel"]),
        full_history=bool(cfg["full_history"]),
        shallow_depth=int(cfg["shallow_depth"]),
        all_branches=bool(cfg["all_branches"]),
        submodules=bool(cfg["submodules"]),
        lfs=bool(cfg["lfs"]),
        ctags=bool(cfg["ctags"]),
        gitleaks=bool(cfg["gitleaks"]),
        retries=int(cfg["retries"]),
        max_concat_file_mb=float(cfg["max_concat_file_mb"]),
        chunk_mb=float(cfg["chunk_mb"]),
        exclude_dirs=set(cfg["exclude_dirs"]),
        skip_ext=set(cfg["skip_ext"]),
        visibility=str(cfg["visibility"]),
        include_forks=bool(cfg["include_forks"]),
        include_archived=bool(cfg["include_archived"]),
    )


def repo_name_from_url(url: str) -> str:
    name = url.rstrip("/").split("/")[-1]
    return name[:-4] if name.endswith(".git") else name


def backoff_sleep(attempt: int) -> None:
    # jittered exponential backoff
    base = min(8.0, 0.6 * (2 ** attempt))
    time.sleep(base + random.random() * 0.4)


def write_text(p: Path, s: str) -> None:
    p.write_text(s, encoding="utf-8", errors="replace")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def is_texty(path: Path, skip_ext: set) -> bool:
    ext = path.suffix.lower()
    if ext in skip_ext:
        return False
    try:
        with path.open("rb") as f:
            b = f.read(4096)
        return TEXT_NULL not in b
    except Exception:
        return False


def should_exclude(rel_parts: Tuple[str, ...], exclude_dirs: set) -> bool:
    return any(part in exclude_dirs for part in rel_parts)


def init_global_fts(db_path: Path) -> None:
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("PRAGMA journal_mode=WAL;")
    cur.execute("CREATE VIRTUAL TABLE IF NOT EXISTS files USING fts5(repo, path, content);")
    con.commit()
    con.close()


def add_to_global_fts(db_path: Path, repo: str, rel_path: str, content: str) -> None:
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("INSERT INTO files(repo, path, content) VALUES (?, ?, ?);", (repo, rel_path, content))
    con.commit()
    con.close()


def discover_repos(target: str, kind: str, cfg: Config, out_file: Path) -> None:
    if not have("gh"):
        raise SystemExit("Missing gh. Install: brew install gh")
    try:
        run(["gh", "auth", "status"], quiet=True)
    except subprocess.CalledProcessError:
        raise SystemExit("Run: gh auth login")

    # gh repo list works for org and user; kind kept for clarity
    cp = run([
        "gh", "repo", "list", target,
        "--limit", "4000",
        "--visibility", cfg.visibility,
        "--json", "sshUrl,isFork,isArchived",
        "-q", ".[] | [.sshUrl, (.isFork|tostring), (.isArchived|tostring)] | @tsv"
    ], quiet=True)

    lines = cp.stdout.splitlines()
    urls: List[str] = []
    for line in lines:
        parts = line.split("\t")
        if len(parts) != 3:
            continue
        url, is_fork, is_arch = parts
        if (not cfg.include_forks) and is_fork.strip() == "true":
            continue
        if (not cfg.include_archived) and is_arch.strip() == "true":
            continue
        urls.append(url.strip())

    urls = sorted(set(u for u in urls if u))
    out_file.write_text("\n".join(urls) + ("\n" if urls else ""), encoding="utf-8")
    print(f"Wrote {out_file} ({len(urls)} repos)")


def update_or_create_mirror(repo_url: str, mirror_dir: Path) -> None:
    if mirror_dir.exists():
        # keep mirror fresh
        run(["git", "remote", "set-url", "origin", repo_url], cwd=mirror_dir, quiet=True, check=False)
        run(["git", "fetch", "--all", "--tags", "--prune"], cwd=mirror_dir, quiet=True, check=False)
    else:
        ensure_dir(mirror_dir.parent)
        run(["git", "clone", "--mirror", repo_url, str(mirror_dir)], quiet=True)


def clone_from_mirror(cfg: Config, mirror_dir: Path, dest_repo_dir: Path) -> None:
    if dest_repo_dir.exists():
        shutil.rmtree(dest_repo_dir)

    if cfg.full_history:
        run(["git", "clone", str(mirror_dir), str(dest_repo_dir)], quiet=True)
    else:
        run(["git", "clone", "--depth", str(cfg.shallow_depth), str(mirror_dir), str(dest_repo_dir)], quiet=True)


def git_meta(repo_dir: Path) -> Dict[str, str]:
    def g(args: List[str]) -> str:
        cp = run(["git"] + args, cwd=repo_dir, quiet=True, check=False)
        return (cp.stdout or "").strip()

    return {
        "default_branch": g(["symbolic-ref", "--quiet", "--short", "HEAD"]) or "unknown",
        "head_commit": g(["rev-parse", "HEAD"]) or "unknown",
        "head_date": g(["show", "-s", "--format=%ci", "HEAD"]) or "unknown",
    }


def build_repo_outputs(cfg: Config, repo_name: str, repo_url: str, repo_dir: Path, out_dir: Path, global_fts: Path) -> Dict:
    ensure_dir(out_dir)

    # git metadata dumps
    meta = {"repo_url": repo_url, **git_meta(repo_dir)}
    write_text(out_dir / "meta.txt", "\n".join([f"{k}={v}" for k, v in meta.items()]) + "\n")

    run(["git", "log", "--oneline", "-n", "5000"], cwd=repo_dir, quiet=True, check=False)
    (out_dir / "git_log_oneline.txt").write_text(
        run(["git", "log", "--oneline", "-n", "5000"], cwd=repo_dir, quiet=True, check=False).stdout or "",
        encoding="utf-8", errors="replace"
    )
    (out_dir / "git_shortlog.txt").write_text(
        run(["git", "shortlog", "-sn"], cwd=repo_dir, quiet=True, check=False).stdout or "",
        encoding="utf-8", errors="replace"
    )
    (out_dir / "git_branches.txt").write_text(
        run(["git", "branch", "-a"], cwd=repo_dir, quiet=True, check=False).stdout or "",
        encoding="utf-8", errors="replace"
    )
    (out_dir / "git_tags.txt").write_text(
        run(["git", "tag", "-l"], cwd=repo_dir, quiet=True, check=False).stdout or "",
        encoding="utf-8", errors="replace"
    )

    # optional: submodules / LFS / branches
    if cfg.all_branches:
        run(["git", "fetch", "--all", "--tags", "--prune"], cwd=repo_dir, quiet=True, check=False)
    if cfg.submodules:
        run(["git", "submodule", "update", "--init", "--recursive"], cwd=repo_dir, quiet=True, check=False)
    if cfg.lfs and have("git") and have("git-lfs"):
        run(["git", "lfs", "pull"], cwd=repo_dir, quiet=True, check=False)

    # optional: tags index
    if cfg.ctags and have("ctags"):
        run([
            "ctags", "-R",
            "--exclude=.git", "--exclude=node_modules", "--exclude=dist", "--exclude=build",
            "--exclude=.next", "--exclude=.cache",
            "-f", str(out_dir / "tags"),
            "."
        ], cwd=repo_dir, quiet=True, check=False)

    # optional: secrets scan
    if cfg.gitleaks and have("gitleaks"):
        run([
            "gitleaks", "detect",
            "--source", ".", "--no-git", "--redact",
            "--report-format", "json",
            "--report-path", str(out_dir / "gitleaks.json")
        ], cwd=repo_dir, quiet=True, check=False)

    # inventory + duplicates + chunked concat + per-repo FTS
    inv_csv = out_dir / "inventory.csv"
    dup_csv = out_dir / "duplicates.csv"
    chunks_dir = out_dir / "all_code_chunks"
    repo_fts = out_dir / "search_fts.sqlite"

    ensure_dir(chunks_dir)

    max_file_bytes = int(cfg.max_concat_file_mb * 1024 * 1024)
    chunk_target = int(cfg.chunk_mb * 1024 * 1024)

    rows: List[Tuple[str, int, str, str]] = []
    hash_map: Dict[str, List[str]] = {}
    ext_counts: Dict[str, int] = {}
    text_files: List[Tuple[str, int]] = []

    # walk repo
    for p in repo_dir.rglob("*"):
        if p.is_dir():
            continue
        rel = p.relative_to(repo_dir)
        parts = rel.parts
        if should_exclude(parts, cfg.exclude_dirs):
            continue
        try:
            sz = p.stat().st_size
        except Exception:
            continue
        ext = p.suffix.lower()
        ext_counts[ext] = ext_counts.get(ext, 0) + 1

        h = ""
        try:
            if sz <= 50 * 1024 * 1024:
                h = sha256_file(p)
                hash_map.setdefault(h, []).append(str(rel))
        except Exception:
            pass

        rows.append((str(rel), sz, ext, h))

        if sz <= max_file_bytes and is_texty(p, cfg.skip_ext):
            text_files.append((str(rel), sz))

    rows.sort(key=lambda x: x[0])

    # write inventory
    with inv_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["path", "bytes", "ext", "sha256"])
        w.writerows(rows)

    dupes = [(h, paths) for h, paths in hash_map.items() if h and len(paths) > 1]
    dupes.sort(key=lambda x: (-len(x[1]), x[0]))

    with dup_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["sha256", "count", "paths"])
        for h, paths in dupes:
            w.writerow([h, len(paths), " | ".join(sorted(paths))])

    # chunked concatenation + global FTS + per-repo FTS
    # init per-repo FTS
    con = sqlite3.connect(repo_fts)
    cur = con.cursor()
    cur.execute("PRAGMA journal_mode=WAL;")
    cur.execute("CREATE VIRTUAL TABLE IF NOT EXISTS files USING fts5(path, content);")
    cur.execute("DELETE FROM files;")
    con.commit()

    chunk_idx = 1
    chunk_bytes = 0
    chunk_path = chunks_dir / f"all_code_{chunk_idx:03d}.txt"
    out = chunk_path.open("w", encoding="utf-8", errors="replace")

    def rotate():
        nonlocal chunk_idx, chunk_bytes, out
        out.close()
        chunk_idx += 1
        chunk_bytes = 0
        np = chunks_dir / f"all_code_{chunk_idx:03d}.txt"
        out = np.open("w", encoding="utf-8", errors="replace")

    for rel, sz in sorted(text_files, key=lambda x: x[0]):
        fp = repo_dir / rel
        try:
            content = fp.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        # rotate chunk based on *approx* size
        inc = len(content.encode("utf-8", errors="ignore"))
        if chunk_bytes + inc > chunk_target and chunk_bytes > 0:
            rotate()

        out.write(f"\n\n===== FILE: {rel} ({sz} bytes) =====\n")
        out.write(content)
        chunk_bytes += inc

        # per-repo FTS
        try:
            cur.execute("INSERT INTO files(path, content) VALUES (?, ?);", (rel, content))
        except Exception:
            pass

        # global FTS (single DB for all repos)
        try:
            add_to_global_fts(global_fts, repo_name, rel, content)
        except Exception:
            pass

    out.close()
    con.commit()
    con.close()

    stats = {
        "repo": repo_name,
        "repo_url": repo_url,
        "default_branch": meta["default_branch"],
        "head_commit": meta["head_commit"],
        "head_date": meta["head_date"],
        "files_total": len(rows),
        "text_files_indexed": len(text_files),
        "duplicates_groups": len(dupes),
        "chunks": chunk_idx,
        "chunk_target_bytes": chunk_target,
        "max_concat_file_bytes": max_file_bytes,
        "ext_counts": dict(sorted(ext_counts.items(), key=lambda kv: (-kv[1], kv[0]))),
    }
    (out_dir / "stats.json").write_text(json.dumps(stats, indent=2), encoding="utf-8")
    return stats


def harvest_repo(cfg: Config, run_dir: Path, cache_dir: Path, global_fts: Path, repo_url: str) -> Tuple[str, bool, str]:
    name = repo_name_from_url(repo_url)
    base = run_dir / name
    repo_dir = base / "repo"
    out_dir = base / "out"
    done_flag = out_dir / ".DONE"
    log_dir = run_dir / "_logs"
    ensure_dir(log_dir)

    log_file = log_dir / f"{name}.log"

    if done_flag.exists():
        return (name, True, "skip (done)")

    ensure_dir(base)
    ensure_dir(out_dir)

    mirror_dir = cache_dir / f"{name}.git"

    # retry loop
    for attempt in range(cfg.retries + 1):
        try:
            with log_file.open("w", encoding="utf-8") as lf:
                lf.write(f"repo={name}\nurl={repo_url}\n")
                lf.flush()

                update_or_create_mirror(repo_url, mirror_dir)
                clone_from_mirror(cfg, mirror_dir, repo_dir)

                stats = build_repo_outputs(cfg, name, repo_url, repo_dir, out_dir, global_fts)

                # zip per repo (optional, fast enough)
                zip_path = base / f"{name}.zip"
                if zip_path.exists():
                    zip_path.unlink()
                run(["zip", "-qr", str(zip_path), "."], cwd=base, quiet=True, check=False)

                done_flag.write_text("ok\n", encoding="utf-8")
                return (name, True, f"ok ({stats.get('text_files_indexed')} files indexed)")
        except Exception as e:
            if attempt >= cfg.retries:
                return (name, False, f"failed: {e}")
            backoff_sleep(attempt)

    return (name, False, "failed: unknown")


def harvest(cfg: Config, repos_file: Path) -> Path:
    run_dir = cfg.out_root / cfg.run_name
    cache_dir = cfg.out_root / "_cache_mirrors"
    global_dir = run_dir / "_global"
    ensure_dir(run_dir)
    ensure_dir(cache_dir)
    ensure_dir(global_dir)
    ensure_dir(run_dir / "_logs")

    # global FTS
    global_fts = global_dir / "search_fts.sqlite"
    if global_fts.exists():
        global_fts.unlink()
    init_global_fts(global_fts)

    # load repo urls
    repo_urls = []
    for line in repos_file.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        repo_urls.append(s)
    repo_urls = sorted(set(repo_urls))

    # record run config
    (run_dir / "RUN_CONFIG.json").write_text(json.dumps(cfg.__dict__, default=str, indent=2), encoding="utf-8")
    (run_dir / "repos.txt").write_text("\n".join(repo_urls) + "\n", encoding="utf-8")

    # parallel harvest
    results = []
    with cf.ThreadPoolExecutor(max_workers=cfg.parallel) as ex:
        futs = [ex.submit(harvest_repo, cfg, run_dir, cache_dir, global_fts, url) for url in repo_urls]
        for fut in cf.as_completed(futs):
            results.append(fut.result())
            name, ok, msg = results[-1]
            print(f"[{name}] {'OK' if ok else 'FAIL'} - {msg}")

    # master index
    master = []
    for name, ok, msg in sorted(results, key=lambda x: x[0]):
        stats_path = run_dir / name / "out" / "stats.json"
        meta_path = run_dir / name / "out" / "meta.txt"
        stats = {}
        meta = {}
        if stats_path.exists():
            stats = json.loads(stats_path.read_text(encoding="utf-8"))
        if meta_path.exists():
            for line in meta_path.read_text(encoding="utf-8", errors="replace").splitlines():
                if "=" in line:
                    k, v = line.split("=", 1)
                    meta[k] = v
        master.append({"repo": name, "ok": ok, "msg": msg, **meta, **stats})

    (run_dir / "MASTER_INDEX.json").write_text(json.dumps(master, indent=2), encoding="utf-8")

    # zip master
    master_zip = run_dir / f"{cfg.run_name}_MASTER.zip"
    if master_zip.exists():
        master_zip.unlink()
    run(["zip", "-qr", str(master_zip), "."], cwd=run_dir, quiet=True, check=False)

    return run_dir


def search_global(run_dir: Path, query: str, limit: int) -> None:
    db = run_dir / "_global" / "search_fts.sqlite"
    if not db.exists():
        raise SystemExit(f"Missing global FTS DB: {db}")
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("SELECT repo, path FROM files WHERE files MATCH ? LIMIT ?;", (query, limit))
    rows = cur.fetchall()
    con.close()
    for repo, path in rows:
        print(f"{repo}\t{path}")


def main() -> None:
    p = argparse.ArgumentParser(prog="noizy_harvest", description="Resumable multi-repo harvest + global search index")
    p.add_argument("--config", type=str, default="", help="Path to JSON config file")

    sp = p.add_subparsers(dest="cmd", required=True)

    d = sp.add_parser("discover", help="Generate repos.txt using gh")
    d.add_argument("target", type=str, help="Org/user name")
    d.add_argument("--kind", type=str, default="org", choices=["org", "user"])
    d.add_argument("--out", type=str, default="repos.txt")

    h = sp.add_parser("harvest", help="Harvest all repos in repos.txt")
    h.add_argument("--repos", type=str, default="repos.txt", help="repo list file")

    s = sp.add_parser("search", help="Search the global SQLite FTS index")
    s.add_argument("run_dir", type=str, help="Run directory (e.g. /Volumes/GABRIEL/HarvestedCode/RUN_GENIUS_...)")
    s.add_argument("query", type=str, help="FTS query, e.g. \"ticket AND status\"")
    s.add_argument("--limit", type=int, default=50)

    args = p.parse_args()
    cfg = load_config(Path(args.config) if args.config else None)

    if args.cmd == "discover":
        discover_repos(args.target, args.kind, cfg, Path(args.out))
    elif args.cmd == "harvest":
        repos_file = Path(args.repos)
        if not repos_file.exists():
            raise SystemExit(f"Missing {repos_file}")
        run_dir = harvest(cfg, repos_file)
        print(f"DONE: {run_dir}")
    elif args.cmd == "search":
        search_global(Path(args.run_dir), args.query, args.limit)
    else:
        raise SystemExit("Unknown command")


if __name__ == "__main__":
    main()
