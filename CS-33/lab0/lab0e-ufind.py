def lowest_highest_tower(grid, qs):
    # apply union find by rank + path compression
    queries = []
    edges = []
    r, c = len(grid), len(grid[0])
    if r == 0:
        return []
    
    parent = list(range(r * c))
    rank = [0] * (r * c)

    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]

    def union(u, v):
        u_root = find(u)
        v_root = find(v)
        if u_root == v_root:
            return
        if rank[u_root] > rank[v_root]:
            parent[v_root] = u_root
        else:
            parent[u_root] = v_root
            if rank[u_root] == rank[v_root]:
                rank[v_root] += 1

    for i in range(r):
        for j in range(c):
            # if within bounds
            if i + 1 < r:
                height = max(grid[i][j], grid[i+1][j])
                edges.append((height, i*c + j, (i+1)*c + j))
            if j + 1 < c:
                height = max(grid[i][j], grid[i][j+1])
                edges.append((height, i*c + j, i*c + (j+1)))
    edges.sort()

    for idx, ((si, sj), (ei, ej)) in enumerate(qs):
        # flatten into 1d
        queries.append((si*c + sj, ei*c + ej, idx))

    ret = [0] * len(qs)
    edge_idx = 0

    for max_height, u, v in edges:
        union(u, v)
        while edge_idx < len(queries):
            start, end, idx = queries[edge_idx]
            if find(start) == find(end):
                ret[idx] = max_height
                edge_idx += 1
            else:
                break
    return ret

lowest_highest_tower([
        [1, 20, 1, 60, 1],
        [1, 30, 1, 30, 1],
    ], [
        ((0, 0), (0, 2)),
        ((0, 2), (0, 4)),
    ])

