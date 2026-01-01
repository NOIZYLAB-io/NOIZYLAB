#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                                                                                                                                      ║
║    █████╗ ██╗    ██████╗ ██████╗  █████╗ ██╗███╗   ██╗    ██╗   ██╗██╗  ████████╗██████╗  █████╗                                                     ║
║   ██╔══██╗██║    ██╔══██╗██╔══██╗██╔══██╗██║████╗  ██║    ██║   ██║██║  ╚══██╔══╝██╔══██╗██╔══██╗                                                    ║
║   ███████║██║    ██████╔╝██████╔╝███████║██║██╔██╗ ██║    ██║   ██║██║     ██║   ██████╔╝███████║                                                    ║
║   ██╔══██║██║    ██╔══██╗██╔══██╗██╔══██║██║██║╚██╗██║    ██║   ██║██║     ██║   ██╔══██╗██╔══██║                                                    ║
║   ██║  ██║██║    ██████╔╝██║  ██║██║  ██║██║██║ ╚████║    ╚██████╔╝███████╗██║   ██║  ██║██║  ██║                                                    ║
║   ╚═╝  ╚═╝╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝     ╚═════╝ ╚══════╝╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝                                                    ║
║                                                                                                                                                      ║
║   🧠🔥 UNIFIED AI BRAIN FOR NOIZYLAB - CLAUDE + OPENAI + LOCAL LLMs 🔥🧠                                                                             ║
║                                                                                                                                                      ║
║   CAPABILITIES:                                                                                                                                      ║
║   • Multi-model routing (Claude Opus, Sonnet, Haiku, GPT-4, Llama)                                                                                   ║
║   • Intelligent task complexity assessment                                                                                                           ║
║   • Automatic model selection based on task                                                                                                          ║
║   • Streaming responses                                                                                                                              ║
║   • Context memory with ekkOS integration                                                                                                            ║
║   • Cost optimization                                                                                                                                ║
║                                                                                                                                                      ║
╚══════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
"""

from __future__ import annotations
import os
import sys
import time
import asyncio
import hashlib
from pathlib import Path
from datetime import datetime, timezone
from typing import Optional, Dict, List, Any, AsyncIterator, Literal
from dataclasses import dataclass, field
from enum import Enum
import json

# Performance imports
try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    UVLOOP = True
except ImportError:
    UVLOOP = False

try:
    import orjson
    def json_dumps(obj): return orjson.dumps(obj).decode()
    def json_loads(s): return orjson.loads(s)
except ImportError:
    json_dumps = json.dumps
    json_loads = json.loads


# ═══════════════════════════════════════════════════════════════════════════════════════════
# 🤖 AI MODEL DEFINITIONS
# ═══════════════════════════════════════════════════════════════════════════════════════════

class ModelProvider(Enum):
    ANTHROPIC = "anthropic"
    OPENAI = "openai"
    OLLAMA = "ollama"
    GROQ = "groq"


class TaskComplexity(Enum):
    SIMPLE = 1      # Quick answers, short tasks
    MODERATE = 2    # Standard tasks, code review
    COMPLEX = 3     # Analysis, planning, architecture
    EXPERT = 4      # Deep reasoning, strategic decisions
    CREATIVE = 5    # Creative writing, brainstorming


@dataclass
class AIModel:
    """Definition of an AI model"""
    name: str
    provider: ModelProvider
    model_id: str
    context_window: int
    cost_per_1k_input: float
    cost_per_1k_output: float
    max_output: int
    speed: float  # tokens/sec estimate
    capabilities: List[str]
    best_for: List[TaskComplexity]
    emoji: str


# Model registry - all available models
AI_MODELS: Dict[str, AIModel] = {
    # ANTHROPIC MODELS
    "claude-opus": AIModel(
        name="Claude Opus 4.5",
        provider=ModelProvider.ANTHROPIC,
        model_id="claude-opus-4-5-20241022",
        context_window=200_000,
        cost_per_1k_input=0.015,
        cost_per_1k_output=0.075,
        max_output=8192,
        speed=50,
        capabilities=["reasoning", "code", "analysis", "creative", "vision"],
        best_for=[TaskComplexity.EXPERT, TaskComplexity.COMPLEX],
        emoji="👑"
    ),
    "claude-sonnet": AIModel(
        name="Claude Sonnet 4",
        provider=ModelProvider.ANTHROPIC,
        model_id="claude-sonnet-4-20250514",
        context_window=200_000,
        cost_per_1k_input=0.003,
        cost_per_1k_output=0.015,
        max_output=8192,
        speed=80,
        capabilities=["reasoning", "code", "analysis", "creative"],
        best_for=[TaskComplexity.MODERATE, TaskComplexity.COMPLEX, TaskComplexity.CREATIVE],
        emoji="⚡"
    ),
    "claude-haiku": AIModel(
        name="Claude Haiku 3.5",
        provider=ModelProvider.ANTHROPIC,
        model_id="claude-haiku-3-5-20241022",
        context_window=200_000,
        cost_per_1k_input=0.0008,
        cost_per_1k_output=0.004,
        max_output=8192,
        speed=150,
        capabilities=["quick", "code", "chat"],
        best_for=[TaskComplexity.SIMPLE, TaskComplexity.MODERATE],
        emoji="🚀"
    ),
    
    # OPENAI MODELS
    "gpt-4o": AIModel(
        name="GPT-4o",
        provider=ModelProvider.OPENAI,
        model_id="gpt-4o",
        context_window=128_000,
        cost_per_1k_input=0.005,
        cost_per_1k_output=0.015,
        max_output=4096,
        speed=60,
        capabilities=["reasoning", "code", "vision", "creative"],
        best_for=[TaskComplexity.COMPLEX, TaskComplexity.CREATIVE],
        emoji="🌟"
    ),
    "gpt-4o-mini": AIModel(
        name="GPT-4o Mini",
        provider=ModelProvider.OPENAI,
        model_id="gpt-4o-mini",
        context_window=128_000,
        cost_per_1k_input=0.00015,
        cost_per_1k_output=0.0006,
        max_output=4096,
        speed=100,
        capabilities=["quick", "code", "chat"],
        best_for=[TaskComplexity.SIMPLE],
        emoji="💨"
    ),
    
    # LOCAL/GROQ MODELS
    "llama-70b": AIModel(
        name="Llama 3.3 70B",
        provider=ModelProvider.GROQ,
        model_id="llama-3.3-70b-versatile",
        context_window=128_000,
        cost_per_1k_input=0.00059,
        cost_per_1k_output=0.00079,
        max_output=32768,
        speed=200,  # Groq is FAST
        capabilities=["reasoning", "code", "chat"],
        best_for=[TaskComplexity.MODERATE, TaskComplexity.COMPLEX],
        emoji="🦙"
    ),
    "mixtral": AIModel(
        name="Mixtral 8x7B",
        provider=ModelProvider.GROQ,
        model_id="mixtral-8x7b-32768",
        context_window=32_768,
        cost_per_1k_input=0.00024,
        cost_per_1k_output=0.00024,
        max_output=32768,
        speed=300,
        capabilities=["code", "chat", "quick"],
        best_for=[TaskComplexity.SIMPLE, TaskComplexity.MODERATE],
        emoji="🌀"
    ),
}


# ═══════════════════════════════════════════════════════════════════════════════════════════
# 🧠 AI BRAIN - UNIFIED INTERFACE
# ═══════════════════════════════════════════════════════════════════════════════════════════

@dataclass
class AIRequest:
    """A request to the AI Brain"""
    prompt: str
    system: Optional[str] = None
    model: Optional[str] = None  # If None, auto-select
    max_tokens: int = 2048
    temperature: float = 0.7
    stream: bool = False
    context: Optional[Dict[str, Any]] = None
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class AIResponse:
    """Response from the AI Brain"""
    content: str
    model_used: str
    provider: str
    input_tokens: int
    output_tokens: int
    cost: float
    elapsed_ms: float
    metadata: Dict[str, Any] = field(default_factory=dict)


class AIBrainUltra:
    """
    🧠 AI BRAIN ULTRA - Unified Multi-Model Intelligence
    
    Features:
    - Automatic model selection based on task complexity
    - Multi-provider support (Anthropic, OpenAI, Groq)
    - Cost optimization
    - Streaming responses
    - Context memory
    """
    
    def __init__(self):
        self.models = AI_MODELS
        self.clients: Dict[str, Any] = {}
        self.metrics = {
            "total_requests": 0,
            "total_tokens": 0,
            "total_cost": 0.0,
            "requests_by_model": {},
            "avg_latency_ms": 0.0
        }
        self._initialized = False
    
    async def initialize(self) -> None:
        """Initialize AI clients"""
        if self._initialized:
            return
        
        # Initialize Anthropic client
        anthropic_key = os.environ.get("ANTHROPIC_API_KEY")
        if anthropic_key:
            try:
                import anthropic
                self.clients["anthropic"] = anthropic.AsyncAnthropic(api_key=anthropic_key)
                print("   ✅ Anthropic client initialized")
            except ImportError:
                print("   ⚠️ anthropic package not installed")
        
        # Initialize OpenAI client
        openai_key = os.environ.get("OPENAI_API_KEY")
        if openai_key:
            try:
                from openai import AsyncOpenAI
                self.clients["openai"] = AsyncOpenAI(api_key=openai_key)
                print("   ✅ OpenAI client initialized")
            except ImportError:
                print("   ⚠️ openai package not installed")
        
        # Initialize Groq client
        groq_key = os.environ.get("GROQ_API_KEY")
        if groq_key:
            try:
                from groq import AsyncGroq
                self.clients["groq"] = AsyncGroq(api_key=groq_key)
                print("   ✅ Groq client initialized")
            except ImportError:
                print("   ⚠️ groq package not installed")
        
        self._initialized = True
    
    def assess_complexity(self, prompt: str) -> TaskComplexity:
        """Assess the complexity of a task based on the prompt"""
        prompt_lower = prompt.lower()
        word_count = len(prompt.split())
        
        # Expert indicators
        expert_keywords = ["analyze", "architect", "design", "strategy", "evaluate", "comprehensive"]
        if any(kw in prompt_lower for kw in expert_keywords) and word_count > 50:
            return TaskComplexity.EXPERT
        
        # Complex indicators
        complex_keywords = ["explain", "implement", "review", "refactor", "debug", "compare"]
        if any(kw in prompt_lower for kw in complex_keywords) or word_count > 100:
            return TaskComplexity.COMPLEX
        
        # Creative indicators
        creative_keywords = ["write", "create", "generate", "brainstorm", "story", "poem"]
        if any(kw in prompt_lower for kw in creative_keywords):
            return TaskComplexity.CREATIVE
        
        # Moderate indicators
        moderate_keywords = ["how", "what", "fix", "update", "change"]
        if any(kw in prompt_lower for kw in moderate_keywords):
            return TaskComplexity.MODERATE
        
        return TaskComplexity.SIMPLE
    
    def select_model(self, complexity: TaskComplexity, prefer_fast: bool = False, 
                     prefer_cheap: bool = False) -> str:
        """Select the best model for the task"""
        candidates = []
        
        for name, model in self.models.items():
            if complexity in model.best_for:
                # Check if we have the client
                provider_name = model.provider.value
                if provider_name not in self.clients:
                    continue
                candidates.append((name, model))
        
        if not candidates:
            # Fallback to any available model
            for name, model in self.models.items():
                if model.provider.value in self.clients:
                    candidates.append((name, model))
                    break
        
        if not candidates:
            raise RuntimeError("No AI models available. Check API keys.")
        
        # Sort by preference
        if prefer_fast:
            candidates.sort(key=lambda x: -x[1].speed)
        elif prefer_cheap:
            candidates.sort(key=lambda x: x[1].cost_per_1k_input + x[1].cost_per_1k_output)
        else:
            # Balance quality and cost
            candidates.sort(key=lambda x: (-len(x[1].capabilities), x[1].cost_per_1k_input))
        
        return candidates[0][0]
    
    async def think(self, request: AIRequest) -> AIResponse:
        """
        Main thinking function - sends request to appropriate AI model
        """
        if not self._initialized:
            await self.initialize()
        
        start_time = time.perf_counter()
        
        # Assess complexity and select model
        if request.model:
            model_name = request.model
        else:
            complexity = self.assess_complexity(request.prompt)
            model_name = self.select_model(complexity)
        
        model = self.models.get(model_name)
        if not model:
            raise ValueError(f"Unknown model: {model_name}")
        
        # Route to appropriate provider
        provider = model.provider.value
        
        if provider == "anthropic":
            response = await self._call_anthropic(request, model)
        elif provider == "openai":
            response = await self._call_openai(request, model)
        elif provider == "groq":
            response = await self._call_groq(request, model)
        else:
            raise ValueError(f"Unknown provider: {provider}")
        
        # Calculate cost
        cost = (
            (response.input_tokens / 1000 * model.cost_per_1k_input) +
            (response.output_tokens / 1000 * model.cost_per_1k_output)
        )
        
        elapsed = (time.perf_counter() - start_time) * 1000
        
        # Update metrics
        self.metrics["total_requests"] += 1
        self.metrics["total_tokens"] += response.input_tokens + response.output_tokens
        self.metrics["total_cost"] += cost
        self.metrics["requests_by_model"][model_name] = self.metrics["requests_by_model"].get(model_name, 0) + 1
        
        return AIResponse(
            content=response.content,
            model_used=model_name,
            provider=provider,
            input_tokens=response.input_tokens,
            output_tokens=response.output_tokens,
            cost=cost,
            elapsed_ms=elapsed,
            metadata={"model_id": model.model_id, "emoji": model.emoji}
        )
    
    async def _call_anthropic(self, request: AIRequest, model: AIModel) -> AIResponse:
        """Call Anthropic API"""
        client = self.clients.get("anthropic")
        if not client:
            raise RuntimeError("Anthropic client not initialized")
        
        messages = [{"role": "user", "content": request.prompt}]
        
        response = await client.messages.create(
            model=model.model_id,
            max_tokens=request.max_tokens,
            system=request.system or "You are a helpful AI assistant.",
            messages=messages,
            temperature=request.temperature
        )
        
        return AIResponse(
            content=response.content[0].text,
            model_used=model.name,
            provider="anthropic",
            input_tokens=response.usage.input_tokens,
            output_tokens=response.usage.output_tokens,
            cost=0,
            elapsed_ms=0
        )
    
    async def _call_openai(self, request: AIRequest, model: AIModel) -> AIResponse:
        """Call OpenAI API"""
        client = self.clients.get("openai")
        if not client:
            raise RuntimeError("OpenAI client not initialized")
        
        messages = []
        if request.system:
            messages.append({"role": "system", "content": request.system})
        messages.append({"role": "user", "content": request.prompt})
        
        response = await client.chat.completions.create(
            model=model.model_id,
            max_tokens=request.max_tokens,
            messages=messages,
            temperature=request.temperature
        )
        
        return AIResponse(
            content=response.choices[0].message.content,
            model_used=model.name,
            provider="openai",
            input_tokens=response.usage.prompt_tokens,
            output_tokens=response.usage.completion_tokens,
            cost=0,
            elapsed_ms=0
        )
    
    async def _call_groq(self, request: AIRequest, model: AIModel) -> AIResponse:
        """Call Groq API"""
        client = self.clients.get("groq")
        if not client:
            raise RuntimeError("Groq client not initialized")
        
        messages = []
        if request.system:
            messages.append({"role": "system", "content": request.system})
        messages.append({"role": "user", "content": request.prompt})
        
        response = await client.chat.completions.create(
            model=model.model_id,
            max_tokens=request.max_tokens,
            messages=messages,
            temperature=request.temperature
        )
        
        return AIResponse(
            content=response.choices[0].message.content,
            model_used=model.name,
            provider="groq",
            input_tokens=response.usage.prompt_tokens,
            output_tokens=response.usage.completion_tokens,
            cost=0,
            elapsed_ms=0
        )
    
    def get_status(self) -> Dict[str, Any]:
        """Get brain status"""
        available_providers = list(self.clients.keys())
        available_models = [
            name for name, model in self.models.items()
            if model.provider.value in available_providers
        ]
        
        return {
            "status": "online" if self._initialized else "offline",
            "providers": available_providers,
            "models_available": available_models,
            "metrics": self.metrics
        }
    
    def get_models_info(self) -> Dict[str, Any]:
        """Get detailed model information"""
        return {
            name: {
                "emoji": model.emoji,
                "name": model.name,
                "provider": model.provider.value,
                "context_window": model.context_window,
                "cost_input": model.cost_per_1k_input,
                "cost_output": model.cost_per_1k_output,
                "capabilities": model.capabilities,
                "available": model.provider.value in self.clients
            }
            for name, model in self.models.items()
        }


# ═══════════════════════════════════════════════════════════════════════════════════════════
# 🚀 GLOBAL INSTANCE & HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════════════════

# Global brain instance
_brain: Optional[AIBrainUltra] = None


async def get_brain() -> AIBrainUltra:
    """Get or create the global AI brain instance"""
    global _brain
    if _brain is None:
        _brain = AIBrainUltra()
        await _brain.initialize()
    return _brain


async def quick_think(prompt: str, model: str = None, system: str = None) -> str:
    """Quick helper for simple AI calls"""
    brain = await get_brain()
    request = AIRequest(prompt=prompt, model=model, system=system)
    response = await brain.think(request)
    return response.content


# ═══════════════════════════════════════════════════════════════════════════════════════════
# 🎯 CLI & DEMO
# ═══════════════════════════════════════════════════════════════════════════════════════════

async def demo():
    """Demo the AI Brain"""
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   🧠 AI BRAIN ULTRA - INITIALIZING                                          ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)
    
    brain = AIBrainUltra()
    await brain.initialize()
    
    # Show status
    status = brain.get_status()
    print(f"\n📊 STATUS: {status['status'].upper()}")
    print(f"   Providers: {', '.join(status['providers']) or 'None (check API keys)'}")
    print(f"   Models: {len(status['models_available'])} available")
    
    # Show models
    print("\n🤖 AVAILABLE MODELS:")
    models = brain.get_models_info()
    for name, info in models.items():
        available = "✅" if info["available"] else "❌"
        print(f"   {info['emoji']} {name}: {info['name']} ({info['provider']}) {available}")
    
    # Test complexity assessment
    print("\n🎯 COMPLEXITY ASSESSMENT:")
    test_prompts = [
        "What is 2+2?",
        "How do I fix this Python error?",
        "Analyze this codebase and create an architecture diagram",
        "Write a creative story about a robot fish"
    ]
    
    for prompt in test_prompts:
        complexity = brain.assess_complexity(prompt)
        print(f"   [{complexity.name}] {prompt[:50]}...")
    
    # Try a real request if we have providers
    if status['providers']:
        print("\n💭 TESTING AI RESPONSE...")
        try:
            response = await brain.think(AIRequest(
                prompt="Say 'Hello from AI Brain Ultra!' in a creative way, in one sentence.",
                max_tokens=100
            ))
            print(f"   {response.metadata.get('emoji', '🤖')} Model: {response.model_used}")
            print(f"   📝 Response: {response.content}")
            print(f"   ⏱️ Elapsed: {response.elapsed_ms:.1f}ms")
            print(f"   💰 Cost: ${response.cost:.6f}")
        except Exception as e:
            print(f"   ❌ Error: {e}")
    
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   🧠 AI BRAIN ULTRA - READY                                                 ║
║                                                                              ║
║   "Intelligence is the ability to adapt to change." - Stephen Hawking       ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)


if __name__ == "__main__":
    asyncio.run(demo())
