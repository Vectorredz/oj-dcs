def sssp(n, edges, s):
    d = [float('inf')] * n
    d[s] = 0
    # loops over the graph n - 1 times
    for _ in range(n):
        detect = False
        for i, j, c in edges:
            if (d[j] > d[i] + c):
                d[j] = d[i] + c
                detect = True
        
        if not detect:
            return d
    return None 


print(sssp(7, [
            (0, 1, 3), 
            (0, 3, 99),
            (0, 2, 2),
            (1, 2, 1),
            (2, 3, 1),
            (2, 5, 2),
            (5, 3, -1000),
            (4, 3, 3),

            # add these to form a cycle
            (1, 6, 500),
            (6, 0, -600),
        ], 0))