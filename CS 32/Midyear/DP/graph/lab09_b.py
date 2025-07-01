n = 5
deps = [
    (2, 1),
    (0, 1),
    (4, 2),
]

def find_task_order(n: int, d: int, dependency: list[tuple[int, int]]):
    # first pass create adjacency list out of the dependencies
    adjancency_list: dict[int, list[int]] = {i: [] for i in range(n)}
    prereq_list: dict[int, list[int]] = {i: [] for i in range(n)}
    visited: set[int] = set()
    stack: list[int] = []
    res: list[int] = []
    
    for dx, dy in dependency:
        adjancency_list[dy].append(dx)
        prereq_list[dx].append(dy)
        
    def _valid_dep(vx: int, flag: bool):
        for wx in prereq_list[vx]:
            if wx in visited:
                flag = True
            else:
                flag = False
        if prereq_list[vx] == []: 
            flag = True
        return flag
    
    
    def dfs(start: int):
        flag: bool = False
        stack.append(start)
        
        while (stack):
            vertex: int = stack.pop()
            visited.add(vertex)
            res.append(vertex)
            
            for vx in adjancency_list[vertex]:
                if (vx not in visited):
                    if (_valid_dep(vx, flag)):
                        stack.append(vx)
                        
    print(prereq_list)
    print(adjancency_list)
    for i in range(n):
        if (i not in visited and _valid_dep(i, False)):
            dfs(i)
        elif (i not in visited and i < n-1):
            dfs(i+1)
            
   
    print(res)
    
    # return res
        
print(find_task_order(n, n, dependency=deps))