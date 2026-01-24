class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)  # 1-indexed

    def _lsb(self, x):
        return x & -x

    # add `delta` at index i
    def update(self, i, delta):
        i += 1  # convert to 1-indexed
        while i <= self.n:
            self.bit[i] += delta
            i += self._lsb(i)

    # sum of [0..i]
    def prefix_sum(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= self._lsb(i)
        return res

    # sum of [l..r]
    def range_sum(self, l, r):
        return self.prefix_sum(r) - self.prefix_sum(l - 1)

class RangeFenwick:
    def __init__(self, n):
        self.fw = Fenwick(n)

    def range_add(self, l, r, val):
        self.fw.update(l, val)
        if r + 1 < self.fw.n:
            self.fw.update(r + 1, -val)

    def point_query(self, i):
        return self.fw.prefix_sum(i)
