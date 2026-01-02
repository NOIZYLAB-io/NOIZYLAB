
import os
import time
from accounts import list_accounts

def show_dashboard():
	accounts = list_accounts()
	count = len(accounts)
	last_update = time.ctime(os.path.getmtime(os.path.join(os.path.dirname(__file__), 'data', 'account_alignment.csv')))
	print("\n=== NoizyCockPit Dashboard ===")
	print(f"Total Accounts: {count}")
	print(f"Last Update: {last_update}")
	print("============================\n")
