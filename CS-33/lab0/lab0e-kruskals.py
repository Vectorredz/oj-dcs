from dataclasses import dataclass
Coord = tuple[int, int]
Query = tuple[Coord, Coord]
@dataclass
class Edge:
    i: int
    j: int
    weight: int
class UnionFind:
    def __init__(self, n):
        self.parent = [*range(n)]
        self.weight = [1]*n
        super().__init__()
    def __getitem__(self, i):
        if self.parent[i] == i:
            return i
        else:
            self.parent[i] = self[self.parent[i]]
            return self.parent[i]
    def unite(self, i, j):
        if (i := self[i]) == (j := self[j]):
            return False
        if self.weight[i] > self.weight[j]:
            i, j = j, i
            assert self.weight[i] <= self.weight[j]
        self.weight[j] += self.weight[i]
        self.parent[i] = j
        return True
def lowest_highest_tower(grid: list[list[int]], qs: list[Query]) -> list[int]:
    # get the edges among the grid
    # construct a graph
    res = []
    r, c = len(grid), len(grid[0])
    n, edges, idx_node, node_idx = build_graph(grid, r,c)    
    sorted_edges = sorted(edges, key=lambda e: e.weight)
    def mst(n: int, src: Coord, dst: Coord, edges: list[Edge]) -> int:
        comps = UnionFind(n)
        src_idx, dst_idx = node_idx[src], node_idx[dst]
        
        for edge in sorted_edges:
            comps.unite(edge.i, edge.j)
            if comps[src_idx] == comps[dst_idx]:
                return edge.weight
    for query in qs:
        x = mst(n, query[0], query[1], edges)
        res.append(x)
    return res

def build_graph(grid, r, c):
    def _within_bounds(i: int, j: int):
        return True if 0 <= i < r and 0 <= j < c else False
    def neighbors(node: Coord):
        coordinates: list[Coord] = []
        i, j = node
        for ni, nj in [(-1,0), (1,0), (0,1), (0,-1)]:
            dr = i + ni
            dc = j + nj
            if (_within_bounds(dr, dc)):
                coordinates.append((dr,dc))
        return coordinates
    nodes = [
        (i,j) 
        for i in range(r)
        for j in range(c)
    ]
    node_idx = {node: i for i, node in enumerate(nodes)}
    idx_node = {i: node for i, node in enumerate(nodes)}
    edges: list[Edge] = [
        Edge(node_idx[(i,j)], node_idx[(ni, nj)], max(grid[i][j], grid[ni][nj])) 
        for i, j in nodes
        for ni, nj in neighbors((i,j))
    ]
    return len(nodes), edges, idx_node, node_idx
            
lowest_highest_tower([
        [1, 5, 1],
        [1, 5, 1],
        [1, 1, 1],
    ], [
        ((0, 0), (0, 2)),
        ((0, 1), (2, 1)),
    ])