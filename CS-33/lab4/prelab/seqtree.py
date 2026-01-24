from dataclasses import dataclass

@dataclass
class Node:
    i: int
    j: int
    val: int
    l: "Node | None" = None
    r: "Node | None" = None

    @classmethod
    def make(cls, seq, i, j):
        # build a tree for interval [i, j)
        if j - i == 1:  # leaf
            return cls(i=i, j=j, val=seq[i])
        else:
            k = (i + j) // 2
            l = cls.make(seq, i, k)
            r = cls.make(seq, k, j)
            return cls(i=i, j=j, val=min(l.val, r.val), l=l, r=r)

    @property
    def is_leaf(self):
        return self.j - self.i == 1

    def range_min(self, i, j):
        # query minimum on [i, j)
        if i <= self.i and self.j <= j:   # fully inside
            return self.val
        elif j <= self.i or self.j <= i:  # disjoint
            return float('inf')
        else:  # partial overlap
            return min(self.l.range_min(i, j), self.r.range_min(i, j))

    def set(self, i, v):
        # point update: set index i to value v
        if not (self.i <= i < self.j):
            return
        if self.is_leaf:
            self.val = v
        else:
            self.l.set(i, v)
            self.r.set(i, v)
            self.val = min(self.l.val, self.r.val)


class RangeMin:
    def __init__(self, seq):
        self.seq = list(seq)
        self.n = len(seq)
        self.root = Node.make(seq, 0, self.n)

    def range_min(self, i, j):  # query on [i, j)
        assert 0 <= i < j <= self.n
        return self.root.range_min(i, j)

    def __setitem__(self, i, v):  # point update
        assert 0 <= i < self.n
        self.root.set(i, v)
