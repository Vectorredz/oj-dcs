# set the base case
    
def parse_grid(str_grid: str):
    rows: list[list[str]] = []
    clean = list(filter(lambda x: x != '\n', str_grid))
    for i in range(0,len(clean),4):
        if (i % 4 == 0):
            rows.append(clean[i:i+4])
    return rows

def grid_paths():
    grid: list[list[str]] = parse_grid(str_grid)
    # 1. Init the dp table
    dp: list[list[int]] = [[0 for _ in range(len(grid) + 1)] for _ in range(len(grid) + 1)]
    blocked_row: bool = False
    blocked_col: bool = False
    # 2. Set the base case for the dp
    for i in range(len(grid) + 1):
        for j in range(len(grid) + 1):
            # base case
            if (i == 0 or j == 0):
                dp[i][j] = 0
            # set the outer edge to 1 since all of them are accesible there
            elif ((i == 1 or j == 1 )):
                # if row is blocked
                if (grid[0][j-1] == '*'):
                    blocked_row = True
                elif (grid[i-1][0] == '*'):
                    blocked_col = True

                if (blocked_row):
                    dp[i][j] = 0
                if (blocked_col):
                    dp[i][j] = 0   
                
                else:
                    dp[i][j] = 1
            else:
                if (grid[i-1][j-1] == '*'):
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

    # return dp[len(grid)][len(grid)]
    # for l in grid:
    #     print(l)

    for k in dp:
        print(k)


str_grid: str = """
....
**..
...*
....
"""

print(grid_paths())