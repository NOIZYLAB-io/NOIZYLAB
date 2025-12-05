"""
NoizyVision Object Detection
============================
Object detection with confidence scoring.
Placeholder - replace with real model for production.
"""

from typing import List, Dict, Tuple
import numpy as np


# Object categories
OBJECT_CATEGORIES = {
    "electronics": ["laptop", "phone", "tablet", "monitor", "keyboard", "mouse", "headphones"],
    "furniture": ["desk", "chair", "sofa", "table", "bed", "shelf"],
    "tools": ["screwdriver", "wrench", "multimeter", "soldering_iron", "pliers"],
    "people": ["person", "hand", "face"],
    "kitchen": ["cup", "bottle", "plate", "microwave", "refrigerator"],
    "office": ["pen", "notebook", "document", "printer"],
}


def detect_objects(arr: np.ndarray) -> List[Dict]:
    """
    Detect objects in a frame.
    Returns list of detections with bounding boxes and confidence.
    
    Placeholder - replace with ONNX/TensorRT inference.
    """
    detections = []
    
    if not isinstance(arr, np.ndarray) or len(arr) == 0:
        return detections
    
    # Placeholder detections
    placeholder_objects = [
        {"label": "laptop", "confidence": 0.92, "bbox": [50, 50, 300, 250]},
        {"label": "keyboard", "confidence": 0.88, "bbox": [100, 300, 400, 380]},
        {"label": "mouse", "confidence": 0.85, "bbox": [420, 320, 480, 370]},
    ]
    
    return placeholder_objects


def detect_objects_simple(arr: np.ndarray) -> List[str]:
    """
    Simple object detection returning just labels.
    """
    detections = detect_objects(arr)
    return [d["label"] for d in detections]


def filter_by_confidence(detections: List[Dict], threshold: float = 0.5) -> List[Dict]:
    """
    Filter detections by confidence threshold.
    """
    return [d for d in detections if d.get("confidence", 0) >= threshold]


def filter_by_category(detections: List[Dict], category: str) -> List[Dict]:
    """
    Filter detections by category.
    """
    if category not in OBJECT_CATEGORIES:
        return detections
    
    allowed = OBJECT_CATEGORIES[category]
    return [d for d in detections if d.get("label") in allowed]


def get_object_category(label: str) -> str:
    """
    Get category for an object label.
    """
    for category, labels in OBJECT_CATEGORIES.items():
        if label in labels:
            return category
    return "unknown"


def count_objects_by_category(detections: List[Dict]) -> Dict[str, int]:
    """
    Count objects by category.
    """
    counts = {}
    for d in detections:
        category = get_object_category(d.get("label", ""))
        counts[category] = counts.get(category, 0) + 1
    return counts


def get_dominant_object(detections: List[Dict]) -> Optional[Dict]:
    """
    Get the object with highest confidence.
    """
    if not detections:
        return None
    return max(detections, key=lambda d: d.get("confidence", 0))


def calculate_iou(box1: List[int], box2: List[int]) -> float:
    """
    Calculate Intersection over Union for two bounding boxes.
    """
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])
    
    intersection = max(0, x2 - x1) * max(0, y2 - y1)
    
    area1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
    area2 = (box2[2] - box2[0]) * (box2[3] - box2[1])
    
    union = area1 + area2 - intersection
    
    return intersection / union if union > 0 else 0


def non_max_suppression(detections: List[Dict], iou_threshold: float = 0.5) -> List[Dict]:
    """
    Apply non-maximum suppression to remove overlapping detections.
    """
    if not detections:
        return []
    
    # Sort by confidence
    sorted_dets = sorted(detections, key=lambda d: d.get("confidence", 0), reverse=True)
    
    keep = []
    while sorted_dets:
        best = sorted_dets.pop(0)
        keep.append(best)
        
        # Remove overlapping boxes
        sorted_dets = [
            d for d in sorted_dets
            if calculate_iou(best.get("bbox", [0,0,0,0]), d.get("bbox", [0,0,0,0])) < iou_threshold
        ]
    
    return keep

