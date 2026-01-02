AUTO_APPROVE = True

def execute_capsule():
    if AUTO_APPROVE:
        run_capsule()
    else:
        confirm = input("Run capsule? (y/n): ")
        if confirm.lower() == 'y':
            run_capsule()

def run_capsule():
    print("Capsule executed!")
    # Add your capsule logic here

# Example usage:
if __name__ == "__main__":
    execute_capsule()
