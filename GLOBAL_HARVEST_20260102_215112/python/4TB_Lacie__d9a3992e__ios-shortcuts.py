#!/usr/bin/env python3
"""
iOS Shortcuts Integration - Mobile API for NoizyLab
====================================================
Provides mobile-optimized endpoints for iOS Shortcuts
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr
import sqlite3
import requests
import json

app = FastAPI(title="NoizyLab Mobile API")

DB_PATH = "../email-intelligence/email_intelligence.db"
API_URL = "http://localhost:8000"

class MobileEmailRequest(BaseModel):
    email: EmailStr
    api_key: str = "mobile-key"

@app.get("/mobile/health")
async def mobile_health():
    """Mobile health check"""
    return {
        "status": "ok",
        "version": "4.0",
        "mobile": True
    }

@app.post("/mobile/validate")
async def mobile_validate(request: MobileEmailRequest):
    """Mobile-optimized email validation"""
    try:
        response = requests.post(
            f"{API_URL}/validate",
            json={"email": request.email},
            headers={"X-API-Key": request.api_key},
            timeout=5
        )
        
        if response.status_code == 200:
            data = response.json()
            return {
                "valid": data.get("valid", False),
                "domain": data.get("domain", ""),
                "score": data.get("quality_score", 0),
                "category": data.get("category", "unknown")
            }
        else:
            raise HTTPException(status_code=response.status_code, detail="Validation failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/mobile/stats")
async def mobile_stats(api_key: str = "mobile-key"):
    """Mobile-optimized stats"""
    try:
        response = requests.get(
            f"{API_URL}/analytics",
            headers={"X-API-Key": api_key},
            timeout=5
        )
        
        if response.status_code == 200:
            data = response.json()
            emails = data.get("emails", [])
            return {
                "total": len(emails),
                "valid": len([e for e in emails if e.get("valid", False)]),
                "categories": len(set([e.get("category", "unknown") for e in emails]))
            }
        else:
            raise HTTPException(status_code=response.status_code)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/mobile/quick-block")
async def mobile_quick_block(domain: str, api_key: str = "mobile-key"):
    """Quick block domain from mobile"""
    # Add to blocklist
    blocklist_path = "../universal-blocker/blocklist.txt"
    try:
        with open(blocklist_path, "a") as f:
            f.write(f"\n{domain}")
        return {"status": "blocked", "domain": domain}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)

