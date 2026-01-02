#!/usr/bin/env python3
"""
AI Chat Interface for NoizyLab
===============================
Chat with your system using natural language
"""

import os
import json
from datetime import datetime
from typing import List, Dict, Optional
import psutil
import sqlite3
from pathlib import Path
import requests


class NoizyLabAIChat:
    """Chat interface for NoizyLab system"""
    
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.conversation_history = []
        self.system_prompt = """You are NoizyLab AI Assistant - an expert system administrator.
You help users manage their NoizyLab infrastructure.
You can:
- Check system status
- Diagnose issues
- Provide recommendations
- Execute commands (when confirmed)
- Explain system metrics
- Plan capacity
- Analyze alerts

Be concise, helpful, and action-oriented."""
        
    def chat(self, user_message: str) -> str:
        """
        Chat with AI about your system
        
        Args:
            user_message: User's question or command
        
        Returns:
            AI response
        """
        # Add to conversation history
        self.conversation_history.append({
            "role": "user",
            "content": user_message
        })
        
        # Get system context
        context = self._get_system_context()
        
        # Build prompt with context
        full_message = f"""User: {user_message}

Current System State:
{context}

Respond helpfully and concisely."""
        
        # Get AI response
        response = self._query_ai(full_message)
        
        # Add to history
        self.conversation_history.append({
            "role": "assistant",
            "content": response
        })
        
        # Keep history manageable
        if len(self.conversation_history) > 20:
            self.conversation_history = self.conversation_history[-20:]
        
        return response
    
    def _query_ai(self, message: str) -> str:
        """Query AI with context"""
        if not self.api_key:
            return self._smart_fallback(message)
        
        try:
            messages = [{"role": "system", "content": self.system_prompt}]
            messages.extend(self.conversation_history[:-1])  # Previous conversation
            messages.append({"role": "user", "content": message})
            
            response = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {self.api_key}"},
                json={
                    "model": "gpt-4o-mini",
                    "messages": messages,
                    "max_tokens": 500,
                    "temperature": 0.7
                },
                timeout=20
            )
            
            if response.status_code == 200:
                return response.json()["choices"][0]["message"]["content"]
        except:
            pass
        
        return self._smart_fallback(message)
    
    def _smart_fallback(self, message: str) -> str:
        """Smart fallback without AI"""
        message_lower = message.lower()
        
        # Status queries
        if any(word in message_lower for word in ["status", "how", "doing", "health"]):
            cpu = psutil.cpu_percent()
            mem = psutil.virtual_memory().percent
            disk = psutil.disk_usage('/').percent
            
            return f"""System Status:
- CPU: {cpu:.1f}% {'🟢' if cpu < 70 else '🟡' if cpu < 90 else '🔴'}
- Memory: {mem:.1f}% {'🟢' if mem < 75 else '🟡' if mem < 90 else '🔴'}
- Disk: {disk:.1f}% {'🟢' if disk < 80 else '🟡' if disk < 95 else '🔴'}

Overall: {'Healthy' if cpu < 70 and mem < 75 else 'Needs Attention'}"""
        
        # Service queries
        elif any(word in message_lower for word in ["service", "running", "down"]):
            return "To check services, run: python3 noizylab_cli.py status"
        
        # Help
        elif "help" in message_lower:
            return """I can help you with:
- System status and health
- Service management
- Performance analysis
- Capacity planning
- Alert diagnosis
- Log analysis

Try asking:
- "What's the system status?"
- "Why is CPU high?"
- "When will disk be full?"
- "Analyze recent alerts"
"""
        
        # Default
        else:
            return "I need OpenAI API key for advanced chat. Set OPENAI_API_KEY environment variable, or ask about system status/services."
    
    def _get_system_context(self) -> str:
        """Get current system context"""
        try:
            context = {
                "timestamp": datetime.now().isoformat(),
                "cpu_percent": psutil.cpu_percent(),
                "memory_percent": psutil.virtual_memory().percent,
                "disk_percent": psutil.disk_usage('/').percent,
                "load_avg": psutil.getloadavg() if hasattr(psutil, 'getloadavg') else None
            }
            
            # Check services
            services = {}
            service_ports = {
                "Slack API": 8003,
                "Network Agent": 8005,
                "Master Dashboard": 8501
            }
            
            for name, port in service_ports.items():
                try:
                    import socket
                    sock = socket.socket()
                    sock.settimeout(0.5)
                    result = sock.connect_ex(('localhost', port))
                    sock.close()
                    services[name] = "running" if result == 0 else "down"
                except:
                    services[name] = "unknown"
            
            context["services"] = services
            
            return json.dumps(context, indent=2)
        except:
            return "{}"


def interactive_chat():
    """Start interactive chat session"""
    print("🤖 NoizyLab AI Assistant")
    print("=" * 50)
    print("Chat with your system! Type 'exit' to quit.\n")
    
    chat = NoizyLabAIChat()
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print("\n👋 Goodbye!")
                break
            
            if not user_input:
                continue
            
            response = chat.chat(user_input)
            print(f"\n🤖 AI: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}\n")


if __name__ == "__main__":
    interactive_chat()

