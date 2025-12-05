from logger.log import logger
from ipc import IPC
from constants import llm_

ipc_ = IPC.connect()


@logger.catch()
def get_model_name(operation: str) -> str:
    """Get the model name for a given operation."""
    if operation == "chat":
        return "openai/sub_chat"
    elif operation == "chat_image":
        return "openai/sub_chat_image"
    elif operation == "swagger":
        return "openai/sub_chat_swagger"
    elif operation == "chat_followup":
        return "openai/sub_chat_followup"
    elif operation == "auto_review":
        return "openai/sub_eval"
    elif operation == "auto_security_scan":
        return "openai/sub_eval"
    elif operation == "auto_apply":
        return "openai/sub_eval"
    elif operation == "auto_fix_suggestions":
        return "openai/sub_eval"
    elif operation == "auto_document":
        return "openai/sub_eval"
    elif operation == "debug_code":
        return "openai/sub_agent"
    elif operation == "optimize_code":
        return "openai/sub_agent"
    elif operation == "review_code":
        return "openai/sub_agent"
    elif operation == "test_code":
        return "openai/sub_agent"
    elif operation == "swagger_generate_query":
        return "openai/sub_swagger_agent"
    elif operation == "swagger_generate_call":
        return "openai/sub_swagger_agent"
    elif operation == "swagger_structure_output":
        return "openai/sub_swagger_agent"
    elif operation == "swagger_generate_summary":
        return "openai/sub_swagger_agent"
    elif operation == "swagger_query_api":
        return "openai/sub_swagger_agent"
    elif operation == "swagger_generate_code_imports":
        return "openai/sub_swagger_agent"
    elif operation == "chat_pro_mode":
        return "openai/cora_chat"
    else:
        return "openai/sub_chat"



def get_model_config(model_name):
    configs = {
        "openai/sub_chat": {
            "context_window": 40000,
            "image_support": False,
            "tools_support": True,
            "variable_temperature": True
        },
        "openai/sub_chat_swagger": {
            "context_window": 128000,
            "image_support": True,
            "tools_support": True,
            "variable_temperature": True
        },
        "openai/sub_chat_followup": {
            "context_window": 128000,
            "image_support": True,
            "tools_support": True,
            "variable_temperature": True
        },
        "openai/sub_chat_image": {
            "context_window": 128000,
            "image_support": True,
            "tools_support": True,
            "variable_temperature": True
        },
        "openai/sub_eval": {
            "context_window": 128000,
            "image_support": True,
            "tools_support": True,
            "variable_temperature": True
        },
        "openai/sub_agent": {
            "context_window": 128000,
            "image_support": True,
            "tools_support": True,
            "variable_temperature": True
        },
        "openai/sub_swagger_agent": {
            "context_window": 128000,
            "image_support": True,
            "tools_support": True,
            "variable_temperature": True
        },
        "ollama/codemate-ai/mini-coder:latest": {
            "context_window": 32000,
            "image_support": False,
            "tools_support": True,
            "variable_temperature": True
        },
        "ollama/codemate-ai/coder:latest": {
            "context_window": 32000,
            "image_support": False,
            "tools_support": True,
            "variable_temperature": True
        },
        "openai/cora_chat": {
            "context_window": 50000,
            "image_support": False,
            "tools_support": True,
            "variable_temperature": True
        }
    }

    return configs.get(model_name, "")

@logger.catch()
def llm_config(operation: str):
    session = ipc_.get("current_session") if ipc_.get("current_session") else None
    if not session:
        logger.error("No session provided for llm config")
        raise ValueError("No session provided for llm config")
    
    model_name = get_model_name(operation)
    model_config = get_model_config(model_name)
    return {
        "base_url": llm_,
        "api_key": session,
        "model": model_name,
        "model_config": model_config
    }