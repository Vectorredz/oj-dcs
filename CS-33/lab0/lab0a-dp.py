dp: list[int | float] = [float('inf')] * (2*(10**5)+ 1)
# set base case
dp[0] = 0
for i in range(len(dp)):
    if (i <= 9 and i != 0):
        dp[i] = 1
    else:
        for j in list(map(lambda x: int(x), str(i))):
            if (j != 0):
                dn_0 = i - (j**2)
                curr = dp[dn_0] + 1 if dn_0 > 0 else 1
                if (curr <= dp[i] or not dp[i]):
                    dp[i] = curr
   
def fastest_resilience(n_0: int) -> int:
    return dp[n_0]