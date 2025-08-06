str1: str = "Rabbbit"
str2: str = "Rabbit"
# str1: str = "abcdxyz"
# str2: str = "xyzabcd"

def lcs(str1: str, str2: str):
    # create a table
    len_str1: int = len(str1) + 1
    len_str2: int = len(str2) + 1

    memo: list[list[int]] = [[0] * (len_str2) for _ in range(len_str1)]
    ret: str = ""
    
    # for i in range(len_str1 - 2 ,-1 ,-1 ):
    #     for j in range(len_str2 -2, -1, -1):
    #         # diagonal
    #         if (str1[i] == str2[j]):
    #             memo[i][j] = 1 + memo[i + 1][j + 1]
    #             ret_str += str1[i]
    #         else:
    #             memo[i][j] = max(memo[i][j+1], memo[i+1][j])              
    
    # print(ret_str[::-1])
    for i in range(len_str1):
        for j in range(len_str2):
            di: int = i - 1
            dj: int = j - 1
            # set boundaries
            if (i == 0 or j == 0):
                memo[i][j] = 0
                
            if (di >= 0 and dj >= 0):
                if (str1[di] == str2[dj]):
                    memo[i][j] = 1 + memo[i-1][j-1]
                else: 
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1])
                    
    length: int = memo[-1][-1]
    curr_len: int = length
    for i in range(len_str1 - 1, -1, -1):
        for j in range(len_str2 -1, -1, -1):
            curr_len = memo[i][j]
            if (memo[i][j-1] != memo[i][j] and memo[i-1][j] != memo[i][j] and memo[i-1][j-1] != memo[i][j] and curr_len == length):
                print(i, j)
                ret += str1[memo[i][j]-1]
                length -= 1
                
    # return ret[::-1]
    for m in memo:
        print(m)
            
print(lcs(str1, str2))