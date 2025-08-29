from collections.abc import Sequence
from heapq import heappop, heappush
type Road = tuple[str, str, int]

class Navigator:
    def __init__(self, roads: Sequence[Road]):
        self.roads = roads
        names: set[str] = set()
        for road in self.roads:
            names.add(road[0])
            names.add(road[1])
            
        self.names = sorted(names)
        self.n = len(self.names)
        
        self.adj: list[list[tuple[int, int]]] = [[] for _ in range(self.n)]
        
        self.flatten: dict[str, int] = {name: idx for idx, name in enumerate(self.names)}
        self.flatten_back: dict[int, str] = {idx: name for idx, name in enumerate(self.names)}
        self.weights: dict[tuple[int, int], int] = {(self.flatten[road[0]], self.flatten[road[1]]): road[2] for road in self.roads}
        for u_name, v_name, w in self.roads:
            u, v, c = self.flatten[u_name], self.flatten[v_name], w
            self.adj[u].append((v, c)) 
        
        super().__init__()

    def get_shortest_route(self, start: str, lair: str) -> list[Road] | None:
        s = self.flatten[start]
        t = self.flatten[lair]
        
        heap: list[tuple[int, int]] = [(0, s)]  # (cost, u)
        dist: list[float | int] = [float('inf')] * self.n
        parents: list[tuple[int, int] | None] = [None] * self.n

        dist[s] = 0
        while heap:
            c, u = heappop(heap)

            if c != dist[u]:
                continue
            if u == t:  # early stop
                break

            for v, dc in self.adj[u]:
                if dc + c < dist[v]:
                    dist[v] = dc + c
                    parents[v] = (u, dc)
                    heappush(heap, (dc + c, v))

        # reconstruct path
        path: list[tuple[int, int, int]] = []
        def dfs(curr) -> list[tuple[str, str, int]] | None:
            if curr == s:
                return []
            if parents[curr] is None:
                return None
            par, c = parents[curr]
            subpath = dfs(par)
            if subpath is None:
                return None
            subpath.append((self.flatten_back[par], self.flatten_back[curr], c))
            return subpath
        
        if parents[t] is None:
            return None
        path = dfs(t, [])
        if path is None: return None
        
        path.reverse()
        # print(path)
        return path
                    
        
    def get_shortest_route_with_stop(self, start: str, pit_stop: str, lair: str) -> list[Road] | None:
        a = self.get_shortest_route(start, pit_stop)
        b = self.get_shortest_route(pit_stop, lair)
        
        if a is None or b is None: return None
        # assert a
        # assert b
        return a + b
roads = (
        ("screen", "ring", 3),
        ("ring", "pen", 1),
        ("pen", "king", 4),
        ("pen", "screen", 1),
    )
navigator = Navigator(roads)
r2 = navigator.get_shortest_route_with_stop("ring", "screen", "king")
print(r2)