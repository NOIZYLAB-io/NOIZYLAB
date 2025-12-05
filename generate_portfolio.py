#!/usr/bin/env python3
"""
FISH MUSIC INC - PORTFOLIO WEBSITE GENERATOR
Auto-generate professional portfolio website
Created by CB_01 for ROB - GORUNFREE! 🎸🔥
"""

import json
from pathlib import Path
from datetime import datetime

class PortfolioGenerator:
    """Generate professional Fish Music Inc portfolio website"""
    
    def __init__(self):
        self.output_dir = Path('/Users/m2ultra/CB-01-FISHMUSICINC/website/public')
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        self.brand = {
            'name': 'Fish Music Inc',
            'tagline': 'Where Creativity Meets Innovation',
            'motto': 'GORUNFREE! 🎸🔥',
            'email': 'rp@fishmusicinc.com',
            'spotify': 'https://open.spotify.com/user/fishmusicinc',
            'domains': ['fishmusicinc.com', 'noizylab.ca', 'noizyfish.com']
        }
    
    def generate_html(self) -> str:
        """Generate complete HTML portfolio"""
        return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.brand['name']} | Professional Music Production & Sound Design</title>
    <meta name="description" content="Fish Music Inc - Professional music production, sound design, and AI-powered curation. 40 years of creative excellence.">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f8f9fa;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }}
        
        header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 80px 0;
            text-align: center;
        }}
        
        header h1 {{
            font-size: 3.5em;
            margin-bottom: 20px;
            font-weight: 800;
        }}
        
        header .tagline {{
            font-size: 1.5em;
            opacity: 0.95;
            margin-bottom: 10px;
        }}
        
        header .motto {{
            font-size: 1.2em;
            opacity: 0.9;
            font-weight: 600;
        }}
        
        nav {{
            background: white;
            padding: 20px 0;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            position: sticky;
            top: 0;
            z-index: 1000;
        }}
        
        nav ul {{
            list-style: none;
            display: flex;
            justify-content: center;
            gap: 40px;
        }}
        
        nav a {{
            text-decoration: none;
            color: #333;
            font-weight: 600;
            transition: color 0.3s;
        }}
        
        nav a:hover {{
            color: #667eea;
        }}
        
        section {{
            padding: 80px 0;
        }}
        
        h2 {{
            font-size: 2.5em;
            margin-bottom: 40px;
            text-align: center;
            color: #2d3748;
        }}
        
        .services {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }}
        
        .service-card {{
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            transition: transform 0.3s, box-shadow 0.3s;
        }}
        
        .service-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 30px rgba(0,0,0,0.15);
        }}
        
        .service-card h3 {{
            font-size: 1.8em;
            margin-bottom: 15px;
            color: #667eea;
        }}
        
        .clients {{
            background: white;
            padding: 80px 0;
        }}
        
        .client-logos {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 40px;
            text-align: center;
        }}
        
        .client-logo {{
            padding: 30px;
            background: #f8f9fa;
            border-radius: 10px;
            font-size: 1.3em;
            font-weight: 700;
            color: #4a5568;
        }}
        
        .playlists {{
            background: #f8f9fa;
        }}
        
        .playlist-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 30px;
        }}
        
        .playlist-card {{
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            transition: transform 0.3s;
        }}
        
        .playlist-card:hover {{
            transform: translateY(-5px);
        }}
        
        .playlist-card .playlist-content {{
            padding: 30px;
        }}
        
        .playlist-card h3 {{
            font-size: 1.4em;
            margin-bottom: 10px;
            color: #2d3748;
        }}
        
        .playlist-card p {{
            color: #718096;
            margin-bottom: 20px;
        }}
        
        .btn {{
            display: inline-block;
            padding: 12px 30px;
            background: #667eea;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-weight: 600;
            transition: background 0.3s;
        }}
        
        .btn:hover {{
            background: #764ba2;
        }}
        
        .contact {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-align: center;
        }}
        
        .contact h2 {{
            color: white;
        }}
        
        .contact-info {{
            font-size: 1.2em;
            margin: 30px 0;
        }}
        
        .contact a {{
            color: white;
            text-decoration: underline;
        }}
        
        footer {{
            background: #2d3748;
            color: white;
            text-align: center;
            padding: 40px 0;
        }}
        
        footer p {{
            opacity: 0.8;
        }}
        
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 30px;
            margin-top: 50px;
        }}
        
        .stat {{
            text-align: center;
            padding: 30px;
            background: rgba(255,255,255,0.1);
            border-radius: 10px;
        }}
        
        .stat-number {{
            font-size: 3em;
            font-weight: 800;
            display: block;
        }}
        
        .stat-label {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>🎸 {self.brand['name']}</h1>
            <p class="tagline">{self.brand['tagline']}</p>
            <p class="motto">{self.brand['motto']}</p>
            
            <div class="stats">
                <div class="stat">
                    <span class="stat-number">40+</span>
                    <span class="stat-label">Years Experience</span>
                </div>
                <div class="stat">
                    <span class="stat-number">100+</span>
                    <span class="stat-label">Projects</span>
                </div>
                <div class="stat">
                    <span class="stat-number">80TB+</span>
                    <span class="stat-label">Audio Archive</span>
                </div>
            </div>
        </div>
    </header>
    
    <nav>
        <div class="container">
            <ul>
                <li><a href="#services">Services</a></li>
                <li><a href="#clients">Clients</a></li>
                <li><a href="#playlists">Spotify</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </div>
    </nav>
    
    <section id="services">
        <div class="container">
            <h2>Professional Services</h2>
            <div class="services">
                <div class="service-card">
                    <h3>🎵 Music Production</h3>
                    <p>Original compositions, arrangements, and full production services. From concept to final master.</p>
                </div>
                <div class="service-card">
                    <h3>🎬 Sound Design</h3>
                    <p>Professional sound design for film, television, commercials, and interactive media.</p>
                </div>
                <div class="service-card">
                    <h3>🎧 Audio Post-Production</h3>
                    <p>Mixing, mastering, and complete audio post-production for all media formats.</p>
                </div>
                <div class="service-card">
                    <h3>🎼 Music Supervision</h3>
                    <p>Expert music curation and licensing for commercial and creative projects.</p>
                </div>
                <div class="service-card">
                    <h3>🤖 AI-Powered Curation</h3>
                    <p>Advanced playlist optimization and music discovery using AI technology.</p>
                </div>
                <div class="service-card">
                    <h3>📊 Production Music</h3>
                    <p>Extensive production music library for immediate licensing.</p>
                </div>
            </div>
        </div>
    </section>
    
    <section id="clients" class="clients">
        <div class="container">
            <h2>Professional Clients</h2>
            <div class="client-logos">
                <div class="client-logo">FUEL</div>
                <div class="client-logo">McDonald's</div>
                <div class="client-logo">Microsoft</div>
                <div class="client-logo">Deadwood</div>
            </div>
            <p style="text-align: center; margin-top: 40px; font-size: 1.1em; color: #4a5568;">
                40 years of delivering excellence to major brands and creative projects
            </p>
        </div>
    </section>
    
    <section id="playlists" class="playlists">
        <div class="container">
            <h2>Spotify Playlists</h2>
            <p style="text-align: center; margin-bottom: 50px; font-size: 1.2em; color: #4a5568;">
                Professional curation meets innovation
            </p>
            <div class="playlist-grid">
                <div class="playlist-card">
                    <div class="playlist-content">
                        <h3>🕺 SO U LIKE TO DANCE?</h3>
                        <p>BPM-organized dance tracks from slow to fast. Perfect for DJs and progressive energy flow.</p>
                        <a href="https://open.spotify.com/user/fishmusicinc" class="btn" target="_blank">Listen on Spotify</a>
                    </div>
                </div>
                <div class="playlist-card">
                    <div class="playlist-content">
                        <h3>🇨🇦 AI IN CANADA</h3>
                        <p>Curated podcast episodes on Canada's AI strategy, policy, and future innovation.</p>
                        <a href="https://open.spotify.com/playlist/6dqpjdW7fQOjlkY2NOiPbn" class="btn" target="_blank">Listen on Spotify</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    
    <section id="contact" class="contact">
        <div class="container">
            <h2>Let's Create Together</h2>
            <div class="contact-info">
                <p><strong>Email:</strong> <a href="mailto:{self.brand['email']}">{self.brand['email']}</a></p>
                <p><strong>Spotify:</strong> <a href="{self.brand['spotify']}" target="_blank">@fishmusicinc</a></p>
            </div>
            <p style="font-size: 1.3em; margin-top: 40px;">{self.brand['motto']}</p>
        </div>
    </section>
    
    <footer>
        <div class="container">
            <p>&copy; {datetime.now().year} {self.brand['name']}. All Rights Reserved.</p>
            <p style="margin-top: 10px;">Where Creativity Meets Innovation</p>
        </div>
    </footer>
</body>
</html>
'''
    
    def generate(self):
        """Generate and save portfolio website"""
        print("\n🌐 GENERATING FISH MUSIC INC PORTFOLIO WEBSITE")
        print("=" * 70)
        
        html = self.generate_html()
        
        # Save index.html
        output_file = self.output_dir / 'index.html'
        with open(output_file, 'w') as f:
            f.write(html)
        
        print(f"\n✅ Portfolio website generated!")
        print(f"   Location: {output_file}")
        print(f"   Size: {len(html)} bytes")
        print(f"\n📋 To view:")
        print(f"   open {output_file}")
        print(f"\n🚀 Ready to deploy to:")
        for domain in self.brand['domains']:
            print(f"   • {domain}")
        
        print(f"\n{self.brand['motto']}")

def main():
    """Main execution"""
    generator = PortfolioGenerator()
    generator.generate()

if __name__ == '__main__':
    main()

