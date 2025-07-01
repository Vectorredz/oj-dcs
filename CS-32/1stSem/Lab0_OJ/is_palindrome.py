def is_palindrome(s: str):
    # k: list[str] = list(s)
    # for i in range(len(k)):
    #     if k[i] == ' ':
    #         k[i] = ''
    # return ''.join(k)
    i = 0
    j = len(s)-1
    count = 0
    while i < len(s)-1 and j > 1:
        if (i != j and s[i].lower() != s[j].lower()):
            count += 1
        i += 1
        j -= 1
    return count
    
print(is_palindrome("madam"))
