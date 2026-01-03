#!/usr/bin/env python3
"""
Generate Gemini Prompt for Adding Emails to Gmail
Optimized for users with limited mobility
"""

def generate_gemini_prompt():
    """Generate the perfect prompt for Gemini"""
    
    prompt = """I need help adding external email addresses to my Gmail account. I have limited mobility in my arms and hands, so I need step-by-step instructions that minimize clicks and use keyboard shortcuts whenever possible.

EMAILS TO ADD:
1. rsplowman@icloud.com (iCloud email)
   - App-specific password: bdzw-ekxx-uhxi-pgym
   - IMAP Server: imap.mail.me.com (Port 993, SSL/TLS)
   - SMTP Server: smtp.mail.me.com (Port 587, STARTTLS/TLS)

2. rsp@noizylab.ca (Microsoft 365 email)
   - IMAP Server: outlook.office365.com (Port 993, SSL/TLS)
   - SMTP Server: smtp.office365.com (Port 587, STARTTLS/TLS)

3. help@noizylab.ca (Microsoft 365 email)
   - IMAP Server: outlook.office365.com (Port 993, SSL/TLS)
   - SMTP Server: smtp.office365.com (Port 587, STARTTLS/TLS)

MY REQUIREMENTS:
- I can use keyboard shortcuts (CMD+V to paste, Tab to navigate, Enter to submit)
- I prefer using arrow keys to scroll instead of mouse
- I can click buttons, but want to minimize clicks as much as possible
- I have macOS Voice Control available if needed
- I need clear, numbered steps with exact values to enter

WHAT I NEED FROM YOU:
1. Step-by-step instructions for adding each email to Gmail's "Send mail as" feature
2. Exact values to paste into each field (I'll copy them to clipboard first)
3. Keyboard shortcuts to use instead of mouse when possible
4. Total number of clicks required for each email
5. Troubleshooting tips if something doesn't work
6. Clear indication of which settings go in which fields

SPECIFIC INSTRUCTIONS NEEDED:
- How to navigate to Gmail Settings → Accounts and Import → Send mail as
- Exact field names in Gmail's interface
- What to paste in each field (email, SMTP server, port, username, password, security)
- How to verify the email after setup
- What to do if I get an error

PLEASE PROVIDE:
- Numbered steps (1, 2, 3, etc.)
- Exact values to copy/paste
- Keyboard shortcuts in parentheses like (CMD+V)
- Click count for each step
- Alternative methods if something fails

Start with rsplowman@icloud.com first, then provide instructions for the other two emails."""
    
    return prompt

def save_prompt_to_files():
    """Save prompt to multiple formats"""
    prompt = generate_gemini_prompt()
    
    # Save as text file
    text_file = Path.home() / "Desktop" / "GEMINI_EMAIL_PROMPT.txt"
    with open(text_file, 'w') as f:
        f.write(prompt)
    
    # Save in project
    project_file = Path(__file__).parent / "GEMINI_EMAIL_PROMPT.txt"
    with open(project_file, 'w') as f:
        f.write(prompt)
    
    # Copy to clipboard
    try:
        import pyperclip
        pyperclip.copy(prompt)
        print("✅ Prompt copied to clipboard!")
    except:
        print("⚠️  Could not copy to clipboard (pyperclip not installed)")
    
    print(f"\n✅ Prompt saved to:")
    print(f"   • Desktop: GEMINI_EMAIL_PROMPT.txt")
    print(f"   • Project: {project_file}")
    print(f"\n📋 The prompt is ready to paste into Gemini!")
    print(f"   Just open Gemini and paste (CMD+V)")

def main():
    """Main function"""
    print("\n" + "="*80)
    print("🤖 GEMINI EMAIL SETUP PROMPT GENERATOR")
    print("="*80)
    
    save_prompt_to_files()
    
    print("\n" + "="*80)
    print("📋 HOW TO USE:")
    print("="*80)
    print("1. Open Gemini AI (gemini.google.com)")
    print("2. Open GEMINI_EMAIL_PROMPT.txt from Desktop")
    print("3. Copy all the text (CMD+A, then CMD+C)")
    print("4. Paste into Gemini (CMD+V)")
    print("5. Gemini will give you step-by-step instructions!")
    print("\n" + "="*80)

if __name__ == "__main__":
    from pathlib import Path
    main()

