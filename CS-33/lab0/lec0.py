# 1. connected components using dfs
# If its a grid problem reduce it to a graph problem

# create dfs for graph
grid: str = """\
. . x . x
. x . . .
x . . . .
x x x x .
. . . . x""" 
def dfs(n: int, edges: list[tuple[int, int]]):

    # init adjacency list 
    adj_list: list[list[int]] = [[] for _ in range(n + 1)]
    visited: list[bool] = [False]*(n+1)
    components: list[list[int]] = []
    connected: list[int] = []
    # create edges
    for x, y in edges:
        adj_list[x].append(y)
        adj_list[y].append(x)
        
    def dfs_recurse(src: int, reachable: list[int]):
        
        if (not visited[src]):
            visited[src] = True
            reachable.append(src)
            for vertex in adj_list[src]:
                if (not visited[vertex]):
                    # reachable.append(vertex)
                    # visited[vertex] = True
                    dfs_recurse(vertex, reachable)
        return reachable
    
    for i in range(n):
        if (not visited[i]):
            components.append(dfs_recurse(i, []))
            visited[i] = True
    
    return components

def _within_bounds(coords: tuple[int, int],r:int,c:int): 
    x, y = coords[0], coords[1]
    return True if 0 <= x < r and 0 <= y < c else False

def neighbors(i: int, j: int, r: int, c: int, lines:list[list[str]]):
    directions: list[tuple[int, int]] = []
    for x, y in [(0,1), (0,-1), (-1,0), (1,0)]:
        dr: int = i + x
        dc: int = j + y
        coords: tuple[int, int] = (dr, dc)
        if (_within_bounds(coords,r,c) and lines[dr][dc] == '.'):
            directions.append(coords)
    return directions


def make_graph(grid: str):
    lines = [line.split() for line in  grid.splitlines()]
    r = len(lines)
    [c] = {*map(len, lines)}
    nodes = [ (i,j) for i in range(r) for j in range(c) if lines[i][j] == '.' ]
    node_idx = {node: i for i , node in enumerate(nodes)}  
    edges = []
    print(node_idx)
    for i, j in nodes:
        for ni, nj in neighbors(i, j, r, c, lines):
            edges.append((node_idx[i,j], node_idx[ni, nj]))
    # return len(edges), edges
    return len(nodes), edges

print(dfs(*make_graph(grid)))

