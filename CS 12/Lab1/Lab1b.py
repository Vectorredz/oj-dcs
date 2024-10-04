def who_gets_the_star(m: int, w: int, p: int, s: int):
    mario, wigi, pearl = abs(s-m), abs(s-w), abs(s-p)
    val = min(mario, wigi, pearl)
    if (val == mario and val == wigi) or (val == mario and val == pearl) or (val == pearl and val == wigi):
        return 'NONE'
    elif val == mario:
        return 'MARIO'
    elif val == wigi:
        return 'WIGI'
    elif val == pearl:
        return 'PEARL'
    else:
        return 'NONE'
    
print(who_gets_the_star(5, 9, 1, 7))