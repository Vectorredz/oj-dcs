from dataclasses import dataclass
from math import isclose
from collections.abc import Sequence

# (cc) segtree from cs33materials

@dataclass
class Node:  # [i, j)
    i: int
    j: int
    val: int
    l: "Node | None" = None
    r: "Node | None" = None

    @classmethod
    def make(cls, seq, i, j):
        # make a tree on indices [i, j)
        if j - i == 1:
            if seq[i] != 0:
                return cls(i=i, j=j, val=1 / seq[i])
            else:
                return cls(i=i, j=j, val=seq[i])
        else:
            k = (i + j) // 2
            assert i < k < j
            l = cls.make(seq, i, k)
            r = cls.make(seq, k, j)
            return cls(i=i, j=j, val=l.val + r.val, l=l, r=r)

    @property
    def is_leaf(self):
        return self.j - self.i == 1

    def range_sum(self, i, j):
        if i <= self.i and self.j <= j:
            # the interval of this node is completely contained
            # in the query interval
            return self.val
        elif j <= self.i or self.j <= i:
            # the intervals are completely disjoint
            return 0
        else:
            # partially overlapping
            l_ans = self.l.range_sum(i, j)
            r_ans = self.r.range_sum(i, j)
            return l_ans + r_ans

    def _add_length(self, i, v):
        if not (self.i <= i < self.j):
            return

        if self.is_leaf:
            self.val = v
            
        else:
            self.l._add_length(i, v)
            self.r._add_length(i, v)
            self.val = self.l.val + self.r.val


class ParallelPencils:
    def __init__(self, lengths: Sequence[int]):    
        self.lengths = list(lengths)    
        self.n = len(lengths)
        self.root = Node.make(self.lengths, 0, self.n)
        super().__init__()

    
    def get_resistance(self, i: int, j: int) -> float:
        s = self.root.range_sum(i, j)
        if s == 0:
            return 0
        else:
            return float(1.0 / s)

    def add_length(self, i, v):
        self.lengths[i] = max(0, self.lengths[i] + v)
        if self.lengths[i] == 0:
            self.root._add_length(i, 0)
        else:
            self.root._add_length(i, 1.0 / self.lengths[i])

      
            

tol = 1e-9
def close_enough(a: float, b: float):
    return isclose(a, b, abs_tol=tol, rel_tol=tol)


def test_ParallelPencils():
    pencils = ParallelPencils((7, 7, 3, 4, 4))
    # print(pencils.get_resistance(0, 3))
    print(pencils.root)
    # assert close_enough(pencils.get_resistance(0, 2), 3.5)  
    # assert close_enough(pencils.get_resistance(2, 5), 1.2)
    # pencils.add_length(1, -5)
    # pencils.add_length(3,  2)
    # # print(pencils.get_resistance(1, 4))
    # assert close_enough(pencils.get_resistance(1, 4), 1.0) 
    # assert close_enough(pencils.get_resistance(0, 5), 0.7179487179) 
test_ParallelPencils()