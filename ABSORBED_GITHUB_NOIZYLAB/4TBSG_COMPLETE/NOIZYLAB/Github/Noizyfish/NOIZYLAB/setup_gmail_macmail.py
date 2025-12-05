#!/usr/bin/env python3
#!/usr/bin/env python3
"""
Quick Setup Script: Gmail in Mac Mail + Add iCloud Email to Gmail
Run this script for step-by-step instructions
"""

def gmail_macmail_setup():
    """Guide for adding Gmail to Mac Mail"""
    print("\n" + "="*70)
    print("📧 ADDING GMAIL TO MAC MAIL")
    print("="*70)
    
    print("\nSTEP 1: Enable IMAP in Gmail")
    print("-" * 70)
    print("1. Go to: https://mail.google.com/mail/u/0/#settings/general")
    print("2. Click 'See all settings'")
    print("3. Go to 'Forwarding and POP/IMAP' tab")
    print("4. Under 'IMAP access', select 'Enable IMAP'")
    print("5. Click 'Save Changes'")
    
    input("\n✅ Press Enter when IMAP is enabled...")
    
    print("\nSTEP 2: Generate App-Specific Password (if 2FA enabled)")
    print("-" * 70)
    has_2fa = input("Do you have 2-Factor Authentication enabled? (y/n): ").strip().lower()
    
    app_password = ""
    if has_2fa == 'y':
        print("\n1. Go to: https://myaccount.google.com/")
        print("2. Click 'Security' → 'App passwords'")
        print("3. Select 'Mail' → 'Mac'")
        print("4. Click 'Generate' and copy the 16-character password")
        app_password = input("\nPaste your app password here (or press Enter to skip): ").strip()
    
    print("\nSTEP 3: Add Gmail to Mac Mail")
    print("-" * 70)
    print("1. Open Mail app")
    print("2. Mail → Settings → Accounts tab")
    print("3. Click '+' button")
    print("4. Select 'Google'")
    print("5. Enter your Gmail address")
    if app_password:
        print(f"6. Enter app password: {app_password}")
    else:
        print("6. Enter your Gmail password")
    print("7. Select what to sync (Mail, Contacts, etc.)")
    print("8. Click 'Done'")
    
    print("\n" + "="*70)
    print("✅ Gmail should now appear in Mac Mail!")
    print("="*70)

def add_icloud_to_gmail():
    """Guide for adding iCloud email to Gmail account"""
    print("\n" + "="*70)
    print("📧 ADDING rsplowman@icloud.com TO GMAIL ACCOUNT")
    print("="*70)
    print("\nThis allows you to use rsplowman@icloud.com when apps")
    print("ask you to 'Sign in with Google' or use Gmail login.")
    
    print("\nSTEP-BY-STEP INSTRUCTIONS:")
    print("-" * 70)
    print("\n1. Go to: https://myaccount.google.com/")
    print("2. Click 'Personal info' in left sidebar")
    print("3. Under 'Contact info', find 'Email'")
    print("4. Click on 'Email'")
    print("5. Click 'Add alternate email' or 'Add email address'")
    print("6. Enter: rsplowman@icloud.com")
    print("7. Click 'Add'")
    print("8. Check rsplowman@icloud.com for verification email")
    print("9. Click the verification link")
    print("10. ✅ Done! You can now use rsplowman@icloud.com for app logins")
    
    print("\n" + "="*70)
    print("HOW TO USE:")
    print("="*70)
    print("\nWhen apps ask 'Sign in with Google':")
    print("  • Enter: rsplowman@icloud.com")
    print("  • Use your Gmail account password (not iCloud password)")
    print("  • Google will recognize it as an alternate email")
    
    print("\n" + "="*70)
    print("⚠️  IMPORTANT:")
    print("="*70)
    print("  • You still use your Gmail password to sign in")
    print("  • This is for account identification, not email forwarding")
    print("  • Some apps may show your primary Gmail address")
    
    print("\n" + "="*70)

def main():
    """Main menu"""
    while True:
        print("\n" + "="*70)
        print("GMAIL + MAC MAIL SETUP")
        print("="*70)
        print("1. Add Gmail to Mac Mail")
        print("2. Add rsplowman@icloud.com to Gmail Account")
        print("3. Both (Complete Setup)")
        print("0. Exit")
        print("="*70)
        
        choice = input("\nSelect option: ").strip()
        
        if choice == "1":
            gmail_macmail_setup()
        elif choice == "2":
            add_icloud_to_gmail()
        elif choice == "3":
            gmail_macmail_setup()
            print("\n")
            add_icloud_to_gmail()
        elif choice == "0":
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid option")
        
        if choice != "0":
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

