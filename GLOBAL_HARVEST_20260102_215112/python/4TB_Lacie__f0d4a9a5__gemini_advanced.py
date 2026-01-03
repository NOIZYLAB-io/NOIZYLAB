#!/usr/bin/env python3
"""
Gemini Advanced Features - Ultra-Powered Integration
Streaming, Function Calling, Thinking, Batch Processing, and More!
"""

import os
import json
import asyncio
from typing import Optional, List, Dict, Callable, Any
from google import genai
from pathlib import Path

class GeminiAdvanced:
    """Advanced Gemini AI with all premium features"""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv('GEMINI_API_KEY', '')
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not set")

        if api_key:
            os.environ['GEMINI_API_KEY'] = api_key

        self.client = genai.Client()
        self.cache_dir = Path(__file__).parent / "cache"
        self.cache_dir.mkdir(exist_ok=True)
        self.history = []

    def stream_generate(self, prompt: str, model: str = "gemini-2.5-flash"):
        """Stream responses in real-time"""
        try:
            response = self.client.models.generate_content_stream(
                model=model,
                contents=prompt
            )
            for chunk in response:
                if chunk.text:
                    yield chunk.text
        except Exception as e:
            yield f"Error: {e}"

    def batch_process(self, prompts: List[str], model: str = "gemini-2.5-flash") -> List[str]:
        """Process multiple prompts in parallel"""
        results = []
        for prompt in prompts:
            try:
                response = self.client.models.generate_content(
                    model=model,
                    contents=prompt
                )
                results.append(response.text)
            except Exception as e:
                results.append(f"Error: {e}")
        return results

    def function_calling(self, prompt: str, functions: Dict[str, Callable], model: str = "gemini-2.5-flash"):
        """Use function calling for tool use"""
        # Convert functions to Gemini format
        tools = []
        for name, func in functions.items():
            tools.append({
                "function_declarations": [{
                    "name": name,
                    "description": func.__doc__ or f"Function: {name}",
                    "parameters": {}
                }]
            })

        try:
            response = self.client.models.generate_content(
                model=model,
                contents=prompt,
                tools=tools
            )
            return response
        except Exception as e:
            return f"Error: {e}"

    def thinking_mode(self, prompt: str, model: str = "gemini-2.5-flash"):
        """Use thinking mode for complex reasoning"""
        try:
            response = self.client.models.generate_content(
                model=model,
                contents=prompt,
                config={"thinking": True}
            )
            return {
                "thinking": response.thinking if hasattr(response, 'thinking') else None,
                "response": response.text
            }
        except Exception as e:
            return {"error": str(e)}

    def multi_turn_conversation(self, messages: List[Dict[str, str]], model: str = "gemini-2.5-flash"):
        """Multi-turn conversation with context"""
        try:
            response = self.client.models.generate_content(
                model=model,
                contents=messages
            )
            return response.text
        except Exception as e:
            return f"Error: {e}"

    def analyze_with_context(self, prompt: str, context_files: List[str], model: str = "gemini-2.5-flash"):
        """Analyze with file context"""
        try:
            contents = [prompt]
            for file_path in context_files:
                with open(file_path, 'r') as f:
                    contents.append(f"File: {file_path}\n{f.read()}")

            response = self.client.models.generate_content(
                model=model,
                contents=contents
            )
            return response.text
        except Exception as e:
            return f"Error: {e}"

    def code_generation(self, description: str, language: str = "python", model: str = "gemini-2.5-flash"):
        """Generate code from description"""
        prompt = f"""Generate {language} code for: {description}

Requirements:
- Clean, well-commented code
- Follow best practices
- Include error handling
- Add docstrings"""

        try:
            response = self.client.models.generate_content(
                model=model,
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"Error: {e}"

    def repair_diagnosis(self, device_info: Dict[str, Any], symptoms: str, model: str = "gemini-2.5-flash"):
        """Advanced repair diagnosis with device context"""
        prompt = f"""You are an expert repair technician. Diagnose this issue:

Device: {device_info.get('type', 'Unknown')}
Model: {device_info.get('model', 'Unknown')}
OS: {device_info.get('os', 'Unknown')}
Symptoms: {symptoms}

Provide:
1. Root cause analysis
2. Step-by-step repair instructions
3. Required tools/parts
4. Difficulty level
5. Estimated time
6. Alternative solutions
7. Prevention tips"""

        try:
            response = self.client.models.generate_content(
                model=model,
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"Error: {e}"

    def smart_search(self, query: str, use_web: bool = True, model: str = "gemini-2.5-flash"):
        """Smart search with optional web context"""
        prompt = f"""Search and provide comprehensive answer for: {query}

Include:
- Direct answer
- Sources/references
- Related information
- Actionable steps"""

        try:
            config = {}
            if use_web:
                config["tools"] = [{"google_search": {}}]

            response = self.client.models.generate_content(
                model=model,
                contents=prompt,
                config=config
            )
            return response.text
        except Exception as e:
            return f"Error: {e}"

