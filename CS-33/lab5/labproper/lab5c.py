from collections import deque

class SugarHeap:
    def __init__(self) -> None:
        self.heap: list[int] = []
        self.versions: list[list[int]] = [[0]]
        
    def push(self, s: int) -> None:
        self.heap.append(s)
        i = len(self.heap) - 1 # starts the heap at the end
        while i > 0:
            if self.heap[p := i - 1 >> 1] < self.heap[i]: # i - 1 // 2 is the parent of the level order child i
                self.heap[p], self.heap[i] = self.heap[i], self.heap[p] # swap the parent and i to maintain maxheap
                i = p # do all over again to all levels
            else:
                break
        # take a snapshot of the heap
        temp = self.heap.copy()
        self.versions.append(temp)
        
    def pop(self) -> int:
        if len(self.heap) <= 0: return 0
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0] # swap the rightmost child to the root
        res = self.heap.pop() # get the min value from the root
        i = 0
        
        # essentially this just rebalances the heap back to its minheap property
        while (c := 2*i + 1) < len(self.heap): # while there are still left childrenn from the heap
            if c + 1 < len(self.heap) and self.heap[c] < self.heap[c + 1]:
                c += 1 # if theres still a right child and that the left is greater than the right
            if self.heap[i] < self.heap[c]: # if the parent is greater than the child
                self.heap[i], self.heap[c] = self.heap[c], self.heap[i] # swap them
                i = c # recurse to the child and do the same
            else:
                break
        
        temp = self.heap.copy()
        self.versions.append(temp)
        return res
        
    def sugar_sum(self) -> int:
        temp = self.heap.copy()
        self.versions.append(temp)
        return sum(self.heap)
        
    def add_sugar(self, v: int) -> None:
        # perform a level order traversal the apply the add sugar 
        def level_order():
            q = deque([0])
            while (q):
                u = q.popleft()
                self.heap[u] += v
                for i in [1, 2]:
                    du = 2*u + i
                    if du < len(self.heap):
                        q.append(du)     
        level_order()
        temp = self.heap.copy()
        self.versions.append(temp)            
               
    def time_travel(self, k: int) -> None:
        if k >= len(self.versions): return None
        if k == 0: return None
        self.heap = self.versions[k].copy()
        temp = self.heap.copy()
        self.versions.append(temp)            

sugar_heap = SugarHeap()
# sugar_heap.pop()
# sugar_heap.pop()
sugar_heap.push(3)
sugar_heap.push(1)
sugar_heap.push(4)
sugar_heap.push(5)
sugar_heap.pop()

print(sugar_heap.versions)