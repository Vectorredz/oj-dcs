from collections.abc import Sequence
from collections import defaultdict
from dataclasses import dataclass
from heapq import heappop, heappush
@dataclass
class Edge:
    i: int
    j: int
    cost: int

def highest_compromised(values: Sequence[int], knows: Sequence[tuple[int, int]]) -> list[int]:
    # 1. make adj list
    n = len(values)
    adj = [[] for _ in range(n)]
    rev_adj = [[] for _ in range(n)]
    visited = [False] * n
    order = [] * n
    
    for i, j in knows:
        edge = Edge(i, j, max(values[i], values[j]))
        rev_edge = Edge(j, i, max(values[i], values[j]))
        adj[i].append(edge)
        rev_adj[j].append(rev_edge)

    # 3. do dfs
    def dfs1(u):
        visited[u] = True
        for edge in adj[u]:
            if not visited[edge.j]:
                dfs1(edge.j)
        order.append(u)

    for i in range(n):
        if not visited[i]:
            dfs1(i)
        
    #  4. reverse the edges 
    visited = [False] * n
    def dfs2(u, idx, comp):
        visited[u] = True
        comp.append(u)
        comps_idx[u] = idx
        for edge in rev_adj[u]:
            if not visited[edge.j]:
                dfs2(edge.j, idx, comp)
    comps = []
    comps_idx = {}
    idx = 0
    for i in reversed(order):
        if not visited[i]:
            comp = []
            dfs2(i, idx, comp)
            idx += 1
            comps.append(comp)
    m = len(comps)
    comps_vals = [0] * m
    for u in range(n):
        comps_vals[comps_idx[u]] = max(comps_vals[comps_idx[u]], values[u])
    
    # create SCC DAG
    dag = [[] for _ in range(m)]
    for u, v in knows:
        du, dv = comps_idx[u], comps_idx[v]
        dag[du].append(dv)
    
    dp = [-1] * m
    
    for scc in range(m-1, -1, -1):
        dp[scc] = comps_vals[scc]
        for v in dag[scc]:
            dp[scc] = max(dp[v], dp[scc])
    ret = [-1] * n
    for i, comp in enumerate(comps):
        for elem in comp:
            ret[elem] = dp[i]
    return ret
highest_compromised([40, 20, 30, 30, 10], [
        (0, 1),
        (0, 3),
        (1, 2),
        (2, 3),
        (3, 1),
        (2, 4),
    ])

