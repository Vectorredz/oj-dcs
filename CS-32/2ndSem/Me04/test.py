# Python program to find the length of longest proper prefix
# that is also suffix by comparing each prefix with suffix

def longestPrefixSuffix(s):
    res = 0
    n = len(s)
    
    # Iterating over all possible lengths
    for length in range(1, n):
        
        # Starting index of suffix
        j = n - length # 9 - 0, 9 - 1 = 8
        
        flag = True
        
        # Comparing proper prefix with suffix of length 'len'
        for k in range(length): 
            if s[k] != s[j + k]: # 8 + 1
                flag = False
                break
        
        # If they match, update the result
        if flag:
            res = length
    
    return res

s = "ababab"
print(longestPrefixSuffix(s))
