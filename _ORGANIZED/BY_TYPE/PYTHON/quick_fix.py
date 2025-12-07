#!/usr/bin/env python3
#!/usr/bin/env python3
"""
Quick Fix for iCloud Gmail Connection Error
"""

print("\n" + "="*70)
print("🔧 FIX: iCloud Gmail Connection Error")
print("="*70)

print("\n❌ PROBLEM:")
print("   Gmail is trying: mail.icloud.com (POP3, Port 110)")
print("   This is WRONG for iCloud!")

print("\n✅ SOLUTION:")
print("   Use IMAP with these correct settings:")

print("\n" + "-"*70)
print("CORRECT SETTINGS:")
print("-"*70)
print("   Server:     imap.mail.me.com")
print("   Port:       993")
print("   Security:   SSL/TLS")
print("   Username:   rsplowman@icloud.com")
print("   Password:   bdzw-ekxx-uhxi-pgym")

print("\n" + "="*70)
print("WHAT TO DO NOW:")
print("="*70)

print("\n1. Click '<< Back' or 'Cancel' in Gmail")
print("2. Look for 'Link accounts with Gmailify (IMAP)' option")
print("3. If you see POP/IMAP choice, choose IMAP")
print("4. Enter these settings:")
print("   • Username: rsplowman@icloud.com")
print("   • Password: bdzw-ekxx-uhxi-pgym")
print("   • Server: imap.mail.me.com")
print("   • Port: 993")
print("   • SSL: Enabled ✅")

print("\n" + "="*70)
print("IF IMAP OPTION NOT AVAILABLE:")
print("="*70)
print("   Change the POP settings to:")
print("   • POP Server: imap.mail.me.com")
print("   • Port: 995 (POP with SSL)")
print("   • Username: rsplowman@icloud.com")
print("   • Password: bdzw-ekxx-uhxi-pgym")
print("   • SSL: Enabled ✅")

print("\n" + "="*70)
print("KEY FIXES:")
print("="*70)
print("   ❌ mail.icloud.com → ✅ imap.mail.me.com")
print("   ❌ Port 110 → ✅ Port 993 (or 995 for POP)")
print("   ❌ Username: rsplowman → ✅ rsplowman@icloud.com")
print("   ❌ No password → ✅ bdzw-ekxx-uhxi-pgym")

print("\n" + "="*70)
print("\n🚀 Go back and try again with the correct settings!")
print("="*70)

