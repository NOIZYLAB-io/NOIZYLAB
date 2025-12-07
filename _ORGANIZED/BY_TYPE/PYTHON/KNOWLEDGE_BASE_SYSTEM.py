#!/usr/bin/env python3
"""
📚 KNOWLEDGE BASE & SELF-HELP SYSTEM
Common Mac issues with solutions - reduces support load!
Clients solve issues themselves = happy clients, less work for you!
SEO-friendly, searchable, professional!
"""

from flask import Flask, render_template_string, request, jsonify
import json
import os

app = Flask(__name__)

KNOWLEDGE_BASE_ARTICLES = {
    "mac_running_slow": {
        "title": "Mac Running Slow? Quick Fixes!",
        "category": "Performance",
        "difficulty": "Easy",
        "time": "10-15 minutes",
        "views": 0,
        "helpful": 0,
        "steps": [
            "Check Activity Monitor for CPU/Memory hogs",
            "Restart your Mac",
            "Clear Safari/Chrome cache",
            "Remove login items (System Settings → Users & Groups)",
            "Free up disk space (aim for 15% free)",
            "Update macOS to latest version",
            "Reset SMC (Intel Macs)",
            "If still slow → Book a RESCUE session!"
        ],
        "prevention": [
            "Keep 15%+ disk space free",
            "Restart weekly",
            "Update regularly",
            "Don't install random apps"
        ]
    },
    "wifi_not_working": {
        "title": "WiFi Not Connecting? Try These!",
        "category": "Network",
        "difficulty": "Easy",
        "time": "5-10 minutes",
        "views": 0,
        "helpful": 0,
        "steps": [
            "Turn WiFi off, wait 10 sec, turn back on",
            "Restart your router",
            "Forget network and reconnect",
            "Check if other devices work (isolate Mac vs network)",
            "Reset network settings",
            "Update macOS",
            "Try different network to test",
            "Still not working → Book RESCUE!"
        ]
    },
    "email_not_sending": {
        "title": "Email Not Sending from Mail.app",
        "category": "Email",
        "difficulty": "Medium",
        "time": "10-15 minutes",
        "steps": [
            "Check internet connection",
            "Go to Mail → Preferences → Accounts",
            "Take account offline, then back online",
            "Check Outbox for stuck messages",
            "Remove and re-add email account",
            "Check with email provider (Gmail, iCloud, etc.)",
            "Try webmail to confirm server working",
            "Need help → Book RESCUE session!"
        ]
    },
    "app_wont_open": {
        "title": "App Won't Open or Keeps Crashing",
        "category": "Apps",
        "difficulty": "Medium",
        "time": "10 minutes",
        "steps": [
            "Force quit the app (Cmd+Option+Esc)",
            "Restart your Mac",
            "Update the app",
            "Delete app preferences (~/Library/Preferences)",
            "Reinstall the app",
            "Check macOS compatibility",
            "Safe mode test",
            "Still crashing → RESCUE session can fix it!"
        ]
    }
}

KNOWLEDGE_BASE_HOME = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>📚 NoizyLab Knowledge Base</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, Arial, sans-serif;
            background: #0f0f23;
            color: #fff;
            padding: 40px 20px;
        }
        .container { max-width: 1200px; margin: 0 auto; }
        
        .header {
            text-align: center;
            margin-bottom: 50px;
        }
        .header h1 {
            color: #00ff88;
            font-size: 3rem;
            margin-bottom: 15px;
        }
        
        .search-box {
            max-width: 600px;
            margin: 0 auto 40px;
        }
        
        .search-box input {
            width: 100%;
            padding: 20px;
            background: rgba(255,255,255,0.05);
            border: 2px solid #00ff88;
            border-radius: 50px;
            color: #fff;
            font-size: 1.2rem;
            text-align: center;
        }
        
        .articles-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px;
        }
        
        .article-card {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(0,255,136,0.2);
            border-radius: 15px;
            padding: 30px;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .article-card:hover {
            border-color: #00ff88;
            transform: translateY(-5px);
            background: rgba(255,255,255,0.06);
        }
        
        .article-card h3 {
            color: #00ff88;
            font-size: 1.5rem;
            margin-bottom: 15px;
        }
        
        .article-meta {
            display: flex;
            gap: 20px;
            color: #888;
            font-size: 0.9rem;
            margin-top: 15px;
        }
        
        .cta-box {
            background: linear-gradient(135deg, #ff0000 0%, #cc0000 100%);
            border-radius: 20px;
            padding: 40px;
            text-align: center;
            margin-top: 60px;
        }
        
        .cta-box h2 {
            font-size: 2rem;
            margin-bottom: 20px;
        }
        
        .btn {
            display: inline-block;
            padding: 18px 40px;
            background: #00ff88;
            color: #0f0f23;
            text-decoration: none;
            border-radius: 10px;
            font-weight: 600;
            font-size: 1.2rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>📚 NoizyLab Knowledge Base</h1>
            <p style="font-size: 1.2rem; color: #888;">
                Common Mac issues & solutions
            </p>
        </div>
        
        <div class="search-box">
            <input type="text" placeholder="🔍 Search for your issue..." id="searchInput" onkeyup="searchArticles()">
        </div>
        
        <div class="articles-grid" id="articlesGrid">
            {% for article_id, article in articles.items() %}
            <div class="article-card" onclick="viewArticle('{{ article_id }}')">
                <h3>{{ article.title }}</h3>
                <p style="color: #ccc; margin: 15px 0;">
                    {{ article.steps|length }} steps to solve this issue
                </p>
                <div class="article-meta">
                    <span>📂 {{ article.category }}</span>
                    <span>⏱️ {{ article.time }}</span>
                    <span>📊 {{ article.difficulty }}</span>
                </div>
            </div>
            {% endfor %}
        </div>
        
        <div class="cta-box">
            <h2>Can't Find a Solution?</h2>
            <p style="font-size: 1.2rem; margin-bottom: 25px;">
                Book a RESCUE session - I'll fix it remotely!
            </p>
            <a href="http://localhost:8000" class="btn">
                🚨 Book RESCUE Session
            </a>
        </div>
    </div>
    
    <script>
        function viewArticle(id) {
            window.location.href = '/article/' + id;
        }
        
        function searchArticles() {
            const query = document.getElementById('searchInput').value.toLowerCase();
            const cards = document.querySelectorAll('.article-card');
            
            cards.forEach(card => {
                const text = card.textContent.toLowerCase();
                if (text.includes(query)) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def knowledge_base_home():
    """Knowledge base homepage"""
    return render_template_string(KNOWLEDGE_BASE_HOME, articles=KNOWLEDGE_BASE_ARTICLES)

@app.route('/article/<article_id>')
def view_article(article_id):
    """View knowledge base article"""
    
    if article_id not in KNOWLEDGE_BASE_ARTICLES:
        return "Article not found", 404
    
    article = KNOWLEDGE_BASE_ARTICLES[article_id]
    
    # Increment views
    article['views'] += 1
    
    return f"""
<!DOCTYPE html>
<html>
<head>
    <title>{article['title']} - NoizyLab</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, Arial, sans-serif;
            background: #0f0f23;
            color: #fff;
            padding: 40px 20px;
            max-width: 800px;
            margin: 0 auto;
        }}
        h1 {{ color: #00ff88; font-size: 2.5rem; margin-bottom: 30px; }}
        .meta {{
            display: flex;
            gap: 30px;
            color: #888;
            margin-bottom: 40px;
            padding-bottom: 20px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }}
        .steps {{
            background: rgba(255,255,255,0.03);
            border-left: 4px solid #00ff88;
            padding: 30px;
            border-radius: 10px;
            margin: 30px 0;
        }}
        .steps h2 {{ color: #00ff88; margin-bottom: 20px; }}
        .steps ol {{
            line-height: 2.2;
            font-size: 1.1rem;
            margin-left: 25px;
        }}
        .steps li {{
            margin-bottom: 15px;
        }}
        .help-box {{
            background: rgba(255,0,0,0.1);
            border: 2px solid #ff0000;
            padding: 25px;
            border-radius: 12px;
            text-align: center;
            margin-top: 40px;
        }}
        .btn {{
            display: inline-block;
            padding: 15px 35px;
            background: #00ff88;
            color: #0f0f23;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 600;
            margin-top: 15px;
        }}
    </style>
</head>
<body>
    <a href="/" style="color: #00ff88; text-decoration: none; font-size: 1.1rem;">← Back to Knowledge Base</a>
    
    <h1>{article['title']}</h1>
    
    <div class="meta">
        <span>📂 {article['category']}</span>
        <span>⏱️ {article['time']}</span>
        <span>📊 {article['difficulty']}</span>
        <span>👀 {article['views']} views</span>
    </div>
    
    <div class="steps">
        <h2>🔧 Solution Steps:</h2>
        <ol>
            {"".join(f"<li>{step}</li>" for step in article['steps'])}
        </ol>
    </div>
    
    {"<div class='steps'><h2>🛡️ Prevention Tips:</h2><ul>" + "".join(f"<li>{tip}</li>" for tip in article.get('prevention', [])) + "</ul></div>" if article.get('prevention') else ""}
    
    <div class="help-box">
        <h2 style="color: #ff0000; margin-bottom: 15px;">Still Having Issues?</h2>
        <p style="font-size: 1.1rem;">
            I can fix it remotely with a RESCUE session!
        </p>
        <a href="http://localhost:8000" class="btn">
            🚨 Book RESCUE Session
        </a>
        <p style="margin-top: 15px; color: #888;">
            $89+ if fixed • $0 if not • Fair & honest
        </p>
    </div>
    
    <div style="margin-top: 40px; text-align: center;">
        <p style="color: #888;">Was this article helpful?</p>
        <button onclick="markHelpful()" style="background: #00ff88; color: #0f0f23; border: none; padding: 10px 20px; border-radius: 5px; margin: 10px 5px; cursor: pointer;">
            👍 Yes
        </button>
        <button style="background: #666; color: #fff; border: none; padding: 10px 20px; border-radius: 5px; margin: 10px 5px; cursor: pointer;">
            👎 No
        </button>
    </div>
    
    <script>
        function markHelpful() {{
            fetch('/api/article-helpful/{article_id}', {{ method: 'POST' }});
            alert('Thank you for your feedback!');
        }}
    </script>
</body>
</html>
"""

@app.route('/api/article-helpful/<article_id>', methods=['POST'])
def mark_helpful(article_id):
    """Mark article as helpful"""
    if article_id in KNOWLEDGE_BASE_ARTICLES:
        KNOWLEDGE_BASE_ARTICLES[article_id]['helpful'] += 1
    return jsonify({'success': True})

if __name__ == '__main__':
    print("📚 KNOWLEDGE BASE SYSTEM")
    print("=" * 60)
    print()
    print("REDUCES SUPPORT LOAD:")
    print("  ✅ Clients solve issues themselves")
    print("  ✅ 24/7 availability")
    print("  ✅ Searchable solutions")
    print("  ✅ SEO-friendly (Google traffic!)")
    print()
    print(f"ARTICLES: {len(KNOWLEDGE_BASE_ARTICLES)}")
    for article_id, article in KNOWLEDGE_BASE_ARTICLES.items():
        print(f"  • {article['title']}")
    print()
    print("BENEFITS:")
    print("  • Happy clients (solve it themselves!)")
    print("  • Less support tickets")
    print("  • Professional image")
    print("  • Organic traffic from Google")
    print()
    print("🌐 Knowledge Base: http://localhost:8800")
    print()
    
    app.run(host='0.0.0.0', port=8800, debug=True)

