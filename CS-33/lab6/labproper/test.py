# idea:
# 1. augment the path  (traverse the path and update the residual)
# 2. find another path
# 3. augment
from collections.abc import Sequence
from dataclasses import dataclass
from collections import deque
type Wire = tuple[int, int, int]
type Plant = tuple[int, int]

@dataclass
class Edge:
    i: int
    j: int
    cap: int
    flow: int
    res: int
    reverse: "Edge | None"

def augmenting_path(s, t, n):
    visited: list[bool] = [False] * n

    queue = deque()
    queue.append(s)
    
    visited[s] = True
    
    while (queue):
        u = queue.pop()
        
        if visited[u]: continue
        
        if u == t:
            # extract edges
            path = []
            while (u != s):
                path.append()
                

def max_siphoned(n: int, wires: Sequence[Wire], plants: Sequence[Plant], hideouts: Sequence[int]) -> int:
    # 1. Initialize the graph
    # since 1-indexed, we can use 0 as the mega source and n+1th index as the mega sink
    
    mega_source: int = 0
    mega_sink: int = n + 1
    graph: list[list["Edge | None"]] = [[] for _ in range(n + 1) ]
    edges = []
    parent: list[int]= [0] * (n + 1)
    
    for src, dst, amp in wires:
        edges.append(Edge(src, dst, amp, 0,0, None))
        parent[dst] = src
    
    # # connect the mega_source to all the sources with their corresponding weights
    
    # for node, amp in plants:
    #     srcEdge = Edge(mega_source, node, amp, 0, 0)
    #     graph[mega_source].append(srcEdge)
        
    # for node in hideouts:
    #     dstEdge = Edge(node, mega_sink, 100000000,0,0 )
    #     graph[node].append(dstEdge)
    
    
    print(parent)
    # for edge in edges:
    #     edge.reverse = Edge(edge.i, edge.j, 0, 0, 0, edge)
    
    # # 2. Traverse the graph
    # flow = 0 
    # while (path := augmenting_path(mega_source, mega_sink, n)):
    #     # find the smallest residual
    #     bottle_neck = min(list(map(lambda x: x.res, path)))
    #     flow += bottle_neck

    #     for edge in path:
    #         edge.flow += bottle_neck
    #         edge.reverse.flow -= bottle_neck

    # return flow

max_siphoned(6, [
    (2, 1, 40),
    (3, 2, 110),
    (2, 6, 60),
    (4, 6, 50),
    (3, 4, 110),
    (2, 5, 40)
], [
    (3, 200),
], [1, 5, 6])