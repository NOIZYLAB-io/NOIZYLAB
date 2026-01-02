#!/usr/bin/env python3
"""
Webhook Hub - Integration Hub for NoizyLab
===========================================
Supports: Zapier, Make.com, Slack, Discord, Microsoft Teams
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import json
from typing import List, Dict, Optional
from datetime import datetime
import sqlite3

app = FastAPI(title="NoizyLab Webhook Hub")

class WebhookEvent(BaseModel):
    event_type: str
    data: Dict
    source: str = "email_intelligence"

# Webhook storage
webhooks_db = "webhooks.db"

def init_db():
    conn = sqlite3.connect(webhooks_db)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS webhooks (
            id INTEGER PRIMARY KEY,
            name TEXT,
            url TEXT,
            events TEXT,
            active INTEGER DEFAULT 1,
            created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.post("/webhook/register")
async def register_webhook(name: str, url: str, events: List[str]):
    """Register a webhook"""
    conn = sqlite3.connect(webhooks_db)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO webhooks (name, url, events) VALUES (?, ?, ?)
    """, (name, url, json.dumps(events)))
    webhook_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return {"webhook_id": webhook_id, "status": "registered"}

@app.post("/webhook/trigger/{event_type}")
async def trigger_webhook(event_type: str, event: WebhookEvent):
    """Trigger webhooks for an event"""
    conn = sqlite3.connect(webhooks_db)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, name, url, events FROM webhooks WHERE active = 1
    """)
    webhooks = cursor.fetchall()
    conn.close()
    
    triggered = []
    async with httpx.AsyncClient() as client:
        for webhook_id, name, url, events_json in webhooks:
            events = json.loads(events_json)
            if event_type in events or "*" in events:
                try:
                    response = await client.post(
                        url,
                        json=event.dict(),
                        timeout=10.0
                    )
                    if response.status_code == 200:
                        triggered.append({"id": webhook_id, "name": name})
                except Exception as e:
                    print(f"Webhook error: {e}")
    
    return {"triggered": len(triggered), "webhooks": triggered}

# Zapier/Make.com endpoints
@app.post("/zapier/email-validated")
async def zapier_email_validated(data: Dict):
    """Zapier webhook for email validation"""
    event = WebhookEvent(
        event_type="email_validated",
        data=data,
        source="zapier"
    )
    return await trigger_webhook("email_validated", event)

@app.post("/make/email-enriched")
async def make_email_enriched(data: Dict):
    """Make.com webhook for email enrichment"""
    event = WebhookEvent(
        event_type="email_enriched",
        data=data,
        source="make"
    )
    return await trigger_webhook("email_enriched", event)

# Slack integration
@app.post("/slack/notify")
async def slack_notify(channel: str, message: str, webhook_url: str):
    """Send Slack notification"""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            webhook_url,
            json={"text": message, "channel": channel}
        )
        return {"status": "sent", "response": response.status_code}

# Discord integration
@app.post("/discord/notify")
async def discord_notify(message: str, webhook_url: str):
    """Send Discord notification"""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            webhook_url,
            json={"content": message}
        )
        return {"status": "sent", "response": response.status_code}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)

