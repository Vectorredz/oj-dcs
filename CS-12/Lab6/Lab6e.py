from typing import Sequence
from dataclasses import dataclass
@dataclass(frozen=True)
class Point:
    x: int
    y: int

# x1≤x≤x2 and y1≤y≤y2

# 1 if x1 <= a.x <= x2 and y1 <= a.y <= y2
def mole_count(x1: int, x2: int, y1: int, y2: int, p: Sequence[Point]):
    return sum(list(map(lambda a: (1 if y1 <= a.y <= y2 else 0) and (1 if x1 <= a.x <= x2 else 0), p)))

print(mole_count(-10, 20, 5, 10, (
            Point(-10, 6),
            Point(-30, -50),
            Point(0, 8),
            Point(0, 0),
            Point(5, 7),
            Point(0, 12),
            Point(-10, 6),
            Point(18, 9),
            Point(21, 11),
        )))