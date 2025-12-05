import json, os

FLAGS_FILE = "./first_run/init_flags.json"


class NoizyWizard:
    def __init__(self):
        if not os.path.exists(FLAGS_FILE):
            json.dump({"completed": False}, open(FLAGS_FILE, "w"))

    def needs_setup(self):
        flags = json.load(open(FLAGS_FILE))
        return not flags.get("completed", False)

    def run(self):
        print("Welcome to NoizyOS Ultra!")
        print("Let's get your system tuned and ready.")

        name = input("Your name: ")
        business = input("Business name (optional): ")

        json.dump({
            "completed": True,
            "user": name,
            "business": business
        }, open(FLAGS_FILE, "w"))

        print("Setup complete. Launching NoizyOS Ultra…")

