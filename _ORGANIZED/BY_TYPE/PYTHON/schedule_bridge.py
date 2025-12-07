"""FrontDesk: Schedule Bridge"""
from ..economy.scheduler import auto_book, get_availability
import uuid

PENDING_BOOKINGS = {}

def schedule_client(client_info, preferred=None):
    """Schedule a client appointment"""
    booking = auto_book(client_info.get("id", str(uuid.uuid4())), preferred)
    if "error" not in booking:
        PENDING_BOOKINGS[booking["id"]] = {**booking, "client_info": client_info, "confirmed": False}
    return booking

def confirm_booking(booking_id):
    if booking_id in PENDING_BOOKINGS:
        PENDING_BOOKINGS[booking_id]["confirmed"] = True
        return PENDING_BOOKINGS[booking_id]
    return None

def get_pending():
    return [b for b in PENDING_BOOKINGS.values() if not b["confirmed"]]

def suggest_times(count=5):
    slots = get_availability(7)
    return slots[:count]

