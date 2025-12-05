"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                         MEMORY THREAD                                        ║
║              What Noizy.AI Remembers - Working Memory                        ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
from datetime import datetime

WORKING_MEMORY = {
    "short_term": [],  # Last few minutes
    "session": [],     # Current session
    "important": [],   # Flagged as important
}

MAX_SHORT_TERM = 20
MAX_SESSION = 100

def remember(content, importance="normal", category="general"):
    """Remember something"""
    memory = {
        "content": content,
        "importance": importance,
        "category": category,
        "remembered_at": datetime.now().isoformat(),
        "recall_count": 0,
    }
    
    # Add to short-term
    WORKING_MEMORY["short_term"].append(memory)
    if len(WORKING_MEMORY["short_term"]) > MAX_SHORT_TERM:
        WORKING_MEMORY["short_term"] = WORKING_MEMORY["short_term"][-MAX_SHORT_TERM:]
    
    # Add to session
    WORKING_MEMORY["session"].append(memory)
    if len(WORKING_MEMORY["session"]) > MAX_SESSION:
        WORKING_MEMORY["session"] = WORKING_MEMORY["session"][-MAX_SESSION:]
    
    # If important, also add to important list
    if importance in ["high", "critical"]:
        WORKING_MEMORY["important"].append(memory)
    
    return {"remembered": True, "memory": memory}

def recall(query=None, category=None, limit=5):
    """Recall memories"""
    memories = WORKING_MEMORY["short_term"] + WORKING_MEMORY["important"]
    
    if category:
        memories = [m for m in memories if m["category"] == category]
    
    if query:
        query_lower = query.lower()
        memories = [m for m in memories if query_lower in str(m["content"]).lower()]
    
    # Sort by recency
    memories = sorted(memories, key=lambda x: x["remembered_at"], reverse=True)
    
    # Update recall count
    for m in memories[:limit]:
        m["recall_count"] += 1
    
    return memories[:limit]

def forget(query=None, category=None):
    """Forget memories matching criteria"""
    forgotten = 0
    
    for memory_type in ["short_term", "session", "important"]:
        original_len = len(WORKING_MEMORY[memory_type])
        
        if query:
            WORKING_MEMORY[memory_type] = [
                m for m in WORKING_MEMORY[memory_type] 
                if query.lower() not in str(m["content"]).lower()
            ]
        elif category:
            WORKING_MEMORY[memory_type] = [
                m for m in WORKING_MEMORY[memory_type] 
                if m["category"] != category
            ]
        
        forgotten += original_len - len(WORKING_MEMORY[memory_type])
    
    return {"forgotten": forgotten}

def get_working_memory():
    """Get current working memory state"""
    return {
        "short_term_count": len(WORKING_MEMORY["short_term"]),
        "session_count": len(WORKING_MEMORY["session"]),
        "important_count": len(WORKING_MEMORY["important"]),
    }

def get_important_memories():
    """Get all important memories"""
    return WORKING_MEMORY["important"]

def clear_short_term():
    """Clear short-term memory"""
    WORKING_MEMORY["short_term"] = []
    return {"cleared": "short_term"}

