from fastapi import APIRouter
from datetime import datetime
import uuid

router = APIRouter()

# In-memory invoice store
INVOICES = {}


@router.post("/create")
def create_invoice(payload: dict):
    """Generate a PDF invoice"""
    email = payload["email"]
    service = payload["service"]
    price = float(payload["price"])
    booking_id = payload.get("booking_id", "N/A")
    
    inv_id = str(uuid.uuid4())[:8]
    date = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # Build invoice content
    invoice_content = f"""
=====================================
        NOIZYLAB INVOICE
=====================================

Invoice ID: {inv_id}
Date: {date}

-------------------------------------
CLIENT INFORMATION
-------------------------------------
Email: {email}

-------------------------------------
SERVICE DETAILS
-------------------------------------
Service: {service}
Booking ID: {booking_id}

-------------------------------------
PAYMENT
-------------------------------------
Amount: ${price:.2f} CAD
Status: PAID

-------------------------------------

Thank you for choosing NoizyLab!
Your device is in good hands.

Questions? Contact: help@noizylab.ca

=====================================
         GORUNFREE!
=====================================
"""
    
    # Store invoice
    INVOICES[inv_id] = {
        "content": invoice_content,
        "email": email,
        "service": service,
        "price": price,
        "booking_id": booking_id,
        "date": date,
        "hex": invoice_content.encode().hex()
    }
    
    return {
        "ok": True,
        "invoice_id": inv_id,
        "content": invoice_content
    }


@router.get("/file/{inv_id}")
def get_invoice_file(inv_id: str):
    """Get invoice file for download"""
    if inv_id not in INVOICES:
        return {"error": "Invoice not found"}
    return {
        "hex": INVOICES[inv_id]["hex"],
        "content": INVOICES[inv_id]["content"]
    }


@router.get("/list/{email}")
def list_invoices(email: str):
    """List all invoices for a client"""
    user_invoices = [
        {"id": k, **{key: v[key] for key in ["date", "service", "price"]}}
        for k, v in INVOICES.items()
        if v["email"] == email
    ]
    return {"invoices": user_invoices}


@router.get("/all")
def all_invoices():
    """List all invoices (technician view)"""
    return {"invoices": list(INVOICES.keys()), "count": len(INVOICES)}

