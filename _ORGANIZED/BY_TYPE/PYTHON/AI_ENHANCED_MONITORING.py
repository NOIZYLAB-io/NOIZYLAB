#!/usr/bin/env python3
"""AI-Enhanced Monitoring - Uses AI Gateway for intelligent alerts"""
import requests
import json
import os

GATEWAY_URL = os.getenv('AI_GATEWAY_URL', '')
AUTH_TOKEN = os.getenv('INTERNAL_AUTH_TOKEN', '')

def ai_analyze_health(health_data):
    """AI analysis of health data"""
    if not GATEWAY_URL or not AUTH_TOKEN:
        return None
    
    prompt = f"Analyze health data and provide critical recommendations:\n{json.dumps(health_data, indent=2)}"
    
    try:
        r = requests.post(GATEWAY_URL,
            headers={'Authorization': f'Bearer {AUTH_TOKEN}', 'Content-Type': 'application/json'},
            json={'model_choice': 'claude', 'prompt': prompt, 'max_tokens': 1024},
            timeout=30
        )
        return r.json()['result'] if r.ok else None
    except:
        return None

def ai_suggest_fixes(issues):
    """AI suggestions for fixing issues"""
    prompt = f"Provide step-by-step fixes for these issues:\n{json.dumps(issues, indent=2)}"
    
    try:
        r = requests.post(GATEWAY_URL,
            headers={'Authorization': f'Bearer {AUTH_TOKEN}'},
            json={'model_choice': 'claude', 'prompt': prompt},
            timeout=30
        )
        return r.json()['result'] if r.ok else None
    except:
        return None

def run_ai_enhanced_check(domain):
    """Run AI-enhanced domain check"""
    print(f"🤖 AI analyzing {domain}...")
    
    health_data = {'domain': domain, 'timestamp': str(datetime.now())}
    analysis = ai_analyze_health(health_data)
    
    if analysis:
        print(f"✅ AI Analysis:\n{analysis}")
    else:
        print("⚠ AI not available, using standard checks")
    
    return analysis

if __name__ == "__main__":
    from datetime import datetime
    run_ai_enhanced_check('noizylab.ca')

