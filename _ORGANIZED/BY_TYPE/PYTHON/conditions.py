"""NoizyFlow Condition Engine"""
def check_conditions(conditions, state):
    for cond in conditions:
        key = cond["key"]
        op = cond["op"]
        val = cond["value"]
        if op == "eq" and state.get(key) != val:
            return False
        if op == "ne" and state.get(key) == val:
            return False
        if op == "lt" and not (state.get(key, 0) < val):
            return False
        if op == "gt" and not (state.get(key, 0) > val):
            return False
        if op == "le" and not (state.get(key, 0) <= val):
            return False
        if op == "ge" and not (state.get(key, 0) >= val):
            return False
    return True

