from collections import deque
Coord = tuple[int, int]
def reachable_rooms(grid: list[str], s: tuple[int, int]) -> list[tuple[int, int]]:
    _grid = list(map(lambda x: list(x),  grid))
    r: int = len(grid)
    c: int = len(grid[0])
    visited: set[Coord] = set()
    doors: dict[Coord, str] = {}
    paths: list[Coord] = []
    def _within_bounds(i: int, j: int):
        return True if 0 <= i < r and 0 <= j < c and grid[i][j] != '#' else False 
    def neighbors(src: Coord):
        coordinates: list[Coord] = []
        i, j = src[0], src[1]
        for nr, nc in [(-1,0), (1, 0), (0,1), (0,-1)]:
            dr = i + nr
            dc = j + nc
            if (_within_bounds(dr,dc)):
                if (src not in doors):
                    doors[src] = ""
                if (doors[src] == ""):
                    coordinates.append((dr,dc))
                if (_grid[dr][dc] == " " or _grid[dr][dc] == '.'):
                    doors[(dr,dc)] = doors[src] 
                    coordinates.append((dr,dc))
                elif (doors[src] == _grid[dr][dc]):
                    coordinates.append((dr,dc))     
        return coordinates
    def bfs(src: Coord):
        queue = deque()
        visited.add(src)
        queue.append(src)     
        while (queue):
            node: Coord = queue.popleft()
            if (_grid[node[0]][node[1]] == ' '):
                paths.append(((node[0] // 2), (node[1] // 2)))
            for vertex in neighbors(node):
                if (vertex not in visited):
                    visited.add(vertex)
                    queue.append(vertex)
                    if (vertex not in doors):
                        if (_grid[vertex[0]][vertex[1]] == 'R'):
                            doors[vertex] = 'B'
                        elif (_grid[vertex[0]][vertex[1]] == 'B'):
                            doors[vertex] = 'R'
    src = (2*s[0] + 1, 2*s[1]+ 1)
    bfs(src)
    return sorted(paths)
