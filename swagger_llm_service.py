from litellm import acompletion
import json
import re
from typing import List, Dict, Any
from logger.log import logger
from prompts import PROMPTS
from BASE.services.llm_config import llm_config
import xmltodict
from datetime import datetime
import asyncio
from BASE.utils.analytics import send_analytics_background
import time

# Generate timestamp
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")


async def generate_queries(query: str, num_prompts: int = 5) -> List[str]:
    """
    Generate search queries for Swagger API documentation using LLM.

    Args:
        query: User's original query
        llm_config: LLM configuration dict with base_url, api_key, model
        num_prompts: Number of search prompts to generate

    Returns:
        List of generated search prompts
    """
    try:
        logger.info(f"Generating {num_prompts} search queries")

        system_prompt = await PROMPTS.get("swagger_queries")

        user_prompt = f"""Break down the following query into {num_prompts} concise search prompts:

{query}

Generate specific search terms that would help find relevant API endpoints, parameters, and responses."""

        llm_ = llm_config("swagger_generate_query")
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
        st__ = time.time()
        comp_msg = []
        comp_msg.append(messages)
        response = await acompletion(
            base_url=llm_.get("base_url", "https://backend.v3.codemateai.dev/v2"),
            api_key=llm_.get("api_key", ""),
            model=llm_.get("model", "gpt-4.1-mini"),
            messages=messages,
            temperature=0.3,
            stream=False,
        )

        et__ = time.time()

        if hasattr(response, "choices") and len(response.choices) > 0:
            content = response.choices[0].message.content
            comp_msg.append({"role": "user", "content": content})
            # Parse the numbered list response
            sub_prompts = []
            lines = content.strip().split("\n")

            for line in lines:
                line = line.strip()
                if line:
                    # Remove numbering (1., 2., etc.) and clean up
                    cleaned_line = re.sub(r"^\d+\.\s*", "", line)
                    cleaned_line = cleaned_line.strip("- ")
                    if cleaned_line:
                        sub_prompts.append(cleaned_line)

            logger.info(f"Generated {len(sub_prompts)} search queries")
            return sub_prompts[:num_prompts]  # Ensure we don't exceed requested number

        logger.error("No valid response from LLM for query generation")
        asyncio.create_task(
            send_analytics_background(et__ - st__, content, comp_msg, "swagger", False)
        )
        return [query]  # Fallback to original query

    except Exception as e:
        logger.error(f"Error generating search queries: {e}")
        return [query]  # Fallback to original query


async def generate_calls(query: str, search_content_in_yaml: str) -> List[Dict]:
    """
    Generate a sequence of API calls based on a user query and available API endpoints.

    Args:
        query (str): User's original query.
        search_content_in_yaml (str): YAML string containing available endpoints.

    Returns:
        List[Dict]: Parsed list of API call sequences in dictionary format.
    """
    try:
        logger.info(f"Generating API calls for query: {query[:100]}...")

        system_prompt = await PROMPTS.get("swagger_generate_call")

        user_prompt = (
            f"Query:\n{query}\n\n"
            f"Available API endpoints:\n{search_content_in_yaml}\n\n"
            "Return only the XML sequence of calls."
        )

        llm_cfg = llm_config("swagger_generate_call")

        llm_messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

        st__ = time.time()
        comp_msg = []
        comp_msg.append(llm_messages)

        print(f"llm messages : {json.dumps(llm_messages, indent=2)}")

        response = await acompletion(
            base_url=llm_cfg.get("base_url", "https://backend.v3.codemateai.dev/v2"),
            api_key=llm_cfg.get("api_key", ""),
            model=llm_cfg.get("model", "gpt-4.1-mini"),
            messages=llm_messages,
            temperature=0.4,
            stream=False,
        )
        et__ = time.time()

        if not (hasattr(response, "choices") and response.choices):
            logger.warning("No response from LLM.")
            return []

        xml_data = response.choices[0].message.content.strip().strip('"').strip("'")
        comp_msg.append({"role": "user", "content": xml_data})
        print(f"llm response for generate_calls: {xml_data}")

        asyncio.create_task(
            send_analytics_background(et__ - st__, xml_data, comp_msg, "swagger", False)
        )


        return xmltodict.parse(xml_data)

    except Exception as e:
        logger.exception(f"Error generating API calls: {e}")
        return []


async def structure_output(structure_prompt: str, swagger_output: Dict) -> Dict:
    """
    Apply structure formatting to swagger output using LLM.

    Args:
        structure_prompt: Instructions for how to structure the output
        swagger_output: The swagger response to be structured
        llm_config: LLM configuration dict

    Returns:
        Structured output dictionary
    """
    try:
        logger.info("Applying structure to swagger output")

        system_prompt = await PROMPTS.get("swagger_structure_output")

        user_prompt = f"""Structure Instructions: {structure_prompt}

Original Swagger Output:
{json.dumps(swagger_output, indent=2)}

Please reformat this output according to the structure instructions. Return only the JSON result."""

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

        llm_ = llm_config("swagger_structure_output")
        st__ = time.time()

        comp_msg = []
        comp_msg.append(messages)

        response = await acompletion(
            base_url=llm_.get("base_url", "https://backend.v3.codemateai.dev/v2"),
            api_key=llm_.get("api_key", ""),
            model=llm_.get("model", "gpt-4.1-mini"),
            messages=messages,
            temperature=0.2,
            stream=False,
        )
        et__ = time.time()
        if hasattr(response, "choices") and len(response.choices) > 0:
            content = response.choices[0].message.content
            comp_msg.append({"role": "user", "content": content})
            try:
                # Try to parse JSON response
                if content.strip().startswith("{"):
                    structured_output = json.loads(content)
                    logger.info("Successfully applied structure to output")
                    return structured_output
                else:
                    # Try to extract JSON from response
                    json_match = re.search(r"\{.*\}", content, re.DOTALL)
                    if json_match:
                        structured_output = json.loads(json_match.group())
                        logger.info("Successfully applied structure to output")
                        return structured_output

            except json.JSONDecodeError as e:
                logger.warning(f"Failed to parse structured JSON response: {e}")

        logger.warning("Failed to apply structure, returning original output")
        asyncio.create_task(
            send_analytics_background(et__ - st__, content, comp_msg, "swagger", False)
        )
        return swagger_output

    except Exception as e:
        logger.error(f"Error applying structure to output: {e}")
        return swagger_output


async def extract_summary(content: str) -> str:
    """Extract summary from content wrapped in <summary> tags"""
    if "<summary>" in content and "</summary>" in content:
        try:
            summary = content.split("<summary>")[-1].split("</summary>")[0].strip()
            return summary
        except (ValueError, IndexError):
            logger.warning("Failed to extract summary")
    return content


async def get_endpoint_summary_simple(endpoint_dict: dict) -> str:
    """
    Generate a concise summary of an API endpoint using LLM.

    Args:
        endpoint_dict: Dictionary containing endpoint details
        llm_config: LLM configuration dictionary

    Returns:
        Formatted summary string wrapped in <summary> tags
    """
    try:
        logger.info(
            f"Generating summary for endpoint: {json.dumps(endpoint_dict)[:100]}..."
        )

        system_prompt = await PROMPTS.get("swagger_summary")

        user_prompt = f"""Generate a clear, concise summary and practical use cases for this API endpoint.
Focus on key functionality, parameters, and expected outcomes.

STRICT REQUIREMENTS:
- Summary must be 5 lines or less
- Include main purpose, key parameters, and expected response
- Be specific and practical
- Use clear, technical language

Endpoint specification:
{json.dumps(endpoint_dict, indent=2)}

Format: Wrap the summary in <summary> tags."""

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]

        llm_ = llm_config("swagger_generate_summary")
        st__ = time.time()
        comp_msg = []
        comp_msg.append(messages)
        response = await acompletion(
            base_url=llm_.get("base_url", "https://backend.v3.codemateai.dev/v2"),
            api_key=llm_.get("api_key", ""),
            model=llm_.get("model", "gpt-4.1-mini"),
            messages=messages,
            temperature=0.3,
            stream=False,
        )
        et__ = time.time()

        content = response.choices[0].message.content.strip()
        comp_msg.append({"role": "user", "content": content})
        # Ensure proper summary tag wrapping
        summary = await extract_summary(content)
        asyncio.create_task(
            send_analytics_background(et__ - st__, content, comp_msg, "swagger", False)
        )
        return summary

    except Exception as e:
        logger.error(f"Error generating endpoint summary: {e}")
        return "Error generating summary"


async def swagger_query_api(query, results):

    results_xml: list[str] = []
    for result in results:
        metadata = result.payload or {}
        endpoint_str = "<endpoint>\n"
        endpoint_str += f"  <path>{metadata.get('name', '')}</path>\n"
        endpoint_str += f"  <summary>{metadata.get('content', '')}</summary>\n"
        endpoint_str += "</endpoint>"
        results_xml.append(endpoint_str)

    # with open(f"swagger_2_{timestamp}.json", "w") as f:
    #     json.dump(results_xml, f, indent=2)

    system_prompt = await PROMPTS.get("swagger_query_api")

    user_prompt = f"""
Following are the search results from a swagger API spec. Your task is to select the most relevant endpoints paths based on the provided query.

<query>{query}</query>
<data>{results_xml}</data>

Expected output format:
<paths>
path1
path2
path3
</paths>

If the search results are not relevant to the query, return the paths as:
<paths>
</paths>

STRICT INSTRUCTION:
When returning the paths, make sure to return the exact paths as provided. Do not add any other paths.
YOU MUST PROVIDE AT LEAST 2 PATHS IRRESPECTIVE OF THE QUERY.
"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    llm_ = llm_config("swagger_query_api")
    st__ = time.time()
    comp_msg = []
    comp_msg.append(messages)
    print(f"messages inside swagger_query_api: {json.dumps(messages, indent=2)}")

    response = await acompletion(
        base_url=llm_.get("base_url", "https://backend.v3.codemateai.dev/v2"),
        api_key=llm_.get("api_key", ""),
        model=llm_.get("model", "gpt-4.1-mini"),
        messages=messages,
        temperature=0.3,
        stream=False,
    )

    et__ = time.time()

    print(f"response inside swagger_query_api: {response.choices}")
    response = response.choices[0].message.content.strip()
    comp_msg.append({"role": "user", "content": response})

    if "<paths>" in response and "</paths>" in response:
        paths_section = response.split("<paths>")[-1].split("</paths>")[0].strip()
        paths = paths_section.split("\n")
        paths = [path.strip() for path in paths if path.strip()]
        print(f"paths: {paths}")
        asyncio.create_task(
            send_analytics_background(et__ - st__, response, comp_msg, "swagger", False)
        )
        return paths
    else:
        return []


def parse_xml_format_for_generate_swagger_code(text: str) -> dict[str, any]:
    """
    Parse XML-like format with <required_imports> and <code> sections.

    Args:
        text (str): The input text containing XML-like tags

    Returns:
        Dict containing 'required_imports' list and 'code' string
    """
    result = {"required_imports": [], "code": ""}

    # Pattern to match <required_imports>...</required_imports>
    imports_pattern = r"<required_imports>(.*?)</required_imports>"
    imports_match = re.search(imports_pattern, text, re.DOTALL)

    if imports_match:
        imports_content = imports_match.group(1).strip()
        # Split by newlines and filter out empty lines
        imports_list = [
            line.strip() for line in imports_content.split("\n") if line.strip()
        ]
        result["required_imports"] = imports_list

    # Pattern to match <code>...</code>
    code_pattern = r"<code>(.*?)</code>"
    code_match = re.search(code_pattern, text, re.DOTALL)

    if code_match:
        code_content = code_match.group(1).strip()
        result["code"] = code_content

    return result


@logger.catch()
async def generate_swagger_code(
    base_url, endpoint, client_language, custom_instructions
):
    """Generate code for a single endpoint."""

    method = endpoint["method"]
    path = endpoint["path"]
    spec = endpoint["spec"]
    system__ = await PROMPTS.get("swagger_generate_code_imports")

    replacements = {
        "{client_language}": client_language,
        "{path}": path,
        "{method}": method.upper(),
        "{base_url}": base_url,
        "{spec}": json.dumps(spec, indent=2),
    }

    system_prompt = system__
    for key, value in replacements.items():
        system_prompt = system_prompt.replace(key, value)

    if custom_instructions is None or custom_instructions == "":
        user_prompt = "Go ahead and generate the code for the given API endpoint."
    else:
        user_prompt = (
            f"Here are some of my custom instructions as well: {custom_instructions}"
        )
    logger.info(f"Custom instructions provided: {custom_instructions}")

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    llm_ = llm_config("swagger_generate_code_imports")
    st__ = time.time()
    comp_msg = []
    comp_msg.append(messages)
    
    response = await acompletion(
        base_url=llm_.get("base_url", "https://backend.v3.codemateai.dev/v2"),
        api_key=llm_.get("api_key", ""),
        model=llm_.get("model", "gpt-4.1-mini"),
        messages=messages,
        temperature=0.3,
        stream=False,
    )

    et__ = time.time()

    response = response.choices[0].message.content.strip()
    comp_msg.append({"role": "user", "content": response})
    asyncio.create_task(
            send_analytics_background(et__ - st__, response, comp_msg, "swagger", False)
        )
    
    return parse_xml_format_for_generate_swagger_code(response)
