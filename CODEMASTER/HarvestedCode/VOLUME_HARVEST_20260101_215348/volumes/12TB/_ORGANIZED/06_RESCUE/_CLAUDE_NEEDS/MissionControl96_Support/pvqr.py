

import os
import csv
import json
import shutil
from datetime import datetime
from typing import List, Dict

ACCOUNTS_FILE = "account_alignment.csv"

# --- Agent Classes ---

class AccountManager:
    def add_account_interactive(self):
        print("\nAdd a new account:")
        fields = [
            "Platform", "Purpose", "Login Email", "Primary Email", "Secondary Email", "Recovery", "2FA",
            "Linked Accounts", "Branding Status", "Automation", "Notes"
        ]
        new_account = {}
        for field in fields:
            if field == "2FA":
                print("  2FA options: [none, sms, app, email, hardware, enabled]")
                value = input("  2FA (choose or describe): ").strip().lower()
                valid_2fa = {"none", "sms", "app", "email", "hardware", "enabled"}
                if value not in valid_2fa:
                    print("  Invalid 2FA option. Defaulting to 'none'.")
                    value = "none"
                new_account[field] = value
            elif field == "Primary Email":
                value = input(f"  Primary Email (default: rp@fishmusicinc.com): ").strip()
                if not value:
                    value = "rp@fishmusicinc.com"
                new_account[field] = value
            elif field == "Secondary Email":
                value = input(f"  Secondary Email (default: rsplowman@icloud.com): ").strip()
                if not value:
                    value = "rsplowman@icloud.com"
                new_account[field] = value
            else:
                value = input(f"  {field}: ")
                new_account[field] = value
        # Check for duplicate by Platform + Login Email
        for acc in self.accounts:
            if acc["Platform"].lower() == new_account["Platform"].lower() and acc["Login Email"].lower() == new_account["Login Email"].lower():
                print("Duplicate account detected! Not adding.")
                return
        self.accounts.append(new_account)
        print("Account added!\n")
    def __init__(self, filename=ACCOUNTS_FILE):
        self.filename = filename
        self.accounts = self.read_accounts_from_csv()
        # Add default Microsoft accounts if not present
        ms_emails = [
            ("rp@fishmusicinc.com", "rsplowman@icloud.com"),
            ("rsplowman@icloud.com", "rp@fishmusicinc.com")
        ]
        for primary, secondary in ms_emails:
            exists = any(
                acc.get("Platform", "").lower() == "microsoft" and acc.get("Primary Email", "").lower() == primary
                for acc in self.accounts
            )
            if not exists:
                self.accounts.append({
                    "Platform": "Microsoft",
                    "Purpose": "Identity, Archive, AI Cockpit",
                    "Login Email": primary,
                    "Primary Email": primary,
                    "Secondary Email": secondary,
                    "Recovery": "yes",
                    "2FA": "app",
                    "Linked Accounts": "Copilot, OneDrive, Outlook",
                    "Branding Status": "active",
                    "Automation": "Copilot",
                    "Notes": "Auto-added for legacy and current MS identity"
                })

    def read_accounts_from_csv(self) -> List[Dict]:
        if not os.path.exists(self.filename):
            print(f"File {self.filename} does not exist.")
            return []
        with open(self.filename, "r", newline="") as file:
            reader = csv.DictReader(file)
            return list(reader)

    def write_accounts_to_csv(self):
        if not self.accounts:
            print("No accounts to write.")
            return
        fieldnames = self.accounts[0].keys()
        with open(self.filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.accounts)
        print(f"✅ Account alignment grid saved as {self.filename}")


class SecurityAgent:
    @staticmethod
    def audit_and_standardize_2fa(accounts: List[Dict]) -> None:
        valid_2fa = {"none", "sms", "app", "email", "hardware", "enabled"}
        best_practices = {
            "microsoft": {"app", "hardware"},
            "facebook": {"app", "hardware"},
            "instagram": {"app", "hardware"},
            "google": {"app", "hardware"},
            "apple": {"app", "hardware"},
            "twitter": {"app", "hardware"},
            "dropbox": {"app", "hardware"},
            "github": {"app", "hardware"},
            "slack": {"app", "hardware"},
        }
        for acc in accounts:
            val = acc.get("2FA", "none").strip().lower()
            if val not in valid_2fa:
                if "auth" in val or "app" in val:
                    acc["2FA"] = "app"
                elif "sms" in val:
                    acc["2FA"] = "sms"
                elif "email" in val:
                    acc["2FA"] = "email"
                elif "hardware" in val:
                    acc["2FA"] = "hardware"
                elif val in ("yes", "on", "active", "enabled"):
                    acc["2FA"] = "enabled"
                else:
                    acc["2FA"] = "none"
            else:
                acc["2FA"] = val
            platform = acc.get("Platform", "").lower()
            if platform in best_practices:
                if acc["2FA"] not in best_practices[platform]:
                    acc["2FA Warning"] = f"Recommended: Use 'app' or 'hardware' for {platform.title()} 2FA."
                else:
                    acc.pop("2FA Warning", None)
            else:
                acc.pop("2FA Warning", None)


class BackupAgent:
    @staticmethod
    def backup_csv(filename: str = ACCOUNTS_FILE) -> None:
        if os.path.exists(filename):
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"{filename}.bak_{timestamp}"
            shutil.copy(filename, backup_name)
            print(f"Backup created: {backup_name}")


# Placeholder for future cloud sync agent
class CloudSyncAgent:
    @staticmethod
    def sync_to_google_drive(filename: str):
        print(f"[CloudSyncAgent] Would sync {filename} to Google Drive here.")
        # Integration code goes here

# Placeholder for future notification agent
class NotificationAgent:
    @staticmethod
    def notify(message: str):
        print(f"[NotificationAgent] {message}")

                for acc in accounts:
                    val = acc.get("2FA", "none").strip().lower()
                    if val not in valid_2fa:
                        if "auth" in val or "app" in val:
                            acc["2FA"] = "app"
                        elif "sms" in val:
                            acc["2FA"] = "sms"
                        elif "email" in val:
                            acc["2FA"] = "email"
                        elif "hardware" in val:
                            acc["2FA"] = "hardware"
                        elif val in ("yes", "on", "active", "enabled"):
                            acc["2FA"] = "enabled"
                        else:
                            acc["2FA"] = "none"
                    else:
                        acc["2FA"] = val
                    platform = acc.get("Platform", "").lower()
                    if platform in best_practices:
                        if acc["2FA"] not in best_practices[platform]:
                            acc["2FA Warning"] = f"Recommended: Use 'app' or 'hardware' for {platform.title()} 2FA."
                        else:
                            acc.pop("2FA Warning", None)
                    else:
                        acc.pop("2FA Warning", None)

        class BackupAgent:
            @staticmethod
            def backup_csv(filename: str = ACCOUNTS_FILE) -> None:
                if os.path.exists(filename):
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    backup_name = f"{filename}.bak_{timestamp}"
                    shutil.copy(filename, backup_name)
                    print(f"Backup created: {backup_name}")

        # Placeholder for future cloud sync agent
        class CloudSyncAgent:
            @staticmethod
            def sync_to_google_drive(filename: str):
                print(f"[CloudSyncAgent] Would sync {filename} to Google Drive here.")
                # Integration code goes here

        # Placeholder for future notification agent
        class NotificationAgent:
            @staticmethod
            def notify(message: str):
                print(f"[NotificationAgent] {message}")

        def main():
            manager = AccountManager()
            SecurityAgent.audit_and_standardize_2fa(manager.accounts)
            while True:
                print("\nAccount Alignment CLI")
                print("1. Display all accounts")
                print("2. Add a new account")
                print("3. Search accounts")
                print("4. Export to JSON")
                print("5. Backup CSV")
                print("6. Sync to Google Drive")
                print("7. Save and exit")
                choice = input("Choose an option (1-7): ").strip()
                if choice == "1":
                    manager.display_accounts()
                elif choice == "2":
                    manager.add_account_interactive()
                    SecurityAgent.audit_and_standardize_2fa(manager.accounts)
                elif choice == "3":
                    keyword = input("Enter search keyword: ")
                    results = manager.search_accounts(keyword)
                    if results:
                        manager.display_accounts()
                    else:
                        print("No matching accounts found.")
                elif choice == "4":
                    manager.export_to_json()
                elif choice == "5":
                    BackupAgent.backup_csv(manager.filename)
                elif choice == "6":
                    CloudSyncAgent.sync_to_google_drive(manager.filename)
                elif choice == "7":
                    BackupAgent.backup_csv(manager.filename)
                    manager.write_accounts_to_csv()
                    manager.export_to_json()
                    CloudSyncAgent.sync_to_google_drive(manager.filename)
                    NotificationAgent.notify("Accounts saved and synced.")
                    print("Goodbye!")
                    break
                else:
                    print("Invalid option. Please try again.")
