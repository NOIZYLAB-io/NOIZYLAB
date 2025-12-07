"""NoizyBrain++ Cognitive Graph - Memory + Logic + Associations"""
GRAPH = {}

def add_concept(a, b, weight=1.0, relation="related"):
    GRAPH.setdefault(a, {})[b] = {"weight": weight, "relation": relation}
    GRAPH.setdefault(b, {})[a] = {"weight": weight, "relation": relation}

def related(a, min_weight=0.0):
    connections = GRAPH.get(a, {})
    return {k: v for k, v in connections.items() if v["weight"] >= min_weight}

def get_graph():
    return GRAPH

def find_path(start, end, max_depth=5):
    if start == end: return [start]
    visited = set()
    queue = [(start, [start])]
    while queue and len(queue[0][1]) <= max_depth:
        node, path = queue.pop(0)
        if node in visited: continue
        visited.add(node)
        for neighbor in GRAPH.get(node, {}):
            if neighbor == end: return path + [neighbor]
            queue.append((neighbor, path + [neighbor]))
    return None

def get_cluster(node, depth=2):
    cluster = set([node])
    frontier = [node]
    for _ in range(depth):
        new_frontier = []
        for n in frontier:
            for neighbor in GRAPH.get(n, {}):
                if neighbor not in cluster:
                    cluster.add(neighbor)
                    new_frontier.append(neighbor)
        frontier = new_frontier
    return list(cluster)

def strengthen(a, b, delta=0.1):
    if a in GRAPH and b in GRAPH[a]:
        GRAPH[a][b]["weight"] = min(1.0, GRAPH[a][b]["weight"] + delta)
        GRAPH[b][a]["weight"] = min(1.0, GRAPH[b][a]["weight"] + delta)

