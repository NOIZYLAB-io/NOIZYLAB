"""NoizyHeart++ Relationship Memory"""
RELATIONSHIPS = {"rob": {"trust": 1.0, "familiarity": 1.0, "interactions": 9999, "preferences": {"humor": True, "direct": True, "technical": True}}}

def get_relationship(user_id="rob"):
    return RELATIONSHIPS.get(user_id, {"trust": 0.5, "familiarity": 0.0, "interactions": 0})

def update_relationship(user_id, trust_delta=0, interaction=True):
    if user_id not in RELATIONSHIPS:
        RELATIONSHIPS[user_id] = {"trust": 0.5, "familiarity": 0.0, "interactions": 0, "preferences": {}}
    RELATIONSHIPS[user_id]["trust"] = min(1.0, max(0.0, RELATIONSHIPS[user_id]["trust"] + trust_delta))
    if interaction:
        RELATIONSHIPS[user_id]["interactions"] += 1
        RELATIONSHIPS[user_id]["familiarity"] = min(1.0, RELATIONSHIPS[user_id]["interactions"] / 100)
    return RELATIONSHIPS[user_id]

