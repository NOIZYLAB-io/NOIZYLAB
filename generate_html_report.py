#!/usr/bin/env python3
"""
HTML REPORT GENERATOR - Create beautiful interactive report
"""

import json
from pathlib import Path
from datetime import datetime

WORKSPACE = Path("/Volumes/4TBSG/KTK 2026 TO SORT")
REPORT_FILE = WORKSPACE / "organization_report.json"
HTML_FILE = WORKSPACE / "library_report.html"

def format_size(bytes_val):
    """Format bytes to human readable"""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_val < 1024.0:
            return f"{bytes_val:.2f} {unit}"
        bytes_val /= 1024.0
    return f"{bytes_val:.2f} PB"

def generate_html_report():
    """Generate beautiful HTML report"""
    
    print("📊 Loading scan data...")
    with open(REPORT_FILE, 'r') as f:
        report = json.load(f)
    
    print("🎨 Generating HTML report...")
    
    # Calculate stats
    total_files = report['total_files']
    total_size = report['total_size']
    categories = report['categories']
    duplicates = report.get('duplicate_groups', 0)
    
    # Generate category rows
    category_rows = []
    for cat_name, cat_info in sorted(categories.items(), 
                                     key=lambda x: x[1]['count'], 
                                     reverse=True):
        count = cat_info['count']
        size = cat_info['size_human']
        percentage = (cat_info['count'] / total_files * 100) if total_files > 0 else 0
        
        category_rows.append(f"""
        <tr>
            <td class="category-name">{cat_name.replace('_', ' ').title()}</td>
            <td class="number">{count:,}</td>
            <td class="size">{size}</td>
            <td>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {percentage}%"></div>
                </div>
                <span class="percentage">{percentage:.1f}%</span>
            </td>
        </tr>
        """)
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Music Library Analysis Report</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            padding: 20px;
            min-height: 100vh;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }}
        
        header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }}
        
        header h1 {{
            font-size: 3em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }}
        
        header p {{
            font-size: 1.2em;
            opacity: 0.9;
        }}
        
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            padding: 40px;
            background: #f8f9fa;
        }}
        
        .stat-card {{
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            text-align: center;
            transition: transform 0.3s ease;
        }}
        
        .stat-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 12px rgba(0,0,0,0.15);
        }}
        
        .stat-value {{
            font-size: 2.5em;
            font-weight: bold;
            color: #667eea;
            margin-bottom: 10px;
        }}
        
        .stat-label {{
            font-size: 1em;
            color: #666;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        .section {{
            padding: 40px;
        }}
        
        .section h2 {{
            font-size: 2em;
            margin-bottom: 30px;
            color: #333;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        
        th {{
            background: #667eea;
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
            text-transform: uppercase;
            font-size: 0.9em;
            letter-spacing: 1px;
        }}
        
        td {{
            padding: 15px;
            border-bottom: 1px solid #eee;
        }}
        
        tr:hover {{
            background: #f8f9fa;
        }}
        
        .category-name {{
            font-weight: 600;
            color: #333;
        }}
        
        .number {{
            color: #667eea;
            font-weight: bold;
            text-align: right;
        }}
        
        .size {{
            color: #764ba2;
            font-weight: bold;
            text-align: right;
        }}
        
        .progress-bar {{
            display: inline-block;
            width: 200px;
            height: 20px;
            background: #eee;
            border-radius: 10px;
            overflow: hidden;
            vertical-align: middle;
        }}
        
        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            transition: width 0.5s ease;
        }}
        
        .percentage {{
            margin-left: 10px;
            color: #666;
            font-weight: 600;
        }}
        
        .alert {{
            background: #fff3cd;
            border: 2px solid #ffc107;
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
        }}
        
        .alert-title {{
            font-size: 1.3em;
            font-weight: bold;
            color: #856404;
            margin-bottom: 10px;
        }}
        
        .alert-text {{
            color: #856404;
            line-height: 1.6;
        }}
        
        footer {{
            background: #2d3748;
            color: white;
            text-align: center;
            padding: 30px;
            font-size: 0.9em;
        }}
        
        .timestamp {{
            opacity: 0.7;
            margin-top: 10px;
        }}
        
        @media (max-width: 768px) {{
            .stats-grid {{
                grid-template-columns: 1fr;
            }}
            
            header h1 {{
                font-size: 2em;
            }}
            
            .progress-bar {{
                width: 100px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🎵 Music Library Analysis</h1>
            <p>Complete scan and organization report</p>
        </header>
        
        <div class="stats-grid">
            <div class="stat-card">
                <div class="stat-value">{total_files:,}</div>
                <div class="stat-label">Total Files</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{format_size(total_size)}</div>
                <div class="stat-label">Total Size</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{len(categories)}</div>
                <div class="stat-label">Categories</div>
            </div>
            <div class="stat-card">
                <div class="stat-value">{duplicates:,}</div>
                <div class="stat-label">Duplicate Groups</div>
            </div>
        </div>
        
        {'<div class="section"><div class="alert"><div class="alert-title">⚠️ Duplicates Detected</div><div class="alert-text">Found ' + f'{duplicates:,}' + ' duplicate file groups. Run duplicate_manager.py to clean up and save space!</div></div></div>' if duplicates > 0 else ''}
        
        <div class="section">
            <h2>📂 Files by Category</h2>
            <table>
                <thead>
                    <tr>
                        <th>Category</th>
                        <th>Files</th>
                        <th>Size</th>
                        <th>Distribution</th>
                    </tr>
                </thead>
                <tbody>
                    {''.join(category_rows)}
                </tbody>
            </table>
        </div>
        
        <footer>
            <p>Generated by 50X FASTER SCANNER & ORGANIZER</p>
            <p class="timestamp">Report generated: {report['timestamp']}</p>
        </footer>
    </div>
</body>
</html>"""
    
    # Write HTML file
    with open(HTML_FILE, 'w') as f:
        f.write(html_content)
    
    print(f"✅ HTML report generated!")
    print(f"📄 Location: {HTML_FILE}")
    print(f"\n💡 Open this file in your web browser to view the interactive report")

def main():
    print("\n" + "🎨"*35)
    print("  HTML REPORT GENERATOR")
    print("🎨"*35 + "\n")
    
    if not REPORT_FILE.exists():
        print("❌ No scan report found!")
        print("Please run fast_organizer.py first.")
        return
    
    generate_html_report()
    
    print(f"\n🌐 To view the report:")
    print(f"   open '{HTML_FILE}'")

if __name__ == "__main__":
    main()

