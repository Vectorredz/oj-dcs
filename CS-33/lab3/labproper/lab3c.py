from collections.abc import Sequence
from dataclasses import dataclass, field

# (cc) Binary lifitng lca from cs33 drives implementation 
@dataclass
class Node:
    label: int
    parent: "Node | None" = None
    children: "list[Node]" = field(default_factory=list)
    depth: int = 0
    jumps: "list[Node]" = field(default_factory=list)
    # node.jumps[k] is the ancestor of this node 2^k steps up

    def compute_stuff(self):
        for child in self.children:
            child.depth = self.depth + 1
            child.compute_stuff()

    def ascend(self, d):
        curr = self

        # power-of-two jumps
        for k in reversed(range(len(curr.jumps))):
            if curr.jumps[k].depth >= d:
                curr = curr.jumps[k]

        assert curr.depth <= d
        return curr

    def __eq__(self, other):
        return self.label == other.label

    def __ne__(self, other):
        return self.label != other.label


def _find_root(n, routes):
    indeg, outdeg = [0] * n, [0] * n
    root = None
    for i, j in routes:
        indeg[j] += 1
        outdeg[i] += 1
    
    # root = indeg.index(min(indeg))
    return 0
    

class TropicalResort:
    def __init__(self, population: Sequence[int], routes: Sequence[tuple[int, int]]):
        self.routes = routes
        self.population = population
        self.n, self.e = len(population), len(routes)
        n = self.n
        self.odds = [0] * self.n
        self.adj = [[] for _ in range(self.n)]
        # parent = [0] * self.n
        root = _find_root(self.n, routes)
        self.r = root
        # compute parents
        for u, v in self.routes:
            # parent[v] = u 
            self.adj[u].append(v)
            self.adj[v].append(u)

        self.nodes = [Node(label=i) for i in range(n)]
        
        parent = self.get_dem_parents(0)
        # set up root, parent and children pointers
        self.root = self.nodes[root]
        self.root.parent = self.root
        for i in range(self.n):
            if i != root:
                self.nodes[i].parent = self.nodes[parent[i]]
                self.nodes[parent[i]].children.append(self.nodes[i])

        # DFS to compute stuff
        self.root.compute_stuff()

        # we need to compute ancestors powers of 2 away
        # p ~ lg n
        p = n.bit_length() + 1
        for node in self.nodes:
            node.jumps = [None]*p
            node.jumps[0] = node.parent

        for k in range(1, p):
            for node in self.nodes:
                node.jumps[k] = node.jumps[k - 1].jumps[k - 1]

        # precompute the prefix sums
        self._prefix_sums()

        super().__init__()

    def get_dem_parents(self, root):
        parents = [0] * self.n
        visited: list[bool] = [False] * self.n
        def dfs(u):
            visited[u] = True
            
            for v in self.adj[u]:
                if not visited[v]:
                    parents[v] = u
                    dfs(v)
        dfs(0)          
        return parents
    
    def lca(self, i, j):
        # get node objects
        i = self.nodes[i]
        j = self.nodes[j]

        # make them the same depth
        i = i.ascend(j.depth)
        j = j.ascend(i.depth)
        assert i.depth == j.depth

        # power-of-two jumps
        for k in reversed(range(len(i.jumps))):
            if i.jumps[k] != j.jumps[k]:
                i = i.jumps[k]
                j = j.jumps[k]
        
        # maybe one more step needed
        if i != j:
            i = i.parent
            j = j.parent

        return i.label

    def _prefix_sums(self):
        visited: list[bool] = [False] * self.n
        self.odds[self.r] = 1 if self.population[self.r] % 2 != 0 else 0
        def dfs(u):
            visited[u] = True
            for v in self.adj[u]:
                if not visited[v]:
                    self.odds[v] = self.odds[u] + 1 if self.population[v] % 2 != 0 else self.odds[u]
                    dfs(v)
                    
        dfs(self.r)
                
    def count_calming_locations(self, s: int, t: int) -> int:
        # get the prefix sums of loners
        if s == t: return 1 if self.population[s] % 2 != 0 else 0
        
        ret = self.lca(s,t)        
        loners = self.odds[s] + self.odds[t] - (2 * self.odds[ret]) + (self.population[ret] % 2)
        return loners