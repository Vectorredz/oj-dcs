from collections.abc import Sequence
from collections import defaultdict, deque
from dataclasses import dataclass

@dataclass
class Edge:
    i: int
    j: int
    dna: str
    idx: int

def hierholtzer(adj: list[list[tuple[int, Edge]]], m: int, start: int):
    stack: list[int] = [start]
    edge_stack: list[Edge] = []   
    path: list[Edge] = []
    visited_edges:list[bool] = [False] * m
    
    while stack:
        v: int = stack.pop()
        while adj[v] and visited_edges[adj[v][-1][1].idx]: adj[v].pop()
        if adj[v]:
            stack.append(v)
            to, edge = adj[v].pop()
            if not visited_edges[edge.idx]:
                visited_edges[edge.idx] = True
                stack.append(to)
                edge_stack.append(edge)
        else:
            if edge_stack:
                path.append(edge_stack.pop())
    path.reverse()
    return path

def find_secret_fragment(m: Sequence[str]) -> str:
    # create nodes from the string[:n-1], string[1:]
    # for elem in m:
    assert len(m) > 0 
    k: int = len(m[0])
    n: int = len(m)
    dnas: set[str] = set() # nodes
    # 1. create nodes
    edges = []
    for dna in m:
        u, v = dna[:k-1], dna[1:]
        dnas.add(u); dnas.add(v)
        
    # 2. flatten the nodes
    flatten = {dna: idx for idx, dna in enumerate(sorted(dnas))}
    # 3. Create edges
    nodes_len: int = len(dnas)
    # to determine which is src and dest; keep track of the indeg and outdeg
    indeg = [0] * nodes_len
    outdeg = [0] * nodes_len
    adj: list[list[int]] = [[] for _ in range(nodes_len)]
    
    for dna in m:
        nu, nv = dna[:k-1], dna[1:]
        u, v = flatten[nu], flatten[nv]
        outdeg[u] += 1
        indeg[v] +=1
        edges.append((u,v, dna))
        
    for idx, (u,v, val) in enumerate(edges):
        adj[u].append((v, Edge(u,v,val,idx)))
        
    # cycle exists
    src = None
    for i in range(nodes_len):
        if outdeg[i] == indeg[i] + 1:
            src = i
            break
    if src is None:
        for i in range(nodes_len):
            # start with src
            if outdeg[i] > 0:
                src = i
                break
    if src is None: return m[0]  
        
    ret_edges = hierholtzer(adj, len(edges), src)

  
    if not ret_edges: return m[0]  
    secret_base = ret_edges[0].dna
    for ret in ret_edges[1:]:
        secret_base += ret.dna[-1]
    # print(secret_base)
    return secret_base
    

    
assert find_secret_fragment((
    "AGA", "AGA", "GAG",
)) == "AGAGA"

assert find_secret_fragment((
    "GTC", "GTA", "TCA", "CAG", "CGT", "TAG", "AGT", "AGC",
)) == "CGTAGTCAGC"

assert find_secret_fragment((
    "TTA", "ATT", "ACC", "TAC",
)) == "ATTACC"

assert find_secret_fragment((
    "AG", "GA",
))  == "AGA"

assert find_secret_fragment((
    "GA", "AG",
)) == "AGA"

assert find_secret_fragment((
    "GA",
)) == "GA"

assert find_secret_fragment((
    "GAG", "AGA", "AGA"
)) == "AGAGA"

# # Single k-mer
# assert find_secret_fragment(("A",)) == "A"
# assert find_secret_fragment(("AG",)) == "AG"
# assert find_secret_fragment(("GTC",)) == "GTC"
# assert find_secret_fragment(("AG", "GA")) == "AGA"
# assert find_secret_fragment(("GA", "AG")) == "GAG"
# assert find_secret_fragment(("AT", "TG")) == "ATG"
# print(find_secret_fragment(("ATG", "TGA", "GAT")))
# print(find_secret_fragment(("AAA", "AAA", "AAA")))
print(find_secret_fragment(("AAA", "AAA", "AAG")))
# print(find_secret_fragment(("")))




