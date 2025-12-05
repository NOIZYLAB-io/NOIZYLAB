"""
NoizyVision Scene Understanding
===============================
Scene classification based on detected objects and context.
"""

from typing import List, Dict, Tuple, Optional


# Scene definitions with associated objects
SCENE_DEFINITIONS = {
    "workstation": {
        "objects": ["laptop", "keyboard", "monitor", "mouse", "desk", "chair"],
        "weight": 1.0,
        "description": "Computer workspace",
    },
    "living_room": {
        "objects": ["sofa", "tv", "couch", "coffee_table", "lamp"],
        "weight": 1.0,
        "description": "Living room area",
    },
    "kitchen": {
        "objects": ["stove", "refrigerator", "microwave", "sink", "counter"],
        "weight": 1.0,
        "description": "Kitchen area",
    },
    "bedroom": {
        "objects": ["bed", "pillow", "lamp", "nightstand", "dresser"],
        "weight": 1.0,
        "description": "Bedroom area",
    },
    "studio": {
        "objects": ["microphone", "speakers", "mixer", "headphones", "audio_interface"],
        "weight": 1.2,  # Higher weight for specialized space
        "description": "Music/recording studio",
    },
    "repair_zone": {
        "objects": ["tools", "screwdriver", "multimeter", "cables", "soldering_iron"],
        "weight": 1.2,
        "description": "Repair/tech workspace",
    },
    "office": {
        "objects": ["desk", "chair", "printer", "document", "pen", "notebook"],
        "weight": 1.0,
        "description": "Office space",
    },
    "outdoor": {
        "objects": ["sky", "tree", "car", "road", "building"],
        "weight": 1.0,
        "description": "Outdoor environment",
    },
}


def scene_from_objects(objects: List[str]) -> str:
    """
    Classify scene based on detected objects.
    """
    scene, _ = classify_scene(objects)
    return scene


def classify_scene(objects: List[str]) -> Tuple[str, float]:
    """
    Classify scene with confidence score.
    """
    if not objects:
        return "unknown", 0.0
    
    best_scene = "unknown"
    best_score = 0.0
    
    objects_lower = [o.lower() for o in objects]
    
    for scene_name, scene_def in SCENE_DEFINITIONS.items():
        scene_objects = scene_def["objects"]
        weight = scene_def["weight"]
        
        # Count matching objects
        matches = sum(1 for obj in objects_lower if obj in scene_objects)
        
        if matches > 0:
            # Score based on match ratio and weight
            score = (matches / len(scene_objects)) * weight
            
            if score > best_score:
                best_score = score
                best_scene = scene_name
    
    return best_scene, min(1.0, best_score)


def get_scene_context(scene: str) -> Dict:
    """
    Get context information for a scene.
    """
    if scene in SCENE_DEFINITIONS:
        return {
            "scene": scene,
            "description": SCENE_DEFINITIONS[scene]["description"],
            "expected_objects": SCENE_DEFINITIONS[scene]["objects"],
        }
    
    return {
        "scene": scene,
        "description": "Unknown scene",
        "expected_objects": [],
    }


def is_restricted_scene(scene: str) -> bool:
    """
    Check if scene is a restricted area.
    """
    restricted = ["repair_zone", "studio", "office"]
    return scene in restricted


def get_scene_recommendations(scene: str) -> List[str]:
    """
    Get recommendations based on scene.
    """
    recommendations = {
        "workstation": ["Check posture", "Take breaks", "Adjust lighting"],
        "studio": ["Check audio levels", "Monitor acoustics", "Backup session"],
        "repair_zone": ["Safety first", "Document work", "Clean workspace"],
        "living_room": ["Relax", "Dim lights for evening"],
        "bedroom": ["Prepare for rest", "Reduce screen time"],
    }
    
    return recommendations.get(scene, [])


def detect_scene_change(previous: str, current: str) -> Optional[Dict]:
    """
    Detect and report scene changes.
    """
    if previous == current:
        return None
    
    return {
        "changed": True,
        "from": previous,
        "to": current,
        "from_context": get_scene_context(previous),
        "to_context": get_scene_context(current),
    }


def get_all_scenes() -> List[str]:
    """
    Get list of all known scenes.
    """
    return list(SCENE_DEFINITIONS.keys())

