#!/usr/bin/env python3
import openai
from flask import request, jsonify
import os

# Set your OpenAI API key here or via environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "YOUR_OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def chatgpt_respond(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"[Error] {e}"

# Flask endpoint for ChatGPT chat
@app.route('/chatgpt', methods=['POST'])
def chatgpt():
    data = request.get_json()
    prompt = data.get('prompt', '')
    reply = chatgpt_respond(prompt)
    return jsonify({"reply": reply})
