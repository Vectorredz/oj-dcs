# find the minimum path sum  
# find the highest ever value among that path

# naive solution

Coord = tuple[int,int]
Query = tuple[Coord, Coord]

def lowest_highest_tower(grid: list[list[int]], qs: list[Query]) -> list[int]:
    # get all the paths from src to dst
    paths: list[Coord] = []
    all_paths: list[list[Coord]] = []
    
    r: int = len(grid)
    c: int = len(grid[0])
    
    visited: set[Coord] = set()
    
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
    
    def get_paths(src: Coord, end: Coord):
        paths.append(grid[src[0]][src[1]])
        visited.add(src)
        
        if (src == end):
            all_paths.append(paths.copy())

        else:
            for vertex in neighbors(src):
                if (vertex not in visited):
                    get_paths(vertex, end)
        paths.pop()
        visited.remove(src)

    res: list[int] = []
    for query in qs:
        s, e = query[0], query[1]
        all_paths: list[list[Coord]] = []
        get_paths(s, e)
        # res.append(max(min(all_paths)))
        # get the sum of all the paths 
        # get the minimum sum and filter that 
        min_path_sum: int = min(list(map(lambda x: sum(x), all_paths)))
        res.append(max(min(list(filter(lambda x: sum(x) == min_path_sum, all_paths)))))
    return res
    

lowest_highest_tower([
        [1, 20, 1, 60, 1],
        [1, 30, 1, 30, 1],
    ], [
        ((0, 0), (0, 2)),
        ((0, 2), (0, 4)),
    ])