#!/usr/bin/env python3
"""
🧠 GLM-4.7 API Test Client
Test the local GLM-4.7 server
"""

from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:8080/v1",
    api_key="sk-no-key-required",
)

print("🧠 Testing GLM-4.7 Local API...")
print("-" * 50)

response = client.chat.completions.create(
    model="glm-4.7",
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": "Write a Python function to calculate fibonacci numbers efficiently."},
    ],
    temperature=1.0,
    top_p=0.95,
    max_tokens=2048,
)

print(response.choices[0].message.content)
