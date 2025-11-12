from collections.abc import Sequence
type Grid = Sequence[Sequence[int]]
type BoolGrid = list[list[bool]]

# (cc) cs33 imple
def max_matching(n, m, adj):  # Kuhn's
    r = [-1]*n; l = [-1]*m
    def try_matching(i):
        assert not vis[i]
        vis[i] = True
        for j in adj[i]:
            if l[j] == -1 or (not vis[l[j]] and try_matching(l[j])):
                r[i] = j; l[j] = i
                return True
        return False
    mm = 0
    for s in range(n):
        vis = [False]*n
        if try_matching(s): mm += 1
    return l, r, mm
def dfs(stack, visR, visL, lmatch, rmatch, adj):
    while stack:
        u = stack.pop()
        if visL[u]: continue
        visL[u] = True
        for v in adj[u]:
            if visR[v]: continue
            visR[v] = True
            if lmatch[v] != -1 and not visL[lmatch[v]]:
                stack.append(lmatch[v])              
    return visL, visR
def largest_team(chairs: Grid) -> int | tuple[int, BoolGrid]:
    R, C = len(chairs),  len(chairs[0])
    # left and right bipartite sets
    left = {}; right = {}
    left_coords = []
    right_coords = []
    color = {}
    for i in range(R):
        for j in range(C):
            v = chairs[i][j]
            if v == -1: continue
            if (i + j) % 2 == 0: left[(i,j)] = len(left_coords); left_coords.append((i,j))
            else: right[(i,j)] = len(right_coords); right_coords.append((i,j))
            if v > 0: color.setdefault(v, []).append((i,j))
    n = len(left_coords); m = len(right_coords)
    adj = [[] for _ in range(n)]
    for idx,(i,j) in enumerate(left_coords):
        for di,dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni,nj = i+di, j+dj
            if (ni,nj) in right: adj[idx].append(right[(ni,nj)])
    for coords in color.values():
        if len(coords) != 2: continue
        a,b = coords
        if a in left and b in right:
            adj[left[a]].append(right[b])
        elif b in left and a in right:
            adj[left[b]].append(right[a])
    lmatch, rmatch, max_match = max_matching(n, m, adj)
    stack = [u for u in range(n) if rmatch[u] == -1]  # free left
    visL = [False]*n
    visR = [False]*m
    # do dfs to discover the min vertex cover
    dfs(stack, visR, visL, lmatch, rmatch, adj)
    in_vc_L = [not visL[i] for i in range(n)]
    in_vc_R = visR
    chosen = [[False]*C for _ in range(R)]
    total = 0
    def independent_set(left, right, left_coords, right_coords, in_vc_L, in_vc_R, chosen):
        nonlocal total
        for (i,j) in left_coords:
            idx = left[(i,j)]
            if not in_vc_L[idx]:
                chosen[i][j] = True; 
                total += 1
        for (i,j) in right_coords:
            idx = right[(i,j)]
            if not in_vc_R[idx]:
                chosen[i][j] = True; 
                total += 1
    independent_set(left, right, left_coords, right_coords, in_vc_L, in_vc_R, chosen)
    return total, chosen

largest_team([
    [ -1,  0, -1, -1, -1,  0],
    [ -1,  0,  0, -1, -1,  0],
    [  0,  0,  0,  0, -1,  0],
    [ -1,  0, -1, -1, -1,  0],
])

largest_team([
    [ 0,  1,  2,  5,  7,  0],
    [-1, -1, -1,  0,  0, -1],
    [ 6, -1, -1,  0, -1,  6],
    [ 3, -1, -1,  0, -1,  3],
    [-1, -1, -1,  0,  0, -1],
    [ 4,  1,  2,  5,  7,  4],
])