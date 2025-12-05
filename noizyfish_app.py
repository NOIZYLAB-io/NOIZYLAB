#!/usr/bin/env python3
"""
🐟 NOIZYFISH.COM - Complete Website & Store
Professional music showcase, store, and business platform
"""

from flask import Flask, render_template_string, request, jsonify, redirect, url_for, session
import json
import os
import sys
from datetime import datetime

# Import email system
sys.path.append('../FishMusic_Email_System')
from ULTIMATE_FISH_MAILER import UltimateFishMailer

app = Flask(__name__)
app.secret_key = 'noizyfish_secret_key_change_in_production'
mailer = UltimateFishMailer()

# HOMEPAGE TEMPLATE
HOMEPAGE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NoizyFish - Original Music & Sound Design</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            background: #000;
            color: #fff;
            line-height: 1.6;
        }
        
        /* Hero Section */
        .hero {
            min-height: 100vh;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 20px;
            position: relative;
            overflow: hidden;
        }
        
        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120"><path fill="%23ffffff" fill-opacity="0.05" d="M0,0 Q300,50 600,20 T1200,40 L1200,120 L0,120 Z"/></svg>') repeat-x bottom;
            opacity: 0.3;
        }
        
        .hero-content {
            position: relative;
            z-index: 1;
            max-width: 800px;
        }
        
        .logo {
            font-size: 80px;
            margin-bottom: 20px;
            animation: float 3s ease-in-out infinite;
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
        }
        
        h1 {
            font-size: 4rem;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        
        .tagline {
            font-size: 1.5rem;
            margin-bottom: 40px;
            opacity: 0.9;
        }
        
        .cta-buttons {
            display: flex;
            gap: 20px;
            justify-content: center;
            flex-wrap: wrap;
        }
        
        .btn {
            padding: 15px 40px;
            font-size: 1.1rem;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            transition: all 0.3s;
            text-decoration: none;
            display: inline-block;
            font-weight: 600;
        }
        
        .btn-primary {
            background: #fff;
            color: #667eea;
        }
        
        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 25px rgba(255,255,255,0.3);
        }
        
        .btn-secondary {
            background: transparent;
            color: #fff;
            border: 2px solid #fff;
        }
        
        .btn-secondary:hover {
            background: #fff;
            color: #667eea;
        }
        
        /* Navigation */
        nav {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background: rgba(0,0,0,0.95);
            padding: 20px 40px;
            z-index: 1000;
            backdrop-filter: blur(10px);
        }
        
        nav ul {
            display: flex;
            justify-content: center;
            gap: 40px;
            list-style: none;
        }
        
        nav a {
            color: #fff;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s;
        }
        
        nav a:hover {
            color: #667eea;
        }
        
        /* Sections */
        section {
            padding: 100px 40px;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        section h2 {
            font-size: 2.5rem;
            margin-bottom: 40px;
            text-align: center;
            background: linear-gradient(135deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        
        /* Music Grid */
        .music-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
            margin-top: 40px;
        }
        
        .track-card {
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            border-radius: 15px;
            overflow: hidden;
            transition: transform 0.3s;
        }
        
        .track-card:hover {
            transform: translateY(-10px);
        }
        
        .track-artwork {
            width: 100%;
            height: 200px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3rem;
        }
        
        .track-info {
            padding: 20px;
        }
        
        .track-title {
            font-size: 1.3rem;
            margin-bottom: 10px;
        }
        
        .track-price {
            color: #667eea;
            font-size: 1.5rem;
            font-weight: bold;
            margin: 10px 0;
        }
        
        /* Contact Form */
        .contact-form {
            max-width: 600px;
            margin: 0 auto;
            background: #1a1a2e;
            padding: 40px;
            border-radius: 15px;
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            margin-bottom: 8px;
            color: #667eea;
        }
        
        input, textarea {
            width: 100%;
            padding: 12px;
            border: 2px solid #667eea;
            border-radius: 8px;
            background: #0f0f1e;
            color: #fff;
            font-size: 1rem;
        }
        
        textarea {
            min-height: 150px;
            resize: vertical;
        }
        
        /* Footer */
        footer {
            background: #0a0a0a;
            padding: 40px;
            text-align: center;
            border-top: 1px solid #667eea;
        }
        
        .social-links {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
        }
        
        .social-links a {
            color: #667eea;
            font-size: 1.5rem;
            transition: transform 0.3s;
            text-decoration: none;
        }
        
        .social-links a:hover {
            transform: scale(1.2);
        }
        
        /* Success Message */
        .success-msg {
            background: #10b981;
            color: white;
            padding: 15px;
            border-radius: 8px;
            margin-bottom: 20px;
            display: none;
        }
        
        .success-msg.show {
            display: block;
            animation: slideIn 0.3s;
        }
        
        @keyframes slideIn {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @media (max-width: 768px) {
            h1 { font-size: 2.5rem; }
            .tagline { font-size: 1.2rem; }
            nav ul { flex-direction: column; gap: 20px; }
        }
    </style>
</head>
<body>
    <nav>
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#music">Music</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
    
    <div class="hero" id="home">
        <div class="hero-content">
            <div class="logo">🐟</div>
            <h1>NoizyFish</h1>
            <p class="tagline">Original Music & Sound Design<br>Creating with Passion, Love & FLOW</p>
            <div class="cta-buttons">
                <a href="#music" class="btn btn-primary">Explore Music</a>
                <a href="#contact" class="btn btn-secondary">Get In Touch</a>
            </div>
        </div>
    </div>
    
    <section id="music">
        <h2>🎵 Latest Releases</h2>
        <div class="music-grid">
            <div class="track-card">
                <div class="track-artwork">🎸</div>
                <div class="track-info">
                    <div class="track-title">Epic Cinematic Theme</div>
                    <p>Orchestral | 3:45</p>
                    <div class="track-price">$9.99</div>
                    <button class="btn btn-primary" style="width: 100%;">Buy Now</button>
                </div>
            </div>
            
            <div class="track-card">
                <div class="track-artwork">🎹</div>
                <div class="track-info">
                    <div class="track-title">Urban Beat</div>
                    <p>Hip Hop | 2:30</p>
                    <div class="track-price">$7.99</div>
                    <button class="btn btn-primary" style="width: 100%;">Buy Now</button>
                </div>
            </div>
            
            <div class="track-card">
                <div class="track-artwork">🎧</div>
                <div class="track-info">
                    <div class="track-title">Ambient Soundscape</div>
                    <p>Electronic | 4:20</p>
                    <div class="track-price">$6.99</div>
                    <button class="btn btn-primary" style="width: 100%;">Buy Now</button>
                </div>
            </div>
        </div>
    </section>
    
    <section id="about">
        <h2>🐟 About NoizyFish</h2>
        <div style="max-width: 800px; margin: 0 auto; text-align: center; font-size: 1.2rem; line-height: 1.8;">
            <p style="margin-bottom: 20px;">
                NoizyFish is the creative studio of Rob, a composer and sound designer with 40 years of experience.
            </p>
            <p style="margin-bottom: 20px;">
                From major commercial work (FUEL, McDonald's, Microsoft) to original compositions, 
                we create music with <strong style="color: #667eea;">passion, love, and FLOW</strong>.
            </p>
            <p style="margin-bottom: 20px;">
                Every note, every sound, every project is crafted with dedication to the art of music creation.
            </p>
            <p style="font-size: 1.5rem; color: #667eea; font-weight: bold;">
                GORUNFREE! 🚀
            </p>
        </div>
    </section>
    
    <section id="contact">
        <h2>📧 Get In Touch</h2>
        
        <div id="successMsg" class="success-msg">
            ✅ Message sent! We'll get back to you soon.
        </div>
        
        <form class="contact-form" id="contactForm">
            <div class="form-group">
                <label for="name">Your Name</label>
                <input type="text" id="name" name="name" required>
            </div>
            
            <div class="form-group">
                <label for="email">Your Email</label>
                <input type="email" id="email" name="email" required>
            </div>
            
            <div class="form-group">
                <label for="subject">Subject</label>
                <input type="text" id="subject" name="subject" required>
            </div>
            
            <div class="form-group">
                <label for="message">Message</label>
                <textarea id="message" name="message" required></textarea>
            </div>
            
            <button type="submit" class="btn btn-primary" style="width: 100%;">
                Send Message
            </button>
        </form>
    </section>
    
    <footer>
        <p>&copy; 2025 NoizyFish. All rights reserved.</p>
        <p style="margin-top: 10px; color: #667eea;">
            Creating music with passion, love & FLOW
        </p>
        <p style="margin-top: 10px;">
            <a href="mailto:rsp@noizyfish.com" style="color: #667eea; text-decoration: none;">
                rsp@noizyfish.com
            </a>
        </p>
        <div class="social-links">
            <a href="#" title="Instagram">📷</a>
            <a href="#" title="YouTube">📺</a>
            <a href="#" title="Spotify">🎵</a>
            <a href="#" title="SoundCloud">☁️</a>
        </div>
    </footer>
    
    <script>
        // Smooth scrolling
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                }
            });
        });
        
        // Contact form submission
        document.getElementById('contactForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const data = Object.fromEntries(formData);
            
            try {
                const response = await fetch('/contact', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(data)
                });
                
                if (response.ok) {
                    document.getElementById('successMsg').classList.add('show');
                    this.reset();
                    setTimeout(() => {
                        document.getElementById('successMsg').classList.remove('show');
                    }, 5000);
                }
            } catch (error) {
                alert('Error sending message. Please try again.');
            }
        });
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    """Homepage"""
    return render_template_string(HOMEPAGE_HTML)

@app.route('/contact', methods=['POST'])
def contact():
    """Handle contact form submissions"""
    try:
        data = request.json
        
        # Send email notification to you
        mailer.send_email_bulletproof(
            to_email="rsp@noizyfish.com",
            subject=f"NoizyFish Contact: {data['subject']}",
            body_text=f"""
New contact form submission from NoizyFish.com

Name: {data['name']}
Email: {data['email']}
Subject: {data['subject']}

Message:
{data['message']}

---
Sent from NoizyFish.com
            """,
            body_html=f"""
<h2>🐟 New Contact Form Submission</h2>

<p><strong>From:</strong> {data['name']} ({data['email']})</p>
<p><strong>Subject:</strong> {data['subject']}</p>

<h3>Message:</h3>
<div style="background: #f4f4f4; padding: 20px; border-radius: 5px;">
    {data['message'].replace(chr(10), '<br>')}
</div>

<hr>
<p style="font-size: 12px; color: #666;">Sent from NoizyFish.com</p>
            """
        )
        
        # Send confirmation to customer
        mailer.send_email_bulletproof(
            to_email=data['email'],
            subject="Thanks for contacting NoizyFish!",
            body_text=f"""
Hi {data['name']}!

Thanks for reaching out! I received your message about "{data['subject']}" 
and I'll get back to you as soon as possible.

GORUNFREE! 🚀

Rob @ NoizyFish
rsp@noizyfish.com
noizyfish.com
            """,
            body_html=f"""
<!DOCTYPE html>
<html>
<body style="font-family: Arial, sans-serif; line-height: 1.6;">
    <div style="max-width: 600px; margin: 0 auto;">
        <h2 style="color: #667eea;">🐟 Thanks for reaching out!</h2>
        
        <p>Hi <strong>{data['name']}</strong>!</p>
        
        <p>Thanks for contacting NoizyFish. I received your message about 
        "<strong>{data['subject']}</strong>" and I'll get back to you as soon as possible.</p>
        
        <p style="color: #667eea; font-size: 18px; font-weight: bold;">GORUNFREE! 🚀</p>
        
        <hr style="border: none; border-top: 1px solid #667eea; margin: 20px 0;">
        
        <p style="font-size: 12px; color: #666;">
            <strong>Rob @ NoizyFish</strong><br>
            rsp@noizyfish.com | noizyfish.com
        </p>
    </div>
</body>
</html>
            """
        )
        
        return jsonify({'success': True})
    
    except Exception as e:
        print(f"Contact form error: {e}")
        return jsonify({'error': str(e)}), 400

@app.route('/api/tracks')
def get_tracks():
    """API endpoint for tracks list"""
    tracks = [
        {
            'id': 1,
            'title': 'Epic Cinematic Theme',
            'genre': 'Orchestral',
            'duration': '3:45',
            'price': 9.99,
            'emoji': '🎸'
        },
        {
            'id': 2,
            'title': 'Urban Beat',
            'genre': 'Hip Hop',
            'duration': '2:30',
            'price': 7.99,
            'emoji': '🎹'
        },
        {
            'id': 3,
            'title': 'Ambient Soundscape',
            'genre': 'Electronic',
            'duration': '4:20',
            'price': 6.99,
            'emoji': '🎧'
        }
    ]
    return jsonify(tracks)

if __name__ == '__main__':
    print("🐟 NOIZYFISH.COM - STARTING...")
    print("=" * 60)
    print("🌐 Website: http://localhost:3000")
    print("📧 Contact form → Auto-sends emails!")
    print("🎵 Music showcase ready")
    print("=" * 60)
    print("GORUNFREE! 🚀")
    print()
    
    app.run(host='0.0.0.0', port=3000, debug=True)
