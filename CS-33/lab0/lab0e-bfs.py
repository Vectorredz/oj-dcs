# find the minimum path sum  
# find the highest ever value among that path

from collections import deque
Coord = tuple[int,int]
Query = tuple[Coord, Coord]

def lowest_highest_tower(grid: list[list[int]], qs: list[Query]) -> list[int]:
    # get all the paths from src to dst
    res: list[int] = []
        
    r: int = len(grid)
    c: int = len(grid[0])
    
    def _within_bounds(di: int, dj: int) -> bool:
        return True if 0 <= di < r and 0 <= dj < c else False
    
    def neighbors(src: Coord):
        coordinates: list[Coord] = []
        r, c = src[0], src[1]
        for i, j in [(0,1), (0,-1), (1,0), (-1,0)]:
            di = r + i
            dj = c + j
            
            if (_within_bounds(di, dj)):
                coordinates.append((di, dj))
        
        return coordinates
    
    paths: list[Coord] = []
    
    # apply bfs also 
    def get_paths(src: Coord, end: Coord):
        visited: set[Coord] = set()
        queue = deque()
        queue.append([src, grid[src[0]][src[1]], [grid[src[0]][src[1]]]])
        visited.add(src)
        min_path: list[None | int] = [None, None]
        while (queue):
            node, path_sum, path = queue.pop()
            if (node == end):
                curr_path = [path_sum, path]
                if (min_path[0] == None or curr_path[0] <= min_path[0] and max(curr_path[1]) <= max(min_path[1])):
                    min_path = curr_path.copy()
                visited.remove(end)
            for vx in neighbors(node):  
                if (vx not in visited): 
                    visited.add(vx)
                    queue.append([vx, path_sum + grid[vx[0]][vx[1]], path + [grid[vx[0]][vx[1]]]])
        return min_path

    # x = get_paths(qs[0][0], qs[0][1])
    # print(x)
    for query in qs:
        res.append(max(get_paths(query[0], query[1])[1]))
    return res   

x = lowest_highest_tower([
        [1, 20, 1, 60, 1],
        [1, 30, 1, 30, 1],
    ], [
        ((0, 0), (0, 2)),
        ((0, 2), (0, 4)),
    ])
print(x)