import os
class Config:
    SECRET_KEY = os.getenv("DASHBOARD_SECRET", "test")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET", "test")
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Strict"
    RATELIMIT_DEFAULT = "200/hour;50/minute"
    AUDIT_LOG_PATH = os.getenv("AUDIT_LOG_PATH", "audit.log")
    # ...other config...
