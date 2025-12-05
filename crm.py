"""NoizyEconomy - Auto CRM (Customer Relationship Management)"""
import uuid
from datetime import datetime, timedelta

CUSTOMER_DB = {}

def get_customer(customer_id):
    """Get customer by ID"""
    return CUSTOMER_DB.get(customer_id)

def create_customer(data):
    """Create a new customer record"""
    customer_id = str(uuid.uuid4())
    customer = {
        "id": customer_id,
        "name": data.get("name"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "address": data.get("address"),
        "created_at": datetime.now().isoformat(),
        "last_contact": datetime.now().isoformat(),
        "total_spent": 0,
        "visit_count": 0,
        "devices": [],
        "notes": [],
        "tags": [],
        "satisfaction_score": None,
        "referral_source": data.get("referral_source"),
        "lifetime_value": 0,
    }
    CUSTOMER_DB[customer_id] = customer
    return customer

def update_customer(customer_id, updates):
    """Update customer record"""
    if customer_id not in CUSTOMER_DB:
        return None
    CUSTOMER_DB[customer_id].update(updates)
    CUSTOMER_DB[customer_id]["last_contact"] = datetime.now().isoformat()
    return CUSTOMER_DB[customer_id]

def add_device(customer_id, device_info):
    """Add a device to customer record"""
    if customer_id not in CUSTOMER_DB:
        return None
    CUSTOMER_DB[customer_id]["devices"].append({
        **device_info,
        "added_at": datetime.now().isoformat(),
    })
    return CUSTOMER_DB[customer_id]

def record_visit(customer_id, amount_spent):
    """Record a customer visit"""
    if customer_id not in CUSTOMER_DB:
        return None
    CUSTOMER_DB[customer_id]["visit_count"] += 1
    CUSTOMER_DB[customer_id]["total_spent"] += amount_spent
    CUSTOMER_DB[customer_id]["lifetime_value"] = calculate_ltv(customer_id)
    CUSTOMER_DB[customer_id]["last_contact"] = datetime.now().isoformat()
    return CUSTOMER_DB[customer_id]

def calculate_ltv(customer_id):
    """Calculate customer lifetime value"""
    customer = CUSTOMER_DB.get(customer_id)
    if not customer:
        return 0
    avg_spend = customer["total_spent"] / max(customer["visit_count"], 1)
    return round(avg_spend * 5, 2)  # Estimate 5 future visits

def detect_upsell(customer_id):
    """Detect upsell opportunities"""
    customer = CUSTOMER_DB.get(customer_id)
    if not customer:
        return []
    
    opportunities = []
    
    # Check device age
    for device in customer.get("devices", []):
        if device.get("age_years", 0) > 4:
            opportunities.append({
                "type": "upgrade",
                "device": device.get("type"),
                "reason": "Device is over 4 years old",
                "suggested_action": "Recommend new device or major upgrade",
            })
    
    # Check visit frequency
    if customer["visit_count"] >= 3:
        opportunities.append({
            "type": "maintenance_plan",
            "reason": "Frequent visitor",
            "suggested_action": "Offer monthly maintenance subscription",
        })
    
    # Check total spent
    if customer["total_spent"] > 500:
        opportunities.append({
            "type": "vip_program",
            "reason": "High-value customer",
            "suggested_action": "Invite to VIP program with discounts",
        })
    
    return opportunities

def get_retention_alerts():
    """Get customers needing attention"""
    alerts = []
    cutoff = datetime.now() - timedelta(days=90)
    
    for customer in CUSTOMER_DB.values():
        last_contact = datetime.fromisoformat(customer["last_contact"])
        if last_contact < cutoff:
            alerts.append({
                "customer_id": customer["id"],
                "name": customer["name"],
                "days_since_contact": (datetime.now() - last_contact).days,
                "action": "Send follow-up email or call",
            })
    
    return alerts

def search_customers(query):
    """Search customers by name, email, or phone"""
    query = query.lower()
    return [c for c in CUSTOMER_DB.values() 
            if query in c.get("name", "").lower() 
            or query in c.get("email", "").lower()
            or query in c.get("phone", "").lower()]

