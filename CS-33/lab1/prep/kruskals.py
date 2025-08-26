# add edges until no cycle
from typing import Sequence

class UnionFind:
    def __init__(self, n: int):
        self.parent = [*range(n + 1)]
        self.weight = [1] * (n + 1)
    
    def __getitem__(self, i):
        if (self.parent[i] == i):
            return i
        else:
            self.parent[i] = self.parent[self.parent[i]]
            return self.parent[i]
    def unite(self, i, j):
        if ((i := self[i]) == (j := self[j])):
            return False
        
        if (self.weight[i] > self.weight[j]):
            i, j = j, i
        
        assert self.weight[i] <= self.weight[j]
        
        self.weight[j] += self.weight[i]
        self.parent[i] = j
        return True
    
def _within_bounds(r, c, i, j):
    return True if (0 <= i < r) and (0 <= j < c) else False

def make_edges_list(mountain):
    r, c = len(mountain), len(mountain[0])
    # ((r, c), elevation)
    
    edges: list[tuple[tuple[int, int], int]] = []
    
    coordinates = [
        (i,j) 
        for i in range(r)
        for j in range(c)
    ]
    
    # assign index per coordinate
    coordinates_idx = {coordinate: idx for idx, coordinate in enumerate(coordinates)}
    test =  0
    for i in range(r):
        for j in range(c):
            for nr, nc in [(1,0),(0,1)]:
                dr, dc = i + nr, j + nc
                
                if (_within_bounds(r,c,dr,dc)):
                    elevation = abs(mountain[dr][dc] - mountain[i][j])
                    # flatten the grid as a graph
                    # (i,j) -- (dr, dc)
                    u, v = coordinates_idx[(i,j)], coordinates_idx[(dr,dc)]
                    edges.append(((u, v), elevation))
                
    return edges

# Kruskals    
def min_ladders(mountain: Sequence[Sequence[int]]) -> int:
    # construct edges out of the mountain
    edges = sorted(make_edges_list(mountain), key=lambda x: x[1])
    vertices = len(mountain) * len(mountain[0])
    mst = []
    same_height = 0

    # try kruskals
    
    rem_edges = [(edge, w) for edge, w in edges if w != 0]
    zero_edges = [(edge, w) for edge, w in edges if w == 0]
    components = UnionFind(vertices)
    
    # First pass: connect the edges with 0 elevation
    for pair, elevation in zero_edges:
        u, v = pair
        if (elevation == 0 and components.unite(u, v)):
            same_height += 1
            
    # Second pass: connect the remaining edges 
    for pair, elevation in rem_edges:
        u, v = pair
        if (components.unite(u, v)):
            mst.append((u,v))
    
    return len(mst)

# # Reverse-delete

def make_adjacency_list(edges, n):
    adj_list = [[] for _ in range(n)]
    for pair, w in edges:
        u, v = pair
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    return adj_list

def min_ladders(edges):
    # sort heavy → light
    n = len(edges) * len(edges[0])
    edges = sorted(make_edges_list(edges), key=lambda x: x[1], reverse=True)
    mst = edges[:]  # start with full graph
    
    for edge in edges:
        mst.remove(edge)
        adj_list = make_adjacency_list(mst, n)
        if not connected(adj_list, n):
            mst.append(edge) 
    
    return len(mst), mst


def connected(adj_list, n):

    # count num of components
    components = []
    stack = []
    visited = [False] * n 
    def dfs(src):
        component = []
        if (not visited[src]):
            stack.append(src)
            visited[src] = True
            
        while (stack):
            node = stack.pop()
            component.append(node)
            for vertex in adj_list[node]:
                if (not visited[vertex]):
                    stack.append(vertex)
                    visited[vertex] = True
        
        return component
    
    for i in range(len(adj_list)):
        components.append(dfs(i))
    
    return True if len(list(filter(lambda x: len(x) > 0, components))) == 1 else False
        
print(min_ladders([
    [1, 2, 2],
    [3, 2, 5],
    [4, 5, 5]
]))
# assert min_ladders([
#     [2, 1, 2],
#     [2, 1, 2],
#     [2, 2, 2]
# ]) == 1
# assert min_ladders([
#     [2, 2, 2],
#     [2, 1, 2],
#     [2, 2, 2]
# ]) == 1

# assert min_ladders([
#     [2, 1, 2],
#     [2, 1, 2],
#     [2, 2, 2]
# ]) == 1

# assert min_ladders([
#     [1, 2, 2],
#     [3, 2, 5],
#     [4, 5, 5]
# ]) == 4