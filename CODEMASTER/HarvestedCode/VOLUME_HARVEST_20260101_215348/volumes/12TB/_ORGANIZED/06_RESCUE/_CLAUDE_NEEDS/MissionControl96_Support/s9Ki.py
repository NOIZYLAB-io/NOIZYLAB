#!/usr/bin/env python3
"""
Noizy.ai Business Launch Script
Starts the complete business infrastructure including:
- Mission Control core system
- Monetization server with Stripe integration
- Stream server for real-time chat
- Dashboard server for client management
"""

import os
import sys
import subprocess
import time
import signal
import threading
from pathlib import Path

# Process tracking
processes = []

def signal_handler(sig, frame):
    """Gracefully shut down all processes."""
    print("\n🛑 Shutting down Noizy.ai Business Infrastructure...")
    for process in processes:
        try:
            process.terminate()
            process.wait(timeout=5)
        except (subprocess.TimeoutExpired, AttributeError):
            try:
                process.kill()
            except:
                pass
    print("✅ All services stopped.")
    sys.exit(0)

def start_service(script_name, description, port=None):
    """Start a service and track the process."""
    print(f"🚀 Starting {description}...")
    
    # Make sure we're in the right directory
    os.chdir(Path(__file__).parent)
    
    # Activate virtual environment
    venv_python = ".venv/bin/python" if os.path.exists(".venv/bin/python") else "python3"
    
    try:
        process = subprocess.Popen([venv_python, script_name], 
                                 stdout=subprocess.PIPE, 
                                 stderr=subprocess.PIPE)
        processes.append(process)
        
        # Give it a moment to start
        time.sleep(2)
        
        # Check if it's still running
        if process.poll() is None:
            if port:
                print(f"✅ {description} started successfully on port {port}")
            else:
                print(f"✅ {description} started successfully")
        else:
            stdout, stderr = process.communicate()
            print(f"❌ {description} failed to start:")
            print(f"STDOUT: {stdout.decode()}")
            print(f"STDERR: {stderr.decode()}")
            
    except Exception as e:
        print(f"❌ Error starting {description}: {e}")

def check_requirements():
    """Ensure all required files and dependencies are available."""
    required_files = [
        "mission_control.py",
        "noizy_monetization.py", 
        "noizy_stream_server.py",
        "dashboard_server.py",
        ".env"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        return False
    
    # Check virtual environment
    if not os.path.exists(".venv"):
        print("❌ Virtual environment not found. Run: python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt")
        return False
    
    return True

def load_env_config():
    """Load and validate environment configuration."""
    env_path = Path(".env")
    if not env_path.exists():
        print("❌ .env file not found")
        return False
    
    # Load environment variables
    with open(env_path) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, _, value = line.partition('=')
                os.environ[key.strip()] = value.strip()
    
    # Validate critical settings
    required_env = ["STRIPE_SECRET_KEY", "JWT_SECRET_KEY", "ADMIN_EMAIL"]
    missing_env = [env for env in required_env if not os.getenv(env)]
    
    if missing_env:
        print(f"⚠️  Missing environment variables: {', '.join(missing_env)}")
        print("   Business features may not work properly")
    
    return True

def main():
    """Main business launch sequence."""
    print("🎯 NOIZY.AI BUSINESS INFRASTRUCTURE")
    print("=" * 50)
    
    # Set up signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Pre-flight checks
    if not check_requirements():
        sys.exit(1)
    
    if not load_env_config():
        sys.exit(1)
    
    print("✅ Pre-flight checks passed")
    print()
    
    # Start services in order
    services = [
        ("mission_control.py", "Mission Control Core", 8000),
        ("noizy_monetization.py", "Stripe Monetization Server", 8001), 
        ("noizy_stream_server.py", "WebSocket Stream Server", 8002),
        ("dashboard_server.py", "Client Dashboard", 8003)
    ]
    
    for script, description, port in services:
        start_service(script, description, port)
        time.sleep(3)  # Stagger startup
    
    print()
    print("🎉 NOIZY.AI BUSINESS READY!")
    print("=" * 50)
    print("🌐 Main Portal:", os.getenv("HOSTING_URL", "http://localhost:8000"))
    print("💳 Payments:", f"{os.getenv('HOSTING_URL', 'http://localhost:8001')}/checkout")
    print("💬 Chat Stream:", f"ws://localhost:8002/ws")
    print("📊 Dashboard:", f"http://localhost:8003")
    print()
    print("🔧 VS Code Extension: noizy-vscode/")
    print("📦 Client Installer: NoizyAI_Installer_v1/")
    print()
    print("Press Ctrl+C to stop all services")
    
    # Keep running until interrupted
    try:
        while True:
            # Check if any process died
            for i, process in enumerate(processes):
                if process.poll() is not None:
                    service_name = services[i][1]
                    print(f"⚠️  {service_name} stopped unexpectedly")
                    # Could add auto-restart logic here
            
            time.sleep(10)
    except KeyboardInterrupt:
        signal_handler(None, None)

if __name__ == "__main__":
    main()