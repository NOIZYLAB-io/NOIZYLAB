#!/usr/bin/env python3
import os
import re
import argparse
from pathlib import Path

import soundfile as sf
import librosa


DEFAULT_DRIVE_PATH = "/Volumes/4TBSG"
DEFAULT_EXTS = [".wav", ".mp3", ".flac", ".aiff", ".ogg"]
DEFAULT_PATTERN = re.compile(r"^[\w\-]+\.(wav|mp3|flac|aiff|ogg)$", re.IGNORECASE)
SF_READABLE_EXTS = {".wav", ".flac", ".aiff", ".ogg"}


from typing import List, Tuple, Optional, Pattern, Dict


def is_name_valid(filename: str, pattern: Pattern) -> bool:
    return bool(pattern.match(filename))


def check_with_soundfile(path: str) -> Tuple[bool, Optional[str]]:
    try:
        with sf.SoundFile(path) as f:
            if f.frames <= 0:
                return False, "zero frames"
            frames_to_read = 256 if f.frames >= 256 else max(1, f.frames)
            data = f.read(frames=frames_to_read, dtype="float32", always_2d=True)
            if getattr(data, "size", 0) == 0:
                return False, "no samples read"
        return True, None
    except Exception as e:
        return False, str(e)


def check_with_librosa(path: str, duration: float = 0.1) -> Tuple[bool, Optional[str]]:
    try:
        y, sr = librosa.load(path, sr=None, mono=False, duration=duration)
        if y is None or sr is None:
            return False, "decoder returned empty"
        size = getattr(y, "size", None)
        if size is not None and size == 0:
            return False, "no samples decoded"
        return True, None
    except Exception as e:
        return False, str(e)


def scan_audio(
    drive_path: str,
    extensions: List[str],
    name_pattern: Pattern,
    fast_duration: float = 0.1,
    include_hidden: bool = False,
):
    issues: List[str] = []
    stats: Dict[str, int] = {
        "files_total": 0,
        "files_audio": 0,
        "naming_issues": 0,
        "integrity_issues": 0,
        "skipped_hidden": 0,
    }

    for root, dirs, files in os.walk(drive_path):
        if not include_hidden:
            hidden_dirs = [d for d in dirs if d.startswith('.')]
            stats["skipped_hidden"] += len(hidden_dirs)
            for d in hidden_dirs:
                dirs.remove(d)

        for file in files:
            stats["files_total"] += 1
            ext = Path(file).suffix.lower()
            if ext not in extensions:
                continue
            stats["files_audio"] += 1
            path = os.path.join(root, file)

            if not is_name_valid(file, name_pattern):
                issues.append(f"Naming issue: {path}")
                stats["naming_issues"] += 1

            ok = True
            reason = None
            if ext in SF_READABLE_EXTS:
                ok, reason = check_with_soundfile(path)
                if not ok:
                    ok2, reason2 = check_with_librosa(path, duration=fast_duration)
                    if ok2:
                        ok, reason = True, None
                    else:
                        reason = f"sf: {reason}; librosa: {reason2}"
                        ok = False
            else:
                ok, reason = check_with_librosa(path, duration=fast_duration)

            if not ok:
                issues.append(f"Integrity issue: {path} - {reason}")
                stats["integrity_issues"] += 1

    return issues, stats


def write_report(report_path: Path, issues: list[str], stats: dict):
    report_path.parent.mkdir(parents=True, exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("Audio Integrity Scan Report\n")
        f.write("===========================\n")
        for k in ["files_total", "files_audio", "naming_issues", "integrity_issues", "skipped_hidden"]:
            f.write(f"{k}: {stats.get(k, 0)}\n")
        f.write("\nFindings:\n")
        for line in issues:
            f.write(line + "\n")


def main():
    parser = argparse.ArgumentParser(description="Scan a drive for audio file naming and integrity issues.")
    parser.add_argument("--path", default=DEFAULT_DRIVE_PATH, help="Root path to scan")
    parser.add_argument("--report", default=None, help="Path to write the report file")
    parser.add_argument("--include-hidden", action="store_true", help="Include hidden folders (dot-prefixed)")
    parser.add_argument("--duration", type=float, default=0.1, help="Seconds to decode for fast integrity check")
    args = parser.parse_args()

    drive_path = args.path
    issues, stats = scan_audio(
        drive_path=drive_path,
        extensions=DEFAULT_EXTS,
        name_pattern=DEFAULT_PATTERN,
        fast_duration=args.duration,
        include_hidden=args.include_hidden,
    )

    if args.report:
        report_path = Path(args.report)
    else:
        report_path = Path(drive_path) / "audio_integrity_report.txt"

    try:
        write_report(report_path, issues, stats)
        print(f"Scan complete. Report saved to {report_path}")
    except PermissionError:
        fallback = Path.cwd() / "audio_integrity_report.txt"
        write_report(fallback, issues, stats)
        print(f"Scan complete. Permission denied at {report_path}. Report saved to {fallback}")


if __name__ == "__main__":
    main()
