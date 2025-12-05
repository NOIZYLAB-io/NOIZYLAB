#!/usr/bin/env python3
"""
Email API Endpoints - Add to api_server_v4.py
=============================================
"""

from fastapi import APIRouter, HTTPException, Depends, Header
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from email_sender import EmailSender
import os

router = APIRouter(prefix="/email", tags=["email"])
sender = EmailSender()

# Import verify_api_key from main API (or define here)
def verify_api_key(api_key: str = Header(None, alias="X-API-Key")):
    """Verify API key"""
    if not api_key:
        raise HTTPException(status_code=401, detail="API key required")
    valid_keys = os.getenv("API_KEYS", "").split(",")
    if api_key not in valid_keys and api_key != "demo-key":
        raise HTTPException(status_code=403, detail="Invalid API key")
    return api_key

# Models
class EmailRequest(BaseModel):
    to: EmailStr
    subject: str
    body: str
    html_body: Optional[str] = None
    attachments: Optional[List[str]] = None

class ContactRequest(BaseModel):
    email: EmailStr
    name: Optional[str] = ""
    company: Optional[str] = ""
    tags: Optional[List[str]] = None
    notes: Optional[str] = ""

class EmailConfigRequest(BaseModel):
    smtp_server: str
    smtp_port: int
    username: str
    password: str
    from_email: EmailStr
    from_name: Optional[str] = "NoizyLab"

# Endpoints
@router.post("/send")
async def send_email(request: EmailRequest, api_key: str = Depends(verify_api_key)):
    """Send email"""
    result = sender.send_email(
        request.to,
        request.subject,
        request.body,
        request.html_body,
        request.attachments
    )
    
    if result['status'] == 'error':
        raise HTTPException(status_code=400, detail=result['message'])
    
    return result

@router.get("/history")
async def get_email_history(limit: int = 50, api_key: str = Depends(verify_api_key)):
    """Get email history"""
    return {"emails": sender.get_email_history(limit)}

@router.post("/contacts")
async def add_contact(request: ContactRequest, api_key: str = Depends(verify_api_key)):
    """Add email contact"""
    sender.add_contact(
        request.email,
        request.name,
        request.company,
        request.tags,
        request.notes
    )
    return {"status": "success", "message": "Contact added"}

@router.get("/contacts")
async def get_contacts(api_key: str = Depends(verify_api_key)):
    """Get all contacts"""
    return {"contacts": sender.get_contacts()}

@router.post("/configure")
async def configure_email(config: EmailConfigRequest, api_key: str = Depends(verify_api_key)):
    """Configure email settings"""
    sender.configure(
        config.smtp_server,
        config.smtp_port,
        config.username,
        config.password,
        config.from_email,
        config.from_name
    )
    return {"status": "success", "message": "Email configured"}

@router.get("/status")
async def email_status(api_key: str = Depends(verify_api_key)):
    """Get email system status"""
    config = sender.config
    return {
        "configured": bool(config.get('username')),
        "smtp_server": config.get('smtp_server'),
        "from_email": config.get('from_email'),
        "from_name": config.get('from_name')
    }

