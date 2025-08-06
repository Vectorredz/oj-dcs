s: str = "rabbbit"
t: str = "rabbit"
valid: list[str] = []
def lcs(s: str, t: str):
    len_s: int = len(s) + 1
    len_t: int = len(t) + 1
    dp: list[list[int]] = [[0] * (len_t) for _ in range(len_s)]
    for i in range(len_s):
        for j in range(len_t):
            di: int = i - 1
            dj: int = j - 1
            # base cases
            if (i == 0):
                dp[i][j] = 0
            if (j == 0):
                dp[i][j] = 1
            elif (di >= 0 and dj >= 0):
                if (s[di] == t[dj]):
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
    
    for d in dp:
        print(d)

print(lcs(s, t))
                        
                

        
        
    