#!/usr/bin/env python3
"""
Gemini Mobile API
REST API for mobile apps
"""

import os
from typing import Optional, Dict
from pathlib import Path

try:
    from flask import Flask, request, jsonify
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

    @app.route('/api/v1/solve', methods=['POST'])
    def solve_problem():
        """Solve IT problem"""
        data = request.json
        problem = data.get('problem', '')
        solution = gemini.solve_problem(problem)
        return jsonify({
            'success': True,
            'solution': solution
        })

    @app.route('/api/v1/diagnose', methods=['POST'])
    def diagnose():
        """Auto-diagnose device issue"""
        data = request.json
        device_info = data.get('device', {})
        symptoms = data.get('symptoms', '')

        from gemini_automation import GeminiAutomation
        auto = GeminiAutomation()
        diagnosis = auto.auto_diagnose(device_info, symptoms)

        return jsonify({
            'success': True,
            'diagnosis': diagnosis
        })

    @app.route('/api/v1/generate-code', methods=['POST'])
    def generate_code():
        """Generate code"""
        data = request.json
        description = data.get('description', '')
        language = data.get('language', 'python')

        code = gemini_advanced.code_generation(description, language)
        return jsonify({
            'success': True,
            'code': code
        })

    @app.route('/api/v1/health', methods=['GET'])
    def health():
        """Health check"""
        return jsonify({
            'status': 'healthy',
            'gemini': 'connected'
        })

    def run_api(host='0.0.0.0', port=8080):
        print(f"🚀 Gemini Mobile API on http://{host}:{port}")
        app.run(host=host, port=port)

    if __name__ == '__main__':
        run_api()

else:
    print("Install: pip install flask flask-cors")

