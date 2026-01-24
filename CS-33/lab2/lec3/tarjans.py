from heapq import heappush, heappop
from collections.abc import Sequence
from collections import defaultdict
type Teleporter = tuple[int, int]

def max_grunts(g: Sequence[int], teleporters: Sequence[Teleporter]) -> int:
    n = len(g)

    # 1. Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in teleporters:
        adj[u-1].append(v-1)

    # --- 2. init variables: order, visited ---
    visited = [False]*n
    order = []
    
    # 3. do dfs 1: store order after for

    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for i in range(n):
        if not visited[i]:
            dfs1(i)
            
    # 4. reverse the edges and do dfs2
    
    rev_adj = [[] for _ in range(n)]
    for u, v in teleporters:
        rev_adj[v-1].append(u-1)

    visited = [False]*n
    components = []

    def dfs2(u, comp):
        visited[u] = True
        comp.append(u)
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v, comp)
                
    # 5. pop the order
    for u in reversed(order):
        if not visited[u]:
            # init the comp every iter
            comp = []
            dfs2(u, comp)
            # store the comp at components
            components.append(comp)

    # Now assign component IDs with enumerate
    comp_id = [-1]*n
    for cid, comp in enumerate(components):
        for u in comp:
            comp_id[u] = cid

    # Build SCC DAG
    scc_val = defaultdict(int)
    for u in range(n):
        scc_val[comp_id[u]] += g[u]

    scc_adj = [[] for _ in range(len(components))]
    for u, v in teleporters:
        cu, cv = comp_id[u-1], comp_id[v-1]
        if cu != cv:
            scc_adj[cu].append(cv)
    
    print(scc_adj)

    # --- "Dijkstra" on DAG (max path DP with PQ) ---
    dist = [-10**18]*len(components)
    pq = []

    for i in range(len(components)):
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
