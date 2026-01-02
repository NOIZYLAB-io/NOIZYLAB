import random

def get_slab_mood(temp, pcie_health):
    if temp > 75 or pcie_health == "Failing":
        return "Distressed"
    elif temp < 45 and pcie_health == "Optimal":
        return "Focused"
    else:
        return random.choice(["Reflective", "Charged", "Neutral"])
