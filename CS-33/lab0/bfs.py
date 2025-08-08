# make a working bfs
from collections import deque
from typing import Deque
import time
grid = [ [ 1, 3, 5],
           [ 2, 4, 6]]

# make a simple working bfs

def _get_paths(grid: list[list[int]]):
    visited: list[tuple[int, int]] = []
    parents: dict[tuple[int, int], list[tuple[int, int]]] = {}
    end: tuple[int, int] = ()
    queue: Deque[tuple[int, int]] = deque()    
    
    def _within_bounds(child_dir: tuple[int ,int]):
        return True if ((0 <= child_dir[1] and child_dir[1] < len(grid[0])) and (0 <= child_dir[0] and child_dir[0] < len(grid))) else False
    
    def bfs(start: tuple[int, int], end: tuple[int, int]):
        if (start not in visited): 
            parents[start] = [None]
            queue.append(start)
            visited.append(start)
        while (queue):
            node: tuple[int, int] = queue.popleft()
            # row = y, col = x
            for dr, dc in [(0, 1), (1, 0)]:
                child_dir: tuple[int, int] = (node[0] + dc, node[1] + dr)
                
                if (_within_bounds(child_dir) and child_dir not in visited):
                    queue.append(child_dir)
                    visited.append(child_dir)
                if (_within_bounds(child_dir) and child_dir != start):
                    if (child_dir not in parents):
                        parents[child_dir] = []
                    parents[child_dir].append(node)
                
    bfs((0,0), end)
    
    paths: list[list[tuple[int, int]] | None] = []
   
    
    def dfs(src: tuple[int ,int], path: list[tuple[int, int]] ):
        # print(src)
        if (src == None):
            paths.append(path)
            return src
        else:
            # print(parents[src])
            # time.sleep(0.3)
            path.append(src)
            for parent in parents[src]:
                sub_path: list[tuple[int, int]] = path.copy()
                dfs(parent, sub_path)
            return path
    
    dfs((1,2), [])
    print(paths)
            
_get_paths(grid)        
    
                