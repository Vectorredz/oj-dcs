from heapq import heappush, heappop
from collections.abc import Sequence
type Teleporter = tuple[int, int]

def max_grunts(g: Sequence[int], teleporters: Sequence[Teleporter]) -> int:
    n = len(g)

    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in teleporters:
        adj[u-1].append(v-1)

    # --- Kosaraju to compress SCCs ---
    visited = [False]*n
    order = []

    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for i in range(n):
        if not visited[i]:
            dfs1(i)

    rev_adj = [[] for _ in range(n)]
    for u, v in teleporters:
        rev_adj[v-1].append(u-1)

    comp = [-1]*n
    def dfs2(u, cid):
        comp[u] = cid
        for v in rev_adj[u]:
            if comp[v] == -1:
                dfs2(v, cid)

    cid = 0
    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u, cid)
            cid += 1

    # Build SCC DAG
    scc_val = [0]*cid
    for u in range(n):
        scc_val[comp[u]] += g[u]

    scc_adj = [[] for _ in range(cid)]
    for u, v in teleporters:
        cu, cv = comp[u-1], comp[v-1]
        if cu != cv:
            scc_adj[cu].append(cv)

    # --- "Dijkstra" on DAG (actually max path DP with PQ) ---
    dist = [-10**18]*cid
    pq = []

    # Start from each SCC individually
    for i in range(cid):
        dist[i] = scc_val[i]
        heappush(pq, (-dist[i], i))

    ans = 0
    while pq:
        curr_neg, u = heappop(pq)
        curr = -curr_neg
        if curr < dist[u]:
            continue
        ans = max(ans, curr)
        for v in scc_adj[u]:
            new_val = curr + scc_val[v]
            if new_val > dist[v]:
                dist[v] = new_val
                heappush(pq, (-new_val, v))

    return ans


# --- Example ---
print(max_grunts([0, 2, 3, 0], [
    (1, 2),
    (1, 3),
    (2, 4),
    (3, 4),
]))  # 3 ✅
