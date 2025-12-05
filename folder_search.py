import os
import json
from typing import Any
from BASE.embeddings.embeddings import generate_embeddings_cloud, EmbeddingServiceError
from BASE.vdb.qdrant import get_qdrant_client
from logger.log import logger
# -----------------------------------------------------------------------------
# Perform folder search
# -----------------------------------------------------------------------------

@logger.catch()
async def _perform_folder_search(
    query: str,
    index_name: str,
    folder_path: str,
    limit: int = 10,
) -> list[dict[str, Any]]:
    """
    Perform a search within a specific folder using Qdrant.
    Args:
        query: Search query string
        index_name: Name of the collection to search in
        folder_path: Path to folder to search within
        limit: Maximum number of results to return
    Returns:
        List of search results with chunks and metadata
    """

    logger.info(f"Performing folder search for query: {query}")
    logger.info(f"folder path: {folder_path}")
    try:
        # Get Qdrant client
        qc = get_qdrant_client()
        
        # Generate embeddings
        embeddings = await generate_embeddings_cloud(False, query)

        # Since we only have the folder name (e.g., "main") but need to match full paths,
        # we'll search without a filter first and then filter results in Python
        # This is more reliable than trying to use MatchText for path matching

        logger.info(f"Searching without folder filter, will filter results by folder path: {folder_path}")

        # Perform search without filter first, then filter results
        # We search with a higher limit to ensure we get enough results after filtering
        search_limit = limit * 5  # Search for more results to account for filtering
        search_results = await qc.search(
            collection_name=index_name,
            query_vector=("vectors", embeddings),
            limit=search_limit,
            with_payload=True,
        )

        logger.info(f"Raw search results count: {len(search_results)}")

        if not search_results:
            return []

        # Filter results by folder path
        # Check if the file path contains the folder name
        filtered_results = []
        for result in search_results:
            payload = result.payload
            file_path = payload.get("file", "")

            # Check if the folder_path appears in the file path
            # This handles cases where folder_path is just the folder name (e.g., "main")
            # and the file path is a full path (e.g., "c:/Users/.../main/file.ts")
            if folder_path.lower() in file_path.lower():
                filtered_results.append(result)

        logger.info(f"Filtered results count: {len(filtered_results)} (filtered by folder: {folder_path})")

        # Limit the filtered results to the requested limit
        filtered_results = filtered_results[:limit]

        # Format results
        results = []
        for result in filtered_results:
            payload = result.payload
            results.append(
                {
                    "file": payload.get("file", ""),
                    "content": {"text": payload.get("content", "")},
                    "additional_metadata": payload.get("additional_metadata", {}),
                }
            )

        # logger.info(f"Folder search results: {json.dumps(results, indent=2)}")
        return results

    except EmbeddingServiceError as e:
        logger.error(f"Embedding service error in _perform_folder_search: {e.message}")
        print(f"Embedding service unavailable: {e.message}")
        return []
    except Exception as e:
        print(f"Error in _perform_folder_search: {e}")
        return []


# -----------------------------------------------------------------------------
# Process folder search
# -----------------------------------------------------------------------------

@logger.catch()
async def process_folder_search(
    query: str,
    tool_id: str,
    folder_path: str,
    index_name: str,
    search_references,
):
    """Handle folder search actions"""
    logger.info("Processing folder search")
    try:
        search_results = await _perform_folder_search(
            query=query,
            index_name=index_name,
            folder_path=folder_path,
        )

        # logger.info(f"Folder search results: {json.dumps(search_results, indent=2)}")

        for chunk in search_results:
            text = chunk["content"]["text"]
            filename = os.path.basename(chunk["file"])
            filepath = chunk["file"]
            search_references.add_search_result(
                path=filepath, name=filename, content=text, type="file"
            )

        status = "success" if search_results else "error"
        if status == "success":
            new_messages = {"status": status, "content": search_results}
        else:
            new_messages = {"status": status, "content": "No search results found for the specified folder and query"}

        return new_messages, search_references
    except Exception as e:
        print(f"Error in process_folder_search: {e}")
        error_message = f"Folder search failed: {str(e)}"
        error_response = {"status": "error", "content": error_message}
        return error_response, search_references


# -----------------------------------------------------------------------------
