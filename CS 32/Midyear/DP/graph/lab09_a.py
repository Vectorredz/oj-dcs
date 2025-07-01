
height: list[list[int]] = [[7,8,7,6,5],
                           [9,9,8,7,4],
                           [8,7,6,5,3],
                           [9,6,5,9,2],
                           [6,5,4,9,1]]

def visit(vertex: int, coord: tuple[int, int]):
    print(vertex, coord)

def find_downward_path(r: int, c: int, height: list[list[int]]):
    
    _row: int = r
    _col: int = c
    
    visited: set[tuple[int, int]] = set()
    stack: list[tuple[int, int]] = []
    
    def _within_bounds(row: int, col: int) -> bool:
        if 0 <= row < r and 0 <= col < c:
            return True
        return False
    
    
    def dfs(coord: tuple[int, int]):
        stack.append(coord)
        visited.add(coord) 
        # loop over the coordinate vertex
        while (stack):
            vertex: tuple[int, int] = stack.pop() # get the top element of the stack
            vx: int = vertex[0] # row 0 
            vy: int = vertex[1] # col 0 
            visit(height[vx][vy], (vx,vy))
            visited.add((vx, vy))
            for dx, dy in [(vx, vy-1), (vx+1, vy), (vx-1, vy), (vx, vy+1)]:
                if (_within_bounds(dx, dy) and height[vx][vy] >= height[dx][dy] and (dx, dy) not in visited):
                    stack.append((dx, dy))

    
    dfs((0,0)) # start at the topmost left 

    
    return True if (r-1, c-1) in visited else False

print(find_downward_path(len(height), len(height[0]), height))