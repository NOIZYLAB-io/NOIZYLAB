"""
NoizyDrive AI File Classifier
=============================
Automatically classifies any file by type, purpose, and context.
Works with ANY file format.
"""

from typing import Dict, Optional, List
import os
import re


# File type mappings
EXTENSION_MAP = {
    # Audio
    "audio": [".wav", ".mp3", ".aiff", ".aif", ".flac", ".ogg", ".m4a", ".wma", ".aac"],
    
    # Video
    "video": [".mov", ".mp4", ".avi", ".mkv", ".wmv", ".flv", ".webm", ".m4v"],
    
    # Images
    "image": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".bmp", ".tiff", ".webp", ".ico", ".psd"],
    
    # Code
    "code": [".py", ".js", ".ts", ".jsx", ".tsx", ".cpp", ".c", ".h", ".java", ".go", ".rs", 
             ".swift", ".kt", ".rb", ".php", ".cs", ".sh", ".bash", ".zsh"],
    
    # Data/Config
    "data": [".json", ".yaml", ".yml", ".xml", ".csv", ".toml", ".ini", ".env"],
    
    # Documents
    "document": [".pdf", ".doc", ".docx", ".txt", ".md", ".rtf", ".odt", ".pages"],
    
    # Spreadsheets
    "spreadsheet": [".xls", ".xlsx", ".numbers", ".ods"],
    
    # Presentations
    "presentation": [".ppt", ".pptx", ".key", ".odp"],
    
    # Archives
    "archive": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz", ".dmg", ".iso"],
    
    # Executables
    "executable": [".exe", ".app", ".msi", ".pkg", ".deb", ".rpm"],
    
    # Fonts
    "font": [".ttf", ".otf", ".woff", ".woff2", ".eot"],
    
    # 3D/CAD
    "3d": [".obj", ".fbx", ".stl", ".blend", ".gltf", ".glb", ".dae"],
    
    # DAW/Music Production
    "project": [".als", ".flp", ".logic", ".ptx", ".rpp", ".cpr", ".aup"],
    
    # Sample Libraries
    "sample_library": [".nki", ".nkm", ".exs", ".sfz", ".kontakt"],
}

# Name pattern classifications
NAME_PATTERNS = {
    "client": [r"client", r"customer"],
    "session": [r"session", r"recording"],
    "backup": [r"backup", r"bak", r"_old", r"_copy"],
    "temp": [r"temp", r"tmp", r"cache"],
    "log": [r"\.log$", r"_log", r"logs?/"],
    "test": [r"test", r"spec", r"_test"],
    "config": [r"config", r"settings", r"preferences"],
}


def classify_file(filename: str, path: str = None) -> str:
    """
    Classify a file by its type.
    Returns category string.
    """
    name = filename.lower()
    ext = os.path.splitext(name)[1]
    
    # Check extension mappings
    for category, extensions in EXTENSION_MAP.items():
        if ext in extensions:
            return category
    
    # Check name patterns
    for category, patterns in NAME_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, name, re.IGNORECASE):
                return category
    
    return "misc"


def classify_detailed(filename: str, path: str = None) -> Dict:
    """
    Get detailed classification with confidence and metadata.
    """
    name = filename.lower()
    ext = os.path.splitext(name)[1]
    base_name = os.path.splitext(name)[0]
    
    result = {
        "filename": filename,
        "extension": ext,
        "primary_class": "misc",
        "secondary_classes": [],
        "confidence": 0.5,
        "tags": [],
    }
    
    # Extension-based classification
    for category, extensions in EXTENSION_MAP.items():
        if ext in extensions:
            result["primary_class"] = category
            result["confidence"] = 0.95
            break
    
    # Add secondary classifications from name patterns
    for category, patterns in NAME_PATTERNS.items():
        for pattern in patterns:
            if re.search(pattern, name, re.IGNORECASE):
                if category != result["primary_class"]:
                    result["secondary_classes"].append(category)
                result["tags"].append(category)
    
    # Extract potential project/client names
    if "client" in result["tags"] or "session" in result["tags"]:
        # Try to extract name
        parts = re.split(r"[_\-\s]", base_name)
        if len(parts) > 1:
            result["extracted_name"] = parts[0]
    
    # Deduplicate
    result["secondary_classes"] = list(set(result["secondary_classes"]))
    result["tags"] = list(set(result["tags"]))
    
    return result


def get_file_priority(class_: str) -> int:
    """
    Get priority level for file class (for sorting/processing).
    Higher = more important.
    """
    priorities = {
        "project": 10,
        "code": 9,
        "document": 8,
        "audio": 7,
        "video": 7,
        "image": 6,
        "data": 6,
        "sample_library": 5,
        "spreadsheet": 5,
        "presentation": 5,
        "3d": 4,
        "font": 3,
        "archive": 2,
        "executable": 2,
        "backup": 1,
        "temp": 0,
        "log": 0,
        "misc": 1,
    }
    return priorities.get(class_, 1)


def should_auto_clean(class_: str, age_days: int) -> bool:
    """
    Determine if a file class should be auto-cleaned after certain age.
    """
    auto_clean_rules = {
        "temp": 7,      # Clean temp files after 7 days
        "log": 30,      # Clean logs after 30 days
        "backup": 90,   # Clean old backups after 90 days
        "cache": 3,     # Clean cache after 3 days
    }
    
    threshold = auto_clean_rules.get(class_)
    if threshold and age_days > threshold:
        return True
    return False


def get_smart_bucket(class_: str, intent: str = None) -> str:
    """
    Get the smart bucket name for organizing files.
    """
    bucket_map = {
        "audio": "Audio",
        "video": "Video",
        "image": "Images",
        "code": "Code",
        "document": "Documents",
        "project": "Projects",
        "sample_library": "Libraries",
        "data": "Data",
        "archive": "Archives",
        "client": "Clients",
        "session": "Sessions",
    }
    
    # Intent can override
    if intent:
        if intent.startswith("client:"):
            return "Clients"
        if intent.startswith("project:"):
            return "Projects"
        if intent.startswith("compute_output:"):
            return "Jobs"
    
    return bucket_map.get(class_, "Misc")

