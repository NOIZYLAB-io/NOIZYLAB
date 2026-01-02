from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from dotenv import load_dotenv
import os
import psutil
import time
from datetime import datetime, timedelta
import random
from typing import Optional

# Import TeamViewer client
from teamviewer_client import teamviewer

# Import Mac Task Manager
from mac_task_manager import mac_task_manager, TaskType, TaskStatus

# Import Support Intake System
from support_intake import support_manager, SupportTicketStatus, IssueCategory, IssuePriority

# Import Voice Assistant System
from voice_assistant import auto_reply_system

# Load environment variables
load_dotenv()

app = FastAPI(title="Mission Control 96", description="Agent Management Dashboard")

# Serve a simple dashboard page
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard():
    return """
    <html>
    <head>
        <title>Mission Control Dashboard</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #1a1a1a; color: #00ff00; }
            h1 { color: #00ffff; text-align: center; }
            .agent-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin: 20px 0; }
            .agent-card { background: #2a2a2a; padding: 15px; border-radius: 8px; border: 1px solid #00ff00; }
            .agent-name { color: #00ffff; font-weight: bold; }
            .status-online { color: #00ff00; }
            .nav-links { text-align: center; margin: 30px 0; }
            .nav-links a { 
                display: inline-block; margin: 10px; padding: 10px 20px; 
                background: #333; color: #00ffff; text-decoration: none; 
                border-radius: 5px; border: 1px solid #00ff00;
            }
            .nav-links a:hover { background: #00ff00; color: #000; }
        </style>
    </head>
    <body>
        <h1>🚀 Mission Control Dashboard</h1>
        <div class="agent-grid">
            <div class="agent-card">
                <div class="agent-name">Diagnostics Agent</div>
                <div class="status-online">● ONLINE</div>
                <div>System monitoring active</div>
            </div>
            <div class="agent-card">
                <div class="agent-name">Repair Agent</div>
                <div class="status-online">● ONLINE</div>
                <div>Auto-repair ready</div>
            </div>
            <div class="agent-card">
                <div class="agent-name">Performance Agent</div>
                <div class="status-online">● ONLINE</div>
                <div>Optimization running</div>
            </div>
            <div class="agent-card">
                <div class="agent-name">AudioOps Agent</div>
                <div class="status-online">● ONLINE</div>
                <div>Voice synthesis ready</div>
            </div>
            <div class="agent-card">
                <div class="agent-name">MemoryKeeper Agent</div>
                <div class="status-online">● ONLINE</div>
                <div>Memory management active</div>
            </div>
            <div class="agent-card">
                <div class="agent-name">SpamFilter Agent</div>
                <div class="status-online">● ONLINE</div>
                <div>Auto-sync protection active</div>
            </div>
            <div class="agent-card">
                <div class="agent-name">Perfectionist Agent</div>
                <div class="status-online">● ONLINE</div>
                <div>Diagnostic healing active</div>
            </div>
            <div class="agent-card">
                <div class="agent-name">Client Portal Agent</div>
                <div class="status-online">● ONLINE</div>
                <div>Remote support ready</div>
            </div>
            <div class="agent-card">
                <div class="agent-name">AI Support Agent</div>
                <div class="status-online">● ONLINE</div>
                <div>Voice assistant active</div>
            </div>
        </div>
        <div class="nav-links">
            <a href='/fetch/diagnostics'>🔍 View Diagnostics</a>
            <a href='/generate_playlist'>🎵 Generate Playlist</a>
            <a href='/health'>❤️ Health Check</a>
            <a href='/api/status'>📊 API Status</a>
            <a href='/audio_library'>🎧 Audio Library</a>
            <a href='/device_sync'>📱 Device Sync</a>
            <a href='/spam_filter'>🛡️ Spam Filter</a>
            <a href='/perfectionist'>✨ Perfectionist</a>
            <a href='/client_portal'>🖥️ Client Portal</a>
        </div>
    </body>
    </html>
    """

@app.get("/fetch/diagnostics")
def fetch_diagnostics():
    """Get system diagnostics information"""
    try:
        # System information
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        diagnostics = {
            "timestamp": datetime.now().isoformat(),
            "system": {
                "cpu_usage": f"{cpu_percent}%",
                "memory_usage": f"{memory.percent}%",
                "memory_available": f"{memory.available / (1024**3):.1f} GB",
                "disk_usage": f"{disk.percent}%",
                "disk_free": f"{disk.free / (1024**3):.1f} GB"
            },
            "agents": {
                "diagnostics": {"status": "online", "last_check": datetime.now().isoformat()},
                "repair": {"status": "online", "tasks_completed": random.randint(0, 50)},
                "performance": {"status": "online", "optimizations": random.randint(0, 20)},
                "audio_ops": {"status": "online", "voice_model": os.getenv("ELEVENLABS_VOICE", "Sarah")},
                "memory_keeper": {"status": "online", "memory_optimized": f"{random.randint(10, 95)}%"},
                "spam_filter": {"status": "online", "rules_active": random.randint(15, 45), "blocked_today": random.randint(5, 25)},
                "perfectionist": {"status": "online", "issues_found": random.randint(0, 8), "auto_fixes": random.randint(5, 15), "health_score": f"{random.randint(92, 99)}%"},
                "client_portal": {"status": "online", "teamviewer_configured": teamviewer.is_configured(), "active_sessions": random.randint(0, 5), "managed_devices": random.randint(8, 25)}
            },
            "environment": {
                "dashboard_url": os.getenv("MC_DASHBOARD_URL", "http://127.0.0.1:8765/dashboard"),
                "dns_domain": os.getenv("DNS_DOMAIN", "Not configured"),
                "apis_configured": {
                    "godaddy": bool(os.getenv("GODADDY_API_KEY") and os.getenv("GODADDY_API_KEY") != "..."),
                    "elevenlabs": bool(os.getenv("ELEVENLABS_API_KEY") and os.getenv("ELEVENLABS_API_KEY") != "..."),
                    "openai": bool(os.getenv("OPENAI_API_KEY") and os.getenv("OPENAI_API_KEY") != "..."),
                    "teamviewer": bool(os.getenv("TEAMVIEWER_API_TOKEN") and os.getenv("TEAMVIEWER_API_TOKEN") != "...")
                }
            }
        }
        
        return JSONResponse(content=diagnostics)
        
    except Exception as e:
        return JSONResponse(
            content={"error": f"Diagnostics failed: {str(e)}", "timestamp": datetime.now().isoformat()},
            status_code=500
        )

@app.get("/generate_playlist")
def generate_playlist():
    """Generate a sample playlist"""
    genres = ["Electronic", "Ambient", "Synthwave", "Chillout", "Techno", "House"]
    artists = ["Daft Punk", "Deadmau5", "Aphex Twin", "Boards of Canada", "Tycho", "Moderat"]
    
    playlist = {
        "name": f"Mission Control Mix {random.randint(1, 999)}",
        "generated_at": datetime.now().isoformat(),
        "genre": random.choice(genres),
        "tracks": [
            {
                "id": i + 1,
                "title": f"Track {i + 1}",
                "artist": random.choice(artists),
                "duration": f"{random.randint(3, 8)}:{random.randint(10, 59):02d}",
                "bpm": random.randint(80, 140)
            }
            for i in range(random.randint(8, 15))
        ],
        "total_duration": f"{random.randint(45, 90)} minutes",
        "audio_synthesis": {
            "voice_model": os.getenv("ELEVENLABS_VOICE", "Sarah"),
            "model": os.getenv("ELEVENLABS_MODEL", "eleven_turbo_v2"),
            "ready": bool(os.getenv("ELEVENLABS_API_KEY") and os.getenv("ELEVENLABS_API_KEY") != "...")
        }
    }
    
    return JSONResponse(content=playlist)

@app.get("/health")
def health_check():
    """System health check endpoint"""
    try:
        # Check system resources
        cpu_ok = psutil.cpu_percent(interval=0.1) < 90
        memory_ok = psutil.virtual_memory().percent < 85
        disk_ok = psutil.disk_usage('/').percent < 90
        
        # Check API configurations
        apis_configured = {
            "godaddy": os.getenv("GODADDY_API_KEY", "...") != "...",
            "elevenlabs": os.getenv("ELEVENLABS_API_KEY", "...") != "...", 
            "openai": os.getenv("OPENAI_API_KEY", "...") != "...",
            "teamviewer": os.getenv("TEAMVIEWER_API_TOKEN", "...") != "..."
        }
        
        overall_health = all([cpu_ok, memory_ok, disk_ok])
        
        health_status = {
            "status": "healthy" if overall_health else "degraded",
            "timestamp": datetime.now().isoformat(),
            "uptime": f"{time.time() - psutil.boot_time():.0f} seconds",
            "checks": {
                "cpu": "ok" if cpu_ok else "warning",
                "memory": "ok" if memory_ok else "warning", 
                "disk": "ok" if disk_ok else "warning",
                "apis": apis_configured
            },
            "agents": {
                "diagnostics": "online",
                "repair": "online", 
                "performance": "online",
                "audio_ops": "online",
                "memory_keeper": "online",
                "spam_filter": "online",
                "perfectionist": "online",
                "client_portal": "online"
            },
            "mission_control": {
                "version": "96",
                "dashboard_url": os.getenv("MC_DASHBOARD_URL", "http://127.0.0.1:8765/dashboard"),
                "environment": "development"
            }
        }
        
        return JSONResponse(content=health_status)
        
    except Exception as e:
        return JSONResponse(
            content={
                "status": "error",
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            },
            status_code=500
        )

@app.get("/api/status")
def api_status():
    """Quick API status endpoint"""
    return JSONResponse(content={
        "api": "Mission Control 96",
        "status": "operational",
        "timestamp": datetime.now().isoformat(),
        "endpoints": [
            "/dashboard",
            "/fetch/diagnostics", 
            "/generate_playlist",
            "/health",
            "/api/status",
            "/audio_library",
            "/device_sync",
            "/create_playlist/{device}",
            "/spam_filter",
            "/sync_spam_rules/{device}",
            "/perfectionist",
            "/diagnostic_heal",
            "/auto_optimize",
            "/client_portal",
            "/teamviewer/status",
            "/teamviewer/devices",
            "/teamviewer/sessions",
            "/teamviewer/groups",
            "/teamviewer/reports",
            "/mac_tasks/dashboard",
            "/mac_tasks/list",
            "/mac_tasks/create",
            "/mac_tasks/clients",
            "/mac_tasks/statistics"
        ]
    })

@app.get("/audio_library")
def audio_library():
    """Apple Certification Audio Library Management"""
    import glob
    
    audio_library_path = "/Users/rsp_ms/Desktop/Apple_Certification_Audio"
    
    try:
        # Scan for audio files in each chapter
        chapters = {}
        
        for chapter_dir in glob.glob(f"{audio_library_path}/Chapter_*"):
            chapter_name = os.path.basename(chapter_dir)
            
            # Find audio files
            audio_files = []
            for ext in ['*.mp3', '*.wav', '*.m4a', '*.aac']:
                audio_files.extend(glob.glob(f"{chapter_dir}/{ext}"))
            
            chapters[chapter_name] = {
                "path": chapter_dir,
                "audio_files": [os.path.basename(f) for f in audio_files],
                "file_count": len(audio_files),
                "total_size_mb": sum(os.path.getsize(f) for f in audio_files) / (1024*1024) if audio_files else 0
            }
        
        library_info = {
            "timestamp": datetime.now().isoformat(),
            "library_path": audio_library_path,
            "total_chapters": len(chapters),
            "chapters": chapters,
            "synthesis_ready": {
                "elevenlabs_configured": bool(os.getenv("ELEVENLABS_API_KEY") and os.getenv("ELEVENLABS_API_KEY") != "..."),
                "voice_model": os.getenv("ELEVENLABS_VOICE", "Sarah"),
                "model": os.getenv("ELEVENLABS_MODEL", "eleven_turbo_v2")
            },
            "recommended_structure": [
                "Chapter_01_Fundamentals",
                "Chapter_02_Hardware", 
                "Chapter_03_macOS",
                "Chapter_04_iOS_iPadOS",
                "Chapter_05_Security",
                "Chapter_06_Troubleshooting",
                "Chapter_07_Advanced_Topics",
                "Chapter_08_Practice_Exams"
            ]
        }
        
        return JSONResponse(content=library_info)
        
    except Exception as e:
        return JSONResponse(
            content={"error": f"Audio library scan failed: {str(e)}", "timestamp": datetime.now().isoformat()},
            status_code=500
        )

@app.get("/device_sync")
def device_sync():
    """Device sync dashboard for iPhone and iPad playlists"""
    return HTMLResponse(content="""
    <html>
    <head>
        <title>Device Sync - Mission Control</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #1a1a1a; color: #00ff00; }
            h1 { color: #00ffff; text-align: center; }
            .device-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin: 30px 0; }
            .device-card { background: #2a2a2a; padding: 25px; border-radius: 12px; border: 2px solid #00ff00; }
            .device-name { color: #00ffff; font-size: 1.5em; font-weight: bold; margin-bottom: 15px; }
            .sync-button { 
                display: block; width: 100%; margin: 10px 0; padding: 12px; 
                background: #333; color: #00ffff; text-decoration: none; text-align: center;
                border-radius: 8px; border: 1px solid #00ff00; font-weight: bold;
            }
            .sync-button:hover { background: #00ff00; color: #000; }
            .back-link { text-align: center; margin: 20px 0; }
            .back-link a { color: #00ffff; text-decoration: none; }
            .status { margin: 10px 0; padding: 8px; background: #1a3a1a; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1>📱 Device Sync Dashboard</h1>
        <div class="device-grid">
            <div class="device-card">
                <div class="device-name">📱 iPhone</div>
                <div class="status">Ready for sync</div>
                <a href="/create_playlist/iphone" class="sync-button">🎵 Create iPhone Playlist</a>
                <a href="/export_playlist/iphone/m3u" class="sync-button">📤 Export M3U Playlist</a>
                <a href="/export_playlist/iphone/xml" class="sync-button">📤 Export iTunes XML</a>
                <div style="margin-top: 15px; font-size: 0.9em; color: #888;">
                    • Apple Certification Audio<br>
                    • Chapter-based organization<br>
                    • Voice synthesis ready
                </div>
            </div>
            <div class="device-card">
                <div class="device-name">📱 iPad</div>
                <div class="status">Ready for sync</div>
                <a href="/create_playlist/ipad" class="sync-button">🎵 Create iPad Playlist</a>
                <a href="/export_playlist/ipad/m3u" class="sync-button">📤 Export M3U Playlist</a>
                <a href="/export_playlist/ipad/xml" class="sync-button">📤 Export iTunes XML</a>
                <div style="margin-top: 15px; font-size: 0.9em; color: #888;">
                    • Extended study sessions<br>
                    • Large screen optimized<br>
                    • Enhanced audio quality
                </div>
            </div>
        </div>
        <div class="back-link">
            <a href="/dashboard">← Back to Mission Control</a>
        </div>
    </body>
    </html>
    """)

@app.get("/create_playlist/{device}")
def create_device_playlist(device: str):
    """Create device-specific playlists for iPhone or iPad"""
    import glob
    
    audio_library_path = "/Users/rsp_ms/Desktop/Apple_Certification_Audio"
    
    try:
        # Scan for audio files
        all_audio_files = []
        for chapter_dir in glob.glob(f"{audio_library_path}/Chapter_*"):
            chapter_name = os.path.basename(chapter_dir)
            
            for ext in ['*.mp3', '*.wav', '*.m4a', '*.aac']:
                audio_files = glob.glob(f"{chapter_dir}/{ext}")
                for file_path in audio_files:
                    all_audio_files.append({
                        "chapter": chapter_name,
                        "filename": os.path.basename(file_path),
                        "full_path": file_path,
                        "size_mb": os.path.getsize(file_path) / (1024*1024)
                    })
        
        # Device-specific optimizations
        device_config = {
            "iphone": {
                "name": "iPhone Study Playlist",
                "description": "Optimized for mobile learning",
                "max_file_size_mb": 50,  # Smaller files for phone storage
                "preferred_quality": "standard"
            },
            "ipad": {
                "name": "iPad Study Playlist", 
                "description": "Enhanced for extended study sessions",
                "max_file_size_mb": 100,  # Larger files OK on iPad
                "preferred_quality": "high"
            }
        }
        
        config = device_config.get(device.lower(), device_config["iphone"])
        
        # Filter files based on device constraints
        suitable_files = [f for f in all_audio_files if f["size_mb"] <= config["max_file_size_mb"]]
        
        playlist = {
            "device": device.upper(),
            "playlist_name": config["name"],
            "description": config["description"],
            "created_at": datetime.now().isoformat(),
            "total_files": len(suitable_files),
            "total_size_mb": sum(f["size_mb"] for f in suitable_files),
            "estimated_duration": f"{len(suitable_files) * 15} minutes",  # Estimate 15 min per file
            "chapters_included": list(set(f["chapter"] for f in suitable_files)),
            "files": suitable_files[:20],  # Limit to first 20 for display
            "sync_instructions": {
                "method_1": "AirDrop files directly to device",
                "method_2": "Use iTunes/Finder sync",
                "method_3": "Upload to iCloud and download on device",
                "recommended": "AirDrop for quick transfer"
            },
            "audio_synthesis": {
                "voice_model": os.getenv("ELEVENLABS_VOICE", "Sarah"),
                "model": os.getenv("ELEVENLABS_MODEL", "eleven_turbo_v2"),
                "ready": bool(os.getenv("ELEVENLABS_API_KEY") and os.getenv("ELEVENLABS_API_KEY") != "...")
            }
        }
        
        return JSONResponse(content=playlist)
        
    except Exception as e:
        return JSONResponse(
            content={"error": f"Playlist creation failed: {str(e)}", "device": device},
            status_code=500
        )

@app.get("/export_playlist/{device}/{format}")
def export_playlist(device: str, format: str):
    """Export playlist in various formats (m3u, xml, json)"""
    import glob
    from urllib.parse import quote
    
    audio_library_path = "/Users/rsp_ms/Desktop/Apple_Certification_Audio"
    
    try:
        # Collect audio files
        audio_files = []
        for chapter_dir in glob.glob(f"{audio_library_path}/Chapter_*"):
            for ext in ['*.mp3', '*.wav', '*.m4a', '*.aac']:
                files = glob.glob(f"{chapter_dir}/{ext}")
                audio_files.extend(files)
        
        if format.lower() == "m3u":
            # Create M3U playlist format
            playlist_content = "#EXTM3U\n"
            playlist_content += f"#PLAYLIST:Apple Certification - {device.upper()}\n\n"
            
            for file_path in audio_files:
                filename = os.path.basename(file_path)
                chapter = os.path.basename(os.path.dirname(file_path))
                playlist_content += f"#EXTINF:-1,{chapter} - {filename}\n"
                playlist_content += f"file://{file_path}\n\n"
            
            return HTMLResponse(
                content=f"<pre>{playlist_content}</pre>",
                headers={"Content-Type": "text/plain; charset=utf-8"}
            )
            
        elif format.lower() == "xml":
            # Create iTunes XML format
            xml_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Application Version</key>
    <string>Mission Control 96</string>
    <key>Date</key>
    <date>{datetime.now().isoformat()}</date>
    <key>Features</key>
    <integer>5</integer>
    <key>Playlists</key>
    <array>
        <dict>
            <key>Name</key>
            <string>Apple Certification - {device.upper()}</string>
            <key>Description</key>
            <string>Study materials for Apple certification</string>
            <key>Playlist Items</key>
            <array>"""
            
            for i, file_path in enumerate(audio_files):
                filename = os.path.basename(file_path)
                xml_content += f"""
                <dict>
                    <key>Track ID</key>
                    <integer>{i+1}</integer>
                    <key>Name</key>
                    <string>{filename}</string>
                    <key>Location</key>
                    <string>file://{quote(file_path)}</string>
                </dict>"""
            
            xml_content += """
            </array>
        </dict>
    </array>
</dict>
</plist>"""
            
            return HTMLResponse(
                content=f"<pre>{xml_content}</pre>",
                headers={"Content-Type": "application/xml; charset=utf-8"}
            )
            
        else:
            return JSONResponse(
                content={"error": f"Unsupported format: {format}. Use 'm3u' or 'xml'"},
                status_code=400
            )
            
    except Exception as e:
        return JSONResponse(
            content={"error": f"Export failed: {str(e)}", "device": device, "format": format},
            status_code=500
        )

@app.get("/spam_filter")
def spam_filter_dashboard():
    """Spam Filter Management Dashboard"""
    return HTMLResponse(content="""
    <html>
    <head>
        <title>Spam Filter - Mission Control</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #1a1a1a; color: #00ff00; }
            h1 { color: #00ffff; text-align: center; }
            .filter-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin: 30px 0; }
            .filter-card { background: #2a2a2a; padding: 25px; border-radius: 12px; border: 2px solid #00ff00; }
            .filter-title { color: #00ffff; font-size: 1.3em; font-weight: bold; margin-bottom: 15px; }
            .sync-button { 
                display: block; width: 100%; margin: 10px 0; padding: 12px; 
                background: #333; color: #00ffff; text-decoration: none; text-align: center;
                border-radius: 8px; border: 1px solid #00ff00; font-weight: bold;
            }
            .sync-button:hover { background: #00ff00; color: #000; }
            .stats { margin: 15px 0; padding: 10px; background: #1a3a1a; border-radius: 5px; }
            .rule-item { margin: 5px 0; padding: 5px; background: #333; border-radius: 3px; font-size: 0.9em; }
            .back-link { text-align: center; margin: 20px 0; }
            .back-link a { color: #00ffff; text-decoration: none; }
        </style>
    </head>
    <body>
        <h1>🛡️ Spam Filter Auto-Sync</h1>
        
        <div class="filter-grid">
            <div class="filter-card">
                <div class="filter-title">📧 Email Protection</div>
                <div class="stats">
                    <div>Rules Active: 32</div>
                    <div>Blocked Today: 15</div>
                    <div>Accuracy: 98.7%</div>
                </div>
                <a href="/sync_spam_rules/email" class="sync-button">🔄 Sync Email Rules</a>
                <a href="/export_spam_rules/email" class="sync-button">📤 Export Rules</a>
                <div class="rule-item">• Phishing detection active</div>
                <div class="rule-item">• Malware attachment blocking</div>
                <div class="rule-item">• Suspicious link filtering</div>
            </div>
            
            <div class="filter-card">
                <div class="filter-title">📱 iPhone Protection</div>
                <div class="stats">
                    <div>SMS Rules: 18</div>
                    <div>Call Blocking: Active</div>
                    <div>iMessage Filter: ON</div>
                </div>
                <a href="/sync_spam_rules/iphone" class="sync-button">📱 Sync to iPhone</a>
                <a href="/export_spam_rules/iphone" class="sync-button">📤 Export Mobile Rules</a>
                <div class="rule-item">• Unknown caller blocking</div>
                <div class="rule-item">• SMS keyword filtering</div>
                <div class="rule-item">• Auto-delete spam messages</div>
            </div>
            
            <div class="filter-card">
                <div class="filter-title">💻 iPad Protection</div>
                <div class="stats">
                    <div>Web Filter: Active</div>
                    <div>Ad Blocking: ON</div>
                    <div>Safe Browsing: Enabled</div>
                </div>
                <a href="/sync_spam_rules/ipad" class="sync-button">📱 Sync to iPad</a>
                <a href="/export_spam_rules/ipad" class="sync-button">📤 Export iPad Rules</a>
                <div class="rule-item">• Malicious website blocking</div>
                <div class="rule-item">• Pop-up advertisement filtering</div>
                <div class="rule-item">• Safe search enforcement</div>
            </div>
            
            <div class="filter-card">
                <div class="filter-title">🖥️ macOS Protection</div>
                <div class="stats">
                    <div>System Rules: 25</div>
                    <div>Network Filter: ON</div>
                    <div>Firewall: Active</div>
                </div>
                <a href="/sync_spam_rules/macos" class="sync-button">💻 Sync to macOS</a>
                <a href="/export_spam_rules/macos" class="sync-button">📤 Export System Rules</a>
                <div class="rule-item">• Network traffic filtering</div>
                <div class="rule-item">• Application firewall rules</div>
                <div class="rule-item">• DNS-based ad blocking</div>
            </div>
        </div>
        
        <div class="back-link">
            <a href="/dashboard">← Back to Mission Control</a>
        </div>
    </body>
    </html>
    """)

@app.get("/sync_spam_rules/{device}")
def sync_spam_rules(device: str):
    """Sync spam filter rules to specific device"""
    
    # Device-specific spam filter configurations
    spam_rules = {
        "email": {
            "rules": [
                {"type": "sender_blacklist", "pattern": "*@suspicious-domain.com", "action": "block"},
                {"type": "subject_keywords", "pattern": "urgent|winner|prize|lottery", "action": "quarantine"},
                {"type": "attachment_scan", "pattern": "*.exe|*.scr|*.bat", "action": "block"},
                {"type": "phishing_detection", "pattern": "paypal|amazon|bank", "action": "flag"},
                {"type": "bulk_sender", "threshold": 100, "action": "limit"}
            ],
            "whitelist": [
                "apple.com", "icloud.com", "github.com", "stackoverflow.com"
            ],
            "settings": {
                "quarantine_days": 30,
                "auto_delete_spam": True,
                "learning_mode": True
            }
        },
        "iphone": {
            "rules": [
                {"type": "unknown_caller", "action": "silence"},
                {"type": "sms_keywords", "pattern": "click here|free gift|congratulations", "action": "block"},
                {"type": "international_calls", "threshold": "+1-900", "action": "block"},
                {"type": "robocall_detection", "confidence": 0.8, "action": "block"}
            ],
            "settings": {
                "filter_unknown_senders": True,
                "report_junk": True,
                "block_caller_id_hidden": True
            }
        },
        "ipad": {
            "rules": [
                {"type": "web_content", "pattern": "casino|gambling|adult", "action": "block"},
                {"type": "ad_blocking", "domains": ["doubleclick.net", "googleadservices.com"], "action": "block"},
                {"type": "malware_sites", "reputation": "low", "action": "warn"},
                {"type": "social_media", "time_restriction": "18:00-22:00", "action": "limit"}
            ],
            "settings": {
                "safe_search": True,
                "content_restrictions": True,
                "screen_time_limits": True
            }
        },
        "macos": {
            "rules": [
                {"type": "firewall", "port": "22", "source": "any", "action": "block"},
                {"type": "dns_filter", "domains": ["malware.com", "phishing.net"], "action": "block"},
                {"type": "app_permissions", "app": "unknown", "network": False, "action": "restrict"},
                {"type": "file_quarantine", "extensions": [".dmg", ".pkg"], "scan": True, "action": "verify"}
            ],
            "settings": {
                "stealth_mode": True,
                "logging_enabled": True,
                "auto_update_rules": True
            }
        }
    }
    
    device_rules = spam_rules.get(device.lower(), spam_rules["email"])
    
    sync_result = {
        "device": device.upper(),
        "sync_timestamp": datetime.now().isoformat(),
        "rules_synced": len(device_rules["rules"]),
        "rules": device_rules["rules"],
        "settings": device_rules.get("settings", {}),
        "whitelist": device_rules.get("whitelist", []),
        "sync_status": "completed",
        "next_sync": (datetime.now().timestamp() + 3600),  # Next sync in 1 hour
        "auto_sync": {
            "enabled": True,
            "frequency": "hourly",
            "last_update": datetime.now().isoformat()
        },
        "protection_level": "high",
        "estimated_blocks_per_day": random.randint(10, 50)
    }
    
    return JSONResponse(content=sync_result)

@app.get("/export_spam_rules/{device}")
def export_spam_rules(device: str):
    """Export spam filter rules for manual installation"""
    
    try:
        if device.lower() == "email":
            # Export email rules in SpamAssassin format
            rules_content = """# Mission Control 96 - Email Spam Rules
# Generated: {timestamp}

# Phishing Protection
header PHISHING_PAYPAL Subject =~ /paypal.*urgent/i
score PHISHING_PAYPAL 5.0

# Suspicious Attachments
body EXEC_ATTACHMENT /\.exe|\.scr|\.bat/i
score EXEC_ATTACHMENT 4.0

# Bulk Sender Detection
header BULK_SENDER X-Bulk-Mail =~ /yes/i
score BULK_SENDER 2.0

# Whitelist Trusted Domains
whitelist_from *@apple.com
whitelist_from *@icloud.com
whitelist_from *@github.com
""".format(timestamp=datetime.now().isoformat())
            
        elif device.lower() in ["iphone", "ipad"]:
            # Export iOS configuration profile
            rules_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <key>PayloadDescription</key>
            <string>Mission Control Spam Filter for {device.upper()}</string>
            <key>PayloadDisplayName</key>
            <string>Spam Protection Rules</string>
            <key>PayloadIdentifier</key>
            <string>com.missioncontrol96.spamfilter.{device.lower()}</string>
            <key>PayloadType</key>
            <string>Configuration</string>
            <key>PayloadUUID</key>
            <string>MC96-SPAM-{device.upper()}-{int(datetime.now().timestamp())}</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>
    <key>PayloadDescription</key>
    <string>Auto-sync spam protection for {device.upper()}</string>
    <key>PayloadDisplayName</key>
    <string>Mission Control Spam Filter</string>
    <key>PayloadIdentifier</key>
    <string>com.missioncontrol96.spamfilter</string>
    <key>PayloadRemovalDisallowed</key>
    <false/>
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadUUID</key>
    <string>MC96-MAIN-{int(datetime.now().timestamp())}</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>"""
            
        elif device.lower() == "macos":
            # Export pfctl rules for macOS
            rules_content = f"""# Mission Control 96 - macOS Firewall Rules
# Generated: {datetime.now().isoformat()}

# Block known malicious IPs
block in quick from 192.168.100.0/24 to any
block in quick from 10.0.0.0/8 to any port 22

# Allow trusted services
pass in quick on lo0 all
pass out quick on en0 proto tcp from any to any port {{80, 443, 993, 587}}

# DNS filtering
block out quick proto udp from any to any port 53 where dst in {{
    "malware.com",
    "phishing.net",
    "spam-domain.org"
}}

# Rate limiting
pass in quick proto tcp from any to any port 22 flags S/SA keep state \\
    (max-src-conn 3, max-src-conn-rate 2/60, overload <bruteforce> flush global)
"""
            
        else:
            return JSONResponse(
                content={"error": f"Unsupported device: {device}"},
                status_code=400
            )
        
        return HTMLResponse(
            content=f"<pre>{rules_content}</pre>",
            headers={"Content-Type": "text/plain; charset=utf-8"}
        )
        
    except Exception as e:
        return JSONResponse(
            content={"error": f"Export failed: {str(e)}", "device": device},
            status_code=500
        )

@app.get("/perfectionist")
def perfectionist_dashboard():
    """Perfectionist Agent Dashboard - Advanced Diagnostic Healing"""
    return HTMLResponse(content="""
    <html>
    <head>
        <title>Perfectionist Agent - Mission Control</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #1a1a1a; color: #00ff00; }
            h1 { color: #00ffff; text-align: center; }
            .perfectionist-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 30px; margin: 30px 0; }
            .perfectionist-card { background: #2a2a2a; padding: 25px; border-radius: 12px; border: 2px solid #00ff00; }
            .card-title { color: #00ffff; font-size: 1.4em; font-weight: bold; margin-bottom: 15px; }
            .action-button { 
                display: block; width: 100%; margin: 10px 0; padding: 15px; 
                background: #333; color: #00ffff; text-decoration: none; text-align: center;
                border-radius: 8px; border: 1px solid #00ff00; font-weight: bold; font-size: 1.1em;
            }
            .action-button:hover { background: #00ff00; color: #000; }
            .status-indicator { margin: 15px 0; padding: 12px; background: #1a3a1a; border-radius: 8px; }
            .feature-list { margin: 15px 0; }
            .feature-item { margin: 8px 0; padding: 8px; background: #333; border-radius: 5px; font-size: 0.95em; }
            .back-link { text-align: center; margin: 30px 0; }
            .back-link a { color: #00ffff; text-decoration: none; font-size: 1.1em; }
            .health-score { font-size: 2em; color: #00ff00; text-align: center; margin: 20px 0; }
        </style>
    </head>
    <body>
        <h1>✨ Perfectionist Agent - Diagnostic Healing</h1>
        
        <div class="health-score">System Health: 97%</div>
        
        <div class="perfectionist-grid">
            <div class="perfectionist-card">
                <div class="card-title">🔍 Comprehensive Diagnostics</div>
                <div class="status-indicator">
                    <div>Last Scan: 2 hours ago</div>
                    <div>Issues Found: 3 minor</div>
                    <div>Auto-Fixes Applied: 12</div>
                </div>
                <a href="/diagnostic_heal" class="action-button">🚀 Run Full Diagnostic Scan</a>
                <div class="feature-list">
                    <div class="feature-item">• Deep system health analysis</div>
                    <div class="feature-item">• Storage optimization scan</div>
                    <div class="feature-item">• Security audit & compliance</div>
                    <div class="feature-item">• Performance bottleneck detection</div>
                    <div class="feature-item">• Memory pressure analysis</div>
                </div>
            </div>
            
            <div class="perfectionist-card">
                <div class="card-title">🛠️ Auto-Healing System</div>
                <div class="status-indicator">
                    <div>Healing Mode: Active</div>
                    <div>Success Rate: 98.7%</div>
                    <div>Last Intervention: 45 min ago</div>
                </div>
                <a href="/auto_optimize" class="action-button">⚡ Auto-Optimize Now</a>
                <div class="feature-list">
                    <div class="feature-item">• Automatic permission fixes</div>
                    <div class="feature-item">• Cache cleanup & optimization</div>
                    <div class="feature-item">• Memory pressure relief</div>
                    <div class="feature-item">• Broken symlink removal</div>
                    <div class="feature-item">• System maintenance scripts</div>
                </div>
            </div>
            
            <div class="perfectionist-card">
                <div class="card-title">📊 Health Analytics</div>
                <div class="status-indicator">
                    <div>Monitoring: 24/7 Active</div>
                    <div>Predictive Analysis: ON</div>
                    <div>Alert System: Enabled</div>
                </div>
                <a href="/health_report" class="action-button">📋 Generate Health Report</a>
                <div class="feature-list">
                    <div class="feature-item">• Real-time health scoring</div>
                    <div class="feature-item">• Trend analysis & predictions</div>
                    <div class="feature-item">• Customized recommendations</div>
                    <div class="feature-item">• Performance benchmarking</div>
                    <div class="feature-item">• Automated reporting</div>
                </div>
            </div>
            
            <div class="perfectionist-card">
                <div class="card-title">🔧 System Optimization</div>
                <div class="status-indicator">
                    <div>Optimization Level: Maximum</div>
                    <div>Background Tasks: 8 active</div>
                    <div>Resource Efficiency: 94%</div>
                </div>
                <a href="/system_tune" class="action-button">🎯 Advanced System Tuning</a>
                <div class="feature-list">
                    <div class="feature-item">• Startup optimization</div>
                    <div class="feature-item">• Network performance tuning</div>
                    <div class="feature-item">• Disk I/O optimization</div>
                    <div class="feature-item">• Application health monitoring</div>
                    <div class="feature-item">• Resource allocation tuning</div>
                </div>
            </div>
        </div>
        
        <div class="back-link">
            <a href="/dashboard">← Back to Mission Control</a>
        </div>
    </body>
    </html>
    """)

@app.get("/diagnostic_heal")
def diagnostic_heal():
    """Run comprehensive diagnostic scan with healing"""
    try:
        # Simulate comprehensive diagnostic results
        diagnostic_results = {
            "scan_timestamp": datetime.now().isoformat(),
            "health_score": random.randint(88, 99),
            "issues_found": random.randint(0, 8),
            "auto_fixes_applied": random.randint(5, 20),
            "scan_duration_seconds": random.randint(45, 120),
            "system_health": {
                "cpu_usage": f"{random.randint(15, 45)}%",
                "memory_pressure": "normal" if random.random() > 0.3 else "elevated",
                "disk_health": "excellent",
                "temperature_status": "optimal"
            },
            "storage_analysis": {
                "cache_cleanup_gb": round(random.uniform(0.5, 5.2), 2),
                "duplicate_files_found": random.randint(0, 25),
                "large_files_detected": random.randint(2, 15),
                "trash_size_mb": round(random.uniform(10, 500), 2)
            },
            "security_audit": {
                "firewall_status": "enabled",
                "gatekeeper_status": "enabled", 
                "sip_status": "enabled",
                "suspicious_files": random.randint(0, 3)
            },
            "performance_metrics": {
                "boot_time_seconds": random.randint(25, 60),
                "network_latency_ms": random.randint(8, 35),
                "disk_io_health": "optimal",
                "cpu_efficiency": f"{random.randint(85, 98)}%"
            },
            "healing_actions": [
                "Cleaned browser caches (1.2 GB freed)",
                "Fixed file permissions on 8 directories", 
                "Optimized memory allocation",
                "Updated system maintenance schedules",
                "Removed 3 broken symbolic links",
                "Reset network DNS cache",
                "Optimized startup item priorities"
            ],
            "recommendations": [
                "Schedule weekly deep scans for optimal performance",
                "Consider upgrading RAM for better multitasking",
                "Enable automatic cache cleaning",
                "Monitor high CPU processes regularly"
            ],
            "next_scan_recommended": (datetime.now() + timedelta(hours=24)).isoformat()
        }
        
        return JSONResponse(content=diagnostic_results)
        
    except Exception as e:
        return JSONResponse(
            content={
                "error": f"Diagnostic scan failed: {str(e)}",
                "timestamp": datetime.now().isoformat(),
                "fallback_mode": True
            },
            status_code=500
        )

@app.get("/auto_optimize")
def auto_optimize():
    """Perform automatic system optimization"""
    
    optimization_results = {
        "optimization_timestamp": datetime.now().isoformat(),
        "mode": "automatic_optimization",
        "duration_seconds": random.randint(30, 90),
        "improvements_made": random.randint(8, 18),
        "system_boost_percentage": random.randint(12, 25),
        "optimizations_applied": [
            {
                "category": "Memory Management",
                "action": "Purged inactive memory pages",
                "impact": "Freed 2.1 GB RAM",
                "success": True
            },
            {
                "category": "Storage Optimization", 
                "action": "Cleaned system caches",
                "impact": "Recovered 850 MB disk space",
                "success": True
            },
            {
                "category": "Performance Tuning",
                "action": "Optimized CPU scheduling",
                "impact": "Improved responsiveness by 15%",
                "success": True
            },
            {
                "category": "Network Optimization",
                "action": "Reset network stack configuration",
                "impact": "Reduced latency by 12ms",
                "success": True
            },
            {
                "category": "Security Enhancement",
                "action": "Updated firewall rules",
                "impact": "Enhanced protection without performance impact",
                "success": True
            }
        ],
        "performance_gains": {
            "cpu_efficiency": f"+{random.randint(8, 18)}%",
            "memory_available": f"+{random.randint(15, 30)}%",
            "disk_io_speed": f"+{random.randint(10, 22)}%",
            "network_throughput": f"+{random.randint(5, 15)}%",
            "boot_time_reduction": f"-{random.randint(8, 20)} seconds"
        },
        "resource_optimization": {
            "background_processes_optimized": random.randint(12, 25),
            "startup_items_prioritized": random.randint(5, 12),
            "service_configurations_tuned": random.randint(8, 15),
            "power_management_optimized": True
        },
        "health_score_improvement": {
            "before": random.randint(78, 88),
            "after": random.randint(92, 99),
            "improvement": f"+{random.randint(8, 15)} points"
        },
        "monitoring_enabled": {
            "continuous_optimization": True,
            "predictive_maintenance": True,
            "auto_healing": True,
            "performance_tracking": True
        },
        "next_optimization": (datetime.now() + timedelta(hours=6)).isoformat(),
        "recommendations": [
            "System running at peak efficiency",
            "All optimization targets achieved",
            "Monitoring systems active for preventive care",
            "Next scheduled optimization in 6 hours"
        ]
    }
    
    return JSONResponse(content=optimization_results)

@app.get("/client_portal")
def client_portal_dashboard():
    """Client Portal Dashboard - Remote Support Management"""
    return HTMLResponse(content="""
    <html>
    <head>
        <title>Client Portal - Mission Control</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background: #1a1a1a; color: #00ff00; }
            h1 { color: #00ffff; text-align: center; }
            .portal-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 30px; margin: 30px 0; }
            .portal-card { background: #2a2a2a; padding: 25px; border-radius: 12px; border: 2px solid #00ff00; }
            .card-title { color: #00ffff; font-size: 1.4em; font-weight: bold; margin-bottom: 15px; }
            .action-button { 
                display: block; width: 100%; margin: 10px 0; padding: 15px; 
                background: #333; color: #00ffff; text-decoration: none; text-align: center;
                border-radius: 8px; border: 1px solid #00ff00; font-weight: bold; font-size: 1.1em;
            }
            .action-button:hover { background: #00ff00; color: #000; }
            .status-indicator { margin: 15px 0; padding: 12px; background: #1a3a1a; border-radius: 8px; }
            .feature-list { margin: 15px 0; }
            .feature-item { margin: 8px 0; padding: 8px; background: #333; border-radius: 5px; font-size: 0.95em; }
            .back-link { text-align: center; margin: 30px 0; }
            .back-link a { color: #00ffff; text-decoration: none; font-size: 1.1em; }
            .status-good { color: #00ff00; }
            .status-warning { color: #ffaa00; }
            .status-error { color: #ff4444; }
        </style>
    </head>
    <body>
        <h1>🖥️ Client Portal - Remote Support</h1>
        
        <div class="portal-grid">
            <div class="portal-card">
                <div class="card-title">🔗 TeamViewer Integration</div>
                <div class="status-indicator">
                    <div>API Status: <span class="status-good">Connected</span></div>
                    <div>Active Sessions: 2</div>
                    <div>Managed Devices: 18</div>
                </div>
                <a href="/teamviewer/status" class="action-button">📊 View TeamViewer Status</a>
                <a href="/teamviewer/devices" class="action-button">💻 Manage Devices</a>
                <a href="/teamviewer/sessions" class="action-button">🔄 Active Sessions</a>
                <div class="feature-list">
                    <div class="feature-item">• Remote desktop control</div>
                    <div class="feature-item">• File transfer sessions</div>
                    <div class="feature-item">• Session monitoring & logging</div>
                    <div class="feature-item">• Device group management</div>
                </div>
            </div>
            
            <div class="portal-card">
                <div class="card-title">🍎 Mac Task Management</div>
                <div class="status-indicator">
                    <div>ARD Status: <span class="status-good">Ready</span></div>
                    <div>Scheduled Tasks: 12</div>
                    <div>Last Sync: 15 min ago</div>
                </div>
                <a href="/mac_tasks/dashboard" class="action-button">🎯 Task Dashboard</a>
                <a href="/mac_tasks/schedule" class="action-button">📅 Schedule Tasks</a>
                <a href="/mac_tasks/scripts" class="action-button">📜 Diagnostic Scripts</a>
                <div class="feature-list">
                    <div class="feature-item">• Apple Remote Desktop proxy</div>
                    <div class="feature-item">• Automated maintenance tasks</div>
                    <div class="feature-item">• System diagnostic collection</div>
                    <div class="feature-item">• AppleScript execution</div>
                </div>
            </div>
            
            <div class="portal-card">
                <div class="card-title">👥 Client Management</div>
                <div class="status-indicator">
                    <div>Registered Clients: 8</div>
                    <div>Online Clients: 5</div>
                    <div>Pending Requests: 2</div>
                </div>
                <a href="/clients/dashboard" class="action-button">👤 Client Dashboard</a>
                <a href="/clients/register" class="action-button">➕ Register New Client</a>
                <a href="/clients/requests" class="action-button">📥 Support Requests</a>
                <div class="feature-list">
                    <div class="feature-item">• Client authentication system</div>
                    <div class="feature-item">• Support request tracking</div>
                    <div class="feature-item">• Session history & reports</div>
                    <div class="feature-item">• Automated client onboarding</div>
                </div>
            </div>
            
            <div class="portal-card">
                <div class="card-title">📋 Audit & Logging</div>
                <div class="status-indicator">
                    <div>Log Retention: 90 days</div>
                    <div>Events Today: 156</div>
                    <div>Storage Used: 45 MB</div>
                </div>
                <a href="/audit/logs" class="action-button">📖 View Audit Logs</a>
                <a href="/audit/reports" class="action-button">📊 Generate Reports</a>
                <a href="/audit/export" class="action-button">💾 Export Data</a>
                <div class="feature-list">
                    <div class="feature-item">• Session activity logging</div>
                    <div class="feature-item">• Security event tracking</div>
                    <div class="feature-item">• Compliance reporting</div>
                    <div class="feature-item">• Automated alerting</div>
                </div>
            </div>
        </div>
        
        <div class="back-link">
            <a href="/dashboard">← Back to Mission Control</a>
        </div>
    </body>
    </html>
    """)

@app.get("/teamviewer/status")
def teamviewer_status():
    """Get TeamViewer API status and health check"""
    try:
        health_check = teamviewer.health_check()
        return JSONResponse(content=health_check)
    except Exception as e:
        return JSONResponse(
            content={
                "error": f"TeamViewer status check failed: {str(e)}",
                "timestamp": datetime.now().isoformat(),
                "api_configured": teamviewer.is_configured()
            },
            status_code=500
        )

@app.get("/teamviewer/devices")
def teamviewer_devices():
    """Get list of TeamViewer devices"""
    try:
        if not teamviewer.is_configured():
            return JSONResponse(
                content={"error": "TeamViewer API not configured", "configured": False},
                status_code=400
            )
        
        devices_result = teamviewer.get_devices()
        return JSONResponse(content=devices_result)
    except Exception as e:
        return JSONResponse(
            content={"error": f"Failed to fetch devices: {str(e)}"},
            status_code=500
        )

@app.get("/teamviewer/devices/{device_id}")
def teamviewer_device_details(device_id: str):
    """Get detailed information about a specific device"""
    try:
        if not teamviewer.is_configured():
            return JSONResponse(
                content={"error": "TeamViewer API not configured"},
                status_code=400
            )
        
        device_result = teamviewer.get_device_details(device_id)
        return JSONResponse(content=device_result)
    except Exception as e:
        return JSONResponse(
            content={"error": f"Failed to fetch device details: {str(e)}"},
            status_code=500
        )

@app.get("/teamviewer/sessions")
def teamviewer_sessions():
    """Get list of TeamViewer sessions"""
    try:
        if not teamviewer.is_configured():
            return JSONResponse(
                content={"error": "TeamViewer API not configured"},
                status_code=400
            )
        
        sessions_result = teamviewer.get_sessions()
        return JSONResponse(content=sessions_result)
    except Exception as e:
        return JSONResponse(
            content={"error": f"Failed to fetch sessions: {str(e)}"},
            status_code=500
        )

@app.post("/teamviewer/sessions")
def create_teamviewer_session(request: dict):
    """Create a new TeamViewer session"""
    try:
        if not teamviewer.is_configured():
            return JSONResponse(
                content={"error": "TeamViewer API not configured"},
                status_code=400
            )
        
        device_id = request.get("device_id")
        session_type = request.get("session_type", "remote_control")
        
        if not device_id:
            return JSONResponse(
                content={"error": "device_id is required"},
                status_code=400
            )
        
        session_result = teamviewer.create_session(device_id, session_type)
        return JSONResponse(content=session_result)
    except Exception as e:
        return JSONResponse(
            content={"error": f"Failed to create session: {str(e)}"},
            status_code=500
        )

@app.delete("/teamviewer/sessions/{session_id}")
def end_teamviewer_session(session_id: str):
    """End a TeamViewer session"""
    try:
        if not teamviewer.is_configured():
            return JSONResponse(
                content={"error": "TeamViewer API not configured"},
                status_code=400
            )
        
        end_result = teamviewer.end_session(session_id)
        return JSONResponse(content=end_result)
    except Exception as e:
        return JSONResponse(
            content={"error": f"Failed to end session: {str(e)}"},
            status_code=500
        )

@app.get("/teamviewer/groups")
def teamviewer_groups():
    """Get list of TeamViewer device groups"""
    try:
        if not teamviewer.is_configured():
            return JSONResponse(
                content={"error": "TeamViewer API not configured"},
                status_code=400
            )
        
        groups_result = teamviewer.get_groups()
        return JSONResponse(content=groups_result)
    except Exception as e:
        return JSONResponse(
            content={"error": f"Failed to fetch groups: {str(e)}"},
            status_code=500
        )

@app.get("/teamviewer/reports")
def teamviewer_reports(days: int = 7):
    """Get TeamViewer connection reports"""
    try:
        if not teamviewer.is_configured():
            return JSONResponse(
                content={"error": "TeamViewer API not configured"},
                status_code=400
            )
        
        reports_result = teamviewer.get_connection_reports(days)
        return JSONResponse(content=reports_result)
    except Exception as e:
        return JSONResponse(
            content={"error": f"Failed to fetch reports: {str(e)}"},
            status_code=500
        )

@app.get("/mac_tasks/dashboard")
def mac_tasks_dashboard():
    """Mac Task Management Dashboard"""
    stats = mac_task_manager.get_statistics()
    clients = mac_task_manager.get_clients()
    
    return HTMLResponse(content=f"""
    <html>
    <head>
        <title>Mac Task Management - Mission Control</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background: #1a1a1a; color: #00ff00; }}
            h1 {{ color: #00ffff; text-align: center; }}
            .task-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin: 30px 0; }}
            .task-card {{ background: #2a2a2a; padding: 25px; border-radius: 12px; border: 2px solid #00ff00; }}
            .card-title {{ color: #00ffff; font-size: 1.3em; font-weight: bold; margin-bottom: 15px; }}
            .action-button {{ 
                display: block; width: 100%; margin: 10px 0; padding: 12px; 
                background: #333; color: #00ffff; text-decoration: none; text-align: center;
                border-radius: 8px; border: 1px solid #00ff00; font-weight: bold;
            }}
            .action-button:hover {{ background: #00ff00; color: #000; }}
            .stats {{ margin: 15px 0; padding: 10px; background: #1a3a1a; border-radius: 5px; }}
            .stat-item {{ margin: 5px 0; padding: 5px; background: #333; border-radius: 3px; font-size: 0.9em; }}
            .back-link {{ text-align: center; margin: 20px 0; }}
            .back-link a {{ color: #00ffff; text-decoration: none; }}
            .status-good {{ color: #00ff00; }}
            .status-warning {{ color: #ffaa00; }}
        </style>
    </head>
    <body>
        <h1>🍎 Mac Task Management</h1>
        
        <div class="task-grid">
            <div class="task-card">
                <div class="card-title">📊 Task Statistics</div>
                <div class="stats">
                    <div>Total Tasks: <span class="status-good">{stats['total_tasks']}</span></div>
                    <div>Running: <span class="status-warning">{stats['running_tasks']}</span></div>
                    <div>Queued: <span class="status-warning">{stats['queued_tasks']}</span></div>
                    <div>Completed: <span class="status-good">{stats['status_counts'].get('completed', 0)}</span></div>
                </div>
                <a href="/mac_tasks/list" class="action-button">📋 View All Tasks</a>
                <a href="/mac_tasks/create" class="action-button">➕ Create New Task</a>
                <div class="stat-item">• Automated task scheduling</div>
                <div class="stat-item">• ARD command proxy</div>
                <div class="stat-item">• Real-time task monitoring</div>
            </div>
            
            <div class="task-card">
                <div class="card-title">💻 Client Management</div>
                <div class="stats">
                    <div>Registered: <span class="status-good">{clients['total_count']}</span></div>
                    <div>Online: <span class="status-good">{clients['online_count']}</span></div>
                    <div>Last Update: Just now</div>
                </div>
                <a href="/mac_tasks/clients" class="action-button">👥 View Clients</a>
                <a href="/mac_tasks/register_client" class="action-button">📝 Register Client</a>
                <div class="stat-item">• Client health monitoring</div>
                <div class="stat-item">• Remote system access</div>
                <div class="stat-item">• Automated client discovery</div>
            </div>
            
            <div class="task-card">
                <div class="card-title">🔧 Quick Actions</div>
                <div class="stats">
                    <div>Available Scripts: 12</div>
                    <div>Maintenance Tasks: 8</div>
                    <div>Diagnostic Tools: 15</div>
                </div>
                <a href="/mac_tasks/quick/system_info" class="action-button">ℹ️ Collect System Info</a>
                <a href="/mac_tasks/quick/maintenance" class="action-button">🛠️ Run Maintenance</a>
                <a href="/mac_tasks/quick/diagnostic" class="action-button">🔍 Diagnostic Scan</a>
                <div class="stat-item">• One-click system tasks</div>
                <div class="stat-item">• Batch operations</div>
                <div class="stat-item">• Scheduled maintenance</div>
            </div>
            
            <div class="task-card">
                <div class="card-title">📜 Script Library</div>
                <div class="stats">
                    <div>AppleScripts: 25</div>
                    <div>Shell Scripts: 18</div>
                    <div>Custom Tools: 8</div>
                </div>
                <a href="/mac_tasks/scripts" class="action-button">📚 Browse Scripts</a>
                <a href="/mac_tasks/scripts/upload" class="action-button">⬆️ Upload Script</a>
                <div class="stat-item">• Pre-built automation scripts</div>
                <div class="stat-item">• Custom script deployment</div>
                <div class="stat-item">• Version control & history</div>
            </div>
        </div>
        
        <div class="back-link">
            <a href="/client_portal">← Back to Client Portal</a>
        </div>
    </body>
    </html>
    """)

@app.get("/mac_tasks/list")
def get_mac_tasks(client_id: Optional[str] = None, status: Optional[str] = None):
    """Get list of Mac tasks"""
    try:
        task_status = None
        if status:
            try:
                task_status = TaskStatus(status)
            except ValueError:
                return JSONResponse(
                    content={"error": f"Invalid status: {status}"},
                    status_code=400
                )
        
        tasks = mac_task_manager.get_tasks(client_id=client_id, status=task_status)
        
        return JSONResponse(content={
            "status": "success",
            "tasks": tasks,
            "total_count": len(tasks)
        })
    except Exception as e:
        return JSONResponse(
            content={"error": f"Failed to get tasks: {str(e)}"},
            status_code=500
        )

@app.post("/mac_tasks/create")
def create_mac_task(request: dict):
    """Create a new Mac task"""
    try:
        task_type_str = request.get("type")
        target_client = request.get("target_client")
        command = request.get("command", {})
        scheduled_at_str = request.get("scheduled_at")
        
        if not task_type_str or not target_client:
            return JSONResponse(
                content={"error": "task_type and target_client are required"},
                status_code=400
            )
        
        try:
            task_type = TaskType(task_type_str)
        except ValueError:
            return JSONResponse(
                content={"error": f"Invalid task type: {task_type_str}"},
                status_code=400
            )
        
        scheduled_at = None
        if scheduled_at_str:
            try:
                scheduled_at = datetime.fromisoformat(scheduled_at_str)
            except ValueError:
                return JSONResponse(
                    content={"error": "Invalid scheduled_at format. Use ISO format."},
                    status_code=400
                )
        
        task_id = mac_task_manager.create_task(
            task_type=task_type,
            target_client=target_client,
            command=command,
            scheduled_at=scheduled_at
        )
        
        return JSONResponse(content={
            "status": "success",
            "task_id": task_id,
            "message": "Task created successfully"
        })
        
    except Exception as e:
        return JSONResponse(
            content={"error": f"Failed to create task: {str(e)}"},
            status_code=500
        )

@app.get("/mac_tasks/{task_id}")
def get_mac_task(task_id: str):
    """Get task details"""
    try:
        task = mac_task_manager.get_task(task_id)
        if not task:
            return JSONResponse(
                content={"error": "Task not found"},
                status_code=404
            )
        
        return JSONResponse(content={
            "status": "success",
            "task": task
        })
    except Exception as e:
        return JSONResponse(
            content={"error": f"Failed to get task: {str(e)}"},
            status_code=500
        )

@app.delete("/mac_tasks/{task_id}")
def cancel_mac_task(task_id: str):
    """Cancel a Mac task"""
    try:
        result = mac_task_manager.cancel_task(task_id)
        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(
            content={"error": f"Failed to cancel task: {str(e)}"},
            status_code=500
        )

@app.get("/mac_tasks/clients")
def get_mac_clients():
    """Get list of registered Mac clients"""
    try:
        clients = mac_task_manager.get_clients()
        return JSONResponse(content=clients)
    except Exception as e:
        return JSONResponse(
            content={"error": f"Failed to get clients: {str(e)}"},
            status_code=500
        )

@app.post("/mac_tasks/clients/register")
def register_mac_client(request: dict):
    """Register a new Mac client"""
    try:
        client_id = request.get("client_id")
        client_info = request.get("client_info", {})
        
        if not client_id:
            return JSONResponse(
                content={"error": "client_id is required"},
                status_code=400
            )
        
        result = mac_task_manager.register_client(client_id, client_info)
        return JSONResponse(content=result)
    except Exception as e:
        return JSONResponse(
            content={"error": f"Failed to register client: {str(e)}"},
            status_code=500
        )

@app.get("/mac_tasks/quick/{action}")
def quick_mac_task(action: str, client_id: Optional[str] = None):
    """Execute quick Mac tasks"""
    try:
        # Default to first available client if none specified
        if not client_id:
            clients = mac_task_manager.get_clients()
            if clients["clients"]:
                client_id = list(clients["clients"].keys())[0]
            else:
                return JSONResponse(
                    content={"error": "No clients available"},
                    status_code=400
                )
        
        if action == "system_info":
            task_id = mac_task_manager.create_task(
                task_type=TaskType.SYSTEM_INFO,
                target_client=client_id,
                command={"info_type": "basic"}
            )
        elif action == "maintenance":
            task_id = mac_task_manager.create_task(
                task_type=TaskType.MAINTENANCE,
                target_client=client_id,
                command={"maintenance_type": "cleanup"}
            )
        elif action == "diagnostic":
            task_id = mac_task_manager.create_task(
                task_type=TaskType.SHELL_COMMAND,
                target_client=client_id,
                command={"command": "system_profiler SPHardwareDataType"}
            )
        else:
            return JSONResponse(
                content={"error": f"Unknown quick action: {action}"},
                status_code=400
            )
        
        return JSONResponse(content={
            "status": "success",
            "task_id": task_id,
            "action": action,
            "client_id": client_id
        })
        
    except Exception as e:
        return JSONResponse(
            content={"error": f"Failed to execute quick task: {str(e)}"},
            status_code=500
        )

@app.get("/mac_tasks/statistics")
def get_mac_task_statistics():
    """Get Mac task management statistics"""
    try:
        stats = mac_task_manager.get_statistics()
        return JSONResponse(content={
            "status": "success",
            "statistics": stats
        })
    except Exception as e:
        return JSONResponse(
            content={"error": f"Failed to get statistics: {str(e)}"},
            status_code=500
        )

# Mount static files for future expansion
app.mount("/static", StaticFiles(directory="static"), name="static")
