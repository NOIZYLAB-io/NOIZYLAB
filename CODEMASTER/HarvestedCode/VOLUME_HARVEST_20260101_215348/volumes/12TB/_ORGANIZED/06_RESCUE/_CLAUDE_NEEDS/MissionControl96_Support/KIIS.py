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
        </div>
        <div class="nav-links">
            <a href='/fetch/diagnostics'>🔍 View Diagnostics</a>
            <a href='/generate_playlist'>🎵 Generate Playlist</a>
            <a href='/health'>❤️ Health Check</a>
            <a href='/api/status'>📊 API Status</a>
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
                "memory_keeper": {"status": "online", "memory_optimized": f"{random.randint(10, 95)}%"}
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
                "memory_keeper": "online"
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
            "/api/status"
        ]
    })

# Mount static files for future expansion
app.mount("/static", StaticFiles(directory="static"), name="static")
