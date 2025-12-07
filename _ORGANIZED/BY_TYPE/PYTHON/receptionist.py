"""NoizyFrontDesk - Main AI Receptionist"""
from datetime import datetime

class FrontDesk:
    """The AI Front Desk Receptionist"""
    
    def __init__(self):
        self.active_conversations = {}
        self.greeting = "Hi! Welcome to NoizyLab. I'm Noizy, your AI assistant. How can I help you today?"
        self.personality = "friendly_professional"
    
    def greet(self, channel="chat"):
        """Generate greeting based on channel"""
        greetings = {
            "chat": "Hi! 👋 Welcome to NoizyLab. I'm Noizy, your AI assistant. How can I help you today?",
            "phone": "Thank you for calling NoizyLab! I'm Noizy, your AI assistant. How may I help you?",
            "email": "Thank you for contacting NoizyLab! I'm Noizy, and I'll be assisting you today.",
        }
        return greetings.get(channel, self.greeting)
    
    def understand_intent(self, message):
        """Understand customer intent from message"""
        message_lower = message.lower()
        
        if any(word in message_lower for word in ["book", "schedule", "appointment", "available"]):
            return "booking"
        if any(word in message_lower for word in ["price", "cost", "how much", "quote"]):
            return "pricing"
        if any(word in message_lower for word in ["slow", "broken", "not working", "problem", "issue", "help"]):
            return "support"
        if any(word in message_lower for word in ["hours", "open", "location", "where"]):
            return "info"
        if any(word in message_lower for word in ["status", "update", "my repair"]):
            return "status"
        
        return "general"
    
    def respond(self, message, context=None):
        """Generate response based on message and context"""
        intent = self.understand_intent(message)
        
        responses = {
            "booking": "I'd be happy to help you book an appointment! What type of device needs service, and what issue are you experiencing?",
            "pricing": "Our pricing depends on the type of service needed. Basic diagnostics start at $50. Can you tell me more about your device and the issue?",
            "support": "I'm sorry to hear you're having trouble! Let me help. What device are you using, and can you describe the problem?",
            "info": "NoizyLab is open Monday-Friday 9am-5pm, Saturday 10am-2pm. We offer both in-home and remote support!",
            "status": "I can check on your repair status. Could you provide your name or ticket number?",
            "general": "Thanks for reaching out! I'm here to help with computer repairs, tech support, and more. What can I assist you with?",
        }
        
        return {
            "intent": intent,
            "response": responses.get(intent, responses["general"]),
            "next_action": self.get_next_action(intent),
        }
    
    def get_next_action(self, intent):
        """Determine next action based on intent"""
        actions = {
            "booking": "collect_device_info",
            "pricing": "collect_device_info",
            "support": "run_prediagnostic",
            "info": "offer_booking",
            "status": "lookup_ticket",
            "general": "clarify_intent",
        }
        return actions.get(intent, "clarify_intent")

FRONT_DESK = FrontDesk()

def handle_inquiry(message, channel="chat", session_id=None):
    """Handle an incoming inquiry"""
    response = FRONT_DESK.respond(message)
    return {
        "session_id": session_id,
        "channel": channel,
        "timestamp": datetime.now().isoformat(),
        **response,
    }

