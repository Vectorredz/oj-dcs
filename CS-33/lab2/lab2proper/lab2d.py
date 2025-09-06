from collections.abc import Sequence
from collections import defaultdict

def all_jammables(freqs_of_radios: Sequence[Sequence[int]]) -> list[tuple[int, int]]:
    n: int = len(freqs_of_radios)
    guards = defaultdict(list)
  
    bridges = []
    ap = []
    edges: list[tuple[int, int]] = []
    radio = set()
   
    valid_pairs = defaultdict(list)  
    
    for i, freq in enumerate(freqs_of_radios):
        for f in freq:
            edge: tuple[int, int] = (f, i)
            radio.add(f)
            valid_pairs[i].append(f) 
            guards[f].append(i)
            edges.append(edge)
            
    freq_id = {f: n + idx for idx, f in enumerate(list(radio)) }
    freq_idp = {n + idx: f for idx, f in enumerate(list(radio)) }
    m = len(radio)
    adj = [[] for _ in range(m + n)]
    valid_nodes = [*range(n)] + ([-1] * m )
    disc = [-1] * (n + m)
    low = [-1] * (n + m)
    time = 0
    # make edges

    for idx, (f, u) in enumerate(edges):
        adj[u].append((freq_id[f], idx))
        adj[freq_id[f]].append((u, idx))

    def dfs(i: int, parent: int, is_root: bool):
        nonlocal time
        disc[i] = time; time += 1
        low[i] = disc[i]
        
        removable = False
        children = 0
        
        for j, idx in adj[i]:
            if disc[j] == -1:
                children += 1
                
                dfs(j, idx, False)
                low[i] = min(low[i], low[j])

                if low[j] > disc[i]:
                    if valid_nodes[j] == -1:
                        if len(guards[freq_idp[j]]) > 1:
                            bridges.append(edges[idx])
                    elif valid_nodes[i] == -1:
                        if len(guards[freq_idp[i]]) > 1:
                            bridges.append(edges[idx])

                if low[j] >= disc[i]:
                    removable = True
            elif parent != idx:
                
                low[i] = min(low[i], disc[j])
            else:
                pass
        if (not is_root and removable) or (is_root and children >= 2):
            ap.append(i)
            
    for s in range(m + n):
        if disc[s] == -1:
            dfs(s, -1, True)
    return bridges
print(all_jammables([[10, 11], [10, 11], [10, 20, 21], [20, 21]]))
# print(all_jammables([[100]]))
# assert all_jammables([[100, 101], [101, 102], [102, 103], [103, 100]]) == []
# assert all_jammables([[50, 51, 52, 53, 54], [53, 54, 55, 56]]) == []
# print(all_jammables([[50, 51, 52, 53, 54], [53, 54, 55, 56]]))