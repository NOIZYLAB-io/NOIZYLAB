#!/usr/bin/env python3
"""
Error Handler - Graceful error handling for all systems
"""

import traceback
import sys
from datetime import datetime
from pathlib import Path

class ErrorHandler:
    """Comprehensive error handler"""

    def __init__(self):
        self.base_dir = Path(__file__).parent
        self.error_log = self.base_dir / "error_logs"
        self.error_log.mkdir(exist_ok=True)

    def handle_error(self, error, context=""):
        """Handle errors gracefully"""
        error_info = {
            "timestamp": datetime.now().isoformat(),
            "error_type": type(error).__name__,
            "error_message": str(error),
            "context": context,
            "traceback": traceback.format_exc()
        }

        # Log error
        log_file = self.error_log / f"error_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        try:
            import json
            with open(log_file, 'w') as f:
                json.dump(error_info, f, indent=2)
        except:
            pass

        # User-friendly message
        print(f"\n⚠️  An error occurred: {error_info['error_message']}")
        print(f"   Error logged to: {log_file.name}")
        print(f"   The system will continue operating...")

        return error_info

    def safe_execute(self, func, *args, **kwargs):
        """Safely execute a function"""
        try:
            return func(*args, **kwargs)
        except Exception as e:
            self.handle_error(e, f"Function: {func.__name__}")
            return None

