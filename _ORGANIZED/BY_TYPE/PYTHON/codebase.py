import os
import time
from concurrent.futures import Future, ThreadPoolExecutor
from itertools import chain
from typing import Any, Callable, Coroutine, Optional

from BASE.utils.files import get_files

from .utils import make_chunks_from_file


def get_files_needing_update_simple(
    files: list[str], file_timestamps: dict
) -> list[str]:
    """Simple implementation to check which files need updating based on timestamps."""
    files_needing_update = []
    for file_path in files:
        if not os.path.exists(file_path):
            continue
        try:
            current_mtime = os.path.getmtime(file_path)
            stored_timestamp = file_timestamps.get(file_path, 0)
            if current_mtime > stored_timestamp:
                files_needing_update.append(file_path)
        except OSError:
            # If we can't get the timestamp, include the file for processing
            files_needing_update.append(file_path)
    return files_needing_update


def cleanup_stale_timestamps_simple(
    file_timestamps: dict, current_files: list[str]
) -> dict:
    """Remove timestamps for files that no longer exist."""
    current_files_set = set(current_files)
    return {
        path: timestamp
        for path, timestamp in file_timestamps.items()
        if path in current_files_set
    }


def update_timestamps_simple(files: list[str]) -> dict:
    """Update timestamps for successfully processed files."""
    updated_timestamps = {}
    for file_path in files:
        try:
            if os.path.exists(file_path):
                updated_timestamps[file_path] = os.path.getmtime(file_path)
        except OSError:
            pass
    return updated_timestamps


async def process_codebase_chunks(
    files: list[str],
    file_timestamps: dict | None = None,
    progress_callback: Callable[[float], Coroutine[Any, Any, Any]] | None = None,
    file_metadata: str | None = None,
) -> list[dict]:
    """Process codebase files and return chunks as simple dictionaries."""
    if file_timestamps is None:
        file_timestamps = {}

    # print("Processing codebase type knowledge base")
    # print(f"Found {len(files)} files for codebase processing")

    MAX_SIZE = 1 * 1024 * 1024  # 1MB in bytes

    filtered_files_info = get_files({"files": files})
    selected_files = [
        f["path"] for f in filtered_files_info if f.get("size", 0) <= MAX_SIZE
    ]

    # Save selected files to files_after.txt
    # with open("files_after.txt", "w", encoding="utf-8") as f:
    #     for file in selected_files:
    #         f.write(file + "\n")
    # print(f"Saved {len(selected_files)} selected files to files_after.txt")

    # Clean up stale timestamps for files that no longer exist
    # print("Cleaning up stale timestamp entries")
    file_timestamps = cleanup_stale_timestamps_simple(file_timestamps, selected_files)

    # Check which files need to be updated based on timestamps
    # print("Checking files for timestamp-based updates")
    files_needing_update = get_files_needing_update_simple(
        selected_files, file_timestamps
    )

    if not files_needing_update:
        print("No files need updating based on timestamps - skipping chunking")
        return []

    # 🔹 Write files needing update to `files_before.txt`
    # with open("files_before.txt", "w", encoding="utf-8") as f:
    #     for file in files_needing_update:
    #         f.write(file + "\n")
    # print(f"Saved {len(files_needing_update)} files to files_before.txt")

    # print(f"Found {len(files_needing_update)} files needing updates out of {len(files)} total files")

    # Log file type distribution for files that need updating
    file_extensions = {}
    total_size = 0
    for file_path in files_needing_update:
        ext = os.path.splitext(file_path)[1] or "no_extension"
        file_extensions[ext] = file_extensions.get(ext, 0) + 1
        try:
            total_size += os.path.getsize(file_path)
        except OSError:
            pass

    # print(f"File distribution for updates: {dict(sorted(file_extensions.items()))}")
    # print(f"Total size of files to update: {total_size / 1024 / 1024:.2f} MB")

    try:
        chunking_phase_start = time.time()
        # print("Starting chunk creation phase")

        MAX_WORKERS = int((os.cpu_count() or 1 / 0.4) * 0.4)
        chunks_by_file = {}
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            chunk_futures = {}
            # Dispatch futures only for files that need updating
            dispatch_start = time.time()
            # print("Dispatching chunk creation tasks to thread pool")
            for file in files_needing_update:
                print(f"Dispatching chunk creation for file: {file}")
                chunk_futures[file] = executor.submit(make_chunks_from_file, file)
            dispatch_time = time.time() - dispatch_start
            # print(f"Dispatched {len(chunk_futures)} chunk creation tasks in {dispatch_time:.2f}s")

            # Collect the results and update timestamps for successfully processed files
            collection_start = time.time()
            completed_files = 0
            successfully_processed_files = []

            for i, (file, chunk_future) in enumerate(chunk_futures.items()):
                file_start = time.time()
                try:
                    # Wait for the future to complete
                    chunks_by_file[file] = chunk_future.result()
                    file_time = time.time() - file_start
                    completed_files += 1
                    successfully_processed_files.append(file)

                    file_chunk_count = len(chunks_by_file[file])
                    # print(f"Completed chunking for file {completed_files}/{len(chunk_futures)}: {file} "
                    #   f"({file_chunk_count} chunks, took {file_time:.2f}s)")
                except Exception as e:
                    print(f"Error processing file '{file}': {e}")
                    chunks_by_file[file] = []  # Empty list for failed files

                progress = i / len(chunk_futures) * 100
                # print(f"Progress: {progress:.2f}%")
                if progress_callback:
                    await progress_callback(progress)

            collection_time = time.time() - collection_start
            # print(f"Chunk collection completed in {collection_time:.2f} seconds")

        # Update timestamps for successfully processed files
        # print("Updating timestamps for successfully processed files")
        updated_timestamps = update_timestamps_simple(successfully_processed_files)
        # print(f"Updated timestamps for {len(updated_timestamps)} files")

        # Flatten chunks from all files
        all_chunks = list(chain(*chunks_by_file.values()))

        # Add file metadata to each chunk if provided
        if file_metadata:
            for chunk in all_chunks:
                chunk["metadata"]["file"] = file_metadata

        total_chunks = len(all_chunks)
        chunking_phase_time = time.time() - chunking_phase_start

        # print(f"Chunk creation completed. Total chunks created: {total_chunks} in {chunking_phase_time:.2f}s")

        if total_chunks == 0:
            print(
                "No chunks found after processing files - this may be expected if no files needed updates"
            )
            return []

        # Log chunking statistics
        files_with_chunks = sum(
            1 for chunks_list in chunks_by_file.values() if len(chunks_list) > 0
        )
        files_without_chunks = len(chunks_by_file) - files_with_chunks
        avg_chunks_per_file = (
            total_chunks / files_with_chunks if files_with_chunks > 0 else 0
        )

        # print(f"Chunking stats - Files with chunks: {files_with_chunks}, "
        #       f"Files without chunks: {files_without_chunks}, "
        #       f"Avg chunks per file: {avg_chunks_per_file:.1f}")

        # print(f"Updated timestamps for {len(successfully_processed_files)} successfully processed files")

        return all_chunks

    except Exception as e:
        print(f"Error processing files: {e}")
        return []