import os
from pathlib import Path
from logger.log import logger

def validate_file_path(file_path: str) -> str:
    """
    Validate and normalize a file path for security and consistency.

    Args:
        file_path: The file path to validate

    Returns:
        str: The validated and normalized file path

    Raises:
        ValueError: If the file path is invalid or contains security risks
    """
    if not file_path or not isinstance(file_path, str):
        raise ValueError("File path must be a non-empty string")

    # Security check: prevent directory traversal
    if ".." in file_path:
        raise ValueError("Invalid file path: directory traversal detected")

    # Security check: prevent absolute paths that could access system files
    if file_path.startswith("/") or (len(file_path) > 1 and file_path[1] == ":"):
        # Allow absolute paths but log them for security monitoring
        logger.warning(f"Absolute file path detected: {file_path}")

    # Normalize path separators and remove redundant separators
    normalized_path = str(Path(file_path).as_posix())

    # Basic validation: ensure it's not empty after normalization
    if not normalized_path or normalized_path == ".":
        raise ValueError("File path cannot be empty or just a dot")

    return normalized_path

class PathSelector:
    @staticmethod
    def get_base_path():
        """Get the base application path"""
        return Path.home() / ".codemate"

    @staticmethod
    def get_cache_path():
        """Get the cache directory path"""
        path = PathSelector.get_base_path() / "cache"
        os.makedirs(path, exist_ok=True)
        return path

    @staticmethod
    def get_logs_path():
        """Get the logs directory path"""
        path = PathSelector.get_base_path() / "logs"
        os.makedirs(path, exist_ok=True)
        return path

    @staticmethod
    def get_qdrant_db_path(make_if_not_exists: bool = True):
        path = PathSelector.get_base_path() / ".neocortex"
        if make_if_not_exists:
            os.makedirs(path, exist_ok=True)
        return path