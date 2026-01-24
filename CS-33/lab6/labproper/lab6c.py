from collections import deque
from collections.abc import  Sequence, Mapping
from dataclasses import dataclass

type Grid = Sequence[str]

INF = 10**18 # very large number but not float

@dataclass
class Edge:
    v: int
    cap: int
    reverse: int

# connect the graphs
def add_edge(u: int, v: int, cap: int, g):
    g[u].append(Edge(v, cap, len(g[v])))
    g[v].append(Edge(u, 0, len(g[u]) - 1))

def max_profit(d: int, ores: Mapping[str, int], quarry: Grid) -> int:
    r: int = len(quarry)
    c: int = len(quarry[0])
    delta: list[tuple[int, int]] = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    cave: list[list[int]] = [[-1] * c for _ in range(r)]
    veins: list[tuple[int, list[tuple[int, int]]]] = []
    veins_id: int = 0

    for i in range(r):
        for j in range(c):
            if cave[i][j] == -1:
                ore = quarry[i][j]
                queue = deque([(i, j)])
                cave[i][j] = veins_id
                cells = [(i, j)]
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in delta:
                        nx, ny = x + dx, y + dy
                        if (
                            0 <= nx < r
                            and 0 <= ny < c
                            and cave[nx][ny] == -1
                            and quarry[nx][ny] == ore
                        ):
                            cave[nx][ny] = veins_id
                            queue.append((nx, ny))
                            cells.append((nx, ny))
                val = ores.get(ore, 0)
                profit = len(cells) * (val - d)
                veins.append((profit, cells))
                veins_id += 1

    # init the graph itself
    n: int = len(veins)
    adj: list[list[int]] = [[] for _ in range(n)]

    # vertical dependencies
    for i in range(n):
        visited_set = set()
        for (x, y) in veins[i][1]:
            if x > 0:
                above_id = cave[x-1][y]
                if above_id != i and above_id not in visited_set:
                    visited_set.add(above_id)
                    adj[i].append(above_id)
                else:
                    continue

    # build flow network
    graph = [[] for _ in range(n + 2)]
    source, sink = n, n + 1
    total = 0

    for i, (p, _) in enumerate(veins):
        if p > 0:
            total += p
            add_edge(source, i, p,graph)
        elif p < 0:
            add_edge(i, sink, -p, graph)

    # connect dependencies (INF capacity)
    for u in range(n):
        for v in adj[u]:
            add_edge(u, v, INF, graph)

    # Do the Dinic’s algorithm
    def bfs():
        level = [-1] * (n + 2)
        level[source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for e in graph[u]:
                if e.cap > 0 and level[e.v] < 0:
                    level[e.v] = level[u] + 1
                    queue.append(e.v)
        return level

    def dfs(u, f):
        if u == sink: return f
        while iteration[u] < len(graph[u]):
            e = graph[u][iteration[u]]
            if e.cap > 0 and level[e.v] == level[u] + 1:
                ret = dfs(e.v, min(f, e.cap))
                if ret > 0:
                    e.cap -= ret
                    graph[e.v][e.reverse].cap += ret
                    return ret
            iteration[u] += 1
        return 0

    max_flow: int = 0
    while 1:
        level = bfs()
        if level[sink] < 0: break
        iteration = [0] * (n + 2) # reset iteration
        while 1:
            ret = dfs(source, INF)
            if ret == 0: break
            max_flow += ret
    return total - max_flow


assert max_profit(10, {
    'A': 8,
    'B': 12,
    'C': 9,
    'D': 30,
}, (
    "ABBC",
    "AABC",
    "AAAC",
    "DCCC",
)) == 14  

assert max_profit(1000, {
    'graph': 1100,
    'G': 1050,
}, (
    "Gg#gG",
    "GgggG",
    "GGGGG",
)) == 0

# assert max_profit(1000, {
#     'a': 1900,
#     'A': 1800,
#     'B': 1800,
#     'x': 980,
#     'X': 990,
#     'y': 1,
#     'b': 1,
#     'r': 33,
#     's': 33,
#     'sink': 33,
#     'u': 33,
#     'v': 33,
# }, (
#     "##ayrXs",
#     "#aatAAA",
#     "#aaxxxx",
#     "#aauBBB",
#     "#bbbvBB",
# )) == 2710

