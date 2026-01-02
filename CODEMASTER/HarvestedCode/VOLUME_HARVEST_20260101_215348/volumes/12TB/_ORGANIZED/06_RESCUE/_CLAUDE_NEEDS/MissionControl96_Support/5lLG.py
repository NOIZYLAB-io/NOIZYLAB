from flask import Blueprint, request, jsonify, session
import pyotp, hmac, hashlib, os
from dotenv import load_dotenv
load_dotenv()

bp = Blueprint("auth", __name__, url_prefix="/api")

SECRET = os.getenv("JWT_SECRET", "test")
TOTP_SECRET = pyotp.random_base32()

@bp.post("/login")
def login():
    data = request.json or {}
    user = data.get("user")
    pw = data.get("pass")
    totp = data.get("totp")
    # Basic user/pass check
    if user != os.getenv("ADMIN_USER") or pw != os.getenv("ADMIN_PASS"):
        return jsonify({"ok": False, "error": "Invalid credentials"}), 401
    # TOTP check
    totp_obj = pyotp.TOTP(TOTP_SECRET)
    if not totp or not totp_obj.verify(totp):
        return jsonify({"ok": False, "error": "Invalid TOTP"}), 401
    session["user"] = user
    return jsonify({"ok": True, "msg": "Login successful"})

@bp.post("/sign-config")
def sign_config():
    config = request.json.get("config", "")
    sig = hmac.new(SECRET.encode(), config.encode(), hashlib.sha256).hexdigest()
    return jsonify({"signature": sig})
