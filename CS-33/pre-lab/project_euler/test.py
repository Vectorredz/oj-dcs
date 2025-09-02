def parse_grid(str_grid: str):
    return [list(line) for line in str_grid.strip().split("\n")]

def grid_paths():
    grid = parse_grid(str_grid)
    rows, cols = len(grid), len(grid[0])
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    
    # Base case: start cell
    if grid[0][0] != '*':
        dp[1][1] = 1

    # Fill DP
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if i == 1 and j == 1:
                continue  # start already set
            if grid[i-1][j-1] == '*':
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[rows][cols], dp  # paths count + table

str_grid = """
....
**..
...*
....
"""

count, table = grid_paths()
print("Unique paths:", count)
for row in table:
    print(row)
