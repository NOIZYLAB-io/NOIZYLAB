#!/usr/bin/env python3
#!/usr/bin/env python3
"""
Code snippets for Gemini AI to help with email setup
"""

# Configuration data for Gemini
ICLOUD_EMAIL_CONFIG = {
    "email": "rsplowman@icloud.com",
    "app_password": "bdzw-ekxx-uhxi-pgym",
    "imap": {
        "server": "imap.mail.me.com",
        "port": 993,
        "security": "SSL/TLS",
        "username": "rsplowman@icloud.com"
    },
    "smtp": {
        "server": "smtp.mail.me.com",
        "port": 587,
        "security": "STARTTLS/TLS",
        "username": "rsplowman@icloud.com"
    }
}

# Prompt template for Gemini
GEMINI_PROMPT = """
I need help setting up my iCloud email in Gmail.

Email: rsplowman@icloud.com
App-Specific Password: bdzw-ekxx-uhxi-pgym

Please provide:
1. Step-by-step instructions for adding this email to Gmail
2. Exact IMAP settings (server, port, security, username)
3. Exact SMTP settings (server, port, security, username)
4. Common troubleshooting tips

Configuration details:
- IMAP Server: imap.mail.me.com
- IMAP Port: 993
- IMAP Security: SSL/TLS
- SMTP Server: smtp.mail.me.com
- SMTP Port: 587
- SMTP Security: STARTTLS/TLS
- Username: rsplowman@icloud.com (full email)
- Password: bdzw-ekxx-uhxi-pgym (app-specific password)

Please guide me through the Gmail interface to add this account.
"""

# Quick reference for Gemini
QUICK_REFERENCE = """
iCloud Email Setup for Gmail - Quick Reference:

Email: rsplowman@icloud.com
Password: bdzw-ekxx-uhxi-pgym (app-specific)

IMAP (Receive):
- Server: imap.mail.me.com
- Port: 993
- Security: SSL/TLS
- Username: rsplowman@icloud.com

SMTP (Send):
- Server: smtp.mail.me.com
- Port: 587
- Security: TLS
- Username: rsplowman@icloud.com

Steps:
1. Gmail → Settings → Accounts and Import
2. Add a mail account → Enter rsplowman@icloud.com
3. Choose IMAP (not POP3)
4. Enter settings above
5. Verify email
"""

def print_gemini_prompt():
    """Print the prompt to give to Gemini"""
    print("\n" + "="*70)
    print("📋 COPY THIS PROMPT TO GEMINI:")
    print("="*70)
    print(GEMINI_PROMPT)
    print("="*70)

def print_quick_reference():
    """Print quick reference"""
    print("\n" + "="*70)
    print("📋 QUICK REFERENCE FOR GEMINI:")
    print("="*70)
    print(QUICK_REFERENCE)
    print("="*70)

def generate_gemini_code():
    """Generate code snippet for Gemini"""
    code = f"""
# iCloud Email Configuration for Gmail
email_config = {{
    "email": "{ICLOUD_EMAIL_CONFIG['email']}",
    "app_password": "{ICLOUD_EMAIL_CONFIG['app_password']}",
    "imap_server": "{ICLOUD_EMAIL_CONFIG['imap']['server']}",
    "imap_port": {ICLOUD_EMAIL_CONFIG['imap']['port']},
    "imap_security": "{ICLOUD_EMAIL_CONFIG['imap']['security']}",
    "smtp_server": "{ICLOUD_EMAIL_CONFIG['smtp']['server']}",
    "smtp_port": {ICLOUD_EMAIL_CONFIG['smtp']['port']},
    "smtp_security": "{ICLOUD_EMAIL_CONFIG['smtp']['security']}",
    "username": "{ICLOUD_EMAIL_CONFIG['imap']['username']}"
}}

print("Gmail Settings:")
print(f"IMAP: {{email_config['imap_server']}}:{{email_config['imap_port']}}")
print(f"SMTP: {{email_config['smtp_server']}}:{{email_config['smtp_port']}}")
"""
    return code

if __name__ == "__main__":
    print("\n" + "="*70)
    print("🤖 GEMINI AI PROMPTS & CODE")
    print("="*70)
    
    print("\n1. PROMPT TO GIVE TO GEMINI:")
    print_gemini_prompt()
    
    print("\n2. QUICK REFERENCE:")
    print_quick_reference()
    
    print("\n3. CODE SNIPPET:")
    print("="*70)
    print(generate_gemini_code())
    print("="*70)
    
    print("\n💡 TIP: Copy the prompt above and paste it into Gemini AI")
    print("   Gemini will guide you through the setup process!")
    print("\n" + "="*70)

