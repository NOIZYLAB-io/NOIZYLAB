
import csv
import os
from typing import List, Dict

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
        print()

def main():
    write_accounts_to_csv(accounts)
    loaded_accounts = read_accounts_from_csv()
    display_accounts(loaded_accounts)

if __name__ == "__main__":
    main()
