from dataclasses import dataclass
from collections import deque

@dataclass
class Edge:
    i: int
    j :int 
    idx: int
    
def eulerian_cycle(n: int, edges: list[Edge], start=0):
    assert 0 <= start < n # checks if the starting node is wwihtin bounds
    
    # 1. Initialize the variables: visited, adj
    visited_edges: list[bool] = [False] * len(edges)
    adj: list[list[tuple[int, Edge]]] = [[] for _ in range(n)]
    for edge in edges:
        adj[edge.i].append((edge.j, edge))
        adj[edge.j].append((edge.i, edge))
        
    
    assert all(len(adj[i]) % 2 == 0 for i in range(n)) # checks whether the nodes has an even degrees
    
    # 2. Consume edges: exhaust the edges until no more unvisited edges
    def consume(i: int):
        curr: int = i
        while (adj[curr]):
            j, edge = adj[curr].pop()
            assert 0 <= edge.idx < len(edges)
            if not visited_edges[edge.idx]:
                visited_edges[edge.idx] = True
                curr = j 
                yield curr, edge
        assert curr == i
        
    # 3. considering stack
    considering = deque([(start, None)])
    while considering:
        i, edge = considering.popleft()
        if edge is not None: yield edge
        new_edges = deque(consume(i))
        while new_edges:
            considering.appendleft(new_edges.pop())

    return all(visited_edges)

def eulerian_path(n: int, edges):
    degrees = [0]*n
    # get all the degrees of the node
    for edge in edges:
        degrees[edge.i] += 1
        degrees[edge.j] += 1
    
    bads = [i for i in range(n) if degrees[i] % 2]
    assert len(bads) % 2 == 0
    
    match bads:
        case []:
            return [*eulerian_cycle(n, edges)]
        case [a, b]:
            dummy = Edge(i=a, j=b, idx=len(edges))
            cyc = [*eulerian_cycle(n, [*edges, dummy])]
            idx = cyc.index(dummy)
            return [*cyc[idx+1:], *cyc[:idx]]
        case _:
            return None

edges = [
    Edge(0, 1, 0),
    Edge(1, 2, 1),
    Edge(2, 0, 2),
]
x= eulerian_path(3, edges)
print(list(x))