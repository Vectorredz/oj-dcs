adj: list[list[int]] =  [[1,2], [0], [3], [1,4], []]

n: int = len(adj)
visited: list[int] = [0] * n

def visit(vertex: int):
    print(vertex)

def dfs(adj_list: list[list[int]]):
    
    idx = 0
    
    def dfs_recurse(idx: int, adj_list: list[list[int]]):
        visited[idx] = 1
        visit(idx)
        
        for vertex in adj_list[idx]:
            if (not visited[vertex]):
                dfs_recurse(vertex, adj_list)
    
    for i in range(len(visited)):
        if (not visited[i]):
            dfs_recurse(idx, adj_list)
            
dfs(adj_list=adj)