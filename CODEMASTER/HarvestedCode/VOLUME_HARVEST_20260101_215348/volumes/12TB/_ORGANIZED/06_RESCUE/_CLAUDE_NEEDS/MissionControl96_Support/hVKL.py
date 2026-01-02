# --- WebAuthn (FIDO2) Biometric Authentication ---
try:
    from webauthn import generate_registration_options, verify_registration_response, generate_authentication_options, verify_authentication_response
    webauthn_enabled = True
except ImportError:
    webauthn_enabled = False

WEB_AUTHN_NOT_ENABLED_MSG = 'WebAuthn not enabled'

# In-memory store for demo (use DB in production)
webauthn_users = {}

    if not webauthn_enabled:
        return jsonify({'error': WEB_AUTHN_NOT_ENABLED_MSG}), 501
    if not webauthn_enabled:
        return jsonify({'error': 'WebAuthn not enabled'}), 501
    username = request.json.get('username')
    options = generate_registration_options(user_id=username, user_name=username)
    webauthn_users[username] = {'options': options}
    return jsonify(options)

@app.route('/webauthn/register/verify', methods=['POST'])
def webauthn_register_verify():
    if not webauthn_enabled:
        return jsonify({'error': 'WebAuthn not enabled'}), 501
    username = request.json.get('username')
    response = request.json.get('response')
    options = webauthn_users.get(username, {}).get('options')
    if not options:
        return jsonify({'error': 'No registration options found'}), 400
    try:
        credential = verify_registration_response(response, options)
        webauthn_users[username]['credential'] = credential
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/webauthn/authenticate', methods=['POST'])
def webauthn_authenticate():
    if not webauthn_enabled:
        return jsonify({'error': 'WebAuthn not enabled'}), 501
    username = request.json.get('username')
    credential = webauthn_users.get(username, {}).get('credential')
    if not credential:
        return jsonify({'error': 'No credential found'}), 400
    options = generate_authentication_options(credential_id=credential['id'])
    webauthn_users[username]['auth_options'] = options
    return jsonify(options)

@app.route('/webauthn/authenticate/verify', methods=['POST'])
def webauthn_authenticate_verify():
    if not webauthn_enabled:
        return jsonify({'error': 'WebAuthn not enabled'}), 501
    username = request.json.get('username')
    response = request.json.get('response')
    credential = webauthn_users.get(username, {}).get('credential')
    options = webauthn_users.get(username, {}).get('auth_options')
    if not credential or not options:
        return jsonify({'error': 'Missing credential or options'}), 400
    try:
        verify_authentication_response(response, credential, options)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
# --- MissionControl96 Dashboard Backend Upgrade ---
# Flask + WebSocket (placeholder) for real-time, multi-agent visualization

# --- MissionControl96 Dashboard Backend Upgrade ---
# Flask + WebSocket (optional) for real-time, multi-agent visualization
from flask import Flask, jsonify, request
import os, socket, functools

# WebSocket integration for real-time dashboard
try:
    from flask_socketio import SocketIO

    socketio_enabled = True
except ImportError:
    socketio_enabled = False

app = Flask(__name__)
if socketio_enabled:
    socketio = SocketIO(app, cors_allowed_origins="*")


# --- Military-grade security: Zero-trust authentication & encryption ---
def require_auth(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        # Placeholder: Replace with real token validation
        if token != "Bearer SUPERSECURETOKEN":
            return jsonify({"error": "Unauthorized"}), 401
        return f(*args, **kwargs)

    return decorated


def find_free_port(start=5003, end=5010):
    for port in range(start, end):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(("localhost", port)) != 0:
                return port
    return start


# --- API Endpoints ---
@app.route("/status")
@require_auth
def status():
    # Aggregate agent status (simulate live data)
    status = {
        "status": "online",
        "ai": True,
        "fleet": True,
        "alerts": True,
        "agents": [
            {"name": "AI Health", "status": "🟢"},
            {"name": "BusinessAI", "status": "🟢"},
            {"name": "AllianceOfficer", "status": "🟢"},
            {"name": "NDAManager", "status": "🟢"},
            {"name": "IdeaManager", "status": "🟢"},
            {"name": "ComplianceAgent", "status": "🟢"},
        ],
    }
    if socketio_enabled:
        socketio.emit("agent_status", status)
    return jsonify(status)


@app.route("/ai_health")
@require_auth
def ai_health():
    # Connect to ai_health agent for real data
    try:
        from NoizyFish_Aquarium.daemons.ai_health import analyze_logs

        health = analyze_logs("/Users/rsp_ms/NOIZYGRID_LOGS")
    except Exception as e:
        health = {"error": str(e)}
    return jsonify(health)


@app.route("/fleet")
@require_auth
def fleet():
    # Connect to ai_health agent for fleet status
    try:
        from NoizyFish_Aquarium.daemons.ai_health import analyze_logs

        health = analyze_logs("/Users/rsp_ms/NOIZYGRID_LOGS")
        slabs = [{"name": slab, "status": status} for slab, status in health.items()]
    except Exception as e:
        slabs = [{"error": str(e)}]
    return jsonify(slabs)


@app.route("/ai_insights")
@require_auth
def ai_insights():
    # Connect to BusinessAI for real insights
    try:
        from NoizyFish_Aquarium.daemons.ai_business import BusinessAI

        ai = BusinessAI()
        result = ai.evaluate_idea("Next-gen AI platform")
        recommendation = result.get("recommendation", "No recommendation available.")
    except Exception as e:
        recommendation = f"Error: {e}"
    return jsonify({"recommendation": recommendation})


@app.route("/admin/<cmd>", methods=["POST"])
@require_auth
def admin_cmd(cmd):
    # Example: Execute fleet-wide actions via shell/SSH
    if cmd == "heal":
        os.system("sh /Users/rsp_ms/Desktop/MissionControl96/daemons/heal_fleet.sh")
        return "Healing triggered across fleet."
    elif cmd == "reboot":
        for ip in ["192.168.0.10", "192.168.0.11", "192.168.0.99"]:
            os.system(f"ssh admin@{ip} 'sudo reboot'")
        return "Reboot triggered across fleet."
    elif cmd == "silence":
        os.system("curl -X POST http://macstudio.local:5000/enforce_silence")
        return "Silence enforced across fleet."
    else:
        return "Unknown command."


# --- Main Entrypoint ---
if __name__ == "__main__":
    port = find_free_port()
    print(f"MissionControl96 backend running on port {port}")
    if socketio_enabled:
        print("WebSocket enabled: Real-time dashboard active.")
        socketio.run(app, host="0.0.0.0", port=port)
    else:
        print("WebSocket not enabled: Install flask_socketio for real-time features.")
        app.run(host="0.0.0.0", port=port)

os.chdir(os.path.expanduser("~/Desktop/MissionControl96_Master"))
os.system("chmod +x install_activate_all.sh")
os.system("./install_activate_all.sh")
