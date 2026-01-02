import csv

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

def write_accounts_to_csv(accounts, filename="account_alignment.csv"):
    if not accounts:
        print("No accounts to write.")
        return
    fieldnames = accounts[0].keys()
    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(accounts)
    print(f"✅ Account alignment grid saved as {filename}")

if __name__ == "__main__":
    write_accounts_to_csv(accounts)
