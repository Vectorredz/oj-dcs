# get all distances between all pairs
from typing import List

class UnionFind():
    def __init__(self, n: int):
        self.parents = [*range(n)]
        self.weights = [1] * n
    
    def __getitem__(self, i: int):
        if (self.parents[i] == i):
            return i
        else:
            self.parents[i] = self[self.parents[i]]
            return self.parents[i]
        
    def unite(self, i: int, j: int):
        if (i := self[i]) == (j := self[j]):
            return False
        if (self.weights[i] > self.weights[j]):
            i, j = j, i
        assert self.weights[j] >= self.weights[i]
        self.weights[j] += self.weights[i]
        self.parents[i] = j
        return True

def minCostConnectPoints(points: List[List[int]]) -> int:
    n = len(points)
    coordinates = {tuple(coord): idx for idx, coord in enumerate(points)}

    def manhattan_distance(u: list[int], v: list[int]):
        xi, yi = u
        xj, yj = v
        return abs(xi - xj) + abs(yi - yj)

    def generate_distances() -> List[tuple[int, ...]]:
        distances: List[tuple[int, ...]] = []
        for i in range(n):
            for j in range(n):
                if (i != j):
                    distances.append((manhattan_distance(points[i], points[j]),coordinates[tuple(points[i])], coordinates[tuple(points[j])]))
        return distances
    
    edges = generate_distances()
    edges = sorted(edges, key=lambda x: x[0])
    
    components = UnionFind(n)
    mst_points: list[tuple[int, ...]] = []
    cost = 0
    
    for edge in edges:
        w, i, j = edge
        if (components.unite(i,j)):
            mst_points.append((i,j))
            cost += w
    print(mst_points, cost)
    return cost
        


# assert minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]) == 20

minCostConnectPoints([[11,12],[-9,5],[-1,5],[9,-8],[20,-17],[18,19],[-1,14],[16,19],[2,16],[14,3],[1,-12],[19,4],[5,-17],[-13,6],[-4,1],[-7,-16],[13,7],[-20,-7],[20,-15]])