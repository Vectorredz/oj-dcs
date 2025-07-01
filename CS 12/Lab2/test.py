arr = [1,2,3,4,5,6]
left: list[bool] = []

left = [True]*(len(arr)//2) + [False]*(len(arr)//2)
print(left)