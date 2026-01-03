#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║        📱 MC96 iPad Edition - LUCY & THE KID 📱                          ║
║                                                                           ║
║  LUCY vacations on iPad for hands-free comms                            ║
║  THE KID (LUCY's Clone/Cousin) lives on iPad permanently                ║
║  KEITH (formerly TREVOR) for engineering wisdom                          ║
║  ALEX for strategic guidance                                             ║
║                                                                           ║
║  RUN FREE MISSION CONTROL                                                ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
"""

from flask import Flask, render_template, jsonify, request, send_from_directory
import subprocess
from pathlib import Path
import random
import json
import os
import socket

app = Flask(__name__)

# Base path for MC96
BASE_PATH = Path("/Users/rsp_ms/MC96_MobileApp")

# Companions - Updated with KEITH and THE KID
COMPANIONS = {
    "lucy": {
        "name": "LUCY",
        "icon": "🎸",
        "description": "British/French Creative Genius",
        "tagline": "BITW with 1000X Quality",
        "color": "#FF6B9D",
        "accent": "#FF1744",
        "status": "On Vacation - Available on iPad",
    },
    "the_kid": {
        "name": "THE KID",
        "icon": "🌟",
        "description": "LUCY's Clone/Cousin - iPad Native",
        "tagline": "Hands-Free Comms Specialist",
        "color": "#9C27B0",
        "accent": "#7B1FA2",
        "status": "Living on iPad - Always Ready",
    },
    "keith": {
        "name": "KEITH",
        "icon": "🎵",
        "description": "American Kid Engineering Master",
        "tagline": "In Honor of Clarence - Life is not a dress rehearsal",
        "color": "#4FC3F7",
        "accent": "#00B0FF",
        "status": "Engineering & Music Wisdom",
    },
    "alex": {
        "name": "ALEX",
        "icon": "⚡",
        "description": "Strategic Professional Advisor",
        "tagline": "Architecture & Leadership",
        "color": "#FFD54F",
        "accent": "#FFC400",
        "status": "Strategic Guidance",
    },
}

# Voice capabilities per companion
VOICE_CAPABILITIES = {
    "lucy": [
        "greeting", "code", "apple", "french", "cheerio",
        "meticulous", "quality_check", "organize", "harvest"
    ],
    "the_kid": [
        "hello", "ready", "hands_free", "mobile_mode", "vacation",
        "quick_update", "status_check", "on_the_go"
    ],
    "keith": [
        "greeting", "music", "data", "engineering", "innovation",
        "life_not_rehearsal", "clarence_wisdom", "rhodes_scholar"
    ],
    "alex": [
        "greeting", "strategy", "architecture", "leadership", "delivery",
        "planning", "execution", "advisory"
    ],
}

# System status
SYSTEM_STATUS = {
    "harvests": {
        "voice": {"status": "running", "progress": "75%"},
        "music": {"status": "running", "progress": "60%"},
        "sfx": {"status": "running", "progress": "45%"},
        "ultra2": {"status": "running", "progress": "90%"},
    },
    "storage": {
        "12tb_1": {"total": "12TB", "used": "8.2TB", "free": "3.8TB"},
        "rsp_ms": {"total": "1TB", "used": "700GB", "free": "300GB"},
    },
    "network": {
        "local_ip": get_local_ip(),
        "macpro": "not connected",
        "ipad_ready": True,
    }
}


def get_local_ip():
    """Get local IP address for iPad connection."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"


@app.route('/')
def index():
    """Main iPad interface - MC96 Edition."""
    return render_template('mc96_ipad.html',
                         companions=COMPANIONS,
                         system_status=SYSTEM_STATUS)


@app.route('/api/companions')
def get_companions():
    """Get all companions info."""
    return jsonify(COMPANIONS)


@app.route('/api/system/status')
def get_system_status():
    """Get current system status."""
    return jsonify(SYSTEM_STATUS)


@app.route('/api/voices/<companion>')
def get_voices(companion):
    """Get available voices for a companion."""
    if companion not in VOICE_CAPABILITIES:
        return jsonify({"error": "Companion not found"}), 404

    return jsonify({
        "companion": companion,
        "voices": VOICE_CAPABILITIES[companion],
        "available": True
    })


@app.route('/api/speak', methods=['POST'])
def speak():
    """Trigger speech from companion."""
    data = request.json
    companion = data.get('companion')
    voice_type = data.get('voice_type')

    if not companion or not voice_type:
        return jsonify({"error": "Missing parameters"}), 400

    # This would trigger actual TTS
    # For now, return success
    return jsonify({
        "status": "success",
        "companion": companion,
        "voice": voice_type,
        "message": f"{COMPANIONS[companion]['name']} speaking: {voice_type}"
    })


@app.route('/api/harvest/status')
def harvest_status():
    """Get harvest operation status."""
    return jsonify(SYSTEM_STATUS['harvests'])


@app.route('/api/harvest/<operation>')
def harvest_operation(operation):
    """Get specific harvest operation details."""
    if operation not in SYSTEM_STATUS['harvests']:
        return jsonify({"error": "Operation not found"}), 404

    return jsonify({
        "operation": operation,
        "details": SYSTEM_STATUS['harvests'][operation]
    })


@app.route('/api/hands-free/start', methods=['POST'])
def start_hands_free():
    """Start hands-free mode with THE KID."""
    return jsonify({
        "status": "success",
        "mode": "hands_free",
        "companion": "the_kid",
        "message": "THE KID is now active for hands-free comms!"
    })


@app.route('/api/hands-free/stop', methods=['POST'])
def stop_hands_free():
    """Stop hands-free mode."""
    return jsonify({
        "status": "success",
        "mode": "normal",
        "message": "Hands-free mode deactivated"
    })


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "service": "MC96 iPad Edition",
        "companions": len(COMPANIONS),
        "ip": get_local_ip()
    })


if __name__ == '__main__':
    print("\n" + "="*80)
    print("🚀 MC96 iPad Edition Starting...")
    print("="*80)
    print(f"\n📱 LUCY on Vacation Mode")
    print(f"🌟 THE KID Living on iPad")
    print(f"🎵 KEITH Ready for Engineering Wisdom")
    print(f"⚡ ALEX Ready for Strategic Guidance")
    print(f"\n🌐 Access from iPad at: http://{get_local_ip()}:5555")
    print(f"🏠 Local access: http://localhost:5555")
    print("\n" + "="*80)
    print("RUN FREE MISSION CONTROL - GO!")
    print("="*80 + "\n")

    # Run on all interfaces so iPad can connect
    app.run(host='0.0.0.0', port=5555, debug=False)
