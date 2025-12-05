"""NoizyCore Avatar Bridge - Maps state to avatar mode"""
def avatar_mode_from_state(state):
    if state.get("threat", 0) > 0.5: return "alert"
    if state.get("stress", 0) > 0.7: return "calm"
    if state.get("compute", 0) > 0.6: return "focused"
    if state.get("energy", 0) > 0.8: return "happy"
    return "neutral"

def get_avatar_config(state, identity="rob"):
    return {"mode": avatar_mode_from_state(state), "identity": identity, "model": f"noizy_{avatar_mode_from_state(state)}.glb"}

