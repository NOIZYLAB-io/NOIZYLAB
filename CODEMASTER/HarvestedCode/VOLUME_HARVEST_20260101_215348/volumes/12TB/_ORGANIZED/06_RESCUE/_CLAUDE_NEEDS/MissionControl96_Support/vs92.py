#!/usr/bin/env python3
"""
Mission Control Server Management Script
Intelligently handles server startup with conflict resolution
"""

import os
import subprocess
import sys
import time
import signal
import psutil
from pathlib import Path

def get_process_using_port(port):
    """Find process using specified port"""
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            for conn in proc.connections():
                if conn.laddr.port == port:
                    return proc
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return None

def is_our_server(process, port):
    """Check if the process is our uvicorn server"""
    if not process:
        return False
    
    cmdline = ' '.join(process.info.get('cmdline', []))
    return (
        'uvicorn' in cmdline and 
        'dashboard_server:app' in cmdline and 
        str(port) in cmdline
    )

def safe_to_kill(process):
    """Determine if it's safe to kill the process"""
    if not process:
        return True
    
    cmdline = ' '.join(process.info.get('cmdline', []))
    
    # Safe to kill if it's our own uvicorn server
    if 'uvicorn' in cmdline and 'dashboard_server' in cmdline:
        return True
    
    # Safe to kill if it's a development server
    if any(dev_indicator in cmdline.lower() for dev_indicator in 
           ['--reload', '--dev', 'development', 'debug']):
        return True
    
    # Not safe if it's a system process or production server
    if any(sys_indicator in cmdline.lower() for sys_indicator in 
           ['systemd', 'nginx', 'apache', '--production', 'gunicorn']):
        return False
    
    return False

def kill_process_gracefully(process, timeout=5):
    """Kill process gracefully with timeout"""
    try:
        print(f"🔄 Gracefully stopping process {process.pid}...")
        process.terminate()
        
        # Wait for graceful shutdown
        try:
            process.wait(timeout=timeout)
            print("✅ Process stopped gracefully")
            return True
        except psutil.TimeoutExpired:
            print("⚠️  Graceful shutdown timed out, forcing kill...")
            process.kill()
            process.wait(timeout=2)
            print("💀 Process force killed")
            return True
            
    except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
        print(f"⚠️  Could not kill process: {e}")
        return False

def start_server(port=8765, host="127.0.0.1"):
    """Start the FastAPI server"""
    venv_python = Path(__file__).parent / ".venv" / "bin" / "python"
    
    if not venv_python.exists():
        print("❌ Virtual environment not found. Please run setup first.")
        return False
    
    cmd = [
        str(venv_python),
        "-m", "uvicorn",
        "dashboard_server:app",
        "--host", host,
        "--port", str(port),
        "--reload"
    ]
    
    print(f"🚀 Starting Mission Control Dashboard on {host}:{port}")
    
    try:
        # Start in background
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=Path(__file__).parent
        )
        
        # Give it a moment to start
        time.sleep(2)
        
        # Check if it's running
        if process.poll() is None:
            print(f"✅ Server started successfully!")
            print(f"🌐 Dashboard: http://{host}:{port}/dashboard")
            print("🔄 Auto-reload enabled for development")
            return True
        else:
            stdout, stderr = process.communicate()
            print(f"❌ Server failed to start:")
            print(f"STDOUT: {stdout.decode()}")
            print(f"STDERR: {stderr.decode()}")
            return False
            
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        return False

def main():
    port = 8765
    host = "127.0.0.1"
    
    print("🎯 Mission Control Server Manager")
    print("=" * 40)
    
    # Check what's using the port
    existing_process = get_process_using_port(port)
    
    if existing_process:
        print(f"🔍 Found process using port {port}: PID {existing_process.pid}")
        
        if is_our_server(existing_process, port):
            print("✅ Our server is already running!")
            print(f"🌐 Dashboard: http://{host}:{port}/dashboard")
            
            response = input("🤔 Restart server? (y/N): ").strip().lower()
            if response in ['y', 'yes']:
                if kill_process_gracefully(existing_process):
                    time.sleep(1)  # Brief pause
                    return start_server(port, host)
                else:
                    print("❌ Failed to stop existing server")
                    return False
            else:
                print("📡 Keeping existing server running")
                return True
        
        else:
            print("⚠️  Different process is using the port")
            cmdline = ' '.join(existing_process.info.get('cmdline', []))
            print(f"Process: {cmdline}")
            
            if safe_to_kill(existing_process):
                print("✅ Process appears safe to terminate")
                response = input("🤔 Kill process and start our server? (y/N): ").strip().lower()
                if response in ['y', 'yes']:
                    if kill_process_gracefully(existing_process):
                        time.sleep(1)
                        return start_server(port, host)
                    else:
                        print("❌ Failed to stop existing process")
                        return False
                else:
                    print("❌ Cannot start server - port in use")
                    return False
            else:
                print("❌ Process does not appear safe to kill")
                print("💡 Try using a different port or manually stop the process")
                return False
    
    else:
        print(f"✅ Port {port} is available")
        return start_server(port, host)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)