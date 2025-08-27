from collections.abc import Sequence
type Corridor = tuple[tuple[int, int], int]

def infiltrate(n: int, corridors: Sequence[Corridor], r: Sequence[int], s: int, e: int) -> int | None:
    
    dist = [[float('inf')]*(n+1) for _ in range(n+1)]
    
    # setup the base case
    for i in range(n+1):
        dist[i][i] = 0
        
    # direct edges
    for edge, c in corridors:
        u, v = edge
        dist[u][v] = min(c, dist[u][v])
        dist[v][u] = min(c, dist[v][u])
        
    # teleporter edges
    for i in r: 
        for j in r:
            dist[i][j] = 0
    
    # main loop
    for k in range(n+1):
        for i in range(n+1):
            for j in range(n+1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                # dist[j][i] = min(dist[j][i], dist[j][k] + dist[k][i])
                
    # return dist[s][e] if dist[s][e] != 'inf' else None


print(infiltrate(4, [
        ((1, 2), 1),
        ((2, 3), 1),
        ((3, 4), 1),
    ], [1, 3], 1, 4))