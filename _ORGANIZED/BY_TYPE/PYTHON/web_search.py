import json
from BASE.embeddings.embeddings import generate_embeddings_cloud
import requests
from constants import general
from ipc import IPC

ipc_ = IPC.connect()

# -----------------------------------------------------------------------------
# Perform web search
# -----------------------------------------------------------------------------


async def process_web_search(*, query: str, tool_id: str, search_references: any):
    """
    Process a web search request.

    Args:
        query: Search query string
        tool_id: ID of the tool making the request
        session: Session ID for authentication
        search_references: SearchReferences object to track search results

    Returns:
        Tuple of (message, search_references)
    """

    session = ipc_.get("current_session") if ipc_.get("current_session") else None
    if not session:
        raise ValueError("Session is required for web search authentication")
    try:
        response = requests.post(
            f"{general}/web_search",
            json={"query": query},
            headers={
                "Content-Type": "application/json",
                "x-session": session,
            },
        )
        data = response.json()
        print(data)
        sources = data["data"]["sources"]

        for source in sources:
            search_references.add_search_result(
                path=source["url"], name=source["title"], content="", type="web"
            )

        status = "success" if sources else "error"
        if status == "success":
            message = {
                "status": status,
                "content": data["data"]["content"],
                "sources": sources,
            }
        else:
            message = {
                "status": status,
                "content": "No web search results found for the specified query",
            }

        return message, search_references
    except Exception as e:
        print(f"Error in process_web_search: {e}")
        error_message = f"Web search failed: {str(e)}"
        error_response = {"status": "error", "content": error_message}
        return error_response, search_references
