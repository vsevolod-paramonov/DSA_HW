
def has_cycle(graph):
    return find_cycle(graph) is not None

def find_cycle(graph):
    visited = set()
    stack = set()
    path = []

    all_nodes = set(graph)
    for vs in graph.values():
        all_nodes.update(vs)

    def dfs(v):
        visited.add(v)
        stack.add(v)
        path.append(v)
        for u in graph.get(v, []):
            if u not in visited:
                res = dfs(u)
                if res:
                    return res
            elif u in stack:
                cycle_start = path.index(u)
                return path[cycle_start:] + [u]
        stack.remove(v)
        path.pop()
        return None

    for v in all_nodes:
        if v not in visited:
            res = dfs(v)
            if res:
                return res
    return None

def top_sort(graph):
    visited = set()
    on_stack = set()
    order = []

    all_nodes = set(graph)
    for vs in graph.values():
        all_nodes.update(vs)

    def dfs(v):
        if v in on_stack:
            raise ValueError
        if v in visited:
            return
        on_stack.add(v)
        for u in graph.get(v, []):
            dfs(u)
        on_stack.remove(v)
        visited.add(v)
        order.append(v)

    for v in all_nodes:
        if v not in visited:
            dfs(v)
    order.reverse()
    return order