#!/usr/bin/env python3
"""NOIZYLAB API Key Environment Setup for Python"""
import os
import sys

# Load API key
api_key = "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"

# Set environment variables
os.environ['NOIZYLAB_API_KEY'] = api_key
os.environ['ANTHROPIC_API_KEY'] = api_key
os.environ['CLAUDE_API_KEY'] = api_key

print("✅ NOIZYLAB API keys loaded into environment")
