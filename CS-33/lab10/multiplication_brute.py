A = [[0 for _ in range(2)] for _ in range(2)]
A[0][0] = 1
A[0][1] = 2
A[1][0] = 3
A[1][1] = 4
B = [[0 for _ in range(2)] for _ in range(2)]
B[0][0] = 1
B[0][1] = 2
B[1][0] = 3
B[1][1] = 4

ret = [[0 for _ in range(2)] for _ in range(2)]

for i in range(2):
    for k in range(2):
        for j in range(2):
            ret[i][k] += A[i][j] * B[j][k]

print(ret)        dfs
