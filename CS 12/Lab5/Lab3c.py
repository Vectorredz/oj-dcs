from typing import TypeVar, Generic, Sequence
from pytest import raises

T = TypeVar('T')

class LoopedList(Generic[T]):
    def __init__(self, contents: Sequence[T]):
        self.contents = list(contents)
        self.length = len(self.contents)
    
    def __getitem__(self, i: int) -> T | None:
        if self.length > 0:
            k: T | None = self.contents[i%self.length]
            if k is not None:
                return k
        else:
            raise IndexError

    def __setitem__(self, i:int, t: T):
        if self.length == 0:
            raise IndexError
        if self.contents:
            self.contents[i%self.length] = t

    def __len__(self) -> int:
        return self.length
    
    def rotate(self, x: int):
        if self.length == 0:
            raise IndexError
        else:
            if self.contents:
                self.contents = self.contents[x%self.length:] + self.contents[:x%self.length]
          
    def __repr__(self):
        return f"{self.contents}"
        




def test_LoopedList():
    l = LoopedList[int]((31, 41, 59, 26))

    assert l[1] == 41
    assert l[5] == 41
    assert l[-7] == 41
    assert l[-1] == 26

    l[11] = 2653  # the list should now represent [31, 41, 59, 2653]

    assert l[-1] == 2653

    l.rotate(13)  # the list should now represent [41, 59, 2653, 31]

    assert l[0] == 41
    assert l[-2] == 2653

    assert l[100] == l[104]

    assert len(l) == 4

    l2 = LoopedList[str](())

    with raises(IndexError):
        l2[0]

test_LoopedList()