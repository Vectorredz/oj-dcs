from collections import defaultdict, deque
from dataclasses import dataclass

@dataclass
class Edge:
    to: int
    idx: int

def parse_ascii_graph(lines):
    H, W = len(lines), len(lines[0])
    nodes = {}
    node_ctr = 0

    # Map '+' positions to node IDs
    for r in range(H):
        for c in range(W):
            if lines[r][c] == '+':
                nodes[(r, c)] = node_ctr
                node_ctr += 1

    adj = [[] for _ in range(node_ctr)]
    edge_id = 0

    def add_edge(a, b):
        nonlocal edge_id
        adj[a].append((b, Edge(b, edge_id)))
        adj[b].append((a, Edge(a, edge_id)))
        edge_id += 1

    # Horizontal edges ("-")
    for r in range(H):
        last_plus = None
        for c in range(W):
            if lines[r][c] == '+':
                if last_plus is not None:
                    if all(ch == '-' for ch in lines[r][last_plus+1:c]):
                        add_edge(nodes[(r, last_plus)], nodes[(r, c)])
                last_plus = c

    # Vertical edges ("|")
    for c in range(W):
        last_plus = None
        for r in range(H):
            if lines[r][c] == '+':
                if last_plus is not None:
                    if all(lines[k][c] == '|' for k in range(last_plus+1, r)):
                        add_edge(nodes[(last_plus, c)], nodes[(r, c)])
                last_plus = r

    return adj

def has_eulerian(n: int, adj):
    # 1. Traverse over the n with non zero degree
    start = -1
    for i in range(n):
        if len(adj[i]) > 0:
            start = i   
            break

    visited: list[bool] = [False] * n
    
    if start == -1: return True
    
    def dfs(start, adj, visited):    
        visited[start] = True  
        
        for v, _ in adj[start]:
            if not visited[v]:
                dfs(v, adj, visited)
                
    dfs(start, adj, visited)
    odd = 0
    for i in range(n):
        if len(adj[i]) > 0 and not visited[i]:
            return False
        
    for i in range(n):
        if len(adj[i]) % 2 != 0:
            odd += 1
        
    if odd == 0:
        return True
    else:
        return False

def round_trip_possible(map_: str) -> bool:
    adj = parse_ascii_graph(map_.splitlines())
    return has_eulerian(len(adj), adj)
assert round_trip_possible("""\
...+--+
...|..|
+--+--+
|.....|
+--+--+
""") == False

assert round_trip_possible("""\
.......
+-----+
.......
""") == False