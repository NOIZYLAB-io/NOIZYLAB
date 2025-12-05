from fastapi import APIRouter
from datetime import datetime
from typing import List, Dict

router = APIRouter()

# In-memory store (replace with database in production)
BOOKINGS: List[Dict] = []


@router.post("/book")
def book(payload: dict):
    """Create a new booking"""
    entry = {
        "id": len(BOOKINGS) + 1,
        "email": payload["email"],
        "type": payload.get("type", "remote"),  # "remote" or "local"
        "time": payload.get("time", "TBD"),
        "service": payload.get("service", "General Repair"),
        "price": float(payload.get("price", 0)),
        "date_booked": datetime.now().isoformat(),
        "status": "pending",
        "paid": False,
        "notes": payload.get("notes", "")
    }
    BOOKINGS.append(entry)
    return {"ok": True, "booking": entry}


@router.get("/user/{email}")
def user_bookings(email: str):
    """Get all bookings for a user"""
    user_books = [b for b in BOOKINGS if b["email"] == email]
    return {"bookings": user_books}


@router.get("/all")
def all_bookings():
    """Get all bookings (technician view)"""
    return {"bookings": BOOKINGS}


@router.get("/pending")
def pending_bookings():
    """Get pending bookings"""
    pending = [b for b in BOOKINGS if b["status"] == "pending"]
    return {"bookings": pending}


@router.post("/markpaid")
def mark_paid(payload: dict):
    """Mark a booking as paid"""
    booking_id = payload.get("id")
    for b in BOOKINGS:
        if b["id"] == booking_id:
            b["paid"] = True
            b["status"] = "confirmed"
            return {"ok": True, "booking": b}
    return {"ok": False, "error": "Booking not found"}


@router.post("/complete")
def complete_booking(payload: dict):
    """Mark a booking as completed"""
    booking_id = payload.get("id")
    for b in BOOKINGS:
        if b["id"] == booking_id:
            b["status"] = "completed"
            return {"ok": True, "booking": b}
    return {"ok": False, "error": "Booking not found"}


@router.post("/cancel")
def cancel_booking(payload: dict):
    """Cancel a booking"""
    booking_id = payload.get("id")
    for b in BOOKINGS:
        if b["id"] == booking_id:
            b["status"] = "cancelled"
            return {"ok": True}
    return {"ok": False, "error": "Booking not found"}


@router.get("/available-slots")
def available_slots():
    """Get available time slots (AI-powered in future)"""
    return {
        "slots": [
            {"date": "2024-12-02", "time": "10:00 AM", "available": True},
            {"date": "2024-12-02", "time": "2:00 PM", "available": True},
            {"date": "2024-12-03", "time": "11:00 AM", "available": True},
            {"date": "2024-12-03", "time": "3:00 PM", "available": True},
        ]
    }

