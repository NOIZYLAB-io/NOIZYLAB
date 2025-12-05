import asyncio
import time
import uuid
from typing import Any, Callable, Coroutine, Optional
import socketio

from BASE.embeddings.embeddings import generate_embeddings_cloud, EmbeddingServiceError
from BASE.chunkers.codebase import process_codebase_chunks
from BASE.chunkers.github import process_github_chunks
from BASE.chunkers.docs import process_docs_chunks
from BASE.chunkers.swagger import process_swagger_chunks
from BASE.chunkers.utils import make_chunks_from_file, make_chunks_from_content
from BASE.chunkers import create_chunk_metadata, create_chunk
from BASE.services.knowledge_bases import exists_knowledge_base_by_path, from_chunks
from logger.log import logger
import json
from startup_config import add_file_path
from typing import AsyncGenerator, Callable, Coroutine, Optional

from ipc import IPC

ipc_ = IPC.connect()


@logger.catch()
async def make_chunks_functional(
    upload_data: dict,
    progress_fn: Callable[[float], Coroutine[Any, Any, Any]],
    error_fn: Callable[[str], Coroutine[Any, Any, Any]],
) -> Optional[list[dict]]:
    """Create chunks using functional chunkers based on upload type."""
    await progress_fn(1)

    # logger.info(f"upload_data: {upload_data}")

    kb_type = upload_data.get("type", "")
    metadata = upload_data.get("metadata", {})
    # logger.info(f"Starting chunking process for knowledge base type: {kb_type}")

    if kb_type == "codebase":
        files = metadata.get("files", [])
        file_timestamps = metadata.get("file_timestamps", {})
        file_metadata = metadata.get("file", "")  # Extract file metadata
        # logger.info(f"Processing {len(files)} codebase files")
        return await process_codebase_chunks(
            files, file_timestamps, progress_fn, file_metadata
        )
    elif kb_type == "git":
        repo_url = metadata.get("repo_url", "")
        target_dir = metadata.get("target_dir", "/tmp/repos")
        # logger.info(f"Processing Github repository: {repo_url}")
        return await process_github_chunks(repo_url, target_dir, progress_fn)
    elif kb_type == "docs":
        urls = metadata.get("urls", [])
        # logger.info(f"Processing {len(urls)} documentation URLs")
        return await process_docs_chunks(urls, progress_fn)
    elif kb_type == "swagger":
        endpoints = metadata.get("endpoints", [])
        base_path = metadata.get("base_path", "/tmp/swagger")
        # logger.info(f"Processing {len(endpoints)} Swagger endpoints")
        return await process_swagger_chunks(endpoints, base_path, progress_fn
        )
    elif kb_type == "DirectFiles":
        files = metadata.get("files", [])
        # logger.info(f"Processing {len(files)} directly uploaded files")
        return await process_direct_files(files, progress_fn, error_fn)
    else:
        logger.error(f"Unknown knowledge base type: {kb_type}")
        await error_fn(f"Unknown knowledge base type: {kb_type}")
        return None



from typing import AsyncGenerator, Callable, Any
import asyncio, time

@logger.catch()
async def fill_embeddings_functional(
    chunks: list[dict],
    progress_fn: Callable[[float], Any],
    error_fn: Callable[[str], Any],
) -> AsyncGenerator[list[dict], None]:
    """
    Generate embeddings for chunks in batches.
    - Runs batches concurrently (up to MAX_CONCURRENT_BATCHES).
    - Reports progress as chunks complete.
    - Yields each processed batch immediately instead of returning all at once.
    """

    print(f"inside fill_embeddings_functional: {len(chunks)} chunks to process")

    if not chunks:
        logger.error("No chunks found for embedding generation")
        await error_fn("No chunks found")
        return

    # logger.info(f"Starting embedding generation for {len(chunks)} chunks")

    completed_chunks = 0
    BATCH_SIZE = 10
    MAX_CONCURRENT_BATCHES = 20

    # Semaphore to limit concurrent batches
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_BATCHES)

    async def process_batch(batch: list[dict], batch_index: int) -> list[dict]:
        nonlocal completed_chunks
        async with semaphore:
            try:
                contents = [chunk["metadata"]["content"] for chunk in batch]
                # logger.debug(f"Processing batch {batch_index} with {len(contents)} chunks")

                embeddings = await generate_embeddings_cloud(batch=True, texts=contents)

                for chunk, embedding in zip(batch, embeddings):
                    chunk["embeddings"] = embedding
                    completed_chunks += 1
                    await progress_fn(completed_chunks / len(chunks) * 100)

                return batch  # return processed batch for yielding

            except EmbeddingServiceError as e:
                logger.error(f"Embedding service error in batch {batch_index}: {e.message}")
                await error_fn(f"Embedding service failed: {e.message}")
                raise
            except Exception as e:
                logger.error(f"Unexpected error in batch {batch_index}: {e}")
                await error_fn(f"Unexpected error: {str(e)}")
                raise

    embedding_phase_start = time.time()
    num_batches = (len(chunks) + BATCH_SIZE - 1) // BATCH_SIZE
    # logger.info(f"Total {num_batches} batches (size={BATCH_SIZE}), max {MAX_CONCURRENT_BATCHES} concurrent")

    tasks = [
        asyncio.create_task(process_batch(chunks[i:i+BATCH_SIZE], i // BATCH_SIZE))
        for i in range(0, len(chunks), BATCH_SIZE)
    ]

    try:
        for coro in asyncio.as_completed(tasks):
            batch = await coro
            yield batch  # yield each completed batch immediately

    except Exception as e:
        logger.error(f"Embedding generation aborted: {e}")
        return

    total_time = time.time() - embedding_phase_start
    avg_time = total_time / len(chunks)
    # logger.info(
    #     f"Embedding generation completed: {len(chunks)} chunks in {total_time:.2f}s "
    #     f"(avg {avg_time:.3f}s per chunk)"
    # )




@logger.catch()
async def process_direct_files(
    files: list[dict],
    progress_fn: Callable[[float], Coroutine[Any, Any, Any]],
    error_fn: Callable[[str], Coroutine[Any, Any, Any]],
) -> Optional[list[dict]]:
    """
    Process files directly uploaded by the user.

    Args:
        files: List of file dictionaries with structure:
            {
                "name": str,
                "content": str,
                "path": str (optional)
            }
        progress_fn: Progress callback function
        error_fn: Error callback function

    Returns:
        List of chunk dictionaries
    """
    if not files:
        logger.warning("No files provided for processing")
        await error_fn("No files provided")
        return None

    logger.info(f"Processing {len(files)} directly uploaded files")

    all_chunks = []
    processed_files = 0

    for file_data in files:
        try:
            file_name = file_data.get("name", "unknown_file")
            file_content = file_data.get("content", "")
            file_path = file_data.get("path", file_name)

            if not file_content:
                logger.warning(f"Skipping empty file: {file_name}")
                continue

            logger.debug(f"Processing file: {file_name}")

            # Determine file extension for language detection
            file_extension = ""
            if "." in file_name:
                file_extension = file_name.split(".")[-1]

            # Create chunks from content
            chunks = make_chunks_from_content(file_content, file_extension)

            # Update chunk metadata with file information
            for chunk in chunks:
                chunk["metadata"]["file"] = file_path
                chunk["metadata"][
                    "name"
                ] = f"{file_name}:{chunk['metadata'].get('additional_metadata', {}).get('line_start', 1)}-{chunk['metadata'].get('additional_metadata', {}).get('line_end', 1)}"

            all_chunks.extend(chunks)
            processed_files += 1

            # Report progress
            progress = (processed_files / len(files)) * 100
            await progress_fn(progress)

            logger.debug(f"Created {len(chunks)} chunks from file: {file_name}")

        except Exception as e:
            logger.error(
                f"Error processing file {file_data.get('name', 'unknown')}: {e}"
            )
            await error_fn(f"Error processing file: {str(e)}")
            continue

    logger.info(
        f"Successfully processed {processed_files} files, created {len(all_chunks)} total chunks"
    )
    return all_chunks






@logger.catch()
async def handle_upload_event(sio: socketio.AsyncServer, sid: str, data: dict = {}):
    """Handle upload events using functional programming approach with streaming embeddings."""


    # Extract upload data from the request
    upload_data = data
    # print(f"upload data in upload kb: {json.dumps(upload_data, indent=2)}")

    request_id = upload_data.get("request_id", "")
    kb_name = upload_data.get("name", "")
    kb_type = upload_data.get("type", "")
    metadata = upload_data.get("metadata", {})

    # Path-based duplicate checking and processing state management for codebase type
    kb_path = None
    if kb_type == "codebase":
        kb_path = metadata.get("path", "")
        logger.info(f"kb_path: {kb_path}")
        
        # Check if already exists in database
        exists = exists_knowledge_base_by_path(kb_path)
        if kb_path and exists:
            logger.error(f"Knowledge base with path '{kb_path}' already exists")
            await sio.emit(
                "upload:error",
                data={
                    "request_id": request_id,
                    "status": "error",
                    "message": f"A knowledge base with path '{kb_path}' already exists.",
                },
                to=sid,
            )
            return
        
        # Check if currently being processed using IPC
        processing_paths = ipc_.get("processing_paths") if ipc_.get("processing_paths") else {}
        if kb_path and kb_path in processing_paths:
            logger.error(f"Knowledge base with path '{kb_path}' is currently being processed")
            await sio.emit(
                "upload:error",
                data={
                    "request_id": request_id,
                    "status": "error",
                    "message": f"A knowledge base with path '{kb_path}' is currently being processed.",
                },
                to=sid,
            )
            return
        
        # Add to processing state
        if kb_path:
            processing_paths[kb_path] = {
                "status": "processing",
                "started_at": int(time.time() * 1000),
                "request_id": request_id,
                "sid": sid
            }
            ipc_.set("processing_paths", processing_paths)
            logger.info(f"Added path '{kb_path}' to processing state via IPC")

    try:
        if kb_type == "docs":
            await sio.emit(
                    to=sid,
                    event="upload:progress",
                    data={
                        "request_id": request_id,
                        "status": "PROGRESS",
                        # "progress": 1,
                        "message": "Scraping documents",
                    },
                ),

        # Step 1: Chunking
        async def step_1_chunking():
            return await make_chunks_functional(
                upload_data,
                progress_fn=lambda progress: sio.emit(
                    to=sid,
                    event="upload:progress",
                    data={
                        "request_id": request_id,
                        "status": "PROGRESS",
                        "progress": progress,
                        "message": "(1/3) Chunking files",
                    },
                ),
                error_fn=lambda message: sio.emit(
                    to=sid,
                    event="upload:error",
                    data={
                        "request_id": request_id,
                        "status": "error",
                        "message": message,
                    },
                ),
            )

        logger.info("Starting step 1: Chunking files")
        chunks = await step_1_chunking()
        if chunks is None:
            logger.error("No chunks returned from chunking step")
            return
        logger.info(f"Step 1 completed. Generated {len(chunks)} chunks")

        # Add Option 1 check here
        if not chunks:
            logger.error("No valid chunks found for embeddings, aborting upload")
            await sio.emit(
                to=sid,
                event="upload:error",
                data={
                    "request_id": request_id,
                    "status": "error",
                    "message": "No valid chunks found for embeddings",
                },
            )
            return

        # -----------------------------------------------------------------------------------------
        # Step 2 + Step 3 (stream embeddings directly into from_chunks)
        # -----------------------------------------------------------------------------------------
        logger.info("Starting step 2: Generating embeddings & storing in Qdrant")

        # Prepare metadata
        kb_id = str(uuid.uuid4())
        complete_metadata = {
            "id": kb_id,
            "cloud_id": None,
            "name": kb_name,
            "description": upload_data.get("description", ""),
            "type": kb_type,
            "source": upload_data.get("source", "Local"),
            "scope": upload_data.get("scope", "personal"),
            "syncConfig": {
                "enabled": upload_data.get("syncConfig", {}).get("enabled", False),
                "lastSynced": upload_data.get("syncConfig", {}).get("lastSynced", 0),
            },
            "isAutoIndexed": upload_data.get("isAutoIndexed", False),
            "metadata": None,
            "status": "ready",
        }

        if kb_type == "codebase":
            files = metadata.get("files", [])
            file_timestamps = metadata.get("file_timestamps", {})
            if not file_timestamps and files:
                current_timestamp = int(time.time() * 1000)
                file_timestamps = {file_path: current_timestamp for file_path in files}
            complete_metadata["metadata"] = {
                "path": metadata.get("path", ""),
                "files": files,
                "file_timestamps": file_timestamps,
            }
        elif kb_type == "git":
            complete_metadata["metadata"] = {
                "repo_url": metadata.get("repo_url", ""),
                "branch": metadata.get("branch", ""),
                "accessToken": metadata.get("accessToken"),
            }
        elif kb_type == "docs":
            complete_metadata["metadata"] = {"urls": metadata.get("urls", [])}
        elif kb_type == "swagger":
            complete_metadata["metadata"] = {
                "endpoints": metadata.get("endpoints", []),
                "source_type": metadata.get("source_type", ""),
                "source_value": metadata.get("source_value", ""),
            }

        # instead of collecting all, stream directly
        kb_result = await from_chunks(
            metadata=complete_metadata,
            chunks_iterable=fill_embeddings_functional(
                chunks,
                progress_fn=lambda progress: sio.emit(
                    to=sid,
                    event="upload:progress",
                    data={
                        "request_id": request_id,
                        "status": "PROGRESS",
                        "progress": progress,
                        "message": "(2/3) Generating embeddings",
                    },
                ),
                error_fn=lambda message: sio.emit(
                    to=sid,
                    event="upload:error",
                    data={
                        "request_id": request_id,
                        "status": "error",
                        "message": message,
                    },
                ),
            ),
        )

        # Add to persistent storage only after successful processing
        if kb_type == "codebase":
            add_file_path(complete_metadata["metadata"]["path"])

        # Report success
        await sio.emit(
            event="upload:success",
            to=sid,
            data={
                "request_id": request_id,
                "status": "success",
                "message": "Knowledgebase prepared",
                "data": kb_result,
            },
        )
        logger.info(f"Success event emitted for request {request_id}")

    except Exception as e:
        logger.error(f"Failed to create knowledge base: {e}")
        await sio.emit(
            to=sid,
            event="upload:error",
            data={
                "request_id": request_id,
                "status": "error",
                "message": f"Failed to create knowledge base: {str(e)}",
            },
        )
    finally:
        # Always remove from processing state when done (success or failure)
        if kb_type == "codebase" and kb_path:
            processing_paths = ipc_.get("processing_paths") if ipc_.get("processing_paths") else {}
            if kb_path in processing_paths:
                del processing_paths[kb_path]
                ipc_.set("processing_paths", processing_paths)
                logger.info(f"Removed path '{kb_path}' from processing state via IPC")
