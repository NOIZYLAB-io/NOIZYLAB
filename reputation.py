"""NoizyEconomy - Auto Reputation Management"""
import uuid
from datetime import datetime

REVIEW_REQUESTS = []
REVIEWS = []

def request_review(customer_id, customer_email, service_date=None):
    """Send automated review request"""
    request_id = str(uuid.uuid4())
    request = {
        "id": request_id,
        "customer_id": customer_id,
        "email": customer_email,
        "service_date": service_date or datetime.now().isoformat(),
        "sent_at": datetime.now().isoformat(),
        "status": "sent",
        "reminder_count": 0,
        "review_received": False,
    }
    REVIEW_REQUESTS.append(request)
    
    # Auto-send email (placeholder)
    send_review_email(customer_email)
    
    return request

def send_review_email(email):
    """Send review request email"""
    # Integration point for email service
    pass

def track_reviews():
    """Get review statistics"""
    total = len(REVIEWS)
    if total == 0:
        return {"total": 0, "average": 0, "five_star": 0, "four_star": 0}
    
    avg = sum(r["rating"] for r in REVIEWS) / total
    return {
        "total": total,
        "average": round(avg, 2),
        "five_star": len([r for r in REVIEWS if r["rating"] == 5]),
        "four_star": len([r for r in REVIEWS if r["rating"] == 4]),
        "three_star": len([r for r in REVIEWS if r["rating"] == 3]),
        "below_three": len([r for r in REVIEWS if r["rating"] < 3]),
        "response_rate": calculate_response_rate(),
    }

def calculate_response_rate():
    """Calculate review response rate"""
    if not REVIEW_REQUESTS:
        return 0
    received = len([r for r in REVIEW_REQUESTS if r["review_received"]])
    return round(received / len(REVIEW_REQUESTS) * 100, 1)

def add_review(customer_id, rating, text, platform="google"):
    """Record a new review"""
    review = {
        "id": str(uuid.uuid4()),
        "customer_id": customer_id,
        "rating": rating,
        "text": text,
        "platform": platform,
        "received_at": datetime.now().isoformat(),
        "responded": False,
        "response_text": None,
    }
    REVIEWS.append(review)
    
    # Mark request as received
    for req in REVIEW_REQUESTS:
        if req["customer_id"] == customer_id and not req["review_received"]:
            req["review_received"] = True
            break
    
    # Alert if negative
    if rating < 3:
        create_negative_review_alert(review)
    
    return review

def create_negative_review_alert(review):
    """Create alert for negative review"""
    return {
        "type": "negative_review",
        "review_id": review["id"],
        "rating": review["rating"],
        "action": "Respond within 24 hours",
        "priority": "high",
    }

def respond_to_review(review_id, response_text):
    """Record response to a review"""
    for review in REVIEWS:
        if review["id"] == review_id:
            review["responded"] = True
            review["response_text"] = response_text
            review["responded_at"] = datetime.now().isoformat()
            return review
    return None

def get_pending_responses():
    """Get reviews needing responses"""
    return [r for r in REVIEWS if not r["responded"]]

