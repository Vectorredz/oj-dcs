from collections import deque
from typing import Deque
roads = [
    [0, 1],
    [1, 0],
    [0, 2],
    [2, 3],
    [3, 1],
    [3, 4],
    [4, 1]
   
]

# 0 2 3 1 
def find_leasurely_path(n: int, r: int, roads: list[list[int]]):
    visited: set[int] = set()
    adj_list: dict[int, list[int]] = {i:[] for i in range(n)}
    curr_path: list[int] = []
    paths: list[list[int]] = []
    
    queue: Deque[int] = deque()
    
        
    # build adjacency list
    for di, dj in roads:
        adj_list[di].append(dj)   
    
    print(adj_list)
    
    # def bfs(src: int, dest: int):
    #     queue.append(src) # 0
        
    #     while (queue):
    #         # add the current vx to the path
    #         src = queue.popleft()
    #         curr_path.append(src) # 0

    #         # if the current vx reaches end add the path
    #         if (src == dest): 
    #             paths.append(curr_path.copy()) # 0
    #             curr_path.remove(src)
    
    #         else:                
    #             for vx in adj_list[src]:
    #                 queue.append(vx)
                    
            
    # bfs(0, 1)
            
        # queue.append(src)

        # while (queue):
        #     vertex: int = queue.popleft()
        #     visited.add(vertex)
                        
        #     for vx in adj_list[vertex]:
        #         if (vx not in visited):
        #             visited.add(vertex)
        #             queue.append(vx)
                    
   

    def dfs():
        def dfs_recurse(src: int, dest: int):
            # add the current vertex to the current path
            curr_path.append(src) 
            
            if (src == dest):
                paths.append(curr_path.copy()) # add the finished path to the paths
            else:
                for vx in adj_list[src]: 
                    dfs_recurse(vx, dest)
            
            curr_path.remove(src)   

        dfs_recurse(0, 1)
    dfs()        
    
    return paths
        
    # longest_path: list[int] = max(paths)

    # for vertex in longest_path:
    #     print(vertex)
    
        
    
    # return longest_path   
  

print(find_leasurely_path(5,len(roads),roads=roads))
    