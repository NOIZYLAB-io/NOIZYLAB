import asyncio
import time
import traceback
from typing import Any, Callable, Coroutine, Optional
from constants import cloud
import socketio
import httpx

from logger.log import logger
from ipc import IPC
from BASE.services.knowledge_bases import (
    update_knowledge_base_cloud_id,
    update_knowledge_base_sync_config,
)
import json
from BASE.services.knowledge_bases import get_knowledge_base_by_id

ipc_ = IPC.connect()


@logger.catch()
async def upload_to_cloud_functional(
    kb_metadata: dict,
    session: str,
    processed_data: list[dict],
    progress_fn: Callable[[float], Coroutine[Any, Any, Any]],
    retries: int = 10,
):
    """Sync the knowledge base to cloud and return cloud ID."""

    logger.info("Starting upload_to_cloud_functional()")
    logger.debug(f"Received kb_metadata: {json.dumps(kb_metadata, indent=2)}")
    logger.debug(f"Received session: {session}")
    logger.debug(f"Processed_data length: {len(processed_data)}")

    # Extract vectors, metadata, and ids from processed_data
    vectors, metadata, ids = [], [], []

    for i, chunk in enumerate(processed_data):
        logger.debug(f"Processing chunk {i+1}/{len(processed_data)}")
        embeddings = chunk.get("embeddings", [])
        vectors.append(embeddings)

        md = {
            "id": chunk.get("metadata", {}).get("id", ""),
            "content": chunk.get("metadata", {}).get("content", ""),
            "file": chunk.get("metadata", {}).get("file", ""),
            "name": chunk.get("metadata", {}).get("name", ""),
            "additional_metadata": chunk.get("metadata", {}).get(
                "additional_metadata", {}
            ),
        }
        metadata.append(md)
        ids.append(md["id"])

    # Get current timestamp
    upload_timestamp = int(time.time()) * 1000
    logger.debug(f"Upload timestamp: {upload_timestamp}")

    # Vector dimension check
    vector_dimensions = len(vectors[0]) if vectors and len(vectors[0]) > 0 else 0
    logger.debug(f"Vector dimensions detected: {vector_dimensions}")

    upload_bin = {
        "collection": {
            "name": kb_metadata.get("name", ""),
            "description": kb_metadata.get("description", ""),
            "timestamp": upload_timestamp,
            "data": {"vectors": vectors, "metadata": metadata, "ids": ids},
            "type": kb_metadata.get("type", "codebase"),
        },
        "config": {"vector_dimensions": vector_dimensions},
    }

    logger.info("Prepared upload_bin payload")
    # logger.debug(f"upload_bin summary: vectors={len(vectors)}, metadata={len(metadata)}, ids={len(ids)}")
    # logger.trace(f"upload_bin full: {json.dumps(upload_bin, indent=2)}")

    error = None
    while retries > 0:
        try:
            logger.info(f"Attempting upload (Retries left: {retries})")
            await progress_fn(0.0)

            async with httpx.AsyncClient(timeout=30000000.0) as client:
                logger.info(f"POST {cloud}/knowledge/upload")
                logger.info(
                    f"Headers: {{'X-Session': session, 'Content-Type': 'application/json'}}"
                )
                logger.info(
                    f"Payload size: {len(json.dumps(upload_bin)) / 1024:.2f} KB"
                )

                req = await client.post(
                    f"{cloud}/knowledge/upload",
                    json=upload_bin,
                    headers={"X-Session": session, "Content-Type": "application/json"},
                )

            logger.info(f"Response: {req}")

            res = req.json()
            logger.info(f"Response JSON parsed successfully: {res}")

            await progress_fn(95.0)
            logger.info("Upload complete")

            return res["collection_id"]

        except (httpx.ConnectError, httpx.ReadError, ConnectionResetError) as e:
            print(e)
            logger.error(f"Connection error: {e}")
            error = e
            retries -= 1
            if retries > 0:
                wait_time = 2 ** (10 - retries)  # Exponential backoff
                logger.warning(
                    f"Retrying in {wait_time} seconds... ({retries} retries left)"
                )
                time.sleep(wait_time)
            await progress_fn(0.0)

        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            error = e
            retries -= 1
            time.sleep(1)
            await progress_fn(0.0)

        await asyncio.sleep(1)

    if error:
        logger.critical(f"Upload failed after all retries. Last error: {error}")
        raise error

    logger.info("Sync to cloud complete (Exit)")


@logger.catch()
def _validate_kb_for_cloud_upload(kb_id: str) -> tuple[bool, str, Optional[dict]]:
    """
    Validate that a knowledge base can be uploaded to cloud.

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
            return (
                False,
                "Cannot upload remote knowledge bases - they are already in the cloud",
                None,
            )

        # Check if KB already has a cloud_id (already uploaded)
        cloud_id = kb.get("cloud_id")
        if cloud_id:
            return (
                False,
                f"Knowledge base already has a cloud ID. Use sync instead of upload.",
                None,
            )

        # All validations passed
        return True, "", kb

    except Exception as e:
        logger.error(f"Error validating KB for cloud upload: {e}")
        return False, f"Error validating knowledge base: {str(e)}", None


@logger.catch()
async def handle_upload_to_cloud_event(
    sio: socketio.AsyncServer, sid: str, data: dict = {}
):
    """Handle uploading an existing local knowledge base to the cloud."""

    # Extract upload data from request
    cloud_upload_data = data
    request_id = cloud_upload_data.get("request_id", "")
    kb_id = cloud_upload_data.get("kb_id", "")
    session = ipc_.get("current_session") if ipc_.get("current_session") else None

    # -----------------------------------------------------------------------------------------
    # 1. Validate Knowledge Base for Cloud Upload --------------------------------------------
    # -----------------------------------------------------------------------------------------

    is_valid, error_message, kb = _validate_kb_for_cloud_upload(kb_id)
    if not is_valid:
        logger.error(f"KB validation failed: {error_message}")
        await sio.emit(
            "upload_to_cloud:error",
            data={
                "request_id": request_id,
                "status": "error",
                "message": error_message,
            },
            to=sid,
        )
        return

    # -----------------------------------------------------------------------------------------
    # 2. Retrieve Existing Chunks from Knowledge Base ---------------------------------------
    # -----------------------------------------------------------------------------------------

    await sio.emit(
        "upload_to_cloud:progress",
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

        chunks = await get_all_chunks_from_kb(kb_id)

        if not chunks:
            raise ValueError("No chunks found in knowledge base")

    except Exception as e:
        logger.error(f"Error retrieving chunks: {e}")
        logger.error(f"Error traceback: {traceback.format_exc()}")
        await sio.emit(
            "upload_to_cloud:error",
            data={
                "request_id": request_id,
                "status": "error",
                "message": f"Failed to retrieve knowledge base chunks: {e}",
            },
            to=sid,
        )
        return

    # -----------------------------------------------------------------------------------------
    # 3. Upload to Cloud ---------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------

    logger.info("Starting upload to cloud")

    async def progress_fn(progress):
        await sio.emit(
            "upload_to_cloud:progress",
            data={
                "request_id": request_id,
                "status": "PROGRESS",
                "progress": progress,
                "message": "Uploading to cloud",
            },
            to=sid,
        )

    try:
        kb = get_knowledge_base_by_id(kb_id)
    except Exception as e:
        logger.error(f"Error retrieving knowledge base: {e}")
        await sio.emit(
            "upload_to_cloud:error",
            data={
                "request_id": request_id,
                "status": "error",
                "message": f"Failed to retrieve knowledge base: {e}",
            },
            to=sid,
        )
        return

    try:
        logger.debug(f"Syncing to cloud with session: {session}")

        cloud_id = await upload_to_cloud_functional(
            kb, session, chunks, progress_fn=progress_fn
        )

        update_knowledge_base_cloud_id(kb_id, cloud_id)

        syncConfig = {
            "enabled": True,
            "lastSynced": int(time.time()) * 1000,
        }
        update_knowledge_base_sync_config(kb_id, syncConfig)

    except Exception as e:
        await sio.emit(
            "upload_to_cloud:error",
            data={
                "request_id": request_id,
                "status": "error",
                "message": f"Failed to upload to cloud: {e}",
            },
            to=sid,
        )
        return

    # -----------------------------------------------------------------------------------------
    # 4. Report Success to the Client -------------------------------------------------------
    # -----------------------------------------------------------------------------------------

    kb_name = kb.get("name", "Unknown")
    logger.info(
        f"Cloud upload process completed successfully for knowledge base: {kb_name}"
    )
    logger.info(f"Uploaded {len(chunks)} chunks to cloud")

    # Report success to the client
    await sio.emit(
        "upload_to_cloud:success",
        data={
            "request_id": request_id,
            "status": "success",
            "message": "Knowledge base uploaded to cloud successfully",
            "data": kb,
        },
        to=sid,
    )
    logger.info(f"Success event emitted to client for request: {request_id}")
