s: str = "abcde"
words: list[str] = ["ab", "bb", "acd", "ace"]
valid: list[str] = []
def lcs(s: str, words: list[str]):
    len_s: int = len(s)
    for t in words:
        dp: list[list[int]] = [[0] *( len(t) + 1) for _ in range(len_s + 1)]
        for i in range(len_s + 1):
            for j in range(len(t) + 1):
                di: int = i - 1
                dj: int = j - 1
                if (i == 0 or j == 0):
                    dp[i][j] = 0
                elif (di >= 0 and dj >= 0):
                    if (s[di] == t[dj]):
                        dp[i][j] = 1 + dp[i-1][j-1]
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        subseq: int = dp[-1][-1]
        for i in dp:
            print(i)
        if (subseq == len(t)):
            valid.append(t)
    return valid

print(len(lcs(s, words)))
                        
                

        
        
    