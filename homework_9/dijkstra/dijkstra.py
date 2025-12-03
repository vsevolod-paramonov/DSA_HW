
import heapq

def dijkstra(graph, start):
    dist = {v: float('inf') for v in graph}
    if start not in dist:
        if not graph:
            return {start: 0}
        dist[start] = 0
    dist[start] = 0
    heap = [(0, start)]
    visited = set()

    while heap:
        _, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)

        for v, w in graph.get(u, {}).items():
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist