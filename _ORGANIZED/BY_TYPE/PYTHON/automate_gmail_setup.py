#!/usr/bin/env python3
#!/usr/bin/env python3
"""
Automated Gmail Setup for iCloud Email
This script automates adding rsplowman@icloud.com to Gmail
"""

import time
import sys

try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False

# Configuration
ICLOUD_EMAIL = "rsplowman@icloud.com"
APP_PASSWORD = "bdzw-ekxx-uhxi-pgym"
GMAIL_URL = "https://mail.google.com"

def check_dependencies():
    """Check if required packages are installed"""
    if not SELENIUM_AVAILABLE:
        print("\n" + "="*70)
        print("❌ Selenium is not installed")
        print("="*70)
        print("\nTo install Selenium, run:")
        print("  pip3 install selenium")
        print("\nYou also need ChromeDriver:")
        print("  brew install chromedriver  (on macOS)")
        print("\nOr use the manual setup guide instead.")
        return False
    return True

def setup_chrome_driver():
    """Setup Chrome driver with options"""
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Uncomment to run in background
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    try:
        driver = webdriver.Chrome(options=chrome_options)
        return driver
    except Exception as e:
        print(f"\n❌ Error setting up Chrome driver: {e}")
        print("\nMake sure ChromeDriver is installed:")
        print("  brew install chromedriver")
        return None

def automate_smtp_setup(driver):
    """Automate SMTP (Send Mail As) setup"""
    print("\n" + "="*70)
    print("📤 AUTOMATING: Send Mail As Setup (SMTP)")
    print("="*70)
    
    try:
        # Navigate to Gmail Settings
        print("\n1. Navigating to Gmail Settings...")
        driver.get(f"{GMAIL_URL}/mail/u/0/#settings/accounts")
        time.sleep(3)
        
        # Click "Add another email address" in Send mail as section
        print("2. Looking for 'Add another email address' button...")
        try:
            add_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Add another email address')]"))
            )
            add_button.click()
            time.sleep(2)
        except Exception as e:
            print(f"   ⚠️  Could not find button automatically: {e}")
            print("   Please click 'Add another email address' manually")
            input("   Press Enter when you've clicked it...")
        
        # Enter name and email
        print("3. Entering email address...")
        try:
            name_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "name"))
            )
            name_field.clear()
            name_field.send_keys("Robert Splowman")
            
            email_field = driver.find_element(By.NAME, "email")
            email_field.clear()
            email_field.send_keys(ICLOUD_EMAIL)
            
            next_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Next')]")
            next_button.click()
            time.sleep(2)
        except Exception as e:
            print(f"   ⚠️  Could not fill form automatically: {e}")
            print("   Please enter manually:")
            print(f"     Name: Robert Splowman")
            print(f"     Email: {ICLOUD_EMAIL}")
            input("   Press Enter when done...")
        
        # Enter SMTP settings
        print("4. Entering SMTP settings...")
        try:
            smtp_server = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "smtpServer"))
            )
            smtp_server.clear()
            smtp_server.send_keys("smtp.mail.me.com")
            
            port_field = driver.find_element(By.NAME, "smtpPort")
            port_field.clear()
            port_field.send_keys("587")
            
            username_field = driver.find_element(By.NAME, "smtpUsername")
            username_field.clear()
            username_field.send_keys(ICLOUD_EMAIL)
            
            password_field = driver.find_element(By.NAME, "smtpPassword")
            password_field.clear()
            password_field.send_keys(APP_PASSWORD)
            
            # Select TLS
            tls_option = driver.find_element(By.XPATH, "//input[@value='tls']")
            if not tls_option.is_selected():
                tls_option.click()
            
            add_account_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Add Account')]")
            add_account_button.click()
            time.sleep(3)
            
            print("   ✅ SMTP settings entered!")
            print("   ⚠️  You'll need to verify the email manually")
            
        except Exception as e:
            print(f"   ⚠️  Could not fill SMTP settings automatically: {e}")
            print("   Please enter manually:")
            print(f"     SMTP Server: smtp.mail.me.com")
            print(f"     Port: 587")
            print(f"     Username: {ICLOUD_EMAIL}")
            print(f"     Password: {APP_PASSWORD}")
            print(f"     Security: TLS")
            input("   Press Enter when done...")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error during automation: {e}")
        return False

def main():
    """Main automation function"""
    print("\n" + "="*70)
    print("🤖 AUTOMATED GMAIL SETUP FOR iCLOUD EMAIL")
    print("="*70)
    
    if not check_dependencies():
        return
    
    print("\n⚠️  IMPORTANT:")
    print("   This script will open Chrome browser")
    print("   You need to be logged into Gmail first")
    print("   Some steps may require manual intervention")
    
    proceed = input("\nContinue? (y/n): ").strip().lower()
    if proceed != 'y':
        print("Cancelled.")
        return
    
    driver = setup_chrome_driver()
    if not driver:
        return
    
    try:
        print("\n" + "="*70)
        print("STEP 1: Log into Gmail")
        print("="*70)
        print("\nThe browser will open. Please log into Gmail if not already logged in.")
        driver.get(GMAIL_URL)
        input("\nPress Enter when you're logged into Gmail...")
        
        # Automate SMTP setup (this is the part that works)
        success = automate_smtp_setup(driver)
        
        if success:
            print("\n" + "="*70)
            print("✅ AUTOMATION COMPLETE!")
            print("="*70)
            print("\nNext steps:")
            print("1. Check your iCloud email for verification")
            print("2. Click the verification link")
            print("3. You can now send emails from rsplowman@icloud.com")
            print("\nNote: Receiving emails via POP3 doesn't work with iCloud.")
            print("      Use Mac Mail app for receiving iCloud emails.")
        else:
            print("\n⚠️  Automation had issues. Please complete manually.")
        
        print("\nBrowser will stay open for 30 seconds...")
        time.sleep(30)
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Automation cancelled by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
    finally:
        driver.quit()
        print("\n✅ Browser closed")

if __name__ == "__main__":
    main()

