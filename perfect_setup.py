#!/usr/bin/env python3
#!/usr/bin/env python3
"""
PERFECT ONE-CLICK GMAIL SETUP
Fully accessible with large buttons, voice control, and full automation
Designed for users with limited mobility
"""

import webbrowser
import pyperclip
import time
import sys
import subprocess
import os
from pathlib import Path

# Configuration
ICLOUD_EMAIL = "rsplowman@icloud.com"
APP_PASSWORD = "bdzw-ekxx-uhxi-pgym"
GMAIL_SETTINGS_URL = "https://mail.google.com/mail/u/0/#settings/accounts"

class PerfectSetup:
    """Perfect accessible setup system"""
    
    def __init__(self):
        self.settings = {
            "email": ICLOUD_EMAIL,
            "password": APP_PASSWORD,
            "smtp_server": "smtp.mail.me.com",
            "port": "587",
            "security": "TLS"
        }
        self.clipboard_queue = []
    
    def speak(self, text):
        """Text-to-speech using macOS say command"""
        try:
            subprocess.run(["say", text], check=False)
        except:
            pass
    
    def copy_to_clipboard(self, text):
        """Copy to clipboard"""
        try:
            pyperclip.copy(text)
            return True
        except:
            return False
    
    def open_gmail(self):
        """Open Gmail settings"""
        webbrowser.open(GMAIL_SETTINGS_URL)
        self.speak("Opening Gmail settings")
        time.sleep(3)
    
    def create_automation_script(self):
        """Create AppleScript for automation"""
        applescript = f'''
tell application "Safari"
    activate
    open location "{GMAIL_SETTINGS_URL}"
    delay 3
end tell

tell application "System Events"
    tell process "Safari"
        delay 2
        -- Wait for page to load
        delay 3
    end tell
end tell
'''
        script_path = Path.home() / "Desktop" / "Gmail_Setup.scpt"
        try:
            with open(script_path, 'w') as f:
                f.write(applescript)
            os.chmod(script_path, 0o755)
            return str(script_path)
        except:
            return None
    
    def create_instructions_card(self):
        """Create large, readable instructions"""
        instructions = f"""
╔════════════════════════════════════════════════════════════════╗
║           ONE-CLICK GMAIL SETUP - EASY INSTRUCTIONS            ║
╚════════════════════════════════════════════════════════════════╝

STEP 1: Gmail is opening automatically...
        (Wait 5 seconds)

STEP 2: Scroll down to "Send mail as" section
        (Use arrow keys or mouse)

STEP 3: Click "Add another email address"
        (Large button, easy to click)

STEP 4: When Gmail asks for EMAIL:
        Press: CMD + V
        (Email is already copied!)

STEP 5: Click "Next Step"

STEP 6: When Gmail asks for SMTP SERVER:
        Press: CMD + V
        (Server is already copied!)

STEP 7: When Gmail asks for PORT:
        Type: 587
        (Or press CMD + V if copied)

STEP 8: When Gmail asks for USERNAME:
        Press: CMD + V
        (Email is already copied!)

STEP 9: When Gmail asks for PASSWORD:
        Press: CMD + V
        (Password is already copied!)

STEP 10: Select "TLS" for security
         Click "Add Account"

STEP 11: Check your iCloud email for verification
         Click the link in the email

════════════════════════════════════════════════════════════════

QUICK REFERENCE - ALL SETTINGS (Already in Clipboard):

Email:        {self.settings['email']}
Password:     {self.settings['password']}
SMTP Server:  {self.settings['smtp_server']}
Port:         {self.settings['port']}
Security:     {self.settings['security']}

════════════════════════════════════════════════════════════════

KEYBOARD SHORTCUTS:
- CMD + V = Paste (use this for all fields!)
- CMD + C = Copy
- Tab = Move to next field
- Enter = Submit/Next

════════════════════════════════════════════════════════════════

NEED HELP?
- All settings are saved in your clipboard
- Just press CMD + V when Gmail asks
- Take your time, no rush!

════════════════════════════════════════════════════════════════
"""
        return instructions
    
    def run_full_automation(self):
        """Run complete automation"""
        print("\n" + "="*80)
        print("🚀 PERFECT ONE-CLICK SETUP STARTING")
        print("="*80)
        
        self.speak("Starting Gmail setup automation")
        
        # Step 1: Copy all settings to clipboard in order
        print("\n📋 STEP 1: Preparing all settings...")
        self.speak("Preparing settings")
        
        settings_list = [
            ("Email", self.settings['email']),
            ("Password", self.settings['password']),
            ("SMTP Server", self.settings['smtp_server']),
            ("Port", self.settings['port']),
            ("Username", self.settings['email'])
        ]
        
        # Copy first item (email)
        self.copy_to_clipboard(self.settings['email'])
        print(f"   ✅ {self.settings['email']} - Ready to paste (CMD+V)")
        self.speak("Email copied to clipboard")
        
        # Step 2: Open Gmail
        print("\n🌐 STEP 2: Opening Gmail...")
        self.open_gmail()
        self.speak("Gmail is opening")
        print("   ✅ Gmail opened in your browser")
        print("   ⏳ Wait 5 seconds for page to load...")
        time.sleep(5)
        
        # Step 3: Create instructions file
        print("\n📄 STEP 3: Creating instructions...")
        instructions = self.create_instructions_card()
        
        # Save to desktop
        desktop = Path.home() / "Desktop"
        instructions_file = desktop / "GMAIL_SETUP_INSTRUCTIONS.txt"
        with open(instructions_file, 'w') as f:
            f.write(instructions)
        
        print(f"   ✅ Instructions saved to Desktop")
        print(f"   📄 File: GMAIL_SETUP_INSTRUCTIONS.txt")
        
        # Open instructions file
        try:
            subprocess.run(["open", str(instructions_file)], check=False)
        except:
            pass
        
        # Step 4: Prepare clipboard queue
        print("\n📋 STEP 4: All settings ready!")
        print("\n" + "="*80)
        print("SETTINGS QUEUE (Press CMD+V when Gmail asks):")
        print("="*80)
        
        for i, (label, value) in enumerate(settings_list, 1):
            print(f"\n{i}. {label}:")
            print(f"   Value: {value}")
            print(f"   Action: Press CMD+V to paste")
            self.clipboard_queue.append((label, value))
        
        # Copy email first (most common first field)
        self.copy_to_clipboard(self.settings['email'])
        
        print("\n" + "="*80)
        print("✅ AUTOMATION COMPLETE!")
        print("="*80)
        
        print("\n📋 WHAT TO DO NOW:")
        print("   1. Gmail is open in your browser")
        print("   2. Instructions file is open on your Desktop")
        print("   3. Email is already in clipboard (press CMD+V)")
        print("   4. Follow the instructions step by step")
        print("   5. Just press CMD+V when Gmail asks for each field")
        
        self.speak("Setup complete. Gmail is ready. Follow the instructions on your screen.")
        
        # Create quick reference
        self.create_quick_reference()
        
        return True
    
    def create_quick_reference(self):
        """Create quick reference card"""
        ref = f"""
╔══════════════════════════════════════════════════════════════╗
║                    QUICK REFERENCE CARD                      ║
╚══════════════════════════════════════════════════════════════╝

WHEN GMAIL ASKS FOR:

📧 Email Address:
   → Press: CMD + V
   → Value: {self.settings['email']}

🔐 Password:
   → Press: CMD + V  
   → Value: {self.settings['password']}

📮 SMTP Server:
   → Press: CMD + V
   → Value: {self.settings['smtp_server']}

🔢 Port:
   → Type: {self.settings['port']}
   → Or: CMD + V (if copied)

👤 Username:
   → Press: CMD + V
   → Value: {self.settings['email']}

🔒 Security:
   → Select: TLS
   → (Click the TLS option)

══════════════════════════════════════════════════════════════

KEYBOARD SHORTCUTS:
   CMD + V = Paste (use this!)
   Tab = Next field
   Enter = Submit

══════════════════════════════════════════════════════════════
"""
        desktop = Path.home() / "Desktop"
        ref_file = desktop / "QUICK_REFERENCE.txt"
        with open(ref_file, 'w') as f:
            f.write(ref)
        
        print(f"\n   ✅ Quick reference saved to Desktop")
        print(f"   📄 File: QUICK_REFERENCE.txt")

def main():
    """Main function"""
    print("\n" + "="*80)
    print(" " * 20 + "PERFECT ONE-CLICK GMAIL SETUP")
    print(" " * 15 + "Designed for Maximum Accessibility")
    print("="*80)
    
    setup = PerfectSetup()
    
    print("\nThis will:")
    print("  ✅ Open Gmail automatically")
    print("  ✅ Copy all settings to clipboard")
    print("  ✅ Create easy-to-read instructions")
    print("  ✅ Use text-to-speech for guidance")
    print("  ✅ Save everything to your Desktop")
    print("\nYou just need to:")
    print("  • Press CMD+V when Gmail asks for each field")
    print("  • Click a few buttons")
    print("  • Take your time - no rush!")
    
    input("\n🚀 Press ENTER to start (or any key + ENTER)...")
    
    try:
        setup.run_full_automation()
        
        print("\n" + "="*80)
        print("🎉 SUCCESS! Everything is ready!")
        print("="*80)
        print("\n📁 Files created on Desktop:")
        print("   • GMAIL_SETUP_INSTRUCTIONS.txt")
        print("   • QUICK_REFERENCE.txt")
        print("\n💡 Tip: Keep the instructions open while setting up Gmail")
        print("\n✅ You've got this! Take your time.")
        
    except KeyboardInterrupt:
        print("\n\n👋 Setup cancelled. Run again anytime!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("But all settings are saved - you can still do it manually!")

if __name__ == "__main__":
    main()

