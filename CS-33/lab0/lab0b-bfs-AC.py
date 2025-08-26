from collections import deque
Coord = tuple[int,int]

def least_jumps(grid: list[list[int]], d: int, u: int, s: Coord, e: Coord) -> int|None:
    r: int = len(grid)
    c: int = len(grid[0])
    visited: set[Coord] = set()
    
    if (s == e):
        return 0

    def _within_bounds(di: int, dj: int) -> bool:
        return True if 0 <= di < r and 0 <= dj < c else False
    
    def _valid_height(i: int, j: int, di: int, dj: int) -> bool:
        if (grid[i][j] > grid[di][dj] and grid[i][j] - grid[di][dj] <= d):
            return True
        elif (grid[i][j] < grid[di][dj] and grid[di][dj] - grid[i][j] <= u):
            return True
        elif (grid[di][dj] == grid[i][j]):
            return True
        else:
            return False
            
    def neighbors(src: Coord) -> list[Coord]:
        coordinates: list[Coord] = []
        r, c = src[0], src[1]
        for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            di = r + i
            dj = c + j
            if (_within_bounds(di, dj) and _valid_height(r, c, di, dj)):
                coordinates.append((di, dj))
        return coordinates
    # use bfs instead of dfs from earlier
    
    def get_least_path(src: Coord, end: Coord):
        queue = deque()   
        queue.append([src, 0])
        visited.add(src)
        
        while queue:
            node, steps = queue.popleft()
            if node == end:
                return steps
            for vertex in neighbors(node):
                if vertex not in visited:
                    visited.add(vertex)
                    queue.append((vertex, steps + 1))
        return None
              
    x = get_least_path(s, e)   
    return x if x is not None else None
    
assert least_jumps([[5]], 0, 0, (0,0), (0,0)) == 0
assert least_jumps([    
    [2,2,2],
    [2,2,2],
], 0, 0, (0,0), (1,2)) == 3
assert least_jumps([
    [5,4],
    [3,2],
], 1, 1, (0,0), (1,1)) == None
assert least_jumps([
    [1,2],
    [3,4],
], 1, 1, (0,0), (1,1)) == None
assert least_jumps([
    [1, 100, 1],
    [1, 100, 1],
    [1, 1,   1],
], 1, 1, (0,0), (0,2)) == 6