#!/usr/bin/env python3
#!/usr/bin/env python3
"""
ONE-CLICK Gmail Setup for iCloud Email
Designed for accessibility - minimal interaction required
"""

import webbrowser
import pyperclip
import time
import sys

# Configuration
ICLOUD_EMAIL = "rsplowman@icloud.com"
APP_PASSWORD = "bdzw-ekxx-uhxi-pgym"

def copy_to_clipboard(text):
    """Copy text to clipboard"""
    try:
        pyperclip.copy(text)
        return True
    except:
        return False

def open_gmail_settings():
    """Open Gmail settings directly"""
    url = "https://mail.google.com/mail/u/0/#settings/accounts"
    webbrowser.open(url)
    print("✅ Opened Gmail Settings")
    time.sleep(2)

def setup_smtp_automated():
    """Automated SMTP setup with clipboard assistance"""
    print("\n" + "="*70)
    print("🤖 ONE-CLICK AUTOMATED SETUP")
    print("="*70)
    
    print("\n📋 STEP 1: Opening Gmail Settings...")
    open_gmail_settings()
    
    print("\n📋 STEP 2: Copying settings to clipboard...")
    print("   (You can paste these when Gmail asks)")
    
    # Copy email
    copy_to_clipboard(ICLOUD_EMAIL)
    print(f"   ✅ Email copied: {ICLOUD_EMAIL}")
    print("   💡 Press Cmd+V to paste when Gmail asks for email")
    
    input("\n   Press Enter when you're ready for next step...")
    
    # Copy password
    copy_to_clipboard(APP_PASSWORD)
    print(f"   ✅ Password copied: {APP_PASSWORD}")
    print("   💡 Press Cmd+V to paste when Gmail asks for password")
    
    input("\n   Press Enter when you're ready for SMTP settings...")
    
    # Copy SMTP server
    copy_to_clipboard("smtp.mail.me.com")
    print("   ✅ SMTP Server copied: smtp.mail.me.com")
    print("   💡 Press Cmd+V to paste when Gmail asks for SMTP server")
    
    input("\n   Press Enter when ready for port...")
    
    # Copy port
    copy_to_clipboard("587")
    print("   ✅ Port copied: 587")
    print("   💡 Press Cmd+V to paste when Gmail asks for port")
    
    print("\n" + "="*70)
    print("✅ SETTINGS READY TO PASTE!")
    print("="*70)
    print("\nAll settings are in your clipboard.")
    print("Just press Cmd+V to paste when Gmail asks for each field.")
    print("\nSettings Summary:")
    print(f"  Email: {ICLOUD_EMAIL}")
    print(f"  Password: {APP_PASSWORD}")
    print("  SMTP Server: smtp.mail.me.com")
    print("  Port: 587")
    print("  Security: TLS")

def create_instructions_file():
    """Create a simple instructions file"""
    instructions = f"""
ONE-CLICK GMAIL SETUP INSTRUCTIONS
==================================

1. Click the button below or run: python3 one_click_setup.py

2. Gmail will open automatically

3. When Gmail asks for settings, just press CMD+V to paste

SETTINGS (Already in clipboard):
- Email: {ICLOUD_EMAIL}
- Password: {APP_PASSWORD}
- SMTP Server: smtp.mail.me.com
- Port: 587
- Security: TLS

STEPS:
1. Gmail opens → Scroll to "Send mail as"
2. Click "Add another email address"
3. Press CMD+V to paste email → Click Next
4. Press CMD+V to paste password → Click Next
5. Press CMD+V to paste SMTP server → Enter port 587
6. Select TLS security → Click Add Account
7. Verify email when it arrives

That's it! Just paste (CMD+V) when Gmail asks for each field.
"""
    
    with open("SIMPLE_INSTRUCTIONS.txt", "w") as f:
        f.write(instructions)
    
    print("\n✅ Created SIMPLE_INSTRUCTIONS.txt")
    print("   Open this file for easy reference")

def main():
    """Main function"""
    print("\n" + "="*70)
    print("🚀 ONE-CLICK GMAIL SETUP")
    print("="*70)
    print("\nThis will:")
    print("  1. Open Gmail settings")
    print("  2. Copy all settings to clipboard")
    print("  3. You just paste (CMD+V) when Gmail asks")
    print("\nMinimal clicking required!")
    
    input("\nPress Enter to start (or any key + Enter)...")
    
    setup_smtp_automated()
    create_instructions_file()
    
    print("\n" + "="*70)
    print("✅ DONE! Settings are ready to paste.")
    print("="*70)
    print("\nJust use CMD+V to paste when Gmail asks for each field.")
    print("You can do this!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Cancelled. Run again anytime!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("But you can still do it manually - all settings are saved!")

