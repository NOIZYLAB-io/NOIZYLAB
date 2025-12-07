"""NoizyFrontDesk - Appointment Booking"""
import uuid
from datetime import datetime

BOOKINGS = {}

def book_appointment(customer_info, slot, service_type="diagnostic"):
    """Book an appointment"""
    booking_id = f"BK-{uuid.uuid4().hex[:8].upper()}"
    
    booking = {
        "id": booking_id,
        "customer_name": customer_info.get("name"),
        "customer_email": customer_info.get("email"),
        "customer_phone": customer_info.get("phone"),
        "device_type": customer_info.get("device_type"),
        "issue_description": customer_info.get("issue"),
        "service_type": service_type,
        "slot": slot,
        "status": "pending_confirmation",
        "created_at": datetime.now().isoformat(),
        "confirmed_at": None,
        "reminder_sent": False,
        "source": customer_info.get("source", "chat"),
    }
    BOOKINGS[booking_id] = booking
    
    # Send confirmation request
    send_confirmation_request(booking)
    
    return booking

def send_confirmation_request(booking):
    """Send confirmation request to customer"""
    # Integration point for email/SMS
    pass

def confirm_booking(booking_id, confirmation_code=None):
    """Confirm a booking"""
    if booking_id not in BOOKINGS:
        return {"error": "Booking not found"}
    
    BOOKINGS[booking_id]["status"] = "confirmed"
    BOOKINGS[booking_id]["confirmed_at"] = datetime.now().isoformat()
    
    # Create ticket for confirmed booking
    from .ticket import create_ticket
    ticket = create_ticket({
        "customer_name": BOOKINGS[booking_id]["customer_name"],
        "device_type": BOOKINGS[booking_id]["device_type"],
        "issue": BOOKINGS[booking_id]["issue_description"],
        "booking_id": booking_id,
    })
    BOOKINGS[booking_id]["ticket_id"] = ticket["id"]
    
    return BOOKINGS[booking_id]

def cancel_booking(booking_id, reason=None):
    """Cancel a booking"""
    if booking_id not in BOOKINGS:
        return {"error": "Booking not found"}
    
    BOOKINGS[booking_id]["status"] = "cancelled"
    BOOKINGS[booking_id]["cancelled_at"] = datetime.now().isoformat()
    BOOKINGS[booking_id]["cancel_reason"] = reason
    
    return BOOKINGS[booking_id]

def reschedule_booking(booking_id, new_slot):
    """Reschedule a booking"""
    if booking_id not in BOOKINGS:
        return {"error": "Booking not found"}
    
    old_slot = BOOKINGS[booking_id]["slot"]
    BOOKINGS[booking_id]["slot"] = new_slot
    BOOKINGS[booking_id]["rescheduled_from"] = old_slot
    BOOKINGS[booking_id]["rescheduled_at"] = datetime.now().isoformat()
    BOOKINGS[booking_id]["status"] = "pending_confirmation"
    
    return BOOKINGS[booking_id]

def get_booking(booking_id):
    """Get booking by ID"""
    return BOOKINGS.get(booking_id)

def get_upcoming_bookings():
    """Get all upcoming confirmed bookings"""
    now = datetime.now()
    upcoming = []
    for booking in BOOKINGS.values():
        if booking["status"] == "confirmed":
            slot_time = datetime.fromisoformat(booking["slot"]["start"]) if isinstance(booking["slot"], dict) else datetime.fromisoformat(booking["slot"])
            if slot_time > now:
                upcoming.append(booking)
    return sorted(upcoming, key=lambda x: x["slot"]["start"] if isinstance(x["slot"], dict) else x["slot"])

def get_todays_bookings():
    """Get today's bookings"""
    today = datetime.now().date()
    todays = []
    for booking in BOOKINGS.values():
        if booking["status"] == "confirmed":
            slot_time = datetime.fromisoformat(booking["slot"]["start"]) if isinstance(booking["slot"], dict) else datetime.fromisoformat(booking["slot"])
            if slot_time.date() == today:
                todays.append(booking)
    return todays

