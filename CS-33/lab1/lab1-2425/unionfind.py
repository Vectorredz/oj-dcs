class UnionFind():
    def __init__(self, n):
        self.parent = [*range(n)]
        self.weight = [1] * n
        
    def __getitem__(self, i):
        if (self.parent[i] == i):
            return i
        else:
            self.parent[i] = self[self.parent[i]]
            return self.parent[i]
    
    def unite(self, i, j):
        if (i := self[i]) == (j := self[j]):
            return False
        if (self.weight[i] > self.weight[j]):
            i, j = j, i
        assert self.weight[i] <= self.weight[j]
        self.weight[j] += self.weight[i]
        self.parent[i] = j
        return True