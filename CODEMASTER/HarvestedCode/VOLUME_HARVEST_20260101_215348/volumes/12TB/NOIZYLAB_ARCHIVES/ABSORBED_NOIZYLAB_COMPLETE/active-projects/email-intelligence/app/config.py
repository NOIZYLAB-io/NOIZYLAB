#!/usr/bin/env python3
"""
Configuration for Email Intelligence App
========================================
"""

import os
from pathlib import Path

# API Keys
API_KEY = os.getenv("GEMINI_API_KEY", os.getenv("API_KEY", ""))
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Database - default to data directory
_app_dir = Path(__file__).parent.parent
DB_PATH = os.getenv("EMAIL_DB_PATH", os.getenv("DB_PATH", str(_app_dir / "data" / "email_intelligence.db")))

# API Configuration
API_URL = os.getenv("API_URL", "http://localhost:8000")
WEBSOCKET_URL = os.getenv("WEBSOCKET_URL", "ws://localhost:8000/ws")

# Slack
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL", "")

# Google Sheets
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID", "")
GOOGLE_SHEETS_JSON = os.getenv("GOOGLE_SHEETS_JSON", "google_sheets.json")

# Processing
BATCH_SIZE = int(os.getenv("BATCH_SIZE", "50"))
ENABLE_ML = os.getenv("ENABLE_ML", "true").lower() == "true"
AI_PROVIDER = os.getenv("AI_PROVIDER", "gemini")

# Ensure database directory exists
db_path_obj = Path(DB_PATH)
if db_path_obj.parent:
    db_path_obj.parent.mkdir(parents=True, exist_ok=True)

