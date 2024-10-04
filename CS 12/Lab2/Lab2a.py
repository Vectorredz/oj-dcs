import math

def wire_cost(lengths: list[tuple[int, str]]) -> int:
    sum_cost: int = 0
    for l in range(len(lengths)):
        if lengths[l][1] == 'm':
            sum_cost += lengths[l][0] 
        elif lengths[l][1] == 'cm':
            sum_cost += (lengths[l][0] / 100) 
        elif lengths[l][1] == 'mm':
            sum_cost += (lengths[l][0] / 1000) 
        elif lengths[l][1] == 'dm':
            sum_cost += (lengths[l][0] / 10) 
        else: 
            sum_cost += 0
    return math.ceil(sum_cost * 2) * 50

print(wire_cost([
        (42, 'm'),
        (160, 'cm'),
        (250, 'mm'),
        (55, 'mm'),
        (90, 'mL'),
        (85, 'cm'),
        (24, 'm'),
    ]))