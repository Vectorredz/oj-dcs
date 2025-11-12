from collections.abc import Sequence

class Combat:
    def __init__(self, n: int, vessels: Sequence[tuple[int, int]]):
        self.n = n
        self.vessels = vessels
        self.bridges = []
        self.adj = [[] for _ in range(n)]
        for i, (a, b) in enumerate(vessels):
            self.adj[a].append((b, i))
            self.adj[b].append((a, i))

        self._find_bridges()
        self.node_to_cc, self.tree = self._build_2ecc()
        self.bridge_map = {}
        for (u, v) in self.bridges:
            if u > v:
                u, v = v, u
            self.bridge_map[(u, v)] = True

        size = len(self.tree)
        self.tin = [-1] * size
        self.tout = [-1] * size
        self.parent = [-1] * size
        self.tree_comp = [-1] * size
        self.time = 0

        comp_id = 0
        for i in range(size):
            if self.tin[i] == -1:
                self._dfs_timer_iter(i, -1)
                stack = [i]
                self.tree_comp[i] = comp_id
                while stack:
                    x = stack.pop()
                    for y in self.tree[x]:
                        if self.tree_comp[y] == -1:
                            self.tree_comp[y] = comp_id
                            stack.append(y)
                comp_id += 1

    # ---------- bridge finding ----------
    def _find_bridges(self):
        n = self.n
        adj = self.adj
        disc = [-1] * n
        low = [0] * n
        bridges_idx = [False] * len(self.vessels)
        time = 0

        stack = []
        for start in range(n):
            if disc[start] != -1:
                continue
            stack.append((start, -1, 0, iter(adj[start])))
            while stack:
                u, pe, stage, it = stack[-1]
                if stage == 0:
                    disc[u] = low[u] = time
                    time += 1
                    stack[-1] = (u, pe, 1, it)
                else:
                    finished = True
                    for v, ei in it:
                        if ei == pe:
                            continue
                        if disc[v] == -1:
                            stack[-1] = (u, pe, 1, it)
                            stack.append((v, ei, 0, iter(adj[v])))
                            finished = False
                            break
                        low[u] = low[u] if low[u] < disc[v] else disc[v]
                    if finished:
                        stack.pop()
                        if pe != -1:
                            pu, pv = self.vessels[pe]
                            parent = pu if pv == u else pv
                            low[parent] = min(low[parent], low[u])
                            if low[u] > disc[parent]:
                                bridges_idx[pe] = True

        self.bridges = [self.vessels[i] for i, b in enumerate(bridges_idx) if b]

    # ---------- build 2ECC ----------
    def _build_2ecc(self):
        n = self.n
        edges = self.vessels
        adj = self.adj

        # mark bridge edges
        bridge_edge = [False] * len(edges)
        bridge_set = set()
        for u, v in self.bridges:
            bridge_set.add((u, v))
            bridge_set.add((v, u))
        for i, (u, v) in enumerate(edges):
            if (u, v) in bridge_set:
                bridge_edge[i] = True

        comp = [-1] * n
        cid = 0
        comps_nodes = []

        for start in range(n):
            if comp[start] != -1:
                continue
            stack = [start]
            comp[start] = cid
            nodes = [start]
            while stack:
                u = stack.pop()
                for v, ei in adj[u]:
                    if bridge_edge[ei]:
                        continue
                    if comp[v] == -1:
                        comp[v] = cid
                        nodes.append(v)
                        stack.append(v)
            comps_nodes.append(nodes)
            cid += 1

        size = cid
        tree = [[] for _ in range(size)]
        for u, v in self.bridges:
            cu, cv = comp[u], comp[v]
            if cu != cv:
                tree[cu].append(cv)
                tree[cv].append(cu)

        self.node_to_cc = comp
        return comp, tree

    # ---------- DFS timer (iterative) ----------
    def _dfs_timer_iter(self, root, parent):
        stack = [(root, parent, 0)]
        time = self.time
        while stack:
            u, p, stage = stack.pop()
            if stage == 0:
                self.tin[u] = time
                time += 1
                self.parent[u] = p
                stack.append((u, p, 1))
                for v in self.tree[u]:
                    if v != p and self.tin[v] == -1:
                        stack.append((v, u, 0))
            else:
                self.tout[u] = time
                time += 1
        self.time = time

    # ---------- query ----------
    def reachable(self, s: int, d: int, k: int) -> bool:
        u, v = self.vessels[k]
        a, b = self.node_to_cc[u], self.node_to_cc[v]
        cs, cd = self.node_to_cc[s], self.node_to_cc[d]

        if a > b:
            a, b = b, a
        if (u > v):
            u, v = v, u

        if (u, v) not in self.bridge_map:
            return self.tree_comp[cs] == self.tree_comp[cd]

        # ensure b is child of a
        if self.parent[b] != a:
            a, b = b, a

        if self.tree_comp[cs] != self.tree_comp[cd]:
            return False

        tin, tout = self.tin, self.tout
        ins = tin[b] <= tin[cs] and tout[cs] <= tout[b]
        ind = tin[b] <= tin[cd] and tout[cd] <= tout[b]
        return ins == ind


def test_Combat():
    combat = Combat(4, [(0, 1), (0, 2), (1, 2), (2, 3)])
    assert combat.reachable(0, 2, 1)
    assert not combat.reachable(1, 3, 3)
    assert combat.reachable(0, 0, 3)
    assert combat.reachable(1, 0, 3)

    combat2 = Combat(7, [(0, 1), (0, 2), (1, 2), (2, 3), (3, 4), (4, 5), (3, 5), (5, 6)])
    assert not combat2.reachable(0, 6, 7)
    assert not combat2.reachable(2, 6, 7)

test_Combat()
