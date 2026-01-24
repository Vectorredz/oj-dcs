from collections.abc import Sequence
from heapq import heappop, heappush

def _within_bounds(i: int, j: int, r: int, c: int):
    return True if 0 <= i < r and 0 <= j < c else False

def to_kilimanjaro(M: Sequence[Sequence[int]]) -> int:
    # make edges list
    r, c = len(M), len(M[0])
    n: int = r * c
    dist: list[float] = [float('inf')] * n
    
    edges = []
    coordinates = [(i,j) for i in range(r) for j in range(c)]
    flatten = {coord: idx for idx, coord in enumerate(coordinates) }
    # flatten_back = {idx: coord for idx, coord in enumerate(coordinates) }
    for i in range(r):
        for j in range(c):
            for ni, nj in [(0,1), (-1,0), (1,0)]:
                di, dj = i + ni, j + nj
                if _within_bounds(di, dj, r, c):
                    fatigue_pts = M[di][dj]
                    edges.append((flatten[(i, j)], flatten[(di, dj)], fatigue_pts))
    
    # test dijkstra
    s = 0
    dist[s] = M[0][0]
    heap = [(M[0][0], s)]
    # visited = [False] * n
    adj = [[] for _ in range(n)]
    
    # create adj_list
    for u, v, c in edges:
        adj[u].append((c, v))

    while (heap):
        c, u  = heappop(heap)
        # allow more paths; removed visited to have multiple paths
        if (c != dist[u]): continue
        # if (u == n-1): continue
        for nc, v in adj[u]:
            dc = nc + c
            if (dist[v] > dc):
                dist[v] = dc
                heappush(heap, (dc, v))
    return dist[-1]
    
to_kilimanjaro((
    (0, 0, -2),
    (1, 0, 4),
    (1, 0, 1),
))

