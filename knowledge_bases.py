import os
import time
from pathlib import Path
from typing import List, Dict, Any
from uuid import uuid4

from database.MicroMongo import MongoClient
from BASE.vdb.qdrant import get_qdrant_client
from qdrant_client.models import (
    Distance,
    VectorParams,
    Filter,
    FieldCondition,
    MatchValue,
    PointStruct,
)
from logger.log import logger
from BASE.chunkers.utils import make_chunks_from_file
from BASE.embeddings.embeddings import generate_embeddings_cloud
from BASE.utils.path_selector import PathSelector
from typing import AsyncGenerator, Callable, Coroutine, Optional

# Initialize MicroMongo client and database
_client = None
_db = None


def get_knowledge_bases_collection():
    """Get the knowledge_bases collection from MicroMongo database."""
    global _client, _db

    if _client is None:
        # Ensure .codemate directory exists
        codemate_path = PathSelector.get_base_path()
        os.makedirs(codemate_path, exist_ok=True)

        # Create database file in .codemate folder
        db_path = codemate_path / "knowledge_bases_db"
        _client = MongoClient(str(db_path))
        _db = _client["codemate"]

    return _db["knowledge_bases"]


def create_knowledge_base(
    name: str, kbid: str, metadata: dict = None, is_auto_indexed: bool = False
):
    """Create a new knowledge base entry."""
    collection = get_knowledge_bases_collection()

    kb_data = {"metadata": metadata}

    result = collection.insert_one(kb_data)
    return result.inserted_id


def get_knowledge_base_by_name(name: str):
    """Get a knowledge base by name."""
    collection = get_knowledge_bases_collection()
    return collection.find_one({"name": name})


def get_knowledge_base_by_id(kbid: str):
    """Get a knowledge base by ID."""
    collection = get_knowledge_bases_collection()
    return collection.find_one({"id": kbid})



def get_knowledge_base_by_path(path: str):
    """Get a knowledge base by path."""
    collection = get_knowledge_bases_collection()
    logger.info(f"path: {path}")

    # TinyMongo doesn't support dot notation queries like "metadata.path"
    # So we need to manually search through all documents
    all_docs = list(collection.find())
    for doc in all_docs:
        if ("metadata" in doc and
            isinstance(doc["metadata"], dict) and
            "path" in doc["metadata"] and
            doc["metadata"]["path"] == path):
            logger.info(f"Found matching document: {doc.get('name', 'unnamed')}")
            return doc

    # No matching document found
    logger.info("No matching document found")
    return None


def get_auto_indexed_knowledge_base_by_path(path: str):
    """Get an auto-indexed knowledge base by path."""
    collection = get_knowledge_bases_collection()
    normalized_path = str(Path(path).resolve())

    # TinyMongo doesn't support dot notation queries like "metadata.path"
    # So we need to manually search through all documents
    all_docs = list(collection.find())
    for doc in all_docs:
        if (doc.get("isAutoIndexed") == True and
            "metadata" in doc and
            isinstance(doc["metadata"], dict) and
            "path" in doc["metadata"] and
            doc["metadata"]["path"] == normalized_path):
            return doc

    return None


def exists_knowledge_base_by_name(name: str) -> bool:
    """Check if a knowledge base with the given name exists."""
    return get_knowledge_base_by_name(name) is not None


def exists_knowledge_base_by_id(kbid: str) -> bool:
    """Check if a knowledge base with the given ID exists."""
    return get_knowledge_base_by_id(kbid) is not None


def exists_knowledge_base_by_path(path: str) -> bool:
    """Check if a knowledge base with the given path exists."""
    return get_knowledge_base_by_path(path) is not None


def exists_auto_indexed_knowledge_base_by_path(path: str) -> bool:
    """Check if an auto-indexed knowledge base with the given path exists."""
    return get_auto_indexed_knowledge_base_by_path(path) is not None


def update_knowledge_base(kbid: str, update_data: dict):
    """Update a knowledge base by ID."""
    logger.info(f"update_data: {update_data}")
    collection = get_knowledge_bases_collection()
    return collection.update_one({"id": kbid}, {"$set": update_data})

def update_knowledge_base_metadata(kbid: str, metadata: dict):
    """Update the metadata field of a knowledge base."""
    logger.info(f"metadata: {metadata}")
    collection = get_knowledge_bases_collection()
    return collection.update_one({"id": kbid}, {"$set": {"metadata": metadata}})


def update_knowledge_base_cloud_id(kbid: str, cloud_id: str = None):
    """Update the cloud_id field of a knowledge base."""
    current_kb = get_knowledge_base_by_id(kbid)
    
    current_kb["cloud_id"] = cloud_id
    update_knowledge_base(kbid, current_kb)




def update_knowledge_base_sync_config(kbid: str, sync_config: dict):
    """Update the sync configuration of a knowledge base."""
    current_kb = get_knowledge_base_by_id(kbid)

    current_kb["syncConfig"] = sync_config
    update_knowledge_base(kbid, current_kb)


def update_knowledge_base_lastSynced(kbid: str, timestamp: int):
    """Update the lastSynced timestamp of a knowledge base."""

    current_kb = get_knowledge_base_by_id(kbid)
    current_kb["syncConfig"]["lastSynced"] = timestamp
    update_knowledge_base(kbid, current_kb)





def delete_knowledge_base(kbid: str):
    """Delete a knowledge base by ID."""
    collection = get_knowledge_bases_collection()
    return collection.delete_one({"id": kbid})


def list_all_knowledge_bases():
    """Get all knowledge bases."""
    collection = get_knowledge_bases_collection()
    return list(collection.find())


def count_knowledge_bases():
    """Count total number of knowledge bases."""
    collection = get_knowledge_bases_collection()
    return collection.count_documents({})



def get_knowledge_base_metadata(kbid: str) -> dict:
    """Get metadata of a knowledge base by ID."""
    collection = get_knowledge_bases_collection()
    doc = collection.find_one({"id": kbid})

    if doc:
        return doc.get("metadata", {})
    else:
        return {}

@logger.catch()
async def from_chunks(
    metadata: dict,
    chunks_iterable: AsyncGenerator[list[dict], None],
) -> dict:
    """
    Save processed chunks to Qdrant database using functional programming approach.

    Args:
        metadata: Dictionary containing knowledge base metadata with structure:
            {
                "id": str,
                "cloud_id": None,
                "name": str,
                "description": str,
                "type": str,
                "source": str,
                "scope": str,
                "syncConfig": {"enabled": bool, "lastSynced": int},
                "isAutoIndexed": bool,
                "metadata": {...}  # Type-specific metadata
            }
        chunks: List of chunk dictionaries with structure:
            {
                "metadata": {
                    "id": str,
                    "file": str,
                    "name": str,
                    "content": str,
                    "additional_metadata": {...}
                },
                "embeddings": [float, ...]
            }

    Returns:
        Dictionary representing the created knowledge base
    """

    kb_id = metadata["id"]
    logger.info(f"Starting from_chunks for knowledge base: {kb_id}")

    qdrant_client = get_qdrant_client()
    collection_name = kb_id

    # 1. Create fresh collection
    logger.debug(f"Creating Qdrant collection: {collection_name}")
    await qdrant_client.create_collection(
        collection_name=collection_name,
        vectors_config={"vectors": VectorParams(size=1024, distance=Distance.DOT)},
    )

    total_inserted = 0
    batch_index = 0
    try:
        async for batch in chunks_iterable:
            batch_index += 1
            if not batch:
                logger.debug(f"Skipping empty batch #{batch_index}")
                continue

            points = [
                PointStruct(
                    id=chunk["metadata"]["id"],
                    vector={"vectors": chunk["embeddings"]},
                    payload=chunk["metadata"],
                )
                for chunk in batch
            ]

            await qdrant_client.upsert(collection_name=collection_name, points=points)
            total_inserted += len(points)

            logger.info(
                f"Batch #{batch_index} inserted with {len(points)} chunks "
                f"(total inserted so far: {total_inserted})"
            )

        # 2. Only insert metadata if all chunks succeeded
        collection = get_knowledge_bases_collection()
        result = collection.insert_one(metadata)
        logger.info(
            f"Knowledge base entry created in DB with ID: {result.inserted_id}, "
            f"total chunks inserted: {total_inserted}"
        )

        return metadata

    except Exception as e:
        logger.error(f"Error during from_chunks for KB {kb_id}: {e}")
        # rollback collection if anything failed
        try:
            await qdrant_client.delete_collection(collection_name=collection_name)
            logger.warning(f"Rolled back collection: {collection_name}")
        except Exception as rollback_err:
            logger.error(f"Rollback failed: {rollback_err}")
        raise e




@logger.catch()
async def get_all_chunks():
    qdrant_client = get_qdrant_client()
    chunks = []

    offset = None
    batch_size = 1000

    while True:
        # Get batch of points

        result = await qdrant_client.scroll(
            collection_name="test",
            limit=batch_size,
            offset=offset,
            with_payload=True,
            with_vectors=True,
        )

        points, next_offset = result

        # Process current batch
        for point in points:
            # Handle embeddings - extract from vectors wrapper if present
            embeddings = point.vector.get("vectors", point.vector) if isinstance(point.vector, dict) else point.vector
            chunk = {"metadata": point.payload, "embeddings": embeddings}
            chunks.append(chunk)

        # Break if no more results
        if not next_offset or len(points) < batch_size:
            break

        # Update offset for next iteration
        offset = next_offset

    return chunks



@logger.catch()
async def get_all_chunks_from_kb(kbid: str) -> list[dict]:
    """
    Get all chunks from a knowledge base using Qdrant with efficient pagination.

    Args:
        kbid: Knowledge base ID

    Returns:
        List of chunk dictionaries
    """
    try:
        qdrant_client = get_qdrant_client()
        chunks = []
        batch_size = 1000  # Process in smaller batches for better memory management
        
        # Initialize pagination
        offset = None
        total_processed = 0

        while True:
            # Get batch of points
            result = await qdrant_client.scroll(
                collection_name=kbid,
                limit=batch_size,
                offset=offset,
                with_payload=True,
                with_vectors=True,
            )
            
            points, next_offset = result
            
            # Process current batch
            batch_chunks = []
            for point in points:
                # Handle embeddings - extract from vectors wrapper if present
                embeddings = point.vector.get("vectors", point.vector) if isinstance(point.vector, dict) else point.vector

                # Handle metadata - flatten if nested (for backward compatibility)
                metadata = point.payload
                if "metadata" in metadata and isinstance(metadata["metadata"], dict):
                    # Old format with nested metadata - flatten it
                    metadata = metadata["metadata"]

                batch_chunks.append({
                    "metadata": metadata,
                    "embeddings": embeddings
                })

            chunks.extend(batch_chunks)
            
            # Update progress
            total_processed += len(batch_chunks)
            logger.debug(f"Processed {total_processed} chunks from KB {kbid}")
            
            # Check if we've retrieved all chunks
            if not next_offset or len(points) < batch_size:
                break
                
            # Update offset for next iteration
            offset = next_offset

        logger.info(f"Successfully retrieved {len(chunks)} total chunks from knowledge base {kbid}")
        return chunks

    except Exception as e:
        logger.error(f"Error retrieving chunks from knowledge base {kbid}: {e}")
        return []





@logger.catch()
def get_chunks_by_file_path(
    kb_id: str, file_path: str
) -> list[dict]:
    """
    Retrieve all chunks associated with a specific file path from the knowledge base's Qdrant collection.

    Args:
        kb_id: Knowledge base ID
        file_path: The file path to search for in chunk metadata
        sort_by_line: Whether to sort chunks by line number (if line_start exists in additional_metadata)

    Returns:
        List of chunk dictionaries for the specified file path
    """
    client = get_qdrant_client()
    chunks = []
    batch_size = 1000

    # Create filter to match the specific file path
    file_filter = Filter(
        must=[FieldCondition(key="file", match=MatchValue(value=file_path))]
    )

    # Use pagination to retrieve all results
    offset = None
    while True:
        scroll_result = client.scroll(
            collection_name=kb_id,
            scroll_filter=file_filter,
            limit=batch_size,
            with_payload=True,
            with_vector=True,
            offset=offset,
        )

        current_batch = scroll_result[0]
        offset = scroll_result[1]

        for point in current_batch:
            # Extract metadata and vectors from the point
            metadata_dict = point.payload
            vectors = (
                point.vector["vectors"]
                if isinstance(point.vector, dict)
                else point.vector
            )

            # Handle nested metadata for backward compatibility
            if "metadata" in metadata_dict and isinstance(metadata_dict["metadata"], dict):
                # Old format with nested metadata - flatten it
                metadata_dict = metadata_dict["metadata"]

            chunk = {"metadata": metadata_dict, "embeddings": vectors}
            chunks.append(chunk)

        # Break if no more results
        if not offset or len(current_batch) < batch_size:
            break

    return chunks


# -----------------------------------------------------------------------------
# General Knowledge Base Operations (moved from watchdog.py)
# -----------------------------------------------------------------------------


@logger.catch()
def get_file_modification_time(file_path: str) -> int:
    """
    Get file modification time in milliseconds.

    Args:
        file_path: Path to the file

    Returns:
        File modification time in milliseconds, or 0 if error
    """
    try:
        if os.path.exists(file_path):
            # Get modification time in seconds and convert to milliseconds
            mtime_seconds = os.path.getmtime(file_path)
            return int(mtime_seconds * 1000)
        else:
            logger.warning(f"File does not exist: {file_path}")
            return 0
    except OSError as e:
        logger.error(f"Error getting modification time for {file_path}: {e}")
        return 0


@logger.catch()
def normalize_path_format(file_path: str) -> str:
    """Normalize file path format for consistent comparison."""
    return str(Path(file_path).as_posix())


@logger.catch()
async def find_kbs_containing_file(file_path: str) -> List[dict]:
    """Find all codebase knowledge bases that contain the specified file"""
    try:
        logger.debug(
            f"[KB_SEARCH] Searching for knowledge bases containing file: {file_path}"
        )

        # Get all knowledge bases
        all_kbs = list_all_knowledge_bases()
        matching_kbs = []

        for kb in all_kbs:
            # Only check codebase type KBs
            kb_type = kb.get("type", "")
            if kb_type != "codebase":
                continue

            kb_id = kb["id"]
            kb_name = kb.get("name", "Unknown")

            try:
                # Use get_chunks_by_file_path to check if file exists in KB
                chunks = get_chunks_by_file_path(kb_id, file_path)
                
                if chunks:
                    matching_kbs.append(kb)
                    logger.debug(
                        f"[KB_SEARCH] KB '{kb_name}' contains file '{file_path}'"
                    )
                else:
                    logger.debug(
                        f"[KB_SEARCH] KB '{kb_name}' does not contain file '{file_path}'"
                    )

            except Exception as e:
                logger.warning(
                    f"[KB_SEARCH] Error checking KB '{kb_name}' for file '{file_path}': {e}"
                )
                continue

        logger.info(
            f"[KB_SEARCH] Found {len(matching_kbs)} knowledge bases containing file '{file_path}'"
        )
        return matching_kbs

    except Exception as e:
        logger.error(
            f"[KB_SEARCH] Error searching for knowledge bases containing file '{file_path}': {e}"
        )
        return []

@logger.catch()
async def delete_file_chunks_from_kb(kb_data: dict, file_path: str) -> int:
    """Delete all chunks for a specific file from a knowledge base"""
    try:
        client = get_qdrant_client()
        total_chunks_deleted = 0
        batch_size = 1000  # Process chunks in batches to manage memory
        kb_id = kb_data["id"]
        kb_name = kb_data.get("name", "Unknown")

        # Create filter to match the specific file path
        file_filter = Filter(
            must=[FieldCondition(key="file", match=MatchValue(value=file_path))]
        )

        logger.debug(
            f"[CHUNK_DELETE] Starting chunk retrieval for file '{file_path}' from KB '{kb_name}'"
        )

        # Use pagination to handle large number of chunks
        offset = None
        while True:
            # Get batch of chunks
            scroll_result = await client.scroll(
                collection_name=kb_id,
                scroll_filter=file_filter,
                limit=batch_size,
                with_payload=True,  # Need payload for detailed logging
                with_vectors=False,  # Don't need vectors for deletion
                offset=offset,
            )

            current_batch = scroll_result[0]
            offset = scroll_result[1]  # Update offset for next iteration

            batch_count = len(current_batch)
            if batch_count == 0:
                break

            total_chunks_deleted += batch_count

            # Log batch information
            logger.info(
                f"[CHUNK_DELETE] Processing batch of {batch_count} chunks from KB '{kb_name}'"
            )

            # Log detailed chunk information for debugging
            for i, chunk in enumerate(current_batch):
                chunk_id = chunk.id
                chunk_payload = chunk.payload or {}
                chunk_content = chunk_payload.get("content", "No content available")
                chunk_name = chunk_payload.get("name", "Unknown")

                # Truncate content for logging
                content_preview = (
                    chunk_content[:200] + "..."
                    if len(chunk_content) > 200
                    else chunk_content
                )
                logger.debug(
                    f"[CHUNK_DELETE] Processing chunk {i+1}/{batch_count} "
                    f"(Total: {total_chunks_deleted}) - "
                    f"ID: {chunk_id}, Name: '{chunk_name}', "
                    f"Content: '{content_preview}'"
                )

            # Delete current batch
            logger.debug(
                f"[CHUNK_DELETE] Deleting batch of {batch_count} chunks from KB '{kb_name}'"
            )
            await client.delete(collection_name=kb_id, points_selector=file_filter)

            # Break if this was the last batch
            if len(current_batch) < batch_size:
                break

            # Memory optimization: Clear batch data
            del current_batch

        if total_chunks_deleted > 0:
            logger.info(
                f"[CHUNK_DELETE] Successfully deleted {total_chunks_deleted} total chunks for file '{file_path}' from KB '{kb_name}'"
            )
        else:
            logger.debug(
                f"[CHUNK_DELETE] No chunks found for file '{file_path}' in KB '{kb_name}'"
            )

        return total_chunks_deleted

    except Exception as e:
        logger.error(
            f"[CHUNK_DELETE] Error deleting chunks from KB '{kb_data.get('name', 'Unknown')}': {e}"
        )
        raise


@logger.catch()
async def process_file_chunks(file_path: str, kb_data: dict) -> List[dict]:
    """Process file into chunks using functional chunker for codebase type only"""
    try:
        kb_name = kb_data.get("name", "Unknown")
        kb_type = kb_data.get("type", "")

        logger.debug(
            f"[CHUNK_PROCESS] Starting file processing for '{file_path}' in KB '{kb_name}' (type: {kb_type})"
        )

        # Only handle codebase type as per requirements
        if kb_type != "codebase":
            raise ValueError(
                f"Unsupported KB type '{kb_type}'. Only codebase type is supported."
            )

        logger.debug(f"[CHUNK_PROCESS] Using functional chunker for file '{file_path}'")
        chunks = make_chunks_from_file(file_path)

        # Update chunk metadata with correct file path and names
        for i, chunk in enumerate(chunks):
            chunk["metadata"]["file"] = file_path
            chunk["metadata"]["name"] = f"{Path(file_path).name} - chunk {i+1}"
            content_length = len(chunk["metadata"].get("content", ""))
            logger.debug(
                f"[CHUNK_PROCESS] Processed chunk {i+1}: Content length: {content_length} chars"
            )

        logger.info(
            f"[CHUNK_PROCESS] Successfully processed {len(chunks)} chunks from file '{file_path}' using functional chunker"
        )
        return chunks

    except Exception as e:
        logger.error(
            f"[CHUNK_PROCESS] Error processing file '{file_path}' for KB '{kb_data.get('name', 'Unknown')}': {e}"
        )
        raise


@logger.catch()
async def insert_chunks_to_kb(kb_data: dict, chunks: List[dict]) -> None:
    """Insert new chunks into knowledge base"""
    try:
        if not chunks:
            logger.debug(
                f"[CHUNK_INSERT] No chunks to insert into KB '{kb_data.get('name', 'Unknown')}'"
            )
            return

        kb_id = kb_data["id"]
        kb_name = kb_data.get("name", "Unknown")
        logger.info(
            f"[CHUNK_INSERT] Starting insertion of {len(chunks)} chunks into KB '{kb_name}'"
        )
        client = get_qdrant_client()

        # Prepare points for insertion and log chunk details
        points = []

        for i, chunk in enumerate(chunks):
            chunk_id = chunk["metadata"].get("id", str(uuid4()))
            chunk_content = chunk["metadata"].get("content", "")
            chunk_name = chunk["metadata"].get("name", f"chunk_{i+1}")
            content_preview = (
                chunk_content[:200] + "..."
                if len(chunk_content) > 200
                else chunk_content
            )

            logger.debug(
                f"[CHUNK_INSERT] Preparing chunk {i+1}/{len(chunks)} - ID: {chunk_id}, Name: '{chunk_name}', Content: '{content_preview}'"
            )

            points.append(
                PointStruct(
                    id=chunk_id, vector={"vectors": chunk["embeddings"]}, payload=chunk["metadata"]
                )
            )

        # Insert points in batches to avoid memory issues
        batch_size = 100
        total_batches = (len(points) + batch_size - 1) // batch_size
        logger.debug(
            f"[CHUNK_INSERT] Inserting {len(points)} points in {total_batches} batch(es) of max {batch_size} points each"
        )

        for batch_num, i in enumerate(range(0, len(points), batch_size), 1):
            batch = points[i : i + batch_size]
            logger.debug(
                f"[CHUNK_INSERT] Inserting batch {batch_num}/{total_batches} with {len(batch)} points"
            )
            await client.upsert(collection_name=kb_id, points=batch)

        logger.info(
            f"[CHUNK_INSERT] Successfully inserted {len(chunks)} chunks into KB '{kb_name}'"
        )

        # Log the IDs of all newly created chunks
        chunk_ids = [chunk["metadata"].get("id") for chunk in chunks]
        logger.debug(f"[CHUNK_INSERT] New chunk IDs created: {chunk_ids}")

    except Exception as e:
        logger.error(
            f"[CHUNK_INSERT] Error inserting chunks into KB '{kb_data.get('name', 'Unknown')}': {e}"
        )
        raise


@logger.catch()
async def update_kb_file_timestamp(
    kb_data: dict, file_path: str, operation: str = "update"
) -> None:
    """
    Update the file timestamp in knowledge base metadata.

    Args:
        kb_data: The knowledge base dictionary
        file_path: The file path that was modified
        operation: The operation type ("update", "delete")
    """
    try:
        # Only update timestamps for codebase type KBs that have timestamp tracking
        kb_type = kb_data.get("type", "")
        if kb_type != "codebase":
            logger.debug(
                f"[TIMESTAMP_UPDATE] Skipping timestamp update for KB '{kb_data.get('name')}' - not a codebase type"
            )
            return

        kb_metadata = kb_data.get("metadata", {})
        file_timestamps = kb_metadata.get("file_timestamps", {})

        if operation == "delete":
            # Remove timestamp entry for deleted files
            if file_path in file_timestamps:
                del file_timestamps[file_path]
                logger.info(
                    f"[TIMESTAMP_UPDATE] Removed timestamp entry for deleted file '{file_path}' from KB '{kb_data.get('name')}'"
                )
            else:
                logger.debug(
                    f"[TIMESTAMP_UPDATE] No timestamp entry found for deleted file '{file_path}' in KB '{kb_data.get('name')}'"
                )
        else:
            # Update timestamp for modified/added files
            current_timestamp = get_file_modification_time(file_path)
            if current_timestamp > 0:
                file_timestamps[file_path] = current_timestamp
                logger.info(
                    f"[TIMESTAMP_UPDATE] Updated timestamp for file '{file_path}' in KB '{kb_data.get('name')}': {current_timestamp}ms"
                )
            else:
                logger.warning(
                    f"[TIMESTAMP_UPDATE] Could not get valid timestamp for file '{file_path}' in KB '{kb_data.get('name')}'"
                )

        # Update the metadata structure
        kb_data["metadata"]["file_timestamps"] = file_timestamps

        # Persist the updated metadata to the database
        try:
            update_knowledge_base_metadata(kb_data["id"], metadata=kb_data["metadata"])
            logger.debug(
                f"[TIMESTAMP_UPDATE] Persisted timestamp changes to database for KB '{kb_data.get('name')}'"
            )
        except Exception as e:
            logger.error(
                f"[TIMESTAMP_UPDATE] Failed to persist timestamp changes for KB '{kb_data.get('name')}': {e}"
            )

    except Exception as e:
        logger.error(
            f"[TIMESTAMP_UPDATE] Error updating timestamp for file '{file_path}' in KB '{kb_data.get('name')}': {e}"
        )
