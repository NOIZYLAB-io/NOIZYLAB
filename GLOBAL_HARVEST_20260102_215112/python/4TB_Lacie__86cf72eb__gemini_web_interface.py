#!/usr/bin/env python3
"""
Gemini Web Interface
Web-based interface for Gemini AI
"""

import os
from pathlib import Path
from typing import Optional

try:
    from flask import Flask, render_template_string, request, jsonify, Response
    from flask_cors import CORS
    FLASK_AVAILABLE = True
except ImportError:
    FLASK_AVAILABLE = False

try:
    from gemini_ai import GeminiAI
    from gemini_advanced import GeminiAdvanced
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

if FLASK_AVAILABLE and GEMINI_AVAILABLE:
    app = Flask(__name__)
    CORS(app)

    gemini = GeminiAI()
    gemini_advanced = GeminiAdvanced()

    HTML_TEMPLATE = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>NOIZYLAB Gemini AI</title>
        <style>
            body { font-family: Arial; max-width: 1200px; margin: 0 auto; padding: 20px; }
            .header { background: #1a1a1a; color: white; padding: 20px; border-radius: 10px; }
            .input-area { margin: 20px 0; }
            textarea { width: 100%; height: 100px; padding: 10px; }
            button { padding: 10px 20px; background: #4285f4; color: white; border: none; cursor: pointer; }
            .response { background: #f5f5f5; padding: 20px; border-radius: 10px; margin-top: 20px; }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🤖 NOIZYLAB Gemini AI</h1>
        </div>
        <div class="input-area">
            <textarea id="prompt" placeholder="Enter your problem or question..."></textarea>
            <br><br>
            <button onclick="solve()">Solve Problem</button>
            <button onclick="generate()">Generate Code</button>
            <button onclick="search()">Smart Search</button>
        </div>
        <div id="response" class="response"></div>
        <script>
            async function solve() {
                const prompt = document.getElementById('prompt').value;
                const response = await fetch('/solve', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({problem: prompt})});
                const data = await response.json();
                document.getElementById('response').innerHTML = '<pre>' + data.solution + '</pre>';
            }
            async function generate() {
                const prompt = document.getElementById('prompt').value;
                const response = await fetch('/generate', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({description: prompt})});
                const data = await response.json();
                document.getElementById('response').innerHTML = '<pre>' + data.code + '</pre>';
            }
            async function search() {
                const prompt = document.getElementById('prompt').value;
                const response = await fetch('/search', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({query: prompt})});
                const data = await response.json();
                document.getElementById('response').innerHTML = '<pre>' + data.result + '</pre>';
            }
        </script>
    </body>
    </html>
    '''

    @app.route('/')
    def index():
        return render_template_string(HTML_TEMPLATE)

    @app.route('/solve', methods=['POST'])
    def solve():
        data = request.json
        solution = gemini.solve_problem(data.get('problem', ''))
        return jsonify({'solution': solution})

    @app.route('/generate', methods=['POST'])
    def generate():
        data = request.json
        code = gemini_advanced.code_generation(data.get('description', ''))
        return jsonify({'code': code})

    @app.route('/search', methods=['POST'])
    def search():
        data = request.json
        result = gemini_advanced.smart_search(data.get('query', ''))
        return jsonify({'result': result})

    @app.route('/stream', methods=['POST'])
    def stream():
        data = request.json
        def generate():
            for chunk in gemini_advanced.stream_generate(data.get('prompt', '')):
                yield f"data: {chunk}\\n\\n"
        return Response(generate(), mimetype='text/event-stream')

    def run_server(host='localhost', port=5000, debug=True):
        print(f"🚀 Starting Gemini Web Interface on http://{host}:{port}")
        app.run(host=host, port=port, debug=debug)

    if __name__ == '__main__':
        run_server()

else:
    def run_server():
        print("❌ Flask or Gemini not available")
        print("Install: pip install flask flask-cors google-genai")

