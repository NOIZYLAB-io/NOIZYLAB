
import json
import time
import yaml
import requests
from pathlib import Path
from logger.log import logger
from BASE.services.swagger.swagger_parser import _extract_endpoints
from .resolver import resolve_references, generate_endpoint_specs




@logger.catch()
async def swagger_list(data: dict):
    """List Swagger endpoints from various sources

    Args:
        data (dict): Request data with keys:
            - type (str): 'file', 'url', or 'content'
            - value (str): File path, URL, or content string
            - full_specs (bool): Whether to return full specifications

    Returns:
        dict: Result containing endpoints or error message
    """
    request_type = data.get("type")
    request_value = data.get("value")
    full_specs = data.get("full_specs", False)

    logger.info(
        f"Processing Swagger list request - Type: {request_type}, "
        f"Full specs: {full_specs}"
    )

    base_uri = "http://your-api-base-url"
    content = None

    try:
        # Load Swagger content based on type
        content_start = time.time()
        if request_type == "file":
            logger.info(f"Loading Swagger from file: {request_value}")
            file_path = Path(request_value)
            if not file_path.exists():
                raise FileNotFoundError(f"Swagger file not found: {request_value}")


            with open(request_value, "r", encoding="utf-8") as file:
                content = json.loads(file.read())

        elif request_type == "url":
            logger.info(f"Loading Swagger from URL: {request_value}")
            response = requests.get(
                url=request_value,
                headers={"Content-Type": "application/json"},
            )


            if response.status_code == 200:
                content = response.json()
            else:
                logger.error(
                    f"HTTP error fetching Swagger spec: {response.status_code}"
                )
                return {"error": f"HTTP error: {response.status_code}"}

        elif request_type == "content":
            logger.info("Loading Swagger from provided content")
            try:
                content = json.loads(request_value)
            except Exception as e:
                try:
                    # the content is in yaml format. convert it to json
                    content = yaml.safe_load(request_value)
                    content = json.loads(json.dumps(content))
                except Exception as e:
                    logger.error(f"Error loading Swagger content: {e}")
                    return {"error": f"Error loading Swagger content: {e}"}

        else:
            logger.error(f"Invalid request type: {request_type}")
            return {"error": "Invalid type. Must be 'file', 'url', or 'content'"}

        content_time = time.time() - content_start
        logger.debug(f"Content loading completed in {content_time:.3f}s")

        # Process the content
        processing_start = time.time()
        result = None

        if not full_specs:
            # Return simple endpoints list
            logger.debug("Generating simple endpoints list")
            result = _extract_endpoints(swagger_data=content)
            logger.info(f"Extracted {len(result)} endpoints")

        else:
            # Generate full endpoint specifications
            logger.debug("Generating full endpoint specifications")

            resolution_start = time.time()
            resolved_spec = resolve_references(
                swagger_dict=content, base_uri=base_uri
            )
            resolution_time = time.time() - resolution_start
            logger.debug(f"Reference resolution completed in {resolution_time:.3f}s")

            spec_generation_start = time.time()
            spec_list = generate_endpoint_specs(resolved_spec)
            spec_generation_time = time.time() - spec_generation_start
            logger.debug(f"Spec generation completed in {spec_generation_time:.3f}s")

            specs = []
            for spec in spec_list:
                specs.append(
                    {
                        "path": spec["path"],
                        "method": spec["method"],
                        "spec": spec["spec"],
                    }
                )
            result = specs
            logger.info(f"Generated full specs for {len(specs)} endpoints")

        processing_time = time.time() - processing_start
        # Log operation statistics

        logger.info(
            f"Swagger list request completed - "
            f"Type: {request_type}, Full specs: {full_specs}, "
            f"Processing time: {processing_time:.3f}s, "
        )

        return result

    except json.JSONDecodeError as e:
        return {"error": "Invalid JSON format"}

    except Exception as e:
        return {"error": str(e)}
