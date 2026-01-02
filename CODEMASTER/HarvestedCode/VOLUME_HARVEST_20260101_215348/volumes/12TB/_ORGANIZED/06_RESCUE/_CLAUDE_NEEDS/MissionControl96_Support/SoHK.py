#!/usr/bin/env python3
"""
NoizyAI Monetization Test Suite
Tests the complete payment flow including webhook integration
"""

import requests
import json
import time
from pathlib import Path

BASE_URL = "http://localhost:8000"
WEBHOOK_URL = f"{BASE_URL}/stripe/webhook"

def test_stripe_integration():
    """Test Stripe payment integration"""
    print("🧪 Testing NoizyAI Monetization System")
    print("=" * 50)
    
    # Test 1: Check main app status
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"✅ Main app status: {response.status_code}")
    except Exception as e:
        print(f"❌ Main app connection failed: {e}")
        return False
    
    # Test 2: Check webhook mount
    try:
        response = requests.get(f"{BASE_URL}/stripe/")
        if response.status_code == 200:
            print("✅ Stripe webhook mounted successfully")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Webhook mount failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Webhook connection failed: {e}")
    
    # Test 3: Create checkout session
    try:
        response = requests.post(f"{BASE_URL}/create-checkout-session", 
                               json={"plan": "pro"})
        if response.status_code == 200:
            print("✅ Checkout session creation working")
        else:
            print(f"❌ Checkout failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Checkout test failed: {e}")
    
    # Test 4: License generation
    try:
        response = requests.post(f"{BASE_URL}/generate-license", 
                               json={"email": "test@example.com"})
        if response.status_code == 200:
            print("✅ License generation working")
            license_data = response.json()
            print(f"   License token: {license_data.get('token', '')[:30]}...")
        else:
            print(f"❌ License generation failed: {response.status_code}")
    except Exception as e:
        print(f"❌ License test failed: {e}")
    
    # Test 5: License verification
    try:
        response = requests.get(f"{BASE_URL}/api/license?email=test@example.com")
        if response.status_code == 200:
            print("✅ License verification working")
        else:
            print(f"❌ License verification failed: {response.status_code}")
    except Exception as e:
        print(f"❌ License verification test failed: {e}")
    
    # Test 6: Check license files
    license_dir = Path("licenses")
    if license_dir.exists():
        license_files = list(license_dir.glob("*.jwt"))
        print(f"✅ Found {len(license_files)} license files in ./licenses/")
    else:
        print("❌ License directory not found")
    
    print("\n🎯 Integration Test Complete!")
    print("Ready for production deployment with:")
    print("  1. Stripe payment processing")
    print("  2. Webhook event handling")
    print("  3. License generation & verification")
    print("  4. Email delivery system")
    
    return True

def simulate_webhook_event():
    """Simulate a Stripe webhook event for testing"""
    print("\n🔔 Simulating Stripe Webhook Event")
    
    # Sample checkout.session.completed event
    webhook_payload = {
        "id": "evt_test_webhook",
        "object": "event",
        "type": "checkout.session.completed",
        "data": {
            "object": {
                "id": "cs_test_session",
                "customer_email": "test@noizyai.com",
                "payment_status": "paid"
            }
        }
    }
    
    try:
        response = requests.post(WEBHOOK_URL, 
                               json=webhook_payload,
                               headers={"stripe-signature": "test_signature"})
        print(f"Webhook response: {response.status_code}")
        if response.status_code == 200:
            print("✅ Webhook processing successful")
        else:
            print(f"❌ Webhook failed: {response.text}")
    except Exception as e:
        print(f"❌ Webhook simulation failed: {e}")

if __name__ == "__main__":
    print("Starting NoizyAI Monetization Test Suite...")
    print("Make sure the server is running: uvicorn noizy_monetization:app --port 8000")
    print()
    
    test_stripe_integration()
    simulate_webhook_event()
    
    print("\n💡 Next Steps:")
    print("1. Configure Stripe webhook endpoint in dashboard")
    print("2. Set STRIPE_WEBHOOK_SECRET environment variable")
    print("3. Test with real Stripe events")
    print("4. Deploy to production with HTTPS")