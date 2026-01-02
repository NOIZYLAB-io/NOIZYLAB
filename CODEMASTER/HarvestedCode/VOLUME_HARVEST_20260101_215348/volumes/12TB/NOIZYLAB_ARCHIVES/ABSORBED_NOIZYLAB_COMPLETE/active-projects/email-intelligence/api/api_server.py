#!/usr/bin/env python3
"""
FastAPI Server with WebSocket - Real-time Email Intelligence API
================================================================
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
import sqlite3
import json
import asyncio
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import pandas as pd
from pydantic import BaseModel
import os

app = FastAPI(title="Email Intelligence API", version="2.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration - Use app.config if available
import sys
from pathlib import Path
_parent_dir = Path(__file__).parent.parent
sys.path.insert(0, str(_parent_dir))

try:
    from app.config import DB_PATH
except ImportError:
    # Default to data directory
    DB_PATH = os.getenv("EMAIL_DB_PATH", os.path.join(_parent_dir, "data", "email_intelligence.db"))

# WebSocket connections
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []
    
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)
    
    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)
    
    async def broadcast(self, message: dict):
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except:
                pass

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

# Database helper
def get_db_connection():
    return sqlite3.connect(DB_PATH)

# Global connection and cursor for /analytics endpoint (your exact pattern)
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# API Endpoints
@app.get("/")
async def root():
    return {
        "service": "Email Intelligence API",
        "version": "2.0",
        "endpoints": {
            "websocket": "/ws",
            "analytics": "/api/analytics",
            "powerbi": "/api/powerbi",
            "insights": "/api/insights",
            "stream": "/api/stream"
        }
    }

@app.get("/api/analytics")
async def get_analytics():
    """Get current analytics"""
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
    
    conn.close()
    
    return AnalyticsResponse(
        total_emails=total,
        categories=categories,
        spam_rate=round(spam_rate, 2),
        avg_validity=round(avg_validity * 100, 2),
        trends=trends
    )

@app.get("/analytics")
async def analytics():
    """Your exact analytics endpoint"""
    cursor.execute("SELECT * FROM email_list")
    rows = cursor.fetchall()
    return {"emails": rows}

@app.get("/api/powerbi")
async def get_powerbi_export():
    """Get Power BI formatted data"""
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
        headers={"Content-Disposition": "attachment; filename=powerbi_export.csv"}
    )

@app.get("/api/insights")
async def get_ai_insights():
    """Get AI-generated insights (placeholder - integrate with Gemini)"""
    # This will be enhanced with Gemini AI
    analytics = await get_analytics()
    
    insights = {
        "summary": f"Total emails analyzed: {analytics.total_emails}",
        "spam_alert": f"Spam rate: {analytics.spam_rate}%",
        "recommendations": [
            "Review high spam score emails",
            "Update blocklist based on trends",
            "Monitor category distribution"
        ],
        "anomalies": []
    }
    
    return insights

@app.get("/api/stream")
async def stream_data():
    """SSE endpoint for real-time data streaming"""
    async def event_generator():
        conn = get_db_connection()
        last_count = 0
        
        while True:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM email_list")
            current_count = cursor.fetchone()[0]
            
            if current_count != last_count:
                analytics = await get_analytics()
                yield f"data: {json.dumps(analytics.dict())}\n\n"
                last_count = current_count
            
            await asyncio.sleep(2)
    
    return StreamingResponse(event_generator(), media_type="text/event-stream")

# WebSocket endpoint
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Send updates every 2 seconds
            analytics = await get_analytics()
            await websocket.send_json(analytics.dict())
            await asyncio.sleep(2)
    except WebSocketDisconnect:
        manager.disconnect(websocket)

# Background task for broadcasting
@app.on_event("startup")
async def startup_event():
    # Start broadcast updates
    asyncio.create_task(broadcast_updates())

@app.on_event("shutdown")
async def shutdown_event():
    """Clean up database connection"""
    global conn
    if conn:
        conn.close()

async def broadcast_updates():
    """Broadcast updates to all WebSocket connections"""
    while True:
        if manager.active_connections:
            analytics = await get_analytics()
            await manager.broadcast(analytics.dict())
        await asyncio.sleep(5)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

