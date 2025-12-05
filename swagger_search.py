import json
from typing import Any
from BASE.embeddings.embeddings import generate_embeddings_cloud, EmbeddingServiceError
from BASE.vdb.qdrant import get_qdrant_client
import requests
import constants
from BASE.services.swagger.swagger_llm_service import swagger_query_api, generate_queries
from logger.log import logger

from datetime import datetime
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")


@logger.catch()
async def _perform_swagger_search(
    query: str,
    index_name: str,
    limit: int = 20,
) -> list[dict[str, Any]]:
    logger.info(f"Performing search for query inside Swagger with fucntion name _perform_swagger_search: {query}")
    qc = get_qdrant_client()

    try:
        logger.info(f"Query inside _perform_swagger_search: {query}")
        query_embeddings = await generate_embeddings_cloud(False, query)
        logger.info(f"Embeddings in _perform_swagger_search:")
        results = await qc.search(
            collection_name=index_name,
            query_vector=("vectors", query_embeddings),
            limit=limit,
            with_payload=True,
        )
        logger.info(f"Search results in _perform_swagger_search: {len(results)} results found")
        # with open(f"swagger_1_{timestamp}.json", "w") as f:
        #     json.dump(json_results, f, indent=2)

        # name -> swagger endpoint spec
        results_map: dict[str, dict[str, Any]] = {}
        for i, result in enumerate(results):
            payload = result.payload or {}
            logger.debug(f"Result #{i} keys: {list(payload.keys())}")

            name = payload.get("name")
            additional_metadata = payload.get("additional_metadata", {})

            if name:
                results_map[name] = additional_metadata
            else:
                logger.warning(f"Result #{i} missing 'name' field")

        # logger.info(f"Results map keys: {list(results_map.keys())}")
        logger.info(f"Result map:")
        api_results = await swagger_query_api(query, results)
        logger.info(f"Filtered API results: {api_results}")
        filtered_results = list(map(lambda x: results_map[x], api_results))
        return filtered_results
    except EmbeddingServiceError as e:
        logger.error(f"Embedding service error in _perform_swagger_search: {e.message}")
        print(f"Embedding service unavailable: {e.message}")
        return []
        # with open(f"swagger_3_{timestamp}.json", "w") as f:
        #     json.dump(filtered_results, f, indent=2)
        return filtered_results
    except Exception as e:
        raise


def _extract_endpoint_info(result: dict) -> tuple[str, str]:
    """Extract endpoint path and HTTP method from result data.

    Args:
        result: The search result dictionary

    Returns:
        tuple: (endpoint_path, http_method)
    """
    try:
        # Try to extract from various possible locations in the result
        endpoint_path = ""
        http_method = "GET"  # Default method

        # Check if result has direct path and method
        if "path" in result:
            endpoint_path = result["path"]
        elif "name" in result:
            endpoint_path = result["name"]

        if "method" in result:
            http_method = result["method"].upper()

        # If not found, try to extract from nested structures
        if not endpoint_path and isinstance(result, dict):
            # Look for path in nested objects
            for key, value in result.items():
                if isinstance(value, dict):
                    if "path" in value:
                        endpoint_path = value["path"]
                        break
                    elif "name" in value:
                        endpoint_path = value["name"]
                        break

        # Ensure method is uppercase
        http_method = http_method.upper() if http_method else "GET"

        return endpoint_path, http_method

    except Exception as e:
        print(f"Error extracting endpoint info: {e}")
        return "", "GET"


def _transform_to_new_format(results: list) -> list:
    """Transform search results to the new structured format.

    Args:
        results: List of search results in the old format

    Returns:
        list: Results in the new structured format
    """
    transformed_results = []

    for result in results:
        try:
            # Extract endpoint path and method
            endpoint_path, http_method = _extract_endpoint_info(result)

            # Parse content if it's a JSON string, otherwise use as-is
            content = result
            if isinstance(result, str):
                try:
                    content = json.loads(result)
                except (json.JSONDecodeError, TypeError):
                    content = result

            # Create the new structured format
            transformed_result = {
                "endpoint": endpoint_path,
                "content": content,
                "additional_metadata": {
                    "method": http_method
                }
            }

            transformed_results.append(transformed_result)

        except Exception as e:
            print(f"Error transforming result: {e}")
            # Fallback: include the original result with minimal structure
            transformed_results.append({
                "endpoint": str(result.get("name", "unknown")) if isinstance(result, dict) else "unknown",
                "content": result,
                "additional_metadata": {
                    "method": "GET"
                }
            })

    return transformed_results


async def process_swagger_search(
    query: str, tool_id: str, kbid: str, search_references
):
    """Process swagger search actions."""
    try:
        logger.info(f"Processing swagger search with query: {query}, tool_id: {tool_id}, kbid: {kbid}")
        # Generate multiple search queries using LLM
        if query.strip() == "":
            query = "list all endpoints"
        logger.info(f"Generating queries for search: {query}")
        query_list = await generate_queries(query)
        logger.info(f"Generated swagger {len(query_list)} queries from LLM for search: {query_list}")

        # Perform search with all generated queries
        all_search_results = []
        for generated_query in query_list:
            print(f"")
            search_results = await _perform_swagger_search(query=generated_query, index_name=kbid)
            all_search_results.extend(search_results)

        # with open(f"swagger_4_{timestamp}.json", "w") as f:
        #     json.dump(all_search_results, f, indent=2)

        # Remove duplicates based on name/path while preserving order
        seen_names = set()
        unique_results = []
        for result in all_search_results:
            result_name = result.get("path", "")
            if result_name not in seen_names:
                seen_names.add(result_name)
                unique_results.append(result)

        # with open(f"swagger_5_{timestamp}.json", "w") as f:
        #     json.dump(unique_results, f, indent=2)

        # Transform results to new structured format
        transformed_results = _transform_to_new_format(unique_results)

        # with open(f"swagger_6_{timestamp}.json", "w") as f:
        #     json.dump(transformed_results, f, indent=2)

        # Add search results to search_references (maintaining existing functionality)
        for result in unique_results:
            search_references.add_search_result(
                type="file",
                name=result.get("name", ""),
                path=result.get("name", ""),
                content=json.dumps(result.get("additional_metadata", {})),
            )

        # Return new structured format
        status = "error"
        if transformed_results:
            status = "success"

        result = {"status": status, "content": transformed_results}

        # with open("swagger_results.json", "w") as f:
        #     json.dump(result, f, indent=2)

        return result, search_references

    except Exception as e:
        print(f"Error in process_swagger_search: {e}")
        raise
