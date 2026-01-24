def apsp(n, edges):
    # initialize the distances
    s = [[float('inf')]*n for _ in range(n)]
    
    # set the base cases
    for i in range(n):
        s[i][i] = 0

    # set 
    for i, j, c in edges:
        s[i][j] = min(c, s[i][j])
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                s[i][j] = min(s[i][j], s[i][k] + s[k][j])
    
    return s

# for row in apsp(7, [
#                 (0, 1, 3), 
#                 (0, 3, 99),
#                 (0, 2, 2),
#                 (1, 2, 1),
#                 (2, 3, 5),
#                 (2, 5, 2),
#                 (5, 3, 2),
#                 (4, 3, 3),
#             ]):
#         print(' '.join(f"{v:>5}" for v in row))

ret = apsp(7, [
                (0, 1, 3), 
                (0, 3, 99),
                (0, 2, 2),
                (1, 2, 1),
                (2, 3, 5),
                (2, 5, 2),
                (5, 3, 2),
                (4, 3, 3),
            ])

print(ret[1])