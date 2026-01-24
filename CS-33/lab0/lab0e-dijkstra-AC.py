from heapq import heapify, heappush, heappop
Coord = tuple[int, int]
Query = tuple[Coord, Coord]
def lowest_highest_tower(grid: list[list[int]], qs: list[Query]) -> list[int]:
    r, c = len(grid), len(grid[0])
    res = []
    def _within_bounds(i: int, j: int):
        return True if 0 <= i < r and 0 <= j < c else False
    def neighbors(src: Coord):
        coordinates: list[Coord] = []
        i, j = src
        for ni, nj in [(1,0), (-1,0), (0,-1), (0,1)]:
            dr = i + ni
            dc = j + nj
            if (_within_bounds(dr, dc)):
                coordinates.append((dr,dc))
        return coordinates
    def dijkstra(src: Coord, dst: Coord):
        # we heap the current (coordinates, sum_path)
        heap = []
        r,c = src
        heappush(heap, (grid[r][c], src, [grid[r][c]]))
        visited.add(src)
        paths = []
        while (heap):
            curr_sum, node, path = heappop(heap)
            visited.add(node)
            if (node == dst):
                paths.append((path, curr_sum))
                x, y = node
                visited.remove(node)
                continue
            
            for vertex in neighbors(node):
                dr, dc = vertex
                weight = curr_sum + grid[dr][dc]
                if (vertex not in visited):
                    heappush(heap, (weight, vertex, path + [grid[dr][dc]]))
        min_sum = float('inf')
        min_path = [float('inf')]
        for path in paths:
            if (path[1] <= min_sum and path[0] <= min_path):
                min_sum = path[1]
                min_path = path[0]
        return min_path
    
    for src, dst in qs:
        visited: set[Coord] = set()
        x = max(dijkstra(src, dst))
        res.append(x)
    return res

x = lowest_highest_tower([
        [1, 20, 1, 60, 1],
        [1, 30, 1, 30, 1],
    ], [
        ((0, 0), (0, 2)),
        ((0, 2), (0, 4)),
    ])
print(x)

