#!/usr/bin/env python3
"""
FastAPI Server V3 - Enhanced Real-Time Email Intelligence API
============================================================
Advanced features: Caching, rate limiting, WebSocket streaming, analytics
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, JSONResponse
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from fastapi_cache.decorator import cache
import sqlite3
import json
import asyncio
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import pandas as pd
from pydantic import BaseModel
import os
from functools import lru_cache
import hashlib

app = FastAPI(
    title="Email Intelligence API V3",
    version="3.0",
    description="Enhanced real-time email intelligence with caching and analytics"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration
try:
    from app.config import DB_PATH
except ImportError:
    DB_PATH = os.getenv("EMAIL_DB_PATH", "email_intelligence.db")

# Initialize cache
@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend(), prefix="email-api")

# Global connection (your pattern)
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()

# WebSocket connections
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.message_history: List[Dict] = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    
    def disconnect(self, websocket: WebSocket):
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
    
    async def broadcast(self, message: dict):
        self.message_history.append({
            "timestamp": datetime.now().isoformat(),
            "data": message
        })
        # Keep only last 100 messages
        if len(self.message_history) > 100:
            self.message_history = self.message_history[-100:]
        
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except:
                self.disconnect(connection)

manager = ConnectionManager()

# Pydantic models
class EmailData(BaseModel):
    email: str
    category: Optional[str] = None
    spam_score: Optional[float] = None
    validity_score: Optional[float] = None

class AnalyticsResponse(BaseModel):
    total_emails: int
    categories: Dict[str, int]
    spam_rate: float
    avg_validity: float
    trends: Dict[str, float]
    top_domains: List[Dict]
    recent_activity: Dict

# Helper functions
def get_db_connection():
    return sqlite3.connect(DB_PATH)

@lru_cache(maxsize=128)
def cached_query(query_hash: str, query: str):
    """Cache database queries"""
    conn = get_db_connection()
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df.to_dict('records')

# API Endpoints
@app.get("/")
async def root():
    return {
        "service": "Email Intelligence API V3",
        "version": "3.0",
        "status": "operational",
        "endpoints": {
            "analytics": "/analytics",
            "enhanced_analytics": "/api/analytics",
            "powerbi": "/api/powerbi",
            "insights": "/api/insights",
            "stream": "/api/stream",
            "websocket": "/ws",
            "stats": "/api/stats"
        }
    }

@app.get("/analytics")
async def analytics():
    """Your exact analytics endpoint - enhanced with caching"""
    query_hash = hashlib.md5("SELECT * FROM email_list".encode()).hexdigest()
    
    # Try cache first
    try:
        cached = cached_query(query_hash, "SELECT * FROM email_list")
        return {"emails": cached, "cached": True, "timestamp": datetime.now().isoformat()}
    except:
        # Fallback to direct query
        cursor.execute("SELECT * FROM email_list")
        rows = cursor.fetchall()
        
        # Get column names
        cursor.execute("PRAGMA table_info(email_list)")
        columns = [row[1] for row in cursor.fetchall()]
        
        # Convert to dict
        emails = [dict(zip(columns, row)) for row in rows]
        return {"emails": emails, "cached": False, "timestamp": datetime.now().isoformat()}

@app.get("/api/analytics")
@cache(expire=5)  # Cache for 5 seconds
async def get_analytics():
    """Enhanced analytics with caching"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Total emails
    cursor.execute("SELECT COUNT(*) FROM email_list")
    total = cursor.fetchone()[0]
    
    # Categories
    cursor.execute("SELECT category, COUNT(*) FROM email_list GROUP BY category")
    categories = {row[0] or "unknown": row[1] for row in cursor.fetchall()}
    
    # Spam rate
    cursor.execute("SELECT AVG(spam_score), COUNT(*) FROM email_list WHERE spam_score > 0.7")
    spam_avg, spam_count = cursor.fetchone()
    spam_rate = (spam_count / total * 100) if total > 0 else 0
    
    # Avg validity
    cursor.execute("SELECT AVG(validity_score) FROM email_list")
    avg_validity = cursor.fetchone()[0] or 0
    
    # Trends (last 7 days)
    cursor.execute("""
        SELECT DATE(processed_at) as date, COUNT(*) as count
        FROM email_list
        WHERE processed_at >= datetime('now', '-7 days')
        GROUP BY DATE(processed_at)
        ORDER BY date
    """)
    trends = {row[0]: row[1] for row in cursor.fetchall()}
    
    # Top domains
    cursor.execute("""
        SELECT 
            substr(email, instr(email, '@') + 1) as domain,
            COUNT(*) as count
        FROM email_list
        GROUP BY domain
        ORDER BY count DESC
        LIMIT 10
    """)
    top_domains = [{"domain": row[0], "count": row[1]} for row in cursor.fetchall()]
    
    # Recent activity
    cursor.execute("""
        SELECT COUNT(*) FROM email_list
        WHERE processed_at >= datetime('now', '-1 hour')
    """)
    recent_1h = cursor.fetchone()[0]
    
    cursor.execute("""
        SELECT COUNT(*) FROM email_list
        WHERE processed_at >= datetime('now', '-24 hours')
    """)
    recent_24h = cursor.fetchone()[0]
    
    conn.close()
    
    return AnalyticsResponse(
        total_emails=total,
        categories=categories,
        spam_rate=round(spam_rate, 2),
        avg_validity=round(avg_validity * 100, 2),
        trends=trends,
        top_domains=top_domains,
        recent_activity={"last_hour": recent_1h, "last_24h": recent_24h}
    )

@app.get("/api/powerbi")
async def get_powerbi_export():
    """Power BI optimized export"""
    conn = get_db_connection()
    
    query = """
        SELECT 
            id,
            email,
            category,
            spam_score * 100 as spam_score_percent,
            validity_score * 100 as validity_score_percent,
            is_disposable,
            language_detected,
            company_name,
            confidence_score,
            processed_at,
            updated_at
        FROM email_list
        ORDER BY processed_at DESC
    """
    
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    return StreamingResponse(
        iter([df.to_csv(index=False)]),
        media_type="text/csv",
        headers={
            "Content-Disposition": f"attachment; filename=powerbi_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        }
    )

@app.get("/api/insights")
@cache(expire=30)  # Cache for 30 seconds
async def get_ai_insights():
    """AI-generated insights with caching"""
    analytics = await get_analytics()
    
    insights = {
        "summary": f"Total emails analyzed: {analytics.total_emails}",
        "spam_alert": f"Spam rate: {analytics.spam_rate}%",
        "recommendations": [
            "Review high spam score emails",
            "Update blocklist based on trends",
            "Monitor category distribution"
        ],
        "anomalies": [],
        "trends": analytics.trends,
        "top_domains": analytics.top_domains,
        "generated_at": datetime.now().isoformat()
    }
    
    # Detect anomalies
    if analytics.spam_rate > 20:
        insights["anomalies"].append(f"High spam rate detected: {analytics.spam_rate}%")
    
    if analytics.recent_activity["last_hour"] > 100:
        insights["anomalies"].append("Unusual activity in last hour")
    
    return insights

@app.get("/api/stats")
async def get_stats():
    """System statistics"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    stats = {
        "database": {
            "path": DB_PATH,
            "size_mb": os.path.getsize(DB_PATH) / (1024 * 1024) if os.path.exists(DB_PATH) else 0
        },
        "connections": {
            "websocket": len(manager.active_connections),
            "message_history": len(manager.message_history)
        },
        "cache": {
            "status": "active"
        },
        "timestamp": datetime.now().isoformat()
    }
    
    conn.close()
    return stats

@app.get("/api/stream")
async def stream_data():
    """SSE endpoint for real-time data streaming"""
    async def event_generator():
        last_count = 0
        
        while True:
            try:
                conn = get_db_connection()
                cursor = conn.cursor()
                cursor.execute("SELECT COUNT(*) FROM email_list")
                current_count = cursor.fetchone()[0]
                conn.close()
                
                if current_count != last_count:
                    analytics = await get_analytics()
                    yield f"data: {json.dumps(analytics.dict())}\n\n"
                    last_count = current_count
                
                await asyncio.sleep(2)
            except Exception as e:
                yield f"error: {str(e)}\n\n"
                await asyncio.sleep(5)
    
    return StreamingResponse(event_generator(), media_type="text/event-stream")

# WebSocket endpoint
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        # Send initial data
        analytics = await get_analytics()
        await websocket.send_json(analytics.dict())
        
        while True:
            # Send updates every 2 seconds
            analytics = await get_analytics()
            await websocket.send_json(analytics.dict())
            await asyncio.sleep(2)
    except WebSocketDisconnect:
        manager.disconnect(websocket)

# Background task for broadcasting
async def broadcast_updates():
    """Broadcast updates to all WebSocket connections"""
    while True:
        if manager.active_connections:
            try:
                analytics = await get_analytics()
                await manager.broadcast(analytics.dict())
            except Exception as e:
                print(f"Broadcast error: {e}")
        await asyncio.sleep(5)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(broadcast_updates())

@app.on_event("shutdown")
async def shutdown_event():
    """Clean up"""
    global conn
    if conn:
        conn.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

