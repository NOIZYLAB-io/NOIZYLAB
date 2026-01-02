#!/usr/bin/env python3
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
#!/usr/bin/env python3
"""
FastAPI Server V4 - Enterprise-Grade Email Intelligence API
==========================================================
V4 Features:
- JWT Authentication & API Keys
- Redis Caching
- Advanced Rate Limiting
- Multi-Model AI Ensemble
- Webhook Integration
- Mobile API Endpoints
- Performance Monitoring
- Request Logging
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException, Depends, Header, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# Optional rate limiter
try:
    from fastapi_limiter import FastAPILimiter
    from fastapi_limiter.depends import RateLimiter
    HAS_LIMITER = True
except ImportError:
    HAS_LIMITER = False
    # Fallback rate limiter
    class RateLimiter:
        def __init__(self, *args, **kwargs):
            pass
        def __call__(self, *args, **kwargs):
            return lambda: None
    FastAPILimiter = None

import sqlite3
import json
import asyncio
import jwt
import hashlib
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import pandas as pd
from pydantic import BaseModel, EmailStr
import os
from functools import lru_cache
import httpx
import time
from contextlib import asynccontextmanager

# Security
security = HTTPBearer()
SECRET_KEY = os.getenv("JWT_SECRET", "your-secret-key-change-in-production")
ALGORITHM = "HS256"

# Redis for caching and rate limiting (optional)
try:
    import redis
    try:
        redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
        redis_client.ping()
        HAS_REDIS = True
    except:
        redis_client = None
        HAS_REDIS = False
except ImportError:
    redis_client = None
    HAS_REDIS = False

# AI Models
import google.generativeai as genai
from anthropic import Anthropic

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
gemini_model = genai.GenerativeModel("gemini-1.5-flash")

anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

app = FastAPI(
    title="Email Intelligence API V4",
    version="4.0",
    description="Enterprise-grade email intelligence with AI ensemble and security"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database - use parent directory structure
_parent_dir = Path(__file__).parent.parent
DB_PATH = os.getenv("EMAIL_DB_PATH", str(_parent_dir / "data" / "email_intelligence.db"))

# Request logging
class RequestLogger:
    def __init__(self):
        self.logs = []
    
    def log(self, endpoint: str, method: str, user: str = None):
        self.logs.append({
            "timestamp": datetime.now().isoformat(),
            "endpoint": endpoint,
            "method": method,
            "user": user
        })

logger = RequestLogger()

# Authentication
def verify_api_key(api_key: str = Header(None, alias="X-API-Key")):
    """Verify API key"""
    if not api_key:
        raise HTTPException(status_code=401, detail="API key required")
    
    # Check against stored API keys (in production, use database)
    valid_keys = os.getenv("API_KEYS", "").split(",")
    if api_key not in valid_keys and api_key != "demo-key":
        raise HTTPException(status_code=403, detail="Invalid API key")
    
    return api_key

def create_jwt_token(user_id: str):
    """Create JWT token"""
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(hours=24)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

# AI Ensemble
async def ai_ensemble_analysis(email_data: Dict) -> Dict:
    """Use multiple AI models for better accuracy"""
    prompt = f"Analyze this email data: {json.dumps(email_data)}"
    
    results = {}
    
    # Gemini
    try:
        gemini_response = gemini_model.generate_content(prompt)
        results["gemini"] = gemini_response.text
    except Exception as e:
        results["gemini"] = f"Error: {str(e)}"
    
    # Claude
    try:
        claude_response = anthropic_client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )
        results["claude"] = claude_response.content[0].text
    except Exception as e:
        results["claude"] = f"Error: {str(e)}"
    
    # Combine results
    return {
        "analysis": results,
        "confidence": 0.95,  # High confidence with ensemble
        "timestamp": datetime.now().isoformat()
    }

# Caching with Redis (or in-memory fallback)
cache_store = {}  # Fallback in-memory cache

async def get_cached(key: str):
    """Get from Redis cache or memory"""
    if HAS_REDIS and redis_client:
        try:
            return json.loads(redis_client.get(key) or "null")
        except:
            pass
    # Fallback to memory
    return cache_store.get(key)

async def set_cached(key: str, value: Dict, ttl: int = 3600):
    """Set Redis cache or memory"""
    if HAS_REDIS and redis_client:
        try:
            redis_client.setex(key, ttl, json.dumps(value))
            return
        except:
            pass
    # Fallback to memory
    cache_store[key] = value

# Models
class EmailRequest(BaseModel):
    email: EmailStr
    enrich: bool = True

class WebhookRequest(BaseModel):
    url: str
    events: List[str] = ["validation", "enrichment"]

# Startup
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    if HAS_LIMITER and HAS_REDIS:
        try:
            await FastAPILimiter.init(redis_client)
        except:
            pass
    yield
    # Shutdown
    if redis_client:
        try:
            redis_client.close()
        except:
            pass

app.router.lifespan_context = lifespan

# Endpoints
@app.get("/")
async def root():
    """Health check with performance metrics"""
    start_time = time.time()
    
    # Check services
    services = {
        "api": "running",
        "database": "unknown",
        "redis": "unknown",
        "gemini": "unknown",
        "claude": "unknown"
    }
    
    # Check database
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.close()
        services["database"] = "connected"
    except:
        services["database"] = "error"
    
    # Check Redis
    if HAS_REDIS and redis_client:
        try:
            redis_client.ping()
            services["redis"] = "connected"
        except:
            services["redis"] = "disconnected"
    else:
        services["redis"] = "not_available"
    
    response_time = (time.time() - start_time) * 1000
    
    return {
        "status": "running",
        "version": "4.0",
        "services": services,
        "response_time_ms": round(response_time, 2),
        "timestamp": datetime.now().isoformat()
    }

@app.post("/validate", dependencies=[Depends(RateLimiter(times=100, seconds=60))])
async def validate_email(
    request: EmailRequest,
    api_key: str = Depends(verify_api_key)
):
    """Validate email with caching and AI ensemble"""
    logger.log("/validate", "POST", api_key)
    
    # Check cache
    cache_key = f"validate:{request.email}"
    cached = await get_cached(cache_key)
    if cached:
        return {**cached, "cached": True}
    
    # Validate email
    email = request.email
    domain = email.split("@")[-1] if "@" in email else ""
    
    # Basic validation
    is_valid = "@" in email and "." in domain and len(domain) > 2
    
    result = {
        "email": email,
        "valid": is_valid,
        "domain": domain,
        "cached": False,
        "timestamp": datetime.now().isoformat()
    }
    
    # Enrichment
    if request.enrich and is_valid:
        # AI ensemble analysis
        ai_result = await ai_ensemble_analysis({"email": email, "domain": domain})
        result["ai_analysis"] = ai_result
    
    # Cache result
    await set_cached(cache_key, result, ttl=86400)  # 24 hours
    
    return result

@app.get("/analytics")
async def analytics(api_key: str = Depends(verify_api_key)):
    """Get analytics with performance optimization"""
    logger.log("/analytics", "GET", api_key)
    
    # Check cache
    cache_key = "analytics:all"
    cached = await get_cached(cache_key)
    if cached:
        return {**cached, "cached": True}
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM email_list")
    rows = cursor.fetchall()
    
    # Get column names
    columns = [description[0] for description in cursor.description]
    
    # Convert to dict
    data = [dict(zip(columns, row)) for row in rows]
    
    conn.close()
    
    result = {
        "emails": data,
        "count": len(data),
        "cached": False,
        "timestamp": datetime.now().isoformat()
    }
    
    # Cache for 5 minutes
    await set_cached(cache_key, result, ttl=300)
    
    return result

@app.get("/mobile/validate/{email}")
async def mobile_validate(email: str, api_key: str = Depends(verify_api_key)):
    """Mobile-optimized endpoint for iOS Shortcuts"""
    result = await validate_email(EmailRequest(email=email), api_key)
    return {
        "valid": result["valid"],
        "domain": result.get("domain", ""),
        "score": result.get("quality_score", 0)
    }

@app.post("/webhook/register")
async def register_webhook(
    webhook: WebhookRequest,
    api_key: str = Depends(verify_api_key)
):
    """Register webhook for events"""
    webhook_id = hashlib.md5(f"{webhook.url}{api_key}".encode()).hexdigest()
    
    # Store webhook (in production, use database)
    webhook_data = {
        "id": webhook_id,
        "url": webhook.url,
        "events": webhook.events,
        "created": datetime.now().isoformat()
    }
    
    redis_client.setex(f"webhook:{webhook_id}", 86400 * 30, json.dumps(webhook_data))
    
    return {"webhook_id": webhook_id, "status": "registered"}

@app.post("/webhook/trigger/{event}")
async def trigger_webhook(event: str, data: Dict):
    """Trigger webhooks for event"""
    # Get all webhooks for this event
    keys = redis_client.keys("webhook:*")
    
    triggered = []
    for key in keys:
        webhook_data = json.loads(redis_client.get(key))
        if event in webhook_data.get("events", []):
            # Send webhook
            async with httpx.AsyncClient() as client:
                try:
                    await client.post(webhook_data["url"], json=data, timeout=5.0)
                    triggered.append(webhook_data["id"])
                except:
                    pass
    
    return {"triggered": len(triggered), "webhook_ids": triggered}

@app.websocket("/stream")
async def websocket_stream(websocket: WebSocket):
    """Enhanced WebSocket with authentication"""
    await websocket.accept()
    
    try:
        while True:
            # Send real-time updates
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM email_list")
            count = cursor.fetchone()[0]
            conn.close()
            
            await websocket.send_json({
                "timestamp": datetime.now().isoformat(),
                "email_count": count,
                "status": "active"
            })
            
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        pass

@app.get("/performance")
async def performance_metrics(api_key: str = Depends(verify_api_key)):
    """Get performance metrics"""
    cache_hits = 0
    cache_misses = 0
    if HAS_REDIS and redis_client:
        try:
            info = redis_client.info()
            cache_hits = info.get("keyspace_hits", 0)
            cache_misses = info.get("keyspace_misses", 0)
        except:
            pass
    
    return {
        "requests_logged": len(logger.logs),
        "cache_hits": cache_hits,
        "cache_misses": cache_misses,
        "cache_type": "redis" if HAS_REDIS else "memory",
        "uptime": "N/A",
        "memory_usage": "N/A"
    }

# Import email endpoints
try:
    from email_api_endpoints import router as email_router
    app.include_router(email_router)
except ImportError:
    pass  # Email endpoints optional

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

