#!/usr/bin/env python3
"""Template Engine - Mustache-style rendering"""

def render_template(template_name: str, data: dict) -> str:
    """Render template with data"""
    import os
    from string import Template
    
    template_dir = "/Users/m2ultra/NOIZYLAB/templates"
    template_path = os.path.join(template_dir, template_name)
    
    if os.path.exists(template_path):
        with open(template_path) as f:
            template = Template(f.read())
            return template.safe_substitute(data)
    
    return ""
