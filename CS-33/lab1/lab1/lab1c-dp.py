from collections.abc import Sequence

def to_kilimanjaro(M: Sequence[Sequence[int]]) -> int:
    r, c = len(M), len(M[0])
    dp = [[0 for _ in range(c + 1)] for _ in range(r + 1)]

    # Base case 1: Set zero the outer grid
    for j in range(1, c + 1):
        for i in range(1, r + 1):
            # Base case 2: get the cummulative sum of the i == 1 (outer edges)
            if (j == 1):
                dp[i][j] = dp[i-1][j] + M[i-1][j-1]
            else: 
                dp[i][j] = dp[i][j-1] + M[i-1][j-1] 
        # Relax the columns 
        for i in range(2, r + 1):
            # if moving up is better than the current cell
            if (dp[i][j] > dp[i-1][j] + M[i-1][j-1]):
                dp[i][j] = dp[i-1][j] + M[i-1][j-1]
        for i in range(r-1, 0, -1):
            # if moving down is better than the current cell
            if (dp[i][j] > dp[i+1][j] + M[i-1][j-1]):
                dp[i][j] = dp[i+1][j] + M[i-1][j-1]

    return dp[r][c]

print(to_kilimanjaro((
    (0, 2, 1),
    (1, 100, 1),
    (10, 10, 1),
)))  # -> 3

# print(to_kilimanjaro((
#     (0, 1, 1),
#     (1, -1, 1),
#     (1, 1, 1),
# )))  # -> 2

# print(to_kilimanjaro((
#     (1, 100, 100),
#     (1, -200, 100),
#     (1, 1, 1),
# )))  # -> -196
