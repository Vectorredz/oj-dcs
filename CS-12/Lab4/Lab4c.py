from typing import Generic, TypeVar, Sequence

T = TypeVar("T")

class BulkRow(Generic[T]):
    def __init__(self, b: Sequence[T]) -> None:
        self.b: list[T] = list(b)
    def push_left(self, item: T, count: int = 1) -> None:
        try:
            if count > 0:
                for _ in range(count):
                    self.b.insert(0, item)
        except:
            raise ValueError
    
    def push_right(self, item: T, count: int = 1) -> None:
        try:
            if count > 0:
                for _ in range(count):
                    self.b.append(item)
        except:
            raise ValueError
    def __getitem__(self, i: int):
        if 0 <= i < len(self.b):
            return self.b[i]
        else:
            raise IndexError
    def __len__(self):
        return len(self.b)
    def __repr__(self):
        return f"{self.b}"
        

b: BulkRow[str] = BulkRow(('snickers', 'cheddar', 'nescafe', 'nescafe', 'washing powder'))

assert b[4] == 'washing powder'
assert len(b) == 5

b.push_left('fairy liquid', 5)

assert b[4] == 'fairy liquid'
assert b[5] == 'snickers'
assert len(b) == 10

b.push_left('fairy liquid')

assert len(b) == 11

# check out-of-bounds
try:
    b[123456]
except IndexError:
    pass
else:
    assert False, "should have raised IndexError!"