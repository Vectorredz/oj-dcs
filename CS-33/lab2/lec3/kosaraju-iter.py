from typing import List, Tuple

def kosaraju(n: int, edges: List[Tuple[int, int]]) -> List[List[int]]:
    adj = [[] for _ in range(n)]
    rev_adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        rev_adj[v].append(u)

    # First DFS: finishing times (iterative with proper ordering)
    visited = [False] * n
    order = []
    
    for start in range(n):
        if visited[start]:
            continue
        
        stack = [start]
        visited[start] = True
        # Use a separate stack to track processing order
        temp_stack = []
        
        while stack:
            node = stack.pop()
            temp_stack.append(node)
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    stack.append(neighbor)
        
        # Add nodes to order in reverse of processing order
        while temp_stack:
            order.append(temp_stack.pop())

    # Second DFS: find SCCs (this part is correct)
    visited = [False] * n
    sccs = []

    for u in reversed(order):
        if visited[u]:
            continue
        comp = []
        stack = [u]
        visited[u] = True
        while stack:
            node = stack.pop()
            comp.append(node)
            for v in rev_adj[node]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)
        sccs.append(comp)

    return sccs


edges = [
    (1,0),
    (0,2),
    (2,1),
    (3,2),
    (4,3),
    (5,4),
    (6,5),
    (6,4),
    (7,4),
    (7,6)
]

x = kosaraju(8, edges)
print(x)
