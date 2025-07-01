def strong_and_balanced_teams(r: list[int]):
    count: int = 0
    k = 5
    for i in range(len(r)):
        students = r[i: k + i]
        stud_idx = list(range(i, k+i))
        if is_valid(stud_idx, students, r):
            count += 1
    return count
    
def is_valid(stud_idx: list[int], students: list[int], r: list[int]): 
    pyright: list[bool] = []
    pyleft: list[bool] = []
    flag: bool = False
    sumRet: int = sum(students)
    midpoint: int = len(r) // 2
    for i in stud_idx:
        if len(r) % 2 != 0:
            if i < midpoint:
                pyleft.append(True)
                pyright.append(False)
            elif i > midpoint:
                pyleft.append(False)
                pyright.append(True)
        else:
            pyleft = [True]*(midpoint) + [False]*(midpoint)
            pyright = [False]*(midpoint) + [True]*(midpoint)

    if sumRet == 0 and (any(left for left in pyleft) and any(right for right in pyright)):
        flag = True
    else:
        flag = False
    return flag

            
assert strong_and_balanced_teams( [20, 30, -5, 2, 5, 10, 0, 5, 9, 5, -1, 0, -6, 2, 5, 2, 9, -1, 10, 10, -5, 999, 80, 1]) == 2