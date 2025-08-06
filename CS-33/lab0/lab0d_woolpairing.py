from typing import Callable
def winnable(n: int, pillars: list[list[int]]) -> bool:
    # 1. iterate and find the wools who has same topmost
    # try bruteforce
    moves: int =  n
    steps: int = 0
    
    if (n == 1): return False # contradiction since we are assuming to have a pairwise blocks
   
    stack: list[list[int]] = [list(reversed(pillar)) for pillar in pillars]
    
    while (moves > 0 and steps < 2*n):
        reset = False
        for i in range(len(stack)):
            for j in range(len(stack)):
                if i != j and (i < len(stack) and j < len(stack)):
                    if (stack[i][-1] == stack[j][-1]):
                        stack[i].pop()                        
                        stack[j].pop()
                        moves -= 1
                        reset = True
                    if (reset == True):
                        func: Callable[[list[int]], bool] = lambda x: x != []
                        stack: list[list[int]] = list(filter(func, stack))
                        break;
                    else:
                        steps += 1
                else:
                    steps += 1
                # if (reset == True):
                #     func: Callable[[list[int]], bool] = lambda x: x != []
                #     stack: list[list[int]] = list(filter(func, stack))
                #     break;
        
    return False if (len(stack) > 0) else True

assert winnable(3, [[1,2], [3,1], [3,2]]) is True
assert winnable(2, [[1, 2], [2, 1]]) is False
assert winnable(1, [[1, 1]]) is False
assert winnable(4, [[1, 2], [1, 3], [2, 4], [4, 3]]) is False
assert winnable(3, [[1, 2], [1, 3], [1, 3]]) is False
assert winnable(2, [[1,1], [2,2]]) is False
assert winnable(2, [[1,2,1,2]]) is False
