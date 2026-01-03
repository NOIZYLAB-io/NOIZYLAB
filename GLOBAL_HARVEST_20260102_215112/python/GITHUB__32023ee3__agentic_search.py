import json
import xml.etree.ElementTree as ET
from typing import Dict, Any
import requests
from constants import general
from ipc import IPC

ipc_ = IPC.connect()


def xml_to_json(xml_str: str) -> Dict[str, Any]:
    """
    Convert XML string to JSON with specific structure for file monitor service.

    Expected output format:
    {
        "content": {"text": "content_text"},
        "additional_metadata": [
            {"file": "filename", "line_start": start, "line_end": end}
        ]
    }

    Args:
        xml_str: XML string to convert

    Returns:
        Dictionary with the converted structure

    Raises:
        ValueError: If XML is invalid or doesn't contain required elements
    """
    try:
        # Parse the XML string
        root = ET.fromstring(xml_str.strip())

        # Initialize result structure
        result = {"content": {"text": ""}, "references": []}

        # Extract content
        content_elem = root.find("content")
        if content_elem is not None and content_elem.text:
            result["content"]["text"] = content_elem.text.strip()

        # Extract references (optional)
        references_elem = root.find("references")
        if references_elem is not None:
            references = references_elem.findall("reference")

            for ref in references:
                try:
                    file_elem = ref.find("file")
                    lines_elem = ref.find("lines")

                    if file_elem is not None and file_elem.text:
                        filename = file_elem.text.strip()

                        # Extract line information
                        if lines_elem is not None:
                            line_elements = lines_elem.findall("line")
                            if line_elements:
                                # Get line numbers and find min/max
                                line_numbers = []
                                for line_elem in line_elements:
                                    if (
                                        line_elem.text
                                        and line_elem.text.strip().isdigit()
                                    ):
                                        line_numbers.append(int(line_elem.text.strip()))

                                if line_numbers:
                                    metadata_entry = {
                                        "file": filename,
                                        "line_start": min(line_numbers),
                                        "line_end": max(line_numbers),
                                    }
                                    result["additional_metadata"].append(metadata_entry)
                            else:
                                # No line elements, add file without line info
                                metadata_entry = {
                                    "file": filename,
                                    "line_start": None,
                                    "line_end": None,
                                }
                                result["additional_metadata"].append(metadata_entry)
                        else:
                            # No lines element, add file without line info
                            metadata_entry = {
                                "file": filename,
                                "line_start": None,
                                "line_end": None,
                            }
                            result["additional_metadata"].append(metadata_entry)

                except Exception as e:
                    # Log the error but continue processing other references
                    print(f"Warning: Error processing reference: {e}")
                    continue

        return result

    except ET.ParseError as e:
        raise ValueError(f"Invalid XML format: {e}")
    except Exception as e:
        raise ValueError(f"Error processing XML: {e}")


async def process_agentic_search(
    *, query: str, tool_id: str, kbid: str, search_references: any
):
    """
    Process an agentic search request.

    Args:
        query: Search query string
        tool_id: ID of the tool making the request
        kbid: Knowledge base ID
        search_references: SearchReferences object to track search results

    Returns:
        Tuple of (message, search_references)
    """

    session = ipc_.get("current_session") if ipc_.get("current_session") else None
    if not session:
        raise ValueError("Session is required for agentic search authentication")
    try:
        response = requests.post(
            f"{general}/smart/search",
            json={"query": query, "collection_id": kbid},
            headers={
                "Content-Type": "application/json",
                "X-Session": session,
            },
        )

        data = response.json()

        json_data = xml_to_json(data["data"]["content"])

        if json_data:
            for ref in json_data["additional_metadata"]:
                search_references.add_search_result(
                    path=ref["file"], name=ref["file"], content="", type="file"
                )

        status = "success" if json_data else "error"
        if status == "success":
            message = {"status": status, "content": json_data}
        else:
            message = {
                "status": status,
                "content": "No agentic search results found for the specified query",
            }

        return message, search_references
    except Exception as e:
        print(f"Error in process_agentic_search: {e}")
        raise
