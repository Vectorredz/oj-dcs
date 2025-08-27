from collections.abc import Sequence
type Pair = tuple[str, str]

def is_supereffective(info: Sequence[Pair], questions: Sequence[Pair]) -> list[bool]:
    
    types = set()
    ret = []
    
    for elem in info:
        if elem[0] not in types:
            types.add(elem[0])
        if elem[1] not in types:
            types.add(elem[1])
            
    types = sorted(types)
    
    flatten = {elem: idx for idx, elem in enumerate(types)}
    edges = []
    n = len(types)

    for elem in info:        
        u, v = flatten[elem[0]], flatten[elem[1]]
        connected_types = (u, v, 1)
        edges.append(connected_types)
                    
    def bellman_ford(src, dest):
        dist = [float('inf')] * n
        dist[src] = 0
        for _ in range(n):
            for u, v, c in edges:
                if (dist[v] > dist[u] + c):
                    dist[v] = dist[u] + c
        # print(src, dest, dist)
        
        return dist[dest]
    
                
    for ques in questions:
        if (ques[0] not in flatten or ques[1] not in flatten):
            ret.append(False)
        else:
            reachable = bellman_ford(flatten[ques[0]], flatten[ques[1]])
            ret.append(True if reachable else False)
        
    return ret        
    
    
assert is_supereffective([
        ("Fire", "Grass"),
        ("Grass", "Water"),
        ("Water", "Fire"),
    ], [
        ("Fire", "Nigga"),
    ]) == [False]
