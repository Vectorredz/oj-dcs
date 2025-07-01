class MinReadyArray:
    def __init__(self):
        self.m: list[int] = []
    def append_right(self, value: int) -> None:
        self.m.append(value)
    def append_left(self, value: int) -> None:
        self.m.insert(0, value)
    def pop_left(self) -> int | None:
        return self.m.pop(0) if self.m else None
    def pop_right(self) -> int | None:
        return self.m.pop() if self.m else None
    def __len__(self) -> int:
        return len(self.m)
    def __getitem__(self, i: int) -> int | None:
        return self.m[i] if i >=  0 and i < len(self.m) else None
    def min(self, i: int, j:int) -> int | None:
        if i >= j or len(self.m) == 0:
            return None
        else:
            if i < 0:
                i = 0
            if j > len(self.m):
                j = len(self.m)
            k = [self.m[x] for x in range(i, j)]
            #array of k within i-j
            if len(k) == 0:
                return None
            array = sorted(k)
            min1 = array[0]

        return min1
    

