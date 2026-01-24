# lab04a.py
from collections.abc import Sequence

class BowserTime:
    def __init__(self, initial_coins: Sequence[int]):
        self.n = len(initial_coins)
        self.base = [0] + list(initial_coins)
        self._ft = [0] * (self.n + 2)

    def add(self, idx: int, delta: int) -> None:
        ft = self._ft
        n = self.n + 1
        while idx <= n:
            ft[idx] += delta
            idx += idx & -idx

    def sums(self, idx: int) -> int:
        s = 0
        ft = self._ft
        while idx > 0:
            s += ft[idx]
            idx -= idx & -idx
        return s

    def _range_add(self, l: int, r: int, x: int) -> None:
        if l > r:
            return
        self.add(l, x)
        self.add(r + 1, -x)

    def give_coins_to_range(self, l: int, r: int, x: int) -> None:
        assert 1 <= l <= r <= self.n
        self._range_add(l, r, x)

    def give_coins_to_all_except(self, j: int, x: int) -> None:
        assert 1 <= j <= self.n
        if j > 1:
            self._range_add(1, j - 1, x)
        if j < self.n:
            self._range_add(j + 1, self.n, x)

    def num_coins(self, j: int) -> int:
        assert 1 <= j <= self.n
        return self.base[j] + self.sums(j)
