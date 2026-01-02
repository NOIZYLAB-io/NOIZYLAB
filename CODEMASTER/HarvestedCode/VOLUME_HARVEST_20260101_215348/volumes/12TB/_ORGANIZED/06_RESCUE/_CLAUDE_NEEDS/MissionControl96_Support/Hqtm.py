
import sys
import time

def fire_ascii_art():
    print(r"""
   ____  _            _     _           _   _     _       _   _     _   
  |  _ \| |          | |   | |         | | | |   (_)     | | | |   | |  
  | |_) | | ___   ___| | __| | ___ _ __| |_| |__  _ _ __ | |_| |__ | |_ 
  |  _ <| |/ _ \ / __| |/ _` |/ _ \ '__| __| '_ \| | '_ \| __| '_ \| __|
  | |_) | | (_) | (__| | (_| |  __/ |  | |_| | | | | | | | |_| | | | |_ 
  |____/|_|\___/ \___|_|\__,_|\___|_|   \__|_| |_|_|_| |_|\__|_| |_|\__|
    """
    )
    print("\nWelcome to NoizyCockPit! Hit me with your best shot!\n")

def main_menu():
    print("What would you like to do?")
    print("1. View Dashboard")
    print("2. Manage Accounts")
    print("3. Generate Account CSV")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    return choice

def main():
    fire_ascii_art()
    while True:
        choice = main_menu()
        if choice == '1':
            print("\n[Dashboard] Feature coming soon!\n")
        elif choice == '2':
            print("\n[Accounts] Feature coming soon!\n")
        elif choice == '3':
            print("\n[CSV Generation] Feature coming soon!\n")
        elif choice == '4':
            print("Goodbye! Stay Noizy!")
            time.sleep(1)
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
