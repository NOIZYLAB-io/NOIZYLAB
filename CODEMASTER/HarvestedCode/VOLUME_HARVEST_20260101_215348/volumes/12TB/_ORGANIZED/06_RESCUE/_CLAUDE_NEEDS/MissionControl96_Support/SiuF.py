#!/usr/bin/env python3
"""
NOIZYGENIE Standard Palatino 14 Style Template
For consistent text presentation across all tools
"""

def get_palatino_html_style():
    """
    Returns standard Palatino 14pt CSS styling for NOIZYGENIE tools
    """
    return """
    <style>
    * { 
        font-family: Palatino, 'Palatino Linotype', 'Book Antiqua', serif; 
        font-size: 14px; 
    }
    body { 
        background: #f8f8f8; 
        padding: 20px; 
        line-height: 1.6; 
        color: #2c3e50;
    }
    h1 { 
        text-align: center; 
        color: #2c3e50; 
        font-size: 24px; 
        font-weight: bold; 
        margin-bottom: 20px;
    }
    h2 { 
        color: #34495e; 
        font-size: 18px; 
        font-weight: bold; 
        margin-top: 25px;
        margin-bottom: 15px;
    }
    h3 { 
        color: #34495e; 
        font-size: 16px; 
        font-weight: bold; 
        margin-top: 20px;
        margin-bottom: 10px;
    }
    p, div, span { 
        font-size: 14px; 
        line-height: 1.6;
    }
    .stats { 
        text-align: center; 
        font-size: 14px; 
        margin: 20px 0; 
        padding: 15px; 
        background: #fff; 
        border-radius: 8px; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    table { 
        border-collapse: collapse; 
        width: 100%; 
        margin-top: 20px; 
        background: #fff; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    th, td { 
        border: 1px solid #ccc; 
        padding: 8px 12px; 
        text-align: left; 
        font-size: 14px; 
    }
    th { 
        background: #34495e; 
        color: #fff; 
        font-weight: bold; 
        font-size: 14px; 
    }
    tr:nth-child(even) { 
        background: #f9f9f9; 
    }
    tr:hover { 
        background: #e8f4fd; 
    }
    .complete { 
        color: #27ae60; 
        font-weight: bold; 
        font-size: 14px; 
    }
    .partial { 
        color: #f39c12; 
        font-weight: bold; 
        font-size: 14px; 
    }
    .fragment { 
        color: #e74c3c; 
        font-weight: bold; 
        font-size: 14px; 
    }
    .unknown { 
        color: #95a5a6; 
        font-weight: bold; 
        font-size: 14px; 
    }
    .timestamp { 
        text-align: center; 
        color: #7f8c8d; 
        font-size: 14px; 
        margin-top: 20px; 
        font-style: italic;
    }
    .code { 
        font-family: 'Monaco', 'Consolas', 'Courier New', monospace; 
        font-size: 12px; 
        background: #f4f4f4; 
        padding: 2px 6px; 
        border-radius: 3px;
    }
    .highlight { 
        background: #fff3cd; 
        padding: 10px; 
        border-radius: 5px; 
        border-left: 4px solid #f39c12;
        margin: 10px 0;
    }
    .success { 
        background: #d4edda; 
        padding: 10px; 
        border-radius: 5px; 
        border-left: 4px solid #27ae60;
        margin: 10px 0;
    }
    .error { 
        background: #f8d7da; 
        padding: 10px; 
        border-radius: 5px; 
        border-left: 4px solid #e74c3c;
        margin: 10px 0;
    }
    </style>
    """

def create_palatino_html_header(title="NOIZYGENIE"):
    """
    Creates standard HTML header with Palatino 14 styling
    """
    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset='UTF-8'>
    <title>{title}</title>
    {get_palatino_html_style()}
</head>
<body>"""

def create_palatino_html_footer():
    """
    Creates standard HTML footer
    """
    from datetime import datetime
    return f"""
    <div class='timestamp'>
        Generated with NOIZYGENIE Arsenal Tools<br>
        {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    </div>
</body>
</html>"""

def print_palatino_terminal(text, style="normal"):
    """
    Print text in terminal with Palatino-style formatting indicators
    """
    styles = {
        "header": "🎹 ",
        "success": "✅ ",
        "warning": "⚠️ ",
        "error": "❌ ",
        "info": "📊 ",
        "complete": "🎉 ",
        "normal": ""
    }
    
    prefix = styles.get(style, "")
    print(f"{prefix}{text}")

# Example usage functions
def demo_palatino_styling():
    """Demo of Palatino 14 styling"""
    print_palatino_terminal("NOIZYGENIE Palatino 14 Demo", "header")
    print_palatino_terminal("This is standard text", "normal")
    print_palatino_terminal("Success message", "success")
    print_palatino_terminal("Warning message", "warning")
    print_palatino_terminal("Error message", "error")
    print_palatino_terminal("Info message", "info")
    print_palatino_terminal("Complete message", "complete")

if __name__ == "__main__":
    demo_palatino_styling()