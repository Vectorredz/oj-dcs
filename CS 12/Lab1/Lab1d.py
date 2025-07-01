def fifth_fury(p: list[int]):
    ret = []
    for i in range(len(p)):
        res: list[int] = []
        for j in range(len(p)):
            if i != j:
                fury = abs(p[i]-p[j])
                res.append(fury)
        ret.append(sorted(res)[-5])
    return ret
        
print(fifth_fury([20, 16, 10, 17, 6, 24, 3, 5, 8, 16, 18, 21, 20, 20, 3, 9, 7, 7, 24, 1, 3, 9]))