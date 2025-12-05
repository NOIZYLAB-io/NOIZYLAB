#!/usr/bin/env python3
# UNIVERSAL AI SELECTOR
# Works on Mac, Windows, Linux via Cloudflare Worker
# GORUNFREEX1000 - Cross-platform edition

import sys
import subprocess
import json
import urllib.request
import urllib.parse
from pathlib import Path

# Configuration
WORKER_URL = "https://ai-genius-cloud.YOUR-SUBDOMAIN.workers.dev"
DEFAULT_MODEL = "claude-sonnet-4"

# Platform detection
import platform
IS_MAC = platform.system() == "Darwin"
IS_WINDOWS = platform.system() == "Windows"
IS_LINUX = platform.system() == "Linux"

def get_selected_text():
    """Get currently selected text (cross-platform)"""
    
    if IS_MAC:
        # macOS - AppleScript
        script = '''
        tell application "System Events"
            keystroke "c" using command down
            delay 0.1
        end tell
        return the clipboard
        '''
        result = subprocess.run(['osascript', '-e', script], 
                              capture_output=True, text=True)
        return result.stdout.strip()
    
    elif IS_WINDOWS:
        # Windows - PowerShell
        script = '''
        Add-Type -AssemblyName System.Windows.Forms
        [System.Windows.Forms.SendKeys]::SendWait("^c")
        Start-Sleep -Milliseconds 100
        Get-Clipboard
        '''
        result = subprocess.run(['powershell', '-Command', script],
                              capture_output=True, text=True)
        return result.stdout.strip()
    
    elif IS_LINUX:
        # Linux - xclip or xsel
        try:
            # Try xclip first
            result = subprocess.run(['xclip', '-o', '-selection', 'primary'],
                                  capture_output=True, text=True)
            return result.stdout.strip()
        except:
            # Fallback to xsel
            result = subprocess.run(['xsel', '--primary', '--output'],
                                  capture_output=True, text=True)
            return result.stdout.strip()
    
    return ""

def send_to_ai(text, model_id=DEFAULT_MODEL):
    """Send text to Cloudflare Worker AI"""
    
    url = f"{WORKER_URL}/api/ask"
    data = {
        "model_id": model_id,
        "message": text
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode('utf-8'),
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            return result.get('response', 'Error: No response')
    except Exception as e:
        return f"Error: {str(e)}"

def copy_to_clipboard(text):
    """Copy text to clipboard (cross-platform)"""
    
    if IS_MAC:
        subprocess.run(['pbcopy'], input=text.encode('utf-8'))
    elif IS_WINDOWS:
        subprocess.run(['clip'], input=text.encode('utf-8'), shell=True)
    elif IS_LINUX:
        try:
            subprocess.run(['xclip', '-selection', 'clipboard'],
                         input=text.encode('utf-8'))
        except:
            subprocess.run(['xsel', '--clipboard', '--input'],
                         input=text.encode('utf-8'))

def show_notification(title, message):
    """Show system notification (cross-platform)"""
    
    if IS_MAC:
        script = f'''
        display notification "{message}" with title "{title}"
        '''
        subprocess.run(['osascript', '-e', script])
    
    elif IS_WINDOWS:
        # Windows Toast notification
        script = f'''
        [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] | Out-Null
        [Windows.Data.Xml.Dom.XmlDocument, Windows.Data.Xml.Dom.XmlDocument, ContentType = WindowsRuntime] | Out-Null
        $template = @"
        <toast>
            <visual>
                <binding template="ToastText02">
                    <text id="1">{title}</text>
                    <text id="2">{message}</text>
                </binding>
            </visual>
        </toast>
        "@
        $xml = New-Object Windows.Data.Xml.Dom.XmlDocument
        $xml.LoadXml($template)
        $toast = [Windows.UI.Notifications.ToastNotification]::new($xml)
        [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("AI GENIUS").Show($toast)
        '''
        subprocess.run(['powershell', '-Command', script])
    
    elif IS_LINUX:
        subprocess.run(['notify-send', title, message])

def main():
    """Main function"""
    
    # Get model from argument or use default
    model_id = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_MODEL
    
    # Get selected text
    print("Getting selected text...")
    text = get_selected_text()
    
    if not text:
        show_notification("AI GENIUS", "No text selected")
        return
    
    # Show notification
    show_notification("AI GENIUS", f"Sending to {model_id}...")
    
    # Send to AI
    print(f"Sending to {model_id}...")
    response = send_to_ai(text, model_id)
    
    # Copy response to clipboard
    copy_to_clipboard(response)
    
    # Show success notification
    show_notification("AI GENIUS", "Response copied to clipboard!")
    
    # Print response
    print("\n" + "="*60)
    print(f"MODEL: {model_id}")
    print("="*60)
    print(response)
    print("="*60)

if __name__ == "__main__":
    main()
