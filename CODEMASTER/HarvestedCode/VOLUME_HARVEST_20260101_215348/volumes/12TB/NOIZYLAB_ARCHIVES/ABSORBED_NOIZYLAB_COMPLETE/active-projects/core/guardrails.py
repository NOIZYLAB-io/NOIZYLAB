#!/usr/bin/env python3
"""Guardrails - Validation & Safety"""

def validate_spf(spf: str) -> bool:
    """Validate SPF record"""
    return "spf.protection.outlook.com" in spf

def validate_dmarc(dmarc: str) -> bool:
    """Validate DMARC record"""
    return dmarc.startswith("v=DMARC1")

# Add more guardrails...
