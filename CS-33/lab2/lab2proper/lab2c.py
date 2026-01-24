from dataclasses import dataclass
from collections.abc import Sequence
from collections import defaultdict
@dataclass
class Edge:
    i :int
    j :int
    
def defusing_batteries(n: int, wires: Sequence[tuple[int, int]]) -> list[int]:
    edges = [Edge(i, j) for i, j in wires]
    return bridges_and_artic_pts(n, edges)

def bridges_and_artic_pts(n, edges):
    adj = [[] for _ in range(n)]
    for idx, edge in enumerate(edges):
        adj[edge.i].append((edge.j, idx))
        adj[edge.j].append((edge.i, idx))
    disc = [-1]*n  # disc[i] = discovery time of node i during DFS
    low = [-1]*n   # low[i] = earliest discovery time among nodes reachable from i's subtree using at most one back edge
    time = 0
    bridges = []
    artic_points = []
    putolable_children = dict.fromkeys([i for i in range(n)], 0)
    def dfs(i, parent_idx, is_root):
        nonlocal time
        assert disc[i] == -1
        disc[i] = time; 
        time += 1
        low[i] = disc[i]
        children_count = 0
        for j, idx in adj[i]:
            if disc[j] == -1:
                # tree edge
                children_count += 1
                dfs(j, idx, False)
                low[i] = min(low[i], low[j])
                if low[j] > disc[i]:
                    bridges.append(edges[idx])

                if low[j] >= disc[i]:
                    putolable_children[i] += 1 # add each side
                    putolable_children[j] += 1 # add each side

            elif parent_idx != idx:
                low[i] = min(low[i], disc[j])
        # print(putolable_children)
        # note that comparison is >= 2 cuz we havent accounted the incoming edge to i yet 
        if (not is_root and putolable_children[i] >= 2) or (is_root and children_count >= 3):
            artic_points.append(i)
   
    for s in range(n):
        if disc[s] == -1:
            dfs(s, -1, True)
            
    return sorted(artic_points)

assert defusing_batteries(8, [
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4),
        (2, 5),
        (2, 6),
        (4, 7),
    ]) == [0,2]

assert defusing_batteries(5, [
        (0, 1),
        (2, 0),
        (2, 1),
        (3, 2),
        (4, 3),
        (2, 4),
    ]) == []

assert defusing_batteries(9, [ (0,1), (0,2), (1,2), (7,8), (0,7), (0,8), (0,5), (0,6), (5,6), (0,3), (0,4), (3,4) ]) == [0]