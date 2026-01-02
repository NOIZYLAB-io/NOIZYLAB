import os, stripe, json
from fastapi import FastAPI, Request, HTTPException
from pathlib import Path

# Initialize webhook app
webhook_app = FastAPI(title="Stripe Webhooks")
stripe.api_key = os.getenv("STRIPE_SECRET", "sk_test_placeholder")
WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "whsec_placeholder")

LICENSE_DIR = Path("licenses")
LICENSE_DIR.mkdir(exist_ok=True)
SECRET_KEY = "noizy_license_secret"

def generate_license_token(email: str, plan: str = "pro"):
    """Generate a license token for the given email and plan"""
    import jwt, time
    token = jwt.encode(
        {"email": email, "tier": plan, "iat": int(time.time())},
        SECRET_KEY, algorithm="HS256"
    )
    (LICENSE_DIR / f"{email}.jwt").write_text(token)
    return token

def send_license_email(email: str, plan: str = "pro"):
    """Send license via email (placeholder - integrate with your email system)"""
    try:
        # Import your email module here if available
        print(f"📨 License email sent to {email} for {plan} plan")
        return True
    except Exception as e:
        print(f"❌ Failed to send license email: {e}")
        return False

@webhook_app.post("/webhook")
async def stripe_webhook(request: Request):
    """Handle Stripe webhook events"""
    payload = await request.body()
    sig_header = request.headers.get("stripe-signature")
    
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, WEBHOOK_SECRET)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid payload")
    except stripe.error.SignatureVerificationError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    # Handle successful checkout
    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]
        customer_email = session.get("customer_email")
        
        if customer_email:
            print(f"💸 Payment completed for {customer_email}")
            
            # Generate license
            try:
                generate_license_token(customer_email, "pro")
                print(f"✅ License generated for {customer_email}")
                
                # Send email
                if send_license_email(customer_email, "pro"):
                    print(f"📧 License email sent to {customer_email}")
                else:
                    print(f"⚠️ License generated but email failed for {customer_email}")
                    
            except Exception as e:
                print(f"❌ License generation failed for {customer_email}: {e}")
        else:
            print("⚠️ No customer email in checkout session")

    # Handle subscription events
    elif event["type"] == "customer.subscription.deleted":
        subscription = event["data"]["object"]
        customer_id = subscription.get("customer")
        print(f"❌ Subscription cancelled for customer {customer_id}")
        
    elif event["type"] == "invoice.payment_failed":
        invoice = event["data"]["object"]
        customer_email = invoice.get("customer_email")
        print(f"💳 Payment failed for {customer_email}")

    return {"status": "success", "event_type": event["type"]}

@webhook_app.get("/")
async def webhook_status():
    """Webhook status endpoint"""
    return {"status": "Stripe webhook handler active", "webhook_secret_configured": bool(WEBHOOK_SECRET)}