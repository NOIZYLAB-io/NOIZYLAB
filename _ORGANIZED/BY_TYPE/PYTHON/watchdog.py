import time
import traceback
from datetime import datetime, timezone
from typing import List

from logger.log import logger
from BASE.utils.path_selector import validate_file_path
from BASE.services.knowledge_bases import (
    find_kbs_containing_file,
    delete_file_chunks_from_kb,
    process_file_chunks,
    insert_chunks_to_kb,
    update_kb_file_timestamp
)
from BASE.embeddings.embeddings import generate_embeddings_cloud, EmbeddingServiceError


# Utility functions for watchdog-specific operations






@logger.catch()
async def generate_embeddings_for_chunks(chunks: List[dict]) -> None:
    """Generate embeddings for all chunks using cloud embeddings"""
    try:
        logger.debug(f"[EMBEDDING_GEN] Starting embedding generation for {len(chunks)} chunks using cloud embeddings")

        # Prepare content for batch embedding generation
        contents = []
        chunks_needing_embeddings = []

        for i, chunk in enumerate(chunks):
            if not chunk.get("embeddings"):  # Only generate if not already present
                content = chunk["metadata"].get("content", "")
                if content:
                    contents.append(content)
                    chunks_needing_embeddings.append(i)
                    logger.debug(f"[EMBEDDING_GEN] Chunk {i+1}/{len(chunks)} needs embedding - ID: {chunk['metadata'].get('id')}")
                else:
                    logger.warning(f"[EMBEDDING_GEN] Chunk {i+1}/{len(chunks)} has no content - ID: {chunk['metadata'].get('id')}")
            else:
                logger.debug(f"[EMBEDDING_GEN] Chunk {i+1}/{len(chunks)} already has embeddings - ID: {chunk['metadata'].get('id')}")

        if contents:
            logger.info(f"[EMBEDDING_GEN] Generating embeddings for {len(contents)} chunks using cloud service")
            try:
                embeddings = await generate_embeddings_cloud(batch=True, texts=contents)

                # Assign embeddings back to chunks
                for i, embedding in enumerate(embeddings):
                    chunk_index = chunks_needing_embeddings[i]
                    chunks[chunk_index]["embeddings"] = embedding
                    logger.debug(f"[EMBEDDING_GEN] Assigned embedding to chunk {chunk_index+1}")

                logger.info(f"[EMBEDDING_GEN] Generated embeddings for {len(contents)}/{len(chunks)} chunks")
            except EmbeddingServiceError as e:
                logger.error(f"[EMBEDDING_GEN] Embedding service error: {e.message}")
                # Don't raise the error, just log it and continue without embeddings
                logger.warning(f"[EMBEDDING_GEN] Continuing without embeddings due to service unavailability")
                return

    except Exception as e:
        logger.error(f"[EMBEDDING_GEN] Error generating embeddings: {e}")
        raise


@logger.catch()
async def update_single_kb(kb_data: dict, file_path: str) -> dict:
    """Update a single knowledge base with the modified file"""
    kb_start_time = time.time()
    chunks_deleted = 0
    chunks_created = 0
    error = None
    status = "failed"
    kb_id = kb_data["id"]
    kb_name = kb_data.get("name", "Unknown")

    try:
        logger.info(f"[KB_UPDATE] Starting update of KB '{kb_name}' (ID: {kb_id}) for file '{file_path}'")

        # Step 1: Delete existing chunks
        logger.debug(f"[KB_UPDATE] Step 1/4: Deleting existing chunks for file '{file_path}' from KB '{kb_name}'")
        chunks_deleted = await delete_file_chunks_from_kb(kb_data, file_path)

        # Step 2: Process file into new chunks
        logger.debug(f"[KB_UPDATE] Step 2/4: Processing file '{file_path}' into chunks for KB '{kb_name}'")
        new_chunks = await process_file_chunks(file_path, kb_data)

        # Step 3: Generate embeddings
        logger.debug(f"[KB_UPDATE] Step 3/4: Generating embeddings for {len(new_chunks)} chunks in KB '{kb_name}'")
        await generate_embeddings_for_chunks(new_chunks)

        # Step 4: Insert new chunks
        logger.debug(f"[KB_UPDATE] Step 4/5: Inserting {len(new_chunks)} new chunks into KB '{kb_name}'")
        await insert_chunks_to_kb(kb_data, new_chunks)

        # Step 5: Update file timestamp in metadata
        logger.debug(f"[KB_UPDATE] Step 5/5: Updating file timestamp in metadata for KB '{kb_name}'")
        await update_kb_file_timestamp(kb_data, file_path, "update")

        chunks_created = len(new_chunks)
        status = "success"

        logger.info(f"[KB_UPDATE] Successfully updated KB '{kb_name}': deleted {chunks_deleted}, created {chunks_created} chunks in {time.time() - kb_start_time:.3f}s")

    except Exception as e:
        error = str(e)
        status = "failed"
        logger.error(f"[KB_UPDATE] Failed to update KB '{kb_name}': {e}")
        logger.debug(f"[KB_UPDATE] Full traceback: {traceback.format_exc()}")

    processing_time = time.time() - kb_start_time

    return {
        "kb_id": kb_id,
        "kb_name": kb_name,
        "status": status,
        "chunks_deleted": chunks_deleted,
        "chunks_created": chunks_created,
        "processing_time_seconds": processing_time,
        "error": error
    }


@logger.catch()
async def delete_single_kb_file(kb_data: dict, file_path: str) -> dict:
    """Delete all chunks for a specific file from a single knowledge base"""
    kb_start_time = time.time()
    chunks_deleted = 0
    error = None
    status = "failed"
    kb_id = kb_data["id"]
    kb_name = kb_data.get("name", "Unknown")

    try:
        logger.info(f"[KB_DELETE] Starting deletion of file '{file_path}' from KB '{kb_name}' (ID: {kb_id})")

        # Step 1: Delete existing chunks for the file
        logger.debug(f"[KB_DELETE] Step 1/2: Deleting all chunks for file '{file_path}' from KB '{kb_name}'")
        chunks_deleted = await delete_file_chunks_from_kb(kb_data, file_path)

        # Step 2: Remove file timestamp from metadata
        logger.debug(f"[KB_DELETE] Step 2/2: Removing file timestamp from metadata for KB '{kb_name}'")
        await update_kb_file_timestamp(kb_data, file_path, "delete")

        status = "success"
        logger.info(f"[KB_DELETE] Successfully deleted {chunks_deleted} chunks for file '{file_path}' from KB '{kb_name}' in {time.time() - kb_start_time:.3f}s")

    except Exception as e:
        error = str(e)
        status = "failed"
        logger.error(f"[KB_DELETE] Failed to delete file '{file_path}' from KB '{kb_name}': {e}")
        logger.debug(f"[KB_DELETE] Full traceback: {traceback.format_exc()}")

    processing_time = time.time() - kb_start_time

    return {
        "kb_id": kb_id,
        "kb_name": kb_name,
        "status": status,
        "chunks_deleted": chunks_deleted,
        "processing_time_seconds": processing_time,
        "error": error
    }





# -----------------------------------------------------------------------------
# Main Route Handler
# -----------------------------------------------------------------------------

@logger.catch()
async def watchdog_file_update(file_path: str) -> dict:
    """Handle file update notification from watchdog server"""
    start_time = time.time()
    timestamp = datetime.now(timezone.utc).isoformat()

    logger.info(f"Processing file update request: {file_path}")

    try:
        file_path_str = validate_file_path(file_path)
        matching_kbs = await find_kbs_containing_file(file_path_str)

        if not matching_kbs:
            return {
                "status": "success",
                "file_path": file_path_str,
                "timestamp": timestamp,
                "processing_time_seconds": time.time() - start_time,
                "summary": {
                    "total_kbs_found": 0,
                    "kbs_updated_successfully": 0,
                    "kbs_failed": 0,
                    "total_chunks_deleted": 0,
                    "total_chunks_created": 0,
                    "total_embeddings_generated": 0
                },
                "kb_results": [],
                "warnings": ["File not found in any knowledge base"],
                "next_actions": ["Verify file path and knowledge base content"]
            }

        kb_results = []
        successful_updates = 0
        failed_updates = 0
        total_chunks_deleted = 0
        total_chunks_created = 0

        for kb_data in matching_kbs:
            kb_name = kb_data.get("name", "Unknown")
            result = await update_single_kb(kb_data, file_path_str)
            kb_results.append(result)

            if result["status"] == "success":
                successful_updates += 1
                total_chunks_deleted += result["chunks_deleted"]
                total_chunks_created += result["chunks_created"]
            else:
                failed_updates += 1
                logger.error(f"Failed to update KB '{kb_name}': {result.get('error')}")

        total_processing_time = time.time() - start_time
        overall_status = "success" if failed_updates == 0 else "partial" if successful_updates > 0 else "failed"

        warnings = []
        next_actions = []

        if failed_updates > 0:
            warnings.append(f"{failed_updates} knowledge base(s) failed to update")
            next_actions.append("Review failed KB updates in the logs")

        if total_chunks_created > total_chunks_deleted * 1.5:
            warnings.append("File size increased significantly - consider reviewing chunking parameters")

        if overall_status == "partial":
            next_actions.append("Consider manual verification of updated content")

        response = {
            "status": overall_status,
            "file_path": file_path_str,
            "timestamp": timestamp,
            "processing_time_seconds": total_processing_time,
            "summary": {
                "total_kbs_found": len(matching_kbs),
                "kbs_updated_successfully": successful_updates,
                "kbs_failed": failed_updates,
                "total_chunks_deleted": total_chunks_deleted,
                "total_chunks_created": total_chunks_created,
                "total_embeddings_generated": total_chunks_created
            },
            "kb_results": kb_results,
            "warnings": warnings,
            "next_actions": next_actions
        }

        logger.info(f"File update completed - Status: {overall_status}, KBs Updated: {successful_updates}/{len(matching_kbs)}")
        return response

    except Exception as e:
        logger.error(f"Error in file update: {str(e)}")
        return {
            "status": "error",
            "file_path": file_path,
            "timestamp": timestamp,
            "processing_time_seconds": time.time() - start_time,
            "error": str(e)
        }


@logger.catch()
async def watchdog_file_delete(file_path: str) -> dict:
    """Handle file deletion notification from watchdog server"""
    start_time = time.time()
    timestamp = datetime.now(timezone.utc).isoformat()

    logger.info(f"Processing file deletion request: {file_path}")

    try:
        if ".." in file_path:
            raise ValueError("Invalid file path: directory traversal detected")

        file_path_str = file_path
        matching_kbs = await find_kbs_containing_file(file_path_str)

        if not matching_kbs:
            return {
                "status": "success",
                "file_path": file_path_str,
                "timestamp": timestamp,
                "processing_time_seconds": time.time() - start_time,
                "summary": {
                    "total_kbs_found": 0,
                    "kbs_processed_successfully": 0,
                    "kbs_failed": 0,
                    "total_chunks_deleted": 0
                },
                "kb_results": [],
                "warnings": ["File not found in any knowledge base"],
                "next_actions": ["Verify file path and knowledge base content"]
            }

        kb_results = []
        successful_deletions = 0
        failed_deletions = 0
        total_chunks_deleted = 0

        for kb_data in matching_kbs:
            kb_name = kb_data.get("name", "Unknown")
            result = await delete_single_kb_file(kb_data, file_path_str)
            kb_results.append(result)

            if result["status"] == "success":
                successful_deletions += 1
                total_chunks_deleted += result["chunks_deleted"]
            else:
                failed_deletions += 1
                logger.error(f"Failed to delete from KB '{kb_name}': {result.get('error')}")

        total_processing_time = time.time() - start_time
        overall_status = "success" if failed_deletions == 0 else "partial" if successful_deletions > 0 else "failed"

        warnings = []
        next_actions = []

        if failed_deletions > 0:
            warnings.append(f"{failed_deletions} knowledge base(s) failed to process deletion")
            next_actions.append("Review failed KB deletions in the logs")

        if total_chunks_deleted == 0 and matching_kbs:
            warnings.append("No chunks were deleted despite file being found in knowledge bases")
            next_actions.append("Verify chunk deletion logic and file path matching")

        if overall_status == "partial":
            next_actions.append("Consider manual verification of remaining content")

        response = {
            "status": overall_status,
            "file_path": file_path_str,
            "timestamp": timestamp,
            "processing_time_seconds": total_processing_time,
            "summary": {
                "total_kbs_found": len(matching_kbs),
                "kbs_processed_successfully": successful_deletions,
                "kbs_failed": failed_deletions,
                "total_chunks_deleted": total_chunks_deleted
            },
            "kb_results": kb_results,
            "warnings": warnings,
            "next_actions": next_actions
        }

        logger.info(f"File deletion completed - Status: {overall_status}, KBs Processed: {successful_deletions}/{len(matching_kbs)}")
        return response

    except Exception as e:
        logger.error(f"Error in file deletion: {str(e)}")
        return {
            "status": "error",
            "file_path": file_path,
            "timestamp": timestamp,
            "processing_time_seconds": time.time() - start_time,
            "error": str(e)
        }
