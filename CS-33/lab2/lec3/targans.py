from heapq import heappush, heappop
from collections.abc import Sequence
type Teleporter = tuple[int, int]

def max_grunts(g: Sequence[int], teleporters: Sequence[Teleporter]) -> int:
    n = len(g)

    # --- Build adjacency list ---
    adj = [[] for _ in range(n)]
    for u, v in teleporters:
        adj[u-1].append(v-1)

    # --- Tarjan's SCC ---
    index = [None]*n
    lowlink = [None]*n
    on_stack = [False]*n
    stack = []
    comps = []
    idx = 0

    def strongconnect(u):
        nonlocal idx
        index[u] = lowlink[u] = idx
        idx += 1
        stack.append(u)
        on_stack[u] = True

        for v in adj[u]:
            if index[v] is None:
                strongconnect(v)
                lowlink[u] = min(lowlink[u], lowlink[v])
            elif on_stack[v]:
                lowlink[u] = min(lowlink[u], index[v])

        # root of SCC
        if lowlink[u] == index[u]:
            comp = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                comp.append(w)
                if w == u:
                    break
            comps.append(comp)

    for u in range(n):
        if index[u] is None:
            strongconnect(u)
    
    print(comps)
    comp_id = [-1]*n
    for cid, comp in enumerate(comps):
        for u in comp:
            comp_id[u] = cid

    # --- Build SCC DAG ---
    k = len(comps)
    scc_val = [0]*k
    for u in range(n):
        scc_val[comp_id[u]] += g[u]

    scc_adj = [[] for _ in range(k)]
    for u, v in teleporters:
        cu, cv = comp_id[u-1], comp_id[v-1]
        if cu != cv:
            scc_adj[cu].append(cv)

    # --- Longest path using PQ (Dijkstra-like) ---
    dist = [-10**18]*k
    pq = []
    ans = 0

    for i in range(k):
        dist[i] = scc_val[i]
        heappush(pq, (-dist[i], i))

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
