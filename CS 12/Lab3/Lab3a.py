from oj import MinReadyArray

class MaxReadyArray:
    def __init__(self):
        self.m = MinReadyArray()
        self.m1 = MinReadyArray()
    
    def append_right(self, value: int) -> None:
        self.m.append_right(-value)
        self.m1.append_right(value)

    def append_left(self, value: int) -> None:
        self.m.append_left(-value)
        self.m1.append_left(value)

    def pop_left(self) -> int | None:
        return None if not self.m else self.m.pop_left() 
    
    def pop_right(self) -> int | None:
        return None if not self.m else self.m.pop_right()

    def __len__(self) -> int:
        return len(self.m)
    
    def __getitem__(self, i:int):
        if 0 <= i < len(self.m):
            k: int | None = self.m[i]
            if k != None:
                return -k
        else:
            return None
    
    def max(self, i: int, j: int) -> int | None:
        if i < 0:
            i = 0
        if j > len(self.m):
            j = len(self.m)
        if i < j:
            k: int | None = self.m.min(i ,j)
            if k:
                return -k
        return None
    
    # def __repr__(self):
    #     return f"{self.m}"


# arr1 = MaxReadyArray()
# arr2 = MaxReadyArray()
# arr1.append_left(10)
# arr1.append_right(20)

# print(arr1[1])


# assert arr1[1] == 20
# assert arr1[-1] is None
# assert arr2[0] is None
# assert arr2.max(-100, 100) is None
# arr1.append_left(30)
# assert arr1.max(1, 3) == 20
# assert arr1.max(0, 3) == 30
# arr2.append_left(40)
# arr2.append_right(40)
# assert arr2.max(-100, 100) == 40
# assert len(arr1) == 3
# arr1.pop_left()
# assert len(arr1) == 2
