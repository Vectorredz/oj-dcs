def most_xp(s: int, c: int, t: int, l: int, m: int) -> int:
    # 1. init the dp table
    # the rows is always at 3
    # the cols depends on the max(s, c)
    rows: int = 3
    cols: int = max(s, c)
    dp: list[list[int]] = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
    
    # setup the items
    # a. torch: 1s x 1c -> t
    # b. ladder: 7s -> l 
    # c. meat: 3c -> m
    
    # setup the constraints
    constraints: list[tuple[int, int]] = []
    for i in range(1, cols + 1): constraints.append((i if i <= s else s, i if i <= c else c))        
    print(constraints)
    # 2. set the base case
    for i in range(rows + 1):
        for j in range(cols + 1):
            if (i == 0):
                dp[i][j] = 0
            elif (j == 0):
                dp[i][j] = 0
            # 3. memoization proper
            else: 
                # track the current sticks and coals
                col_sticks: int = constraints[j - 1][0]
                curr_sticks: int = col_sticks
                col_coals: int = constraints[j - 1][1]
                curr_coals: int = col_coals
                # curr_
                # a. torch case
                if (i == 1):
                    # note that the current sticks aand current coals are the same as the col
                    if (curr_sticks == curr_coals): # as long as there are enough sticks and coals to lend there would be a torch
                        dp[i][j] = t * min(curr_sticks, curr_coals)
                    else: # either sticks or coals are exhausted
                        dp[i][j] = max(dp[i][j-1], min(col_coals, col_sticks))
                # # b. ladder case
                elif (i == 2):
                    ladders = col_sticks // 7 # this is the current occupied 
                    curr_sticks = ladders * 7 # currently occupied sticks
                    avail_sticks = col_sticks - curr_sticks # number of unused sticks
                    if (curr_sticks >= 7):
                        dp[i][j] = max(ladders * l  + dp[i-1][col_coals - curr_sticks if col_coals - curr_sticks > 0 else 0],
                                       dp[i-1][j],
                                       dp[i][j-1])
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                else:
                    meats = col_coals // 3 # this is the current occupied 
                    curr_coals = meats * 3 # currently occupied sticks
                    avail_coals = col_coals - curr_coals # number of unused sticks
                    if (col_coals >= 3):
                        if (avail_coals >= 1 and col_coals < 7):
                            dp[i][j] = meats * m + dp[i-1][col_sticks - curr_coals if col_sticks - curr_coals > 0 else 0]
                        elif (col_coals >= 7):
                            dp[i][j] = meats * m + dp[i-1][j]
                        else: 
                            dp[i][j] = meats * m
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
             
    for row in dp:
        print(row)
    return dp[rows][cols]

# most_xp(14, 9, 1, 10, 20)
most_xp(5, 5, 3, 10, 20) 
# No sticks or coal, can't craft anything
assert most_xp(0, 0, 1, 10, 20) == 0

# Enough for 2 ladders only (14 sticks, no coal)
assert most_xp(14, 0, 5, 10, 20) == 20  # 2 ladders × 10 XP

# Best is 1 cooked meat (3 coal) + 2 torches (2 sticks + 2 coal)
assert most_xp(5, 5, 3, 10, 20) == 26  # 20 + 6

# 2 cooked meat = 6 coal → only 6 available → max 2 × 25 XP
assert most_xp(0, 6, 2, 10, 25) == 50

# Only sticks available → max ladders: 100 // 7 = 14 → 14 × 10 XP
assert most_xp(100, 0, 3, 10, 20) == 140

# Only coal available → max meats: 30 // 3 = 10 → 10 × 20 XP
assert most_xp(0, 30, 3, 10, 20) == 200

# # 7 torches (1 stick + 1 coal) = 7 × 5 XP = 35 (best combo)
# assert most_xp(7, 7, 5, 7, 10) == 35

# Best is 1 meat (3 coal) = 100 XP + 2 torches (2 stick + 2 coal) = 10 XP
assert most_xp(5, 5, 5, 100, 100) == 110
