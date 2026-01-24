# 1. Create SCC's
# 2. Condense the SCC's into DAG
# 3. Make a cycle for the SCC
"""
case a: resulting DAG is connected (multiple SCC)
- Force them to create a loop
case b: resulting DAG is disconnected (multiple SCC)
- Zero; each SCC by their own doesn't create single SCC
case c: resulting DAG is a single (Single SCC)
- n (n - 1); all pairs are valid scc
"""

from collections.abc import Sequence
from collections import defaultdict
def routes_to_add(routes: Sequence[tuple[str, str]]) -> int:
    cities: set[str] = set()
    for x,y in routes: cities.add(x); cities.add(y)
    n = len(cities)
    cities_idx = {city: idx for idx, city in enumerate(cities)}
    adj: list[list[int]] = [[] for _ in range(n)]; rev_adj: list[list[int]] = [[] for _ in range(n)]
    for x, y in routes: adj[cities_idx[x]].append(cities_idx[y]); rev_adj[cities_idx[y]].append(cities_idx[x]) 
    order: list[int] = []
    visited: list[bool] = [False] * n
    sccs: list[list[int]] = []
    def dfs1(u):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)
    for i in range(n):
        if not visited[i]:
            dfs1(i)   
    visited: list[bool] = [False] * n   
    def dfs2(u, comp):
        visited[u] = True
        comp.append(u)
        for v in rev_adj[u]:
            if not visited[v]:
                dfs2(v, comp)
    for i in reversed(order):
        if not visited[i]:
            comp: list[int] = []
            dfs2(i, comp)
            sccs.append(comp)
    dn = len(sccs)
    scc_idx = {idx: comp for idx, comp in enumerate(sccs)}
    scc_map = defaultdict(int)
    visited: list[bool] = [False] * dn
    for i in range(dn):
        comp = scc_idx[i]
        for c in comp:
            scc_map[c] = i
    dag: list[list[int]] = [[] for _ in range(dn)]
    gad: list[list[int]] = [[] for _ in range(dn)]
    for x, y in routes:
        dx = scc_map[cities_idx[x]]
        dy = scc_map[cities_idx[y]]
        if dx != dy:
            dag[dx].append(dy)
            gad[dy].append(dx)    
        dag[dx] = list(set(dag[dx]))
        gad[dy] = list(set(gad[dy]))
    indeg, outdeg  = [0] * dn, [0] * dn
    ends = []
    for u in range(dn):
        for v in dag[u]:
            indeg[v] += 1
        for v in gad[u]:
            outdeg[v] += 1
    def make_cycle(u):
        visited[u] = True
        if not dag[u]:
            ends.append(u)
        for v in dag[u]:
            if not visited[v]:
                return make_cycle(v)
    for i in range(dn):
        if not visited[i]:
            make_cycle(i)      
    sources = [i for i in range(dn) if indeg[i] == 0]
    if dn == 1: return n * (n - 1) # case c
    elif len(sources) == 1 and len(ends) == 1: # case a:
        src_size = len(sccs[sources[0]])
        sink_size = len(sccs[ends[0]])
        return src_size * sink_size 
    elif len(sources) > 1 and len(ends) > 1: return 0  # case b 
    else: return 0

        
assert routes_to_add([
        ("LA", "Chicago"), 
        ("Chicago", "Paris"),
        ("Paris", "NYC"),
        ("NYC", "Chicago"),
        ("Paris", "Moscow"),
    ]) == 1

assert routes_to_add([
        ("A", "C"), 
        ("B", "C"),
        ("C", "D"),
        ("D", "E"),
        ("D", "F"),
    ]) == 0

assert routes_to_add([
        ("A", "B"), 
        ("B", "C"),
        ("C", "A"),
    ]) == 6

assert routes_to_add([
        ("A", "B"),
        ("B", "A"),
        ("C", "D"),
        ("D", "C"),
    ]) == 0