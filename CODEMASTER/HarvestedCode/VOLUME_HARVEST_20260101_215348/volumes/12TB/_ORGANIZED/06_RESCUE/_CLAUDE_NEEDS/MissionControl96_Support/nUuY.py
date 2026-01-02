import os, jwt, time, stripe, json
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, JSONResponse

# Import webhook app
from stripe_webhook import webhook_app

app = FastAPI(title="Noizy.ai Monetization API")

# Mount Stripe webhook handler
app.mount("/stripe", webhook_app)
STRIPE_SECRET = os.getenv("STRIPE_SECRET", "sk_test_placeholder")
stripe.api_key = STRIPE_SECRET
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "rsp@noizyfish.com")

LICENSE_DIR = Path("licenses")
LICENSE_DIR.mkdir(exist_ok=True)
SECRET_KEY = "noizy_license_secret"

@app.post("/create-checkout-session")
async def create_checkout_session(req: Request):
    data = await req.json()
    plan = data.get("plan", os.getenv("STRIPE_PLAN_PRO"))
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        mode="subscription",
        line_items=[{"price": plan, "quantity": 1}],
        success_url="https://noizy.ai/success",
        cancel_url="https://noizy.ai/cancel"
    )
    return JSONResponse({"url": session.url})

@app.post("/generate-license")
async def generate_license(req: Request):
    data = await req.json()
    email = data.get("email")
    plan = data.get("plan", "pro")
    token = jwt.encode(
        {"email": email, "tier": plan, "iat": int(time.time())},
        SECRET_KEY, algorithm="HS256"
    )
    (LICENSE_DIR / f"{email}.jwt").write_text(token)
    return {"license": token}

@app.get("/api/license")
async def check_license():
    """License endpoint that the website can ping"""
    token_path = "license.jwt"
    if not os.path.exists(token_path):
        return {"valid": False, "reason": "no_license", "upgrade_url": "https://noizy.ai/upgrade"}
    
    try:
        token = open(token_path).read().strip()
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return {"valid": True, "email": data["email"], "tier": data["tier"]}
    except Exception as e:
        return {"valid": False, "reason": str(e), "upgrade_url": "https://noizy.ai/upgrade"}

def verify_license(token_path="license.jwt"):
    """Helper function for Mission Control to check license"""
    if not os.path.exists(token_path):
        return False, "missing"
    token = open(token_path).read().strip()
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return True, data
    except Exception as e:
        return False, str(e)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8766)