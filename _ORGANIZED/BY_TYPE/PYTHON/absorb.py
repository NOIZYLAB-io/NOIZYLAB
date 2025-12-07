"""
NoizyChat Memory Absorption
===========================
Chats become memories in NoizyMind.
"""

from typing import Dict, Optional
from .models import ChatMessage, SenderType, MessageType


def absorb_message(msg: ChatMessage) -> Dict:
    """
    Absorb a chat message into NoizyMind memory.
    """
    # Import here to avoid circular imports
    try:
        from ..noizymind.encoder import store_memory
    except ImportError:
        # Fallback if NoizyMind not available
        return {"absorbed": False, "reason": "noizymind_not_available"}
    
    # Build memory content
    memory_content = f"{msg.sender}: {msg.text}"
    
    # Build metadata
    meta = {
        "type": "chat",
        "message_id": msg.id,
        "sender": msg.sender,
        "receiver": msg.receiver,
        "sender_type": msg.sender_type.value if isinstance(msg.sender_type, SenderType) else msg.sender_type,
        "timestamp": msg.timestamp,
        "thread_id": msg.thread_id,
    }
    
    # Add context
    if msg.context:
        meta["context"] = msg.context
    
    # Store in memory
    try:
        store_memory(memory_content, meta=meta)
        return {"absorbed": True, "memory_content": memory_content}
    except Exception as e:
        return {"absorbed": False, "error": str(e)}


def should_absorb(msg: ChatMessage) -> bool:
    """
    Determine if a message should be absorbed into memory.
    """
    # Don't absorb system messages
    if msg.sender_type == SenderType.SYSTEM:
        return False
    
    # Don't absorb very short messages
    if len(msg.text) < 5:
        return False
    
    # Don't absorb commands
    if msg.message_type == MessageType.COMMAND:
        return False
    
    # Absorb everything else
    return True


def extract_key_info(msg: ChatMessage) -> Dict:
    """
    Extract key information from a message for memory indexing.
    """
    text_lower = msg.text.lower()
    
    info = {
        "has_question": "?" in msg.text,
        "has_task": any(word in text_lower for word in ["todo", "task", "need to", "should", "must"]),
        "has_emotion": any(word in text_lower for word in ["happy", "sad", "frustrated", "angry", "excited"]),
        "has_client_ref": "client" in text_lower,
        "has_tech_ref": any(word in text_lower for word in ["fix", "repair", "diagnostic", "error", "bug"]),
        "word_count": len(msg.text.split()),
    }
    
    return info


def summarize_thread(messages: list) -> str:
    """
    Summarize a thread for memory storage.
    """
    if not messages:
        return ""
    
    # Get participants
    participants = set()
    for m in messages:
        participants.add(m.sender)
        participants.add(m.receiver)
    
    # Build summary
    summary_parts = [
        f"Conversation between: {', '.join(participants)}",
        f"Messages: {len(messages)}",
        f"Started: {messages[0].timestamp}",
        f"Last: {messages[-1].timestamp}",
    ]
    
    # Add key topics (simple extraction)
    all_text = " ".join(m.text for m in messages)
    if "client" in all_text.lower():
        summary_parts.append("Topic: Client-related")
    if "fix" in all_text.lower() or "repair" in all_text.lower():
        summary_parts.append("Topic: Technical support")
    
    return " | ".join(summary_parts)

