import os
import json
from typing import Any
from BASE.embeddings.embeddings import generate_embeddings_cloud, EmbeddingServiceError
from BASE.services.knowledge_bases import exists_knowledge_base_by_id
from logger.log import logger, LogDB, trace_context, set_trace_id, clear_trace_id
import time
import httpx
from constants import SSL_CONTEXT, cloud
from BASE.vdb.qdrant import get_qdrant_client
from ipc import IPC

ipc_ = IPC.connect()

# -----------------------------------------------------------------------------
# Perform context search
# -----------------------------------------------------------------------------


@logger.catch()
async def _perform_remote_search(query: str, kbid: str) -> list[dict[str, Any]]:
    """
    Perform a remote vector search using cloud embeddings.
    """
    try:
        data = {"collection_id": kbid, "search_queries": query}
        session = ipc_.get("current_session") if ipc_.get("current_session") else None
        if not session:
            raise ValueError("Session is required for cloud search authentication")
        # Generate embeddings using cloud service
        async with httpx.AsyncClient(verify=SSL_CONTEXT) as client:
            response = await client.post(
                f"{cloud}/knowledge/search",
                json=data,
                headers={"X-Session": session},
            )
            results = response.json()
            logger.info(f"Remote search results: {json.dumps(results)}")
            results = list(
                map(
                    lambda x: {
                        "file": x.get("payload").get("file", ""),
                        "content": {"text": x.get("payload").get("content", "")},
                        "additional_metadata": {
                            "line_start": (
                                x.get("payload").get("lines", [])[0]
                                if len(x.get("payload").get("lines", [])) > 0
                                else None
                            ),
                            "line_end": (
                                x.get("payload").get("lines", [])[1]
                                if len(x.get("payload").get("lines", [])) > 1
                                else None
                            ),
                        },
                    },
                    results,
                )
            )
            return results
    except Exception as e:
        print(f"Error in perform_remote_search: {e}")
        return []


@logger.catch()
async def _perform_qdrant_search(
    query: str,
    kbid: str,
    limit: int = 30,
) -> list[dict[str, Any]]:
    """
    Perform a local vector search using cloud embeddings.
    """
    try:
        # Generate embeddings using cloud service
        qc = get_qdrant_client()
        embeddings = await generate_embeddings_cloud(False, query)
        # print(f"Embeddings: {embeddings}")
        if embeddings is None:
            raise ValueError("No embeddings generated")

        search_results = await qc.search(
            collection_name=kbid,
            query_vector=("vectors", embeddings),
            limit=limit,
            with_payload=True,
        )

        # Convert results to list of dicts
        # json_results = [res.dict() for res in search_results]

        # # Save to JSON file
        # with open("results.json", "w", encoding="utf-8") as f:
        #     json.dump(json_results, f, ensure_ascii=False, indent=4)

        scores = list(map(lambda x: x.score, search_results))
        print(f"Search Scores: {sum(scores) / len(scores)}")

        if not search_results:
            return []

        results = []
        for result in search_results:
            payload = result.payload
            results.append(
                {
                    "file": payload.get("file", ""),
                    "content": {"text": payload.get("content", str(payload))},
                    "additional_metadata": payload.get("additional_metadata", {}),
                }
            )

        # Log the processed results instead of raw ScoredPoint objects
        # logger.info(f"Search results: {json.dumps(results, indent=2)}")
        return results
    except EmbeddingServiceError as e:
        logger.error(f"Embedding service error in _perform_qdrant_search: {e.message}")
        print(f"Embedding service unavailable: {e.message}")
        return []
    except Exception as e:
        print(f"Error in _perform_qdrant_search: {e}")
        return []


@logger.catch()
async def _perform_local_search(
    query: str,
    kbid: str,
    limit: int = 30,
    session: str = "",
) -> list[dict[str, Any]]:
    """
    Perform a local vector search using cloud embeddings.
    """
    try:
        # Generate embeddings using cloud service
        kb_exists_locally = exists_knowledge_base_by_id(kbid)
        if kb_exists_locally:
            on_cloud = False
            search_kbid = kbid
            logger.info(
                f"Knowledge base {kbid} found locally - performing local search"
            )
        else:
            on_cloud = True
            search_kbid = kbid
            logger.info(
                f"Knowledge base {kbid} not found locally - performing cloud search"
            )

        # Simulate local search results using kbid
        if on_cloud:
            return await _perform_remote_search(query=query, kbid=search_kbid)
        else:
            return await _perform_qdrant_search(
                query=query, kbid=search_kbid, limit=limit
            )

    except Exception as e:
        print(f"Error in perform_local_search: {e}")
        return []


# -----------------------------------------------------------------------------
# Process context search
# -----------------------------------------------------------------------------


@logger.catch()
async def process_context_search(
    query: str, tool_id: str, kbid: str, search_references, session: str = ""
) -> tuple[list[dict[str, Any]], Any]:
    """Handle context search actions"""
    try:
        search_results = await _perform_local_search(
            query=query, kbid=kbid, session=session
        )

        # logger.info(f"")

        # logger.info(f"Search results: {json.dumps(search_results, indent=2)}")

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
            new_messages = {
                "status": status,
                "content": "No search results found for the specified knowledge base and query",
            }

        # logger.info(f"Context search results: {json.dumps(new_messages, indent=2)}")
        return new_messages, search_references
    except Exception as e:
        print(f"Error in process_context_search: {e}")
        error_message = f"Context search failed: {str(e)}"
        error_response = {"status": "error", "content": error_message}
        return error_response, search_references


# -----------------------------------------------------------------------------


@logger.catch()
async def process_new_kb_search(
    query: str, kbid: str, session: str = ""
) -> list[dict[str, Any]]:
    """Handle context search actions and return simplified results"""
    try:
        search_results = await _perform_local_search(
            query=query, kbid=kbid, session=session
        )

        results = []
        for chunk in search_results:
            results.append(
                {
                    "file": os.path.basename(chunk["file"]),
                    "content": chunk["content"]["text"],
                }
            )

        return results
    except Exception as e:
        print(f"Error in process_context_search: {e}")
        return []