"""NoizyEconomy - Auto Email Outreach & Warm Lead Detection"""
import uuid
from datetime import datetime, timedelta

EMAIL_LOG = []
WARM_LEADS = []

EMAIL_TEMPLATES = {
    "welcome": {
        "subject": "Welcome to NoizyLab! 🎉",
        "body": "Hi {name},\n\nThank you for choosing NoizyLab for your tech needs. We're here to help!\n\nBest,\nThe NoizyLab Team",
    },
    "follow_up": {
        "subject": "How's your device running?",
        "body": "Hi {name},\n\nIt's been a week since your service. How's everything working?\n\nLet us know if you need anything!\n\nBest,\nNoizyLab",
    },
    "reactivation": {
        "subject": "We miss you! 💻",
        "body": "Hi {name},\n\nIt's been a while since we last helped you. Need any tech support?\n\nBook a session today and get 10% off!\n\nBest,\nNoizyLab",
    },
    "promotion": {
        "subject": "Special Offer Just for You! 🎁",
        "body": "Hi {name},\n\n{promo_details}\n\nBook now to claim your discount!\n\nBest,\nNoizyLab",
    },
}

def send_email(customer_id, email, template_name, custom_data=None):
    """Send an automated email"""
    template = EMAIL_TEMPLATES.get(template_name)
    if not template:
        return {"error": "Template not found"}
    
    subject = template["subject"]
    body = template["body"]
    
    # Replace placeholders
    if custom_data:
        for key, value in custom_data.items():
            subject = subject.replace(f"{{{key}}}", str(value))
            body = body.replace(f"{{{key}}}", str(value))
    
    email_record = {
        "id": str(uuid.uuid4()),
        "customer_id": customer_id,
        "to": email,
        "subject": subject,
        "body": body,
        "template": template_name,
        "sent_at": datetime.now().isoformat(),
        "opened": False,
        "clicked": False,
    }
    EMAIL_LOG.append(email_record)
    
    # Integration point for actual email sending
    
    return email_record

def warm_lead_detect(customer_data):
    """Detect warm leads based on behavior signals"""
    signals = []
    score = 0
    
    # Website visit frequency
    if customer_data.get("recent_visits", 0) > 3:
        signals.append("frequent_visitor")
        score += 25
    
    # Viewed pricing page
    if customer_data.get("viewed_pricing"):
        signals.append("pricing_interest")
        score += 30
    
    # Started booking but didn't complete
    if customer_data.get("abandoned_booking"):
        signals.append("abandoned_booking")
        score += 35
    
    # Opened recent emails
    if customer_data.get("email_opens", 0) > 2:
        signals.append("email_engaged")
        score += 20
    
    # Clicked email links
    if customer_data.get("email_clicks", 0) > 0:
        signals.append("email_clicker")
        score += 25
    
    # Returning customer
    if customer_data.get("previous_customer"):
        signals.append("returning_customer")
        score += 30
    
    # Referred by someone
    if customer_data.get("referral"):
        signals.append("referral")
        score += 20
    
    lead = {
        "customer_id": customer_data.get("id"),
        "email": customer_data.get("email"),
        "score": min(score, 100),
        "signals": signals,
        "detected_at": datetime.now().isoformat(),
        "status": "warm" if score >= 50 else "cold",
        "recommended_action": get_recommended_action(score, signals),
    }
    
    if score >= 50:
        WARM_LEADS.append(lead)
    
    return lead

def get_recommended_action(score, signals):
    """Get recommended action for a lead"""
    if score >= 80:
        return "Call immediately - high intent"
    if "abandoned_booking" in signals:
        return "Send booking reminder email"
    if score >= 50:
        return "Send personalized follow-up"
    return "Add to nurture campaign"

def get_warm_leads():
    """Get all warm leads"""
    return sorted(WARM_LEADS, key=lambda x: x["score"], reverse=True)

def get_email_stats():
    """Get email campaign statistics"""
    total = len(EMAIL_LOG)
    if total == 0:
        return {"total": 0, "open_rate": 0, "click_rate": 0}
    
    opened = len([e for e in EMAIL_LOG if e["opened"]])
    clicked = len([e for e in EMAIL_LOG if e["clicked"]])
    
    return {
        "total_sent": total,
        "opened": opened,
        "clicked": clicked,
        "open_rate": round(opened / total * 100, 1),
        "click_rate": round(clicked / total * 100, 1),
    }

def schedule_drip_campaign(customer_id, email, campaign_type="welcome"):
    """Schedule a drip email campaign"""
    schedule = []
    
    if campaign_type == "welcome":
        schedule = [
            {"template": "welcome", "delay_days": 0},
            {"template": "follow_up", "delay_days": 7},
        ]
    elif campaign_type == "reactivation":
        schedule = [
            {"template": "reactivation", "delay_days": 0},
            {"template": "promotion", "delay_days": 3},
        ]
    
    for item in schedule:
        send_date = datetime.now() + timedelta(days=item["delay_days"])
        item["customer_id"] = customer_id
        item["email"] = email
        item["scheduled_for"] = send_date.isoformat()
    
    return schedule

