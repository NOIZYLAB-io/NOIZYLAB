#!/usr/bin/env python3
"""
Universal Webhook Manager
=========================
Manage and route webhooks from any source to any destination
"""

import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
from fastapi import FastAPI, Request, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse
import requests
import json
import hmac
import hashlib


app = FastAPI(title="NoizyLab Webhook Manager", version="1.0.0")


class WebhookManager:
    """Universal webhook management system"""
    
    def __init__(self):
        self.db_path = Path(__file__).parent / "webhooks.db"
        self._init_database()
    
    def _init_database(self):
        """Initialize webhook database"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        # Webhook endpoints
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS webhook_endpoints (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                url TEXT NOT NULL,
                method TEXT DEFAULT 'POST',
                headers TEXT,
                auth_type TEXT,
                auth_credentials TEXT,
                enabled BOOLEAN DEFAULT 1,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Webhook routes (source -> destination mapping)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS webhook_routes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                source_pattern TEXT NOT NULL,
                destination_endpoint_id INTEGER,
                transform_script TEXT,
                filter_script TEXT,
                enabled BOOLEAN DEFAULT 1,
                priority INTEGER DEFAULT 0,
                FOREIGN KEY (destination_endpoint_id) REFERENCES webhook_endpoints(id)
            )
        """)
        
        # Webhook logs
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS webhook_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                source TEXT,
                route_id INTEGER,
                endpoint_id INTEGER,
                payload TEXT,
                response_status INTEGER,
                response_body TEXT,
                duration REAL,
                success BOOLEAN,
                error TEXT
            )
        """)
        
        # Webhook queue (for retry)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS webhook_queue (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                endpoint_id INTEGER,
                payload TEXT,
                retry_count INTEGER DEFAULT 0,
                max_retries INTEGER DEFAULT 3,
                next_retry DATETIME,
                status TEXT DEFAULT 'pending',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (endpoint_id) REFERENCES webhook_endpoints(id)
            )
        """)
        
        conn.commit()
        conn.close()
    
    def register_endpoint(self, name: str, url: str, method: str = "POST",
                         headers: Optional[Dict] = None, auth_type: Optional[str] = None,
                         auth_credentials: Optional[str] = None) -> int:
        """Register a new webhook endpoint"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO webhook_endpoints (name, url, method, headers, auth_type, auth_credentials)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            name,
            url,
            method,
            json.dumps(headers) if headers else None,
            auth_type,
            auth_credentials
        ))
        
        endpoint_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return endpoint_id
    
    def create_route(self, name: str, source_pattern: str, destination_endpoint_id: int,
                    transform_script: Optional[str] = None, filter_script: Optional[str] = None,
                    priority: int = 0) -> int:
        """Create a webhook route"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO webhook_routes 
            (name, source_pattern, destination_endpoint_id, transform_script, filter_script, priority)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, source_pattern, destination_endpoint_id, transform_script, filter_script, priority))
        
        route_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return route_id
    
    def send_webhook(self, endpoint_id: int, payload: Dict) -> Dict:
        """Send webhook to endpoint"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT url, method, headers, auth_type, auth_credentials
            FROM webhook_endpoints
            WHERE id = ? AND enabled = 1
        """, (endpoint_id,))
        
        result = cursor.fetchone()
        conn.close()
        
        if not result:
            return {"success": False, "error": "Endpoint not found or disabled"}
        
        url, method, headers_json, auth_type, auth_credentials = result
        
        # Parse headers
        headers = json.loads(headers_json) if headers_json else {}
        headers.setdefault("Content-Type", "application/json")
        
        # Add authentication
        if auth_type == "bearer":
            headers["Authorization"] = f"Bearer {auth_credentials}"
        elif auth_type == "basic":
            import base64
            encoded = base64.b64encode(auth_credentials.encode()).decode()
            headers["Authorization"] = f"Basic {encoded}"
        
        # Send request
        start_time = datetime.now()
        
        try:
            if method.upper() == "POST":
                response = requests.post(url, json=payload, headers=headers, timeout=10)
            elif method.upper() == "PUT":
                response = requests.put(url, json=payload, headers=headers, timeout=10)
            else:
                response = requests.get(url, params=payload, headers=headers, timeout=10)
            
            duration = (datetime.now() - start_time).total_seconds()
            
            # Log result
            self._log_webhook(
                source="direct",
                endpoint_id=endpoint_id,
                payload=payload,
                response_status=response.status_code,
                response_body=response.text,
                duration=duration,
                success=response.status_code < 400
            )
            
            return {
                "success": response.status_code < 400,
                "status_code": response.status_code,
                "response": response.text,
                "duration": duration
            }
            
        except Exception as e:
            duration = (datetime.now() - start_time).total_seconds()
            
            self._log_webhook(
                source="direct",
                endpoint_id=endpoint_id,
                payload=payload,
                response_status=0,
                response_body=None,
                duration=duration,
                success=False,
                error=str(e)
            )
            
            return {"success": False, "error": str(e)}
    
    def _log_webhook(self, source: str, endpoint_id: int, payload: Dict,
                    response_status: int, response_body: Optional[str],
                    duration: float, success: bool, error: Optional[str] = None):
        """Log webhook call"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO webhook_logs
            (source, endpoint_id, payload, response_status, response_body, duration, success, error)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            source,
            endpoint_id,
            json.dumps(payload),
            response_status,
            response_body,
            duration,
            success,
            error
        ))
        
        conn.commit()
        conn.close()
    
    def get_webhook_stats(self) -> Dict:
        """Get webhook statistics"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT 
                COUNT(*) as total,
                SUM(CASE WHEN success = 1 THEN 1 ELSE 0 END) as successful,
                AVG(duration) as avg_duration,
                MAX(duration) as max_duration
            FROM webhook_logs
            WHERE timestamp > datetime('now', '-24 hours')
        """)
        
        total, successful, avg_duration, max_duration = cursor.fetchone()
        conn.close()
        
        return {
            "total_24h": total or 0,
            "successful_24h": successful or 0,
            "failed_24h": (total - successful) if total else 0,
            "success_rate": (successful / total * 100) if total else 0,
            "avg_duration": avg_duration or 0,
            "max_duration": max_duration or 0
        }


# Global webhook manager
webhook_manager = WebhookManager()


@app.post("/webhooks/receive/{source}")
async def receive_webhook(source: str, request: Request, background_tasks: BackgroundTasks):
    """Receive and route webhooks"""
    payload = await request.json()
    
    # Find matching routes
    conn = sqlite3.connect(str(webhook_manager.db_path))
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT id, destination_endpoint_id, transform_script, filter_script
        FROM webhook_routes
        WHERE source_pattern = ? AND enabled = 1
        ORDER BY priority DESC
    """, (source,))
    
    routes = cursor.fetchall()
    conn.close()
    
    if not routes:
        return {"message": "No routes configured", "payload_received": True}
    
    results = []
    
    for route_id, endpoint_id, transform_script, filter_script in routes:
        # Apply filter if present
        if filter_script:
            # Simple eval-based filter (in production, use safer method)
            try:
                if not eval(filter_script, {"payload": payload}):
                    continue
            except:
                pass
        
        # Transform payload if script present
        transformed_payload = payload
        if transform_script:
            try:
                transformed_payload = eval(transform_script, {"payload": payload})
            except:
                pass
        
        # Send to destination (in background)
        background_tasks.add_task(
            webhook_manager.send_webhook,
            endpoint_id,
            transformed_payload
        )
        
        results.append({
            "route_id": route_id,
            "endpoint_id": endpoint_id,
            "queued": True
        })
    
    return {
        "success": True,
        "source": source,
        "routes_matched": len(results),
        "results": results
    }


@app.post("/webhooks/send/{endpoint_name}")
async def send_webhook_by_name(endpoint_name: str, payload: Dict):
    """Send webhook to named endpoint"""
    conn = sqlite3.connect(str(webhook_manager.db_path))
    cursor = conn.cursor()
    
    cursor.execute("SELECT id FROM webhook_endpoints WHERE name = ?", (endpoint_name,))
    result = cursor.fetchone()
    conn.close()
    
    if not result:
        raise HTTPException(status_code=404, detail="Endpoint not found")
    
    endpoint_id = result[0]
    result = webhook_manager.send_webhook(endpoint_id, payload)
    
    return result


@app.get("/webhooks/stats")
async def get_stats():
    """Get webhook statistics"""
    return webhook_manager.get_webhook_stats()


@app.get("/webhooks/endpoints")
async def list_endpoints():
    """List all webhook endpoints"""
    conn = sqlite3.connect(str(webhook_manager.db_path))
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT id, name, url, method, enabled, created_at
        FROM webhook_endpoints
        ORDER BY created_at DESC
    """)
    
    endpoints = []
    for row in cursor.fetchall():
        endpoints.append({
            "id": row[0],
            "name": row[1],
            "url": row[2],
            "method": row[3],
            "enabled": bool(row[4]),
            "created_at": row[5]
        })
    
    conn.close()
    return {"endpoints": endpoints}


@app.get("/webhooks/logs")
async def get_logs(limit: int = 100):
    """Get recent webhook logs"""
    conn = sqlite3.connect(str(webhook_manager.db_path))
    cursor = conn.cursor()
    
    cursor.execute("""
        SELECT timestamp, source, endpoint_id, response_status, duration, success, error
        FROM webhook_logs
        ORDER BY timestamp DESC
        LIMIT ?
    """, (limit,))
    
    logs = []
    for row in cursor.fetchall():
        logs.append({
            "timestamp": row[0],
            "source": row[1],
            "endpoint_id": row[2],
            "response_status": row[3],
            "duration": row[4],
            "success": bool(row[5]),
            "error": row[6]
        })
    
    conn.close()
    return {"logs": logs}


if __name__ == "__main__":
    import uvicorn
    
    print("🎣 Starting Webhook Manager...")
    print("📡 API: http://localhost:8006")
    
    uvicorn.run(app, host="0.0.0.0", port=8006)

