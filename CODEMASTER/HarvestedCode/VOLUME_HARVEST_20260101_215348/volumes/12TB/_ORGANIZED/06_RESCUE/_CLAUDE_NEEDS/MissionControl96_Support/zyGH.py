
from typing import List, Dict

ACCOUNTS_FILE = "account_alignment.csv"

# --- Agent Classes ---
class AccountManager:
            def __init__(self, filename=ACCOUNTS_FILE):
                self.filename = filename
                self.accounts = self.read_accounts_from_csv()

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
