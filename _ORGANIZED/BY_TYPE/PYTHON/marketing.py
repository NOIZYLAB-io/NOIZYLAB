"""NoizyEconomy - Auto-Generated Marketing Content"""
import uuid
from datetime import datetime

CONTENT_DB = {}
SCHEDULED_POSTS = []

TEMPLATES = {
    "service_promo": [
        "💻 Computer running slow? We can help! Fast, affordable tech support. Book now!",
        "🔧 Expert computer repair at your doorstep. Same-day service available!",
        "🚀 Speed up your PC today! Professional diagnostics and optimization.",
    ],
    "tip": [
        "💡 Tech Tip: Restart your computer weekly to keep it running smoothly!",
        "💡 Pro Tip: Keep your software updated to stay secure and fast!",
        "💡 Did you know? Cleaning dust from your PC can improve performance by 20%!",
    ],
    "testimonial_request": [
        "Loved our service? Leave us a review! Your feedback helps us grow. ⭐",
        "Happy with your repair? Share your experience and help others find us!",
    ],
    "seasonal": [
        "🎄 Holiday Special: 15% off all services this month!",
        "📚 Back to School: Student discount on laptop repairs!",
        "🌞 Summer Sale: Free diagnostics with any repair!",
    ],
}

def generate_content(content_type="service_promo", custom_data=None):
    """Generate marketing content"""
    import random
    
    templates = TEMPLATES.get(content_type, TEMPLATES["service_promo"])
    base_content = random.choice(templates)
    
    if custom_data:
        for key, value in custom_data.items():
            base_content = base_content.replace(f"{{{key}}}", str(value))
    
    content_id = str(uuid.uuid4())
    content = {
        "id": content_id,
        "type": content_type,
        "content": base_content,
        "created_at": datetime.now().isoformat(),
        "status": "draft",
        "platforms": [],
    }
    CONTENT_DB[content_id] = content
    return content

def schedule_post(content_id, platform, scheduled_time):
    """Schedule a post for a platform"""
    if content_id not in CONTENT_DB:
        return None
    
    post = {
        "content_id": content_id,
        "platform": platform,
        "scheduled_time": scheduled_time.isoformat() if isinstance(scheduled_time, datetime) else scheduled_time,
        "status": "scheduled",
        "posted_at": None,
    }
    SCHEDULED_POSTS.append(post)
    CONTENT_DB[content_id]["platforms"].append(platform)
    CONTENT_DB[content_id]["status"] = "scheduled"
    return post

def get_scheduled_posts():
    """Get all scheduled posts"""
    return [p for p in SCHEDULED_POSTS if p["status"] == "scheduled"]

def generate_week_content():
    """Generate a week's worth of content"""
    content_plan = []
    types = ["service_promo", "tip", "service_promo", "tip", "testimonial_request", "service_promo", "tip"]
    
    for i, content_type in enumerate(types):
        content = generate_content(content_type)
        content_plan.append(content)
    
    return content_plan

def get_content_stats():
    """Get content generation stats"""
    return {
        "total_generated": len(CONTENT_DB),
        "scheduled": len([c for c in CONTENT_DB.values() if c["status"] == "scheduled"]),
        "posted": len([c for c in CONTENT_DB.values() if c["status"] == "posted"]),
        "drafts": len([c for c in CONTENT_DB.values() if c["status"] == "draft"]),
    }

