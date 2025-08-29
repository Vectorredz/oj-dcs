from collections.abc import Sequence
from heapq import heappop, heappush

def _within_bounds(i: int, j: int, r: int, c: int):
    return 0 <= i < r and 0 <= j < c

def to_kilimanjaro(M: Sequence[Sequence[int]]) -> int:
    r, c = len(M), len(M[0])
    n = r * c
    dist = [float('inf')] * n

    # flatten grid coords → index
    coordinates = [(i, j) for i in range(r) for j in range(c)]
    flatten = {coord: idx for idx, coord in enumerate(coordinates)}

    # start at (0,0)
    s = 0
    dist[s] = M[0][0]
    heap = [(M[0][0], s)]

    dirs = [(0, 1), (1, 0), (-1, 0)]

    while heap:
        cost, u = heappop(heap)
        if cost > dist[u]:
            continue
        if u == n - 1:
            continue
        # no adj list
        i, j = coordinates[u]
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if _within_bounds(ni, nj, r, c):
                v = flatten[(ni, nj)]
                nc = cost + M[ni][nj]
                if nc < dist[v]:
                    dist[v] = nc
                    heappush(heap, (nc, v))

    return dist[-1]

# test
assert to_kilimanjaro((
    (1, -2),
    (0,  3),
)) == 2
