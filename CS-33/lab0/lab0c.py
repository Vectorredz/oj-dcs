
# create two parallel grids
# 1. rooms grid that contains coordinates
# - traverse first the grid and init a rooms grid
# 2. entire grid for comparison
# remove comments / spaces for memory save 2kb
from collections import deque
Coord = tuple[int, int]
State = tuple[Coord, str]
def reachable_rooms(grid: list[str], s: tuple[int, int]) -> list[tuple[int, int]]:
    _grid = list(map(lambda x: list(x), grid))
    r, c = len(grid), len(grid[0])
    visited: set[State] = set()
    paths: set[Coord] = set()    
    def _within_bounds(i: int, j: int): return True if 0 <= i < r and 0 <= j < c else False 
    def neighbors(src: Coord, door: str):
        states: list[State] = []
        i, j = src[0], src[1]
        for nr, nc in [(-1,0), (1, 0), (0,-1), (0,1)]:
            sr, sc = i + nr,  j + nc
            # skip over separator cells
            dr, dc = i + (2*nr), j + (2*nc)
            if not (_within_bounds(sr, sc) and _within_bounds(dr, dc)):
                continue
            next_sep = _grid[sr][sc] # R
            if (next_sep == '#' or _grid[dr][dc] != ' '): continue
            if (next_sep == '.' or next_sep == ' '):
                states.append(((dr,dc), door))
            elif (next_sep in ('R', 'B')):
                if (door == "" or next_sep != door):
                    states.append(((dr, dc), next_sep))                         
        return states
    def bfs(src: Coord, door: str):
        queue = deque()
        visited.add((src, door))
        queue.append((src, door))
        while (queue):
            node, lastDoor = queue.popleft()
            if (_grid[node[0]][node[1]] == " "):
                paths.add(((node[0] - 1) // 2, (node[1] - 1) // 2))
            for state in neighbors(node, lastDoor):
                if (state not in visited):
                    visited.add(state)
                    # we are expecting an alternate colored door
                    queue.append(state)
    bfs((2*s[0] + 1, 2*s[1]+ 1), "")
    return sorted(paths)

reachable_rooms([
        "#######",
        "# B B #",
        "###R###",
        "# R R #",
        "###R###",
        "# R R #",
        "#######",
    ], (1, 1))

