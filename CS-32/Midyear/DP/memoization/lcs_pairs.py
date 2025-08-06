s: str = "banana"
t: str = "bababanaba"

def lcs(s: str, t: str):
    # create a table
    len_s: int = len(s) + 1
    len_t: int = len(t) + 1

    dp: list[list[int]] = [[0] * (len_t) for _ in range(len_s)]
    ret: str = ""
    
    
    for i in range(len_s):
        for j in range(len_t):
            di: int = i - 1
            dj: int = j - 1
            if (i == 0 or j == 0):
                dp[i][j] = 0
            if (di >= 0 and dj >= 0):
                if (s[di] == t[dj]):
                    dp[i][j] = dp[i-1][j] + dp[i][j-1] + dp[i-1][j-1] - dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
    print(dp)
    
lcs(s, t)
                
   