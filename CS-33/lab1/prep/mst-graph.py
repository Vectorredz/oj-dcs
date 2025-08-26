# given list of edges create adjacency list

class UnionFind:
    def __init__(self, n):
        self.parent = [*range(n + 1)]
        self.weight = [1] * (n + 1)
        super().__init__()
        
    def __getitem__(self, i):
        if (self.parent[i] == i):
            return i
        else:
            self.parent[i] = self.parent[self.parent[i]]
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

def kruskals(n: int, edges: list[tuple[tuple[int, int], int]]):
    mst = []
    # # sort the edges
    components = UnionFind(n)
    used_tracks = 0
    total_tracks  = 0
    free_tracks = []
    edges = sorted(edges, key=lambda edge: edge[1])
    # loop onto the edges until no cycle is form
    for edge, w in edges:
        i, j = edge
        if (components.unite(i,j)):
            mst.append((i,j))
            used_tracks += w
        else:
            free_tracks.append(edges.index(((i,j), w)) + 1)
        total_tracks += w
    return total_tracks - used_tracks, free_tracks
    
    

# def make_adjacency_list(edges: list[list[int]]):
#     # find vertices
#     v = (max(max([[e[0], e[1]] for e in edges]))) 
#     adj_list = [[] for _ in range(v)]  
#     # (vertex, weight)      
#     # print(adj_list)
#     for i, j, w in edges:
#         adj_list[i].append((j,w))
    
#     print(adj_list, v)


x = kruskals(3, [
    ((1, 2), 5),
    ((2, 3), 6),
    ((3, 1), 7),
    ])
print(x)