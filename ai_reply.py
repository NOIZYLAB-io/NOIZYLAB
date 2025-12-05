"""
NoizyChat AI Reply Engine
=========================
Generates AI responses based on context and personas.
"""

from typing import Dict, Optional
from .models import ChatMessage, SenderType


# AI Persona templates
AI_PERSONAS = {
    "assistant": {
        "name": "Noizy Assistant",
        "style": "helpful",
        "greeting": "Hey Rob, how can I help?",
    },
    "technician": {
        "name": "Noizy Tech",
        "style": "technical",
        "greeting": "Ready for diagnostics. What's the issue?",
    },
    "friend": {
        "name": "Noizy Friend",
        "style": "casual",
        "greeting": "What's up? Let's chat!",
    },
    "coach": {
        "name": "Noizy Coach",
        "style": "motivational",
        "greeting": "Let's make today amazing!",
    },
    "calm": {
        "name": "Noizy Calm",
        "style": "soothing",
        "greeting": "Take a breath. I'm here.",
    },
}


def ai_reply(msg: ChatMessage, persona: str = "assistant") -> str:
    """
    Generate an AI reply based on message content and context.
    """
    text_lower = msg.text.lower()
    context = msg.context or {}
    
    # Help requests
    if "help" in text_lower:
        return "Sure Rob, what do you need help with?"
    
    # Client session context
    if context.get("client_session"):
        return "Let me prepare diagnostics for this client session."
    
    # Technical issues
    if any(word in text_lower for word in ["error", "bug", "broken", "fix", "crash"]):
        return "I see there's an issue. Let me analyze what's happening and suggest a fix."
    
    # Task-related
    if any(word in text_lower for word in ["task", "todo", "remind"]):
        return "I'll add that to your task list and set up a reminder."
    
    # Scheduling
    if any(word in text_lower for word in ["schedule", "book", "calendar", "meeting"]):
        return "I can help you schedule that. What time works best?"
    
    # Stress/emotion detection
    if any(word in text_lower for word in ["stressed", "tired", "overwhelmed"]):
        return "I hear you. Let's take it one step at a time. What's the most important thing right now?"
    
    # Greetings
    if any(word in text_lower for word in ["hi", "hello", "hey"]):
        persona_info = AI_PERSONAS.get(persona, AI_PERSONAS["assistant"])
        return persona_info["greeting"]
    
    # Questions
    if "?" in msg.text:
        return "That's a good question. Let me think about that..."
    
    # Acknowledgments
    if any(word in text_lower for word in ["thanks", "thank you", "awesome", "great"]):
        return "You're welcome! Anything else I can help with?"
    
    # Default
    return "Message received. I'm here if you need anything."


def get_contextual_response(msg: ChatMessage, memory_context: Dict = None) -> str:
    """
    Generate a response using memory context.
    """
    response = ai_reply(msg)
    
    if memory_context:
        # Personalize based on memory
        if memory_context.get("user_name"):
            response = response.replace("Rob", memory_context["user_name"])
        
        # Reference past interactions
        if memory_context.get("last_topic"):
            response += f" By the way, how did that {memory_context['last_topic']} go?"
    
    return response


def select_persona(msg: ChatMessage) -> str:
    """
    Select the best AI persona for the conversation.
    """
    context = msg.context or {}
    text_lower = msg.text.lower()
    
    # Technical context
    if context.get("diagnostic") or any(word in text_lower for word in ["fix", "error", "debug"]):
        return "technician"
    
    # Stress/calm context
    if context.get("calm_mode") or any(word in text_lower for word in ["stressed", "anxious", "overwhelmed"]):
        return "calm"
    
    # Motivational context
    if any(word in text_lower for word in ["goal", "achieve", "motivation"]):
        return "coach"
    
    # Casual chat
    if context.get("casual") or any(word in text_lower for word in ["chat", "talk", "hey"]):
        return "friend"
    
    # Default
    return "assistant"


def format_response(text: str, persona: str) -> str:
    """
    Format response based on persona style.
    """
    persona_info = AI_PERSONAS.get(persona, AI_PERSONAS["assistant"])
    style = persona_info["style"]
    
    if style == "technical":
        # More precise language
        text = text.replace("I think", "Analysis indicates")
        text = text.replace("maybe", "possibly")
    
    elif style == "casual":
        # More relaxed language
        text = text.replace("I will", "I'll")
        text = text.replace("cannot", "can't")
    
    elif style == "soothing":
        # Calmer language
        text = text.replace("!", ".")
        text = "Take your time. " + text
    
    return text

