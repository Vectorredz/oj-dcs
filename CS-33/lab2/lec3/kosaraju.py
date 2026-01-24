def kosaraju(n, edges):
    # Build adjacency lists
    adj = [[] for _ in range(n)]
    rev_adj = [[] for _ in range(n)]
    for u,v in edges:
        adj[u].append(v)
        rev_adj[v].append(u)

    # First DFS: compute finishing order
    visited = [False]*n  
    order = []
    def dfs(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs(v)
        order.append(u)  # append at finish (postorder)

    for i in range(n):
        if not visited[i]:
            dfs(i)

    # Second DFS: collect SCCs
    visited = [False]*n
    sccs = []
    def dfs_rev(u, comp):
        visited[u] = True
        comp.append(u)
        for v in rev_adj[u]:
            if not visited[v]:
                dfs_rev(v, comp)

    while order:
        u = order.pop()
        if not visited[u]:
            comp = []
            dfs_rev(u, comp)
            sccs.append(comp)

    return sccs

    
                    
edges = [(1,0),
         (0,2),
         (2,1),
         (3,2),
         (4,3),
         (5,4),
         (6,5),
         (6,4),
         (7,4),
         (7,6)]

x = kosaraju(8, edges)
print(x)