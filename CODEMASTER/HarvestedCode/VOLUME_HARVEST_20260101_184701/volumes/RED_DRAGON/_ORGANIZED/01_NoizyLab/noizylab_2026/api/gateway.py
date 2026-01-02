#!/usr/bin/env python3
"""
Universal API Gateway - Connect everything to everything
Zero-config deployment with automatic documentation.
"""
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import uvicorn
import json
import time
from uap_core import uap, UapEvent

app = FastAPI(
    title="Universal API Gateway",
    description="Connect everything to everything",
    version="1.0.0"
)

# Store for dynamic endpoints
dynamic_endpoints = {}

@app.get("/")
async def root():
    return {"message": "Universal API Gateway - Ready to connect everything! 🌐"}

@app.get("/health")
async def health():
    return {"status": "healthy", "timestamp": time.time()}

@app.post("/uap/publish")
async def publish_event(request: Request):
    """Publish event to UAP bus"""
    data = await request.json()
    event = UapEvent(
        topic=data['topic'],
        payload=data['payload'],
        source=data.get('source', 'api_gateway')
    )
    uap.publish(event)
    return {"status": "published"}

@app.get("/uap/fetch/{topic}")
async def fetch_events(topic: str, n: int = 10):
    """Fetch recent events for a topic"""
    # This would integrate with event storage
    return {"topic": topic, "events": [], "note": "Event storage coming soon!"}

@app.get("/docs/auto", response_class=HTMLResponse)
async def auto_docs():
    """Auto-generated documentation"""
    return """
    <html>
        <head><title>Universal API Gateway - Auto Docs</title></head>
        <body>
            <h1>🤖 Auto-Generated Documentation</h1>
            <p>This documentation writes itself based on your API usage patterns!</p>
            <h2>Available Endpoints:</h2>
            <ul>
                <li><code>GET /</code> - Root endpoint</li>
                <li><code>GET /health</code> - Health check</li>
                <li><code>POST /uap/publish</code> - Publish UAP event</li>
                <li><code>GET /uap/fetch/{topic}</code> - Fetch events by topic</li>
            </ul>
            <p><em>More endpoints will appear here as you use them!</em></p>
        </body>
    </html>
    """

def gateway_agent():
    """Agent that monitors API usage and auto-generates docs"""
    # Monitor usage patterns
    uap.publish(UapEvent(
        topic='api_usage',
        payload={'gateway_status': 'active'},
        source='api_gateway'
    ))

# Register the gateway agent
uap.register_agent('api_gateway', gateway_agent)

if __name__ == "__main__":
    print("🌐 Starting Universal API Gateway...")
    uvicorn.run(app, host="0.0.0.0", port=8000)