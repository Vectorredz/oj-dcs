"""
Assumption:
- Rows -> Person
- Cols -> Jobs
"""
from itertools import permutations

def assigment():
    person1: list[int] = [20,25,22,28]
    person2: list[int] = [15,18,23,17]
    person3: list[int] = [19,17,21,24]
    person4: list[int] = [25,23,24,24]
    
    matches: list[list[int]] = []
    matches.append(person1)
    matches.append(person2)
    matches.append(person3)
    matches.append(person4)
    
    n: int = len(matches)
    k: int = len(matches[0])
    
    x = list(set(list(permutations(sorted(list(range(n)) * n), k))))
    
    min_cost: float = float('inf')
    for perm in x:
        cost: int = 0
        for i in range(k):
            cost += matches[i][perm[i]]
        if (cost <= min_cost):
            min_cost = cost
            
    return min_cost

print(assigment())