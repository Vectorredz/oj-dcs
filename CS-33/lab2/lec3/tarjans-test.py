# 1. make adj list
# 2. init disc, time ,low\
# 3. do dfs
def tarjans(n, edges):
    adj = [[] for _ in range(n)]
    for i, j in edges:
        adj[i].append(j)
    
    disc = [-1] * n
    low = [-1] * n
    time = 0
    stack = []
    on_stack = [False] * n
    sccs = []
    
    def dfs(u):
        # 4. init variables
        nonlocal time
        disc[u] = time; time += 1
        low[u] = disc[u]
        
        stack.append(u)
        on_stack[u] = True
        # 5. traverse the graph
        for v in adj[u]:
            #  tree edge
            if disc[v] == -1:
                dfs(v)
                low[u] = min(low[u], low[v])
            # back edge
            elif on_stack[v]:
                low[u] = min(low[u], disc[v])
        # root of the scc
        
        if low[u] == disc[u]:
            comps = []
            while True:
                node = stack.pop()
                on_stack[node] = False
                comps.append(node)
                if (u == node):
                    break
            sccs.append(comps)
        
                
    # 6. Init the dfs loop
    for i in range(n):
        if disc[i] == -1:
            dfs(i)
            
    return sccs
    


edges = (
    (0, 1),
    (1, 2),
    (2, 0),
    (1, 3),
    (3, 4),
    (4, 5),
    (5, 3),
    (6, 4),
    (6, 7),
    (7, 6),
    (6, 8),
    (8, 9),
    (9, 10),
    (10, 8),
    (10, 11),
)
sccs = tarjans(12, edges)
print("Strongly Connected Components:", sccs)