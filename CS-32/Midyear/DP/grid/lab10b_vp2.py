grid: list[list[int]] = [[1,  1, 1, 0],
                        [ 1, -1, 1, 1],
                        [ 1,  1, -1,1],
                        [ 0,  1, 1, 0]]
def poutine_path(r: int, c: int, grid: list[list[int]]):
    dp: list[list[int]] = [[0 for _ in range(c + 1)] for _ in range(r + 1)]
    
    for i in range(r, -1, -1):
        for j in range(c + 1):
            # base case 1
            if (i == r or j == 0):
                dp[i][j] = 0
            # base case 2
            elif (i == r-1):
                dp[i][j] = grid[i][j-1] + dp[i][j-1]
                
            elif (j == 1):
                dp[i][j] = grid[i][j-1] + dp[i+1][j]
                
            else:
                # #  bounds check
                if (grid[i][j-1] == -1):
                    dp[i][j] = -1
                else:
                    pivot = list(filter(lambda x: x != -1, [dp[i][j-1], dp[i+1][j-1], dp[i+1][j]]))
                    dp[i][j] = grid[i][j-1] + min(pivot)
    # return -1 if dp[0][-1] == 0 else 0
    for k in dp:
        print(k)


print(poutine_path(len(grid),len(grid[0]), grid))