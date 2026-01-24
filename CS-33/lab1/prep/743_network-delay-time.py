# Directed graph
# kth node is the source

from heapq import heappop, heappush
from typing import List

def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    def make_adj_list():
        # directed graph
        adj_list: List[List[tuple[int, tuple[int, int]]]] = [[] for _ in range(1, n+2)]
        for u, v, w in times:
            adj_list[u].append((w, (u,v)))
        return adj_list
    
    adj_list = make_adj_list()
    visited: List[bool] = [False] * (n+1)
    heap = [(0, (k,k))]
    times: list[int] = [-1] * (n+1)

    while (heap):
        time, network = heappop(heap)
        u, v = network
        if (visited[v]): continue
        visited[v] = True
        times[v] = time
        for dt,dn in adj_list[v]:
            du, dv = dn
            if (k == dv): continue
            heappush(heap, (dt + time, dn))
    
    reachable = visited[1:]
    return max(times) if max(times) and all(reachable) else -1

assert networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2
assert networkDelayTime( [[2,1,1],[2,3,1],[3,4,1]], 4, 2) == 2
assert networkDelayTime( [[1,2,1]], 2, 1) == 1
assert networkDelayTime( [[1,2,1]], 2, 2) == -1
assert networkDelayTime([[1,2,1],[2,3,2],[1,3,2]], 3, 1) == 2
networkDelayTime( [[1,2,1]], 2, 2)
assert networkDelayTime([[1,2,1],[2,3,2],[1,3,1]], 3, 2) == -1
