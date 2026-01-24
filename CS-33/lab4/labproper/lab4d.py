from collections.abc import Sequence
from dataclasses import dataclass, field

# (cc) PATH_MIN cs33 implementation

@dataclass
class Node:
    label: int
    val: int = 0
    parent: "Node | None" = None
    adj: "list[Node | None]" = field(default_factory=list)
    index: int = 0
    depth: int = 0
    size: int = 1
    topmost: "Node | None" = None

    def is_preferred_child(self):
        return self.parent.adj[0] is self

    def traverse(self):
        if self.parent is not self:
            self.depth = self.parent.depth + 1

        for node in list(self.adj):
            if node is not self.parent:
                node.parent = self
                node.traverse()
                self.size += node.size

        # remove parent from adjacency list
        self.adj = [node for node in self.adj if node is not self.parent]

        # put the heaviest child in front
        if self.adj:
            i = max(range(len(self.adj)), key=lambda i: self.adj[i].size)
            self.adj[i], self.adj[0] = self.adj[0], self.adj[i]

    def flatten(self, target):
        self.index = len(target)
        target.append(self.label)  

        # compute topmost
        if self.parent is not self and self.is_preferred_child():
            self.topmost = self.parent.topmost
        else:
            self.topmost = self

        for child in self.adj:
            child.flatten(target)


class Fenwick:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1) # 1-indexed

    def _lsb(self, x: int) -> int:
        return x & -x # mask strat

    def add(self, i: int, delta: int):
        i += 1
        while i <= self.n:
            self.bit[i] += delta
            i += self._lsb(i)

    def prefix_sum(self, i: int) -> int:
        i += 1
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= self._lsb(i)
        return s

    def range_sum(self, l: int, r: int) -> int:
        if r < l:
            return 0
        if l == 0:
            return self.prefix_sum(r)
        return self.prefix_sum(r) - self.prefix_sum(l - 1)


class Stores:
    def __init__(self, customers: Sequence[int], roads: Sequence[tuple[int, int]]):
        self.customers = list(customers)
        self.n = len(self.customers)

        # construct nodes adj list
        self.nodes: list[Node] = [Node(label=i) for i in range(self.n)] # nodes of i with index/label i
        
        # adj of adj
        for a, b in roads:
            self.nodes[a].adj.append(self.nodes[b])
            self.nodes[b].adj.append(self.nodes[a])

        # if root is at zero
        if self.n == 0:
            self.root = None
            self.order = []
            self.pos = []
            # two segtrees rooted at 0
            self.even = Fenwick(0)
            self.odd = Fenwick(0)
            return

        self.root = self.nodes[0]
        self.root.parent = self.root
        self.root.depth = 0

        self.root.traverse()

        # flatten into array positions (HLD order)
        flat = []
        self.root.flatten(flat)
        self.pos = [0] * self.n
        for node in self.nodes:
            self.pos[node.label] = node.index

        # two fenwicks: idea here is that if even it has equal amount of candidate nodes while odd it has +1 na sobra (might or might not include lca)
        self.even = Fenwick(self.n)
        self.odd = Fenwick(self.n)

        # init nodes of customers
        for node in self.nodes:
            idx = node.index
            val = self.customers[node.label]
            if (node.depth % 2 == 0): 
                self.even.add(idx, val)
            else:
                self.odd.add(idx, val)

    def _subtree_sum(self, u: Node, v: Node, parity: int) -> int:
        l: int = v.index
        r: int = u.index
        
        if parity != 0:
            return self.odd.range_sum(l, r)
        else:
            return self.even.range_sum(l, r)

    def _path_sum_parity(self, a: int, b: int, parity: int) -> int:
        """Return sum of nodes on path a->b whose depth parity == parity."""
        u = self.nodes[a]
        v = self.nodes[b]
        res = 0
        # path climb; lca kinda 
        while u.topmost is not v.topmost:
            if u.topmost.depth >= v.topmost.depth:
                head = u.topmost
                res += self._subtree_sum(u, head, parity)
                
                u = head.parent
            else:
                head = v.topmost
                res += self._subtree_sum(v, head, parity)
                
                v = head.parent
        # LCA found
        if u.index >= v.index:
            res += self._subtree_sum(u, v, parity)
        else:
            res += self._subtree_sum(v, u, parity)
            
        return res

    def update_customers(self, i: int, c: int) -> None:
        if self.customers[i] == c: return # same value
        temp = self.customers[i]
            
        self.customers[i] = c
        
        node = self.nodes[i]
        idx = node.index
        # update the seg trees for sum accumulation
        if node.depth % 2 == 0:
            self.even.add(idx, c - temp)
        else:
            self.odd.add(idx, c - temp)

    def customers_sold_to(self, i: int, j: int) -> int:
        if i < 0 or j < 0: return 0
        if i == j: return self.customers[i]
        include_parity = self.nodes[i].depth & 1
        total = self._path_sum_parity(i, j, include_parity)
        return total


# def test_Stores():
#     stores = Stores((20, 30, 50, 30, 20, 10, 40, 30, 20), (
#         (0, 1),
#         (0, 2),
#         (0, 3),
#         (2, 4),
#         (3, 5),
#         (3, 6),
#         (6, 7),
#         (6, 8),
#     ))

#     assert stores.customers_sold_to(0, 4) == 40
#     assert stores.customers_sold_to(0, 4) == 40
#     assert stores.customers_sold_to(8, 0) == 50 
#     assert stores.customers_sold_to(0, 8) == 60 
#     assert stores.customers_sold_to(5, 6) == 50 

#     stores.update_customers(6, 10)
#     stores.update_customers(0, 50)

#     assert stores.customers_sold_to(4, 7) == 80 

#     # TODO add more tests here
# test_Stores()