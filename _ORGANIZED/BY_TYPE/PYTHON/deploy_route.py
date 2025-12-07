"""
NoizyOS Ultra — Deploy API Routes
=================================
Version checking, update distribution, and deployment management.
"""

from fastapi import APIRouter
from fastapi.responses import FileResponse
from ..deploy.version import (
    VERSION, UPDATE_SERVER, CHANNELS,
    get_update_info, set_channel_version
)
import os

router = APIRouter()


@router.get("/version")
def get_version():
    """Get current server version."""
    return {
        "version": VERSION,
        "server": "NoizyOS Ultra Backend"
    }


@router.get("/latest")
def get_latest():
    """Get latest stable version info."""
    return UPDATE_SERVER


@router.get("/check/{current_version}")
def check_update(current_version: str, channel: str = "stable"):
    """
    Check if an update is available.
    
    Args:
        current_version: Client's current version
        channel: Update channel (stable/beta/dev)
    """
    return get_update_info(current_version, channel)


@router.get("/channels")
def list_channels():
    """List all update channels."""
    return {
        "channels": list(CHANNELS.keys()),
        "info": {k: {"version": v["version"], "notes": v["notes"]} 
                 for k, v in CHANNELS.items()}
    }


@router.get("/channel/{channel}")
def get_channel(channel: str):
    """Get info for a specific channel."""
    if channel not in CHANNELS:
        return {"error": "Channel not found"}
    return CHANNELS[channel]


@router.get("/download/{channel}")
def download_update(channel: str):
    """
    Download update package.
    In production, this would serve actual installer files.
    """
    if channel not in CHANNELS:
        return {"error": "Channel not found"}
    
    # Check for actual package file
    package_dir = "/Volumes/6TB/noizyOS_v2/packages"
    version = CHANNELS[channel]["version"]
    
    # Try different package formats
    for ext in [".pkg", ".dmg", ".exe", ".zip"]:
        package_path = os.path.join(package_dir, f"noizylab_{version}{ext}")
        if os.path.exists(package_path):
            return FileResponse(
                package_path,
                filename=f"NoizyLab_{version}{ext}",
                media_type="application/octet-stream"
            )
    
    return {
        "error": "Package not found",
        "channel": channel,
        "version": version,
        "note": "Build packages using the installer scripts"
    }


@router.post("/release")
def create_release(payload: dict):
    """
    Create a new release (admin endpoint).
    
    Payload:
        channel: stable/beta/dev
        version: New version string
        notes: Release notes
    """
    channel = payload.get("channel", "stable")
    version = payload.get("version")
    notes = payload.get("notes")
    
    if not version:
        return {"ok": False, "error": "Version required"}
    
    success = set_channel_version(channel, version, notes)
    return {"ok": success, "channel": channel, "version": version}


@router.get("/install-script/{platform}")
def get_install_script(platform: str):
    """
    Get installation script for a platform.
    
    Platforms: macos, windows, linux
    """
    scripts = {
        "macos": """#!/bin/bash
# NoizyOS Ultra Installer for macOS

echo "Installing NoizyOS Ultra..."

# Download package
curl -O http://localhost:8080/deploy/download/stable

# Install
sudo installer -pkg noizylab_*.pkg -target /

# Start service
sudo launchctl load /Library/LaunchDaemons/com.noizylab.agent.plist

echo "Installation complete!"
""",
        "windows": """@echo off
REM NoizyOS Ultra Installer for Windows

echo Installing NoizyOS Ultra...

REM Download installer
curl -O http://localhost:8080/deploy/download/stable

REM Run installer
NoizyLab_Installer.exe /S

REM Install service
nssm install NoizyLab-Agent "C:\\NoizyLab\\noizylab_agent.exe"
nssm start NoizyLab-Agent

echo Installation complete!
pause
""",
        "linux": """#!/bin/bash
# NoizyOS Ultra Installer for Linux

echo "Installing NoizyOS Ultra..."

# Download package
curl -O http://localhost:8080/deploy/download/stable

# Extract
tar -xzf noizylab_*.tar.gz -C /opt/

# Create systemd service
sudo cp /opt/noizylab/noizylab.service /etc/systemd/system/
sudo systemctl enable noizylab
sudo systemctl start noizylab

echo "Installation complete!"
"""
    }
    
    if platform not in scripts:
        return {"error": "Unknown platform", "supported": list(scripts.keys())}
    
    return {"platform": platform, "script": scripts[platform]}

