
def find_connected_components(graph):
    all_nodes = set(graph.keys())
    for adj in graph.values():
        all_nodes.update(adj)
    visited = set()
    components = []
    
    for vertex in all_nodes:
        if vertex not in visited:
            comp = []
            stack = [vertex]
            while stack:
                v = stack.pop()
                if v not in visited:
                    visited.add(v)
                    comp.append(v)
                    stack.extend(graph.get(v, []))
            components.append(comp)
    return components