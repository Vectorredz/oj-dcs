grid: list[list[int]] = [
                        [50, 9, -1, 0, 0, 0],
                        [ 7, 4,  2,0,0,0],
                        [ 9, 6, -1, 99,1,-1],
                        [ 5, 5,  5,-1, 9, 11],
                        [ 0, 1,  1, 8, 10, 1],
                    ]
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
                #  bounds check
                if (grid[i][j-2] == -1 and grid[i+1][j-1] == -1) or (dp[i][j-1] == 0 and dp[i+1][j] == 0):
                    dp[i][j] = 0
                elif (grid[i][j-1] == -1):
                    dp[i][j] = 0
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j]) + grid[i][j-1]
            
    return -1 if dp[0][-1] == 0 else 0
    for k in dp:
        print(k)


print(poutine_path(len(grid),len(grid[0]), grid))