import heapq

def prims_mst(graph, start):
    visited = set()
    min_heap = [(0, start)]
    total_cost = 0

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if u in visited:
            continue

        visited.add(u)
        total_cost += weight
        print(f"Include edge with weight {weight} to node {u}")
        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(min_heap, (w, v))
    print("Total MST cost: ", total_cost)


graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}

prims_mst(graph, 'A')
