import os
from typing import Any
import mimetypes
from logger.log import logger

# Default excluded dirs and extensions
DEFAULT_EXCLUDED_DIRS = {
    "__pycache__",
    "node_modules",
    "vendor",
    ".git",
    ".svn",
    "dist",
    ".venv",
    "build",
    "target",
    "_build",
    ".idea",
    ".vscode",
    ".terraform",
    ".gradle",
    ".dart_tool",
    ".pytest_cache",
    ".mypy_cache",
    ".next",
    ".nuxt",
    ".eggs",
    "bin",
    "obj",
    "out",
}

DEFAULT_TEXT_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".jsx",
    ".tsx",
    ".java",
    ".go",
    ".rb",
    ".cpp",
    ".c",
    ".h",
    ".hpp",
    ".cs",
    ".json",
    ".yaml",
    ".yml",
    ".md",
    ".txt",
    ".html",
    ".css",
    ".xml",
    ".sh",
    ".swift",
    ".kt",
    ".kts",
    ".rs",
    ".dart",
    ".php",
    ".pl",
    ".pm",
    ".scala",
    ".ex",
    ".exs",
    ".hs",
    ".tf",
    ".tfvars",
    ".ini",
    ".cfg",
    ".toml",
    ".sql",
}

# Heuristic caching to avoid repeated checks
heuristic_cache = {}

@logger.catch()
def get_file_size(filepath):
    """Get file size in bytes, return 0 if error"""
    try:
        return os.path.getsize(filepath)
    except OSError:
        return 0

@logger.catch()
def is_text_file(filepath):
    """Check if a file is a text file using multiple methods"""
    if os.path.isdir(filepath):
        return False

    ext = os.path.splitext(filepath)[1].lower()
    if ext in DEFAULT_TEXT_EXTENSIONS:
        return True

    mime, _ = mimetypes.guess_type(filepath)
    if mime and mime.startswith("text"):
        return True

    # Fallback: read first 512 bytes to check for binary data
    try:
        with open(filepath, "rb") as f:
            chunk = f.read(512)
            return b"\0" not in chunk
    except Exception:
        return False

@logger.catch()
def should_skip_dir(dirpath):
    """Check if a directory should be skipped using heuristics"""
    if dirpath in heuristic_cache:
        return heuristic_cache[dirpath]

    checks = [
        lambda d: os.path.isfile(os.path.join(d, "pyvenv.cfg")),
        lambda d: os.path.isdir(os.path.join(d, "conda-meta")),
        lambda d: os.path.isfile(os.path.join(d, "package.json"))
        and len(os.listdir(d)) > 20,
        lambda d: any(f.endswith(".class") for f in os.listdir(d)),
        lambda d: any(f.endswith((".dll", ".exe")) for f in os.listdir(d)),
        lambda d: os.path.isdir(os.path.join(d, "debug"))
        or os.path.isdir(os.path.join(d, "release")),
        lambda d: os.path.isfile(os.path.join(d, ".terraform.lock.hcl"))
        or os.path.isdir(os.path.join(d, ".terraform")),
    ]

    try:
        for check in checks:
            if check(dirpath):
                heuristic_cache[dirpath] = True
                return True
    except Exception:
        pass

    heuristic_cache[dirpath] = False
    return False


@logger.catch()
async def handle_get_folder_paths_recursive_event(sio, sid: str, data: dict[str, Any]):
    """Handle get_folder_paths_recursive event"""
    try:
        root_path = data["path"]
        if not os.path.exists(root_path):
            await sio.emit(
                "get_folder_paths_recursive:error",
                {"error": f"Path does not exist: {root_path}"},
                to=sid,
            )
            return

        folder_paths = []
        processed_dirs = 0
        skipped_dirs = 0

        for root, dirs, _ in os.walk(root_path):
            processed_dirs += len(dirs)
            # Remove ignored folders from dirs to prevent walking into them
            original_dir_count = len(dirs)
            dirs[:] = [d for d in dirs if d not in DEFAULT_EXCLUDED_DIRS]
            skipped_dirs += original_dir_count - len(dirs)

            # Get relative path from the input root_path
            rel_path = os.path.relpath(root, root_path).replace(os.sep, "/")
            if rel_path != ".":  # Skip the root directory
                # This is a subdirectory
                folder_paths.append(
                    {
                        "path": os.path.join(root_path, rel_path).replace(os.sep, "/"),
                        "name": rel_path,  # Using just the relative path instead of joining with root folder name
                    }
                )

        await sio.emit("get_folder_paths_recursive:response", folder_paths, to=sid)

    except Exception:
        await sio.emit(
            "get_folder_paths_recursive:error",
            {"error": "Invalid request. Expected JSON with 'path' field"},
            to=sid,
        )


@logger.catch()
async def handle_get_file_paths_recursive_event(sio, sid: str, data: dict[str, Any]):
    """Handle get_file_paths_recursive event"""
    try:
        root_path = data["path"]
        if not os.path.exists(root_path):
            await sio.emit(
                "get_file_paths_recursive:error",
                {"error": f"Path does not exist: {root_path}"},
                to=sid,
            )
            return

        all_files = []
        ignored_files = []
        root_name = os.path.basename(root_path)

        root_node = {
            "name": root_name,
            "path": "",
            "metadata": {"absolutePath": root_path},
            "children": [],
        }

        # Helper function to find or create path in tree
        def get_or_create_path(current_children, parts, current_abs_path):
            for i, part in enumerate(parts):
                existing = next(
                    (p for p in current_children if p["name"] == part), None
                )
                if existing is None:
                    new_path = "/".join(parts[: i + 1])
                    new_abs_path = os.path.join(current_abs_path, part).replace(
                        os.sep, "/"
                    )
                    existing = {
                        "name": part,
                        "path": new_path,
                        "metadata": {"absolutePath": new_abs_path},
                        "children": [],
                    }
                    current_children.append(existing)
                current_children = existing["children"]
            return current_children

        # First pass: collect files excluding forbidden folders
        for root, dirs, files in os.walk(root_path):
            # Remove forbidden directories from dirs to prevent walking into them
            dirs[:] = [d for d in dirs if d not in DEFAULT_EXCLUDED_DIRS]

            # Skip if current directory is forbidden
            if any(
                forbidden in root.split(os.sep) for forbidden in DEFAULT_EXCLUDED_DIRS
            ):
                continue

            for file in files:
                abs_file_path = os.path.join(root, file).replace(os.sep, "/")
                all_files.append(abs_file_path)
                if not is_text_file(abs_file_path):
                    ignored_files.append(abs_file_path)

        # Second pass: build tree structure excluding forbidden folders
        for root, dirs, files in os.walk(root_path):
            # Remove forbidden directories from dirs to prevent walking into them
            dirs[:] = [d for d in dirs if d not in DEFAULT_EXCLUDED_DIRS]

            # Skip if current directory is forbidden
            if any(
                forbidden in root.split(os.sep) for forbidden in DEFAULT_EXCLUDED_DIRS
            ):
                continue

            for file in files:
                # Get path relative to root
                rel_path = os.path.relpath(root, root_path)
                if rel_path == ".":
                    parts = []
                else:
                    parts = rel_path.replace(os.sep, "/").split("/")

                # Add file to tree
                current_level = root_node["children"]
                if parts:
                    current_level = get_or_create_path(current_level, parts, root_path)

                file_abs_path = os.path.join(root, file).replace(os.sep, "/")
                file_rel_path = "/".join([*parts, file]) if parts else file
                current_level.append(
                    {
                        "name": file,
                        "path": file_rel_path,
                        "metadata": {"absolutePath": file_abs_path},
                        "children": [],
                    }
                )

        # Sort function to put folders first
        def sort_nodes(nodes):
            nodes.sort(key=lambda x: (len(x["children"]) == 0, x["name"].lower()))
            for node in nodes:
                if node["children"]:
                    sort_nodes(node["children"])

        # Sort the tree
        sort_nodes(root_node["children"])

        response = {
            "value": [root_node],
            "allFiles": all_files,
            "ignoredFiles": ignored_files,
            "workspacePath": root_path.replace(os.sep, "/"),
        }

        await sio.emit("get_file_paths_recursive:response", response, to=sid)

    except Exception:
        await sio.emit(
            "get_file_paths_recursive:error",
            {"error": "Invalid request. Expected JSON with 'path' field"},
            to=sid,
        )
