from collections import deque
from typing import Deque
adj: list[list[int]] = [[1,2], [0,2,3], [0,1,4], [1,4], [2,3]]

def bfs(adj: list[list[int]]):
    n: int = len(adj)
    visited: list[int] = [0] * n
    q: Deque[int] = deque()
    
    visited[0] = 1
    q.append(0)   
    
    while (q):
        idx = q.popleft()
        print(idx, q)
        for vx in adj[idx]:
            if not visited[vx]:
                visited[vx] = 1
                q.append(vx)
    return 

def visit(vertex: int) -> None:
    print(vertex)
    return

print(bfs(adj=adj))