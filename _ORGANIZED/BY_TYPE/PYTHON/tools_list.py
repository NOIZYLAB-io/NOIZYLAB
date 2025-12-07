TOOLS_LIST = {
    "codebase": {
        "type": "function",
        "function": {
            "name": "context_search",
            "description": "Search for relevant information within a specific knowledge-base using semantic search.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query to find relevant information"
                    },
                    "kbid": {
                        "type": "string",
                        "description": "The knowledge-base ID to search within"
                    }
                },
                "required": ["query", "kbid"],
            }
        }
    },
    "git": {
        "type": "function",
        "function": {
            "name": "context_search",
            "description": "Search for relevant information within a git repository knowledge-base using semantic search.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query to find relevant information"
                    },
                    "kbid": {
                        "type": "string",
                        "description": "The knowledge-base ID to search within"
                    }
                },
                "required": ["query", "kbid"],
            }
        }
    },
    "docs": {
        "type": "function",
        "function": {
            "name": "context_search",
            "description": "Search for relevant information within a documentation knowledge-base using semantic search.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query to find relevant information"
                    },
                    "kbid": {
                        "type": "string",
                        "description": "The knowledge-base ID to search within"
                    }
                },
                "required": ["query", "kbid"],
            }
        }
    },
    "folder": {
        "type": "function",
        "function": {
            "name": "folder_search",
            "description": "Search for relevant information within a specific folder using semantic search within a knowledge-base.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query to find relevant information"
                    },
                    "kbid": {
                        "type": "string",
                        "description": "The knowledge-base ID to search within"
                    },
                    "folder_path": {
                        "type": "string",
                        "description": "The folder to search within"
                    }
                },
                "required": ["query", "kbid", "folder_path"],
            }
        }
    },
    "websearch": {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the web for relevant information and external resources.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query to find relevant information on the web"
                    }
                },
                "required": ["query"]
            }
        }
    },
    "swagger": {
        "type": "function",
        "function": {
            "name": "swagger_search",
            "description": "Search API documentation and endpoints using Swagger/OpenAPI specifications",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query to find relevant API endpoints do not make it empty string or null or undefined i want to search for all endpoints "
                    },
                    "kbid": {
                        "type": "string",
                        "description": "The knowledge base ID containing the Swagger documentation"
                    }
                },
                "required": ["query", "kbid"]
            }
        }
    },
    "agentic_search": {
        "type": "function",
        "function": {
            "name": "agentic_search",
            "description": "Search for relevant information within a specific knowledge-base using semantic search.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query to find relevant information"
                    },
                    "kbid": {
                        "type": "string",
                        "description": "The knowledge-base ID to search within"
                    }
                },
                "required": ["query", "kbid"],
            }
        }
    }
}


def get(contexts: list, is_web_search: bool = False, mode: str = "NORMAL") -> list:
    """
    Returns a deduplicated list of tools based on provided contexts and web search flag.
    
    Args:
        contexts: List of context dictionaries containing type information
        is_web_search: Boolean flag to include web search tool
        mode: Mode string to include additional tools like agentic_search in PRO mode
        
    Returns:
        List of unique tool dictionaries (deduplicated by function name)
    """
    # print(f"Getting tools list for contexts: {contexts}")

    # Early return for empty contexts unless web search is enabled
    if not contexts and not is_web_search and mode != "PRO":
        return []

    # Build initial tools list using list comprehension
    tools_list = [
        tool for context in (contexts or [])
        if (tool := TOOLS_LIST.get(context["type"])) is not None
    ]

    # Add websearch tool if requested
    if is_web_search:
        if (web_tool := TOOLS_LIST.get("websearch")):
            tools_list.append(web_tool)

    # Add agentic_search tool if in PRO mode
    if mode == "PRO":
        if (agentic_tool := TOOLS_LIST.get("agentic_search")):
            tools_list.append(agentic_tool)

    # Deduplicate tools by function name using dict for O(1) lookup
    unique_tools_dict = {}
    for tool in tools_list:
        function_name = tool["function"]["name"]
        if function_name not in unique_tools_dict:
            unique_tools_dict[function_name] = tool

    unique_tools = list(unique_tools_dict.values())

    print(f"Returning tools list: {unique_tools}")
    return unique_tools


# Example usage and test
# if __name__ == "__main__":
#     # Test case: git, codebase, and web search
#     test_contexts = [
#         {"type": "git"},
#         {"type": "codebase"},
#         {"type": "docs"}
#     ]
    
#     result = get(test_contexts, is_web_search=True)
#     print("\nTest Result:")
#     for tool in result:
#         print(f"- {tool['function']['name']}")
    
    # Expected output: context_search, web_search (only 2 tools, not 3)