class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v : v for v in vertices}
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_u] = root_v
            return True
        return False
    

def kruskal(vertices, edges):
    ds = DisjointSet(vertices)
    mst = []
    total_cost = 0

    edges.sort(key=lambda x : x[2])


    for u, v,w in edges:
        if ds.union(u, v):
            mst.append((u,v,w))
            total_cost += w
    print("Edges in MST:")
    for u, v, w in mst:
        print(f"{u} - {v} : {w}")
    
    print('Total MST Cost', total_cost)

vertices = ['A', 'B', 'C', 'D']
edges = [
    ('A', 'B', 1),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 6),
    ('C', 'D', 4)
]

kruskal(vertices, edges)
