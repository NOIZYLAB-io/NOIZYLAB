from litellm import acompletion
import json
from logger.log import logger, LogDB, trace_context, set_trace_id, clear_trace_id
import time
import traceback
import asyncio
from ..utils.utils import log_memory_usage
import os
from prompts import PROMPTS
from typing import Dict, Any
from BASE.services.tokenizer import truncate_text_by_tokens
from BASE.services.llm_config import llm_config
from BASE.utils.analytics import send_analytics_background


@logger.catch()
async def debug_code(data: Dict[str, Any], session_id: str) -> Dict[str, Any]:
    """
    Analyze and debug code using LLM to identify and fix potential issues.
    
    Args:
        data: Dictionary containing code and configuration
        session_id: Session identifier for tracking and authentication
        
    Returns:
        Dict containing debugged code or error message
    """
    logger.info(f"Starting code analysis for session {session_id}")
    
    # Validate and prepare input code
    if not (code := data.get("code")):
        raise ValueError("Code input is required for analysis")
    
    trimmed_code = truncate_text_by_tokens(code)

    debug_analysis_prompt = await PROMPTS.get("debug_analysis")
    
    # Define analysis criteria
    analysis_prompt = {
        "role": "system",
        "content": debug_analysis_prompt
    }

    llm_ = llm_config("debug_code")
    st__ = time.time()
    comp_msg = []
    # Perform initial code analysis
    analysis_msg = [analysis_prompt, {"role": "user", "content": trimmed_code}]
    comp_msg.append(analysis_msg)
    try:
        analysis_response = await acompletion(
            base_url=llm_.get("base_url", "https://backend.v3.codemateai.dev/v2"),
            api_key=llm_.get("api_key", session_id),
            model=llm_.get("model", "gpt-4.1-mini"),
            messages=analysis_msg,
            temperature=0.1
        )
        analysis = analysis_response.choices[0].message.content
        comp_msg.append({"role": "user", "content": analysis})
    except Exception as e:
        logger.error("Code analysis failed", exc_info=True)
        return {"error": str(e), "phase": "analysis"}

    # Generate optimized code based on analysis

    debug_prompt = await PROMPTS.get("debug_code")
    debug_prompt_system = {
        "role": "system",
        "content": debug_prompt
    }

    debug_msg = [
        debug_prompt_system,
        {"role": "user", "content": f"Analysis:\n{analysis}\n\nCode:\n{trimmed_code}"}
    ]

    comp_msg.append(debug_msg)

    
    try:
        debug_response = await acompletion(
            base_url=llm_.get("base_url", "https://backend.v3.codemateai.dev/v2"),
            api_key=llm_.get("api_key", session_id),
            model=llm_.get("model", "gpt-4.1-mini"),
            messages=debug_msg,
            temperature=0.1
        )

        et__ = time.time()
        debug = debug_response.choices[0].message.content
        comp_msg.append({"role": "user", "content": debug})

        # Send analytics in background - non-blocking
        asyncio.create_task(
            send_analytics_background(et__ - st__, analysis+debug, comp_msg, "debug", False)
        )

        return {
            "debugged_code": debug,
            "analysis": analysis
        }
    except Exception as e:
        logger.error("Code debugging failed", exc_info=True)
        return {"error": str(e), "phase": "debugging"}
    




@logger.catch()
async def optimize_code(data: Dict[str, Any], session_id: str) -> Dict[str, Any]:
    """
    Analyze and debug code using LLM to identify and fix potential issues.
    
    Args:
        data: Dictionary containing code and configuration
        session_id: Session identifier for tracking and authentication
        
    Returns:
        Dict containing debugged code or error message
    """
    logger.info(f"Starting code analysis for session {session_id}")
    
    # Validate and prepare input code
    if not (code := data.get("code")):
        raise ValueError("Code input is required for analysis")
    
    trimmed_code = truncate_text_by_tokens(code)
    
    # Define analysis criteria

    optimize_analysis = await PROMPTS.get("optimize_analysis")

    analysis_prompt = {
        "role": "system",
        "content": optimize_analysis
    }

    llm_ = llm_config("optimize_code")
    st__ = time.time()
    comp_msg = []
    analysis_msg = [analysis_prompt, {"role": "user", "content": trimmed_code}]
    comp_msg.append(analysis_msg)
    # Perform initial code analysis
    try:
        analysis_response = await acompletion(
            base_url=llm_.get("base_url", "https://backend.v3.codemateai.dev/v2"),
            api_key=llm_.get("api_key", session_id),
            model=llm_.get("model", "gpt-4.1-mini"),
            messages=analysis_msg,
            temperature=0.1
        )
        analysis = analysis_response.choices[0].message.content
        comp_msg.append({"role":"user", "content": analysis})
    except Exception as e:
        logger.error("Code analysis failed", exc_info=True)
        return {"error": str(e), "phase": "analysis"}

    # Generate optimized code based on analysis

    optimize_prompt = await PROMPTS.get("optimize_code")

    optimize_prompt_system = {
        "role": "system",
        "content": optimize_prompt
    }

    opt_msg = [
                optimize_prompt_system,
                {"role": "user", "content": f"Analysis:\n{analysis}\n\nCode:\n{trimmed_code}"}
            ]
    
    comp_msg.append(opt_msg)
    
    try:
        optimized_response = await acompletion(
            base_url=llm_.get("base_url", "https://backend.v3.codemateai.dev/v2"),
            api_key=llm_.get("api_key", session_id),
            model=llm_.get("model", "gpt-4.1-mini"),
            messages=opt_msg,
            temperature=0.1
        )

        opt_content = optimized_response.choices[0].message.content
        comp_msg.append({"role":"user", "content": opt_content})
        et__ = time.time()
        # Send analytics in background - non-blocking
        asyncio.create_task(
            send_analytics_background(et__ - st__, opt_content, comp_msg, "optimize", False)
        )

        return opt_content
    except Exception as e:
        logger.error("Code debugging failed", exc_info=True)
        return {"error": str(e), "phase": "debugging"}
    


    


    

@logger.catch()
async def review_code(data: Dict[str, Any], session_id: str) -> Dict[str, Any]:
    """
    Analyze and debug code using LLM to identify and fix potential issues.
    
    Args:
        data: Dictionary containing code and configuration
        session_id: Session identifier for tracking and authentication
        
    Returns:
        Dict containing debugged code or error message
    """
    logger.info(f"Starting code analysis for session {session_id}")
    
    # Validate and prepare input code
    if not (code := data.get("code")):
        raise ValueError("Code input is required for analysis")
    
    trimmed_code = truncate_text_by_tokens(code)
    
    report = {
        "understanding": "",
        "code_eval": "",
        "security_eval": ""
    }

    ru_prompt = await PROMPTS.get("review_understanding")


    messages = [
        {"role": "system", "content": ru_prompt},
        {"role": "user", "content": trimmed_code}
    ]

    llm_ = llm_config("review_code")
    st__ = time.time()

    comp_msg = []
    comp_msg.append(messages)
    
    # Perform initial code analysis
    try:
        response = await acompletion(
            base_url=llm_.get("base_url", "https://backend.v3.codemateai.dev/v2"),
            api_key=llm_.get("api_key", session_id),
            model=llm_.get("model", "gpt-4.1-mini"),
            messages=messages,
            temperature=0.1
        )
        content_und = response.choices[0].message.content
        comp_msg.append({"role":"user", "content": content_und})
        # if there are ```  remove them form starting and ending 
        if content_und.startswith("```"):
            content_und = content_und[3:]
        if content_und.endswith("```"):
            content_und = content_und[:-3]

        report["understanding"]  = content_und
    except Exception as e:
        logger.error("Code analysis failed", exc_info=True)
        return {"error": str(e), "phase": "analysis"}

    # Generate optimized code based on analysis
    rce_prompt = await PROMPTS.get("review_code_eval")
    
    messages = [
        {"role": "system", "content": rce_prompt},
        {"role": "user", "content": rce_prompt},
    ]
    comp_msg.append(messages)
    
    try:
        response = await acompletion(
            base_url=llm_.get("base_url", "https://backend.v3.codemateai.dev/v2"),
            api_key=llm_.get("api_key", session_id),
            model=llm_.get("model", "gpt-4.1-mini"),
            messages=messages,
            temperature=0.1
        )
        content_eval  = response.choices[0].message.content
        comp_msg.append({"role":"user", "content": content_eval})
        if content_eval.startswith("```"):
            content_eval = content_eval[3:]
        if content_eval.endswith("```"):
            content_eval = content_eval[:-3]

        report["code_eval"] = content_eval
    except Exception as e:
        logger.error("Code debugging failed", exc_info=True)
        return {"error": str(e), "phase": "debugging"}
    

    rse_prompt = await PROMPTS.get("review_security_eval")
    
    messages = [
        {"role": "system", "content": rse_prompt},
        {"role": "user", "content": f"CODE:======\n\n{trimmed_code}"}
    ]

    comp_msg.append(messages)

    try:
        response = await acompletion(
            base_url=llm_.get("base_url", "https://backend.v3.codemateai.dev/v2"),
            api_key=llm_.get("api_key", session_id),
            model=llm_.get("model", "gpt-4.1-mini"),
            messages=messages,
            temperature=0.1
        )
        content_report  = response.choices[0].message.content
        comp_msg.append({"role":"user", "content": content_report})
        et__ = time.time()
        if content_report.startswith("```"):
            content_report = content_report[3:]
        if content_report.endswith("```"):
            content_report = content_report[:-3]

        report["security_eval"] = content_report
    except Exception as e:
        logger.error("Code debugging failed", exc_info=True)
        return {"error": str(e), "phase": "debugging"}
    asyncio.create_task(
            send_analytics_background(et__ - st__, content_und+content_eval+content_report, comp_msg, "review", False)
        )
    return report





@logger.catch()
async def test_code(data: Dict[str, Any], session_id: str) -> Dict[str, Any]:
    """
    Analyze and debug code using LLM to identify and fix potential issues.
    
    Args:
        data: Dictionary containing code and configuration
        session_id: Session identifier for tracking and authentication
        
    Returns:
        Dict containing debugged code or error message
    """
    logger.info(f"Starting code analysis for session {session_id}")
    
    # Validate and prepare input code
    if not (code := data.get("code")):
        raise ValueError("Code input is required for analysis")
    
    language = data.get("language", None)
    custom_instruction = data.get("custom_instruction", None)
    file_name = data.get("file_name", None)
    
    trimmed_code = truncate_text_by_tokens(code)
    
    report = {
        "understanding": "",
        "code": ""
    }

    understanding_prompt = await PROMPTS.get("test_understanding")
    
    understanding_content = f"[LANGUAGE]: {language}\n\n[FILE NAME]: {file_name}\n\n[CODE]: {trimmed_code}"
    
    understanding_messages = [
        {"role": "system", "content": understanding_prompt},
        {"role": "user", "content": understanding_content}
    ]

    llm_ = llm_config("test_code")
    st__ = time.time()

    comp_msg = []
    comp_msg.append(understanding_messages)
    
    # Perform initial code analysis
    try:
        response = await acompletion(
            base_url=llm_.get("base_url", "https://backend.v3.codemateai.dev/v2"),
            api_key=llm_.get("api_key", session_id),
            model=llm_.get("model", "gpt-4.1-mini"),
            messages=understanding_messages,
            temperature=0.1
        )
        report["understanding"]  = response.choices[0].message.content
        comp_msg.append({"role": "user", "content": response.choices[0].message.content})
    except Exception as e:
        logger.error("Code analysis failed", exc_info=True)
        return {"error": str(e), "phase": "analysis"}

    # Generate optimized code based on analysis
    testcase_prompt = await PROMPTS.get("test_code")
    
    testcase_content = ""
    if custom_instruction:
        testcase_content += f"[INSTRUCTIONS]: {custom_instruction}\n\n"
        
    testcase_content += f"[LANGUAGE]: {language}\n\n[FILE NAME]: {file_name}\n\n[CODE]: {trimmed_code}\n\n[UNDERSTANDING]: {report['understanding']}"
    
    testcase_messages = [
        {"role": "system", "content": testcase_prompt},
        {"role": "user", "content": testcase_content}
    ]

    comp_msg.append(testcase_messages)
    
    try:
        response = await acompletion(
            base_url=llm_.get("base_url", "https://backend.v3.codemateai.dev/v2"),
            api_key=llm_.get("api_key", session_id),
            model=llm_.get("model", "gpt-4.1-mini"),
            messages=testcase_messages,
            temperature=0.1
        )
        et__ = time.time()
        report["code"]  = response.choices[0].message.content
        comp_msg.append({"role": "user", "content": response.choices[0].message.content})
    except Exception as e:
        logger.error("Code debugging failed", exc_info=True)
        return {"error": str(e), "phase": "debugging"}
    
    asyncio.create_task(
            send_analytics_background(et__ - st__, report["understanding"]+report["code"], comp_msg, "test", False)
        )
    return report










    





