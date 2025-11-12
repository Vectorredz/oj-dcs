# debug_fenwick_vs_segtree.py
from collections.abc import Sequence
from fractions import Fraction
from math import isclose
import random
from dataclasses import dataclass

class Fenwick:
    def __init__(self, n: int) -> None:
        self.n: int = n
        self.bit: list[float] = [0.0] * (n + 1)  # 1-indexed

    def _lsb(self, x: int) -> int:
        return x & -x  # bit mask strat

    # update corresponding values
    def update(self, i: int, val: float):
        i += 1
        while i <= self.n:
            self.bit[i] += val
            i += self._lsb(i)  # cascade update to its children

    def prefix_sum(self, i: int) -> float:
        i += 1
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= self._lsb(i) # backtrack to its parents; highest power of 2
        return res

    def range_sum(self, l: int, r: int) -> float:
        return self.prefix_sum(r) - self.prefix_sum(l-1)


class ParallelPencils:
    def __init__(self, lengths: Sequence[int]):
        self.lengths = list(lengths)
        self.len = len(lengths)
        # init fenwick bit array
        self.fn = Fenwick(self.len)

        # construct mr. fenwick
        for i, L in enumerate(self.lengths):
            if L != 0:
                self.fn.update(i, 1.0/L)
            else:
                self.fn.update(i, L)

    def add_length(self, i: int, l: int) -> None:
        # self.lengths = max(0, +=l)
        prev_f = 1 / self.lengths[i] if self.lengths[i] != 0 else 0
        
        self.lengths[i] = max(0, self.lengths[i] + l)
        if self.lengths[i] == 0:
            delta = - prev_f + 0
        else:
            new = 1 / self.lengths[i]
            delta = - prev_f + new
        self.fn.update(i, delta)      
     
        
    def get_resistance(self, i: int, j: int) -> float:
        s = self.fn.range_sum(i, j - 1)
        if abs(s) < 1e-12:  
            return 0.0
        return 1.0 / s

# ---------- Segment tree (your working version) ----------
@dataclass
class Node:
    i: int
    j: int
    val: float
    l: "Node|None" = None
    r: "Node|None" = None

    @classmethod
    def make(cls, seq, i, j):
        if j - i == 1:
            if seq[i] != 0:
                return cls(i=i, j=j, val=1.0/seq[i])
            else:
                return cls(i=i, j=j, val=0.0)
        else:
            k = (i + j) // 2
            l = cls.make(seq, i, k)
            r = cls.make(seq, k, j)
            return cls(i=i, j=j, val=l.val + r.val, l=l, r=r)

    @property
    def is_leaf(self):
        return self.j - self.i == 1

    def range_sum(self, i, j):
        if i <= self.i and self.j <= j:
            return self.val
        elif j <= self.i or self.j <= i:
            return 0.0
        else:
            return self.l.range_sum(i, j) + self.r.range_sum(i, j)

    def _add_length(self, idx, v):
        if not (self.i <= idx < self.j):
            return
        if self.is_leaf:
            self.val = v
        else:
            self.l._add_length(idx, v)
            self.r._add_length(idx, v)
            self.val = self.l.val + self.r.val

class ParallelPencilsSeg:
    def __init__(self, lengths: Sequence[int]):
        self.lengths = list(lengths)
        self.n = len(lengths)
        self.root = Node.make(self.lengths, 0, self.n)

    def add_length(self, i, v):
        self.lengths[i] = max(0, self.lengths[i] + v)
        if self.lengths[i] == 0:
            self.root._add_length(i, 0.0)
        else:
            self.root._add_length(i, 1.0 / self.lengths[i])

    def get_resistance(self, i, j):
        s = self.root.range_sum(i, j)
        if s == 0.0:
            return 0.0
        return 1.0 / s

# ---------- brute force exact (Fraction) ----------
def brute_resistance(lengths, i, j, exact=False):
    if exact:
        s = Fraction(0, 1)
        for k in range(i, j):
            L = lengths[k]
            if L != 0:
                s += Fraction(1, L)
        if s == 0:
            return Fraction(0, 1)
        return Fraction(1, 1) / s
    else:
        s = 0.0
        for k in range(i, j):
            L = lengths[k]
            if L != 0:
                s += 1.0 / L
        if s == 0.0:
            return 0.0
        return 1.0 / s

# ---------- runner that compares all three ----------
def run_ops_and_compare(initial, ops, exact=False, quiet=False):
    f = ParallelPencilsFenwick(initial)
    s = ParallelPencilsSeg(initial)
    lengths = list(initial)

    for step, op in enumerate(ops, 1):
        typ = op[0]
        if typ == 'add':
            _, idx, delta = op
            # apply to all
            f.add_length(idx, delta)
            s.add_length(idx, delta)
            lengths[idx] = max(0, lengths[idx] + delta)
        elif typ == 'query':
            _, L, R = op
            # segtree uses [L,R) and fenwick wrapper uses get_resistance(L,R)
            res_f = f.get_resistance(L, R)
            res_s = s.get_resistance(L, R)
            res_b = brute_resistance(lengths, L, R, exact=exact)
            # convert Fraction to float for comparison if needed
            if exact:
                # compare Fraction vs Fraction
                ok = (Fraction(res_f).limit_denominator() == res_b) if not isinstance(res_f, Fraction) else (res_f == res_b)
            else:
                ok = isclose(res_f, res_s, rel_tol=1e-12, abs_tol=1e-12)
            if not ok:
                print("=== MISMATCH at step", step, "op=", op)
                print("lengths:", lengths)
                print("Fenwick bit:", f.fn.bit)
                print("Fenwick result:", res_f)
                print("Segtree result:", res_s)
                print("Brute result :", res_b)
                return False
            if not quiet:
                print("OK query", op, "=>", res_f)
        else:
            raise ValueError("unknown op")
    print("All ops matched.")
    return True

# ---------- usage examples ----------
if __name__ == "__main__":
    # Example 1: your test sequence
    initial = [7,7,3,4,4]
    ops = [
        ('query', 0, 2),
        ('query', 2, 5),
        ('add', 1, -5),
        ('add', 3, 2),
        ('query', 1, 4),
        ('query', 0, 5)
    ]
    print("=== Running your sample ops ===")
    run_ops_and_compare(initial, ops, exact=False)

    # Example 2: random fuzz (small)
    print("\n=== Random fuzz test ===")
    for _ in range(200):
        n = 8
        a = [random.randint(0, 10) for _ in range(n)]
        ops = []
        for __ in range(30):
            if random.random() < 0.5:
                i = random.randrange(n)
                delta = random.randint(-5, 5)
                ops.append(('add', i, delta))
            else:
                L = random.randrange(0, n)
                R = random.randrange(L+1, n+1)
                ops.append(('query', L, R))
        ok = run_ops_and_compare(a, ops, exact=False, quiet=True)
        if not ok:
            break
    else:
        print("Random fuzz passed.")
