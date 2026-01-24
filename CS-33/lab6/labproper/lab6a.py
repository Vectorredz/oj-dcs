from collections import deque
from collections.abc import Sequence
from dataclasses import dataclass

type Wire = tuple[int, int, int]
type Plant = tuple[int, int]

@dataclass
class Edge:
    i: int
    j: int
    cap: int
    flow: int
    reverse: "Edge | None" = None

    @property
    def res(self):
        return self.cap - self.flow


def levelling(s, t, graph, level):
    for i in range(len(level)): level[i] = -1
    queue = deque([s])
    level[s] = 0
    while queue:
        u = queue.popleft()
        for e in graph[u]:
            if e.res > 0 and level[e.j] == -1:
                level[e.j] = level[u] + 1
                queue.append(e.j)
    return level[t] != -1


def accumulate_flow(s, t, f, graph, level, it_ptr):
    stack = [(s, f, [])]  
    total_flow = 0
    while stack:
        u, avail, path = stack.pop()
        if u == t:
            pushed = avail
            for e in path:
                e.flow += pushed
                e.reverse.flow -= pushed
            total_flow += pushed
            continue

        while it_ptr[u] < len(graph[u]):
            e = graph[u][it_ptr[u]]
            it_ptr[u] += 1
            if e.res > 0 and level[e.j] == level[u] + 1:
                pushed = min(avail, e.res)
                stack.append((u, avail - pushed, path))
                stack.append((e.j, pushed, path + [e]))
                break

    return total_flow


def max_siphoned(n: int, wires: Sequence[Wire], plants: Sequence[Plant], hideouts: Sequence[int]) -> int:
    mega_source: int = 0
    mega_sink: int = n + 1
    graph = [[] for _ in range(n + 2)]

    # normal edges
    for src, dst, amp in wires:
        edgeu = Edge(src, dst, amp, 0)
        edgev = Edge(dst, src, 0, 0)
        edgeu.reverse = edgev
        edgev.reverse = edgeu
        graph[src].append(edgeu)
        graph[dst].append(edgev)

    # source connections
    for node, amp in plants:
        edgeu = Edge(mega_source, node, amp, 0)
        edgev = Edge(node, mega_source, 0, 0)
        edgeu.reverse = edgev
        edgev.reverse = edgeu
        graph[mega_source].append(edgeu)
        graph[node].append(edgev)

    # sink connections
    for node in hideouts:
        edgeu = Edge(node, mega_sink, 10**9, 0)
        edgev = Edge(mega_sink, node, 0, 0)
        edgeu.reverse = edgev
        edgev.reverse = edgeu
        graph[node].append(edgeu)
        graph[mega_sink].append(edgev)

    max_flow: int = 0
    level = [-1] * (n + 2)

    while levelling(mega_source, mega_sink, graph, level):
        it_ptr = [0] * (n + 2)
        while True:
            accum = accumulate_flow(mega_source, mega_sink, 10**9, graph, level, it_ptr)
            if accum == 0:
                break
            max_flow += accum

    return max_flow


# tests
assert max_siphoned(6, [
    (2, 1, 40),
    (3, 2, 110),
    (2, 6, 60),
    (4, 6, 50),
    (3, 4, 110),
    (2, 5, 40)
], [
    (3, 200),
], [1, 5, 6]) == 160

assert max_siphoned(10, [
    (2, 6, 100),
    (9, 8, 150),
    (6, 9, 100),
    (6, 3, 30),
    (6, 1, 20),
    (8, 4, 100),
    (9, 7, 200),
    (10, 9, 100),
    (8, 5, 100),
    (8, 6, 200)
], [
    (2, 100),
    (10, 90),
], [3, 4, 5]) == 180
