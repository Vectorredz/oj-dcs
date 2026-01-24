# Notes
# rooms 1 -> n 
# corridors 1 -> c
# steps
# no self loops
# undirected graph
# multi loops

from heapq import heappop, heappush
from collections.abc import Sequence
type Corridor = tuple[tuple[int, int], int]

def infiltrate(n: int, corridors: Sequence[Corridor], r: Sequence[int], s: int, e: int) -> int | None:
    # make adj list
    adj_list: list[list[tuple[int, int, int]]] = [[] for _ in range(n + 1)]
    for corridor, step in corridors:
        u, v = corridor
        adj_list[u].append((step, u,v))
        adj_list[v].append((step, v,u))
    
    # teleporter
    rn: int = len(r)
    # for i in r:
    #     for j in r:
    #         if (i != j):
    #             adj_list[i].append((0, i, j))
    #             adj_list[j].append((0, j, i))
    
    for i in r:
        adj_list[i].append((0, 0, 0))
        adj_list[0].append((0, 0, i))
                
    # for u in r:
    #     adj[u].append((0, 0))
    #     adj[0].append((u, 0))
                
    dist: list[float | int]  = [float('inf')] * (n + 1)
    visited: list[bool] = [False] * (n+ 1)
    heap: list[tuple[int, int, int]] = [(0, 0, s)]
    
    while (heap):
        step, u, v = heappop(heap)
        if (visited[v]): continue
        
        dist[v] = step
        visited[v] = True
        
        for dstep, du, dv in adj_list[v]:
            heappush(heap, (dstep + step, du, dv))
    
    return dist[e] if dist[e] != float('inf') else None
    
infiltrate(4, [
        ((1, 2), 1),
        ((2, 3), 1),
        ((3, 4), 1),
    ], [1, 3], 1, 4)