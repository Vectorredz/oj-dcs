from heapq import heappop, heappush

class BizarreBuilding:
    
    def __init__(self, n: int, x: int, c: int, y: int, d: int, e: int, f: int):
        self.n = n # n floors 
        
        # button 1
        self.x = x # x floors above 
        self.c = c # c cost
        
        # button 2
        self.y = y # y floors lower
        self.d = d # d cost 
        
        # button 3
        self.e = e # 1 floor higher cost f
        
        # button 4
        self.f = f # 1 floor lower cost f
        
        # create edges for each floors
        self.edges = []
        for u in range(n):
            # connect the nodes to an edge
            for du, nc in [(x, c), (-y, d), (1,e), (-1,f)]:
                # new possible floor
                v = u + du
                dc = nc
                if (self._within_bounds(n, v)):
                    self.edges.append((u, v, dc))
        
        # make adjacency list
        self.adj = [[] for _ in range(n)]
        for u, v, c in self.edges:
            self.adj[u].append((v, c))  
        
        super().__init__()

    def shortest_escape_time(self, s: int, t: int) -> int:
        # apply dijkstra on the edges
        visited: list[bool] = [False] * self.n
        dist: list[float | int] = [float('inf')] * self.n
        heap = [(0, s)]
        
        dist[s] = 0
        while (heap):
            c, u = heappop(heap)
            if (visited[u]): continue
            
            visited[u] = True
            
            for v, dc in self.adj[u]:
                # relaxation
                if (dist[v] > c + dc):
                    dist[v] = c + dc
                    heappush(heap, (c + dc, v))
        
        return dist[t] if dist[t] != float('inf') else -1
    
    def _within_bounds(self, n: int, i: int):
        return True if 0 <= i < n else False

bizarre_building = BizarreBuilding(10, 1, 5, 3, 7, 6, 6)
assert bizarre_building.shortest_escape_time(3, 2) == 6
assert bizarre_building.shortest_escape_time(0, 9) == 45