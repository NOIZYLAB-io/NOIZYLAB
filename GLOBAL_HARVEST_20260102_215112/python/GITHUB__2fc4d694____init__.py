"""Core utilities for AI-Tools."""

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:  # pragma: no cover - import-time only for typing
    from .fishmusic_collection import AudioSample, CollectionFormatter, scan_collection

__all__ = [
    "AudioSample",
    "scan_collection",
    "CollectionFormatter",
]


def __getattr__(name: str) -> Any:  # pragma: no cover - simple attribute proxy
    if name in __all__:
        from .fishmusic_collection import AudioSample, CollectionFormatter, scan_collection

        exports = {
            "AudioSample": AudioSample,
            "scan_collection": scan_collection,
            "CollectionFormatter": CollectionFormatter,
        }
        return exports[name]
    raise AttributeError(f"module 'ai_tools' has no attribute {name!r}")
