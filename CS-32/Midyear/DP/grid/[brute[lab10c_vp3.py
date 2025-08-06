NORMAL = "Normal"
FRIENDLY = "Friendly"
DANGEROUS = "Dangerous"

grid: list[list[str]] =  [
  [DANGEROUS, DANGEROUS],
  [FRIENDLY, FRIENDLY],
  [NORMAL, NORMAL]
]


def poutine_path(r: int, c: int , grid: list[list[str]]):
    # dp: list[list[list[int]]] = [[[-1 for _ in range(3)] for _ in range(c + 1)] for _ in range(r + 1)]
    dp: list[list[int]] = [[-1 for _ in range(c + 1)] for _ in range(r + 1)]
    lives: int = 1
    
    for i in range(r, -1, -1):
        normal: int = 0
        friendly: int = 0
        dangerous: int = 0
        for j in range(c + 1):
            if (i == r or j == 0):
                dp[i][j] = 0
            elif (i == r-1):  
                if (lives >= 1):
                    if (grid[i][j-1] == 'Dangerous'):
                        lives -= 1  
                    else:            
                        dp[i][j] = 1
                else:
                    dp[i][j] = 0
            elif (j == 1):
                if (lives >= 1):
                    if (grid[i][j-1] == 'Dangerous'):
                        lives -= 1  
                    else:            
                        dp[i][j] = 1
                else:
                    dp[i][j] = 0
            else:
                max_sum: int = dp[i][j-1] + dp[i+1][j-1] + dp[i+1][j]
                if (grid[i][j-1] == 'Normal'):
                    dp[i][j] = max_sum
                elif (grid[i][j-1] == 'Friendly'):
                    dp[i][j] = max_sum
                    lives += 1
                else:
                    if (lives >= 0):
                        if (grid[i][j-2] == 'Normal'):
                            normal += dp[i][j-1]
                        elif (grid[i][j-2] == 'Friendly'):
                            friendly += dp[i][j-1]
                        else:
                            dangerous += dp[i][j-1]
                        if (grid[i+1][j-2] == 'Normal'):
                            normal += dp[i+1][j-1]
                        elif (grid[i+1][j-2] == 'Friendly'):
                            friendly += dp[i+1][j-1]
                        else:
                            dangerous += dp[i+1][j-1]
                        if (grid[i+1][j-1] == 'Normal'):
                            normal += dp[i+1][j]
                        elif (grid[i+1][j-1] == 'Friendly'):
                            friendly += dp[i+1][j]
                        else:
                            dangerous += dp[i+1][j]
                        lives -= 1
                        dp[i][j] = dangerous - normal + friendly + dangerous
    for k in dp:  
        print(k)
    
poutine_path(len(grid), len(grid[0]), grid)
                