#!/usr/bin/env python3
"""
Download Llama Models from Meta
Handles signed URLs and model downloads
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse, parse_qs
import hashlib

BASE = Path("/Users/m2ultra/NOIZYLAB")
MODELS_DIR = BASE / "models" / "llama"
MODELS_DIR.mkdir(parents=True, exist_ok=True)

def download_file(url, destination, chunk_size=8192):
    """Download file with progress"""
    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        downloaded = 0
        
        with open(destination, 'wb') as f:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    if total_size > 0:
                        percent = (downloaded / total_size) * 100
                        print(f"\r  Progress: {percent:.1f}% ({downloaded}/{total_size} bytes)", end='', flush=True)
        
        print()  # New line after progress
        return True
    except Exception as e:
        print(f"\n❌ Error downloading: {e}")
        return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 download_llama_model.py <url>")
        print("\nExample:")
        print("  python3 download_llama_model.py 'https://llama3-3.llamameta.net/...'")
        sys.exit(1)
    
    url = sys.argv[1]
    
    print("=" * 80)
    print(" " * 20 + "📥 Download Llama Model")
    print("=" * 80)
    print()
    print(f"URL: {url[:80]}...")
    print(f"Destination: {MODELS_DIR}")
    print()
    
    # Try to extract filename from URL or use hash
    parsed = urlparse(url)
    filename = os.path.basename(parsed.path) or f"model_{hashlib.md5(url.encode()).hexdigest()[:8]}.bin"
    
    destination = MODELS_DIR / filename
    
    print(f"Downloading to: {destination}")
    print()
    
    if download_file(url, destination):
        file_size = destination.stat().st_size
        print(f"✅ Download complete!")
        print(f"   File: {destination}")
        print(f"   Size: {file_size / (1024*1024):.2f} MB")
    else:
        print("❌ Download failed")
        if destination.exists():
            destination.unlink()  # Remove partial file
        sys.exit(1)

if __name__ == "__main__":
    main()

