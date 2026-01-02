import sys

def select_volume(default=None):
    if len(sys.argv) > 1:
        try:
            vol = int(sys.argv[1])
            if 0 <= vol <= 100:
                print(f"Volume set to {vol}")
                return vol
            else:
                print("Please enter a number between 0 and 100.")
                return select_volume(default)
        except ValueError:
            print("Invalid input. Please enter a number.")
            return select_volume(default)
    while True:
        try:
            prompt = f"Enter volume (0-100){' [' + str(default) + ']' if default is not None else ''}: "
            inp = input(prompt)
            vol = int(inp) if inp else default
            if vol is not None and 0 <= vol <= 100:
                print(f"Volume set to {vol}")
                return vol
            else:
                print("Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    select_volume(default=50)




