"""Utilities for cataloguing the FISHMUSIC field recording collection.

This module focuses on working with small, locally stored collections of WAV
files that capture underwater recordings.  The primary entry point is the
``scan_collection`` function which inspects a directory tree and produces a
structured summary of all compatible audio assets.  The summary can then be
rendered to JSON or Markdown to support documentation and dataset cards.
"""

from __future__ import annotations

import argparse
import dataclasses
import datetime as _dt
import json
import os
from pathlib import Path
from typing import Iterable, List, Sequence
import wave

SUPPORTED_SUFFIXES: Sequence[str] = (".wav",)


@dataclasses.dataclass(slots=True)
class AudioSample:
    """Metadata describing a single audio asset.

    Attributes
    ----------
    file_path:
        Full path to the audio file.
    species:
        The inferred species or subject name derived from the file name.  The
        first token of the stem (delimited by ``_`` or ``-``) is treated as the
        subject.
    channels:
        Number of audio channels in the sample.
    sample_rate:
        Sample rate reported by the WAV header.
    duration_seconds:
        Length of the recording in seconds, rounded to three decimal places.
    captured_at:
        Optional timestamp encoded in the file name using the
        ``YYYYMMDDThhmmss`` pattern.  When the pattern is not present this
        attribute is ``None``.
    tags:
        Additional tokens derived from the file name, useful for surfacing
        recording notes such as ``night`` or ``reef``.
    """

    file_path: Path
    species: str
    channels: int
    sample_rate: int
    duration_seconds: float
    captured_at: _dt.datetime | None
    tags: List[str]

    @property
    def stem(self) -> str:
        return self.file_path.stem


class CollectionFormatter:
    """Format :class:`AudioSample` instances into machine readable summaries."""

    def __init__(self, samples: Iterable[AudioSample]):
        self._samples = list(samples)

    def to_json(self) -> str:
        """Return the collection as a JSON string."""

        payload = [dataclasses.asdict(sample) | {"file_path": str(sample.file_path)} for sample in self._samples]
        return json.dumps(payload, indent=2, default=str)

    def to_markdown(self) -> str:
        """Return the collection as a Markdown table."""

        if not self._samples:
            return "| File | Species | Duration (s) | Sample Rate | Tags |\n| --- | --- | --- | --- | --- |"

        lines = [
            "| File | Species | Duration (s) | Sample Rate | Tags |",
            "| --- | --- | --- | --- | --- |",
        ]
        for sample in self._samples:
            tags = ", ".join(sample.tags) if sample.tags else "—"
            lines.append(
                f"| {sample.file_path.name} | {sample.species} | {sample.duration_seconds:.3f} | "
                f"{sample.sample_rate} | {tags} |"
            )
        return "\n".join(lines)


def scan_collection(root: os.PathLike[str] | str) -> List[AudioSample]:
    """Scan *root* for supported audio files and extract metadata.

    Parameters
    ----------
    root:
        Directory containing the FISHMUSIC recordings.  The directory is
        traversed recursively.

    Returns
    -------
    list[AudioSample]
        A list of metadata objects sorted by file path.
    """

    root_path = Path(root).expanduser().resolve()
    if not root_path.exists():
        raise FileNotFoundError(f"Collection root does not exist: {root_path}")

    samples: List[AudioSample] = []

    for path in sorted(root_path.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in SUPPORTED_SUFFIXES:
            continue

        sample = _build_sample(path)
        samples.append(sample)

    return samples


def _build_sample(path: Path) -> AudioSample:
    with wave.open(str(path), "rb") as wav_file:
        channels = wav_file.getnchannels()
        sample_rate = wav_file.getframerate()
        frame_count = wav_file.getnframes()
        duration_seconds = round(frame_count / float(sample_rate), 3) if sample_rate else 0.0

    species, captured_at, tags = _parse_stem(path.stem)

    return AudioSample(
        file_path=path,
        species=species,
        channels=channels,
        sample_rate=sample_rate,
        duration_seconds=duration_seconds,
        captured_at=captured_at,
        tags=tags,
    )


def _parse_stem(stem: str) -> tuple[str, _dt.datetime | None, List[str]]:
    tokens = [token for token in stem.replace("-", "_").split("_") if token]
    if not tokens:
        return "unknown", None, []

    species = tokens[0].lower()
    tags: List[str] = []
    captured_at: _dt.datetime | None = None

    for token in tokens[1:]:
        try:
            captured_at = _dt.datetime.strptime(token, "%Y%m%dT%H%M%S")
            continue
        except ValueError:
            pass

        tags.append(token.lower())

    return species, captured_at, tags


def _cli(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Summarise a FISHMUSIC recording collection.")
    parser.add_argument("root", type=Path, help="Root directory containing audio files.")
    parser.add_argument(
        "--format",
        choices=("json", "markdown"),
        default="json",
        help="Output format for the summary (default: json).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Optional path to write the summary.  When omitted the summary is printed to stdout.",
    )
    args = parser.parse_args(argv)

    samples = scan_collection(args.root)
    formatter = CollectionFormatter(samples)
    if args.format == "json":
        summary = formatter.to_json()
    else:
        summary = formatter.to_markdown()

    if args.output:
        args.output.write_text(summary, encoding="utf-8")
    else:
        print(summary)

    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry
    raise SystemExit(_cli())
