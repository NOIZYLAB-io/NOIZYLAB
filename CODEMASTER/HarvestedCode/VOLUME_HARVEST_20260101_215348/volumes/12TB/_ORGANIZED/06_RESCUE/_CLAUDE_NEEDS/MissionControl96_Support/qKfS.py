def audit_and_standardize_2fa(accounts: List[Dict]) -> None:
    """Standardize the 2FA field for all accounts, including Facebook."""
    valid_2fa = {"none", "sms", "app", "email", "hardware", "enabled"}
    for acc in accounts:
        val = acc.get("2FA", "none").strip().lower()
        if val not in valid_2fa:
            # Try to infer from description
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

    # Microsoft-specific 2FA audit
    for acc in accounts:
        if acc.get("Platform", "").lower() == "microsoft":
            if acc["2FA"] not in ("app", "hardware"):
                acc["2FA Warning"] = "Recommended: Use 'app' or 'hardware' for Microsoft 2FA."
            else:
                acc.pop("2FA Warning", None)

import csv
import os
from typing import List, Dict

import json
import shutil
from datetime import datetime

ACCOUNTS_FILE = "account_alignment.csv"

accounts = [
    {
        "Platform": "Microsoft",
        "Purpose": "Identity, Archive, AI Cockpit",
        "Login Email": "rob@noizy.ai",
        "Recovery": "yes",
        "2FA": "enabled",
        "Linked Accounts": "Copilot, OneDrive, Outlook",
        "Branding Status": "active",
        "Automation": "Copilot",
        "Notes": "Primary backbone"
    },
    {
        "Platform": "Instagram",
        "Purpose": "Visual Drops, Outreach",
        "Login Email": "rob@noizyfish.com",
        "Recovery": "yes",
        "2FA": "enabled",
        "Linked Accounts": "Facebook",
        "Branding Status": "needs update",
        "Automation": "Meta Suite",
        "Notes": "Weekly drops planned"
    },
    # Add more platforms here...
]

def write_accounts_to_csv(accounts: List[Dict], filename: str = ACCOUNTS_FILE) -> None:
    if not accounts:
        print("No accounts to write.")
        return
    fieldnames = accounts[0].keys()
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(accounts)
    print(f"✅ Account alignment grid saved as {filename}")

def backup_csv(filename: str = ACCOUNTS_FILE) -> None:
    if os.path.exists(filename):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"{filename}.bak_{timestamp}"
        shutil.copy(filename, backup_name)
        print(f"Backup created: {backup_name}")

def read_accounts_from_csv(filename: str = ACCOUNTS_FILE) -> List[Dict]:
    if not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        return []
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)

def display_accounts(accounts: List[Dict]) -> None:
    if not accounts:
        print("No accounts to display.")
        return
    for i, account in enumerate(accounts, 1):
        print(f"Account {i}:")
        for key, value in account.items():
            print(f"  {key}: {value}")
        if account.get("Platform", "").lower() == "microsoft" and account.get("2FA Warning"):
            print(f"  ⚠️ 2FA Warning: {account['2FA Warning']}")
        print()


def add_account_interactive(accounts: List[Dict]) -> None:
    print("\nAdd a new account:")
    fields = [
        "Platform", "Purpose", "Login Email", "Recovery", "2FA",
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
        else:
            value = input(f"  {field}: ")
            new_account[field] = value
    # Check for duplicate by Platform + Login Email
    for acc in accounts:
        if acc["Platform"].lower() == new_account["Platform"].lower() and acc["Login Email"].lower() == new_account["Login Email"].lower():
            print("Duplicate account detected! Not adding.")
            return
    accounts.append(new_account)
    print("Account added!\n")

def search_accounts(accounts: List[Dict], keyword: str) -> List[Dict]:
    keyword = keyword.lower()
    return [a for a in accounts if any(keyword in str(v).lower() for v in a.values())]

def main():
    loaded_accounts = read_accounts_from_csv()
    audit_and_standardize_2fa(loaded_accounts)
    while True:
        print("\nAccount Alignment CLI")
        print("1. Display all accounts")
        print("2. Add a new account")
        print("3. Search accounts")
        print("4. Export to JSON")
        print("5. Backup CSV")
        print("6. Save and exit")
        choice = input("Choose an option (1-6): ").strip()
        if choice == "1":
            display_accounts(loaded_accounts)
        elif choice == "2":
            add_account_interactive(loaded_accounts)
            audit_and_standardize_2fa(loaded_accounts)
        elif choice == "3":
            keyword = input("Enter search keyword: ")
            results = search_accounts(loaded_accounts, keyword)
            if results:
                display_accounts(results)
            else:
                print("No matching accounts found.")
        elif choice == "4":
            json_file = ACCOUNTS_FILE.replace('.csv', '.json')
            with open(json_file, 'w') as jf:
                json.dump(loaded_accounts, jf, indent=2)
            print(f"Exported to {json_file}")
        elif choice == "5":
            backup_csv()
        elif choice == "6":
            backup_csv()
            write_accounts_to_csv(loaded_accounts)
            json_file = ACCOUNTS_FILE.replace('.csv', '.json')
            with open(json_file, 'w') as jf:
                json.dump(loaded_accounts, jf, indent=2)
            print(f"Exported to {json_file}")
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
