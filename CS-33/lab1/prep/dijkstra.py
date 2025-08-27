from heapq import heappop, heappush
from collections import defaultdict
# start with prim


    

# def sssp(v: int, edges: list[tuple[int, int, int]]):
#     # make adjacency list
#     def make_adj_list(v, edges):
#         adj_list = [[] for _ in range(v)]
        
#         for i, j, w in edges:
#             adj_list[i].append(((i,j), w))
#             adj_list[j].append(((j,i), w))
                    
#         return adj_list
    
#     adj_list = make_adj_list(v, edges)
    
#     # prim proper
#     heap = []
#     visited = [False]*v
#     mst = []
#     # heap = (w, u, v)
#     s = 0
#     heappush(heap, (0,(s, s)))
#     total = 0
    
#     while (len(mst) < (v - 1) and heap):
#         w, edge = heappop(heap)
#         i, j = edge
#         if (visited[j]):
#             continue
#         visited[j] = True
#         mst.append(edge)
#         for _edge, dw in adj_list[j]:
#             di, dj = _edge
#             heappush(heap, (dw, (di, dj)))
    
#     return mst, total


def sssp(v: int, edges: list[tuple[int, int, int]], s: int):
    # create adj list for directed graphs
    def make_adj_list():
        adj_list = [[] for _ in range(v)]
        
        for i,j, w in edges:
            adj_list[i].append((w, (i,j)))
            adj_list[j].append((w, (j,i)))
        return adj_list
    
    pq = [(0, (s, s), [])]
    dist = {i: (float('inf'), []) for i in range(v)}
    visited = [False] * v
    parents: list[int] = [-1] * v

    
    while (pq):
        w, edge, path = heappop(pq)
        i, j = edge
        if (visited[j]): continue
        assert not visited[j]
        
        # store the paths in a dictionary
        
        dist[j] = w, path + [j]
        print(dist)
        parents[j] = i
        
        visited[j] = True
        for dw, _edge in make_adj_list()[j]:
            heappush(pq, (dw + w, _edge, path + [j]))    

    path = []
    def dfs(src, dest):
        if (dest == src):
            path.append(dest)
            return src
        else:
            dfs(src, parents[dest])
            path.append(dest)
        return path            
                

    print(dfs(0, 5)  )  
    


print(sssp(7, [
            (0, 1, 3), 
            (0, 3, 99),
            (0, 2, 2),
            (1, 2, 1),
            (2, 3, 1),
            (2, 5, 2),
            (5, 3, 2),
            (4, 3, 3),
        ], 0))