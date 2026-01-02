#!/usr/bin/env python3
"""
Llama Engine for AI Aggregator
Integrates Meta Llama models with the AI Aggregator system
"""

import os
from typing import Dict, Optional
from llama_api import LlamaAPI

class LlamaEngine:
    """Llama API Engine for AI Aggregator"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv('LLAMA_API_KEY', '')
        self.client = None
        self.name = "Llama (Meta)"
        self.enabled = bool(self.api_key)
        
        if self.enabled:
            try:
                self.client = LlamaAPI(self.api_key)
            except Exception as e:
                print(f"Warning: Failed to initialize Llama API: {e}")
                self.enabled = False
    
    async def query(self, prompt: str, model: str = "llama-3.1-8b", **kwargs) -> Dict:
        """Query Llama API"""
        if not self.enabled:
            return {
                "engine": self.name,
                "error": "Llama API not configured",
                "status": "error",
                "timestamp": None
            }
        
        try:
            response = self.client.run({
                "model": model,
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                **kwargs
            })
            
            return {
                "engine": self.name,
                "response": response.get("message", {}).get("content", ""),
                "model": model,
                "status": "success",
                "timestamp": response.get("timestamp")
            }
        except Exception as e:
            return {
                "engine": self.name,
                "error": str(e),
                "status": "error",
                "timestamp": None
            }
