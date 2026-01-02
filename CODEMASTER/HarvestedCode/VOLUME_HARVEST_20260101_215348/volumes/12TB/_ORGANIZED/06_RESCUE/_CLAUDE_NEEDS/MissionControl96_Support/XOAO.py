def select_volume():
    while True:
        try:
            vol = int(input("Enter volume (0-100): "))
            if 0 <= vol <= 100:
                print(f"Volume set to {vol}")
                return vol
            else:
                print("Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    select_volume()
