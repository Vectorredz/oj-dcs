def tarjans_scc(n, edges):
    # build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)

    disc = [-1] * n   # discovery time of each node
    low = [-1] * n    # low-link values
    stack = []
    on_stack = [False] * n
    time = 0
    sccs = []

    def dfs(u):
        nonlocal time
        disc[u] = time; time += 1
        low[u] = disc[u]
        
        stack.append(u)
        on_stack[u] = True

        for v in adj[u]:
            if disc[v] == -1:  # tree edge
                dfs(v)
                low[u] = min(low[u], low[v])
            elif on_stack[v]:  # back edge
                low[u] = min(low[u], disc[v])

        # if u is root of SCC
        if low[u] == disc[u]:
            comp = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                comp.append(w)
                if w == u:
                    break
            sccs.append(comp)

    # run DFS on all nodes
    for i in range(n):
        if disc[i] == -1:
            dfs(i)

    return sccs


# Example usage
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

sccs = tarjans_scc(12, edges)
print("Strongly Connected Components:", sccs)
