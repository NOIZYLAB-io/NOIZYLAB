#!/usr/bin/env python3
from re import sub


def escape_markdown(text: str) -> str:
    return sub(r'([\\#*_[\]])', r'\\\1', text)
