#!/usr/bin/env python3
"""NOIZYLAB AI Gateway Python Client - 10X SPEED"""
import requests
import json
import os
from datetime import datetime

GATEWAY_URL = os.getenv('AI_GATEWAY_URL', 'https://noizylab-ai-gateway.workers.dev')
AUTH_TOKEN = os.getenv('INTERNAL_AUTH_TOKEN', '')

def call_ai(prompt, model='claude', max_tokens=2048, temperature=0.7):
    """Call AI Gateway"""
    response = requests.post(GATEWAY_URL, 
        headers={'Authorization': f'Bearer {AUTH_TOKEN}', 'Content-Type': 'application/json'},
        json={'model_choice': model, 'prompt': prompt, 'max_tokens': max_tokens, 'temperature': temperature},
        timeout=30
    )
    return response.json() if response.ok else None

def analyze_domain(domain_data):
    """Analyze domain health with AI"""
    prompt = f"Analyze domain health and provide recommendations:\n{json.dumps(domain_data, indent=2)}"
    return call_ai(prompt, 'claude')

def generate_email(subject, context):
    """Generate professional email"""
    prompt = f"Write professional email. Subject: {subject}\nContext: {context}"
    return call_ai(prompt, 'claude')

def analyze_alerts(alerts):
    """Analyze monitoring alerts"""
    prompt = f"Analyze alerts and suggest fixes:\n{json.dumps(alerts, indent=2)}"
    return call_ai(prompt, 'claude')

if __name__ == "__main__":
    print("🚀 NOIZYLAB AI Gateway - Ready!")
    result = call_ai("Test: Summarize domain health monitoring in one sentence", 'claude')
    if result:
        print(f"✅ Gateway working: {result.get('result', '')[:100]}...")

