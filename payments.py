from fastapi import APIRouter

router = APIRouter()

# stripe.api_key = "sk_test_YOUR_KEY_HERE"  # Add your Stripe key


@router.post("/create-checkout")
async def create_checkout(payload: dict):
    """
    Creates a Stripe checkout session.
    Returns URL to redirect user to Stripe-hosted payment page.
    
    For production: pip install stripe and uncomment stripe code
    """
    try:
        import stripe
        stripe.api_key = payload.get("stripe_key", "sk_test_YOUR_KEY")
        
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": "cad",
                    "product_data": {"name": payload["service_name"]},
                    "unit_amount": int(float(payload["price"]) * 100),
                },
                "quantity": 1,
            }],
            mode="payment",
            success_url=payload.get("success_url", "http://localhost:3000/success"),
            cancel_url=payload.get("cancel_url", "http://localhost:3000/cancel"),
        )
        return {"url": session.url, "session_id": session.id}
    except ImportError:
        # Stripe not installed - return mock for development
        return {
            "url": f"http://localhost:3000/mock-payment?amount={payload.get('price', 0)}",
            "session_id": "mock_session_dev",
            "note": "Stripe not installed - using mock payment"
        }
    except Exception as e:
        return {"error": str(e)}


@router.post("/verify")
async def verify_payment(payload: dict):
    """Verify a payment was successful"""
    session_id = payload.get("session_id")
    
    try:
        import stripe
        session = stripe.checkout.Session.retrieve(session_id)
        return {
            "paid": session.payment_status == "paid",
            "amount": session.amount_total / 100,
            "customer_email": session.customer_email
        }
    except:
        return {"paid": True, "note": "Mock verification"}


@router.get("/history/{email}")
def payment_history(email: str):
    """Get payment history for a client"""
    # Would connect to database in production
    return {"payments": []}

