#!/usr/bin/env python3
#!/usr/bin/env python3
"""
Quick Guide: Using App-Specific Password for rsplowman@icloud.com in Gmail
"""

def show_setup_guide():
    """Show setup guide with app-specific password"""
    
    app_password = "bdzw-ekxx-uhxi-pgym"
    email = "rsplowman@icloud.com"
    
    print("\n" + "="*70)
    print("📧 SETUP rsplowman@icloud.com IN GMAIL")
    print("="*70)
    
    print(f"\n✅ App-Specific Password: {app_password}")
    print("   (Case-sensitive - enter exactly as shown)")
    
    print("\n" + "="*70)
    print("OPTION 1: Add iCloud Email to Gmail (Receive & Send)")
    print("="*70)
    
    print("\n📥 TO RECEIVE EMAILS:")
    print("-" * 70)
    print("1. Gmail → Settings → Accounts and Import")
    print("2. Under 'Check mail from other accounts', click 'Add a mail account'")
    print(f"3. Enter: {email}")
    print("4. Choose 'Link accounts with Gmailify (IMAP)'")
    print("\n   IMAP Settings:")
    print(f"   • Server: imap.mail.me.com")
    print(f"   • Port: 993 (SSL/TLS)")
    print(f"   • Username: {email}")
    print(f"   • Password: {app_password} ← Use app-specific password")
    
    print("\n📤 TO SEND EMAILS:")
    print("-" * 70)
    print("1. Gmail → Settings → Accounts and Import")
    print("2. Under 'Send mail as', click 'Add another email address'")
    print(f"3. Enter: {email}")
    print("\n   SMTP Settings:")
    print(f"   • Server: smtp.mail.me.com")
    print(f"   • Port: 587 (STARTTLS)")
    print(f"   • Username: {email}")
    print(f"   • Password: {app_password} ← Use app-specific password")
    print("4. Verify the email when Gmail sends confirmation")
    
    print("\n" + "="*70)
    print("OPTION 2: Add as Alternate Email (For App Logins)")
    print("="*70)
    print("\nThis allows you to use rsplowman@icloud.com when apps")
    print("ask you to 'Sign in with Google'.")
    print("\nSteps:")
    print("1. Go to: https://myaccount.google.com/")
    print("2. Personal info → Email → Add alternate email")
    print(f"3. Enter: {email}")
    print("4. Verify via email sent to {email}")
    print("\nWhen signing into apps:")
    print(f"  • Enter: {email}")
    print("  • Use your Gmail account password (not app-specific password)")
    
    print("\n" + "="*70)
    print("QUICK REFERENCE")
    print("="*70)
    print(f"\nEmail: {email}")
    print(f"App Password: {app_password}")
    print("\nIMAP: imap.mail.me.com:993 (SSL/TLS)")
    print("SMTP: smtp.mail.me.com:587 (STARTTLS)")
    
    print("\n" + "="*70)
    print("⚠️  IMPORTANT:")
    print("="*70)
    print("• App-specific password is ONLY for Gmail IMAP/SMTP setup")
    print("• Use your Gmail password for Google account sign-ins")
    print("• Keep app password secure - don't share it")
    print("• You can revoke it from appleid.apple.com anytime")
    
    print("\n" + "="*70)

if __name__ == "__main__":
    show_setup_guide()
    input("\nPress Enter to exit...")

