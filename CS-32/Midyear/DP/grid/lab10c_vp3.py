NORMAL = "Normal"
FRIENDLY = "Friendly"
DANGEROUS = "Dangerous"

from functools import reduce

grid: list[list[str]] =  [
[NORMAL, NORMAL, NORMAL, DANGEROUS, NORMAL],
[NORMAL, FRIENDLY, DANGEROUS, NORMAL, NORMAL],
[NORMAL, NORMAL, NORMAL, NORMAL, NORMAL]]

def poutine_path(r: int, c: int , grid: list[list[str]]):
    # dp: list[list[list[int]]] = [[[-1 for _ in range(3)] for _ in range(c + 1)] for _ in range(r + 1)]
    # dp: list[list[tuple[str, int]]] = [[('none', -1) for _ in range(c + 1)] for _ in range(r + 1)]
    lives: int = 1
    for i in range(r, -1, -1):
        for j in range(c + 1):
            if (i == r or j == 0):
                dp[i][j] = ('none', 0)
            elif (i == r-1):
                if (grid[i][j-1] == 'Normal'):
                    dp[i][j] = ('Normal', 1 )
                elif (grid[i][j-1] == 'Friendly'):
                    dp[i][j] = ('Friendly', 1)
                else:
                    dp[i][j] = ('Dangerous', 1 )
            elif (j == 1):
                if (grid[i][j-1] == 'Normal'):
                    dp[i][j] = ('Normal', 1)
                elif (grid[i][j-1] == 'Friendly'):
                    dp[i][j] = ('Friendly', 1)
                else:
                    dp[i][j] = ('Dangerous', 1 )
            else:
                # if current cell is 'Normal' just add all the sides
                if (grid[i][j-1] == 'Normal'):
                    dp[i][j] = ('Normal', dp[i][j-1][1] + dp[i+1][j][1] + dp[i+1][j-1][1])
                elif (grid[i][j-1] == 'Friendly'):
                    dp[i][j] = ('Friendly', dp[i][j-1][1] + dp[i+1][j][1] + dp[i+1][j-1][1])
                    lives += 1
                elif (grid[i][j-1] == 'Dangerous'):
                    max_sum: int = dp[i][j-1][1] + dp[i+1][j][1] + dp[i+1][j-1][1]
                    # extactor
                    # normal_cells = reduce(lambda x, y: x + y, )
                    # friendly_cells = reduce(lambda x, y: x + y, list(filter(lambda x: x[0] == 'Friendly', [dp[i][j-1], dp[i+1][j-1], dp[i+1][j]])))
                    # dangerous_cells = reduce(lambda x, y: x + y, list(filter(lambda x: x[0] == 'Dangerous', [dp[i][j-1], dp[i+1][j-1], dp[i+1][j]])))

                    # print(list(filter(lambda x: x[0] == 'Normal', [dp[i][j-1], dp[i+1][j-1], dp[i+1][j]])))
                    # dp[i][j] = ('Dangerous', normal_cells)
                    valid_cells: list[int] = [dp[i][j-1], dp[i+1][j-1], dp[i+1][j]]
                    for elem in valid_cells:
                        if ()
            # for k in range(3):
            #     # base cases
            #     if (i == r or j == 0):
            #         dp[i][j][k] = 0 
            #     elif (i == r-1):
            #         if (grid[i][j-1] == 'Normal' and k == lives):
            #             dp[i][j][k] = 1 + dp[i][j-1][k]
            #         # elif (grid[i][j-1] == 'Friendly' and k == lives):
            #         #     lives += 1
            #         #     dp[i][j][k] = 1 + dp[i][j-1][k]
            #     elif (j == 1):
            #         if (grid[i][j-1] == 'Normal' and k == lives):
            #             dp[i][j][k] = 1 + dp[i+1][j][k]
            #     else:
            #         # if (k == lives):
            #             if (grid[i][j-1] == 'Normal'):
            #                 dp[i][j][k] = 1 + dp[i+1][j][k] + dp[i][j-1][k]
            #             elif (grid[i][j-1] == 'Friendly'):
            #                 lives += 1
            #                 dp[i][j][k] = 1 + dp[i+1][j][k] + dp[i][j-1][k]
            #             else:
            #                 lives -= 1
            #                 dp[i][j][k] = 0
                
    for k in dp:
        print(k)
    
poutine_path(len(grid), len(grid[0]), grid)
                