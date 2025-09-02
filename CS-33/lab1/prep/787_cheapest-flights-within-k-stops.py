# n cities
# flights as edges

from typing import List
from heapq import heappop, heappush
from collections import deque

def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    # make adjlist
    def make_adj_list():
        adj: list[list[tuple[int, int ,int]]] = [[] for _ in range(n)]
        for flight in flights:
            u, v, w = flight
            # directed
            adj[u].append((w, u, v))
        return adj
    adj = make_adj_list()

    heap: list[tuple[int, int, int]] = [(0,src,src, 0)]
    visited: list[bool] = [False] * n
    dist: list[float | int] = [float('inf')] * n
    
    while (heap):
        w, u, v, ctr = heappop(heap)
        if (v == dst): return w

        if (ctr <= k):
            for dw, du, dv in adj[v]:
                heappush(heap, (dw + w, du, dv, ctr + 1))


    return -1

x = findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1)
# x= findCheapestPrice(5, [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]], 2, 1, 1)
# x = findCheapestPrice(4, [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], 0, 3, 1)
# x = findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1)
print(x)