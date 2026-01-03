#!/usr/bin/env python3
"""
AI Engine Aggregator - Main Flask Application
Sends prompts to multiple AI engines simultaneously and displays responses
"""

from flask import Flask, render_template, request, jsonify, Response, stream_with_context
from flask_cors import CORS
import asyncio
import aiohttp
import os
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import concurrent.futures
import re
import math

app = Flask(__name__)
CORS(app)

# Load configuration
CONFIG_FILE = 'config.json'
DEFAULT_CONFIG = {
    "openai": {"api_key": "", "enabled": True, "display_name": "ChatGPT (GPT-4)"},
    "anthropic": {"api_key": "", "enabled": True, "display_name": "Claude (Anthropic)"},
    "google": {"api_key": "", "enabled": True, "display_name": "Gemini (Google)"},
    "github_copilot": {"api_key": "", "enabled": False, "display_name": "GitHub Copilot Pro"},
    "windsurf": {"api_key": "", "enabled": False, "display_name": "Windsurf AI"},
    "vscode_insiders": {"api_key": "", "enabled": False, "display_name": "VS Code Insiders AI"},
    "cursor": {"api_key": "", "enabled": False, "display_name": "Cursor AI (Auto)", "is_local": True},
    "mistral": {"api_key": "", "enabled": False, "display_name": "Mistral AI"},
    "perplexity": {"api_key": "", "enabled": False, "display_name": "Perplexity"},
    "cohere": {"api_key": "", "enabled": False, "display_name": "Cohere"},
    "xai": {"api_key": "", "enabled": False, "display_name": "Grok (xAI)"},
    "openrouter": {"api_key": "", "enabled": False, "display_name": "OpenRouter (Multi-Model)"}
}

def load_config():
    """Load configuration from file or create default"""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return DEFAULT_CONFIG.copy()

def save_config(config):
    """Save configuration to file"""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=2)

config = load_config()

# Subscription monitoring
SUBSCRIPTION_FILE = 'subscriptions.json'
USAGE_FILE = 'usage.json'

def load_subscriptions():
    """Load subscription/service level information"""
    if os.path.exists(SUBSCRIPTION_FILE):
        with open(SUBSCRIPTION_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_subscriptions(subscriptions):
    """Save subscription information"""
    with open(SUBSCRIPTION_FILE, 'w') as f:
        json.dump(subscriptions, f, indent=2)

def load_usage():
    """Load usage statistics"""
    if os.path.exists(USAGE_FILE):
        with open(USAGE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_usage(usage):
    """Save usage statistics"""
    with open(USAGE_FILE, 'w') as f:
        json.dump(usage, f, indent=2)

def update_usage(engine_name: str, tokens_used: int = 0, cost: float = 0.0):
    """Update usage statistics for an engine"""
    usage = load_usage()
    today = datetime.now().strftime("%Y-%m-%d")
    
    if engine_name not in usage:
        usage[engine_name] = {
            "daily": {},
            "monthly": {},
            "total": {"requests": 0, "tokens": 0, "cost": 0.0}
        }
    
    if today not in usage[engine_name]["daily"]:
        usage[engine_name]["daily"][today] = {"requests": 0, "tokens": 0, "cost": 0.0}
    
    usage[engine_name]["daily"][today]["requests"] += 1
    usage[engine_name]["daily"][today]["tokens"] += tokens_used
    usage[engine_name]["daily"][today]["cost"] += cost
    
    # Update monthly stats
    month = datetime.now().strftime("%Y-%m")
    if month not in usage[engine_name]["monthly"]:
        usage[engine_name]["monthly"][month] = {"requests": 0, "tokens": 0, "cost": 0.0}
    
    usage[engine_name]["monthly"][month]["requests"] += 1
    usage[engine_name]["monthly"][month]["tokens"] += tokens_used
    usage[engine_name]["monthly"][month]["cost"] += cost
    
    # Update total
    usage[engine_name]["total"]["requests"] += 1
    usage[engine_name]["total"]["tokens"] += tokens_used
    usage[engine_name]["total"]["cost"] += cost
    
    save_usage(usage)

async def check_subscription_status(engine_name: str, api_key: str) -> Dict:
    """Check subscription status for an AI engine"""
    subscriptions = load_subscriptions()
    engine_config = subscriptions.get(engine_name, {})
    
    status = {
        "engine": engine_name,
        "plan": engine_config.get("plan", "Unknown"),
        "tier": engine_config.get("tier", "Free"),
        "status": "active",
        "limits": engine_config.get("limits", {}),
        "billing": engine_config.get("billing", {}),
        "last_checked": datetime.now().isoformat()
    }
    
    # Try to fetch real-time status from API if supported
    try:
        if engine_name == "openai":
            async with aiohttp.ClientSession() as session:
                headers = {"Authorization": f"Bearer {api_key}"}
                async with session.get(
                    "https://api.openai.com/v1/usage",
                    headers=headers,
                    timeout=aiohttp.ClientTimeout(total=10)
                ) as response:
                    if response.status == 200:
                        data = await response.json()
                        status["api_status"] = "connected"
                        status["usage"] = data
        elif engine_name == "anthropic":
            # Anthropic doesn't have a public usage API, use configured data
            status["api_status"] = "configured"
        elif engine_name == "google":
            status["api_status"] = "configured"
        else:
            status["api_status"] = "configured"
    except:
        status["api_status"] = "error"
    
    return status

class AIEngine:
    """Base class for AI engine integrations"""
    
    def __init__(self, name: str, api_key: str, enabled: bool = True):
        self.name = name
        self.api_key = api_key
        self.enabled = enabled
    
    async def query(self, prompt: str) -> Dict:
        """Query the AI engine and return response"""
        raise NotImplementedError

class OpenAIEngine(AIEngine):
    """OpenAI GPT integration"""
    
    async def query(self, prompt: str) -> Dict:
        if not self.api_key:
            return {"error": "API key not configured", "engine": self.name}
        
        try:
            async with aiohttp.ClientSession() as session:
                headers = {
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                }
                payload = {
                    "model": "gpt-4",
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.7
                }
                
                async with session.post(
                    "https://api.openai.com/v1/chat/completions",
                    headers=headers,
                    json=payload,
                    timeout=aiohttp.ClientTimeout(total=60)
                ) as response:
                    data = await response.json()
                    if response.status == 200:
                        return {
                            "engine": self.name,
                            "response": data["choices"][0]["message"]["content"],
                            "model": data["model"],
                            "status": "success",
                            "timestamp": datetime.now().isoformat()
                        }
                    else:
                        return {
                            "engine": self.name,
                            "error": data.get("error", {}).get("message", "Unknown error"),
                            "status": "error",
                            "timestamp": datetime.now().isoformat()
                        }
        except Exception as e:
            return {
                "engine": self.name,
                "error": str(e),
                "status": "error",
                "timestamp": datetime.now().isoformat()
            }

class AnthropicEngine(AIEngine):
    """Anthropic Claude integration"""
    
    async def query(self, prompt: str) -> Dict:
        if not self.api_key:
            return {"error": "API key not configured", "engine": self.name}
        
        try:
            async with aiohttp.ClientSession() as session:
                headers = {
                    "x-api-key": self.api_key,
                    "anthropic-version": "2023-06-01",
                    "Content-Type": "application/json"
                }
                payload = {
                    "model": "claude-3-opus-20240229",
                    "max_tokens": 4096,
                    "messages": [{"role": "user", "content": prompt}]
                }
                
                async with session.post(
                    "https://api.anthropic.com/v1/messages",
                    headers=headers,
                    json=payload,
                    timeout=aiohttp.ClientTimeout(total=60)
                ) as response:
                    data = await response.json()
                    if response.status == 200:
                        return {
                            "engine": self.name,
                            "response": data["content"][0]["text"],
                            "model": data["model"],
                            "status": "success",
                            "timestamp": datetime.now().isoformat()
                        }
                    else:
                        return {
                            "engine": self.name,
                            "error": data.get("error", {}).get("message", "Unknown error"),
                            "status": "error",
                            "timestamp": datetime.now().isoformat()
                        }
        except Exception as e:
            return {
                "engine": self.name,
                "error": str(e),
                "status": "error",
                "timestamp": datetime.now().isoformat()
            }

class GoogleEngine(AIEngine):
    """Google Gemini integration"""
    
    async def query(self, prompt: str) -> Dict:
        if not self.api_key:
            return {"error": "API key not configured", "engine": self.name}
        
        try:
            async with aiohttp.ClientSession() as session:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={self.api_key}"
                payload = {
                    "contents": [{
                        "parts": [{"text": prompt}]
                    }]
                }
                
                async with session.post(
                    url,
                    json=payload,
                    timeout=aiohttp.ClientTimeout(total=60)
                ) as response:
                    data = await response.json()
                    if response.status == 200:
                        return {
                            "engine": self.name,
                            "response": data["candidates"][0]["content"]["parts"][0]["text"],
                            "model": "gemini-pro",
                            "status": "success",
                            "timestamp": datetime.now().isoformat()
                        }
                    else:
                        return {
                            "engine": self.name,
                            "error": data.get("error", {}).get("message", "Unknown error"),
                            "status": "error",
                            "timestamp": datetime.now().isoformat()
                        }
        except Exception as e:
            return {
                "engine": self.name,
                "error": str(e),
                "status": "error",
                "timestamp": datetime.now().isoformat()
            }

class GitHubCopilotEngine(AIEngine):
    """GitHub Copilot Pro integration"""
    
    async def query(self, prompt: str) -> Dict:
        if not self.api_key:
            return {"error": "API key not configured", "engine": self.name}
        
        try:
            async with aiohttp.ClientSession() as session:
                headers = {
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                    "X-GitHub-Api-Version": "2022-11-28"
                }
                payload = {
                    "model": "copilot-chat",
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.7
                }
                
                async with session.post(
                    "https://api.github.com/copilot/chat/completions",
                    headers=headers,
                    json=payload,
                    timeout=aiohttp.ClientTimeout(total=60)
                ) as response:
                    data = await response.json()
                    if response.status == 200:
                        return {
                            "engine": self.name,
                            "response": data["choices"][0]["message"]["content"],
                            "model": "copilot-chat",
                            "status": "success",
                            "timestamp": datetime.now().isoformat()
                        }
                    else:
                        return {
                            "engine": self.name,
                            "error": data.get("error", {}).get("message", "Unknown error"),
                            "status": "error",
                            "timestamp": datetime.now().isoformat()
                        }
        except Exception as e:
            return {
                "engine": self.name,
                "error": str(e),
                "status": "error",
                "timestamp": datetime.now().isoformat()
            }

class MistralEngine(AIEngine):
    """Mistral AI integration"""
    
    async def query(self, prompt: str) -> Dict:
        if not self.api_key:
            return {"error": "API key not configured", "engine": self.name}
        
        try:
            async with aiohttp.ClientSession() as session:
                headers = {
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                }
                payload = {
                    "model": "mistral-large-latest",
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.7
                }
                
                async with session.post(
                    "https://api.mistral.ai/v1/chat/completions",
                    headers=headers,
                    json=payload,
                    timeout=aiohttp.ClientTimeout(total=60)
                ) as response:
                    data = await response.json()
                    if response.status == 200:
                        return {
                            "engine": self.name,
                            "response": data["choices"][0]["message"]["content"],
                            "model": data["model"],
                            "status": "success",
                            "timestamp": datetime.now().isoformat()
                        }
                    else:
                        return {
                            "engine": self.name,
                            "error": data.get("error", {}).get("message", "Unknown error"),
                            "status": "error",
                            "timestamp": datetime.now().isoformat()
                        }
        except Exception as e:
            return {
                "engine": self.name,
                "error": str(e),
                "status": "error",
                "timestamp": datetime.now().isoformat()
            }

class PerplexityEngine(AIEngine):
    """Perplexity AI integration"""
    
    async def query(self, prompt: str) -> Dict:
        if not self.api_key:
            return {"error": "API key not configured", "engine": self.name}
        
        try:
            async with aiohttp.ClientSession() as session:
                headers = {
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                }
                payload = {
                    "model": "pplx-70b-online",
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.7
                }
                
                async with session.post(
                    "https://api.perplexity.ai/chat/completions",
                    headers=headers,
                    json=payload,
                    timeout=aiohttp.ClientTimeout(total=60)
                ) as response:
                    data = await response.json()
                    if response.status == 200:
                        return {
                            "engine": self.name,
                            "response": data["choices"][0]["message"]["content"],
                            "model": data["model"],
                            "status": "success",
                            "timestamp": datetime.now().isoformat()
                        }
                    else:
                        return {
                            "engine": self.name,
                            "error": data.get("error", {}).get("message", "Unknown error"),
                            "status": "error",
                            "timestamp": datetime.now().isoformat()
                        }
        except Exception as e:
            return {
                "engine": self.name,
                "error": str(e),
                "status": "error",
                "timestamp": datetime.now().isoformat()
            }

class CohereEngine(AIEngine):
    """Cohere integration"""
    
    async def query(self, prompt: str) -> Dict:
        if not self.api_key:
            return {"error": "API key not configured", "engine": self.name}
        
        try:
            async with aiohttp.ClientSession() as session:
                headers = {
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                }
                payload = {
                    "model": "command",
                    "prompt": prompt,
                    "max_tokens": 4096
                }
                
                async with session.post(
                    "https://api.cohere.ai/v1/generate",
                    headers=headers,
                    json=payload,
                    timeout=aiohttp.ClientTimeout(total=60)
                ) as response:
                    data = await response.json()
                    if response.status == 200:
                        return {
                            "engine": self.name,
                            "response": data["generations"][0]["text"],
                            "model": data["model"],
                            "status": "success",
                            "timestamp": datetime.now().isoformat()
                        }
                    else:
                        return {
                            "engine": self.name,
                            "error": data.get("message", "Unknown error"),
                            "status": "error",
                            "timestamp": datetime.now().isoformat()
                        }
        except Exception as e:
            return {
                "engine": self.name,
                "error": str(e),
                "status": "error",
                "timestamp": datetime.now().isoformat()
            }

class WindsurfEngine(AIEngine):
    """Windsurf AI integration - uses OpenAI-compatible API"""
    
    async def query(self, prompt: str) -> Dict:
        if not self.api_key:
            return {"error": "API key not configured", "engine": self.name}
        
        try:
            async with aiohttp.ClientSession() as session:
                headers = {
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                }
                payload = {
                    "model": "gpt-4",
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.7
                }
                
                # Windsurf uses OpenAI-compatible API
                async with session.post(
                    "https://api.windsurf.ai/v1/chat/completions",
                    headers=headers,
                    json=payload,
                    timeout=aiohttp.ClientTimeout(total=60)
                ) as response:
                    if response.status == 200:
                        data = await response.json()
                        return {
                            "engine": self.name,
                            "response": data["choices"][0]["message"]["content"],
                            "model": data.get("model", "windsurf-ai"),
                            "status": "success",
                            "timestamp": datetime.now().isoformat()
                        }
                    else:
                        # Fallback to OpenAI endpoint if Windsurf-specific fails
                        async with session.post(
                            "https://api.openai.com/v1/chat/completions",
                            headers=headers,
                            json=payload,
                            timeout=aiohttp.ClientTimeout(total=60)
                        ) as fallback_response:
                            data = await fallback_response.json()
                            if fallback_response.status == 200:
                                return {
                                    "engine": self.name,
                                    "response": data["choices"][0]["message"]["content"],
                                    "model": data.get("model", "windsurf-ai"),
                                    "status": "success",
                                    "timestamp": datetime.now().isoformat()
                                }
                            else:
                                return {
                                    "engine": self.name,
                                    "error": data.get("error", {}).get("message", "Unknown error"),
                                    "status": "error",
                                    "timestamp": datetime.now().isoformat()
                                }
        except Exception as e:
            return {
                "engine": self.name,
                "error": str(e),
                "status": "error",
                "timestamp": datetime.now().isoformat()
            }

class VSCodeInsidersEngine(AIEngine):
    """VS Code Insiders AI integration"""
    
    async def query(self, prompt: str) -> Dict:
        if not self.api_key:
            return {"error": "API key not configured", "engine": self.name}
        
        try:
            async with aiohttp.ClientSession() as session:
                headers = {
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                }
                payload = {
                    "model": "gpt-4",
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.7
                }
                
                # VS Code Insiders uses OpenAI-compatible API
                async with session.post(
                    "https://api.openai.com/v1/chat/completions",
                    headers=headers,
                    json=payload,
                    timeout=aiohttp.ClientTimeout(total=60)
                ) as response:
                    data = await response.json()
                    if response.status == 200:
                        return {
                            "engine": self.name,
                            "response": data["choices"][0]["message"]["content"],
                            "model": data.get("model", "vscode-ai"),
                            "status": "success",
                            "timestamp": datetime.now().isoformat()
                        }
                    else:
                        return {
                            "engine": self.name,
                            "error": data.get("error", {}).get("message", "Unknown error"),
                            "status": "error",
                            "timestamp": datetime.now().isoformat()
                        }
        except Exception as e:
            return {
                "engine": self.name,
                "error": str(e),
                "status": "error",
                "timestamp": datetime.now().isoformat()
            }

class CursorEngine(AIEngine):
    """Cursor AI (Auto) integration - uses local API or OpenAI-compatible endpoint"""
    
    async def query(self, prompt: str) -> Dict:
        if not self.api_key:
            return {"error": "API key not configured", "engine": self.name}
        
        try:
            async with aiohttp.ClientSession() as session:
                headers = {
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                }
                payload = {
                    "model": "gpt-4",
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.7
                }
                
                # Try Cursor-specific endpoint, fallback to OpenAI
                endpoints = [
                    "https://api.cursor.sh/v1/chat/completions",
                    "https://api.openai.com/v1/chat/completions"
                ]
                
                last_error = None
                for endpoint in endpoints:
                    try:
                        async with session.post(
                            endpoint,
                            headers=headers,
                            json=payload,
                            timeout=aiohttp.ClientTimeout(total=60)
                        ) as response:
                            data = await response.json()
                            if response.status == 200:
                                return {
                                    "engine": self.name,
                                    "response": data["choices"][0]["message"]["content"],
                                    "model": data.get("model", "cursor-ai"),
                                    "status": "success",
                                    "timestamp": datetime.now().isoformat()
                                }
                    except Exception as e:
                        last_error = e
                        continue
                
                return {
                    "engine": self.name,
                    "error": f"Failed to connect: {str(last_error)}",
                    "status": "error",
                    "timestamp": datetime.now().isoformat()
                }
        except Exception as e:
            return {
                "engine": self.name,
                "error": str(e),
                "status": "error",
                "timestamp": datetime.now().isoformat()
            }

class GrokEngine(AIEngine):
    """Grok (xAI) integration"""
    
    async def query(self, prompt: str) -> Dict:
        if not self.api_key:
            return {"error": "API key not configured", "engine": self.name}
        
        try:
            async with aiohttp.ClientSession() as session:
                headers = {
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                }
                payload = {
                    "model": "grok-beta",
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.7
                }
                
                async with session.post(
                    "https://api.x.ai/v1/chat/completions",
                    headers=headers,
                    json=payload,
                    timeout=aiohttp.ClientTimeout(total=60)
                ) as response:
                    data = await response.json()
                    if response.status == 200:
                        return {
                            "engine": self.name,
                            "response": data["choices"][0]["message"]["content"],
                            "model": data.get("model", "grok-beta"),
                            "status": "success",
                            "timestamp": datetime.now().isoformat()
                        }
                    else:
                        return {
                            "engine": self.name,
                            "error": data.get("error", {}).get("message", "Unknown error"),
                            "status": "error",
                            "timestamp": datetime.now().isoformat()
                        }
        except Exception as e:
            return {
                "engine": self.name,
                "error": str(e),
                "status": "error",
                "timestamp": datetime.now().isoformat()
            }

class OpenRouterEngine(AIEngine):
    """OpenRouter integration - access to multiple models"""
    
    async def query(self, prompt: str) -> Dict:
        if not self.api_key:
            return {"error": "API key not configured", "engine": self.name}
        
        try:
            async with aiohttp.ClientSession() as session:
                headers = {
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                    "HTTP-Referer": "https://ai-aggregator.local",
                    "X-Title": "AI Aggregator"
                }
                payload = {
                    "model": "openai/gpt-4",
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0.7
                }
                
                async with session.post(
                    "https://openrouter.ai/api/v1/chat/completions",
                    headers=headers,
                    json=payload,
                    timeout=aiohttp.ClientTimeout(total=60)
                ) as response:
                    data = await response.json()
                    if response.status == 200:
                        return {
                            "engine": self.name,
                            "response": data["choices"][0]["message"]["content"],
                            "model": data.get("model", "openrouter"),
                            "status": "success",
                            "timestamp": datetime.now().isoformat()
                        }
                    else:
                        return {
                            "engine": self.name,
                            "error": data.get("error", {}).get("message", "Unknown error"),
                            "status": "error",
                            "timestamp": datetime.now().isoformat()
                        }
        except Exception as e:
            return {
                "engine": self.name,
                "error": str(e),
                "status": "error",
                "timestamp": datetime.now().isoformat()
            }

def get_engines(selected_engines: List[str]) -> List[AIEngine]:
    """Get initialized AI engines based on configuration"""
    engines = []
    engine_classes = {
        "openai": OpenAIEngine,
        "anthropic": AnthropicEngine,
        "google": GoogleEngine,
        "github_copilot": GitHubCopilotEngine,
        "windsurf": WindsurfEngine,
        "vscode_insiders": VSCodeInsidersEngine,
        "cursor": CursorEngine,
        "mistral": MistralEngine,
        "perplexity": PerplexityEngine,
        "cohere": CohereEngine,
        "xai": GrokEngine,
        "openrouter": OpenRouterEngine
    }
    
    for engine_name in selected_engines:
        if engine_name in config and engine_name in engine_classes:
            engine_config = config[engine_name]
            if engine_config.get("enabled", False) and engine_config.get("api_key"):
                engines.append(
                    engine_classes[engine_name](
                        engine_name,
                        engine_config["api_key"],
                        engine_config.get("enabled", True)
                    )
                )
    
    return engines

async def query_all_engines(engines: List[AIEngine], prompt: str) -> List[Dict]:
    """Query all engines simultaneously"""
    tasks = [engine.query(prompt) for engine in engines]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    # Handle exceptions
    processed_results = []
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            processed_results.append({
                "engine": engines[i].name,
                "error": str(result),
                "status": "error",
                "timestamp": datetime.now().isoformat()
            })
        else:
            processed_results.append(result)
    
    return processed_results

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/api/config', methods=['GET'])
def get_config():
    """Get current configuration"""
    # Don't expose API keys in response
    safe_config = {k: {"enabled": v.get("enabled", False)} for k, v in config.items()}
    return jsonify(safe_config)

@app.route('/api/config', methods=['POST'])
def update_config():
    """Update configuration"""
    global config
    new_config = request.json
    config.update(new_config)
    save_config(config)
    return jsonify({"status": "success"})

@app.route('/api/query', methods=['POST'])
def query_engines():
    """Query selected AI engines"""
    data = request.json
    prompt = data.get('prompt', '')
    selected_engines = data.get('engines', [])
    
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400
    
    if not selected_engines:
        return jsonify({"error": "At least one engine must be selected"}), 400
    
    # Get enabled engines
    engines = get_engines(selected_engines)
    
    if not engines:
        return jsonify({"error": "No valid engines configured"}), 400
    
    # Run async query
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    results = loop.run_until_complete(query_all_engines(engines, prompt))
    loop.close()
    
    # Track usage for successful responses
    for result in results:
        if result.get("status") == "success":
            engine_name = result.get("engine")
            # Estimate tokens (rough approximation: 1 token ≈ 4 characters)
            response_text = result.get("response", "")
            estimated_tokens = len(response_text) // 4
            
            # Estimate cost (varies by engine, using average rates)
            cost_estimates = {
                "openai": 0.03 / 1000,  # GPT-4 pricing
                "anthropic": 0.015 / 1000,  # Claude pricing
                "google": 0.0005 / 1000,  # Gemini pricing
                "mistral": 0.008 / 1000,
                "perplexity": 0.001 / 1000,
                "cohere": 0.0015 / 1000,
                "xai": 0.002 / 1000
            }
            cost_per_token = cost_estimates.get(engine_name, 0.01 / 1000)
            estimated_cost = estimated_tokens * cost_per_token
            
            update_usage(engine_name, estimated_tokens, estimated_cost)
    
    return jsonify({"results": results, "prompt": prompt})

@app.route('/api/engines', methods=['GET'])
def get_available_engines():
    """Get list of available AI engines with their status"""
    engines_info = []
    engine_names = {
        "openai": {"display_name": "ChatGPT (GPT-4)", "icon": "🤖", "category": "primary"},
        "anthropic": {"display_name": "Claude (Anthropic)", "icon": "🧠", "category": "primary"},
        "google": {"display_name": "Gemini (Google)", "icon": "💎", "category": "primary"},
        "github_copilot": {"display_name": "GitHub Copilot Pro", "icon": "⚡", "category": "coding"},
        "windsurf": {"display_name": "Windsurf AI", "icon": "🌊", "category": "coding"},
        "vscode_insiders": {"display_name": "VS Code Insiders AI", "icon": "💻", "category": "coding"},
        "cursor": {"display_name": "Cursor AI (Auto)", "icon": "🎯", "category": "coding"},
        "mistral": {"display_name": "Mistral AI", "icon": "🌊", "category": "recommended"},
        "perplexity": {"display_name": "Perplexity", "icon": "🔍", "category": "recommended"},
        "cohere": {"display_name": "Cohere", "icon": "🌟", "category": "recommended"},
        "xai": {"display_name": "Grok (xAI)", "icon": "🚀", "category": "recommended"},
        "openrouter": {"display_name": "OpenRouter (Multi-Model)", "icon": "🔄", "category": "recommended"}
    }
    
    for engine_id, info in engine_names.items():
        engine_config = config.get(engine_id, {})
        engines_info.append({
            "id": engine_id,
            "display_name": engine_config.get("display_name", info["display_name"]),
            "icon": info["icon"],
            "category": info["category"],
            "enabled": engine_config.get("enabled", False) and bool(engine_config.get("api_key", ""))
        })
    
    return jsonify(engines_info)

@app.route('/api/history', methods=['GET'])
def get_history():
    """Get query history"""
    history_file = 'history.json'
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            return jsonify(json.load(f))
    return jsonify([])

@app.route('/api/history', methods=['POST'])
def save_history():
    """Save query to history"""
    history_file = 'history.json'
    history = []
    if os.path.exists(history_file):
        with open(history_file, 'r') as f:
            history = json.load(f)
    
    entry = request.json
    entry['timestamp'] = datetime.now().isoformat()
    history.insert(0, entry)
    
    # Keep only last 50 entries
    history = history[:50]
    
    with open(history_file, 'w') as f:
        json.dump(history, f, indent=2)
    
    return jsonify({"status": "success"})

@app.route('/api/export', methods=['POST'])
def export_responses():
    """Export responses in various formats"""
    data = request.json
    format_type = data.get('format', 'json')
    responses = data.get('responses', [])
    prompt = data.get('prompt', '')
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if format_type == 'json':
        content = json.dumps({
            "prompt": prompt,
            "timestamp": datetime.now().isoformat(),
            "responses": responses
        }, indent=2)
        filename = f"export_{timestamp}.json"
        return jsonify({"content": content, "filename": filename, "mime": "application/json"})
    
    elif format_type == 'markdown':
        md_content = f"# AI Aggregator Export\n\n**Prompt:** {prompt}\n\n**Timestamp:** {datetime.now().isoformat()}\n\n---\n\n"
        for response in responses:
            engine = response.get('engine', 'Unknown')
            content = response.get('response', response.get('error', ''))
            md_content += f"## {engine}\n\n{content}\n\n---\n\n"
        filename = f"export_{timestamp}.md"
        return jsonify({"content": md_content, "filename": filename, "mime": "text/markdown"})
    
    elif format_type == 'blended':
        # Create a blended response combining all successful responses
        successful_responses = [r for r in responses if r.get('status') == 'success']
        blended = f"# Blended Response\n\n**Original Prompt:** {prompt}\n\n"
        blended += "## Key Insights from All Engines:\n\n"
        
        # Extract key points from each response
        for response in successful_responses:
            engine = response.get('engine', 'Unknown')
            content = response.get('response', '')
            blended += f"### {engine}:\n{content}\n\n---\n\n"
        
        filename = f"blended_{timestamp}.md"
        return jsonify({"content": blended, "filename": filename, "mime": "text/markdown"})
    
    elif format_type == 'csv':
        # Export as CSV
        import csv
        import io
        output = io.StringIO()
        writer = csv.writer(output)
        
        writer.writerow(['Engine', 'Status', 'Response', 'Error', 'Timestamp'])
        for response in responses:
            writer.writerow([
                response.get('engine', ''),
                response.get('status', ''),
                response.get('response', '').replace('\n', ' ').replace('\r', ''),
                response.get('error', ''),
                response.get('timestamp', '')
            ])
        
        filename = f"export_{timestamp}.csv"
        return jsonify({"content": output.getvalue(), "filename": filename, "mime": "text/csv"})
    
    elif format_type == 'html':
        # Export as HTML
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>AI Aggregator Export</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; }}
        .container {{ max-width: 1200px; margin: 0 auto; background: white; padding: 20px; border-radius: 8px; }}
        h1 {{ color: #333; }}
        .prompt {{ background: #f0f0f0; padding: 15px; border-radius: 4px; margin-bottom: 20px; }}
        .response-card {{ border: 1px solid #ddd; border-radius: 4px; padding: 15px; margin-bottom: 15px; }}
        .response-header {{ display: flex; justify-content: space-between; margin-bottom: 10px; }}
        .engine-name {{ font-weight: bold; color: #6366f1; }}
        .status-success {{ color: #10b981; }}
        .status-error {{ color: #ef4444; }}
        .response-content {{ white-space: pre-wrap; word-wrap: break-word; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>AI Engine Aggregator Export</h1>
        <div class="prompt">
            <strong>Original Prompt:</strong><br>
            {escapeHtml(prompt)}
        </div>
"""
        
        for response in responses:
            engine = response.get('engine', 'Unknown')
            status = response.get('status', 'error')
            content = response.get('response') or response.get('error', '')
            
            html_content += f"""
        <div class="response-card">
            <div class="response-header">
                <span class="engine-name">{escapeHtml(engine)}</span>
                <span class="status-{status}">{status.upper()}</span>
            </div>
            <div class="response-content">{escapeHtml(content)}</div>
        </div>
"""
        
        html_content += """
    </div>
</body>
</html>
"""
        
        filename = f"export_{timestamp}.html"
        return jsonify({"content": html_content, "filename": filename, "mime": "text/html"})
    
    elif format_type == 'text':
        # Plain text export
        text_content = f"AI ENGINE AGGREGATOR EXPORT\n"
        text_content += f"{'='*50}\n\n"
        text_content += f"Original Prompt:\n{prompt}\n\n"
        text_content += f"{'='*50}\n\n"
        
        for response in responses:
            engine = response.get('engine', 'Unknown')
            status = response.get('status', 'error')
            content = response.get('response') or response.get('error', '')
            
            text_content += f"Engine: {engine}\n"
            text_content += f"Status: {status}\n"
            text_content += f"{'-'*50}\n"
            text_content += f"{content}\n\n"
            text_content += f"{'='*50}\n\n"
        
        filename = f"export_{timestamp}.txt"
        return jsonify({"content": text_content, "filename": filename, "mime": "text/plain"})
    
    return jsonify({"error": "Invalid format"}), 400

def escapeHtml(text):
    """Escape HTML special characters"""
    if not text:
        return ""
    return (str(text)
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
            .replace('"', "&quot;")
            .replace("'", "&#x27;"))

@app.route('/api/subscriptions', methods=['GET'])
def get_subscriptions():
    """Get subscription information for all engines"""
    subscriptions = load_subscriptions()
    usage = load_usage()
    
    # Build subscription status for each configured engine
    subscription_status = []
    for engine_id, engine_config in config.items():
        if engine_config.get("enabled") and engine_config.get("api_key"):
            sub_info = subscriptions.get(engine_id, {})
            usage_info = usage.get(engine_id, {})
            
            # Calculate current month usage
            current_month = datetime.now().strftime("%Y-%m")
            month_usage = usage_info.get("monthly", {}).get(current_month, {})
            
            subscription_status.append({
                "engine": engine_id,
                "display_name": engine_config.get("display_name", engine_id),
                "plan": sub_info.get("plan", "Not Set"),
                "tier": sub_info.get("tier", "Unknown"),
                "status": sub_info.get("status", "active"),
                "limits": sub_info.get("limits", {}),
                "billing": sub_info.get("billing", {}),
                "usage": {
                    "monthly": month_usage,
                    "total": usage_info.get("total", {})
                },
                "last_updated": sub_info.get("last_updated", datetime.now().isoformat())
            })
    
    return jsonify(subscription_status)

@app.route('/api/subscriptions', methods=['POST'])
def update_subscription():
    """Update subscription information for an engine"""
    data = request.json
    engine_id = data.get('engine')
    
    if not engine_id:
        return jsonify({"error": "Engine ID is required"}), 400
    
    subscriptions = load_subscriptions()
    
    if engine_id not in subscriptions:
        subscriptions[engine_id] = {}
    
    # Update subscription info
    subscriptions[engine_id].update({
        "plan": data.get('plan', subscriptions[engine_id].get('plan', 'Unknown')),
        "tier": data.get('tier', subscriptions[engine_id].get('tier', 'Free')),
        "limits": data.get('limits', subscriptions[engine_id].get('limits', {})),
        "billing": data.get('billing', subscriptions[engine_id].get('billing', {})),
        "status": data.get('status', 'active'),
        "last_updated": datetime.now().isoformat()
    })
    
    save_subscriptions(subscriptions)
    return jsonify({"status": "success", "subscription": subscriptions[engine_id]})

@app.route('/api/subscriptions/<engine_id>/check', methods=['POST'])
async def check_subscription(engine_id):
    """Check subscription status for a specific engine"""
    engine_config = config.get(engine_id)
    if not engine_config or not engine_config.get("api_key"):
        return jsonify({"error": "Engine not configured"}), 400
    
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    status = await check_subscription_status(engine_id, engine_config["api_key"])
    loop.close()
    
    return jsonify(status)

@app.route('/api/usage', methods=['GET'])
def get_usage():
    """Get usage statistics"""
    usage = load_usage()
    subscriptions = load_subscriptions()
    
    # Enhance usage data with subscription limits
    enhanced_usage = {}
    for engine_id, usage_data in usage.items():
        sub_info = subscriptions.get(engine_id, {})
        limits = sub_info.get("limits", {})
        
        current_month = datetime.now().strftime("%Y-%m")
        month_usage = usage_data.get("monthly", {}).get(current_month, {})
        
        enhanced_usage[engine_id] = {
            "daily": usage_data.get("daily", {}),
            "monthly": usage_data.get("monthly", {}),
            "total": usage_data.get("total", {}),
            "current_month": month_usage,
            "limits": limits,
            "utilization": calculate_utilization(month_usage, limits)
        }
    
    return jsonify(enhanced_usage)

def calculate_utilization(usage: Dict, limits: Dict) -> Dict:
    """Calculate utilization percentage"""
    utilization = {}
    
    # Check token limits
    if "tokens_per_month" in limits:
        tokens_used = usage.get("tokens", 0)
        tokens_limit = limits["tokens_per_month"]
        utilization["tokens"] = {
            "used": tokens_used,
            "limit": tokens_limit,
            "percentage": min(100, (tokens_used / tokens_limit * 100) if tokens_limit > 0 else 0)
        }
    
    # Check request limits
    if "requests_per_month" in limits:
        requests_used = usage.get("requests", 0)
        requests_limit = limits["requests_per_month"]
        utilization["requests"] = {
            "used": requests_used,
            "limit": requests_limit,
            "percentage": min(100, (requests_used / requests_limit * 100) if requests_limit > 0 else 0)
        }
    
    # Check cost limits
    if "cost_per_month" in limits:
        cost_used = usage.get("cost", 0.0)
        cost_limit = limits["cost_per_month"]
        utilization["cost"] = {
            "used": cost_used,
            "limit": cost_limit,
            "percentage": min(100, (cost_used / cost_limit * 100) if cost_limit > 0 else 0)
        }
    
    return utilization

@app.route('/api/dashboard', methods=['GET'])
def get_dashboard():
    """Get comprehensive dashboard data"""
    subscriptions = load_subscriptions()
    usage = load_usage()
    
    # Calculate totals
    total_cost_this_month = 0.0
    total_requests_this_month = 0
    total_tokens_this_month = 0
    current_month = datetime.now().strftime("%Y-%m")
    
    active_subscriptions = []
    for engine_id, engine_config in config.items():
        if engine_config.get("enabled") and engine_config.get("api_key"):
            sub_info = subscriptions.get(engine_id, {})
            usage_info = usage.get(engine_id, {})
            month_usage = usage_info.get("monthly", {}).get(current_month, {})
            
            total_cost_this_month += month_usage.get("cost", 0.0)
            total_requests_this_month += month_usage.get("requests", 0)
            total_tokens_this_month += month_usage.get("tokens", 0)
            
            active_subscriptions.append({
                "engine": engine_id,
                "display_name": engine_config.get("display_name", engine_id),
                "plan": sub_info.get("plan", "Not Set"),
                "monthly_cost": month_usage.get("cost", 0.0),
                "monthly_requests": month_usage.get("requests", 0),
                "monthly_tokens": month_usage.get("tokens", 0),
                "status": sub_info.get("status", "active")
            })
    
    # Calculate daily usage for last 7 days
    daily_usage = []
    for i in range(6, -1, -1):
        date = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
        day_cost = 0.0
        day_requests = 0
        for engine_id, usage_info in usage.items():
            day_data = usage_info.get("daily", {}).get(date, {})
            day_cost += day_data.get("cost", 0.0)
            day_requests += day_data.get("requests", 0)
        daily_usage.append({
            "date": date,
            "cost": day_cost,
            "requests": day_requests
        })
    
    return jsonify({
        "summary": {
            "total_cost_this_month": round(total_cost_this_month, 2),
            "total_requests_this_month": total_requests_this_month,
            "total_tokens_this_month": total_tokens_this_month,
            "active_subscriptions": len(active_subscriptions),
            "average_cost_per_request": round(total_cost_this_month / total_requests_this_month, 4) if total_requests_this_month > 0 else 0.0
        },
        "subscriptions": active_subscriptions,
        "daily_usage": daily_usage,
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/prompt-templates', methods=['GET'])
def get_prompt_templates():
    """Get available prompt templates"""
    templates_file = 'prompt_templates.json'
    
    if os.path.exists(templates_file):
        with open(templates_file, 'r') as f:
            return jsonify(json.load(f))
    
    # Default templates
    default_templates = {
        "categories": {
            "coding": [
                {
                    "id": "code_review",
                    "name": "Code Review",
                    "prompt": "Review the following code for security vulnerabilities, performance issues, and best practices:\n\n{code}\n\nProvide specific, actionable feedback.",
                    "tags": ["code", "review", "security"]
                },
                {
                    "id": "explain_code",
                    "name": "Explain Code",
                    "prompt": "Explain the following code in simple terms:\n\n{code}\n\nBreak down what it does, how it works, and any important concepts.",
                    "tags": ["code", "explanation", "learning"]
                },
                {
                    "id": "debug_code",
                    "name": "Debug Code",
                    "prompt": "Help me debug this code:\n\n{code}\n\nError: {error}\n\nWhat's wrong and how can I fix it?",
                    "tags": ["code", "debug", "error"]
                }
            ],
            "writing": [
                {
                    "id": "blog_post",
                    "name": "Blog Post",
                    "prompt": "Write a blog post about: {topic}\n\nTarget audience: {audience}\n\nTone: {tone}\n\nLength: {length} words",
                    "tags": ["writing", "blog", "content"]
                },
                {
                    "id": "email",
                    "name": "Professional Email",
                    "prompt": "Write a professional email:\n\nTo: {recipient}\nSubject: {subject}\nPurpose: {purpose}\n\nTone: {tone}",
                    "tags": ["writing", "email", "communication"]
                },
                {
                    "id": "summary",
                    "name": "Summary",
                    "prompt": "Summarize the following in {length} sentences:\n\n{content}",
                    "tags": ["writing", "summary", "analysis"]
                }
            ],
            "analysis": [
                {
                    "id": "swot",
                    "name": "SWOT Analysis",
                    "prompt": "Perform a SWOT analysis for: {topic}\n\nConsider:\n- Strengths\n- Weaknesses\n- Opportunities\n- Threats",
                    "tags": ["analysis", "business", "strategy"]
                },
                {
                    "id": "compare",
                    "name": "Compare & Contrast",
                    "prompt": "Compare and contrast:\n\n{item1} vs {item2}\n\nConsider key similarities and differences, pros and cons of each.",
                    "tags": ["analysis", "comparison"]
                },
                {
                    "id": "research",
                    "name": "Research Question",
                    "prompt": "Research and provide insights on: {question}\n\nInclude:\n- Key findings\n- Important considerations\n- Recommendations",
                    "tags": ["analysis", "research"]
                }
            ],
            "learning": [
                {
                    "id": "explain_concept",
                    "name": "Explain Concept",
                    "prompt": "Explain {concept} to someone with {level} knowledge level.\n\nUse examples and analogies to make it clear.",
                    "tags": ["learning", "education", "explanation"]
                },
                {
                    "id": "create_tutorial",
                    "name": "Create Tutorial",
                    "prompt": "Create a step-by-step tutorial for: {topic}\n\nTarget audience: {audience}\n\nInclude prerequisites and examples.",
                    "tags": ["learning", "tutorial", "guide"]
                }
            ]
        }
    }
    
    return jsonify(default_templates)

@app.route('/api/prompt-templates', methods=['POST'])
def save_prompt_template():
    """Save a new prompt template"""
    templates_file = 'prompt_templates.json'
    templates = {"categories": {}}
    
    if os.path.exists(templates_file):
        with open(templates_file, 'r') as f:
            templates = json.load(f)
    
    data = request.json
    category = data.get('category', 'custom')
    template = data.get('template', {})
    
    if category not in templates["categories"]:
        templates["categories"][category] = []
    
    templates["categories"][category].append(template)
    
    with open(templates_file, 'w') as f:
        json.dump(templates, f, indent=2)
    
    return jsonify({"status": "success"})

@app.route('/api/saved-prompts', methods=['GET'])
def get_saved_prompts():
    """Get saved prompts"""
    saved_file = 'saved_prompts.json'
    if os.path.exists(saved_file):
        with open(saved_file, 'r') as f:
            return jsonify(json.load(f))
    return jsonify([])

@app.route('/api/saved-prompts', methods=['POST'])
def save_prompt():
    """Save a prompt"""
    saved_file = 'saved_prompts.json'
    saved = []
    
    if os.path.exists(saved_file):
        with open(saved_file, 'r') as f:
            saved = json.load(f)
    
    prompt_data = request.json
    prompt_data['id'] = datetime.now().isoformat()
    prompt_data['created'] = datetime.now().isoformat()
    
    saved.insert(0, prompt_data)
    
    # Keep only last 100
    saved = saved[:100]
    
    with open(saved_file, 'w') as f:
        json.dump(saved, f, indent=2)
    
    return jsonify({"status": "success", "prompt": prompt_data})

@app.route('/api/response-feedback', methods=['POST'])
def save_feedback():
    """Save feedback/rating for a response"""
    feedback_file = 'feedback.json'
    feedback = []
    
    if os.path.exists(feedback_file):
        with open(feedback_file, 'r') as f:
            feedback = json.load(f)
    
    data = request.json
    data['timestamp'] = datetime.now().isoformat()
    feedback.append(data)
    
    with open(feedback_file, 'w') as f:
        json.dump(feedback, f, indent=2)
    
    return jsonify({"status": "success"})

@app.route('/api/response-analysis', methods=['POST'])
def analyze_responses():
    """Analyze and compare responses"""
    data = request.json
    responses = data.get('responses', [])
    
    analysis = {
        "total_responses": len(responses),
        "successful": len([r for r in responses if r.get('status') == 'success']),
        "failed": len([r for r in responses if r.get('status') == 'error']),
        "statistics": {},
        "comparison": {}
    }
    
    successful = [r for r in responses if r.get('status') == 'success']
    
    if successful:
        # Calculate average length
        lengths = [len(r.get('response', '')) for r in successful]
        analysis["statistics"]["average_length"] = sum(lengths) // len(lengths) if lengths else 0
        analysis["statistics"]["min_length"] = min(lengths) if lengths else 0
        analysis["statistics"]["max_length"] = max(lengths) if lengths else 0
        
        # Estimate tokens
        tokens = [len(r.get('response', '')) // 4 for r in successful]
        analysis["statistics"]["average_tokens"] = sum(tokens) // len(tokens) if tokens else 0
        
        # Response time (if available)
        if 'timestamp' in successful[0]:
            analysis["statistics"]["response_times_available"] = True
        
        # Comparison metrics
        analysis["comparison"]["most_detailed"] = max(successful, key=lambda x: len(x.get('response', '')))["engine"]
        analysis["comparison"]["most_concise"] = min(successful, key=lambda x: len(x.get('response', '')))["engine"]
    
    return jsonify(analysis)

if __name__ == '__main__':
    # Ensure config file exists
    if not os.path.exists(CONFIG_FILE):
        save_config(config)
        print(f"Created {CONFIG_FILE}. Please add your API keys.")
    
    print("Starting AI Aggregator Server...")
    print("Open http://localhost:5000 in your browser")
    app.run(debug=True, port=5000, host='0.0.0.0')

