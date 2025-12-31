#!/usr/bin/env python3
"""
🧠 CODEMASTER AI GATEWAY 🧠
============================
Thin proxy to GOD AI endpoints with:
- Rate limiting
- Caching
- Policy enforcement
- Evidence Pack generation

GOD Endpoints:
- /embed (fast embeddings)
- /stt (speech to text)
- /tts (text to speech)
- /reason (LLM planning)
- /verify (evidence verifier rewrite pass)

RULE: AI is "advisory + formatter" unless evidence-backed
"""

import os
import json
import time
import hashlib
import asyncio
import httpx
from pathlib import Path
from datetime import datetime, timedelta
from typing import Optional, Dict, Any, List
from dataclasses import dataclass
from collections import defaultdict
from functools import lru_cache
import threading

# ═══════════════════════════════════════════════════════════════
# 📁 CONFIGURATION
# ═══════════════════════════════════════════════════════════════

GOD_HOST = os.environ.get("GOD_HOST", "http://localhost:11434")  # Ollama default
GOD_MODEL = os.environ.get("GOD_MODEL", "llama3.2")
CACHE_DIR = Path(os.environ.get("AI_CACHE", "/Users/m2ultra/NOIZY_AI/cache/ai"))
RATE_LIMIT_WINDOW = 60  # seconds
RATE_LIMITS = {
    "embed": 100,    # requests per window
    "reason": 20,
    "stt": 30,
    "tts": 30,
    "verify": 50,
}

# ═══════════════════════════════════════════════════════════════
# 🚦 RATE LIMITER
# ═══════════════════════════════════════════════════════════════

class RateLimiter:
    """Token bucket rate limiter"""
    
    def __init__(self):
        self.requests = defaultdict(list)
        self.lock = threading.Lock()
    
    def check(self, endpoint: str, actor_id: str = "default") -> bool:
        """Check if request is allowed"""
        key = f"{endpoint}:{actor_id}"
        limit = RATE_LIMITS.get(endpoint, 100)
        now = time.time()
        window_start = now - RATE_LIMIT_WINDOW
        
        with self.lock:
            # Clean old requests
            self.requests[key] = [t for t in self.requests[key] if t > window_start]
            
            if len(self.requests[key]) >= limit:
                return False
            
            self.requests[key].append(now)
            return True
    
    def remaining(self, endpoint: str, actor_id: str = "default") -> int:
        """Get remaining requests in window"""
        key = f"{endpoint}:{actor_id}"
        limit = RATE_LIMITS.get(endpoint, 100)
        now = time.time()
        window_start = now - RATE_LIMIT_WINDOW
        
        with self.lock:
            current = len([t for t in self.requests[key] if t > window_start])
            return max(0, limit - current)

# ═══════════════════════════════════════════════════════════════
# 💾 RESPONSE CACHE
# ═══════════════════════════════════════════════════════════════

class ResponseCache:
    """LRU cache for AI responses"""
    
    def __init__(self, cache_dir: Path = CACHE_DIR, max_age_hours: int = 24):
        self.cache_dir = cache_dir
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.max_age = timedelta(hours=max_age_hours)
    
    def _hash_key(self, endpoint: str, params: Dict) -> str:
        """Generate cache key"""
        content = json.dumps({"endpoint": endpoint, "params": params}, sort_keys=True)
        return hashlib.sha256(content.encode()).hexdigest()[:16]
    
    def get(self, endpoint: str, params: Dict) -> Optional[Dict]:
        """Get cached response"""
        key = self._hash_key(endpoint, params)
        cache_file = self.cache_dir / f"{key}.json"
        
        if cache_file.exists():
            data = json.loads(cache_file.read_text())
            cached_at = datetime.fromisoformat(data['cached_at'])
            if datetime.now() - cached_at < self.max_age:
                return data['response']
        return None
    
    def set(self, endpoint: str, params: Dict, response: Dict):
        """Cache a response"""
        key = self._hash_key(endpoint, params)
        cache_file = self.cache_dir / f"{key}.json"
        
        data = {
            'cached_at': datetime.now().isoformat(),
            'endpoint': endpoint,
            'response': response,
        }
        cache_file.write_text(json.dumps(data))
    
    def clear(self, older_than_hours: int = None):
        """Clear cache"""
        if older_than_hours is None:
            for f in self.cache_dir.glob("*.json"):
                f.unlink()
        else:
            cutoff = datetime.now() - timedelta(hours=older_than_hours)
            for f in self.cache_dir.glob("*.json"):
                data = json.loads(f.read_text())
                if datetime.fromisoformat(data['cached_at']) < cutoff:
                    f.unlink()

# ═══════════════════════════════════════════════════════════════
# 🧠 AI GATEWAY
# ═══════════════════════════════════════════════════════════════

@dataclass
class AIResponse:
    """Structured AI response"""
    success: bool
    content: Any
    model: str
    cached: bool = False
    latency_ms: float = 0
    error: Optional[str] = None
    
    def to_dict(self) -> Dict:
        return {
            'success': self.success,
            'content': self.content,
            'model': self.model,
            'cached': self.cached,
            'latency_ms': self.latency_ms,
            'error': self.error,
        }

class AIGateway:
    """AI Gateway to GOD endpoints"""
    
    def __init__(self, host: str = GOD_HOST, model: str = GOD_MODEL):
        self.host = host
        self.model = model
        self.rate_limiter = RateLimiter()
        self.cache = ResponseCache()
        self.client = httpx.AsyncClient(timeout=120.0)
    
    async def embed(self, text: str, actor_id: str = "default") -> AIResponse:
        """Generate embeddings for text"""
        if not self.rate_limiter.check("embed", actor_id):
            return AIResponse(success=False, content=None, model=self.model, 
                            error="Rate limit exceeded")
        
        # Check cache
        params = {"text": text}
        cached = self.cache.get("embed", params)
        if cached:
            return AIResponse(success=True, content=cached, model=self.model, cached=True)
        
        start = time.time()
        try:
            response = await self.client.post(
                f"{self.host}/api/embeddings",
                json={"model": self.model, "prompt": text}
            )
            response.raise_for_status()
            data = response.json()
            
            self.cache.set("embed", params, data.get('embedding', []))
            
            return AIResponse(
                success=True,
                content=data.get('embedding', []),
                model=self.model,
                latency_ms=(time.time() - start) * 1000,
            )
        except Exception as e:
            return AIResponse(success=False, content=None, model=self.model, error=str(e))
    
    async def reason(self, prompt: str, system: str = None, 
                     actor_id: str = "default",
                     temperature: float = 0.7,
                     max_tokens: int = 2048) -> AIResponse:
        """LLM reasoning/planning"""
        if not self.rate_limiter.check("reason", actor_id):
            return AIResponse(success=False, content=None, model=self.model,
                            error="Rate limit exceeded")
        
        start = time.time()
        try:
            messages = []
            if system:
                messages.append({"role": "system", "content": system})
            messages.append({"role": "user", "content": prompt})
            
            response = await self.client.post(
                f"{self.host}/api/chat",
                json={
                    "model": self.model,
                    "messages": messages,
                    "stream": False,
                    "options": {
                        "temperature": temperature,
                        "num_predict": max_tokens,
                    }
                }
            )
            response.raise_for_status()
            data = response.json()
            
            return AIResponse(
                success=True,
                content=data.get('message', {}).get('content', ''),
                model=self.model,
                latency_ms=(time.time() - start) * 1000,
            )
        except Exception as e:
            return AIResponse(success=False, content=None, model=self.model, error=str(e))
    
    async def verify(self, answer: str, claims: List[Dict], 
                     actor_id: str = "default") -> AIResponse:
        """
        Verify and rewrite answer based on evidence.
        This is the AI-assisted verification pass.
        """
        if not self.rate_limiter.check("verify", actor_id):
            return AIResponse(success=False, content=None, model=self.model,
                            error="Rate limit exceeded")
        
        # Build verification prompt
        claims_text = "\n".join([
            f"- Claim: {c['claim_text']}\n  Evidence: {c.get('support', 'NONE')}"
            for c in claims
        ])
        
        prompt = f"""You are an evidence verifier. Review this answer and claims.
RULES:
1. Any claim without evidence must be marked UNSUPPORTED
2. Claims with evidence get SUPPORTED or PARTIAL
3. Rewrite the answer to only include supported claims
4. If no claims are supported, output "UNKNOWN" with next retrieval steps

ANSWER:
{answer}

CLAIMS:
{claims_text}

Output JSON with:
- verified_answer: the rewritten answer
- claim_statuses: list of {{claim, status, reason}}
- confidence: 0.0 to 1.0
"""
        
        result = await self.reason(
            prompt=prompt,
            system="You are a strict evidence verifier. Output valid JSON only.",
            actor_id=actor_id,
            temperature=0.1,
        )
        
        # Try to parse JSON from response
        if result.success:
            try:
                # Find JSON in response
                content = result.content
                if '```json' in content:
                    content = content.split('```json')[1].split('```')[0]
                elif '```' in content:
                    content = content.split('```')[1].split('```')[0]
                
                parsed = json.loads(content)
                result.content = parsed
            except:
                # Return raw if JSON parsing fails
                pass
        
        return result
    
    async def stt(self, audio_path: str, actor_id: str = "default") -> AIResponse:
        """Speech to text (requires Whisper endpoint)"""
        if not self.rate_limiter.check("stt", actor_id):
            return AIResponse(success=False, content=None, model="whisper",
                            error="Rate limit exceeded")
        
        start = time.time()
        try:
            # Try local Whisper via Ollama or dedicated endpoint
            with open(audio_path, 'rb') as f:
                audio_data = f.read()
            
            # This would need a Whisper endpoint configured
            # For now, return placeholder
            return AIResponse(
                success=False,
                content=None,
                model="whisper",
                error="STT endpoint not configured. Set GOD_STT_ENDPOINT.",
            )
        except Exception as e:
            return AIResponse(success=False, content=None, model="whisper", error=str(e))
    
    async def tts(self, text: str, voice: str = "default", 
                  actor_id: str = "default") -> AIResponse:
        """Text to speech"""
        if not self.rate_limiter.check("tts", actor_id):
            return AIResponse(success=False, content=None, model="tts",
                            error="Rate limit exceeded")
        
        # This would need a TTS endpoint configured
        return AIResponse(
            success=False,
            content=None,
            model="tts",
            error="TTS endpoint not configured. Set GOD_TTS_ENDPOINT.",
        )
    
    def stats(self) -> Dict:
        """Get gateway statistics"""
        return {
            'host': self.host,
            'model': self.model,
            'rate_limits': {
                k: {
                    'limit': v,
                    'remaining': self.rate_limiter.remaining(k),
                }
                for k, v in RATE_LIMITS.items()
            },
        }
    
    async def close(self):
        """Close the HTTP client"""
        await self.client.aclose()

# ═══════════════════════════════════════════════════════════════
# 🌐 FASTAPI SERVER
# ═══════════════════════════════════════════════════════════════

def create_app():
    """Create FastAPI app for AI Gateway"""
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
    
    app = FastAPI(title="🧠 CODEMASTER AI Gateway", version="0.1.0")
    gateway = AIGateway()
    
    class EmbedRequest(BaseModel):
        text: str
        actor_id: str = "default"
    
    class ReasonRequest(BaseModel):
        prompt: str
        system: str = None
        actor_id: str = "default"
        temperature: float = 0.7
        max_tokens: int = 2048
    
    class VerifyRequest(BaseModel):
        answer: str
        claims: List[Dict]
        actor_id: str = "default"
    
    @app.get("/health")
    async def health():
        return {"status": "ok", "model": gateway.model}
    
    @app.get("/stats")
    async def stats():
        return gateway.stats()
    
    @app.post("/embed")
    async def embed(req: EmbedRequest):
        result = await gateway.embed(req.text, req.actor_id)
        if not result.success:
            raise HTTPException(status_code=429 if "Rate limit" in (result.error or "") else 500,
                              detail=result.error)
        return result.to_dict()
    
    @app.post("/reason")
    async def reason(req: ReasonRequest):
        result = await gateway.reason(
            req.prompt, req.system, req.actor_id, req.temperature, req.max_tokens
        )
        if not result.success:
            raise HTTPException(status_code=429 if "Rate limit" in (result.error or "") else 500,
                              detail=result.error)
        return result.to_dict()
    
    @app.post("/verify")
    async def verify(req: VerifyRequest):
        result = await gateway.verify(req.answer, req.claims, req.actor_id)
        if not result.success:
            raise HTTPException(status_code=429 if "Rate limit" in (result.error or "") else 500,
                              detail=result.error)
        return result.to_dict()
    
    return app

# ═══════════════════════════════════════════════════════════════
# 🎯 CLI
# ═══════════════════════════════════════════════════════════════

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='🧠 CODEMASTER AI Gateway')
    parser.add_argument('command', choices=['serve', 'test', 'stats'])
    parser.add_argument('--host', default='0.0.0.0')
    parser.add_argument('--port', type=int, default=8100)
    parser.add_argument('--prompt', help='Test prompt')
    
    args = parser.parse_args()
    
    if args.command == 'serve':
        import uvicorn
        app = create_app()
        uvicorn.run(app, host=args.host, port=args.port)
    
    elif args.command == 'test':
        async def test():
            gateway = AIGateway()
            prompt = args.prompt or "What is 2+2? Be brief."
            print(f"\n🧠 Testing AI Gateway...")
            print(f"   Host: {gateway.host}")
            print(f"   Model: {gateway.model}")
            print(f"   Prompt: {prompt}\n")
            
            result = await gateway.reason(prompt)
            if result.success:
                print(f"✅ Response ({result.latency_ms:.0f}ms):")
                print(f"   {result.content}")
            else:
                print(f"❌ Error: {result.error}")
            
            await gateway.close()
        
        asyncio.run(test())
    
    elif args.command == 'stats':
        gateway = AIGateway()
        stats = gateway.stats()
        print("\n📊 AI GATEWAY STATS\n")
        print(f"  Host: {stats['host']}")
        print(f"  Model: {stats['model']}")
        print("\n  Rate Limits:")
        for endpoint, info in stats['rate_limits'].items():
            print(f"    {endpoint}: {info['remaining']}/{info['limit']} remaining")

if __name__ == "__main__":
    main()
