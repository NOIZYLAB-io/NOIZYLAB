import json
import copy
from typing import Any
from logger.log import logger

# Import action modules
from BASE.actions.context_search import process_context_search
from BASE.actions.folder_search import process_folder_search
from BASE.actions.swagger_search import process_swagger_search
from BASE.actions.web_search import process_web_search
from BASE.actions.agentic_search import process_agentic_search
from ipc import IPC

ipc_ = IPC.connect()


class SearchReferences:
    """Simple search references tracker for tool execution."""

    def __init__(self, request_id: str = ""):
        self.search_results = {"request_id": request_id, "results": []}

    def add_search_result(self, path: str, type: str, name: str, content: str):
        self.search_results["results"].append(
            {"path": path, "type": type, "name": name, "content": content}
        )

    def get_search_result(self):
        return copy.deepcopy(self.search_results)


async def execute_tool_call(tool_call: dict[str, Any]) -> tuple[dict[str, Any], bool]:
    """
    Execute a tool call and return the result.

    Args:
        tool_call: Tool call from LLM response

    Returns:
        Tuple of (tool_result, needs_followup)
    """
    logger.info(f"Executing tool call: {tool_call}")
    function_name = tool_call["function"]["name"]
    function_args = json.loads(tool_call["function"]["arguments"])
    tool_id = tool_call["id"]

    logger.info(f"Executing tool call: {function_name} with args: {function_args}")

    try:
        # Create search references for this tool call
        search_references = SearchReferences(request_id=tool_id)

        # Route to appropriate action handler
        if function_name == "context_search":
            result, search_refs = await process_context_search(
                query=function_args["query"],
                tool_id=tool_id,
                kbid=function_args["kbid"],
                search_references=search_references,
            )

        elif function_name == "folder_search":
            result, search_refs = await process_folder_search(
                query=function_args["query"],
                tool_id=tool_id,
                folder_path=function_args["folder_path"],
                index_name=function_args["kbid"],
                search_references=search_references,
            )

        elif function_name == "web_search":
            result, search_refs = await process_web_search(
                query=function_args["query"],
                tool_id=tool_id,
                search_references=search_references,
            )

        elif function_name == "agentic_search":
            result, search_refs = await process_agentic_search(
                query=function_args["query"],
                tool_id=tool_id,
                kbid=function_args["kbid"],
                search_references=search_references,
            )

        elif function_name == "swagger_search":
            logger.info(
                f"Processing swagger search with query: {function_args['query']}, tool_id: {tool_id}, kbid: {function_args['kbid']}"
            )
            result, search_refs = await process_swagger_search(
                query=function_args["query"],
                tool_id=tool_id,
                kbid=function_args["kbid"],
                search_references=search_references,
            )

        else:
            raise ValueError(f"Unknown tool function: {function_name}")

        # Format tool result for LLM
        tool_result = {"tool_call_id": tool_id, "content": json.dumps(result)}
        return tool_result, False  # Success, no follow-up needed

    except Exception as e:
        logger.error(f"Error executing tool call {function_name}: {e}")

        error_result = {
            "tool_call_id": tool_id,
            "content": json.dumps({"error": str(e), "status": "error"}),
        }
        return error_result, True  # Error requires follow-up
