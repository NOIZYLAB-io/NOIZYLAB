"""
NoizyTask AI Priority Scoring Engine
====================================
Adaptive priority based on stress, energy, urgency, and context.
"""

from typing import Dict, Optional
from .models import Task, TaskPriority, TaskType
from datetime import datetime, timedelta


def score_priority(
    task: Task,
    mood: str = "neutral",
    energy: float = 1.0,
    stress: str = "low",
    context: Dict = None
) -> TaskPriority:
    """
    Calculate adaptive priority based on user state and context.
    """
    if context is None:
        context = {}
    
    # Start with base priority
    base = task.priority.value if isinstance(task.priority, TaskPriority) else task.priority
    
    # Stress adjustment
    if stress == "high":
        # When stressed, reduce priority of non-critical tasks
        if base < TaskPriority.CRITICAL.value:
            base -= 1
    elif stress == "low":
        # When calm, can handle more
        pass
    
    # Energy adjustment
    if energy < 0.3:
        # Low energy - deprioritize complex tasks
        if task.estimated_minutes and task.estimated_minutes > 30:
            base -= 1
    elif energy > 0.8:
        # High energy - good time for challenging tasks
        if task.task_type in [TaskType.COMPUTE, TaskType.DIAGNOSTIC]:
            base += 1
    
    # Client tasks get boost
    if task.task_type == TaskType.CLIENT or "client" in task.context:
        base += 1
    
    # Urgent context boost
    if context.get("urgent") or "urgent" in task.tags:
        base += 1
    
    # Due date urgency
    if task.due_date:
        due = datetime.fromisoformat(task.due_date)
        hours_until = (due - datetime.now()).total_seconds() / 3600
        
        if hours_until < 1:
            base = TaskPriority.URGENT.value
        elif hours_until < 4:
            base = max(base, TaskPriority.CRITICAL.value)
        elif hours_until < 24:
            base = max(base, TaskPriority.HIGH.value)
    
    # Time of day adjustment
    hour = datetime.now().hour
    if 9 <= hour <= 11:  # Morning peak
        # Good time for high-priority work
        pass
    elif 14 <= hour <= 16:  # Afternoon slump
        if base >= TaskPriority.HIGH.value:
            base -= 1
    
    # Clamp to valid range
    base = max(TaskPriority.LOW.value, min(TaskPriority.URGENT.value, base))
    
    return TaskPriority(base)


def calculate_urgency_score(task: Task) -> float:
    """
    Calculate urgency score (0-1) for a task.
    """
    score = 0.0
    
    # Priority contribution
    priority_weight = {
        TaskPriority.LOW: 0.1,
        TaskPriority.NORMAL: 0.3,
        TaskPriority.HIGH: 0.5,
        TaskPriority.CRITICAL: 0.8,
        TaskPriority.URGENT: 1.0,
    }
    score += priority_weight.get(task.priority, 0.3) * 0.4
    
    # Due date contribution
    if task.due_date:
        due = datetime.fromisoformat(task.due_date)
        hours_until = (due - datetime.now()).total_seconds() / 3600
        
        if hours_until < 0:
            score += 0.4  # Overdue
        elif hours_until < 4:
            score += 0.35
        elif hours_until < 24:
            score += 0.25
        elif hours_until < 72:
            score += 0.15
        else:
            score += 0.05
    
    # Client task boost
    if task.task_type == TaskType.CLIENT:
        score += 0.2
    
    return min(1.0, score)


def should_defer(task: Task, energy: float, stress: str) -> bool:
    """
    Determine if a task should be deferred based on current state.
    """
    # Never defer urgent or critical
    if task.priority in [TaskPriority.URGENT, TaskPriority.CRITICAL]:
        return False
    
    # Defer if very low energy and task is complex
    if energy < 0.2 and task.estimated_minutes and task.estimated_minutes > 30:
        return True
    
    # Defer if high stress and task is not essential
    if stress == "high" and task.priority == TaskPriority.LOW:
        return True
    
    return False


def suggest_optimal_time(task: Task) -> str:
    """
    Suggest optimal time to work on a task.
    """
    # Complex tasks - morning
    if task.estimated_minutes and task.estimated_minutes > 60:
        return "morning (9-11am)"
    
    # Creative tasks - late morning
    if task.task_type == TaskType.PERSONAL:
        return "late morning (10-12pm)"
    
    # Routine tasks - afternoon
    if task.priority == TaskPriority.LOW:
        return "afternoon (2-4pm)"
    
    # Client tasks - business hours
    if task.task_type == TaskType.CLIENT:
        return "business hours (9am-5pm)"
    
    return "any time"


def batch_similar_tasks(tasks: list) -> Dict[str, list]:
    """
    Group similar tasks for batch processing.
    """
    batches = {}
    
    for task in tasks:
        # Group by type
        key = task.task_type.value if isinstance(task.task_type, TaskType) else str(task.task_type)
        
        if key not in batches:
            batches[key] = []
        batches[key].append(task)
    
    return batches

