import asyncio
import time
import traceback
from typing import Any, Callable, Coroutine, Optional
import socketio
import httpx
import json
from logger.log import logger
from ipc import IPC
from constants import cloud
from BASE.services.knowledge_bases import update_knowledge_base_lastSynced
ipc_ = IPC.connect()


@logger.catch()
async def _get_modified_chunks_for_sync(
    kb: dict,
    all_chunks: list[dict],
    buffer_time_ms: int = 5000  # 5 second buffer to avoid edge cases
) -> list[dict]:
    """
    Get chunks from files that have been modified since the last sync.

    Args:
        kb: The knowledge base dictionary
        all_chunks: All chunks from the knowledge base
        buffer_time_ms: Buffer time in milliseconds to avoid edge cases

    Returns:
        List of chunks from modified files only
    """
    try:
        # Get last sync timestamp
        sync_config = kb.get("syncConfig", {})
        last_synced = sync_config.get("lastSynced", 0)
        logger.info(f"Last synced timestamp: {last_synced}")
        if last_synced <= 0:
            # If never synced, return all chunks
            logger.info("Knowledge base has never been synced, returning all chunks")
            return all_chunks

        # Get file timestamps from metadata
        kb_metadata = kb.get("metadata", {})
        file_timestamps = kb_metadata.get("file_timestamps", {})
        if not file_timestamps:
            logger.warning("No file timestamps available, returning all chunks")
            return all_chunks

        # Find modified files (with buffer time)
        sync_threshold = last_synced - buffer_time_ms
        modified_files = set()

        for file_path, file_timestamp in file_timestamps.items():
            logger.debug(f"File timestamp: {file_path} - {file_timestamp}")
            if file_timestamp > sync_threshold:
                modified_files.add(file_path)


        # Log modified files

        logger.info(f"Found {len(modified_files)} modified files since last sync")
        logger.debug(f"Modified files: {list(modified_files)[:5]}...")  # Log first 5 files

        # Filter chunks to only include those from modified files
        modified_chunks = []
        for chunk in all_chunks:
            chunk_file = chunk.get("metadata", {}).get("file", "")

            if chunk_file in modified_files:
                modified_chunks.append(chunk)

        logger.info(f"Filtered to {len(modified_chunks)} chunks from modified files")
        return modified_chunks

    except Exception as e:
        logger.error(f"Error filtering modified chunks: {e}")
        logger.error(f"Error traceback: {traceback.format_exc()}")
        # On error, return all chunks to be safe
        return all_chunks


@logger.catch()
def _validate_kb_for_cloud_sync(kb_id: str) -> tuple[bool, str, Optional[dict]]:
    """
    Validate that a knowledge base can be synced to cloud.

    Returns:
        tuple: (is_valid, error_message, kb_object)
    """
    try:
        from BASE.services.knowledge_bases import get_knowledge_base_by_id

        # Check if KB exists
        kb = get_knowledge_base_by_id(kb_id)
        if not kb:
            return False, f"Knowledge base with ID {kb_id} not found", None

        # Check if KB is local (not remote)
        source = kb.get("source", "").upper()
        if source == "REMOTE":
            return False, "Cannot sync remote knowledge bases - they are already in the cloud", None

        # Check if KB has a cloud_id (required for sync)
        cloud_id = kb.get("cloud_id")
        if not cloud_id:
            return False, f"Knowledge base does not have a cloud ID. Upload to cloud first before syncing.", None

        # All validations passed
        return True, "", kb

    except Exception as e:
        logger.error(f"Error validating KB for cloud sync: {e}")
        return False, f"Error validating knowledge base: {str(e)}", None


@logger.catch()
async def handle_sync_to_cloud_event(sio: socketio.AsyncServer, sid: str, data: dict = {}):
    """Handle syncing an existing cloud knowledge base with incremental updates."""

    # Extract sync data from request
    cloud_sync_data = data
    request_id = cloud_sync_data.get("request_id", "")
    kb_id = cloud_sync_data.get("kb_id", "")
    session = ipc_.get("current_session")

    logger.info(f"Starting cloud sync process for KB: {kb_id}")

    # -----------------------------------------------------------------------------------------
    # 1. Validate Knowledge Base for Cloud Sync ----------------------------------------------
    # -----------------------------------------------------------------------------------------

    is_valid, error_message, kb = _validate_kb_for_cloud_sync(kb_id)
    if not is_valid:
        logger.error(f"KB validation failed: {error_message}")
        await sio.emit(
            "sync_to_cloud:error",
            data={
                "request_id": request_id,
                "status": "error",
                "message": error_message,
            },
            to=sid,
        )
        return

    # -----------------------------------------------------------------------------------------
    # 2. Retrieve All Chunks from Knowledge Base --------------------------------------------
    # -----------------------------------------------------------------------------------------

    await sio.emit(
        "sync_to_cloud:progress",
        data={
            "request_id": request_id,
            "status": "PROGRESS",
            "progress": 10,
            "message": "Retrieving knowledge base chunks",
        },
        to=sid,
    )

    try:

        # Get chunks from Qdrant using functional approach
        from BASE.services.knowledge_bases import get_all_chunks_from_kb
        all_chunks = await get_all_chunks_from_kb(kb_id)

        if not all_chunks:
            raise ValueError("No chunks found in knowledge base")

    except Exception as e:
        logger.error(f"Error retrieving chunks: {e}")
        logger.error(f"Error traceback: {traceback.format_exc()}")
        await sio.emit(
            "sync_to_cloud:error",
            data={
                "request_id": request_id,
                "status": "error",
                "message": f"Failed to retrieve knowledge base chunks: {e}",
            },
            to=sid,
        )
        return

    # -----------------------------------------------------------------------------------------
    # 3. Filter Chunks Based on File Timestamps (Incremental Sync) -------------------------
    # -----------------------------------------------------------------------------------------

    await sio.emit(
        "sync_to_cloud:progress",
        data={
            "request_id": request_id,
            "status": "PROGRESS",
            "progress": 30,
            "message": "Analyzing modified files for incremental sync",
        },
        to=sid,
    )

    try:
        filter_start = time.time()
        modified_chunks = await _get_modified_chunks_for_sync(kb, all_chunks)
        filter_time = time.time() - filter_start

        logger.info(
            f"Filtered to {len(modified_chunks)} modified chunks out of {len(all_chunks)} total chunks in {filter_time:.2f}s"
        )

        if not modified_chunks:
            # No modified chunks, sync is already up to date
            logger.info("No modified chunks found - knowledge base is already up to date")
            await sio.emit(
                "sync_to_cloud:success",
                data={
                    "request_id": request_id,
                    "status": "success",
                    "message": "Knowledge base is already up to date - no sync needed",
                    "data": {
                        "total_chunks": len(all_chunks),
                        "modified_chunks": 0,
                        "sync_skipped": True
                    },
                },
                to=sid,
            )
            return

    except Exception as e:
        logger.error(f"Error filtering modified chunks: {e}")
        logger.error(f"Error traceback: {traceback.format_exc()}")
        await sio.emit(
            "sync_to_cloud:error",
            data={
                "request_id": request_id,
                "status": "error",
                "message": f"Failed to analyze modified files: {e}",
            },
            to=sid,
        )
        return

    # -----------------------------------------------------------------------------------------
    # 4. Prepare Update Payload for Cloud API -----------------------------------------------
    # -----------------------------------------------------------------------------------------

    await sio.emit(
        "sync_to_cloud:progress",
        data={
            "request_id": request_id,
            "status": "PROGRESS",
            "progress": 50,
            "message": "Preparing incremental update payload",
        },
        to=sid,
    )

    try:
        # Prepare vectors, metadata, and IDs for modified chunks only
        vectors = []
        metadata = []
        ids = []

        for chunk in modified_chunks:
            embeddings = chunk.get("embeddings", [])
            vectors.append(embeddings)
            metadata.append({
                "id": chunk.get("metadata", {}).get("id", ""),
                "content": chunk.get("metadata", {}).get("content", ""),
                "file": chunk.get("metadata", {}).get("file", ""),
                "name": chunk.get("metadata", {}).get("name", ""),
                "additional_metadata": chunk.get("metadata", {}).get("additional_metadata", {}),
            })
            ids.append(chunk.get("metadata", {}).get("id", ""))


        vector_dimensions = len(vectors[0]) if vectors and len(vectors[0]) > 0 else 0

        # Create update payload with exact schema
        current_timestamp = int(time.time()) * 1000
        kb_cloud_id = kb.get("cloud_id")
        update_payload = {
            "collection_id": kb_cloud_id,
            "update_queries": {
                "vectors": vectors,
                "metadata": metadata,
                "ids": ids
            }
        }

        logger.info(f"Prepared update payload with {len(modified_chunks)} modified chunks")
        logger.debug(f"Update payload structure: collection_id={kb_cloud_id}, chunks={len(modified_chunks)}, timestamp={current_timestamp}")
        logger.debug(f"Sample chunk data: {modified_chunks[0] if modified_chunks else 'No chunks'}")
        logger.debug(f"Vectors length: {len(vectors)}, Metadata length: {len(metadata)}, IDs length: {len(ids)}")

    except Exception as e:
        logger.error(f"Error preparing update payload: {e}")
        logger.error(f"Error traceback: {traceback.format_exc()}")
        await sio.emit(
            "sync_to_cloud:error",
            data={
                "request_id": request_id,
                "status": "error",
                "message": f"Failed to prepare update payload: {e}",
            },
            to=sid,
        )
        return

    # -----------------------------------------------------------------------------------------
    # 5. Send Update Request to Cloud API ---------------------------------------------------
    # -----------------------------------------------------------------------------------------

    cloud_sync_start = time.time()
    logger.info("Starting incremental sync to cloud")

    await sio.emit(
            "sync_to_cloud:progress",
            data={
                "request_id": request_id,
                "status": "PROGRESS",
                "progress": 70,
                "message": "Syncing modified chunks to cloud",
            },
            to=sid,
    )

    try:

        # logger.info(f"Sending update payload to cloud: {json.dumps(update_payload, indent=2)}")

        # Get session for authentication
        if not session:
            raise ValueError("Session is required for cloud sync authentication")

        logger.debug(f"Syncing to cloud with session: {session}")


        async with httpx.AsyncClient(
            timeout=300.0,  # 5 minute timeout
        ) as client:
            response = await client.post(
                f"{cloud}/knowledge/update",
                json=update_payload,
                headers={
                    "X-Session": session,
                    "Content-Type": "application/json",
                },
            )


        await sio.emit(
            "sync_to_cloud:progress",
            data={
                "request_id": request_id,
                "status": "PROGRESS",
                "progress": 90,
                "message": "Waiting for cloud response",
            },
            to=sid,
        )

        # logger.info(f"Cloud sync response: {response.status_code}")

        if response.status_code != 200:
            response_data = response.json() if response.headers.get("content-type", "").startswith("application/json") else {"error": response.text}
            error_message = response_data.get("error", f"HTTP {response.status_code}")
            logger.error(f"Cloud sync failed with status {response.status_code}: {error_message}")
            logger.debug(f"Response headers: {dict(response.headers)}")
            logger.debug(f"Response body: {response.text[:1000]}...")  # Log first 1000 chars
            raise RuntimeError(f"Cloud sync failed: {error_message}")

        response_data = response.json()
        logger.info(f"Cloud sync successful: {response_data}")

        # Update lastSynced timestamp after successful sync
        update_knowledge_base_lastSynced(kb_id, current_timestamp)

        cloud_sync_time = time.time() - cloud_sync_start
        logger.info(
            f"Incremental cloud sync completed successfully in {cloud_sync_time:.2f} seconds"
        )

    except Exception as e:
        cloud_sync_time = time.time() - cloud_sync_start
        logger.error(f"ERROR FROM incremental sync_to_cloud after {cloud_sync_time:.2f}s: {e}")
        logger.error(f"Cloud sync error traceback: {traceback.format_exc()}")
        await sio.emit(
            "sync_to_cloud:error",
            data={
                "request_id": request_id,
                "status": "error",
                "message": f"Failed to sync to cloud: {e}",
            },
            to=sid,
        )
        return

    # -----------------------------------------------------------------------------------------
    # 6. Report Success to the Client -------------------------------------------------------
    # -----------------------------------------------------------------------------------------

    kb_name = kb.get("metadata", {}).get("name", "Unknown")
    logger.info(
        f"Incremental cloud sync process completed successfully for knowledge base: {kb_name}"
    )
    logger.info(f"Synced {len(modified_chunks)} modified chunks out of {len(all_chunks)} total chunks")

    # Report success to the client
    await sio.emit(
        "sync_to_cloud:success",
        data={
            "request_id": request_id,
            "status": "success",
            "message": "Knowledge base synced to cloud successfully",
            "data": {
                "total_chunks": len(all_chunks),
                "modified_chunks": len(modified_chunks),
                "sync_time_seconds": cloud_sync_time,
                "last_synced": current_timestamp * 1000,
                "kb_data": kb
            },
        },
        to=sid,
    )
    logger.info(
        f"Success event emitted to client for request: {request_id}"
    )