"""NoizyBrain++ - The Main Cognitive Loop"""
from .fusion import fuse_context, extract_priorities, summarize_context
from .planner import plan, get_plan_priority, decompose_plan
from .reflections import reflect, evaluate_reflection
from .intention import form_intention, should_execute
from .thinkers import execute_intention, validate_action
from .router import route_thought
from .cognitive_graph import add_concept, related

class NoizyBrain:
    """The unified reasoning engine"""
    
    def __init__(self):
        self.thought_history = []
        self.intention_queue = []
        self.learning_log = []
    
    def think(self, state, memory=None, events=None):
        """Main cognitive loop"""
        memory = memory or []
        events = events or []
        
        # Build working context
        ctx = fuse_context(state, memory, events)
        priorities = extract_priorities(ctx)
        
        # Plan
        p = plan(ctx)
        plan_priority = get_plan_priority(p)
        steps = decompose_plan(p)
        
        # Reflect
        r = reflect(ctx, p)
        reflection_eval = evaluate_reflection(r, ctx)
        
        # Form intention
        intent = form_intention(p, r)
        
        # Route to appropriate Genius
        routed = route_thought(p)
        
        # Execute if appropriate
        action = None
        if should_execute(intent):
            action = execute_intention(intent)
            if validate_action(action):
                self.intention_queue.append(intent)
        
        # Build thought record
        thought = {
            "context": ctx,
            "context_summary": summarize_context(ctx),
            "priorities": priorities,
            "plan": p,
            "plan_priority": plan_priority,
            "steps": steps,
            "reflection": r,
            "reflection_eval": reflection_eval,
            "intent": intent,
            "routed_to": routed,
            "action": action,
            "executed": action is not None,
        }
        
        # Log thought
        self.thought_history.append(thought)
        if len(self.thought_history) > 100:
            self.thought_history = self.thought_history[-50:]
        
        # Learn associations
        if p and r:
            add_concept(p, r, weight=0.8, relation="leads_to")
        
        return thought
    
    def get_thought_history(self, limit=20):
        return self.thought_history[-limit:]
    
    def get_pending_intentions(self):
        return self.intention_queue
    
    def clear_intentions(self):
        self.intention_queue = []

# Global brain instance
BRAIN = NoizyBrain()

def think(state, memory=None, events=None):
    """Convenience function for global brain"""
    return BRAIN.think(state, memory, events)

def get_brain():
    return BRAIN

