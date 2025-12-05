"""NoizyReality++ Spatial Mapping"""
SPATIAL_MAP = {}
ANCHORS = {}

def map_room(room_id, dimensions, objects):
    SPATIAL_MAP[room_id] = {"dimensions": dimensions, "objects": objects}
    return room_id

def add_anchor(anchor_id, room_id, position, label):
    ANCHORS[anchor_id] = {"room": room_id, "position": position, "label": label}

def get_spatial_anchors(room_id=None):
    if room_id:
        return {k: v for k, v in ANCHORS.items() if v["room"] == room_id}
    return ANCHORS

def get_room_map(room_id):
    return SPATIAL_MAP.get(room_id)

