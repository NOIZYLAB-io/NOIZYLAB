"""
GitHub Repository Chunker with Enhanced Git Control Integration

This module provides functionality to clone GitHub repositories and process
them into chunks for knowledge base creation. It has been enhanced to use
the centralized git control module for improved authentication support,
cross-platform compatibility, and better error handling.

Features:
- Support for both public and private repositories
- Automatic authentication token detection and usage
- Cross-platform compatibility (Windows, Linux, macOS)
- Graceful fallback to simple git clone when git control is unavailable
- Maintains backward compatibility with existing API
"""

from itertools import chain
import os
import uuid
import time
import asyncio
from concurrent.futures import ThreadPoolExecutor, Future
from typing import Any, Callable, Coroutine, Optional

from .utils import make_chunks_from_file

# Try to import git control module for enhanced functionality
try:
    from BASE.gitcontrol import GitControl, GitControlError
    GIT_CONTROL_AVAILABLE = True
except ImportError:
    GIT_CONTROL_AVAILABLE = False
    GitControl = None
    GitControlError = Exception


def get_auth_token_for_repo(repo_url: str) -> Optional[str]:
    """Get authentication token for repository URL from git control config."""
    if not GIT_CONTROL_AVAILABLE:
        return None

    try:
        gc = GitControl()
        provider = gc._get_provider_from_url(repo_url)
        if provider:
            token = gc.config.get_token(provider)
            if token:
                print(f"Found authentication token for {provider}")
                return token
        return None
    except Exception as e:
        print(f"Could not retrieve authentication token: {e}")
        return None


async def clone_repository_enhanced(repo_url: str, target_path: str, token: Optional[str] = None) -> bool:
    """Enhanced repository cloning using git control module with fallback."""
    if GIT_CONTROL_AVAILABLE:
        try:
            print(f"Using enhanced git control for cloning: {repo_url}")
            gc = GitControl()

            # Run git control clone in thread pool to maintain async compatibility
            loop = asyncio.get_event_loop()
            clone_start = time.time()

            success = await loop.run_in_executor(
                None,
                gc.clone_repository,
                repo_url,
                target_path,
                None,  # branch (use default)
                token   # authentication token
            )

            clone_time = time.time() - clone_start

            if success:
                print(f"Git repository cloned successfully using git control in {clone_time:.2f} seconds to {target_path}")
                return True
            else:
                print("Git control clone failed, falling back to simple clone")
                # Fall through to simple clone

        except GitControlError as e:
            print(f"Git control error: {e}, falling back to simple clone")
            # Fall through to simple clone
        except Exception as e:
            print(f"Unexpected error with git control: {e}, falling back to simple clone")
            # Fall through to simple clone

    # Fallback to original simple implementation
    return await clone_repository_simple(repo_url, target_path)


async def clone_repository_simple(repo_url: str, target_path: str) -> bool:
    """Simple repository cloning function."""
    print(f"Repository will be cloned to: {target_path}")
    try:
        clone_command = ["git", "clone", repo_url, target_path]
        print(f"Executing git clone command: {' '.join(clone_command)}")

        clone_start = time.time()
        process = await asyncio.create_subprocess_exec(
            *clone_command,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        clone_time = time.time() - clone_start

        if process.returncode == 0:
            print(f"Git repository cloned successfully in {clone_time:.2f} seconds to {target_path}")
            return True
        else:
            error_output = stderr.decode() if stderr else "No error output"
            print(f"Error cloning repository. Return code: {process.returncode}")
            print(f"Command error: {error_output}")

            if "git" in error_output.lower() and "not found" in error_output.lower():
                raise RuntimeError("Git CLI not found. Please install Git.")
            else:
                raise RuntimeError(f"Error cloning repository: {error_output}")

    except Exception as e:
        print(f"Error cloning repository: {e}")
        raise RuntimeError(f"Error cloning repository: {e}")


def discover_files_simple(repo_dir: str) -> list[str]:
    """Simple file discovery function."""
    file_discovery_start = time.time()
    files = []

    # Simple recursive file discovery
    for root, dirs, filenames in os.walk(repo_dir):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            files.append(file_path)

    file_discovery_time = time.time() - file_discovery_start
    print(f"Found {len(files)} files in cloned repository (discovery took {file_discovery_time:.2f}s)")

    # Calculate repository size
    repo_size = 0
    for file_path in files:
        try:
            repo_size += os.path.getsize(file_path)
        except OSError:
            pass
    print(f"Repository size: {repo_size / 1024 / 1024:.2f} MB")

    return files


async def process_github_chunks(
    repo_url: str,
    target_dir: str,
    progress_callback: Callable[[float], Coroutine[Any, Any, Any]] | None = None,
    token: Optional[str] = None,
) -> list[dict]:

    """
    Process GitHub repository and return chunks as simple dictionaries.

    This function now supports both public and private repositories through
    the git control module integration. It will automatically detect and use
    authentication tokens when available, falling back to simple git clone
    for public repositories or when git control is not available.

    Args:
        repo_url: GitHub repository URL (https or git format)
        target_dir: Directory where repository will be cloned
        progress_callback: Optional callback for progress updates
        token: Optional authentication token (auto-detected if not provided)

    Returns:
        List of chunk dictionaries ready for embedding
    """
    print("Processing Github type knowledge base")

    # Create unique target path
    target_path = os.path.join(target_dir, str(uuid.uuid4()))

    # Get authentication token if not provided
    if token is None:
        token = get_auth_token_for_repo(repo_url)

    # Clone repository using enhanced method
    await clone_repository_enhanced(repo_url, target_path, token)

    # Discover files
    files = discover_files_simple(target_path)

    print(f"Found {len(files)} files for github processing")

    # Log file type distribution
    file_extensions = {}
    total_size = 0
    for file_path in files:
        ext = os.path.splitext(file_path)[1] or "no_extension"
        file_extensions[ext] = file_extensions.get(ext, 0) + 1
        try:
            total_size += os.path.getsize(file_path)
        except OSError:
            pass

    print(f"File distribution: {dict(sorted(file_extensions.items()))}")
    print(f"Total github size: {total_size / 1024 / 1024:.2f} MB")

    try:
        chunking_phase_start = time.time()
        print("Starting chunk creation phase")

        MAX_WORKERS = int(os.cpu_count() * 0.4)
        chunks_by_file = {}
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            chunk_futures = {}
            # Dispatch all the futures
            dispatch_start = time.time()
            print("Dispatching chunk creation tasks to thread pool")
            for file in files:
                chunk_futures[file] = executor.submit(make_chunks_from_file, file)
            dispatch_time = time.time() - dispatch_start
            print(f"Dispatched {len(chunk_futures)} chunk creation tasks in {dispatch_time:.2f}s")

            # Collect the results
            collection_start = time.time()
            completed_files = 0
            for i, (file, chunk_future) in enumerate(chunk_futures.items()):
                file_start = time.time()
                # Wait for the future to complete
                chunks_by_file[file] = chunk_future.result()
                file_time = time.time() - file_start
                completed_files += 1

                file_chunk_count = len(chunks_by_file[file])
                # print(f"Completed chunking for file {completed_files}/{len(chunk_futures)}: {file} "
                    #   f"({file_chunk_count} chunks, took {file_time:.2f}s)")

                progress = i / len(chunk_futures) * 100
                # print(f"Progress: {progress:.2f}%")
                if progress_callback:
                    await progress_callback(progress)

            collection_time = time.time() - collection_start
            print(f"Chunk collection completed in {collection_time:.2f} seconds")

        total_chunks = len(list(chain(*chunks_by_file.values())))
        chunking_phase_time = time.time() - chunking_phase_start

        print(f"Chunk creation completed. Total chunks created: {total_chunks} in {chunking_phase_time:.2f}s")

        if total_chunks == 0:
            print("No chunks found after processing all files")
            return []

        # Log chunking statistics
        files_with_chunks = sum(
            1 for chunks_list in chunks_by_file.values() if len(chunks_list) > 0
        )
        files_without_chunks = len(chunks_by_file) - files_with_chunks
        avg_chunks_per_file = (
            total_chunks / files_with_chunks if files_with_chunks > 0 else 0
        )

        print(f"Chunking stats - Files with chunks: {files_with_chunks}, "
              f"Files without chunks: {files_without_chunks}, "
              f"Avg chunks per file: {avg_chunks_per_file:.1f}")

        return list(chain(*chunks_by_file.values()))

    except Exception as e:
        print(f"Error processing files: {e}")
        return []
