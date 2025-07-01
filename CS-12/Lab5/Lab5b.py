def decompose(d: int):  
    k = 10**(len(str(d))-1)
    n1, n2, n3 = k,k,k
    currSum = sum([n1,n2,n3])
    

    # currSum = sum([n1,n2,n3])
    # print(n1, n2, n3)
    # diff = d-currSum
    # if diff % 2 == 0:
    #     n2 += diff//2
    #     n3 += diff//2
    #     currSum = sum([n1,n2,n3])
    # elif diff % 2 != 0:
    #     n1 += diff//3
    #     n2 += diff//3
    #     n3 += diff//3
    #     currSum = sum([n1,n2,n3])
    # else:
    #     return None
    # return (n1, n2, n3)

print(decompose(4000))
    

