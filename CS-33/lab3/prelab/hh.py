from dataclasses import dataclass
from collections import deque

@dataclass
class Edge:
    i: int
    j: int
    idx: int
    
def make_adj(n: int, edges: list[tuple[int, int]]):
    adj: list[list[tuple[int, Edge]]] = [[] for _ in range(n)]
    # create Edge instance per edge
    for idx, edge in enumerate(edges):
        u, v = edge[0], edge[1]
        _edge = Edge(u, v, idx)        
        adj[_edge.i].append((_edge.j, _edge)) 
        adj[_edge.j].append((_edge.i, _edge)) 
    return adj
    
def hh(n: int, edges: list[tuple[int, int]]):
    # 1. make the adj list

    adj = make_adj(n, edges)
    visited_edges = [False] * len(edges)
    
    if not has_eulerian(n, edges): return False
    
    # 2. Consume edges
    
    def consume(i: int):
        curr: int = i
        while adj[curr]:
            j, edge = adj[curr].pop()
            if not visited_edges[edge.idx]:
                curr = j
                visited_edges[edge.idx] = True
                yield curr, edge
    
    start = 0
    considering = deque([(start, None)])
    # 3. Considering
    while considering:
        i, edge = considering.popleft()
        if edge is not None:
            yield edge
        new_edges = deque(consume(i))
        while new_edges:
            considering.appendleft(new_edges.pop())

def has_eulerian(n: int, edges: list[tuple[int, int]]):
    # 1. Traverse over the n with non zero degree
    adj = make_adj(n, edges)
    start = -1
    for i in range(n):
        if len(adj[i]) > 0:
            start = i   
            break

    visited: list[bool] = [False] * n
    
    def dfs(start, adj, visited):    
        visited[start] = True  
        
        for v, edge in adj[start]:
            if not visited[v]:
                dfs(v, adj, visited)
                
    dfs(start, adj, visited)
    odd = 0
    for i in range(n):
        if visited[i] and len(adj[i]) > 0:
            if len(adj[i]) % 2 != 0:
                odd += 1
            continue
        else:
            return False
        
    if odd == 0:
        return True
    elif odd == 2:
        return True
    else:
        return False
    
def eulerian_path(n, edges):
    degs = [0]*n
    for edge in edges:
        degs[edge.i] += 1
        degs[edge.j] += 1

    bads = [i for i in range(n) if degs[i] % 2]
    assert len(bads) % 2 == 0

    match bads:
        case []:
            return [*hh(n, edges)]
        case [a, b]:
            dummy = Edge(i=a, j=b, idx=len(edges))
            cyc = [*hh(n, [*edges, dummy])]
            idx = cyc.index(dummy)
            return [*cyc[idx+1:], *cyc[:idx]]
        case _:
            return None
    
              
edges = [(0, 1), (1, 2), (2, 0)]
n = 3


# assert (3,edges ) == 

# result = list(hh(n, edges))
# print(result)

    