"""AutoImprover: Module Evaluator"""
from datetime import datetime

EVALUATIONS = []
SCORES = {}

def evaluate_module(module_name, metrics=None):
    """Evaluate a module's performance"""
    metrics = metrics or {}
    score = 100
    issues = []
    
    # Check error rate
    if metrics.get("error_rate", 0) > 0.1: score -= 20; issues.append("High error rate")
    # Check latency
    if metrics.get("latency", 0) > 0.5: score -= 15; issues.append("High latency")
    # Check memory usage
    if metrics.get("memory_mb", 0) > 500: score -= 10; issues.append("High memory usage")
    # Check success rate
    if metrics.get("success_rate", 1) < 0.9: score -= 25; issues.append("Low success rate")
    
    evaluation = {"module": module_name, "score": max(0, score), "issues": issues, "metrics": metrics, "evaluated_at": datetime.now().isoformat()}
    EVALUATIONS.append(evaluation)
    SCORES[module_name] = score
    return evaluation

def evaluate_all(modules):
    """Evaluate all modules"""
    return [evaluate_module(m, {}) for m in modules]

def get_worst_modules(limit=5):
    return sorted(SCORES.items(), key=lambda x: x[1])[:limit]

def get_evaluation_history(module_name=None):
    if module_name: return [e for e in EVALUATIONS if e["module"] == module_name]
    return EVALUATIONS[-100:]

