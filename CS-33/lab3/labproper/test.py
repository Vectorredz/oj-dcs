from collections.abc import Sequence
from collections import deque
from dataclasses import dataclass

@dataclass
class Edge:
    i: int
    j: int
    dna: str
    idx: int

def hierholzer(adj, m, start):
    """Stack-based Hierholzer: returns list of Edge in traversal order (length m)."""
    visited = [False] * m
    stack = [start]
    edge_stack = []   # parallel stack: edge used to get to node on `stack`
    path = []

    while stack:
        v = stack[-1]
        # skip already visited edges sitting at the end (cleanup)
        while adj[v] and visited[adj[v][-1][1].idx]:
            adj[v].pop()
        if adj[v]:
            to, edge = adj[v].pop()
            if not visited[edge.idx]:
                visited[edge.idx] = True
                stack.append(to)
                edge_stack.append(edge)
        else:
            stack.pop()
            if edge_stack:
                path.append(edge_stack.pop())

    path.reverse()
    if len(path) != m:
        raise ValueError("Hierholzer did not use all edges")
    return path

def find_secret_fragment(m: Sequence[str]) -> str:
    if not m:
        return ""
    if len(m) == 1:
        return m[0]

    k = len(m[0])
    # build nodes (k-1 mers)
    dnas = set()
    edges = []
    for dna in m:
        pref = dna[:k-1]
        suf  = dna[1:]
        dnas.add(pref); dnas.add(suf)
        edges.append((pref, suf, dna))

    # map nodes (sorted for determinism)
    flatten = {dna: idx for idx, dna in enumerate(sorted(dnas))}
    nodes_len = len(flatten)

    indeg = [0] * nodes_len
    outdeg = [0] * nodes_len
    adj = [[] for _ in range(nodes_len)]

    for idx, (pu, pv, dna) in enumerate(edges):
        u, v = flatten[pu], flatten[pv]
        outdeg[u] += 1
        indeg[v]  += 1
        adj[u].append((v, Edge(u, v, dna, idx)))

    # choose start: node with out = in + 1 if exists, else any node with out>0
    start = None
    for i in range(nodes_len):
        if outdeg[i] == indeg[i] + 1:
            start = i
            break
    if start is None:
        for i in range(nodes_len):
            if outdeg[i] > 0:
                start = i
                break

    if start is None:
        return m[0]  # no edges (shouldn't happen here)

    # optional: make deterministic pop order (so pop() returns edges in input order)
    for lst in adj:
        lst.reverse()

    # run Hierholzer
    path_edges = hierholzer(adj, len(edges), start)

    # reconstruct string: first k-mer then last char of each subsequent edge
    secret = path_edges[0].dna
    for e in path_edges[1:]:
        secret += e.dna[-1]
    return secret

# quick check for the failing testcase:
print(find_secret_fragment((
    "GTC", "GTA", "TCA", "CAG", "CGT", "TAG", "AGT", "AGC",
)))
# expected: CGTCAGTAGC
