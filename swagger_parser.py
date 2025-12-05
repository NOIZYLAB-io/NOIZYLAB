# Minimal swagger parser with only essential endpoint extraction functionality


def _extract_endpoints(swagger_data):
    """
    Extract standalone endpoints from parsed Swagger data.

    Args:
        swagger_data (dict): Parsed Swagger specification

    Returns:
        list: List of standalone endpoint objects
    """
    endpoints = []

    # Get base path from Swagger data
    base_path = swagger_data.get("basePath", "")

    # Get global produces, consumes, parameters if available
    global_produces = swagger_data.get("produces", [])
    global_consumes = swagger_data.get("consumes", [])



    # Handle OpenAPI v2 (Swagger) and OpenAPI v3 formats
    paths = swagger_data.get("paths", {})

    # Process each path
    for path, path_item in paths.items():
        # Handle path-level parameters
        path_parameters = path_item.get("parameters", [])

        # Process each HTTP method for the path
        for method, operation in path_item.items():
            # Skip non-operation keys
            if method in ["parameters", "$ref"]:
                continue

            # Create standalone endpoint
            endpoint = {
                "path": base_path + path,
                "method": method.upper(),
                "operation_id": operation.get(
                    "operationId", f"{method}_{path}".replace("/", "_")
                ),
                "summary": operation.get("summary", ""),
                "description": operation.get("description", ""),
                "parameters": path_parameters + operation.get("parameters", []),
                "responses": operation.get("responses", {}),
                "consumes": operation.get("consumes", global_consumes),
                "produces": operation.get("produces", global_produces),
                "tags": operation.get("tags", []),
            }

            # Handle OpenAPI v3 requestBody if present
            if "requestBody" in operation:
                endpoint["request_body"] = operation["requestBody"]

            # Include security requirements if present
            if "security" in operation:
                endpoint["security"] = operation["security"]
            elif "security" in swagger_data:
                endpoint["security"] = swagger_data["security"]

            endpoints.append(endpoint)

    return endpoints
