from collections import deque
from typing import Deque
row: int = 8
col: int = 8
board: list[list[int]] = [[0 if ((i+j) % 2 == 0) else 1 for j in range(col)] for i in range(row)]
start: tuple[int, int] = (0,0)
end: tuple[int, int] = (7,7)
visited: set[tuple[int, int]] = set()
parents: dict[tuple[int, int], list[tuple[int, int] | None]] = {}
# Solving smaller problems
"""
Start the knight at [0,0]
end the knight at [2,4]

1 1 1 
1 1 1
1 1 1
1 1 1
1 1 1

"""
def knight_travails(board: list[list[int]], start: tuple[int, int], end: tuple[int, int]):
    def _within_bounds(x: int, y: int):
        return True if (0 <= x < col and 0 <= y < row) else False 

    def bfs():
        queue: Deque[tuple[int, int]] = deque()
        queue.append(start)
        visited.add(start)

        # create an empty parent array for the root
        parents[start] = [None]

        directions: list[tuple[int, int]] = [(1,2), (2,1), (-1,-2), (-2, -1), (-1, 2), (-2, 1), (1, -2), (2, -1)]

        while (queue):
            cell = queue.popleft()
            x, y = cell[0], cell[1]
            for nx, ny in directions:
                dx: int = x + nx
                dy: int = y + ny
                
                if (_within_bounds(dx, dy) and (dx, dy) not in visited):
                    visited.add((dx, dy))
                    # add the parents of that 
                    queue.append((dx, dy))
                if (_within_bounds(dx, dy) and (dx,dy) != start):
                    if ((dx, dy) not in parents.keys()):
                        parents[(dx,dy)] = []   
                    parents[(dx,dy)].append((x,y))

                # init the list of parents
        
    bfs()

    paths: list[list[tuple[int, int]]] = []

    # avoid cycles among the ancestors and parent 
    
    def dfs(root: tuple[int, int], path: list[tuple[int, int]]):
        
        # path.append(root)
        
        # if (root == start):
        #     paths.append(path.copy())
        # else:
        #     for parent in parents[root]:
        #        return dfs(parent, path)
            
        # path.remove(root)
        
     
        if (root == None):
            paths.append(path)
            return root
        
        else:
            path.append(root) # adds the current root to the sub path [(1,2), (0,0)]
            for parent in parents[root]:
                if (parent not in path):
                    dfs(parent, path.copy())
            return path


    dfs(end, [])
    print(paths)

    # print(parents[end])
    
knight_travails(board, start, end)


        

    