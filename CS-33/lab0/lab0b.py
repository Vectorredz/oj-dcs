Coord = tuple[int,int]

def least_jumps(grid: list[list[int]], d: int, u: int, s: Coord, e: Coord) -> int|None:
    paths: list[Coord] = []
    r: int = len(grid)
    c: int = len(grid[0])
    visited: set[Coord] = set()
    paths: list[Coord] = []
    all_paths: list[list[Coord]] = []

    def _within_bounds(di: int, dj: int) -> bool:
        return True if 0 <= di < r and 0 <= dj < c else False
    
    def _valid_height(i: int, j: int, di: int, dj: int) -> bool:
        if (grid[i][j] > grid[di][dj] and grid[i][j] - grid[di][dj] <= d):
            return True
        elif (grid[i][j] < grid[di][dj] and grid[di][dj] - grid[i][j] <= u):
            return True
        elif (grid[di][dj] - grid[i][j]) == 0:
            return True
        else:
            return False
            
    def neighbors(src: Coord):
        coordinates: list[Coord] = []
        r, c = src[0], src[1]
        for i, j in [(0,1), (0,-1), (1,0), (-1,0)]:
            di = r + i
            dj = c + j
            if (_within_bounds(di, dj) and _valid_height(r, c, di, dj)):
                coordinates.append((di, dj))
        return coordinates
    
    def get_paths(src: Coord, end: Coord):
        paths.append(src)
        visited.add(src)
        if (src == end):
            all_paths.append(paths.copy())
        else:
            for vertex in neighbors(src):
                if (vertex not in visited):
                    get_paths(vertex, end)
        paths.pop()
        visited.remove(src)

    visited.add(s)
    get_paths(s, e)
    x = len(sorted(all_paths)[0]) - 1 if len(sorted(all_paths)) > 0 else None
    return x