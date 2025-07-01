def where_are_the_microsnails(s: int, initial: list[tuple[tuple[int, int], str]]):
    init_x, init_y = (initial[0][0][0], initial[0][0][1])
    x, y = (init_x, init_y)
    facing: str = initial[0][1] 
    
    while s > 0:
        if facing == 'N':
            y += 1
            facing = 'W'
            s -= 1
            
        elif facing == 'W':
            x -= 1
            facing = 'S'
            s -= 1
        elif facing == 'S':
            y -= 1
            facing = 'E'
            s -= 1
        elif facing == 'E':
            x += 1
            facing = 'N'
            s -= 1
        print(x, y)
    return 

print(where_are_the_microsnails(5, [((-1,0), 'N')]))
