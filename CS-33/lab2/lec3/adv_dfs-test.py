# 1. make adj list
# 2. init disc, time, and low
# 3. do dfs

def bridges_and_artic(n, edges):
    
    adj = [[] for _ in range(n)]
    for idx, edge in enumerate(edges):
        i, j = edge
        adj[i].append((j, idx))
        adj[j].append((i, idx))
    
    disc = [-1] * n
    low = [-1] * n
    time = 0
    bridges = []
    ap = []
    
    def dfs(u, parent_idx, is_root):
        nonlocal time
        # 4. init variables
        
        disc[u] = time; time += 1
        low[u] = disc[u]
        
        has_removable_child = False
        children = 0
        
        # 5. traverse the graph
        for v, idx in adj[u]:
            # tree edge
            if (disc[v] == - 1):
                children += 1
                
                dfs(v, idx, False)
                
                # 6. update the low link of the parent node
                low[u] = min(low[u], low[v])
                
                # bridges detection
                if low[v] > disc[u]:
                    bridges.append(edges[idx]) # (u, v)
                # mark ap points   
                if low[v] >= disc[u]:
                    has_removable_child = True
            # back edge       
            elif parent_idx != idx:
                low[u] = min(low[u], disc[v])
            
        # post order, get the ap points
        if (is_root and children >= 2) or (not is_root and has_removable_child):
            ap.append(u)

    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1, True)
    
    return bridges, ap
            
                
                
            

            
            
    
                    
    





edges = (
    (0, 2),
    (5, 2),
    (5, 4),
    (0, 4),
    (2, 3),
    (3, 1),
    (1, 7),
    (7, 3),
    (7, 6),
)

x = bridges_and_artic(8, edges)
print(x)