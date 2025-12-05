from logger.log import logger, LogDB, trace_context, set_trace_id, clear_trace_id
from prompts import PROMPTS
from litellm import acompletion
from typing import Dict, Any
from BASE.services.llm_config import llm_config
import json
import re
from BASE.utils.analytics import send_analytics_background
import time
import asyncio

@logger.catch()
async def auto_action_review(data: Dict[str, Any], session_id: str) -> Dict[str, Any]:
    """Handle auto-action for code review."""
    # logger.info(f"Processing auto-action for code review: {data}")

    language = data["language"]
    file_content = data["file_content"]

    system_prompt = await PROMPTS.get("auto_action_review")
    user_prompt = f"""Review this {language} code:
```
{file_content}
```"""
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    llm_ = llm_config("auto_review")

    st__ = time.time()
    comp_msg = []

    comp_msg.append(messages)

    response = await acompletion(
        base_url=llm_.get("base_url", "https://backend.v3.codemateai.dev/v2"),
        api_key=llm_.get("api_key", session_id),
        model=llm_.get("model", "gpt-4.1-mini"),
        messages=messages,
        temperature=0.1,
    )

    et__ = time.time()

    content = response.choices[0].message.content
    comp_msg.append({"role": "user", "content": content})
    analysis = {}
    

    logger.info(f"content for auto_action_review: {content}")

    try:
        # Parse score
        if "<score>" in content and "</score>" in content:
            try:
                analysis["score"] = int(content.split("<score>")[-1].split("</score>")[0].strip())
            except (ValueError, IndexError):
                logger.warning("Failed to parse score")

        # Parse summary
        if "<summary>" in content and "</summary>" in content:
            analysis["summary"] = content.split("<summary>")[-1].split("</summary>")[0].strip()

        # Parse issues
        issues = []
        if "<issues>" in content and "</issues>" in content:
            issues_section = content.split("<issues>")[-1].split("</issues>")[0].strip()
            
            for block in issues_section.split("<issue>")[1:]:
                if "</issue>" not in block:
                    continue
                    
                issue_content = block.split("</issue>")[0]
                issue = {}
                
                for field in ["severity", "category", "line", "description", "fix"]:
                    tag = f"<{field}>"
                    end_tag = f"</{field}>"
                    if tag in issue_content and end_tag in issue_content:
                        try:
                            value = issue_content.split(tag)[-1].split(end_tag)[0].strip()
                            issue[field] = int(value) if field == "line" else value
                        except (ValueError, IndexError):
                            logger.warning(f"Failed to parse {field}")
                
                if issue:
                    issues.append(issue)

        analysis["issues"] = issues
    except Exception as e:
        logger.warning(f"Failed to parse review content: {str(e)}")
        analysis = {"issues": f"Failed to parse review content: {str(e)}"}

    asyncio.create_task(
            send_analytics_background(et__ - st__, content, comp_msg, "auto_review", False)
        )
    return analysis



@logger.catch()
async def auto_action_security_scan(data: Dict[str, Any], session_id: str) -> Dict[str, Any]:
    """Handle auto-action for code review."""
    # logger.info(f"Processing auto-action for code review: {data}")

    language = data["language"]
    file_content = data["file_content"]
    file_path = data.get("file_path", "unknown")

    system__ = await PROMPTS.get("auto_action_security_scan")
    system_prompt = f"""{system__}
Here's the {language} code to analyze:
<code>
{file_content}
</code>
   """
    user_prompt = f"""File Path: {file_path}
Language: {language}

Code to Scan for Security Vulnerabilities:
```{language}
{file_content}
```

Please perform a comprehensive security analysis following the specified format. Rate each issue's severity on a scale of 1-10."""
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    llm_ = llm_config("auto_security_scan")
    st__ = time.time()
    comp_msg = []
    comp_msg.append(messages)

    response = await acompletion(
        base_url=llm_.get("base_url", "https://backend.v3.codemateai.dev/v2"),
        api_key=llm_.get("api_key", session_id),
        model=llm_.get("model", "gpt-4.1-mini"),
        messages=messages,
        temperature=0.1,
    )
    et__ = time.time()
    content = response.choices[0].message.content
    comp_msg.append({"role": "user", "content": content})
    try:
        overall_eval = content.split("<overall_eval>")[-1].split("</overall_eval>")[0].strip()
    
        # Parse security problems
        problems = []
        problems_section = content.split("<problems>")[-1].split("</problems>")[0].strip()
        
        if problems_section:
            # Process each problem block
            for block in problems_section.split("<problem>")[1:]:  # Skip empty first element
                if "</problem>" not in block:
                    continue
                    
                problem_content = block.split("</problem>")[0]
                problem_data = {}
                
                # Extract problem components using helper function
                for field in ["title", "severity", "description", "target_code_block"]:
                    tag = f"<{field}>"
                    end_tag = f"</{field}>"
                    if tag in problem_content and end_tag in problem_content:
                        problem_data[field] = problem_content.split(tag)[-1].split(end_tag)[0].strip()
                
                if problem_data.get("title"):  # Only add if title exists
                    problems.append(problem_data)
        
        result = {
            "overall_eval": overall_eval,
            "problems_identified": problems
        }
    except Exception as e:
        logger.warning(f"Failed to process security scan content: {str(e)}")
        result = {"overall_eval": "Failed to process security scan content", "problems_identified": []}

    asyncio.create_task(
            send_analytics_background(et__ - st__, content, comp_msg, "auto_security_scan", False)
        )
    return result


@logger.catch()
async def auto_action_auto_apply(data: Dict[str, Any], session_id: str) -> Dict[str, Any]:
    """Handle auto-action for code review."""
    # logger.info(f"Processing auto-action for code review: {data}")

    language = data["language"]
    file_content = data["file_content"]

    system_prompt = await PROMPTS.get("auto_action_auto_apply")


    file_path = data.get("file_path", "unknown")
    fixes_text = data.get("fixes_text", "")

    user_prompt = f"""File Path: {file_path}
Language: {language}

Original Code:
```{language}
{file_content}
```

Fixes to Apply:
{fixes_text}

Please apply the approved fixes"""
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    llm_ = llm_config("auto_apply")
    st__ = time.time()
    comp_msg = []
    comp_msg.append(messages)

    response = await acompletion(
        base_url=llm_.get("base_url", "https://backend.v3.codemateai.dev/v2"),
        api_key=llm_.get("api_key", session_id),
        model=llm_.get("model", "gpt-4.1-mini"),
        messages=messages,
        temperature=0.1,
    )
    et__ = time.time()

    try:
        content = response.choices[0].message.content
        comp_msg.append({"role": "user", "content": content})
        result = {"content": content}
        asyncio.create_task(
            send_analytics_background(et__ - st__, content, comp_msg, "auto_fix_apply", False)
        )
        return result
    except Exception as e:
        logger.warning(f"Failed to process auto-apply content: {str(e)}")
        return {"content": f"Failed to process auto-apply content: {str(e)}"}


@logger.catch()
async def auto_action_fix_suggestions(data: Dict[str, Any], session_id: str) -> Dict[str, Any]:
    """Handle auto-action for code review."""
    # logger.info(f"Processing auto-action for code review: {data}")

    language = data["language"]
    file_content = data["file_content"]
    file_path = data.get("file_path", "unknown")
    title = data.get("title", "Security Issue")
    description = data.get("description", "Security vulnerability found")
    target_code_block = data.get("target_code_block", file_content)

    system__ = await PROMPTS.get("auto_action_fix_suggestions")
    system_prompt = f"""

    {system__}
    Security Issue Details:
- Title: {title}
- Description: {description}
- Language: {language}
- file_content: {file_content}

Original Code to Fix:
<target_code>
{target_code_block}
</target_code>
   """

    user_prompt = f"""File Path: {file_path}
Language: {language}

Current Code:
```{language}
{file_content}
```
Please generate specific, actionable fixes for these issues"""
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    llm_ = llm_config("auto_fix_suggestions")
    st__ = time.time()
    comp_msg = []
    comp_msg.append(messages)
    response = await acompletion(
        base_url=llm_.get("base_url", "https://backend.v3.codemateai.dev/v2"),
        api_key=llm_.get("api_key", session_id),
        model=llm_.get("model", "gpt-4.1-mini"),
        messages=messages,
        temperature=0.1,
    )
    et__ = time.time()

    content = response.choices[0].message.content
    comp_msg.append({"role": "user", "content": content})
    fixes = []

    try:
       if "<fixes>" in content and "</fixes>" in content:
        fixes_section = content.split("<fixes>")[-1].split("</fixes>")[0].strip()

        if fixes_section:
            # Split by <fix> tags and process each one
            fix_blocks = fixes_section.split("<fix>")[1:]  # Skip the first empty element

            for block in fix_blocks:
                if "</fix>" in block:
                    fix_content = block.split("</fix>")[0]

                    # Extract old_code and new_code
                    old_code = ""
                    new_code = ""

                    if "<old_code>" in fix_content and "</old_code>" in fix_content:
                        old_code = fix_content.split("<old_code>")[-1].split("</old_code>")[0].strip()

                    if "<new_code>" in fix_content and "</new_code>" in fix_content:
                        new_code = fix_content.split("<new_code>")[-1].split("</new_code>")[0].strip()

                    if old_code and new_code:  # Only add if we have both parts
                        fixes.append({
                            "old_code": old_code,
                            "new_code": new_code
                        })
        result = {"fixes": fixes}
    except (ValueError, IndexError) as e:
        logger.warning(f"Failed to parse fixes content: {str(e)}")
        result = {"fixes": []}

    asyncio.create_task(
            send_analytics_background(et__ - st__, content, comp_msg, "auto_fix", False)
        )
    return result





@logger.catch()
async def auto_action_document(data: Dict[str, Any], session_id: str) -> Dict[str, Any]:
    """Handle auto-action for code optimization."""
    # logger.info(f"Processing auto-action for code optimization: {data}")

    language = data["language"]
    file_content = data["file_content"]

    system_prompt = await PROMPTS.get("auto_action_docs")
    # logger.info(f"system_prompt for auto_action_document: {system_prompt}")
    
    user_prompt = f"""
```
{file_content}
```"""
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    llm_ = llm_config("auto_document")
    st__ = time.time()
    comp_msg = []
    comp_msg.append(messages)
    response = await acompletion(
        base_url=llm_.get("base_url", "https://backend.v3.codemateai.dev/v2"),
        api_key=llm_.get("api_key", session_id),
        model=llm_.get("model", "gpt-4.1-mini"),
        messages=messages,
        temperature=0.1,
    )

    # logger.info(f"messages docuemnt: {json.dumps(messages, indent=2)}")


    et__ = time.time()
    content = response.choices[0].message.content
    comp_msg.append({"role": "user", "content": content})

    logger.info(f"content for auto_action_document: {content}")

    try:
        cleaned_content = re.sub(r'```\w+\n', '```\n', content)
        result = {'docs': cleaned_content}
    except (ValueError, IndexError) as e:
        result = {'docs': "Error parsing docs content:"}
        logger.warning(f"Failed to parse docs content: {str(e)}")

    asyncio.create_task(
            send_analytics_background(et__ - st__, content, comp_msg, "auto_doc", False)
        )
    return result


@logger.catch()
async def auto_actions(data: Dict[str, Any], session_id: str, operation: str) -> Dict[str, Any]:
    """Handle auto-actions from the watchdog."""

    if operation == "review":
        return await auto_action_review(data, session_id)
    elif operation == "security_scan":
        return await auto_action_security_scan(data, session_id)
    elif operation == "auto_apply":
        return await auto_action_auto_apply(data, session_id)
    elif operation == "fix_suggestions":
        return await auto_action_fix_suggestions(data, session_id)
    elif operation == "document":
        return await auto_action_document(data, session_id)
    else:
        return {"error": "Invalid operation"}
