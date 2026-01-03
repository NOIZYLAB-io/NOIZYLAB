#!/usr/bin/env python3
"""
Interactive Step-by-Step Wizard for Adding iCloud Email to Gmail
"""

def print_step(step_num, title, content):
    """Print a formatted step"""
    print("\n" + "="*70)
    print(f"STEP {step_num}: {title}")
    print("="*70)
    for line in content:
        print(line)
    input("\n✅ Press Enter when you've completed this step...")

def main():
    """Main wizard"""
    print("\n" + "="*70)
    print("🚀 INTERACTIVE WIZARD: Add rsplowman@icloud.com to Gmail")
    print("="*70)
    print("\nThis wizard will guide you step-by-step.")
    print("Complete each step, then press Enter to continue.")
    
    input("\nPress Enter to begin...")
    
    # Step 1
    print_step(1, "Open Gmail Settings", [
        "1. Open your web browser",
        "2. Go to: https://mail.google.com",
        "3. Make sure you're logged into Gmail",
        "4. Click the gear icon (⚙️) in top right",
        "5. Click 'See all settings'"
    ])
    
    # Step 2
    print_step(2, "Go to Accounts and Import", [
        "1. Click the 'Accounts and Import' tab",
        "2. Scroll to 'Check mail from other accounts'",
        "3. Click 'Add a mail account'"
    ])
    
    # Step 3
    print_step(3, "Enter Your Email", [
        "1. In the popup, enter: rsplowman@icloud.com",
        "2. Click 'Next'"
    ])
    
    # Step 4
    print_step(4, "Choose IMAP (IMPORTANT!)", [
        "⚠️  CRITICAL: Choose 'Link accounts with Gmailify (IMAP)'",
        "",
        "If you see both options:",
        "  ✅ Choose: 'Link accounts with Gmailify (IMAP)'",
        "  ❌ DO NOT choose: 'Import emails (POP3)'",
        "",
        "Click 'Next' after choosing IMAP"
    ])
    
    # Step 5
    print("\n" + "="*70)
    print("STEP 5: Enter the Correct Settings")
    print("="*70)
    print("\n📋 COPY AND PASTE THESE EXACT VALUES:")
    print("-" * 70)
    print("\nUsername:")
    print("  rsplowman@icloud.com")
    print("\nPassword:")
    print("  bdzw-ekxx-uhxi-pgym")
    print("\nIMAP Server:")
    print("  imap.mail.me.com")
    print("\nPort:")
    print("  993")
    print("\nSecurity:")
    print("  ✅ Check: 'Always use a secure connection (SSL)'")
    print("-" * 70)
    print("\n⚠️  IMPORTANT:")
    print("  • Server MUST be: imap.mail.me.com (NOT mail.icloud.com)")
    print("  • Port MUST be: 993 (NOT 110)")
    print("  • Username MUST be full email: rsplowman@icloud.com")
    print("  • Password MUST be app-specific: bdzw-ekxx-uhxi-pgym")
    input("\n✅ Press Enter when you've entered all settings and clicked 'Add Account'...")
    
    # Step 6
    print("\n" + "="*70)
    print("STEP 6: Set Up Sending (Optional)")
    print("="*70)
    print("\nGmail will ask if you want to send mail as rsplowman@icloud.com")
    print("\nIf you want to send emails from this address:")
    print("  1. Check the box")
    print("  2. Click 'Next'")
    print("  3. Enter your name")
    print("  4. Click 'Next Step'")
    print("\nThen enter SMTP settings:")
    print("  SMTP Server: smtp.mail.me.com")
    print("  Port: 587")
    print("  Username: rsplowman@icloud.com")
    print("  Password: bdzw-ekxx-uhxi-pgym")
    print("  Security: TLS (enabled)")
    print("  5. Click 'Add Account'")
    input("\n✅ Press Enter when done (or if you skipped this step)...")
    
    # Step 7
    print("\n" + "="*70)
    print("STEP 7: Verify Your Email")
    print("="*70)
    print("\nGmail sent a verification email to rsplowman@icloud.com")
    print("\nWhere to check:")
    print("  • Mac Mail app → rsplowman@icloud.com account → Inbox")
    print("  • OR icloud.com/mail → Log in → Check inbox")
    print("\nWhat to do:")
    print("  1. Find the email from Gmail")
    print("  2. Open it")
    print("  3. Click the verification link")
    print("     OR enter the verification code")
    print("\n💡 Tip: Check Spam folder if you don't see it!")
    input("\n✅ Press Enter when you've verified the email...")
    
    # Success
    print("\n" + "="*70)
    print("🎉 SUCCESS! Your iCloud Email is Connected!")
    print("="*70)
    print("\n✅ You can now:")
    print("  • Receive emails from rsplowman@icloud.com in Gmail")
    print("  • Send emails from rsplowman@icloud.com through Gmail")
    print("  • Manage all emails in one place")
    print("\n" + "="*70)
    print("\n🎊 Congratulations! Setup complete!")
    print("="*70)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Wizard cancelled. You can run it again anytime!")
    except Exception as e:
        print(f"\n❌ Error: {e}")

