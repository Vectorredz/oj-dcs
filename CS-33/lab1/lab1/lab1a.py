from collections.abc import Sequence
from heapq import heappop, heappush
type Road = tuple[str, str, int]

class Navigator:
    def __init__(self, roads: Sequence[Road]):
        self.roads = list(roads)
        names: set[str] = set()
        for u, v, _ in self.roads:
            names.add(u); 
            names.add(v)

        self.names = sorted(names)
        self.n = len(self.names)

        self.flatten: dict[str, int] = {name: i for i, name in enumerate(self.names)}
        self.flatten_back: dict[int, str] = {i: name for i, name in enumerate(self.names)}

        self.adj: list[list[tuple[int, int]]] = [[] for _ in range(self.n)]
        for u_name, v_name, w in self.roads:
            u = self.flatten[u_name]; 
            v = self.flatten[v_name]
            self.adj[u].append((v, w))

    def _dijkstra(self, s: int, t: int | None = None):
        INF = float('inf')
        dist: list[float] = [INF] * self.n
        parent: list[tuple[int, int] | None] = [None] * self.n

        dist[s] = 0
        heap: list[tuple[int, int]] = [(0, s)]
        while heap:
            d, u = heappop(heap)
            dist[u] = d
            if d != dist[u]: continue
            if t is not None and u == t: # lair is existent
                break
            for v, w in self.adj[u]:
                parent[v] = (u, w)
                heappush(heap, (d + w, v))
        # print(parent)
        return dist, parent

    def get_shortest_route(self, start: str, lair: str) -> list[Road] | None:
        s = self.flatten[start]
        t = self.flatten[lair]

        dist, parent = self._dijkstra(s, t)
        
        if dist[t] == float('inf'): # unreachable
            return None

        path: list[Road] = []
        cur = t
        while cur != s:
            p = parent[cur]
            if p is None:
                return None  #
            prev, w = p
            path.append((self.flatten_back[prev], self.flatten_back[cur], w))
            cur = prev
        path.reverse()
        return path  

    def get_shortest_route_with_stop(self, start: str, pit_stop: str, lair: str) -> list[Road] | None:
        a = self.get_shortest_route(start, pit_stop)
        b = self.get_shortest_route(pit_stop, lair)
        if a is None or b is None:
            return None
        return a + b
roads = (
        ("screen", "ring", 3),
        ("ring", "pen", 1),
        ("pen", "king", 4),
        ("pen", "screen", 1),
    )
navigator = Navigator(roads)
r1 = navigator.get_shortest_route("screen", "king")
print(r1)