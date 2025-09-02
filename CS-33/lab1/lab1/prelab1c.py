

def minPathSum(matrix: list[list[int]]):
    r, c = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(c + 1)] for _ in range(c + 1)]
    
    for i in range(r + 1):
        for j in range(c + 1):
            if (i == 0 or j == 0):
                dp[i][j] = 0
            elif (i == 1):
                dp[i][j] = matrix[i-1][j-1] + dp[i][j-1]
            elif (j == 1):
                dp[i][j] = matrix[i-1][j-1] + dp[i-1][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + matrix[i-1][j-1]

    return dp[r][c]
assert minPathSum([[1,3,1],[1,5,1],[4,2,1]]) == 7