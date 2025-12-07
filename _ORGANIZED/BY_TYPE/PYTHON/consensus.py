"""NoizySync++ Consensus Layer - Multi-node agreement"""
PENDING_ACTIONS = {}
VOTES = {}

def propose_action(action_id, action, proposer):
    PENDING_ACTIONS[action_id] = {"action": action, "proposer": proposer, "votes": {proposer: True}}
    return action_id

def vote(action_id, node_id, approve):
    if action_id in PENDING_ACTIONS:
        PENDING_ACTIONS[action_id]["votes"][node_id] = approve

def get_consensus(action_id, required_votes=2):
    if action_id not in PENDING_ACTIONS:
        return None
    votes = PENDING_ACTIONS[action_id]["votes"]
    approvals = sum(1 for v in votes.values() if v)
    return approvals >= required_votes

def execute_if_consensus(action_id, required=2):
    if get_consensus(action_id, required):
        return PENDING_ACTIONS.pop(action_id)["action"]
    return None

