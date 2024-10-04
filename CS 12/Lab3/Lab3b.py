from oj import MinReadyArray

class MaxReadyArray:
    def __init__(self) -> None:
        self.array = MinReadyArray()
        self.array2 = MinReadyArray()

    def append_right(self, value: int) -> None:
        self.array.append_right(-value)
        self.array2.append_right(value)

    def append_left(self, value: int) -> None:
        self.array.append_left(-value)
        self.array2.append_left(value)

    def pop_left(self) -> int | None:
        self.array2.pop_left()
        if len(self.array) == 0:
            return None
        popped = self.array.pop_left()
        if popped is not None:
            return -popped
        else:
            return None
        
    def pop_right(self) -> int | None:
        self.array2.pop_right()
        if len(self.array) == 0:
            return None
        popped = self.array.pop_right()
        if popped is not None:
            return -popped
        else:
            return None
    
    def __len__(self) -> int:
        return len(self.array)

    def __getitem__(self, i: int) -> int | None:
        if 0 <= i < len(self.array):
            a: int | None = self.array[i]
            if a is not None:
                return -a
        else:
            return None
        
    def min(self, i: int, j: int) -> int | None:
        return self.array2.min(i, j)

    def max(self, i: int, j: int) -> int | None:
        if i < 0:
            i = 0
        if j > len(self.array):
            j = len(self.array)
        if i < j:
            b: int | None = self.array.min(i, j)
            if b != None:
                return -b
        else:
            return None

class Moles:
    def __init__(self, n: list[tuple[int, int]]) -> None:
        self.cx: MaxReadyArray = MaxReadyArray()
        self.cy: MaxReadyArray = MaxReadyArray()
        self.n = n

        for x in n:
            self.cx.append_right(x[0])
            self.cy.append_right(x[1])

    def burrow(self, x: int, y: int) -> None:
        self.cx.pop_left()
        self.cy.pop_left()
        self.cx.append_right(x)
        self.cy.append_right(y)

    def __getitem__(self, i: int) -> tuple[int, int]:
        a = self.cx[i]
        b = self.cy[i]
        if (a is not None and b is not None):
            return (a, b)
        else:
            return (0, 0)

    def spread(self, i: int, j: int) -> int:
        biggestx = self.cx.max(i, j)
        biggesty = self.cy.max(i, j)
        smolx = self.cx.min(i, j)
        smoly = self.cy.min(i, j)
        if biggestx is not None and biggesty is not None and smolx is not None and smoly is not None:
            return abs(((biggestx+1) - (smolx-1)) * ((biggesty+1) - (smoly-1)))
        else:
            return 0
        
    def __str__(self):
        self.n = [self.cx] + [self.cy]
        return f"{self.n}"
    

m = Moles([(10, 20), (20, 10), (30, 30)])

# perform operations
assert m.spread(0, 2) == 144
assert m.spread(1, 3) == 264
assert m[0] == (10, 20)

m.burrow(10, 20)

print(m)
# assert m.spread(1, 3) == 24
# assert m[0] == (20, 10)