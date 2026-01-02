from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from dotenv import load_dotenv
import os
import psutil
import time
from datetime import datetime
import random

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
        </div>
        <div class="nav-links">
            <a href='/fetch/diagnostics'>🔍 View Diagnostics</a>
            <a href='/generate_playlist'>🎵 Generate Playlist</a>
            <a href='/health'>❤️ Health Check</a>
            <a href='/api/status'>📊 API Status</a>
            <a href='/audio_library'>🎧 Audio Library</a>
            <a href='/device_sync'>📱 Device Sync</a>
            <a href='/spam_filter'>🛡️ Spam Filter</a>
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
                "spam_filter": {"status": "online", "rules_active": random.randint(15, 45), "blocked_today": random.randint(5, 25)}
            },
            "environment": {
                "dashboard_url": os.getenv("MC_DASHBOARD_URL", "http://127.0.0.1:8765/dashboard"),
                "dns_domain": os.getenv("DNS_DOMAIN", "Not configured"),
                "apis_configured": {
                    "godaddy": bool(os.getenv("GODADDY_API_KEY") and os.getenv("GODADDY_API_KEY") != "..."),
                    "elevenlabs": bool(os.getenv("ELEVENLABS_API_KEY") and os.getenv("ELEVENLABS_API_KEY") != "..."),
                    "openai": bool(os.getenv("OPENAI_API_KEY") and os.getenv("OPENAI_API_KEY") != "...")
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
            "openai": os.getenv("OPENAI_API_KEY", "...") != "..."
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
                "spam_filter": "online"
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
            "/sync_spam_rules/{device}"
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

# Mount static files for future expansion
app.mount("/static", StaticFiles(directory="static"), name="static")
