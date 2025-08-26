from collections.abc import Sequence, Iterable

def heappush(heap, val):
    heap.append(val)
    i = len(heap) - 1
    while (i > 0):
        if (heap[p := i - 1 >> 1] > heap[i]):
            heap[p], heap[i] = heap[i], heap[p]
            i = p
        else:
            break

def heappop(heap):
    heap[0], heap[-1] = heap[-1], heap[0]
    res = heap.pop()
    i = 0
    while (c := 2*i + 1) < len(heap):
        if (c + 1 < len(heap) and heap[c] > heap[c + 1]):
            c += 1
        if (heap[i] > heap[c]):
            heap[i], heap[c] = heap[c], heap[i]
            i = c
        else:
            break
    return res

def _within_bounds(i, j, r, c):
    return True if 0 <= i < r and 0 <= j < c else False

def make_adj_list(n, mountains):
    r, c = len(mountains), len(mountains[0])   
    edges = []  
    adj_list = [[] for _ in range(n)]   
    
    coordinates = [
        (i, j)
        for i in range(r)
        for j in range(c)
    ]
    
    coordinates_idx = {coord: idx for idx, coord in enumerate(coordinates)}
    
    for i in range(r):
        for j in range(c):
            for ni, nj in [(1,0), (-1,0), (0,1), (0,-1)]:
                dr = ni + i
                dc = nj + j
                if (_within_bounds(dr, dc, r, c)):
                    elevation = abs(mountains[i][j] - mountains[dr][dc])
                    edges.append(((coordinates_idx[(i,j)], coordinates_idx[(dr,dc)]), elevation))
    
    for pairs, w in edges:
        u, v = pairs
        adj_list[u].append((w, (u, v)))
        adj_list[v].append((w, (v, u)))
    
    return list(map(lambda x: list(set(x)), adj_list))
              
def min_ladders(mountains):
    # create adj_list
    n = len(mountains) * len(mountains[0])
    adj_list = make_adj_list(n, mountains)
    
    visited = {0}
    
    heap = []
    mst = []
    
    for w, edge in adj_list[0]:
        heappush(heap, (w, edge))
        
    # connect the weights
    connection = 0
        
    while (len(mst) < n-1 and heap):
        w, edge = heappop(heap)
        u, v = edge
        if v in visited:
            continue
        visited.add(v)
        
        if (w != 0):
            connection += 1
        mst.append((edge, w))
        for dw, dedge in adj_list[v]:
            du, dv = dedge
            if dv not in visited:
                heappush(heap, (dw, dedge))
                
    return mst, connection
        
# Give a grid

x = min_ladders([
    [2, 1, 2],
    [2, 1, 2],
    [2, 2, 2]
])

print(x)